# File: D (Python 2.2)

from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from direct.fsm import FSM
from direct.distributed import DistributedObject
from direct.showutil import Rope
from direct.showbase import PythonUtil
from direct.task import Task
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals

class DistributedCashbotBossCrane(DistributedObject.DistributedObject, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCashbotBossCrane')
    firstMagnetBit = 21
    craneMinY = 8
    craneMaxY = 25
    armMinH = -45
    armMaxH = 45
    shadowOffset = 1
    emptyFrictionCoef = 0.10000000000000001
    emptySlideSpeed = 10
    emptyRotateSpeed = 20
    lookAtPoint = Point3(0.29999999999999999, 0, 0.10000000000000001)
    lookAtUp = Vec3(0, -1, 0)
    neutralStickHinge = VBase3(0, 90, 0)
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        FSM.FSM.__init__(self, 'DistributedCashbotBossCrane')
        self.boss = None
        self.index = None
        self.avId = 0
        self.cableLength = 20
        self.numLinks = 3
        self.initialArmPosition = (0, 20, 0)
        self.slideSpeed = self.emptySlideSpeed
        self.rotateSpeed = self.emptyRotateSpeed
        self.changeSeq = 0
        self.lastChangeSeq = 0
        self.moveSound = None
        self.links = []
        self.activeLinks = []
        self.collisions = NodePathCollection()
        self.physicsActivated = 0
        self.snifferActivated = 0
        self.magnetOn = 0
        self.root = NodePath('root')
        self.hinge = self.root.attachNewNode('hinge')
        self.hinge.setPos(0, -17.600000000000001, 38.5)
        self.controls = self.root.attachNewNode('controls')
        self.controls.setPos(0, -4.9000000000000004, 0)
        self.arm = self.hinge.attachNewNode('arm')
        self.crane = self.arm.attachNewNode('crane')
        self.cable = self.hinge.attachNewNode('cable')
        self.topLink = self.crane.attachNewNode('topLink')
        self.topLink.setPos(0, 0, -1)
        self.shadow = None
        self.p0 = Point3(0, 0, 0)
        self.v1 = Vec3(1, 1, 1)
        self.armSmoother = SmoothMover()
        self.linkSmoothers = []
        self.smoothStarted = 0
        self._DistributedCashbotBossCrane__broadcastPeriod = 0.20000000000000001
        self.cable.node().setFinal(1)
        self.crane.setPos(*self.initialArmPosition)
        self.heldObject = None
        self.closeButton = None
        self.craneAdviceLabel = None
        self.magnetAdviceLabel = None
        self.atLimitSfx = base.loadSfx('phase_4/audio/sfx/MG_cannon_adjust.mp3')
        self.magnetOnSfx = base.loadSfx('phase_10/audio/sfx/CBHQ_CFO_magnet_on.mp3')
        self.magnetLoopSfx = base.loadSfx('phase_10/audio/sfx/CBHQ_CFO_magnet_loop.wav')
        self.magnetSoundInterval = Parallel(SoundInterval(self.magnetOnSfx), Sequence(Wait(0.5), Func(base.playSfx, self.magnetLoopSfx, looping = 1)))
        self.craneMoveSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_elevator_up_down.mp3')
        self.fadeTrack = None

    
    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.name = 'crane-%s' % self.doId
        self.root.setName(self.name)
        self.root.setPosHpr(*ToontownGlobals.CashbotBossCranePosHprs[self.index])
        self.rotateLinkName = self.uniqueName('rotateLink')
        self.snifferEvent = self.uniqueName('sniffer')
        self.triggerName = self.uniqueName('trigger')
        self.triggerEvent = 'enter%s' % self.triggerName
        self.shadowName = self.uniqueName('shadow')
        self.flickerName = self.uniqueName('flicker')
        self.smoothName = self.uniqueName('craneSmooth')
        self.posHprBroadcastName = self.uniqueName('craneBroadcast')
        self.craneAdviceName = self.uniqueName('craneAdvice')
        self.magnetAdviceName = self.uniqueName('magnetAdvice')
        self.controlModel = self.boss.controls.copyTo(self.controls)
        self.cc = NodePath('cc')
        column = self.controlModel.find('**/column')
        column.getChildren().reparentTo(self.cc)
        self.cc.reparentTo(column)
        self.stickHinge = self.cc.attachNewNode('stickHinge')
        self.stick = self.boss.stick.copyTo(self.stickHinge)
        self.stickHinge.setHpr(self.neutralStickHinge)
        self.stick.setHpr(0, -90, 0)
        self.stick.flattenLight()
        self.bottom = self.controlModel.find('**/bottom')
        self.bottom.wrtReparentTo(self.cc)
        self.bottomPos = self.bottom.getPos()
        cs = CollisionSphere(0, -5, -2, 3)
        cs.setTangible(0)
        cn = CollisionNode(self.triggerName)
        cn.addSolid(cs)
        cn.setIntoCollideMask(OTPGlobals.WallBitmask)
        self.trigger = self.root.attachNewNode(cn)
        self.trigger.stash()
        cs = CollisionTube(0, 2.7000000000000002, 0, 0, 2.7000000000000002, 3, 1.2)
        cn = CollisionNode('tube')
        cn.addSolid(cs)
        cn.setIntoCollideMask(OTPGlobals.WallBitmask)
        self.tube = self.controlModel.attachNewNode(cn)
        cs = CollisionSphere(0, 0, 2, 3)
        cn = CollisionNode('safetyBubble')
        cn.addSolid(cs)
        cn.setIntoCollideMask(OTPGlobals.PieBitmask)
        self.controls.attachNewNode(cn)
        arm = self.boss.craneArm.copyTo(self.crane)
        self.boss.cranes[self.index] = self

    
    def disable(self):
        DistributedObject.DistributedObject.disable(self)
        del self.boss.cranes[self.index]
        self.cleanup()

    
    def cleanup(self):
        if self.state != 'Off':
            self.demand('Off')
        
        self.boss = None

    
    def accomodateToon(self, toon):
        origScale = self.controlModel.getSz()
        origCcPos = self.cc.getPos()
        origBottomPos = self.bottom.getPos()
        origStickHingeHpr = self.stickHinge.getHpr()
        scale = toon.getGeomNode().getChild(0).getSz(render)
        self.controlModel.setScale(scale)
        self.cc.setPos(0, 0, 0)
        toon.setPosHpr(self.controls, 0, 0, 0, 0, 0, 0)
        toon.pose('leverNeutral', 0)
        toon.update()
        pos = toon.rightHand.getPos(self.cc)
        self.cc.setPos(pos[0], pos[1], pos[2] - 1)
        self.bottom.setZ(toon, 0.0)
        self.bottom.setPos(self.bottomPos[0], self.bottomPos[1], self.bottom.getZ())
        self.stickHinge.lookAt(toon.rightHand, self.lookAtPoint, self.lookAtUp)
        lerpTime = 0.5
        return Parallel(self.controlModel.scaleInterval(lerpTime, scale, origScale, blendType = 'easeInOut'), self.cc.posInterval(lerpTime, self.cc.getPos(), origCcPos, blendType = 'easeInOut'), self.bottom.posInterval(lerpTime, self.bottom.getPos(), origBottomPos, blendType = 'easeInOut'), self.stickHinge.quatInterval(lerpTime, self.stickHinge.getHpr(), origStickHingeHpr, blendType = 'easeInOut'))

    
    def getRestoreScaleInterval(self):
        lerpTime = 1
        return Parallel(self.controlModel.scaleInterval(lerpTime, 1, blendType = 'easeInOut'), self.cc.posInterval(lerpTime, Point3(0, 0, 0), blendType = 'easeInOut'), self.bottom.posInterval(lerpTime, self.bottomPos, blendType = 'easeInOut'), self.stickHinge.quatInterval(lerpTime, self.neutralStickHinge, blendType = 'easeInOut'))

    
    def makeToonGrabInterval(self, toon):
        origPos = toon.getPos()
        origHpr = toon.getHpr()
        a = self.accomodateToon(toon)
        newPos = toon.getPos()
        newHpr = toon.getHpr()
        origHpr.setX(PythonUtil.fitSrcAngle2Dest(origHpr[0], newHpr[0]))
        toon.setPosHpr(origPos, origHpr)
        walkTime = 0.20000000000000001
        reach = ActorInterval(toon, 'leverReach')
        if reach.getDuration() < walkTime:
            reach = Sequence(ActorInterval(toon, 'walk', loop = 1, duration = walkTime - reach.getDuration()), reach)
        
        i = Sequence(Parallel(toon.posInterval(walkTime, newPos, origPos), toon.hprInterval(walkTime, newHpr, origHpr), reach), Func(self.startWatchJoystick, toon))
        i = Parallel(i, a)
        return i

    
    def _DistributedCashbotBossCrane__toonPlayWithCallback(self, animName, numFrames):
        duration = numFrames / 24.0
        self.toon.play(animName)
        taskMgr.doMethodLater(duration, self._DistributedCashbotBossCrane__toonPlayCallback, self.uniqueName('toonPlay'))

    
    def _DistributedCashbotBossCrane__toonPlayCallback(self, task):
        if self.changeSeq == self.lastChangeSeq:
            self._DistributedCashbotBossCrane__toonPlayWithCallback('leverNeutral', 40)
        else:
            self._DistributedCashbotBossCrane__toonPlayWithCallback('leverPull', 40)
            self.lastChangeSeq = self.changeSeq

    
    def startWatchJoystick(self, toon):
        self.toon = toon
        taskMgr.add(self._DistributedCashbotBossCrane__watchJoystick, self.uniqueName('watchJoystick'))
        self._DistributedCashbotBossCrane__toonPlayWithCallback('leverNeutral', 40)
        self.accept(toon.uniqueName('disable'), self._DistributedCashbotBossCrane__handleUnexpectedExit, extraArgs = [
            toon.doId])

    
    def stopWatchJoystick(self):
        taskMgr.remove(self.uniqueName('toonPlay'))
        taskMgr.remove(self.uniqueName('watchJoystick'))
        if self.toon:
            self.ignore(self.toon.uniqueName('disable'))
        
        self.toon = None

    
    def _DistributedCashbotBossCrane__watchJoystick(self, task):
        self.toon.setPosHpr(self.controls, 0, 0, 0, 0, 0, 0)
        self.toon.update()
        self.stickHinge.lookAt(self.toon.rightHand, self.lookAtPoint, self.lookAtUp)
        return Task.cont

    
    def _DistributedCashbotBossCrane__handleUnexpectedExit(self, toonId):
        self.notify.warning('%s: unexpected exit for %s' % (self.doId, toonId))
        if self.toon and self.toon.doId == toonId:
            self.stopWatchJoystick()
        

    
    def _DistributedCashbotBossCrane__activatePhysics(self):
        if not (self.physicsActivated):
            for (an, anp, cnp) in self.activeLinks:
                self.boss.physicsMgr.attachPhysicalNode(an)
                base.cTrav.addCollider(cnp, self.handler)
            
            self.collisions.unstash()
            self.physicsActivated = 1
        

    
    def _DistributedCashbotBossCrane__deactivatePhysics(self):
        if self.physicsActivated:
            for (an, anp, cnp) in self.activeLinks:
                self.boss.physicsMgr.removePhysicalNode(an)
                base.cTrav.removeCollider(cnp)
            
            self.collisions.stash()
            self.physicsActivated = 0
        

    
    def _DistributedCashbotBossCrane__straightenCable(self):
        for linkNum in range(self.numLinks):
            (an, anp, cnp) = self.activeLinks[linkNum]
            an.getPhysicsObject().setVelocity(0, 0, 0)
            z = (float(linkNum + 1) / float(self.numLinks)) * self.cableLength
            anp.setPos(self.crane.getPos(self.cable))
            anp.setZ(-z)
        

    
    def setCableLength(self, length):
        self.cableLength = length
        linkWidth = float(length) / float(self.numLinks)
        self.shell.setRadius(linkWidth + 1)

    
    def setupCable(self):
        activated = self.physicsActivated
        self.clearCable()
        self.handler = PhysicsCollisionHandler()
        self.handler.setStaticFrictionCoef(0.10000000000000001)
        self.handler.setDynamicFrictionCoef(self.emptyFrictionCoef)
        linkWidth = float(self.cableLength) / float(self.numLinks)
        self.shell = CollisionInvSphere(0, 0, 0, linkWidth + 1)
        self.links = []
        self.links.append((self.topLink, Point3(0, 0, 0)))
        anchor = self.topLink
        for linkNum in range(self.numLinks):
            anchor = self._DistributedCashbotBossCrane__makeLink(anchor, linkNum)
        
        self.collisions.stash()
        self.bottomLink = self.links[-1][0]
        self.middleLink = self.links[-2][0]
        self.magnet = self.bottomLink.attachNewNode('magnet')
        self.wiggleMagnet = self.magnet.attachNewNode('wiggleMagnet')
        taskMgr.add(self._DistributedCashbotBossCrane__rotateMagnet, self.rotateLinkName)
        magnetModel = self.boss.magnet.copyTo(self.wiggleMagnet)
        magnetModel.setHpr(90, 45, 90)
        self.gripper = magnetModel.attachNewNode('gripper')
        self.gripper.setPos(0, 0, -4)
        cn = CollisionNode('sniffer')
        self.sniffer = magnetModel.attachNewNode(cn)
        self.sniffer.stash()
        cs = CollisionSphere(0, 0, -10, 6)
        cs.setTangible(0)
        cn.addSolid(cs)
        cn.setIntoCollideMask(BitMask32(0))
        cn.setFromCollideMask(ToontownGlobals.CashbotBossObjectBitmask)
        self.snifferHandler = CollisionHandlerEvent()
        self.snifferHandler.addInPattern(self.snifferEvent)
        self.snifferHandler.addAgainPattern(self.snifferEvent)
        rope = self.makeSpline()
        rope.reparentTo(self.cable)
        rope.setTexture(self.boss.cableTex)
        ts = TextureStage.getDefault()
        rope.setTexScale(ts, 0.14999999999999999, 0.13)
        rope.setTexOffset(ts, 0.82999999999999996, 0.01)
        if activated:
            self._DistributedCashbotBossCrane__activatePhysics()
        

    
    def clearCable(self):
        self._DistributedCashbotBossCrane__deactivatePhysics()
        taskMgr.remove(self.rotateLinkName)
        self.links = []
        self.activeLinks = []
        self.linkSmoothers = []
        self.collisions.clear()
        self.cable.getChildren().detach()
        self.topLink.getChildren().detach()
        self.gripper = None

    
    def makeSpline(self):
        rope = Rope.Rope()
        rope.setup(min(len(self.links), 4), self.links)
        rope.curve.normalizeKnots()
        rn = rope.ropeNode
        rn.setRenderMode(RopeNode.RMTube)
        rn.setNumSlices(3)
        rn.setTubeUp(Vec3(0, -1, 0))
        rn.setUvMode(RopeNode.UVParametric)
        rn.setUvDirection(1)
        rn.setThickness(0.5)
        return rope

    
    def startShadow(self):
        self.shadow = self.boss.geom.attachNewNode('%s-shadow' % self.name)
        self.shadow.setColor(1, 1, 1, 0.29999999999999999)
        self.shadow.setDepthWrite(0)
        self.shadow.setTransparency(1)
        self.shadow.setBin('shadow', 0)
        self.shadow.node().setFinal(1)
        self.magnetShadow = loader.loadModelCopy('phase_3/models/props/drop_shadow')
        self.magnetShadow.reparentTo(self.shadow)
        self.craneShadow = loader.loadModelCopy('phase_3/models/props/square_drop_shadow')
        self.craneShadow.setScale(0.5, 4, 1)
        self.craneShadow.setPos(0, -12, 0)
        self.craneShadow.flattenLight()
        self.craneShadow.reparentTo(self.shadow)
        taskMgr.add(self._DistributedCashbotBossCrane__followShadow, self.shadowName)
        rope = self.makeSpline()
        rope.reparentTo(self.shadow)
        rope.setColor(1, 1, 1, 0.20000000000000001)
        tex = self.craneShadow.findTexture('*')
        rope.setTexture(tex)
        rn = rope.ropeNode
        rn.setRenderMode(RopeNode.RMTape)
        rn.setNumSubdiv(6)
        rn.setThickness(0.80000000000000004)
        rn.setTubeUp(Vec3(0, 0, 1))
        rn.setMatrix(Mat4.translateMat(0, 0, self.shadowOffset) * Mat4.scaleMat(1, 1, 0.01))

    
    def stopShadow(self):
        if self.shadow:
            self.shadow.removeNode()
            self.shadow = None
            self.magnetShadow = None
            self.craneShadow = None
        
        taskMgr.remove(self.shadowName)

    
    def _DistributedCashbotBossCrane__followShadow(self, task):
        p = self.magnet.getPos(self.boss.geom)
        self.magnetShadow.setPos(p[0], p[1], self.shadowOffset)
        self.craneShadow.setPosHpr(self.crane, 0, 0, 0, 0, 0, 0)
        self.craneShadow.setZ(self.shadowOffset)
        return Task.cont

    
    def _DistributedCashbotBossCrane__makeLink(self, anchor, linkNum):
        an = ActorNode('link%s' % linkNum)
        anp = NodePath(an)
        cn = CollisionNode('cn')
        sphere = CollisionSphere(0, 0, 0, 1)
        cn.addSolid(sphere)
        cnp = anp.attachNewNode(cn)
        self.handler.addCollider(cnp, anp)
        self.activeLinks.append((an, anp, cnp))
        self.linkSmoothers.append(SmoothMover())
        anp.reparentTo(self.cable)
        z = (float(linkNum + 1) / float(self.numLinks)) * self.cableLength
        anp.setPos(self.crane.getPos())
        anp.setZ(-z)
        mask = BitMask32.bit(self.firstMagnetBit + linkNum)
        cn.setFromCollideMask(mask)
        cn.setIntoCollideMask(BitMask32(0))
        shellNode = CollisionNode('shell%s' % linkNum)
        shellNode.addSolid(self.shell)
        shellNP = anchor.attachNewNode(shellNode)
        shellNode.setIntoCollideMask(mask)
        self.collisions.addPath(shellNP)
        self.collisions.addPath(cnp)
        self.links.append((anp, Point3(0, 0, 0)))
        return anp

    
    def _DistributedCashbotBossCrane__rotateMagnet(self, task):
        self.magnet.lookAt(self.middleLink, self.p0, self.v1)
        return Task.cont

    
    def _DistributedCashbotBossCrane__enableControlInterface(self):
        gui = loader.loadModelOnce('phase_3.5/models/gui/avatar_panel_gui')
        self.closeButton = DirectButton(image = (gui.find('**/CloseBtn_UP'), gui.find('**/CloseBtn_DN'), gui.find('**/CloseBtn_Rllvr'), gui.find('**/CloseBtn_UP')), relief = None, scale = 2, text = 'Leave crane', text_scale = 0.040000000000000001, text_pos = (0, -0.070000000000000007), text_fg = VBase4(1, 1, 1, 1), pos = (1.05, 0, -0.81999999999999995), command = self._DistributedCashbotBossCrane__exitCrane)
        self.accept('escape', self._DistributedCashbotBossCrane__exitCrane)
        self.accept('control', self._DistributedCashbotBossCrane__controlPressed)
        self.accept('control-up', self._DistributedCashbotBossCrane__controlReleased)
        self.accept('InputState-forward', self._DistributedCashbotBossCrane__upArrow)
        self.accept('InputState-reverse', self._DistributedCashbotBossCrane__downArrow)
        self.accept('InputState-turnLeft', self._DistributedCashbotBossCrane__leftArrow)
        self.accept('InputState-turnRight', self._DistributedCashbotBossCrane__rightArrow)
        taskMgr.add(self._DistributedCashbotBossCrane__watchControls, 'watchCraneControls')
        taskMgr.doMethodLater(5, self._DistributedCashbotBossCrane__displayCraneAdvice, self.craneAdviceName)
        taskMgr.doMethodLater(10, self._DistributedCashbotBossCrane__displayMagnetAdvice, self.magnetAdviceName)
        NametagGlobals.setOnscreenChatForced(1)
        self.arrowVert = 0
        self.arrowHorz = 0

    
    def _DistributedCashbotBossCrane__disableControlInterface(self):
        self._DistributedCashbotBossCrane__turnOffMagnet()
        if self.closeButton:
            self.closeButton.destroy()
            self.closeButton = None
        
        self._DistributedCashbotBossCrane__cleanupCraneAdvice()
        self._DistributedCashbotBossCrane__cleanupMagnetAdvice()
        self.ignore('escape')
        self.ignore('control')
        self.ignore('control-up')
        self.ignore('InputState-forward')
        self.ignore('InputState-reverse')
        self.ignore('InputState-turnLeft')
        self.ignore('InputState-turnRight')
        self.arrowVert = 0
        self.arrowHorz = 0
        NametagGlobals.setOnscreenChatForced(0)
        taskMgr.remove('watchCraneControls')
        self._DistributedCashbotBossCrane__setMoveSound(None)

    
    def _DistributedCashbotBossCrane__displayCraneAdvice(self, task):
        if self.craneAdviceLabel == None:
            self.craneAdviceLabel = DirectLabel(text = 'Use the arrow keys to move the overhead crane.', text_fg = VBase4(1, 1, 1, 1), text_align = TextNode.ACenter, relief = None, pos = (0, 0, 0.68999999999999995), scale = 0.10000000000000001)
        

    
    def _DistributedCashbotBossCrane__cleanupCraneAdvice(self):
        if self.craneAdviceLabel:
            self.craneAdviceLabel.destroy()
            self.craneAdviceLabel = None
        
        taskMgr.remove(self.craneAdviceName)

    
    def _DistributedCashbotBossCrane__displayMagnetAdvice(self, task):
        if self.magnetAdviceLabel == None:
            self.magnetAdviceLabel = DirectLabel(text = 'Hold down the control key to pick things up.', text_fg = VBase4(1, 1, 1, 1), text_align = TextNode.ACenter, relief = None, pos = (0, 0, 0.55000000000000004), scale = 0.10000000000000001)
        

    
    def _DistributedCashbotBossCrane__cleanupMagnetAdvice(self):
        if self.magnetAdviceLabel:
            self.magnetAdviceLabel.destroy()
            self.magnetAdviceLabel = None
        
        taskMgr.remove(self.magnetAdviceName)

    
    def _DistributedCashbotBossCrane__watchControls(self, task):
        if self.arrowHorz or self.arrowVert:
            self._DistributedCashbotBossCrane__moveCraneArcHinge(self.arrowHorz, self.arrowVert)
        else:
            self._DistributedCashbotBossCrane__setMoveSound(None)
        return Task.cont

    
    def _DistributedCashbotBossCrane__exitCrane(self):
        if self.closeButton:
            self.closeButton.destroy()
            self.closeButton = DirectLabel(relief = None, text = 'Leaving crane', pos = (1.05, 0, -0.88), text_pos = (0, 0), text_scale = 0.059999999999999998, text_fg = VBase4(1, 1, 1, 1))
        
        self._DistributedCashbotBossCrane__cleanupCraneAdvice()
        self._DistributedCashbotBossCrane__cleanupMagnetAdvice()
        self.d_requestFree()

    
    def _DistributedCashbotBossCrane__incrementChangeSeq(self):
        self.changeSeq = self.changeSeq + 1 & 255

    
    def _DistributedCashbotBossCrane__controlPressed(self):
        self._DistributedCashbotBossCrane__cleanupMagnetAdvice()
        self._DistributedCashbotBossCrane__turnOnMagnet()

    
    def _DistributedCashbotBossCrane__controlReleased(self):
        self._DistributedCashbotBossCrane__turnOffMagnet()

    
    def _DistributedCashbotBossCrane__turnOnMagnet(self):
        if not (self.magnetOn):
            self._DistributedCashbotBossCrane__incrementChangeSeq()
            self.magnetOn = 1
            if not (self.heldObject):
                self._DistributedCashbotBossCrane__activateSniffer()
            
        

    
    def _DistributedCashbotBossCrane__turnOffMagnet(self):
        if self.magnetOn:
            self.magnetOn = 0
            self._DistributedCashbotBossCrane__deactivateSniffer()
            self.releaseObject()
        

    
    def _DistributedCashbotBossCrane__upArrow(self, pressed):
        self._DistributedCashbotBossCrane__incrementChangeSeq()
        self._DistributedCashbotBossCrane__cleanupCraneAdvice()
        if pressed:
            self.arrowVert = 1
        elif self.arrowVert > 0:
            self.arrowVert = 0
        

    
    def _DistributedCashbotBossCrane__downArrow(self, pressed):
        self._DistributedCashbotBossCrane__incrementChangeSeq()
        self._DistributedCashbotBossCrane__cleanupCraneAdvice()
        if pressed:
            self.arrowVert = -1
        elif self.arrowVert < 0:
            self.arrowVert = 0
        

    
    def _DistributedCashbotBossCrane__rightArrow(self, pressed):
        self._DistributedCashbotBossCrane__incrementChangeSeq()
        self._DistributedCashbotBossCrane__cleanupCraneAdvice()
        if pressed:
            self.arrowHorz = 1
        elif self.arrowHorz > 0:
            self.arrowHorz = 0
        

    
    def _DistributedCashbotBossCrane__leftArrow(self, pressed):
        self._DistributedCashbotBossCrane__incrementChangeSeq()
        self._DistributedCashbotBossCrane__cleanupCraneAdvice()
        if pressed:
            self.arrowHorz = -1
        elif self.arrowHorz < 0:
            self.arrowHorz = 0
        

    
    def _DistributedCashbotBossCrane__moveCraneArcHinge(self, xd, yd):
        dt = globalClock.getDt()
        h = self.arm.getH() - xd * self.rotateSpeed * dt
        limitH = max(min(h, self.armMaxH), self.armMinH)
        self.arm.setH(limitH)
        y = self.crane.getY() + yd * self.slideSpeed * dt
        limitY = max(min(y, self.craneMaxY), self.craneMinY)
        if not limitH != h:
            pass
        atLimit = limitY != y
        if atLimit:
            now = globalClock.getFrameTime()
            x = math.sin(now * 79) * 0.050000000000000003
            z = math.sin(now * 70) * 0.02
            self.crane.setPos(x, limitY, z)
            self._DistributedCashbotBossCrane__setMoveSound(self.atLimitSfx)
        else:
            self.crane.setPos(0, limitY, 0)
            self._DistributedCashbotBossCrane__setMoveSound(self.craneMoveSfx)

    
    def _DistributedCashbotBossCrane__setMoveSound(self, sfx):
        if sfx != self.moveSound:
            if self.moveSound:
                self.moveSound.stop()
            
            self.moveSound = sfx
            if self.moveSound:
                base.playSfx(self.moveSound, looping = 1, volume = 0.5)
            
        

    
    def _DistributedCashbotBossCrane__activateSniffer(self):
        if not (self.snifferActivated):
            self.sniffer.unstash()
            base.cTrav.addCollider(self.sniffer, self.snifferHandler)
            self.accept(self.snifferEvent, self._DistributedCashbotBossCrane__sniffedSomething)
            self.startFlicker()
            self.snifferActivated = 1
        

    
    def _DistributedCashbotBossCrane__deactivateSniffer(self):
        if self.snifferActivated:
            base.cTrav.removeCollider(self.sniffer)
            self.sniffer.stash()
            self.ignore(self.snifferEvent)
            self.stopFlicker()
            self.snifferActivated = 0
        

    
    def startFlicker(self):
        self.magnetSoundInterval.start()
        self.lightning = []
        for i in range(4):
            t = float(i) / 3.0 - 0.5
            l = self.boss.lightning.copyTo(self.gripper)
            l.setScale(random.choice([
                1,
                -1]), 1, 5)
            l.setZ(random.uniform(-5, -5.5))
            l.flattenLight()
            l.setTwoSided(1)
            l.setBillboardAxis()
            l.setScale(random.uniform(0.5, 1.0))
            if t < 0:
                l.setX(t - 0.69999999999999996)
            else:
                l.setX(t + 0.69999999999999996)
            l.setR(-20 * t)
            l.setP(random.uniform(-20, 20))
            self.lightning.append(l)
        
        taskMgr.add(self._DistributedCashbotBossCrane__flickerLightning, self.flickerName)

    
    def stopFlicker(self):
        self.magnetSoundInterval.finish()
        self.magnetLoopSfx.stop()
        taskMgr.remove(self.flickerName)
        for l in self.lightning:
            l.detachNode()
        
        self.lightning = None

    
    def _DistributedCashbotBossCrane__flickerLightning(self, task):
        for l in self.lightning:
            if random.random() < 0.5:
                l.hide()
            else:
                l.show()
        
        return Task.cont

    
    def _DistributedCashbotBossCrane__sniffedSomething(self, entry):
        np = entry.getIntoNodePath()
        doId = int(np.getNetTag('object'))
        obj = base.cr.doId2do.get(doId)
        if obj and obj.state != 'LocalDropped':
            obj.d_requestGrab()
            obj.demand('LocalGrabbed', localAvatar.doId, self.doId)
        

    
    def grabObject(self, obj):
        if self.state == 'Off':
            return None
        
        if self.heldObject != None:
            self.releaseObject()
        
        self._DistributedCashbotBossCrane__deactivateSniffer()
        obj.wrtReparentTo(self.gripper)
        if obj.lerpInterval:
            obj.lerpInterval.finish()
        
        obj.lerpInterval = Parallel(obj.posInterval(ToontownGlobals.CashbotBossToMagnetTime, Point3(*obj.grabPos)), obj.quatInterval(ToontownGlobals.CashbotBossToMagnetTime, VBase3(obj.getH(), 0, 0)), obj.toMagnetSoundInterval)
        obj.lerpInterval.start()
        self.heldObject = obj
        self.handler.setDynamicFrictionCoef(obj.craneFrictionCoef)
        self.slideSpeed = obj.craneSlideSpeed
        self.rotateSpeed = obj.craneRotateSpeed
        if self.avId == localAvatar.doId and not (self.magnetOn):
            self.releaseObject()
        

    
    def dropObject(self, obj):
        if obj.lerpInterval:
            obj.lerpInterval.finish()
        
        obj.wrtReparentTo(render)
        obj.lerpInterval = Parallel(obj.quatInterval(ToontownGlobals.CashbotBossFromMagnetTime, VBase3(obj.getH(), 0, 0), blendType = 'easeOut'))
        obj.lerpInterval.start()
        p1 = self.bottomLink.node().getPhysicsObject()
        v = render.getRelativeVector(self.bottomLink, p1.getVelocity())
        obj.physicsObject.setVelocity(v * 1.5)
        if self.heldObject == obj:
            self.heldObject = None
            self.handler.setDynamicFrictionCoef(self.emptyFrictionCoef)
            self.slideSpeed = self.emptySlideSpeed
            self.rotateSpeed = self.emptyRotateSpeed
        

    
    def releaseObject(self):
        if self.heldObject:
            obj = self.heldObject
            obj.d_requestDrop()
            if obj.state == 'Grabbed':
                obj.demand('LocalDropped', localAvatar.doId, self.doId)
            
        

    
    def _DistributedCashbotBossCrane__hitTrigger(self, event):
        self.d_requestControl()

    
    def setBossCogId(self, bossCogId):
        self.bossCogId = bossCogId
        self.boss = base.cr.doId2do[bossCogId]

    
    def setIndex(self, index):
        self.index = index

    
    def setState(self, state, avId):
        if state == 'C':
            self.demand('Controlled', avId)
        elif state == 'F':
            self.demand('Free')
        else:
            self.notify.error('Invalid state from AI: %s' % state)

    
    def d_requestControl(self):
        self.sendUpdate('requestControl')

    
    def d_requestFree(self):
        self.sendUpdate('requestFree')

    
    def b_clearSmoothing(self):
        self.d_clearSmoothing()
        self.clearSmoothing()

    
    def d_clearSmoothing(self):
        self.sendUpdate('clearSmoothing', [
            0])

    
    def clearSmoothing(self, bogus = None):
        self.armSmoother.clearPositions(1)
        for smoother in self.linkSmoothers:
            smoother.clearPositions(1)
        

    
    def reloadPosition(self):
        self.armSmoother.clearPositions(0)
        self.armSmoother.setPos(self.crane.getPos())
        self.armSmoother.setHpr(self.arm.getHpr())
        self.armSmoother.setPhonyTimestamp()
        for linkNum in range(self.numLinks):
            smoother = self.linkSmoothers[linkNum]
            (an, anp, cnp) = self.activeLinks[linkNum]
            smoother.clearPositions(0)
            smoother.setPos(anp.getPos())
            smoother.setPhonyTimestamp()
        

    
    def doSmoothTask(self, task):
        self.armSmoother.computeAndApplySmoothPosHpr(self.crane, self.arm)
        for linkNum in range(self.numLinks):
            smoother = self.linkSmoothers[linkNum]
            anp = self.activeLinks[linkNum][1]
            smoother.computeAndApplySmoothPos(anp)
        
        return Task.cont

    
    def startSmooth(self):
        if not (self.smoothStarted):
            taskName = self.smoothName
            taskMgr.remove(taskName)
            self.reloadPosition()
            taskMgr.add(self.doSmoothTask, taskName)
            self.smoothStarted = 1
        

    
    def stopSmooth(self):
        if self.smoothStarted:
            taskName = self.smoothName
            taskMgr.remove(taskName)
            self.forceToTruePosition()
            self.smoothStarted = 0
        

    
    def forceToTruePosition(self):
        if self.armSmoother.getLatestPosition():
            self.armSmoother.applySmoothPos(self.crane)
            self.armSmoother.applySmoothHpr(self.arm)
        
        self.armSmoother.clearPositions(1)
        for linkNum in range(self.numLinks):
            smoother = self.linkSmoothers[linkNum]
            (an, anp, cnp) = self.activeLinks[linkNum]
            if smoother.getLatestPosition():
                smoother.applySmoothPos(anp)
            
            smoother.clearPositions(1)
        

    
    def setCablePos(self, changeSeq, y, h, links, timestamp):
        self.changeSeq = changeSeq
        if self.smoothStarted:
            now = globalClock.getFrameTime()
            local = globalClockDelta.networkToLocalTime(timestamp, now)
            self.armSmoother.setY(y)
            self.armSmoother.setH(h)
            self.armSmoother.setTimestamp(local)
            self.armSmoother.markPosition()
            for linkNum in range(self.numLinks):
                smoother = self.linkSmoothers[linkNum]
                lp = links[linkNum]
                smoother.setPos(*lp)
                smoother.setTimestamp(local)
                smoother.markPosition()
            
        else:
            self.crane.setY(y)
            self.arm.setH(h)

    
    def d_sendCablePos(self):
        timestamp = globalClockDelta.getFrameNetworkTime()
        links = []
        for linkNum in range(self.numLinks):
            (an, anp, cnp) = self.activeLinks[linkNum]
            p = anp.getPos()
            links.append((p[0], p[1], p[2]))
        
        self.sendUpdate('setCablePos', [
            self.changeSeq,
            self.crane.getY(),
            self.arm.getH(),
            links,
            timestamp])

    
    def stopPosHprBroadcast(self):
        taskName = self.posHprBroadcastName
        taskMgr.remove(taskName)

    
    def startPosHprBroadcast(self):
        taskName = self.posHprBroadcastName
        self.b_clearSmoothing()
        self.d_sendCablePos()
        taskMgr.remove(taskName)
        taskMgr.doMethodLater(self._DistributedCashbotBossCrane__broadcastPeriod, self._DistributedCashbotBossCrane__posHprBroadcast, taskName)

    
    def _DistributedCashbotBossCrane__posHprBroadcast(self, task):
        self.d_sendCablePos()
        taskName = self.posHprBroadcastName
        taskMgr.doMethodLater(self._DistributedCashbotBossCrane__broadcastPeriod, self._DistributedCashbotBossCrane__posHprBroadcast, taskName)
        return Task.done

    
    def enterOff(self):
        self.clearCable()
        self.root.detachNode()

    
    def exitOff(self):
        if self.boss:
            self.setupCable()
        
        self.root.reparentTo(render)

    
    def enterControlled(self, avId):
        self.avId = avId
        toon = base.cr.doId2do.get(avId)
        if not toon:
            return None
        
        self.grabTrack = self.makeToonGrabInterval(toon)
        if avId == localAvatar.doId:
            self.boss.toCraneMode()
            camera.reparentTo(self.hinge)
            camera.setPosHpr(0, -20, -5, 0, -20, 0)
            self.tube.stash()
            localAvatar.setPosHpr(self.controls, 0, 0, 0, 0, 0, 0)
            localAvatar.sendCurrentPosition()
            self._DistributedCashbotBossCrane__activatePhysics()
            self._DistributedCashbotBossCrane__enableControlInterface()
            self.startPosHprBroadcast()
            self.startShadow()
            self.accept('exitCrane', self._DistributedCashbotBossCrane__exitCrane)
        else:
            self.startSmooth()
            toon.stopSmooth()
            self.grabTrack = Sequence(self.grabTrack, Func(toon.startSmooth))
        self.grabTrack.start()

    
    def exitControlled(self):
        self.ignore('exitCrane')
        self.grabTrack.finish()
        del self.grabTrack
        if self.toon and not self.toon.isDisabled():
            self.toon.loop('neutral')
            self.toon.startSmooth()
        
        self.stopWatchJoystick()
        self.stopPosHprBroadcast()
        self.stopShadow()
        self.stopSmooth()
        if self.avId == localAvatar.doId:
            self._DistributedCashbotBossCrane__disableControlInterface()
            self._DistributedCashbotBossCrane__deactivatePhysics()
            self.tube.unstash()
            camera.reparentTo(base.localAvatar)
            camera.setPos(base.localAvatar.cameraPositions[0][0])
            camera.setHpr(0, 0, 0)
            if self.cr:
                place = self.cr.playGame.getPlace()
                if place and hasattr(place, 'fsm'):
                    if place.fsm.getCurrentState().getName() == 'crane':
                        place.setState('finalBattle')
                    
                
            
            self.boss.toFinalBattleMode()
        
        self._DistributedCashbotBossCrane__straightenCable()

    
    def enterFree(self):
        if self.fadeTrack:
            self.fadeTrack.finish()
            self.fadeTrack = None
        
        self.restoreScaleTrack = Sequence(Wait(6), self.getRestoreScaleInterval())
        self.restoreScaleTrack.start()
        if self.avId == localAvatar.doId:
            self.controlModel.setAlphaScale(0.29999999999999999)
            self.controlModel.setTransparency(1)
            taskMgr.doMethodLater(5, self._DistributedCashbotBossCrane__allowDetect, self.triggerName)
            self.fadeTrack = Sequence(Func(self.controlModel.setTransparency, 1), self.controlModel.colorScaleInterval(0.20000000000000001, VBase4(1, 1, 1, 0.29999999999999999)))
            self.fadeTrack.start()
        else:
            self.trigger.unstash()
            self.accept(self.triggerEvent, self._DistributedCashbotBossCrane__hitTrigger)
        self.avId = 0

    
    def _DistributedCashbotBossCrane__allowDetect(self, task):
        if self.fadeTrack:
            self.fadeTrack.finish()
        
        self.fadeTrack = Sequence(self.controlModel.colorScaleInterval(0.20000000000000001, VBase4(1, 1, 1, 1)), Func(self.controlModel.clearColorScale), Func(self.controlModel.clearTransparency))
        self.fadeTrack.start()
        self.trigger.unstash()
        self.accept(self.triggerEvent, self._DistributedCashbotBossCrane__hitTrigger)

    
    def exitFree(self):
        if self.fadeTrack:
            self.fadeTrack.finish()
            self.fadeTrack = None
        
        self.restoreScaleTrack.pause()
        del self.restoreScaleTrack
        taskMgr.remove(self.triggerName)
        self.controlModel.clearColorScale()
        self.controlModel.clearTransparency()
        self.trigger.stash()
        self.ignore(self.triggerEvent)

    
    def enterMovie(self):
        self._DistributedCashbotBossCrane__activatePhysics()

    
    def exitMovie(self):
        self._DistributedCashbotBossCrane__deactivatePhysics()
        self._DistributedCashbotBossCrane__straightenCable()


