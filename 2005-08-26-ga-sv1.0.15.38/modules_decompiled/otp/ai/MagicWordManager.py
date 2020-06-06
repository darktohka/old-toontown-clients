# File: M (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from otp.avatar import Avatar
import string
from direct.showbase import PythonUtil
from otp.otpbase import OTPGlobals
from direct.distributed.ClockDelta import *

class MagicWordManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('MagicWordManager')
    neverDisable = 1
    GameAvatarClass = None
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.shownFontNode = None
        self.csShown = 0

    
    def generate(self):
        self.accept('magicWord', self.b_setMagicWord)

    
    def disable(self):
        self.ignore('magicWord')
        self.hidefont()
        DistributedObject.DistributedObject.disable(self)

    
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
        if word == '~oobe':
            base.oobe()
        elif word == '~oobeCull':
            base.oobeCull()
        elif word == '~tex':
            base.toggleTexture()
        elif word == '~wire':
            base.toggleWireframe()
        elif word[:9] == '~showfont':
            self.showfont(word[9:])
        elif word == '~hidefont':
            self.hidefont()
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
        elif word == '~showShadowCollisions':
            self.showShadowCollisions()
        elif word == '~hideShadowCollisions':
            self.hideShadowCollisions()
        elif word == '~showCollisions':
            self.showCollisions()
        elif word == '~hideCollisions':
            self.hideCollisions()
        elif word == '~showCameraCollisions':
            self.showCameraCollisions()
        elif word == '~hideCameraCollisions':
            self.hideCameraCollisions()
        elif wordIs('~stress'):
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
        elif word == '~exec':
            ChatManager = ChatManager
            import otp.chat
            ChatManager.ChatManager.execChat = 1
        elif word == '~run':
            self.toggleRun()
        elif word == '~who':
            avIds = []
            for av in Avatar.Avatar.ActiveAvatars:
                if hasattr(av, 'getFriendsList'):
                    avIds.append(av.doId)
                
            
            self.d_setWho(avIds)
        elif word[:5] == '~sync':
            tm = self.cr.timeManager
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
                self.cr.stopPeriodTimer()
                self.cr.resetPeriodTimer(seconds)
                self.cr.startPeriodTimer()
            
            if self.cr.periodTimerExpired:
                response = 'Period timer has expired.'
            elif self.cr.periodTimerStarted:
                elapsed = globalClock.getFrameTime() - self.cr.periodTimerStarted
                secondsRemaining = self.cr.periodTimerSecondsRemaining - elapsed
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
            DirectSession = DirectSession
            import direct.directtools
            if fEnableLight:
                direct.enableLight()
            else:
                direct.enable()
            self.setMagicWordResponse('Enabled DIRECT')
        elif word == '~net':
            if self.cr.networkPlugPulled():
                self.cr.restoreNetworkPlug()
                self.cr.startHeartbeat()
                response = 'Network restored.'
            else:
                self.cr.pullNetworkPlug()
                self.cr.stopHeartbeat()
                response = 'Network disconnected.'
            self.setMagicWordResponse(response)
        elif word == '~axis':
            axis = loader.loadModel('models/misc/xyzAxis.bam')
            axis.reparentTo(render)
            axis.setPos(base.localAvatar, 0, 0, 0)
            axis.setHpr(render, 0, 0, 0)
            axis10 = loader.loadModel('models/misc/xyzAxis.bam')
            axis10.reparentTo(render)
            axis10.setPos(base.localAvatar, 0, 0, 0)
            axis10.setScale(10)
            axis10.setHpr(render, 0, 0, 0)
            axis10.setColorScale(1, 1, 1, 0.40000000000000002)
            axis10.setTransparency(1)
        elif word == '~clearAxes' or word == '~clearAxis':
            render.findAllMatches('**/xyzAxis.egg').detach()
        elif word == '~osd':
            onScreenDebug.enabled = not (onScreenDebug.enabled)
        elif wordIs('~fps'):
            self.doFps(word, avId, zoneId)
        elif wordIs('~sleep'):
            args = word.split()
            if len(args) > 1:
                s = float(args[1])
                base.mwClientSleep = s
                response = 'sleeping %s' % s
            else:
                base.mwClientSleep = 0.0
                response = 'not sleeping'
            self.setMagicWordResponse(response)
        else:
            return 0
        return 1

    
    def toggleRun(self):
        inputState.set('debugRunning', inputState.isSet('debugRunning') != True)

    
    def d_setMagicWord(self, magicWord, avId, zoneId):
        self.sendUpdate('setMagicWord', [
            magicWord,
            avId,
            zoneId])

    
    def b_setMagicWord(self, magicWord, avId = None, zoneId = None):
        if self.cr.wantMagicWords:
            if avId == None:
                avId = base.localAvatar.doId
            
            if zoneId == None:
                
                try:
                    zoneId = self.cr.playGame.getPlace().getZoneId()
                except:
                    pass

                if zoneId == None:
                    zoneId = 0
                
            
            self.d_setMagicWord(magicWord, avId, zoneId)
            self.setMagicWord(magicWord, avId, zoneId)
        

    
    def setMagicWordResponse(self, response):
        base.localAvatar.setChatAbsolute(response, CFSpeech | CFTimeout)

    
    def d_setWho(self, avIds):
        self.sendUpdate('setWho', [
            avIds])

    
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
        self.notify.error('Pure virtual - please override me.')

    
    def identifyDistributedObjects(self, name):
        result = []
        lowerName = string.lower(name)
        for obj in self.cr.doId2do.values():
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
                bitmask |= OTPGlobals.WallBitmask
            elif w == 'floor':
                bitmask |= OTPGlobals.FloorBitmask
            elif w == 'cam':
                bitmask |= OTPGlobals.CameraBitmask
            elif w == 'catch':
                bitmask |= OTPGlobals.CatchBitmask
            elif w == 'ghost':
                bitmask |= OTPGlobals.GhostBitmask
            elif w == 'pet':
                bitmask |= OTPGlobals.PetBitmask
            elif w == 'furniture':
                bitmask |= OTPGlobals.FurnitureSideBitmask | OTPGlobals.FurnitureTopBitmask | OTPGlobals.FurnitureDragBitmask
            elif w == 'furnitureside':
                bitmask |= OTPGlobals.FurnitureSideBitmask
            elif w == 'furnituretop':
                bitmask |= OTPGlobals.FurnitureTopBitmask
            elif w == 'furnituredrag':
                bitmask |= OTPGlobals.FurnitureDragBitmask
            elif w == 'pie':
                bitmask |= OTPGlobals.PieBitmask
            else:
                invalid += ' ' + w
        
        if invalid:
            self.setMagicWordResponse('Unknown CS keyword(s): %s' % invalid)
        
        return bitmask

    
    def hidefont(self):
        if self.shownFontNode != None:
            self.shownFontNode.removeNode()
            self.shownFontNode = None
        

    
    def showShadowCollisions(self):
        
        try:
            base.shadowTrav.showCollisions(render)
        except:
            self.setMagicWordResponse('CollisionVisualizer is not compiled in.')


    
    def hideShadowCollisions(self):
        base.shadowTrav.hideCollisions()

    
    def showCollisions(self):
        
        try:
            base.cTrav.showCollisions(render)
        except:
            self.setMagicWordResponse('CollisionVisualizer is not compiled in.')


    
    def hideCollisions(self):
        base.cTrav.hideCollisions()

    
    def showCameraCollisions(self):
        
        try:
            base.ccTrav.showCollisions(render)
        except:
            self.setMagicWordResponse('CollisionVisualizer is not compiled in.')


    
    def hideCameraCollisions(self):
        base.ccTrav.hideCollisions()

    
    def doFps(self, word, avId, zoneId):
        args = word.split()
        response = None
        if len(args) == 1 or args[1] == 'normal':
            if globalClock.getMode() != ClockObject.MNormal:
                globalClock.setMode(ClockObject.MNormal)
                response = 'Normal frame rate set.'
            else:
                base.setFrameRateMeter(not (base.frameRateMeter))
        elif args[1] == 'forced':
            fps = float(args[2])
            globalClock.setMode(ClockObject.MForced)
            globalClock.setDt(1.0 / fps)
            response = 'Frame rate forced to %s fps.' % fps
            base.setFrameRateMeter(1)
        elif args[1] == 'degrade':
            factor = float(args[2])
            globalClock.setMode(ClockObject.MDegrade)
            globalClock.setDegradeFactor(factor)
            response = 'Frame rate degraded by factor of %s.' % factor
            base.setFrameRateMeter(1)
        elif args[1][-1] == '%':
            percent = float(args[1][:-1])
            if percent == 100:
                globalClock.setMode(ClockObject.MNormal)
                response = 'Normal frame rate set.'
            else:
                globalClock.setMode(ClockObject.MDegrade)
                globalClock.setDegradeFactor(100.0 / percent)
                response = 'Frame rate degraded to %s percent.' % percent
            base.setFrameRateMeter(1)
        else:
            
            try:
                fps = float(args[1])
            except:
                fps = None

            if fps != None:
                globalClock.setMode(ClockObject.MForced)
                globalClock.setDt(1.0 / fps)
                response = 'Frame rate forced to %s fps.' % fps
                base.setFrameRateMeter(1)
            else:
                response = 'Unknown fps command: ~s' % args[1]
        if response != None:
            self.setMagicWordResponse(response)
        

    
    def identifyAvatar(self, name):
        for av in Avatar.Avatar.ActiveAvatars:
            if isinstance(av, self.GameAvatarClass) and av.getName() == name:
                return av.doId
            
        
        lowerName = string.lower(name)
        for av in Avatar.Avatar.ActiveAvatars:
            if isinstance(av, self.GameAvatarClass) and string.strip(string.lower(av.getName())) == lowerName:
                return av.doId
            
        
        
        try:
            avId = int(name)
            return avId
        except:
            pass

        return None


