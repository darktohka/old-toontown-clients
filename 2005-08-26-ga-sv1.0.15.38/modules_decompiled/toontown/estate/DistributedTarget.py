# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase.PandaObject import *
from direct.interval.IntervalGlobal import *
from toontown.toonbase.ToontownGlobals import *
from toontown.toonbase import ToontownTimer
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal

class DistributedTarget(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTarget')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.geom = None
        self.numConsecutiveHits = 0
        self.enabled = 0
        self.score = 0
        self.hitTime = 0
        self.targetBounceTrack = None

    
    def disable(self):
        self.ignoreAll()
        DistributedObject.DistributedObject.disable(self)
        if self.targetBounceTrack:
            self.targetBounceTrack.finish()
            self.targetBounceTrack = None
        

    
    def generateInit(self):
        self.load()

    
    def load(self):
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.posAboveShtikerBook()
        self.timer.hide()
        self.geom = loader.loadModel('../dmodels/models/misc/smiley')
        self.geom.reparentTo(base.cr.playGame.hood.loader.geom)
        self.geom.setPos(0, 0, 40)
        self.geom.setScale(3)
        self.hitSound = base.loadSfx('phase_4/audio/sfx/MG_Tag_A.mp3')
        self.rewardSound = base.loadSfx('phase_4/audio/sfx/MG_pos_buzzer.wav')
        self.scoreText = TextNode('scoreText')
        self.scoreText.setTextColor(1, 0, 0, 1)
        self.scoreText.setAlign(self.scoreText.ACenter)
        self.scoreText.setFont(getSignFont())
        self.scoreText.setText('0')
        self.scoreNode = self.timer.attachNewNode(self.scoreText)
        self.scoreNode.setPos(0, 0, 0.29999999999999999)
        self.scoreNode.setScale(0.25)
        colSphere = CollisionSphere(0, 0, 0, 3.5)
        colSphere.setTangible(0)
        colNode = CollisionNode('targetSphere')
        colNode.addSolid(colSphere)
        colSphereNode = self.geom.attachNewNode(colNode)
        self.accept('hitTarget', self.handleHitTarget)
        self.accept('missedTarget', self.handleMissedTarget)
        self.accept('f3-up', self.handleHitTarget)
        self.accept('entertargetSphere', self.handleEnterTarget)

    
    def delete(self):
        self.ignoreAll()
        self.scoreNode.removeNode()
        del self.scoreNode
        self.geom.removeNode()
        del self.geom
        self.timer.destroy()
        del self.timer
        del self.rewardSound
        del self.hitSound
        DistributedObject.DistributedObject.delete(self)

    
    def setState(self, enabled, score, time):
        self.enabled = enabled
        if enabled:
            self.geom.setColor(0, 1, 0)
        else:
            self.geom.setColor(1, 0, 0)
            self.timer.hide()
        if score != self.score:
            self.setLevel(score)
        
        if time != self.hitTime:
            self.setTimer(time)
        

    
    def setReward(self, reward):
        base.playSfx(self.rewardSound)

    
    def handleEnterTarget(self, collEntry):
        self.handleHitTarget()

    
    def handleHitTarget(self, avId = None, vel = None):
        if not avId:
            avId = base.localAvatar.doId
        
        if self.enabled:
            self.sendUpdate('setResult', [
                avId])
        
        if vel:
            if self.targetBounceTrack:
                self.targetBounceTrack.finish()
            
            pos = self.geom.getPos()
            dist = Vec3(vel)
            dist.normalize()
            newPos = pos - dist * 1.5
            springPos = pos + dist
            self.notify.debug('reaction distance = %s,%s,%s' % (vel[0], vel[1], vel[2]))
            self.targetBounceTrack = Sequence(LerpPosInterval(node = self.geom, duration = 0.10000000000000001, pos = newPos, blendType = 'easeOut'), LerpPosInterval(node = self.geom, duration = 0.25, pos = springPos, blendType = 'easeOut'), LerpPosInterval(node = self.geom, duration = 0.20000000000000001, pos = pos, blendType = 'easeOut'))
            self.targetBounceTrack.start()
        

    
    def handleMissedTarget(self):
        if self.enabled:
            self.sendUpdate('setResult', [
                0])
        

    
    def handleHitCloud(self):
        if self.enabled:
            self.sendUpdate('setBonus', [
                0.5])
        

    
    def setLevel(self, level):
        self.notify.debug('setLevel(%s)' % level)
        self.score = level
        base.playSfx(self.hitSound)
        self.scoreText.setText('+' + str(self.score))

    
    def setTimer(self, time):
        self.hitTime = time
        self.notify.debug('updateTimer(%s)' % self.enabled)
        if self.enabled:
            self.timer.show()
            self.notify.debug('hitTime = %s' % self.hitTime)
            self.timer.setTime(self.hitTime)
            self.timer.countdown(self.hitTime)
        

    
    def setPosition(self, x, y, z):
        self.geom.setPos(x, y, z)


