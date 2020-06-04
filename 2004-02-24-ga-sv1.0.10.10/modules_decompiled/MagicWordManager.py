# File: M (Python 2.2)

from ShowBaseGlobal import *
import DistributedObject
import DistributedToon
import DirectNotifyGlobal
import TownBattleAttackPanel
import RoguesGallery
import Avatar
import ChatManager
import ToontownGlobals
import string
import Toon
import PythonUtil
import DistributedSuitPlanner
from ClockDelta import *

class MagicWordManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('MagicWordManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.rogues = None
        self.dbg_running_fast = 0
        self.shownFontNode = None
        self.csShown = 0

    
    def generate(self):
        self.accept('magicWord', self.b_setMagicWord)
        if base.config.GetBool('want-chat', 0):
            self.d_setMagicWord('~chat', toonbase.localToon.doId, 0)
        
        if base.config.GetBool('want-run', 0):
            self.toggleRun()
        
        if base.config.GetBool('immortal-mode', 0):
            self.d_setMagicWord('~immortal', toonbase.localToon.doId, 0)
        

    
    def disable(self):
        self.ignore('magicWord')
        if self.dbg_running_fast:
            self.toggleRun()
        
        self.hidefont()

    
    def setMagicWord(self, word, avId, zoneId):
        
        try:
            self.doMagicWord(word, avId, zoneId)
        except:
            self.notify.warning('Ignoring error in magic word.')
            response = PythonUtil.describeException(backTrace = 1)
            self.setMagicWordResponse(response)


    
    def doMagicWord(self, word, avId, zoneId):
        
        def wordIs(w, word = word):
            if not word[:len(w) + 1] == '%s ' % w:
                pass
            return word == w

        print word
        if word == '~endgame':
            print 'Requesting minigame abort...'
            messenger.send('minigameAbort')
        elif word == '~wingame':
            print 'Requesting minigame victory...'
            messenger.send('minigameVictory')
        elif word == '~oobe':
            base.oobe()
        elif word == '~tex':
            base.toggleTexture()
        elif word == '~wire':
            base.toggleWireframe()
        elif word[:9] == '~showfont':
            self.showfont(word[9:])
        elif word == '~hidefont':
            self.hidefont()
        elif word == '~walk':
            
            try:
                fsm = toonbase.tcr.playGame.getPlace().fsm
                fsm.forceTransition('walk')
            except:
                pass

        elif word == '~movie':
            
            try:
                fsm = toonbase.tcr.playGame.getPlace().fsm
                fsm.forceTransition('movie')
            except:
                pass

        elif word == '~sit':
            
            try:
                toonbase.tcr.playGame.getPlace().fsm.request('sit')
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
        elif word[:7] == '~showCS' or word[:7] == '~showcs':
            bitmask = self.getCSBitmask(word[7:])
            render.showCS(bitmask)
            self.csShown = 1
        elif word[:7] == '~hideCS' or word[:7] == '~hidecs':
            bitmask = self.getCSBitmask(word[7:])
            render.hideCS(bitmask)
            self.csShown = 0
        elif word[:3] == '~cs':
            bitmask = self.getCSBitmask(word[3:])
            if self.csShown:
                render.hideCS(bitmask)
                self.csShown = 0
            else:
                render.showCS(bitmask)
                self.csShown = 1
        elif word == '~showCollisions':
            self.showCollisions()
        elif word == '~hideCollisions':
            self.hideCollisions()
        elif word == '~showCameraCollisions':
            self.showCameraCollisions()
        elif word == '~hideCameraCollisions':
            self.hideCameraCollisions()
        elif word == '~showPaths':
            for obj in self.cr.doId2do.values():
                if isinstance(obj, DistributedSuitPlanner.DistributedSuitPlanner):
                    obj.showPaths()
                
            
            place = toonbase.tcr.playGame.getPlace()
            if hasattr(place, 'showPaths'):
                place.showPaths()
            
        elif word == '~hidePaths':
            for obj in self.cr.doId2do.values():
                if isinstance(obj, DistributedSuitPlanner.DistributedSuitPlanner):
                    obj.hidePaths()
                
            
            place = toonbase.tcr.playGame.getPlace()
            if hasattr(place, 'hidePaths'):
                place.hidePaths()
            
        elif word == '~listen':
            toonbase.localToon.garbleChat = 0
        elif word == '~nochat' and word == '~chat' or word == '~superchat':
            toonbase.localToon.garbleChat = 1
        elif word[:7] == '~stress':
            factor = word[7:]
            if factor:
                factor = float(factor)
                LOD.setStressFactor(factor)
                response = 'Set LOD stress factor to %s' % factor
            else:
                factor = LOD.getStressFactor()
                response = 'LOD stress factor is %s' % factor
            self.setMagicWordResponse(response)
        elif word[:5] == '~for ':
            self.forAnother(word, avId, zoneId)
        elif word[:11] == '~photoshoot':
            toonbase.tcr.playGame.hood.sky.hide()
            toonbase.tcr.playGame.getPlace().loader.geom.hide()
            base.win.setClearColor(VBase4(1, 1, 1, 1))
            toonbase.localToon.stopLookAroundNow()
            toonbase.localToon.stopBlink()
            toonbase.localToon.setNameVisible(0)
        elif word[:9] == '~badname ':
            word = '~for %s ~badname' % word[9:]
            print 'word is %s' % word
            self.forAnother(word, avId, zoneId)
        elif word[:6] == '~doId ':
            name = string.strip(word[6:])
            objs = self.identifyDistributedObjects(name)
            if len(objs) == 0:
                response = '%s is unknown.' % name
            else:
                response = ''
                for (name, obj) in objs:
                    response += '\n%s %d' % (name, obj.doId)
                
                response = response[1:]
            self.setMagicWordResponse(response)
        elif word == '~hideAttack':
            TownBattleAttackPanel.hideAttackPanel(1)
        elif word == '~showAttack':
            TownBattleAttackPanel.hideAttackPanel(0)
        elif word == '~collisions_on':
            toonbase.localToon.collisionsOn()
        elif word == '~collisions_off':
            toonbase.localToon.collisionsOff()
        elif word == '~battle_detect_off':
            import DistributedSuit
            DistributedSuit.ALLOW_BATTLE_DETECT = 0
        elif word == '~battle_detect_on':
            import DistributedSuit
            DistributedSuit.ALLOW_BATTLE_DETECT = 1
        elif word == '~battle':
            toonbase.localToon.setWantBattles(not (toonbase.localToon.wantBattles))
            if toonbase.localToon.wantBattles:
                response = 'battles ON'
            else:
                response = 'battles OFF'
            self.setMagicWordResponse(response)
        elif word == '~addCameraPosition':
            toonbase.localToon.addCameraPosition()
        elif word == '~removeCameraPosition':
            toonbase.localToon.removeCameraPosition()
        elif word == '~printCameraPosition':
            toonbase.localToon.printCameraPosition(toonbase.localToon.cameraIndex)
        elif word == '~printCameraPositions':
            toonbase.localToon.printCameraPositions()
        elif word == '~exec':
            ChatManager.ChatManager.execChat = 1
        elif word == '~run':
            self.toggleRun()
        elif word == '~who':
            avIds = []
            for av in Avatar.Avatar.ActiveAvatars:
                if isinstance(av, DistributedToon.DistributedToon):
                    avIds.append(av.doId)
                
            
            self.d_setWho(avIds)
        elif word[:5] == '~sync':
            tm = toonbase.tcr.timeManager
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
                toonbase.tcr.stopPeriodTimer()
                toonbase.tcr.resetPeriodTimer(seconds)
                toonbase.tcr.startPeriodTimer()
            
            if toonbase.tcr.periodTimerExpired:
                response = 'Period timer has expired.'
            elif toonbase.tcr.periodTimerStarted:
                elapsed = globalClock.getFrameTime() - toonbase.tcr.periodTimerStarted
                secondsRemaining = toonbase.tcr.periodTimerSecondsRemaining - elapsed
                response = 'Period timer expires in %s seconds.' % int(secondsRemaining)
            else:
                response = 'Period timer not set.'
            self.setMagicWordResponse(response)
        elif word[:7] == '~DIRECT':
            args = word.split()
            fEnableLight = 0
            if len(args) > 1:
                if direct and args[1] == 'CAM':
                    direct.enable()
                    taskMgr.removeTasksMatching('updateSmartCamera*')
                    camera.wrtReparentTo(render)
                    direct.cameraControl.enableMouseFly()
                    self.setMagicWordResponse('Enabled DIRECT camera')
                    return None
                elif args[1] == 'LIGHT':
                    fEnableLight = 1
                
            
            base.startTk()
            import DirectSession
            if fEnableLight:
                direct.enableLight()
            else:
                direct.enable()
            self.setMagicWordResponse('Enabled DIRECT')
        elif word[:3] == '~TT':
            if not direct:
                return None
            
            args = word.split()
            if len(args) > 1:
                if args[1] == 'CAM':
                    direct.cameraControl.disableMouseFly()
                    camera.wrtReparentTo(toonbase.localToon)
                    toonbase.localToon.startUpdateSmartCamera()
                    self.setMagicWordResponse('Disabled DIRECT camera')
                    return None
                
            
            direct.disable()
            camera.wrtReparentTo(toonbase.localToon)
            toonbase.localToon.startUpdateSmartCamera()
            self.setMagicWordResponse('Disabled DIRECT')
        elif word == '~net':
            if toonbase.tcr.networkPlugPulled():
                toonbase.tcr.restoreNetworkPlug()
                toonbase.tcr.startHeartbeat()
                response = 'Network restored.'
            else:
                toonbase.tcr.pullNetworkPlug()
                toonbase.tcr.stopHeartbeat()
                response = 'Network disconnected.'
            self.setMagicWordResponse(response)
        elif word == '~cogPageFull':
            toonbase.localToon.suitPage.updateAllCogs(3)
        elif word == '~axis':
            axis = loader.loadModel('models/misc/xyzAxis.bam')
            axis.reparentTo(render)
            axis.setPos(toonbase.localToon, 0, 0, 0)
            axis.setHpr(render, 0, 0, 0)
            axis10 = loader.loadModel('models/misc/xyzAxis.bam')
            axis10.reparentTo(render)
            axis10.setPos(toonbase.localToon, 0, 0, 0)
            axis10.setScale(10)
            axis10.setHpr(render, 0, 0, 0)
            axis10.setColorScale(1, 1, 1, 0.40000000000000002)
            axis10.setTransparency(1)
        elif word == '~clearAxes' or word == '~clearAxis':
            render.findAllMatches('**/xyzAxis.egg').detach()
        elif word == '~fedit':
            if not __dev__:
                self.setMagicWordResponse('client not running in dev mode')
            else:
                import DistributedFactory
                import DistributedFactoryEditor
                import EditorGlobals
                EditorGlobals.assertReadyToEdit()
                editUsername = EditorGlobals.getEditUsername()
                factories = toonbase.tcr.doFindAll('DistributedFactory')
                factory = None
                for f in factories:
                    if isinstance(f, DistributedFactoryEditor.DistributedFactoryEditor):
                        if f.editorIsLocalToon():
                            self.setMagicWordResponse('already editing factory')
                            return None
                        
                        if f.getEditUsername() == editUsername:
                            self.setMagicWordResponse("you ('%s') are already editing this factory" % editUsername)
                            return None
                        
                    
                    if isinstance(f, DistributedFactory.DistributedFactory):
                        factory = f
                    
                
                if factory is None:
                    self.setMagicWordResponse('factory not found')
                    return None
                
                factoryDoId = factory.getDoId()
                cmd = '~factoryEdit %s %s' % (factoryDoId, editUsername)
                self.b_setMagicWord(cmd)
        elif word == '~fshow':
            import DistributedFactory
            factories = toonbase.tcr.doFindAll('DistributedFactory')
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
            import DistributedFactory
            factories = toonbase.tcr.doFindAll('DistributedFactory')
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
                goons = toonbase.tcr.doFindAll('Goon')
                for goon in goons:
                    goon.undead()
            except:
                self.notify.warning('Error in undead')

        elif word == '~resyncGoons':
            
            try:
                goons = toonbase.tcr.doFindAll('Goon')
                for goon in goons:
                    goon.resync()
            except:
                self.notify.warning('Error in resyncing')

        elif wordIs('~fps'):
            self.doFps(word, avId, zoneId)
        

    
    def toggleRun(self):
        if self.dbg_running_fast:
            self.dbg_running_fast = 0
            ToontownGlobals.ToonForwardSpeed = self.save_fwdspeed
            ToontownGlobals.ToonReverseSpeed = self.save_revspeed
            ToontownGlobals.ToonRotateSpeed = self.save_rotspeed
            toonbase.localToon.setWalkSpeedNormal()
        else:
            self.dbg_running_fast = 1
            self.save_fwdspeed = ToontownGlobals.ToonForwardSpeed
            self.save_revspeed = ToontownGlobals.ToonReverseSpeed
            self.save_rotspeed = ToontownGlobals.ToonRotateSpeed
            ToontownGlobals.ToonForwardSpeed = 60
            ToontownGlobals.ToonReverseSpeed = 30
            ToontownGlobals.ToonRotateSpeed = 100
            toonbase.localToon.setWalkSpeedNormal()

    
    def d_setMagicWord(self, magicWord, avId, zoneId):
        self.sendUpdate('setMagicWord', [
            magicWord,
            avId,
            zoneId])

    
    def b_setMagicWord(self, magicWord, avId = None, zoneId = None):
        if self.cr.wantMagicWords:
            if avId == None:
                avId = toonbase.localToon.doId
            
            if zoneId == None:
                
                try:
                    zoneId = toonbase.tcr.playGame.getPlace().getZoneId()
                except:
                    pass

                if zoneId == None:
                    zoneId = 0
                
            
            self.d_setMagicWord(magicWord, avId, zoneId)
            self.setMagicWord(magicWord, avId, zoneId)
        

    
    def setMagicWordResponse(self, response):
        toonbase.localToon.setChatAbsolute(response, CFSpeech | CFTimeout)

    
    def requestTeleport(self, loaderId, whereId, hoodId, zoneId, avId):
        place = toonbase.tcr.playGame.getPlace()
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

    
    def d_setWho(self, avIds):
        self.sendUpdate('setWho', [
            avIds])

    
    def exit_rogues(self):
        self.rogues.exit()
        del self.rogues
        self.rogues = None

    
    def forAnother(self, word, avId, zoneId):
        b = 5
        while word[b:b + 2] != ' ~':
            b += 1
            if b >= len(word):
                self.setMagicWordResponse('No next magic word!')
                return None
            
        nextWord = word[b + 1:]
        name = string.strip(word[5:b])
        id = self.identifyAvatar(name)
        if id == None:
            self.setMagicWordResponse("Don't know who %s is." % name)
            return None
        
        self.d_setMagicWord(nextWord, id, zoneId)

    
    def identifyAvatar(self, name):
        for av in Avatar.Avatar.ActiveAvatars:
            if isinstance(av, DistributedToon.DistributedToon) and av.getName() == name:
                return av.doId
            
        
        lowerName = string.lower(name)
        for av in Avatar.Avatar.ActiveAvatars:
            if isinstance(av, DistributedToon.DistributedToon) and string.strip(string.lower(av.getName())) == lowerName:
                return av.doId
            
        
        
        try:
            avId = int(name)
            return avId
        except:
            pass

        return None

    
    def identifyDistributedObjects(self, name):
        result = []
        lowerName = string.lower(name)
        for obj in toonbase.tcr.doId2do.values():
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
        tn.freeze()
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
            
        

    
    def hidefont(self):
        if self.shownFontNode != None:
            self.shownFontNode.removeNode()
            self.shownFontNode = None
        

    
    def showCollisions(self):
        
        try:
            base.cTrav.showCollisions(render)
        except:
            self.setMagicWordResponse('CollisionVisualizer is not compiled in.')
            return None


    
    def hideCollisions(self):
        base.cTrav.hideCollisions()

    
    def showCameraCollisions(self):
        
        try:
            base.ccTrav.showCollisions(render)
        except:
            self.setMagicWordResponse('CollisionVisualizer is not compiled in.')
            return None


    
    def hideCameraCollisions(self):
        base.ccTrav.hideCollisions()

    
    def doFps(self, word, avId, zoneId):
        args = word.split()
        response = None
        if len(args) == 1:
            if base.frameRateMeter:
                base.frameRateMeter.clearLayer()
                base.frameRateMeter = None
            else:
                base.frameRateMeter = FrameRateMeter('frameRateMeter')
                base.frameRateMeter.setupLayer(base.win)
        elif args[1] == 'normal':
            globalClock.setMode(ClockObject.MNormal)
            response = 'Normal frame rate set.'
        elif args[1] == 'forced':
            fps = float(args[2])
            globalClock.setMode(ClockObject.MForced)
            globalClock.setDt(1.0 / fps)
            response = 'Frame rate forced to %s fps.' % fps
        elif args[1] == 'degrade':
            factor = float(args[2])
            globalClock.setMode(ClockObject.MDegrade)
            globalClock.setDegradeFactor(factor)
            response = 'Frame rate degraded by factor of %s.' % factor
        elif args[1][-1] == '%':
            percent = float(args[1][:-1])
            if percent == 100:
                globalClock.setMode(ClockObject.MNormal)
                response = 'Normal frame rate set.'
            else:
                globalClock.setMode(ClockObject.MDegrade)
                globalClock.setDegradeFactor(100.0 / percent)
                response = 'Frame rate degraded to %s percent.' % percent
        else:
            
            try:
                fps = float(args[1])
            except:
                fps = None

            if fps != None:
                globalClock.setMode(ClockObject.MForced)
                globalClock.setDt(1.0 / fps)
                response = 'Frame rate forced to %s fps.' % fps
            else:
                response = 'Unknown fps command: ~s' % args[1]
        if response != None:
            self.setMagicWordResponse(response)
        


