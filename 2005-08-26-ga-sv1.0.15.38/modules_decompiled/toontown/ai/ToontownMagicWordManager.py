# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.distributed import DistributedObject
from toontown.toon import DistributedToon
from direct.directnotify import DirectNotifyGlobal
from toontown.town import TownBattleAttackPanel
from toontown.suit import RoguesGallery
from otp.avatar import Avatar
from otp.chat import ChatManager
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
import string
from toontown.toon import Toon
from direct.showbase import PythonUtil
from toontown.suit import DistributedSuitPlanner
from toontown.suit import DistributedBossCog
from otp.otpbase import OTPGlobals
from direct.distributed.ClockDelta import *
from otp.ai import MagicWordManager

class ToontownMagicWordManager(MagicWordManager.MagicWordManager):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownMagicWordManager')
    neverDisable = 1
    GameAvatarClass = DistributedToon.DistributedToon
    
    def __init__(self, cr):
        MagicWordManager.MagicWordManager.__init__(self, cr)
        self.rogues = None
        self.dbg_running_fast = 0

    
    def generate(self):
        self.accept('magicWord', self.b_setMagicWord)
        if base.config.GetBool('want-chat', 0):
            self.d_setMagicWord('~chat', base.localAvatar.doId, 0)
        
        if base.config.GetBool('want-run', 0):
            self.toggleRun()
        
        if base.config.GetBool('immortal-mode', 0):
            self.d_setMagicWord('~immortal', base.localAvatar.doId, 0)
        
        mintFloor = base.config.GetInt('mint-floor', -1)
        if mintFloor != -1:
            self.d_setMagicWord('~mintFloor %s' % mintFloor, base.localAvatar.doId, 0)
        
        mintId = base.config.GetInt('mint-id', -1)
        if mintId != -1:
            self.d_setMagicWord('~mint %s' % mintId, base.localAvatar.doId, 0)
        
        autoRestock = base.config.GetInt('auto-restock', -1)
        if autoRestock != -1:
            self.d_setMagicWord('~autoRestock %s' % autoRestock, base.localAvatar.doId, 0)
        

    
    def disable(self):
        self.ignore('magicWord')
        if self.dbg_running_fast:
            self.toggleRun()
        
        MagicWordManager.MagicWordManager.disable(self)

    
    def doMagicWord(self, word, avId, zoneId):
        
        def wordIs(w, word = word):
            if not word[:len(w) + 1] == '%s ' % w:
                pass
            return word == w

        if MagicWordManager.MagicWordManager.doMagicWord(self, word, avId, zoneId) == 1:
            pass
        1
        if word == '~endgame':
            print 'Requesting minigame abort...'
            messenger.send('minigameAbort')
        elif word == '~wingame':
            print 'Requesting minigame victory...'
            messenger.send('minigameVictory')
        elif word == '~walk':
            
            try:
                fsm = base.cr.playGame.getPlace().fsm
                fsm.forceTransition('walk')
            except:
                pass

        elif word == '~movie':
            
            try:
                fsm = base.cr.playGame.getPlace().fsm
                fsm.forceTransition('movie')
            except:
                pass

        elif word == '~sit':
            
            try:
                base.cr.playGame.getPlace().fsm.request('sit')
            except:
                pass

        elif word[:7] == '~rogues':
            suitname = None
            if len(word) > 7:
                suitname = word[7:].split(' ')[1]
            
            self.rogues = RoguesGallery.RoguesGallery(suitname)
            self.rogues.enter()
            if suitname != None:
                self.rogues.animate()
            
            self.acceptOnce('mouse1', self.exit_rogues)
        elif word == '~showPaths':
            for obj in self.cr.doId2do.values():
                if isinstance(obj, DistributedSuitPlanner.DistributedSuitPlanner):
                    obj.showPaths()
                
            
            place = base.cr.playGame.getPlace()
            if hasattr(place, 'showPaths'):
                place.showPaths()
            
        elif word == '~hidePaths':
            for obj in self.cr.doId2do.values():
                if isinstance(obj, DistributedSuitPlanner.DistributedSuitPlanner):
                    obj.hidePaths()
                
            
            place = base.cr.playGame.getPlace()
            if hasattr(place, 'hidePaths'):
                place.hidePaths()
            
        elif word == '~listen':
            base.localAvatar.garbleChat = 0
        elif word == '~nochat' and word == '~chat' or word == '~superchat':
            base.localAvatar.garbleChat = 1
        elif word == '~exec':
            ChatManager.ChatManager.execChat = 1
        elif word[:11] == '~photoshoot':
            base.cr.playGame.hood.sky.hide()
            base.cr.playGame.getPlace().loader.geom.hide()
            base.win.setClearColor(VBase4(1, 1, 1, 1))
            base.localAvatar.stopLookAroundNow()
            base.localAvatar.stopBlink()
            base.localAvatar.setNameVisible(0)
        elif word == '~hideAttack':
            TownBattleAttackPanel.hideAttackPanel(1)
        elif word == '~showAttack':
            TownBattleAttackPanel.hideAttackPanel(0)
        elif word == '~collisions_on':
            base.localAvatar.collisionsOn()
        elif word == '~collisions_off':
            base.localAvatar.collisionsOff()
        elif word == '~battle_detect_off':
            DistributedSuit = DistributedSuit
            import toontown.suit
            DistributedSuit.ALLOW_BATTLE_DETECT = 0
        elif word == '~battle_detect_on':
            DistributedSuit = DistributedSuit
            import toontown.suit
            DistributedSuit.ALLOW_BATTLE_DETECT = 1
        elif word == '~battles':
            base.localAvatar.setWantBattles(not (base.localAvatar.wantBattles))
            if base.localAvatar.wantBattles:
                response = 'battles ON'
            else:
                response = 'battles OFF'
            self.setMagicWordResponse(response)
        elif wordIs('~skipBattleMovie'):
            ToontownBattleGlobals.SkipMovie = not (ToontownBattleGlobals.SkipMovie)
            if ToontownBattleGlobals.SkipMovie:
                response = 'battle movies will be skipped'
            else:
                response = 'battle movies will be played'
            self.setMagicWordResponse(response)
        elif word == '~addCameraPosition':
            base.localAvatar.addCameraPosition()
        elif word == '~removeCameraPosition':
            base.localAvatar.removeCameraPosition()
        elif word == '~printCameraPosition':
            base.localAvatar.printCameraPosition(base.localAvatar.cameraIndex)
        elif word == '~printCameraPositions':
            base.localAvatar.printCameraPositions()
        elif word[:5] == '~sync':
            tm = base.cr.timeManager
            if tm == None:
                response = 'No TimeManager.'
                self.setMagicWordResponse(response)
            else:
                tm.extraSkew = 0.0
                skew = string.strip(word[5:])
                if skew != '':
                    tm.extraSkew = float(skew)
                
                globalClockDelta.clear()
                tm.handleHotkey()
        elif word[:7] == '~period':
            timeout = string.strip(word[7:])
            if timeout != '':
                seconds = int(timeout)
                base.cr.stopPeriodTimer()
                base.cr.resetPeriodTimer(seconds)
                base.cr.startPeriodTimer()
            
            if base.cr.periodTimerExpired:
                response = 'Period timer has expired.'
            elif base.cr.periodTimerStarted:
                elapsed = globalClock.getFrameTime() - base.cr.periodTimerStarted
                secondsRemaining = base.cr.periodTimerSecondsRemaining - elapsed
                response = 'Period timer expires in %s seconds.' % int(secondsRemaining)
            else:
                response = 'Period timer not set.'
            self.setMagicWordResponse(response)
        elif word[:3] == '~TT':
            if not direct:
                return None
            
            args = word.split()
            if len(args) > 1:
                if args[1] == 'CAM':
                    direct.cameraControl.disableMouseFly()
                    camera.wrtReparentTo(base.localAvatar)
                    base.localAvatar.startUpdateSmartCamera()
                    self.setMagicWordResponse('Disabled DIRECT camera')
                    return None
                
            
            direct.disable()
            camera.wrtReparentTo(base.localAvatar)
            base.localAvatar.startUpdateSmartCamera()
            self.setMagicWordResponse('Disabled DIRECT')
        elif word == '~net':
            if base.cr.networkPlugPulled():
                base.cr.restoreNetworkPlug()
                base.cr.startHeartbeat()
                response = 'Network restored.'
            else:
                base.cr.pullNetworkPlug()
                base.cr.stopHeartbeat()
                response = 'Network disconnected.'
            self.setMagicWordResponse(response)
        elif word == '~cogPageFull':
            base.localAvatar.suitPage.updateAllCogs(3)
        elif wordIs('~mintId'):
            args = word.split()
            postName = 'mintIdOverride'
            if len(args) < 2:
                if bboard.has(postName):
                    bboard.remove(postName)
                
            else:
                
                try:
                    id = int(args[1])
                    foo = ToontownGlobals.MintNumRooms[id]
                except:
                    pass

                bboard.post(postName, id)
        elif wordIs('~mintRoom'):
            args = word.split()
            postName = 'mintRoom'
            if len(args) < 2:
                if bboard.has(postName):
                    bboard.remove(postName)
                
            else:
                
                try:
                    id = int(args[1])
                except:
                    pass

                bboard.post(postName, id)
        elif wordIs('~mintWarp'):
            args = word.split()
            if len(args) < 2:
                self.setMagicWordResponse('Usage: ~mintWarp roomId')
                return None
            
            
            try:
                roomNum = int(args[1])
            except:
                self.setMagicWordResponse('roomId not found: %s' % args[1])
                return None

            if not bboard.has('mint'):
                self.setMagicWordResponse('not in a mint')
                return None
            
            mint = bboard.get('mint')
            if not mint.warpToRoom(roomNum):
                self.setMagicWordResponse('invalid roomId: %s' % args[1])
                return None
            
        elif wordIs('~mintLayouts'):
            MintLayout = MintLayout
            import toontown.coghq
            MintLayout.printAllCashbotInfo()
            self.setMagicWordResponse('logged mint layouts')
        elif word == '~edit':
            if not __dev__:
                self.setMagicWordResponse('client not running in dev mode')
                return None
            
            EditorGlobals = EditorGlobals
            import otp.level
            level = bboard.get(EditorGlobals.EditTargetPostName)
            if level == None:
                self.setMagicWordResponse('no level available for editing')
                return None
            
            DistributedInGameEditor = DistributedInGameEditor
            import toontown.coghq
            EditorGlobals.assertReadyToEdit()
            editUsername = EditorGlobals.getEditUsername()
            editors = base.cr.doFindAll('DistributedInGameEditor')
            for e in editors:
                if isinstance(e, DistributedInGameEditor.DistributedInGameEditor):
                    if e.getLevelDoId() == level.doId:
                        if e.editorIsLocalToon() or e.getEditUsername() == editUsername:
                            self.setMagicWordResponse("you ('%s') are already editing this level" % editUsername)
                            return None
                        
                    
                
            
            cmd = '~inGameEdit %s %s' % (level.doId, editUsername)
            self.b_setMagicWord(cmd)
        elif word == '~fshow':
            DistributedFactory = DistributedFactory
            import toontown.coghq
            factories = base.cr.doFindAll('DistributedFactory')
            factory = None
            for f in factories:
                if isinstance(f, DistributedFactory.DistributedFactory):
                    factory = f
                    break
                
            
            if factory is None:
                self.setMagicWordResponse('factory not found')
                return None
            
            factory.setColorZones(not (factory.fColorZones))
        elif wordIs('~fzone'):
            args = word.split()
            if len(args) < 2:
                self.setMagicWordResponse('Usage: ~fzone <zoneNum>')
                return None
            
            zoneId = int(args[1])
            DistributedFactory = DistributedFactory
            import toontown.coghq
            factories = base.cr.doFindAll('DistributedFactory')
            factory = None
            for f in factories:
                if isinstance(f, DistributedFactory.DistributedFactory):
                    factory = f
                    break
                
            
            if factory is None:
                self.setMagicWordResponse('factory not found')
                return None
            
            factory.warpToZone(zoneId)
        elif word == '~undead':
            
            try:
                goons = base.cr.doFindAll('Goon')
                for goon in goons:
                    goon.undead()
            except:
                self.notify.warning('Error in undead')

        elif word == '~resyncGoons':
            
            try:
                goons = base.cr.doFindAll('Goon')
                for goon in goons:
                    goon.resync()
            except:
                self.notify.warning('Error in resyncing')

        elif wordIs('~catalog'):
            self.doCatalog(word)
        elif wordIs('~petCam') and base.wantPets:
            petId = base.localAvatar.getPetId()
            pet = self.cr.doId2do.get(petId)
            if pet:
                if not hasattr(pet, 'camNode'):
                    pet.camNode = pet.attachNewNode('camNode')
                    pet.camNode.setPos(0, 0, 2.5)
                
                base.cam.reparentTo(pet.camNode)
            
        elif wordIs('~lockPet') and base.wantPets:
            petId = base.localAvatar.getPetId()
            pet = self.cr.doId2do.get(petId)
            if pet:
                if not pet.isLockedDown():
                    pet.lockPet()
                
            
        elif wordIs('~unlockPet') and base.wantPets:
            petId = base.localAvatar.getPetId()
            pet = self.cr.doId2do.get(petId)
            if pet:
                if pet.isLockedDown():
                    pet.unlockPet()
                
            
        elif wordIs('~resetPetTutorial') and base.wantPets:
            base.localAvatar.setPetTutorialDone(False)
            response = 'Pet Tutorial flag reset'
            self.setMagicWordResponse(response)
        elif wordIs('~bossBattle'):
            self.doBossBattle(word)
        

    
    def doCatalog(self, word):
        args = word.split()
        if len(args) == 1:
            return None
        elif args[1] == 'reload':
            phone = base.cr.doFind('phone')
            if phone and phone.phoneGui:
                phone.phoneGui.reload()
                response = 'Reloaded catalog screen'
            else:
                response = 'Phone is not active.'
        elif args[1] == 'dump':
            if len(args) <= 2:
                response = 'Specify output filename.'
            else:
                CatalogGenerator = CatalogGenerator
                import toontown.catalog
                cg = CatalogGenerator.CatalogGenerator()
                cg.outputSchedule(args[2])
                response = 'Catalog schedule written to file %s.' % args[2]
        else:
            return None
        self.setMagicWordResponse(response)

    
    def toggleRun(self):
        if self.dbg_running_fast:
            self.dbg_running_fast = 0
            OTPGlobals.ToonForwardSpeed = self.save_fwdspeed
            OTPGlobals.ToonReverseSpeed = self.save_revspeed
            OTPGlobals.ToonRotateSpeed = self.save_rotspeed
            base.localAvatar.setWalkSpeedNormal()
        else:
            self.dbg_running_fast = 1
            self.save_fwdspeed = OTPGlobals.ToonForwardSpeed
            self.save_revspeed = OTPGlobals.ToonReverseSpeed
            self.save_rotspeed = OTPGlobals.ToonRotateSpeed
            OTPGlobals.ToonForwardSpeed = 60
            OTPGlobals.ToonReverseSpeed = 30
            OTPGlobals.ToonRotateSpeed = 100
            base.localAvatar.setWalkSpeedNormal()

    
    def requestTeleport(self, loaderId, whereId, hoodId, zoneId, avId):
        place = base.cr.playGame.getPlace()
        if loaderId == '':
            loaderId = ZoneUtil.getBranchLoaderName(zoneId)
        
        if whereId == '':
            whereId = ZoneUtil.getToonWhereName(zoneId)
        
        if hoodId == 0:
            hoodId = place.loader.hood.id
        
        if avId == 0:
            avId = -1
        
        place.fsm.forceTransition('teleportOut', [
            {
                'loader': loaderId,
                'where': whereId,
                'how': 'teleportIn',
                'hoodId': hoodId,
                'zoneId': zoneId,
                'shardId': None,
                'avId': avId }])

    
    def exit_rogues(self):
        self.rogues.exit()
        del self.rogues
        self.rogues = None

    
    def identifyDistributedObjects(self, name):
        result = []
        lowerName = string.lower(name)
        for obj in base.cr.doId2do.values():
            className = obj.__class__.__name__
            
            try:
                name = obj.getName()
            except:
                name = className

            if string.lower(name) == lowerName and string.lower(className) == lowerName or string.lower(className) == 'distributed' + lowerName:
                result.append((name, obj))
            
        
        return result

    
    def getCSBitmask(self, str):
        words = string.lower(str).split()
        if len(words) == 0:
            return None
        
        invalid = ''
        bitmask = BitMask32.allOff()
        for w in words:
            if w == 'wall':
                bitmask |= ToontownGlobals.WallBitmask
            elif w == 'floor':
                bitmask |= ToontownGlobals.FloorBitmask
            elif w == 'cam':
                bitmask |= ToontownGlobals.CameraBitmask
            elif w == 'catch':
                bitmask |= ToontownGlobals.CatchBitmask
            elif w == 'ghost':
                bitmask |= ToontownGlobals.GhostBitmask
            elif w == 'furniture':
                bitmask |= ToontownGlobals.FurnitureSideBitmask | ToontownGlobals.FurnitureTopBitmask | ToontownGlobals.FurnitureDragBitmask
            elif w == 'furnitureside':
                bitmask |= ToontownGlobals.FurnitureSideBitmask
            elif w == 'furnituretop':
                bitmask |= ToontownGlobals.FurnitureTopBitmask
            elif w == 'furnituredrag':
                bitmask |= ToontownGlobals.FurnitureDragBitmask
            elif w == 'pie':
                bitmask |= ToontownGlobals.PieBitmask
            else:
                invalid += ' ' + w
        
        if invalid:
            self.setMagicWordResponse('Unknown CS keyword(s): %s' % invalid)
        
        return bitmask

    
    def showfont(self, fontname):
        fontname = string.strip(string.lower(fontname))
        if fontname == '' or fontname == 'interface':
            font = ToontownGlobals.getInterfaceFont()
        elif fontname == 'toon':
            font = ToontownGlobals.getToonFont()
        elif fontname == 'sign':
            font = ToontownGlobals.getSignFont()
        elif fontname == 'building':
            font = ToontownGlobals.getBuildingNametagFont()
        elif fontname == 'minnie':
            font = ToontownGlobals.getMinnieFont()
        elif fontname == 'suit':
            font = ToontownGlobals.getSuitFont()
        else:
            self.setMagicWordResponse('Unknown font: %s' % fontname)
            return None
        if not isinstance(font, DynamicTextFont):
            self.setMagicWordResponse('Font %s is not dynamic.' % fontname)
            return None
        
        self.hidefont()
        self.shownFontNode = aspect2d.attachNewNode('shownFont')
        tn = TextNode('square')
        tn.setCardActual(0.0, 1.0, -1.0, 0.0)
        tn.setFrameActual(0.0, 1.0, -1.0, 0.0)
        tn.setCardColor(1, 1, 1, 0.5)
        tn.setFrameColor(1, 1, 1, 1)
        tn.setFont(font)
        tn.setText(' ')
        numXPages = 2
        numYPages = 2
        pageScale = 0.80000000000000004
        pageMargin = 0.10000000000000001
        numPages = font.getNumPages()
        x = 0
        y = 0
        for pi in range(numPages):
            page = font.getPage(pi)
            tn.setCardTexture(page)
            np = self.shownFontNode.attachNewNode(tn.generate())
            np.setScale(pageScale)
            (np.setPos(((float(x) / numXPages) * 2 - 1) + pageMargin, 0, 1 - (float(y) / numYPages) * 2 - pageMargin),)
            x += 1
            if x >= numXPages:
                y += 1
                x = 0
            
        

    
    def doBossBattle(self, word):
        args = word.split()
        bossCog = None
        for distObj in self.cr.doId2do.values():
            if isinstance(distObj, DistributedBossCog.DistributedBossCog):
                bossCog = distObj
                break
            
        
        response = None
        if len(args) == 1:
            pass
        1
        if args[1] == 'safe':
            if len(args) <= 2:
                flag = not (bossCog.localToonIsSafe)
            else:
                flag = int(args[2])
            bossCog.localToonIsSafe = flag
            if flag:
                response = 'LocalToon is now safe from boss attacks'
            else:
                response = 'LocalToon is now vulnerable to boss attacks'
        elif args[1] == 'stun':
            bossCog.stunAllGoons()
        elif args[1] == 'destroy':
            bossCog.destroyAllGoons()
        
        if response:
            self.setMagicWordResponse(response)
        


