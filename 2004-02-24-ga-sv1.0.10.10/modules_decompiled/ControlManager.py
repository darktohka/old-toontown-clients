# File: C (Python 2.2)

from ShowBaseGlobal import *
import Avatar
import DirectNotifyGlobal
import GhostWalker
import GravityWalker
import NonPhysicsWalker
import PhysicsWalker
import Task

class ControlManager:
    notify = DirectNotifyGlobal.directNotify.newCategory('ControlManager')
    wantAvatarPhysicsIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    wantAvatarPhysicsDebug = base.config.GetBool('want-avatar-physics-debug', 0)
    
    def __init__(self, avatar):
        self.avatar = avatar
        self.enableJumpCounter = 1
        self.swimControls = NonPhysicsWalker.NonPhysicsWalker()
        self.ghostControls = GhostWalker.GhostWalker()
        self.walkControls = GravityWalker.GravityWalker(gravity = -32.173999999999999 * 2.0)
        self.currentControls = self.walkControls
        self.isEnabled = 1
        inputState.watch('forward', 'arrow_up', 'arrow_up-up')
        inputState.watch('forward', 'control-arrow_up', 'control-arrow_up-up')
        inputState.watch('forward', 'alt-arrow_up', 'alt-arrow_up-up')
        inputState.watch('forward', 'shift-arrow_up', 'shift-arrow_up-up')
        inputState.watch('reverse', 'arrow_down', 'arrow_down-up')
        inputState.watch('reverse', 'control-arrow_down', 'control-arrow_down-up')
        inputState.watch('reverse', 'alt-arrow_down', 'alt-arrow_down-up')
        inputState.watch('reverse', 'shift-arrow_down', 'shift-arrow_down-up')
        inputState.watch('turnLeft', 'arrow_left', 'arrow_left-up')
        inputState.watch('turnLeft', 'control-arrow_left', 'control-arrow_left-up')
        inputState.watch('turnLeft', 'alt-arrow_left', 'alt-arrow_left-up')
        inputState.watch('turnLeft', 'shift-arrow_left', 'shift-arrow_left-up')
        inputState.watch('turnRight', 'arrow_right', 'arrow_right-up')
        inputState.watch('turnRight', 'control-arrow_right', 'control-arrow_right-up')
        inputState.watch('turnRight', 'alt-arrow_right', 'alt-arrow_right-up')
        inputState.watch('turnRight', 'shift-arrow_right', 'shift-arrow_right-up')
        inputState.watch('jump', 'control', 'control-up')
        inputState.watch('jump', 'alt-control', 'alt-control-up')
        inputState.watch('jump', 'shift-control', 'shift-control-up')
        inputState.watch('slideLeft', 'home', 'home-up')
        inputState.watch('slideRight', 'end', 'end-up')
        inputState.watch('levitateUp', 'page_up', 'page_up-up')
        inputState.watch('levitateDown', 'page_down', 'page_down-up')
        inputState.watch('run', 'shift', 'shift-up')
        inputState.watch('slide', 'slide-is-disabled', 'slide-is-disabled')

    
    def add(self, controls, name = 'basic'):
        controls = self.controls.get(name)
        if controls is not None:
            print 'Replacing controls:', name
            controls.delete()
        
        self.controls[name] = controls

    
    def use(self, name = 'basic'):
        controls = self.controls.get(name)
        if controls is not None:
            if controls is not self.currentControls:
                self.currentControls.disableAvatarControls()
                self.currentControls.setCollisionsActive(0)
                self.currentControls = controls
                self.currentControls.setCollisionsActive(1)
            
        else:
            print 'Unkown controls:', name

    
    def setSpeeds_new(self, toonForwardSpeed, toonJumpForce, toonReverseSpeed, toonRotateSpeed):
        for controls in self.controls.values():
            controls.setWalkSpeed(toonForwardSpeed, toonJumpForce, toonReverseSpeed, toonRotateSpeed)
        

    
    def useSwimControls(self):
        if self.currentControls is not self.swimControls:
            self.currentControls.disableAvatarControls()
            self.currentControls.setCollisionsActive(0)
            self.swimControls.setCollisionsActive(1)
            self.currentControls = self.swimControls
            if self.isEnabled:
                self.currentControls.enableAvatarControls()
            
        

    
    def useGhostControls(self):
        if self.currentControls is not self.ghostControls:
            self.currentControls.disableAvatarControls()
            self.currentControls.setCollisionsActive(0)
            self.ghostControls.setCollisionsActive(1)
            self.currentControls = self.ghostControls
            if self.isEnabled:
                self.currentControls.enableAvatarControls()
            
        

    
    def useWalkControls(self):
        if self.currentControls is not self.walkControls:
            self.currentControls.disableAvatarControls()
            self.currentControls.setCollisionsActive(0)
            self.walkControls.setCollisionsActive(1)
            self.currentControls = self.walkControls
            if self.isEnabled:
                self.currentControls.enableAvatarControls()
            
        

    
    def delete(self):
        self.disable()

    
    def setSpeeds(self, toonForwardSpeed, toonJumpForce, toonReverseSpeed, toonRotateSpeed):
        self.swimControls.setWalkSpeed(toonForwardSpeed, toonJumpForce, toonReverseSpeed, toonRotateSpeed)
        self.ghostControls.setWalkSpeed(toonForwardSpeed, toonJumpForce, toonReverseSpeed, toonRotateSpeed)
        self.walkControls.setWalkSpeed(toonForwardSpeed, toonJumpForce, toonReverseSpeed, toonRotateSpeed)

    
    def getSpeeds(self):
        return self.currentControls.getSpeeds()

    
    def initializeCollisions(self, cTrav, wallBitmask, floorBitmask, ghostBitmask, avatarRadius, floorOffset):
        self.walkControls.initializeCollisions(cTrav, self.avatar, wallBitmask, floorBitmask, avatarRadius, floorOffset)
        self.walkControls.setAirborneHeightFunc(self.avatar.getAirborneHeight)
        self.walkControls.disableAvatarControls()
        self.walkControls.setCollisionsActive(0)
        self.swimControls.initializeCollisions(cTrav, self.avatar, wallBitmask, floorBitmask, avatarRadius, floorOffset)
        self.swimControls.setAirborneHeightFunc(self.avatar.getAirborneHeight)
        self.swimControls.disableAvatarControls()
        self.swimControls.setCollisionsActive(0)
        self.ghostControls.initializeCollisions(cTrav, self.avatar, ghostBitmask, floorBitmask, avatarRadius, floorOffset)
        self.ghostControls.setAirborneHeightFunc(self.avatar.getAirborneHeight)
        self.ghostControls.disableAvatarControls()
        self.ghostControls.setCollisionsActive(0)

    
    def deleteCollisions(self):
        self.walkControls.deleteCollisions()
        self.swimControls.deleteCollisions()
        self.ghostControls.deleteCollisions()

    
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
        if 1:
            airborneHeight = self.avatar.getAirborneHeight()
            onScreenDebug.add('airborneHeight', '% 10.4f' % (airborneHeight,))
        
        return Task.cont


