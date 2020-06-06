# File: D (Python 2.2)

from direct.showbase.PandaObject import *
from direct.showbase.ShowBaseGlobal import *
import Playground
import whrandom
from direct.fsm import State
from direct.actor import Actor
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import Place

class DDPlayground(Playground.Playground):
    notify = DirectNotifyGlobal.directNotify.newCategory('DDPlayground')
    
    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.cameraSubmerged = -1
        self.toonSubmerged = -1
        self.activityFsm = ClassicFSM.ClassicFSM('Activity', [
            State.State('off', self.enterOff, self.exitOff, [
                'OnBoat']),
            State.State('OnBoat', self.enterOnBoat, self.exitOnBoat, [
                'off'])], 'off', 'off')
        self.activityFsm.enterInitialState()

    
    def load(self):
        Playground.Playground.load(self)

    
    def unload(self):
        del self.activityFsm
        Playground.Playground.unload(self)

    
    def enter(self, requestStatus):
        self.nextSeagullTime = 0
        taskMgr.add(self._DDPlayground__seagulls, 'dd-seagulls')
        self.loader.hood.setWhiteFog()
        donald = self.loader.donald
        donald.loop('wheel')
        donald.setZ(3.9500000000000002)
        donald.setY(-1.0)
        donald.reparentTo(base.cr.playGame.hood.loader.boat)
        Playground.Playground.enter(self, requestStatus)

    
    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.remove('dd-check-toon-underwater')
        taskMgr.remove('dd-check-cam-underwater')
        taskMgr.remove('dd-seagulls')
        self.loader.hood.setNoFog()
        donald = self.loader.donald
        donald.stop()
        donald.reparentTo(hidden)

    
    def enterStart(self):
        self.cameraSubmerged = 0
        self.toonSubmerged = 0
        taskMgr.add(self._DDPlayground__checkToonUnderwater, 'dd-check-toon-underwater')
        taskMgr.add(self._DDPlayground__checkCameraUnderwater, 'dd-check-cam-underwater')

    
    def enterDoorOut(self):
        taskMgr.remove('dd-check-toon-underwater')

    
    def exitDoorOut(self):
        pass

    
    def enterDoorIn(self, requestStatus):
        Playground.Playground.enterDoorIn(self, requestStatus)
        taskMgr.add(self._DDPlayground__checkToonUnderwater, 'dd-check-toon-underwater')

    
    def _DDPlayground__checkCameraUnderwater(self, task):
        if camera.getZ(render) < 1.0:
            self._DDPlayground__submergeCamera()
        else:
            self._DDPlayground__emergeCamera()
        return Task.cont

    
    def _DDPlayground__checkToonUnderwater(self, task):
        if base.localAvatar.getZ() < -2.3314585000000001:
            self._DDPlayground__submergeToon()
        else:
            self._DDPlayground__emergeToon()
        return Task.cont

    
    def _DDPlayground__submergeCamera(self):
        if self.cameraSubmerged == 1:
            return None
        
        self.loader.hood.setUnderwaterFog()
        base.playSfx(self.loader.underwaterSound, looping = 1, volume = 0.80000000000000004)
        self.loader.seagullSound.stop()
        taskMgr.remove('dd-seagulls')
        self.cameraSubmerged = 1
        self.walkStateData.setSwimSoundAudible(1)

    
    def _DDPlayground__emergeCamera(self):
        if self.cameraSubmerged == 0:
            return None
        
        self.loader.hood.setWhiteFog()
        self.loader.underwaterSound.stop()
        self.nextSeagullTime = whrandom.random() * 8.0
        taskMgr.add(self._DDPlayground__seagulls, 'dd-seagulls')
        self.cameraSubmerged = 0
        self.walkStateData.setSwimSoundAudible(0)

    
    def _DDPlayground__submergeToon(self):
        if self.toonSubmerged == 1:
            return None
        
        base.playSfx(self.loader.submergeSound)
        self.fsm.request('walk')
        self.walkStateData.fsm.request('swimming', [
            self.loader.swimSound])
        pos = base.localAvatar.getPos(render)
        base.localAvatar.d_playSplashEffect(pos[0], pos[1], 1.675)
        self.toonSubmerged = 1

    
    def _DDPlayground__emergeToon(self):
        if self.toonSubmerged == 0:
            return None
        
        self.walkStateData.fsm.request('walking')
        self.toonSubmerged = 0

    
    def _DDPlayground__seagulls(self, task):
        if task.time < self.nextSeagullTime:
            return Task.cont
        
        base.playSfx(self.loader.seagullSound)
        self.nextSeagullTime = task.time + whrandom.random() * 4.0 + 8.0
        return Task.cont

    
    def handleBookClose(self):
        Playground.Playground.handleBookClose(self)
        if self.toonSubmerged == 1:
            self.walkStateData.fsm.request('swimming', [
                self.loader.swimSound])
        

    
    def enterTeleportIn(self, requestStatus):
        self.toonSubmerged = -1
        taskMgr.remove('dd-check-toon-underwater')
        Playground.Playground.enterTeleportIn(self, requestStatus)

    
    def teleportInDone(self):
        self.toonSubmerged = -1
        taskMgr.add(self._DDPlayground__checkToonUnderwater, 'dd-check-toon-underwater')
        Playground.Playground.teleportInDone(self)

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterOnBoat(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPDonaldsBoat)
        base.playSfx(self.loader.waterSound, looping = 1)

    
    def exitOnBoat(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPRender)
        self.loader.waterSound.stop()


