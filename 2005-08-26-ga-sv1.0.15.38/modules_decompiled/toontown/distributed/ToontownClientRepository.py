# File: T (Python 2.2)

import types
import time
from pandac.PandaModules import *
from pandac.DCSubatomicType import *
from direct.showbase.ShowBaseGlobal import *
from direct.distributed.ClockDelta import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import ivalMgr
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedSmoothNode
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from direct.task import Task
from direct.fsm import ClassicFSM
from direct.fsm import State
from otp.avatar import Avatar
from otp.avatar import DistributedAvatar
from otp.friends import FriendSecret
from otp.login import TTAccount
from otp.login import AccountServerConstants
from otp.login import LoginScreen
from otp.login import LoginGSAccount
from otp.login import LoginGoAccount
from otp.login import LoginWebPlayTokenAccount
from otp.login import LoginTTAccount
from otp.login import HTTPUtil
from otp.distributed import OTPClientRepository
from otp.distributed import PotentialAvatar
from otp.distributed import PotentialShard
from otp.distributed import DistributedDistrict
from otp.distributed.OtpDoGlobals import *
from toontown.toonbase.ToonBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from toontown.launcher.DownloadForceAcknowledge import *
from toontown.friends import FriendHandle
from toontown.friends import FriendsListPanel
from toontown.login import DateObject
from toontown.login import AccountServerDate
from toontown.login import AvatarChooser
from toontown.makeatoon import MakeAToon
from toontown.pets import DistributedPet, PetDetail, PetHandle
from toontown.toonbase import TTLocalizer
from toontown.toontowngui import TTDialog
from toontown.toon import LocalToon
from toontown.toon import ToonDNA
from ToontownMsgTypes import *
import HoodMgr
import PlayGame

class ToontownClientRepository(OTPClientRepository.OTPClientRepository):
    SupportTutorial = 1
    
    def __init__(self, serverVersion, launcher = None):
        OTPClientRepository.OTPClientRepository.__init__(self, serverVersion, launcher, playGame = PlayGame.PlayGame)
        if wantOtpServer:
            self.gameRootDoId = OTP_DO_ID_TOONTOWN
        
        setInterfaceFont(TTLocalizer.InterfaceFont)
        setSignFont(TTLocalizer.SignFont)
        if self.http.getVerifySsl() != HTTPClient.VSNoVerify:
            self.http.setVerifySsl(HTTPClient.VSNoDateCheck)
        
        prepareAvatar(self.http)
        self._ToontownClientRepository__forbidCheesyEffects = 0
        self.friendManager = None
        self.trophyManager = None
        self.bankManager = None
        self.catalogManager = None
        self.welcomeValleyManager = None
        self.newsManager = None
        self.distributedDistrict = None
        self.furnitureManager = None
        self.objectManager = None
        self.friendsMap = { }
        self.friendsOnline = { }
        self.friendsMapPending = 0
        self.friendsListError = 0
        self.elderFriendsMap = { }
        self.dateObject = DateObject.DateObject()
        self.accountServerDate = AccountServerDate.AccountServerDate()
        self.hoodMgr = HoodMgr.HoodMgr(self)

    
    def congratulations(self, avatarChoice):
        self.acceptedScreen = loader.loadModel('phase_3/models/gui/toon_council')
        self.acceptedScreen.setScale(0.66700000000000004)
        self.acceptedScreen.reparentTo(aspect2d)
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        self.acceptedBanner = DirectLabel(parent = self.acceptedScreen, relief = None, text = OTPLocalizer.CRNameCongratulations, text_scale = 0.17999999999999999, text_fg = Vec4(0.59999999999999998, 0.10000000000000001, 0.10000000000000001, 1), text_pos = (0, 0.050000000000000003), text_font = getMinnieFont())
        newName = avatarChoice.approvedName
        self.acceptedText = DirectLabel(parent = self.acceptedScreen, relief = None, text = OTPLocalizer.CRNameAccepted % newName, text_scale = 0.125, text_fg = Vec4(0, 0, 0, 1), text_pos = (0, -0.14999999999999999))
        self.okButton = DirectButton(parent = self.acceptedScreen, image = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')), relief = None, text = 'Ok', scale = 1.5, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0, 0, -1), command = self._ToontownClientRepository__handleCongrats, extraArgs = [
            avatarChoice])
        buttons.removeNode()

    
    def _ToontownClientRepository__handleCongrats(self, avatarChoice):
        self.acceptedBanner.destroy()
        self.acceptedText.destroy()
        self.okButton.destroy()
        self.acceptedScreen.removeNode()
        del self.acceptedScreen
        del self.okButton
        del self.acceptedText
        del self.acceptedBanner
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_WISHNAME_CLEAR)
        datagram.addUint32(avatarChoice.id)
        datagram.addUint8(1)
        self.send(datagram)
        self.loginFSM.request('waitForSetAvatarResponse', [
            avatarChoice])

    
    def betterlucknexttime(self, avList, index):
        self.rejectDoneEvent = 'rejectDone'
        self.rejectDialog = TTDialog.TTGlobalDialog(doneEvent = self.rejectDoneEvent, message = TTLocalizer.NameShopNameRejected, style = TTDialog.Acknowledge)
        self.rejectDialog.show()
        self.acceptOnce(self.rejectDoneEvent, self._ToontownClientRepository__handleReject, [
            avList,
            index])

    
    def _ToontownClientRepository__handleReject(self, avList, index):
        self.rejectDialog.cleanup()
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_WISHNAME_CLEAR)
        avid = 0
        for k in avList:
            if k.position == index:
                avid = k.id
            
        
        if avid == 0:
            self.notify.error('Avatar rejected not found in avList.  Index is: ' + str(index))
        
        datagram.addUint32(avid)
        datagram.addUint8(0)
        self.send(datagram)
        self.loginFSM.request('waitForAvatarList')

    
    def enterChooseAvatar(self, avList):
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        self.sendSetAvatarIdMsg(0)
        self.clearFriendState()
        if self.music == None and base.musicManagerIsValid:
            self.music = base.musicManager.getSound('phase_3/audio/bgm/tt_theme.mid')
            if self.music:
                self.music.setLoop(1)
                self.music.setVolume(0.90000000000000002)
                self.music.play()
            
        
        base.playMusic(self.music, looping = 1, volume = 0.90000000000000002, interrupt = None)
        self.handler = self.handleChooseAvatar
        self.avChoiceDoneEvent = 'avatarChooserDone'
        self.avChoice = AvatarChooser.AvatarChooser(avList, self.loginFSM, self.avChoiceDoneEvent)
        self.avChoice.load(self.isPaid())
        self.avChoice.enter()
        self.accept(self.avChoiceDoneEvent, self._ToontownClientRepository__handleAvatarChooserDone, [
            avList])

    
    def _ToontownClientRepository__handleAvatarChooserDone(self, avList, doneStatus):
        done = doneStatus['mode']
        if done == 'exit':
            self.loginFSM.request('shutdown')
            return None
        
        index = self.avChoice.getChoice()
        for av in avList:
            if av.position == index:
                avatarChoice = av
                self.notify.info('================')
                self.notify.info('Chose avatar id: %s' % av.id)
                self.notify.info('Chose avatar name: %s' % av.name)
                dna = ToonDNA.ToonDNA()
                dna.makeFromNetString(av.dna)
                self.notify.info('Chose avatar dna: %s' % (dna.asTuple(),))
                self.notify.info('Chose avatar position: %s' % av.position)
                self.notify.info('isPaid: %s' % self.isPaid())
                self.notify.info('freeTimeLeft: %s' % self.freeTimeLeft())
                self.notify.info('allowSecretChat: %s' % self.allowSecretChat())
                self.notify.info('================')
            
        
        if done == 'chose':
            self.avChoice.exit()
            if avatarChoice.approvedName != '':
                self.congratulations(avatarChoice)
                avatarChoice.approvedName = ''
            elif avatarChoice.rejectedName != '':
                avatarChoice.rejectedName = ''
                self.betterlucknexttime(avList, index)
            else:
                self.loginFSM.request('waitForSetAvatarResponse', [
                    avatarChoice])
        elif done == 'nameIt':
            self.goToPickAName(avList, index)
        elif done == 'create':
            self.loginFSM.request('createAvatar', [
                avList,
                index])
        elif done == 'delete':
            self.loginFSM.request('waitForDeleteAvatarResponse', [
                avatarChoice])
        

    
    def exitChooseAvatar(self):
        self.handler = None
        self.avChoice.exit()
        self.avChoice.unload()
        self.avChoice = None
        self.ignore(self.avChoiceDoneEvent)

    
    def goToPickAName(self, avList, index):
        self.avChoice.exit()
        self.loginFSM.request('createAvatar', [
            avList,
            index])

    
    def enterCreateAvatar(self, avList, index, newDNA = None):
        if self.music:
            self.music.stop()
            self.music = None
        
        if newDNA != None:
            self.newPotAv = PotentialAvatar.PotentialAvatar('deleteMe', [
                '',
                '',
                '',
                ''], newDNA.makeNetString(), index, 1)
            avList.append(self.newPotAv)
        
        base.transitions.noFade()
        self.avCreate = MakeAToon.MakeAToon(self.loginFSM, avList, 'makeAToonComplete', index, self.isPaid())
        self.avCreate.load()
        self.avCreate.enter()
        self.handler = self.handleCreateAvatar
        self.accept('makeAToonComplete', self._ToontownClientRepository__handleMakeAToon, [
            avList,
            index])
        self.accept('nameShopCreateAvatar', self.sendCreateAvatarMsg)
        self.accept('nameShopPost', self.relayMessage)

    
    def relayMessage(self, dg):
        self.send(dg)

    
    def handleCreateAvatar(self, msgType, di):
        if msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        elif msgType == CLIENT_CREATE_AVATAR_RESP and msgType == CLIENT_SET_NAME_PATTERN_ANSWER or msgType == CLIENT_SET_WISHNAME_RESP:
            self.avCreate.ns.nameShopHandler(msgType, di)
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def _ToontownClientRepository__handleMakeAToon(self, avList, avPosition):
        done = self.avCreate.getDoneStatus()
        if done == 'cancel':
            if hasattr(self, 'newPotAv'):
                if self.newPotAv in avList:
                    avList.remove(self.newPotAv)
                
            
            self.avCreate.exit()
            self.loginFSM.request('chooseAvatar', [
                avList])
        elif done == 'created':
            self.avCreate.exit()
            if not (base.launcher) or base.launcher.getPhaseComplete(3.5):
                for i in avList:
                    if i.position == avPosition:
                        newPotAv = i
                    
                
                self.loginFSM.request('waitForSetAvatarResponse', [
                    newPotAv])
            else:
                self.loginFSM.request('chooseAvatar', [
                    avList])
        else:
            self.notify.error('Invalid doneStatus from MakeAToon: ' + str(done))

    
    def exitCreateAvatar(self):
        self.ignore('makeAToonComplete')
        self.ignore('nameShopPost')
        self.ignore('nameShopCreateAvatar')
        self.avCreate.unload()
        self.avCreate = None
        self.handler = None
        if hasattr(self, 'newPotAv'):
            del self.newPotAv
        

    
    def handleAvatarResponseMsg(self, di):
        self.cleanupWaitingForDatabase()
        avatarId = di.getUint32()
        returnCode = di.getUint8()
        if returnCode == 0:
            dclass = self.dclassesByName['DistributedToon']
            NametagGlobals.setMasterArrowsOn(0)
            loader.beginBulkLoad('localAvatarPlayGame', OTPLocalizer.CREnteringToontown, 400, 1, TTLocalizer.TIP_GENERAL)
            localAvatar = LocalToon.LocalToon(self)
            localAvatar.dclass = dclass
            base.localAvatar = localAvatar
            __builtins__['localAvatar'] = base.localAvatar
            NametagGlobals.setToon(base.localAvatar)
            localAvatar.doId = avatarId
            self.localAvatarDoId = avatarId
            if wantOtpServer:
                parentId = None
                zoneId = None
                localAvatar.setLocation(parentId, zoneId)
            
            localAvatar.generate()
            localAvatar.updateAllRequiredFields(dclass, di)
            self.doId2do[avatarId] = localAvatar
            localAvatar.initInterface()
            self.sendGetFriendsListRequest()
            self.loginFSM.request('playingGame')
        else:
            self.notify.error('Bad avatar: return code %d' % returnCode)

    
    def exitPlayingGame(self):
        ivalMgr.interrupt()
        if self.objectManager != None:
            self.objectManager.destroy()
            self.objectManager = None
        
        FriendSecret.unloadFriendSecret()
        FriendsListPanel.unloadFriendsList()
        messenger.send('cancelFriendInvitation')
        if wantOtpServer:
            for (doId, obj) in self.doId2do.items():
                if not isinstance(obj, LocalToon.LocalToon) and not isinstance(obj, DistributedDistrict.DistributedDistrict):
                    self.deleteObject(doId)
                
            
        
        if hasattr(base, 'localAvatar'):
            camera.reparentTo(render)
            camera.setPos(0, 0, 0)
            camera.setHpr(0, 0, 0)
            del self.doId2do[base.localAvatar.getDoId()]
            base.localAvatar.disable()
            base.localAvatar.delete()
            NametagGlobals.setToon(base.cam)
            del base.localAvatar
            del __builtins__['localAvatar']
        
        loader.abortBulkLoad()
        inputState.delete()
        self.detectLeakedTasks([])
        self.detectLeakedEvents([
            'destroy-ToontownLoadingScreenTitle',
            'destroy-ToontownLoadingScreenTip',
            'destroy-ToontownLoadingScreenWaitBar'])
        self.detectLeakedIntervals()

    
    def reachedQuietZone(self):
        if self.trophyManager != None:
            self.trophyManager.d_requestTrophyScore()
        
        OTPClientRepository.OTPClientRepository.reachedQuietZone(self)

    
    def enterTutorialQuestion(self, hoodId, zoneId, avId):
        self.handler = self.handleTutorialQuestion
        self._ToontownClientRepository__requestTutorial(hoodId, zoneId, avId)

    
    def handleTutorialQuestion(self, msgType, di):
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            self.handleGenerateWithRequiredOther(di)
        elif msgType == CLIENT_OBJECT_UPDATE_FIELD:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_DISABLE_RESP:
            self.handleDisable(di)
        elif msgType == CLIENT_OBJECT_DELETE_RESP:
            self.handleDelete(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self.handleGetFriendsList(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self.handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self.handleFriendOffline(di)
        elif msgType == CLIENT_GET_AVATAR_DETAILS_RESP:
            self.handleGetAvatarDetailsResp(di)
        elif msgType == CLIENT_SERVER_UP:
            self.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.handleServerDown(di)
        elif msgType == CLIENT_GET_STATE_RESP:
            pass
        elif msgType == CLIENT_DONE_SET_ZONE_RESP:
            pass
        else:
            self.handleUnexpectedMsgType(msgType, di)

    
    def _ToontownClientRepository__requestTutorial(self, hoodId, zoneId, avId):
        self.notify.debug('requesting tutorial')
        self.acceptOnce('startTutorial', self._ToontownClientRepository__handleStartTutorial, [
            avId])
        messenger.send('requestTutorial')
        self.waitForDatabaseTimeout(requestName = 'RequestTutorial')

    
    def _ToontownClientRepository__handleStartTutorial(self, avId, zoneId):
        self.gameFSM.request('playGame', [
            Tutorial,
            zoneId,
            avId])

    
    def exitTutorialQuestion(self):
        self.cleanupWaitingForDatabase()
        self.handler = None
        self.handlerArgs = None
        self.ignore('startTutorial')
        taskMgr.remove('waitingForTutorial')

    
    def fillUpFriendsMap(self):
        if self.isFriendsMapComplete():
            return 1
        
        if not (self.friendsMapPending) and not (self.friendsListError):
            self.notify.warning('Friends list stale; fetching new list.')
            self.sendGetFriendsListRequest()
        
        return 0

    
    def isFriend(self, doId):
        for (friendId, flags) in base.localAvatar.friendsList:
            if friendId == doId:
                self.identifyFriend(doId)
                return 1
            
        
        return 0

    
    def getFriendFlags(self, doId):
        for (friendId, flags) in base.localAvatar.friendsList:
            if friendId == doId:
                return flags
            
        
        return 0

    
    def isFriendOnline(self, doId):
        return self.friendsOnline.has_key(doId)

    
    def addAvatarToFriendsList(self, avatar):
        self.friendsMap[avatar.doId] = avatar

    
    def identifyFriend(self, doId):
        if self.friendsMap.has_key(doId):
            return self.friendsMap[doId]
        
        avatar = None
        if self.doId2do.has_key(doId):
            avatar = self.doId2do[doId]
        elif self.cache.contains(doId):
            avatar = self.cache.dict[doId]
        else:
            self.notify.warning("Don't know who friend %d is." % doId)
            return None
        if base.wantPets:
            if avatar.isPet():
                if avatar.bFake:
                    handle = PetHandle.PetHandle(avatar)
                else:
                    handle = avatar
            else:
                handle = FriendHandle.FriendHandle(doId, avatar.getName(), avatar.style, avatar.getPetId())
        else:
            handle = FriendHandle.FriendHandle(doId, avatar.getName(), avatar.style, '')
        self.friendsMap[doId] = handle
        return handle

    
    def identifyAvatar(self, doId):
        if self.doId2do.has_key(doId):
            return self.doId2do[doId]
        else:
            return self.identifyFriend(doId)

    
    def isFriendsMapComplete(self):
        for (friendId, flags) in base.localAvatar.friendsList:
            if self.identifyFriend(friendId) == None:
                return 0
            
        
        if base.wantPets and base.localAvatar.hasPet():
            print str(self.friendsMap)
            print str(self.friendsMap.has_key(base.localAvatar.getPetId()))
            if self.friendsMap.has_key(base.localAvatar.getPetId()) == None:
                return 0
            
        
        return 1

    
    def removeFriend(self, avatarId):
        base.localAvatar.sendUpdate('friendsNotify', [
            base.localAvatar.doId,
            1], sendToId = avatarId)
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_REMOVE_FRIEND)
        datagram.addUint32(avatarId)
        self.send(datagram)
        self.estateMgr.removeFriend(base.localAvatar.doId, avatarId)
        for pair in base.localAvatar.friendsList:
            friendId = pair[0]
            if friendId == avatarId:
                base.localAvatar.friendsList.remove(pair)
                return None
            
        

    
    def clearFriendState(self):
        print 'Cleared Friend State'
        self.friendsMap = { }
        self.friendsOnline = { }
        self.friendsMapPending = 0
        self.friendsListError = 0

    
    def sendGetFriendsListRequest(self):
        self.friendsMapPending = 1
        self.friendsListError = 0
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_GET_FRIEND_LIST)
        self.send(datagram)

    
    def cleanPetsFromFriendsMap(self):
        for (objId, obj) in self.friendsMap.items():
            DistributedPet = DistributedPet
            import toontown.pets
            if isinstance(obj, DistributedPet.DistributedPet):
                print 'Removing %s reference from the friendsMap' % obj.getName()
                del self.friendsMap[objId]
            
        

    
    def removePetFromFriendsMap(self):
        doId = base.localAvatar.getPetId()
        if doId and self.friendsMap.has_key(doId):
            del self.friendsMap[doId]
        

    
    def addPetToFriendsMap(self, callback = None):
        doId = base.localAvatar.getPetId()
        if not doId or self.friendsMap.has_key(doId):
            if callback:
                callback()
            
            return None
        
        
        def petDetailsCallback(petAvatar):
            handle = PetHandle.PetHandle(petAvatar)
            self.friendsMap[doId] = handle
            petAvatar.disable()
            petAvatar.delete()
            if callback:
                callback()
            

        PetDetail.PetDetail(doId, petDetailsCallback)

    
    def handleGetFriendsList(self, di):
        error = di.getUint8()
        if error:
            self.notify.warning('Got error return from friends list.')
            self.friendsListError = 1
        else:
            count = di.getUint16()
            for i in range(0, count):
                doId = di.getUint32()
                name = di.getString()
                dnaString = di.getString()
                dna = ToonDNA.ToonDNA()
                dna.makeFromNetString(dnaString)
                petId = di.getUint32()
                handle = FriendHandle.FriendHandle(doId, name, dna, petId)
                self.friendsMap[doId] = handle
                if self.friendsOnline.has_key(doId):
                    self.friendsOnline[doId] = handle
                
            
            if base.wantPets and base.localAvatar.hasPet():
                
                def handleAddedPet():
                    self.friendsMapPending = 0
                    messenger.send('friendsMapComplete')

                self.addPetToFriendsMap(handleAddedPet)
                return None
            
        self.friendsMapPending = 0
        messenger.send('friendsMapComplete')

    
    def handleFriendOnline(self, di):
        doId = di.getUint32()
        self.notify.debug('Friend %d now online.' % doId)
        if not self.friendsOnline.has_key(doId):
            self.friendsOnline[doId] = self.identifyFriend(doId)
            messenger.send('friendOnline', [
                doId])
        

    
    def handleFriendOffline(self, di):
        doId = di.getUint32()
        self.notify.debug('Friend %d now offline.' % doId)
        
        try:
            del self.friendsOnline[doId]
            messenger.send('friendOffline', [
                doId])
        except:
            pass


    
    def getFirstBattle(self):
        DistributedBattleBase = DistributedBattleBase
        import toontown.battle
        for dobj in self.doId2do.values():
            if isinstance(dobj, DistributedBattleBase.DistributedBattleBase):
                return dobj
            
        

    
    def forbidCheesyEffects(self, forbid):
        wasAllowed = self._ToontownClientRepository__forbidCheesyEffects != 0
        if forbid:
            self._ToontownClientRepository__forbidCheesyEffects += 1
        else:
            self._ToontownClientRepository__forbidCheesyEffects -= 1
        isAllowed = self._ToontownClientRepository__forbidCheesyEffects != 0
        if wasAllowed != isAllowed:
            for av in Avatar.Avatar.ActiveAvatars:
                if hasattr(av, 'reconsiderCheesyEffect'):
                    av.reconsiderCheesyEffect()
                
            
            base.localAvatar.reconsiderCheesyEffect()
        

    
    def areCheesyEffectsAllowed(self):
        return self._ToontownClientRepository__forbidCheesyEffects == 0

    if wantOtpServer:
        
        def getStartingDistrict(self):
            answer = None
            for s in self.activeDistrictMap.values():
                if s.available:
                    if answer is None or answer.avatarCount < s.avatarCount:
                        answer = s
                    
                
            
            return answer

    

