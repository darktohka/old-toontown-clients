# File: W (Python 2.2)

from ShowBaseGlobal import *
import DirectNotifyGlobal
import PandaObject
import StateData
import FSM
import State
import Emote

class Walk(PandaObject.PandaObject, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('Walk')
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = FSM.FSM('Walk', [
            State.State('off', self.enterOff, self.exitOff, [
                'walking',
                'swimming',
                'slowWalking',
                'jumping']),
            State.State('walking', self.enterWalking, self.exitWalking, [
                'swimming',
                'slowWalking',
                'jumping']),
            State.State('swimming', self.enterSwimming, self.exitSwimming, [
                'walking',
                'slowWalking']),
            State.State('slowWalking', self.enterSlowWalking, self.exitSlowWalking, [
                'walking',
                'swimming']),
            State.State('jumping', self.enterJumping, self.exitJumping, [
                'walking',
                'swimming'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.IsSwimSoundAudible = 0
        self.swimSoundPlaying = 0

    
    def load(self):
        pass

    
    def unload(self):
        del self.fsm

    
    def enter(self, slowWalk = 0):
        toonbase.localToon.lifter.clear()
        toonbase.localToon.startPosHprBroadcast()
        toonbase.localToon.startBlink()
        toonbase.localToon.attachCamera()
        toonbase.localToon.startUpdateSmartCamera()
        toonbase.localToon.addTabHook()
        toonbase.localToon.showName()
        toonbase.localToon.collisionsOn()
        self.accept('control', self._Walk__handleJumpKey)

    
    def exit(self):
        self.fsm.request('off')
        toonbase.localToon.stopUpdateSmartCamera()
        toonbase.localToon.stopPosHprBroadcast()
        toonbase.localToon.stopBlink()
        toonbase.localToon.detachCamera()
        toonbase.localToon.removeTabHook()
        toonbase.localToon.collisionsOff()
        self.ignore('control')

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterWalking(self):
        if toonbase.localToon.hp > 0:
            toonbase.localToon.startTrackAnimToSpeed()
            toonbase.localToon.setWalkSpeedNormal()
        else:
            self.fsm.request('slowWalking')

    
    def exitWalking(self):
        toonbase.localToon.stopTrackAnimToSpeed()

    
    def setSwimSoundAudible(self, IsSwimSoundAudible):
        self.IsSwimSoundAudible = IsSwimSoundAudible
        if IsSwimSoundAudible == 0 and self.swimSoundPlaying:
            self.swimSound.stop()
            self.swimSoundPlaying = 0
        

    
    def enterSwimming(self, swimSound):
        toonbase.localToon.setWalkSpeedNormal()
        self.swimSound = swimSound
        self.swimSoundPlaying = 0
        toonbase.localToon.b_setAnimState('swim', toonbase.localToon.animMultiplier)
        taskMgr.add(self._Walk__swim, 'localToonSwimming')

    
    def exitSwimming(self):
        taskMgr.remove('localToonSwimming')
        self.swimSound.stop()
        del self.swimSound
        self.swimSoundPlaying = 0

    
    def _Walk__swim(self, task):
        speed = base.mouseInterfaceNode.getSpeed()
        if speed == 0 and self.swimSoundPlaying:
            self.swimSoundPlaying = 0
            self.swimSound.stop()
        elif speed > 0 and self.swimSoundPlaying == 0 and self.IsSwimSoundAudible:
            self.swimSoundPlaying = 1
            base.playSfx(self.swimSound, looping = 1)
        
        return Task.cont

    
    def enterSlowWalking(self):
        self.accept(toonbase.localToon.uniqueName('positiveHP'), self._Walk__handlePositiveHP)
        toonbase.localToon.startTrackAnimToSpeed()
        toonbase.localToon.setWalkSpeedSlow()

    
    def _Walk__handlePositiveHP(self):
        self.fsm.request('walking')

    
    def exitSlowWalking(self):
        toonbase.localToon.stopTrackAnimToSpeed()
        self.ignore(toonbase.localToon.uniqueName('positiveHP'))

    
    def _Walk__handleJumpKey(self):
        state = self.fsm.getCurrentState().getName()
        if state == 'walking':
            self.fsm.request('jumping')
        

    
    def enterJumping(self):
        Emote.DisableBody(toonbase.localToon, 'Walk, enterJumping')
        toonbase.localToon.stopTrackAnimToSpeed()
        toonbase.localToon.b_setAnimState('jump', 1.0)
        toonbase.localToon.wakeUp()
        
        def returnToWalk(state):
            self.fsm.request('walking')
            return Task.done

        jumpTime = toonbase.localToon.getJumpDuration()
        taskMgr.doMethodLater(jumpTime, returnToWalk, toonbase.localToon.uniqueName('walkReturnTask'))

    
    def exitJumping(self):
        taskMgr.remove(toonbase.localToon.uniqueName('walkReturnTask'))
        Emote.ReleaseBody(toonbase.localToon, 'Walk, exitJumping')


