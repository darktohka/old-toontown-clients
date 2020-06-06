# File: C (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from otp.avatar import Avatar
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task

class ControlManager:
    notify = DirectNotifyGlobal.directNotify.newCategory('ControlManager')
    wantAvatarPhysicsIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    wantAvatarPhysicsDebug = base.config.GetBool('want-avatar-physics-debug', 0)
    
    def __init__(self):
        self.enableJumpCounter = 1
        self.controls = { }
        self.currentControls = None
        self.isEnabled = 1
        inputState.watch('run', 'running-on', 'running-off')
        inputState.watch('forward', 'arrow_up', 'arrow_up-up')
        inputState.watch('forward', 'control-arrow_up', 'arrow_up-up')
        inputState.watch('forward', 'shift-control-arrow_up', 'arrow_up-up')
        inputState.watch('forward', 'alt-arrow_up', 'arrow_up-up')
        inputState.watch('forward', 'control-alt-arrow_up', 'arrow_up-up')
        inputState.watch('forward', 'shift-arrow_up', 'arrow_up-up')
        inputState.watch('reverse', 'arrow_down', 'arrow_down-up')
        inputState.watch('reverse', 'control-arrow_down', 'arrow_down-up')
        inputState.watch('reverse', 'shift-control-arrow_down', 'arrow_down-up')
        inputState.watch('reverse', 'alt-arrow_down', 'arrow_down-up')
        inputState.watch('reverse', 'control-alt-arrow_down', 'arrow_down-up')
        inputState.watch('reverse', 'shift-arrow_down', 'arrow_down-up')
        inputState.watch('turnLeft', 'arrow_left', 'arrow_left-up')
        inputState.watch('turnLeft', 'control-arrow_left', 'arrow_left-up')
        inputState.watch('turnLeft', 'shift-control-arrow_left', 'arrow_left-up')
        inputState.watch('turnLeft', 'alt-arrow_left', 'alt-arrow_left-up')
        inputState.watch('turnLeft', 'control-alt-arrow_left', 'alt-arrow_left-up')
        inputState.watch('turnLeft', 'shift-arrow_left', 'arrow_left-up')
        inputState.watch('turnLeft', 'mouse-look_left', 'mouse-look_left-done')
        inputState.watch('turnRight', 'arrow_right', 'arrow_right-up')
        inputState.watch('turnRight', 'control-arrow_right', 'arrow_right-up')
        inputState.watch('turnRight', 'shift-control-arrow_right', 'arrow_right-up')
        inputState.watch('turnRight', 'alt-arrow_right', 'arrow_right-up')
        inputState.watch('turnRight', 'control-alt-arrow_right', 'arrow_right-up')
        inputState.watch('turnRight', 'shift-arrow_right', 'arrow_right-up')
        inputState.watch('turnRight', 'mouse-look_right', 'mouse-look_right-done')
        inputState.watch('jump', 'control', 'control-up')
        inputState.watch('slideLeft', 'home', 'home-up')
        inputState.watch('slideRight', 'end', 'end-up')
        inputState.watch('levitateUp', 'page_up', 'page_up-up')
        inputState.watch('levitateDown', 'page_down', 'page_down-up')
        inputState.watch('run', 'shift', 'shift-up')
        inputState.watch('slide', 'mouse3', 'mouse3-up')

    
    def add(self, controls, name = 'basic'):
        oldControls = self.controls.get(name)
        if oldControls is not None:
            print 'Replacing controls:', name
            oldControls.disableAvatarControls()
            oldControls.setCollisionsActive(0)
            oldControls.delete()
        
        controls.disableAvatarControls()
        controls.setCollisionsActive(0)
        self.controls[name] = controls

    
    def use(self, name, avatar):
        controls = self.controls.get(name)
        if controls is not None:
            if controls is not self.currentControls:
                if self.currentControls is not None:
                    self.currentControls.disableAvatarControls()
                    self.currentControls.setCollisionsActive(0)
                    self.currentControls.setAvatar(None)
                
                self.currentControls = controls
                self.currentControls.setAvatar(avatar)
                self.currentControls.setCollisionsActive(1)
                if self.isEnabled:
                    self.currentControls.enableAvatarControls()
                
                messenger.send('use-%s-controls' % (name,), [
                    avatar])
            
        else:
            print 'Unkown controls:', name

    
    def setSpeeds(self, forwardSpeed, jumpForce, reverseSpeed, rotateSpeed):
        for controls in self.controls.values():
            controls.setWalkSpeed(forwardSpeed, jumpForce, reverseSpeed, rotateSpeed)
        

    
    def delete(self):
        self.disable()
        del self.controls
        del self.currentControls

    
    def getSpeeds(self):
        return self.currentControls.getSpeeds()

    
    def setTag(self, key, value):
        for controls in self.controls.values():
            controls.setTag(key, value)
        

    
    def deleteCollisions(self):
        for controls in self.controls.values():
            controls.deleteCollisions()
        

    
    def collisionsOn(self):
        self.currentControls.setCollisionsActive(1)

    
    def collisionsOff(self):
        self.currentControls.setCollisionsActive(0)

    
    def placeOnFloor(self):
        self.currentControls.placeOnFloor()

    
    def enable(self):
        self.isEnabled = 1
        self.currentControls.enableAvatarControls()

    
    def disable(self):
        self.isEnabled = 0
        self.currentControls.disableAvatarControls()

    
    def enableAvatarJump(self):
        self.enableJumpCounter += 1
        if self.enableJumpCounter:
            self.enableJumpCounter = 1
            inputState.unforce('jump')
        

    
    def disableAvatarJump(self):
        self.enableJumpCounter -= 1
        if self.enableJumpCounter <= 0:
            inputState.force('jump', 0)
        

    
    def monitor(self, foo):
        return Task.cont


