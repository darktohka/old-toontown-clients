# File: P (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import PandaObject
from direct.fsm import StateData
from direct.fsm import ClassicFSM
from direct.fsm import State
from ToontownMsgTypes import *
from toontown.toonbase import ToontownGlobals
from toontown.hood import TTHood
from toontown.hood import DDHood
from toontown.hood import MMHood
from toontown.hood import BRHood
from toontown.hood import DGHood
from toontown.hood import DLHood
from toontown.hood import SellbotHQ, CashbotHQ
from toontown.hood import TutorialHood
from direct.task import TaskManagerGlobal
from toontown.hood import QuietZoneState
from toontown.hood import ZoneUtil
from toontown.hood import EstateHood
from toontown.toonbase import TTLocalizer

class PlayGame(PandaObject.PandaObject, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayGame')
    notify.setDebug(1)
    Hood2ClassDict = {
        ToontownGlobals.ToontownCentral: TTHood.TTHood,
        ToontownGlobals.DonaldsDock: DDHood.DDHood,
        ToontownGlobals.TheBrrrgh: BRHood.BRHood,
        ToontownGlobals.MinniesMelodyland: MMHood.MMHood,
        ToontownGlobals.DaisyGardens: DGHood.DGHood,
        ToontownGlobals.DonaldsDreamland: DLHood.DLHood,
        ToontownGlobals.Tutorial: TutorialHood.TutorialHood,
        ToontownGlobals.MyEstate: EstateHood.EstateHood,
        ToontownGlobals.SellbotHQ: SellbotHQ.SellbotHQ,
        ToontownGlobals.CashbotHQ: CashbotHQ.CashbotHQ }
    Hood2StateDict = {
        ToontownGlobals.ToontownCentral: 'TTHood',
        ToontownGlobals.DonaldsDock: 'DDHood',
        ToontownGlobals.TheBrrrgh: 'BRHood',
        ToontownGlobals.MinniesMelodyland: 'MMHood',
        ToontownGlobals.DaisyGardens: 'DGHood',
        ToontownGlobals.DonaldsDreamland: 'DLHood',
        ToontownGlobals.Tutorial: 'TutorialHood',
        ToontownGlobals.MyEstate: 'EstateHood',
        ToontownGlobals.SellbotHQ: 'SellbotHQ',
        ToontownGlobals.CashbotHQ: 'CashbotHQ' }
    
    def __init__(self, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.place = None
        self.fsm = ClassicFSM.ClassicFSM('PlayGame', [
            State.State('start', self.enterStart, self.exitStart, [
                'quietZone']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'TTHood',
                'DDHood',
                'BRHood',
                'MMHood',
                'DGHood',
                'DLHood',
                'SellbotHQ',
                'CashbotHQ',
                'TutorialHood',
                'EstateHood']),
            State.State('TTHood', self.enterTTHood, self.exitTTHood, [
                'quietZone']),
            State.State('DDHood', self.enterDDHood, self.exitDDHood, [
                'quietZone']),
            State.State('BRHood', self.enterBRHood, self.exitBRHood, [
                'quietZone']),
            State.State('MMHood', self.enterMMHood, self.exitMMHood, [
                'quietZone']),
            State.State('DGHood', self.enterDGHood, self.exitDGHood, [
                'quietZone']),
            State.State('DLHood', self.enterDLHood, self.exitDLHood, [
                'quietZone']),
            State.State('SellbotHQ', self.enterSellbotHQ, self.exitSellbotHQ, [
                'quietZone']),
            State.State('CashbotHQ', self.enterCashbotHQ, self.exitCashbotHQ, [
                'quietZone']),
            State.State('TutorialHood', self.enterTutorialHood, self.exitTutorialHood, [
                'quietZone']),
            State.State('EstateHood', self.enterEstateHood, self.exitEstateHood, [
                'quietZone'])], 'start', 'start')
        self.fsm.enterInitialState()
        self.parentFSM = parentFSM
        self.parentFSM.getStateNamed('playGame').addChild(self.fsm)
        self.hoodDoneEvent = 'hoodDone'
        self.hood = None

    
    def enter(self, hoodId, zoneId, avId):
        if hoodId == ToontownGlobals.Tutorial:
            loaderName = 'townLoader'
            whereName = 'toonInterior'
        elif hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(avId, zoneId)
            return None
        else:
            loaderName = ZoneUtil.getLoaderName(zoneId)
            whereName = ZoneUtil.getToonWhereName(zoneId)
        self.fsm.request('quietZone', [
            {
                'loader': loaderName,
                'where': whereName,
                'how': 'teleportIn',
                'hoodId': hoodId,
                'zoneId': zoneId,
                'shardId': None,
                'avId': avId }])

    
    def exit(self):
        pass

    
    def load(self):
        pass

    
    def loadDnaStoreTutorial(self):
        self.dnaStore = DNAStorage()
        loader.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_tutorial.dna')
        loader.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')

    
    def loadDnaStore(self):
        if not hasattr(self, 'dnaStore'):
            self.dnaStore = DNAStorage()
            loader.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
            self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
            self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
            self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
            loader.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
        

    
    def unloadDnaStore(self):
        if hasattr(self, 'dnaStore'):
            self.dnaStore.resetNodes()
            self.dnaStore.resetTextures()
            del self.dnaStore
            ModelPool.garbageCollect()
            TexturePool.garbageCollect()
        

    
    def unload(self):
        self.unloadDnaStore()
        if self.hood:
            self.notify.info('Aggressively cleaning up hood: %s' % self.hood)
            self.hood.exit()
            self.hood.unload()
            self.hood = None
        

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def handleHoodDone(self):
        doneStatus = self.hood.getDoneStatus()
        shardId = doneStatus['shardId']
        if shardId != None:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
            return None
        
        how = doneStatus['how']
        if how in [
            'tunnelIn',
            'teleportIn',
            'doorIn',
            'elevatorIn']:
            self.fsm.request('quietZone', [
                doneStatus])
        else:
            self.notify.error('Exited hood with unexpected mode %s' % how)

    
    def enterQuietZone(self, requestStatus):
        self.quietZoneDoneEvent = 'quietZoneDone'
        self.acceptOnce(self.quietZoneDoneEvent, self.handleQuietZoneDone)
        self.acceptOnce('enterWaitForSetZoneResponse', self.handleWaitForSetZoneResponse)
        self.quietZoneStateData = QuietZoneState.QuietZoneState(self.quietZoneDoneEvent)
        self.quietZoneStateData.load()
        self.quietZoneStateData.enter(requestStatus)

    
    def exitQuietZone(self):
        self.ignore(self.quietZoneDoneEvent)
        self.ignore('enterWaitForSetZoneResponse')
        del self.quietZoneDoneEvent
        self.quietZoneStateData.exit()
        self.quietZoneStateData.unload()
        self.quietZoneStateData = None

    
    def handleWaitForSetZoneResponse(self, requestStatus):
        hoodId = requestStatus['hoodId']
        canonicalHoodId = ZoneUtil.getCanonicalZoneId(hoodId)
        toHoodPhrase = ToontownGlobals.hoodNameMap[canonicalHoodId][0]
        hoodName = ToontownGlobals.hoodNameMap[canonicalHoodId][-1]
        zoneId = requestStatus['zoneId']
        loaderName = requestStatus['loader']
        avId = requestStatus.get('avId', -1)
        ownerId = requestStatus.get('ownerId', avId)
        count = ToontownGlobals.hoodCountMap[canonicalHoodId]
        if loaderName == 'safeZoneLoader':
            count += ToontownGlobals.safeZoneCountMap[canonicalHoodId]
        elif loaderName == 'townLoader':
            count += ToontownGlobals.townCountMap[canonicalHoodId]
        
        if not (loader.inBulkBlock):
            if hoodId == ToontownGlobals.MyEstate:
                if avId == -1:
                    loader.beginBulkLoad('hood', TTLocalizer.HeadingToYourEstate, count, 1, TTLocalizer.TIP_ESTATE)
                else:
                    owner = base.cr.identifyAvatar(ownerId)
                    if owner == None:
                        friend = base.cr.identifyAvatar(avId)
                        if friend != None:
                            avName = friend.getName()
                            loader.beginBulkLoad('hood', TTLocalizer.HeadingToFriend % avName, count, 1, TTLocalizer.TIP_ESTATE)
                        else:
                            self.notify.warning("we can't perform this teleport")
                            return None
                    else:
                        avName = owner.getName()
                        loader.beginBulkLoad('hood', TTLocalizer.HeadingToEstate % avName, count, 1, TTLocalizer.TIP_ESTATE)
            elif ZoneUtil.isCogHQZone(zoneId):
                loader.beginBulkLoad('hood', TTLocalizer.HeadingToHood % (toHoodPhrase, hoodName), count, 1, TTLocalizer.TIP_COGHQ)
            else:
                loader.beginBulkLoad('hood', TTLocalizer.HeadingToHood % (toHoodPhrase, hoodName), count, 1, TTLocalizer.TIP_GENERAL)
        
        if hoodId == ToontownGlobals.Tutorial:
            self.loadDnaStoreTutorial()
        else:
            self.loadDnaStore()
        hoodClass = self.getHoodClassByNumber(canonicalHoodId)
        self.hood = hoodClass(self.fsm, self.hoodDoneEvent, self.dnaStore, hoodId)
        self.hood.load()
        self.hood.loadLoader(requestStatus)
        loader.endBulkLoad('hood')

    
    def handleQuietZoneDone(self):
        status = base.cr.handlerArgs
        hoodId = ZoneUtil.getCanonicalZoneId(status['hoodId'])
        hoodState = self.getHoodStateByNumber(hoodId)
        self.fsm.request(hoodState, [
            status])

    
    def enterTTHood(self, requestStatus):
        print 'enterTTHood'
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitTTHood(self):
        print 'exitTTHood'
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        base.cr.cache.flush()

    
    def enterDDHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitDDHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        base.cr.cache.flush()

    
    def enterMMHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitMMHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        base.cr.cache.flush()

    
    def enterBRHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitBRHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        base.cr.cache.flush()

    
    def enterDGHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitDGHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        base.cr.cache.flush()

    
    def enterDLHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitDLHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        base.cr.cache.flush()

    
    def enterSellbotHQ(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitSellbotHQ(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        base.cr.cache.flush()

    
    def enterCashbotHQ(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitCashbotHQ(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        base.cr.cache.flush()

    
    def enterTutorialHood(self, requestStatus):
        messenger.send('toonArrivedTutorial')
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        base.localAvatar.book.obscureButton(1)
        base.localAvatar.book.setSafeMode(1)
        base.localAvatar.laffMeter.obscure(1)
        base.localAvatar.chatMgr.obscure(1, 1)
        base.localAvatar.obscureFriendsListButton(1)
        requestStatus['how'] = 'tutorial'
        if base.config.GetString('language', 'english') == 'japanese':
            musicVolume = base.config.GetFloat('tutorial-music-volume', 0.5)
            requestStatus['musicVolume'] = musicVolume
        
        self.hood.enter(requestStatus)

    
    def exitTutorialHood(self):
        self.unloadDnaStore()
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        base.cr.cache.flush()
        base.localAvatar.book.obscureButton(0)
        base.localAvatar.book.setSafeMode(0)
        base.localAvatar.laffMeter.obscure(0)
        base.localAvatar.chatMgr.obscure(0, 0)
        base.localAvatar.obscureFriendsListButton(-1)

    
    def enterEstateHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitEstateHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        base.cr.cache.flush()

    
    def getEstateZoneAndGoHome(self, avId, zoneId):
        self.doneStatus = {
            'avId': avId,
            'zoneId': zoneId,
            'hoodId': ToontownGlobals.MyEstate,
            'loader': 'safeZoneLoader',
            'how': 'teleportIn',
            'shardId': None }
        self.acceptOnce('setLocalEstateZone', self.goHome)
        if avId > 0:
            base.cr.estateMgr.getLocalEstateZone(avId)
        else:
            base.cr.estateMgr.getLocalEstateZone(base.localAvatar.getDoId())

    
    def goHome(self, ownerId, zoneId):
        self.notify.debug('goHome ownerId = %s' % ownerId)
        if ownerId > 0 and ownerId != base.localAvatar.doId and not base.cr.isFriend(ownerId):
            self.doneStatus['failed'] = 1
            taskMgr.remove('goHomeFailed')
            taskMgr.add(self.goHomeFailed, 'goHomeFailed')
            return None
        
        if ownerId == 0 and zoneId == 0:
            self.doneStatus['failed'] = 1
            self.goHomeFailed(None)
            return None
        
        if self.doneStatus['zoneId'] != zoneId:
            self.doneStatus['where'] = 'house'
        else:
            self.doneStatus['where'] = 'estate'
        self.doneStatus['ownerId'] = ownerId
        self.fsm.request('quietZone', [
            self.doneStatus])

    
    def goHomeFailed(self, task):
        self.notify.debug('goHomeFailed')
        failedToVisitAvId = self.doneStatus.get('avId')
        if failedToVisitAvId > 0:
            message = TTLocalizer.EstateTeleportFailedNotFriends % base.cr.identifyAvatar(failedToVisitAvId).getName()
        else:
            message = TTLocalizer.EstateTeleportFailed
        self.notify.debug('goHomeFailed, why =: %s' % message)
        self.ignore('setLocalEstateZone')
        zoneId = base.localAvatar.lastHood
        loaderName = ZoneUtil.getLoaderName(zoneId)
        whereName = ZoneUtil.getToonWhereName(zoneId)
        base.localAvatar.setSystemMessage(0, message)
        self.fsm.request('quietZone', [
            {
                'loader': loaderName,
                'where': whereName,
                'how': 'teleportIn',
                'hoodId': zoneId,
                'zoneId': zoneId,
                'shardId': None }])
        return Task.done

    
    def getCatalogCodes(self, category):
        numCodes = self.dnaStore.getNumCatalogCodes(category)
        codes = []
        for i in range(numCodes):
            codes.append(self.dnaStore.getCatalogCode(category, i))
        
        return codes

    
    def getNodePathList(self, catalogGroup):
        result = []
        codes = self.getCatalogCodes(catalogGroup)
        for code in codes:
            np = self.dnaStore.findNode(code)
            result.append(np)
        
        return result

    
    def getNodePathDict(self, catalogGroup):
        result = { }
        codes = self.getCatalogCodes(catalogGroup)
        for code in codes:
            np = self.dnaStore.findNode(code)
            result[code] = np
        
        return result

    
    def getHoodClassByNumber(self, hoodNumber):
        return self.Hood2ClassDict[hoodNumber]

    
    def getHoodStateByNumber(self, hoodNumber):
        return self.Hood2StateDict[hoodNumber]

    
    def setPlace(self, place):
        self.place = place

    
    def getPlace(self):
        return self.place

    
    def getPlaceId(self):
        if self.hood:
            return self.hood.hoodId
        else:
            return None


