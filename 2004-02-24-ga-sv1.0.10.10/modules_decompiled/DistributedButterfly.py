# File: D (Python 2.2)

from ShowBaseGlobal import *
from PandaObject import *
from ClockDelta import *
from IntervalGlobal import *
import DirectNotifyGlobal
import DistributedObject
import FSM
import State
import NodePath
import Mopath
import ToontownGlobals
import Actor
import ButterflyGlobals
import RandomNumGen
import random

class DistributedButterfly(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedButterfly')
    id = 0
    wingTypes = ('wings_1', 'wings_2', 'wings_3', 'wings_4', 'wings_5', 'wings_6')
    yellowColors = (Vec4(1, 1, 1, 1), Vec4(0.20000000000000001, 0, 1, 1), Vec4(0.80000000000000004, 0, 1, 1))
    whiteColors = (Vec4(0.80000000000000004, 0, 0.80000000000000004, 1), Vec4(0, 0.80000000000000004, 0.80000000000000004, 1), Vec4(0.90000000000000002, 0.40000000000000002, 0.59999999999999998, 1), Vec4(0.90000000000000002, 0.40000000000000002, 0.40000000000000002, 1), Vec4(0.80000000000000004, 0.5, 0.90000000000000002, 1), Vec4(0.40000000000000002, 0.10000000000000001, 0.69999999999999996, 1))
    paleYellowColors = (Vec4(0.80000000000000004, 0, 0.80000000000000004, 1), Vec4(0.59999999999999998, 0.59999999999999998, 0.90000000000000002, 1), Vec4(0.69999999999999996, 0.59999999999999998, 0.90000000000000002, 1), Vec4(0.80000000000000004, 0.59999999999999998, 0.90000000000000002, 1), Vec4(0.90000000000000002, 0.59999999999999998, 0.90000000000000002, 1), Vec4(1, 0.59999999999999998, 0.90000000000000002, 1))
    shadowScaleBig = Point3(0.070000000000000007, 0.070000000000000007, 0.070000000000000007)
    shadowScaleSmall = Point3(0.01, 0.01, 0.01)
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.fsm = FSM.FSM('DistributedButterfly', [
            State.State('off', self.enterOff, self.exitOff, [
                'Flying',
                'Landed']),
            State.State('Flying', self.enterFlying, self.exitFlying, [
                'Landed']),
            State.State('Landed', self.enterLanded, self.exitLanded, [
                'Flying'])], 'off', 'off')
        self.butterfly = None
        self.butterflyNode = None
        self.curIndex = 0
        self.destIndex = 0
        self.time = 0.0
        self.ival = None
        self.fsm.enterInitialState()

    
    def generate(self):
        if self.butterfly:
            return None
        
        self.butterfly = Actor.Actor()
        self.butterfly.loadModel('phase_4/models/props/SZ_butterfly-mod.bam')
        self.butterfly.loadAnims({
            'flutter': 'phase_4/models/props/SZ_butterfly-flutter.bam',
            'glide': 'phase_4/models/props/SZ_butterfly-glide.bam',
            'land': 'phase_4/models/props/SZ_butterfly-land.bam' })
        index = self.doId % len(self.wingTypes)
        chosenType = self.wingTypes[index]
        node = self.butterfly.getGeomNode()
        for type in self.wingTypes:
            wing = node.find('**/' + type)
            if type != chosenType:
                wing.removeNode()
            elif index == 0 or index == 1:
                color = self.yellowColors[self.doId % len(self.yellowColors)]
            elif index == 2 or index == 3:
                color = self.whiteColors[self.doId % len(self.whiteColors)]
            elif index == 4:
                color = self.paleYellowColors[self.doId % len(self.paleYellowColors)]
            else:
                color = Vec4(1, 1, 1, 1)
            wing.setColor(color)
        
        self.butterfly2 = Actor.Actor(other = self.butterfly)
        self.butterfly.enableBlend(blendType = PartBundle.BTLinear)
        self.butterfly.loop('flutter')
        self.butterfly.loop('land')
        self.butterfly.loop('glide')
        rng = RandomNumGen.RandomNumGen(self.doId)
        playRate = 0.59999999999999998 + 0.80000000000000004 * rng.random()
        self.butterfly.setPlayRate(playRate, 'flutter')
        self.butterfly.setPlayRate(playRate, 'land')
        self.butterfly.setPlayRate(playRate, 'glide')
        self.butterfly2.setPlayRate(playRate, 'flutter')
        self.butterfly2.setPlayRate(playRate, 'land')
        self.butterfly2.setPlayRate(playRate, 'glide')
        self.glideWeight = rng.random() * 2
        lodNode = LODNode('butterfly-node')
        lodNode.addSwitch(100, 40)
        lodNode.addSwitch(40, 0)
        self.butterflyNode = NodePath.NodePath(lodNode)
        self.butterfly2.setH(180.0)
        self.butterfly2.reparentTo(self.butterflyNode)
        self.butterfly.setH(180.0)
        self.butterfly.reparentTo(self.butterflyNode)
        self._DistributedButterfly__initCollisions()
        self.dropShadow = loader.loadModelCopy('phase_3/models/props/drop_shadow')
        self.dropShadow.setColor(0, 0, 0, 0.29999999999999999)
        self.dropShadow.setPos(0, 0.10000000000000001, -0.050000000000000003)
        self.dropShadow.setScale(self.shadowScaleBig)
        self.dropShadow.reparentTo(self.butterfly)

    
    def disable(self):
        self.butterflyNode.reparentTo(hidden)
        if self.ival != None:
            self.ival.finish()
        
        self._DistributedButterfly__ignoreAvatars()
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        self.butterfly = None
        self.butterfly2 = None
        self.butterflyNode.removeNode()
        self._DistributedButterfly__deleteCollisions()
        self.ival = None
        del self.fsm
        DistributedObject.DistributedObject.delete(self)

    
    def uniqueButterflyName(self, name):
        DistributedButterfly.id += 1
        return name + '-%d' % DistributedButterfly.id

    
    def _DistributedButterfly__detectAvatars(self):
        self.accept('enter' + self.cSphereNode.getName(), self._DistributedButterfly__handleCollisionSphereEnter)

    
    def _DistributedButterfly__ignoreAvatars(self):
        self.ignore('enter' + self.cSphereNode.getName())

    
    def _DistributedButterfly__initCollisions(self):
        self.cSphere = CollisionSphere(0.0, 1.0, 0.0, 3.0)
        self.cSphere.setTangible(0)
        self.cSphereNode = CollisionNode(self.uniqueButterflyName('cSphereNode'))
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.butterflyNode.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereNode.setCollideMask(ToontownGlobals.WallBitmask)

    
    def _DistributedButterfly__deleteCollisions(self):
        del self.cSphere
        del self.cSphereNode
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath

    
    def _DistributedButterfly__handleCollisionSphereEnter(self, collEntry):
        self.sendUpdate('avatarEnter', [])

    
    def setArea(self, playground, area):
        self.playground = playground
        self.area = area

    
    def setState(self, stateIndex, curIndex, destIndex, time, timestamp):
        self.curIndex = curIndex
        self.destIndex = destIndex
        self.time = time
        self.fsm.request(ButterflyGlobals.states[stateIndex], [
            globalClockDelta.localElapsedTime(timestamp)])

    
    def enterOff(self, ts = 0.0):
        if self.butterflyNode != None:
            self.butterflyNode.reparentTo(hidden)
        
        return None

    
    def exitOff(self):
        if self.butterflyNode != None:
            self.butterflyNode.reparentTo(render)
        
        return None

    
    def enterFlying(self, ts):
        self._DistributedButterfly__detectAvatars()
        curPos = ButterflyGlobals.ButterflyPoints[self.playground][self.area][self.curIndex]
        destPos = ButterflyGlobals.ButterflyPoints[self.playground][self.area][self.destIndex]
        flyHeight = max(curPos[2], destPos[2]) + ButterflyGlobals.BUTTERFLY_HEIGHT[self.playground]
        curPosHigh = Point3(curPos[0], curPos[1], flyHeight)
        destPosHigh = Point3(destPos[0], destPos[1], flyHeight)
        if ts <= self.time:
            flyTime = self.time - ButterflyGlobals.BUTTERFLY_TAKEOFF[self.playground] + ButterflyGlobals.BUTTERFLY_LANDING[self.playground]
            self.butterflyNode.setPos(curPos)
            self.dropShadow.show()
            self.dropShadow.setScale(self.shadowScaleBig)
            oldHpr = self.butterflyNode.getHpr()
            self.butterflyNode.headsUp(destPos)
            newHpr = self.butterflyNode.getHpr()
            self.butterflyNode.setHpr(oldHpr)
            takeoffShadowT = 0.20000000000000001 * ButterflyGlobals.BUTTERFLY_TAKEOFF[self.playground]
            landShadowT = 0.20000000000000001 * ButterflyGlobals.BUTTERFLY_LANDING[self.playground]
            self.butterfly2.loop('flutter')
            self.ival = Sequence(Parallel(LerpPosHprInterval(self.butterflyNode, ButterflyGlobals.BUTTERFLY_TAKEOFF[self.playground], curPosHigh, newHpr), LerpAnimInterval(self.butterfly, ButterflyGlobals.BUTTERFLY_TAKEOFF[self.playground], 'land', 'flutter'), LerpAnimInterval(self.butterfly, ButterflyGlobals.BUTTERFLY_TAKEOFF[self.playground], None, 'glide', startWeight = 0, endWeight = self.glideWeight), Sequence(LerpScaleInterval(self.dropShadow, takeoffShadowT, self.shadowScaleSmall, startScale = self.shadowScaleBig), HideInterval(self.dropShadow))), LerpPosInterval(self.butterflyNode, flyTime, destPosHigh), Parallel(LerpPosInterval(self.butterflyNode, ButterflyGlobals.BUTTERFLY_LANDING[self.playground], destPos), LerpAnimInterval(self.butterfly, ButterflyGlobals.BUTTERFLY_LANDING[self.playground], 'flutter', 'land'), LerpAnimInterval(self.butterfly, ButterflyGlobals.BUTTERFLY_LANDING[self.playground], None, 'glide', startWeight = self.glideWeight, endWeight = 0), Sequence(Wait(ButterflyGlobals.BUTTERFLY_LANDING[self.playground] - landShadowT), ShowInterval(self.dropShadow), LerpScaleInterval(self.dropShadow, landShadowT, self.shadowScaleBig, startScale = self.shadowScaleSmall))), name = self.uniqueName('Butterfly'))
            self.ival.start(ts)
        else:
            self.ival = None
            self.butterflyNode.setPos(destPos)
            self.butterfly.setControlEffect('land', 1.0)
            self.butterfly.setControlEffect('flutter', 0.0)
            self.butterfly.setControlEffect('glide', 0.0)
            self.butterfly2.loop('land')
        return None

    
    def exitFlying(self):
        self._DistributedButterfly__ignoreAvatars()
        if self.ival != None:
            self.ival.finish()
            self.ival = None
        
        return None

    
    def enterLanded(self, ts):
        self._DistributedButterfly__detectAvatars()
        curPos = ButterflyGlobals.ButterflyPoints[self.playground][self.area][self.curIndex]
        self.butterflyNode.setPos(curPos)
        self.dropShadow.show()
        self.dropShadow.setScale(self.shadowScaleBig)
        self.butterfly.setControlEffect('land', 1.0)
        self.butterfly.setControlEffect('flutter', 0.0)
        self.butterfly.setControlEffect('glide', 0.0)
        self.butterfly2.pose('land', random.randrange(self.butterfly2.getNumFrames('land')))
        return None

    
    def exitLanded(self):
        self._DistributedButterfly__ignoreAvatars()
        return None


