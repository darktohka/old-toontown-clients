# File: D (Python 2.2)

from pandac.PandaModules import *
from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
import MovingPlatform
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
import DistributedSwitch
from direct.distributed import DelayDelete
from toontown.toonbase import TTLocalizer

class DistributedButton(DistributedSwitch.DistributedSwitch):
    countdownSeconds = 3.0
    
    def __init__(self, cr):
        self.countdownTrack = None
        DistributedSwitch.DistributedSwitch.__init__(self, cr)

    
    def setSecondsOn(self, secondsOn):
        self.secondsOn = secondsOn

    
    def avatarExit(self, avatarId):
        DistributedSwitch.DistributedSwitch.avatarExit(self, avatarId)
        if self.secondsOn != -1.0 and self.secondsOn > 0.0 and self.countdownSeconds > 0.0 and self.countdownSeconds < self.secondsOn and self.fsm.getCurrentState().getName() == 'playing':
            track = self.switchCountdownTrack()
            if track is not None:
                track.start(0.0)
                self.countdownTrack = track
            
        

    
    def setupSwitch(self):
        model = loader.loadModelCopy('phase_9/models/cogHQ/CogDoor_Button')
        if model:
            buttonBase = model.find('**/buttonBase')
            change = render.attachNewNode('changePos')
            buttonBase.reparentTo(change)
            rootNode = render.attachNewNode(self.getName() + '-buttonBase_root')
            change.reparentTo(rootNode)
            self.buttonFrameNode = rootNode
            self.buttonFrameNode.show()
            button = model.find('**/button')
            change = render.attachNewNode('change')
            button.reparentTo(change)
            rootNode = render.attachNewNode(self.getName() + '-button_root')
            rootNode.setColor(self.color)
            change.reparentTo(rootNode)
            self.buttonNode = rootNode
            self.buttonNode.show()
            self.buttonFrameNode.reparentTo(self)
            self.buttonNode.reparentTo(self)
            if 1:
                radius = 0.5
                cSphere = CollisionSphere(0.0, 0.0, radius, radius)
                cSphere.setTangible(0)
                cSphereNode = CollisionNode(self.getName())
                cSphereNode.addSolid(cSphere)
                cSphereNode.setCollideMask(ToontownGlobals.WallBitmask)
                self.cSphereNodePath = rootNode.attachNewNode(cSphereNode)
            
            if 1:
                collisionFloor = button.find('**/collision_floor')
                if collisionFloor.isEmpty():
                    top = 0.47499999999999998
                    size = 0.5
                    floor = CollisionPolygon(Point3(-size, -size, top), Point3(size, -size, top), Point3(size, size, top), Point3(-size, size, top))
                    floor.setTangible(1)
                    floorNode = CollisionNode('collision_floor')
                    floorNode.addSolid(floor)
                    collisionFloor = button.attachNewNode(floorNode)
                else:
                    change = collisionFloor.getParent().attachNewNode('changeFloor')
                    change.setScale(0.5, 0.5, 1.0)
                    collisionFloor.reparentTo(change)
                collisionFloor.node().setFromCollideMask(BitMask32.allOff())
                collisionFloor.node().setIntoCollideMask(ToontownGlobals.FloorBitmask)
            
            self.buttonFrameNode.flattenMedium()
            self.buttonNode.flattenMedium()
        

    
    def delete(self):
        DistributedSwitch.DistributedSwitch.delete(self)

    
    def enterTrigger(self, args = None):
        DistributedSwitch.DistributedSwitch.enterTrigger(self, args)

    
    def exitTrigger(self, args = None):
        DistributedSwitch.DistributedSwitch.exitTrigger(self, args)

    
    def switchOnTrack(self):
        onSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_switch_pressed.mp3')
        duration = 0.80000000000000004
        halfDur = duration * 0.5
        pos = Vec3(0.0, 0.0, -0.20000000000000001)
        color = Vec4(0.0, 1.0, 0.0, 1.0)
        track = Sequence(Func(self.setIsOn, 1), Parallel(SoundInterval(onSfx, node = self.node, volume = 0.90000000000000002), LerpPosInterval(nodePath = self.buttonNode, duration = duration, pos = pos, blendType = 'easeInOut'), Sequence(Wait(halfDur), LerpColorInterval(nodePath = self.buttonNode, duration = halfDur, color = color, blendType = 'easeOut'))))
        return track

    
    def switchCountdownTrack(self):
        wait = self.secondsOn - self.countdownSeconds
        countDownSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_switch_depressed.mp3')
        track = Parallel(SoundInterval(countDownSfx), Sequence(Wait(wait), Wait(0.5), LerpColorInterval(nodePath = self.buttonNode, duration = 0.10000000000000001, color = self.color, blendType = 'easeIn'), LerpColorInterval(nodePath = self.buttonNode, duration = 0.10000000000000001, color = Vec4(0.0, 1.0, 0.0, 1.0), blendType = 'easeOut'), Wait(0.5), LerpColorInterval(nodePath = self.buttonNode, duration = 0.10000000000000001, color = self.color, blendType = 'easeIn'), LerpColorInterval(nodePath = self.buttonNode, duration = 0.10000000000000001, color = Vec4(0.0, 1.0, 0.0, 1.0), blendType = 'easeOut'), Wait(0.40000000000000002), LerpColorInterval(nodePath = self.buttonNode, duration = 0.10000000000000001, color = self.color, blendType = 'easeIn'), LerpColorInterval(nodePath = self.buttonNode, duration = 0.10000000000000001, color = Vec4(0.0, 1.0, 0.0, 1.0), blendType = 'easeOut'), Wait(0.29999999999999999), LerpColorInterval(nodePath = self.buttonNode, duration = 0.10000000000000001, color = self.color, blendType = 'easeIn'), LerpColorInterval(nodePath = self.buttonNode, duration = 0.10000000000000001, color = Vec4(0.0, 1.0, 0.0, 1.0), blendType = 'easeOut'), Wait(0.20000000000000001), LerpColorInterval(nodePath = self.buttonNode, duration = 0.10000000000000001, color = self.color, blendType = 'easeIn'), LerpColorInterval(nodePath = self.buttonNode, duration = 0.10000000000000001, color = Vec4(0.0, 1.0, 0.0, 1.0), blendType = 'easeOut'), Wait(0.10000000000000001)))
        return track

    
    def switchOffTrack(self):
        offSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_switch_popup.mp3')
        duration = 1.0
        halfDur = duration * 0.5
        pos = Vec3(0.0)
        track = Sequence(Parallel(SoundInterval(offSfx, node = self.node, volume = 1.0), LerpPosInterval(nodePath = self.buttonNode, duration = duration, pos = pos, blendType = 'easeInOut'), Sequence(Wait(halfDur), LerpColorInterval(nodePath = self.buttonNode, duration = halfDur, color = self.color, blendType = 'easeIn'))), Func(self.setIsOn, 0))
        return track

    
    def exitPlaying(self):
        if self.countdownTrack:
            self.countdownTrack.finish()
        
        self.countdownTrack = None
        DistributedSwitch.DistributedSwitch.exitPlaying(self)


