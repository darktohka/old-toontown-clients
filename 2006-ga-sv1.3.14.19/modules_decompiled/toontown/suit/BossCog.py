# File: B (Python 2.2)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from otp.avatar import Avatar
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.toonbase import TTLocalizer
from toontown.battle import BattleParticles
import Suit
import SuitDNA
from toontown.battle import BattleProps
from direct.showbase.PythonUtil import Functor
import string
import types
ModelDict = {
    's': 'phase_9/models/char/sellbotBoss' }
AnimList = ('Ff_speech', 'ltTurn2Wave', 'wave', 'Ff_lookRt', 'turn2Fb', 'Ff_neutral', 'Bb_neutral', 'Ff2Bb_spin', 'Bb2Ff_spin', 'Fb_neutral', 'Bf_neutral', 'Fb_firstHit', 'Fb_downNeutral', 'Fb_downHit', 'Fb_fall', 'Fb_down2Up', 'Fb_downLtSwing', 'Fb_downRtSwing', 'Fb_DownThrow', 'Fb_UpThrow', 'Fb_jump')

class BossCog(Avatar.Avatar):
    notify = DirectNotifyGlobal.directNotify.newCategory('BossCog')
    
    def __init__(self):
        Avatar.Avatar.__init__(self)
        self.setFont(ToontownGlobals.getSuitFont())
        self.setPlayerType(NametagGroup.CCSuit)
        self.setPickable(0)
        self.doorA = None
        self.doorB = None
        self.bubbleL = None
        self.bubbleR = None
        self.raised = 1
        self.forward = 1
        self.happy = 1
        self.dizzy = 0
        self.nowRaised = 1
        self.nowForward = 1
        self.nowHappy = 1
        self.currentAnimIval = None
        self.queuedAnimIvals = []
        self.treadsLeftPos = 0
        self.treadsRightPos = 0
        self.animDoneEvent = 'BossCogAnimDone'
        self.animIvalName = 'BossCogAnimIval'

    
    def delete(self):
        Avatar.Avatar.delete(self)
        self.stopAnimate()
        if self.doorA:
            self.doorA.requestFinalState()
            self.doorB.requestFinalState()
        

    
    def setDNAString(self, dnaString):
        self.dna = SuitDNA.SuitDNA()
        self.dna.makeFromNetString(dnaString)
        self.setDNA(self.dna)

    
    def setDNA(self, dna):
        if self.style:
            pass
        1
        self.style = dna
        self.generateBossCog()
        self.initializeDropShadow()
        self.initializeNametag3d()

    
    def generateBossCog(self):
        self.throwSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_frisbee_gears.mp3')
        self.swingSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_swipe.mp3')
        self.spinSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_spin.mp3')
        self.rainGearsSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_raining_gears.mp3')
        self.swishSfx = loader.loadSfx('phase_5/audio/sfx/General_throw_miss.mp3')
        self.boomSfx = loader.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.mp3')
        self.deathSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_big_death.mp3')
        self.upSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_raise_up.mp3')
        self.downSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_collapse.mp3')
        self.reelSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_reeling_backwards.mp3')
        self.birdsSfx = loader.loadSfx('phase_4/audio/sfx/SZ_TC_bird1.mp3')
        self.dizzyAlert = loader.loadSfx('phase_5/audio/sfx/AA_sound_aoogah.mp3')
        self.grunt = loader.loadSfx('phase_9/audio/sfx/Boss_COG_VO_grunt.mp3')
        self.murmur = loader.loadSfx('phase_9/audio/sfx/Boss_COG_VO_murmur.mp3')
        self.statement = loader.loadSfx('phase_9/audio/sfx/Boss_COG_VO_statement.mp3')
        self.question = loader.loadSfx('phase_9/audio/sfx/Boss_COG_VO_question.mp3')
        self.dialogArray = [
            self.grunt,
            self.murmur,
            self.statement,
            self.question,
            self.statement,
            self.statement]
        dna = self.style
        filePrefix = ModelDict[dna.dept]
        self.loadModel(filePrefix + '-legs-zero', 'legs')
        self.loadModel(filePrefix + '-torso-zero', 'torso')
        self.loadModel(filePrefix + '-head-zero', 'head')
        self.attach('head', 'torso', 'joint34')
        self.attach('torso', 'legs', 'joint_pelvis')
        self.rotateNode = self.attachNewNode('rotate')
        geomNode = self.getGeomNode()
        geomNode.reparentTo(self.rotateNode)
        self.frontAttack = self.rotateNode.attachNewNode('frontAttack')
        self.frontAttack.setPos(0, -10, 10)
        self.frontAttack.setScale(2)
        self.nametag3d.setZ(26)
        self.nametag3d.setScale(2)
        for partName in ('legs', 'torso', 'head'):
            animDict = { }
            for anim in AnimList:
                animDict[anim] = '%s-%s-%s' % (filePrefix, partName, anim)
            
            self.loadAnims(animDict, partName)
        
        self.stars = BattleProps.globalPropPool.getProp('stun')
        self.stars.setPosHprScale(7, 0, 0, 0, 0, 90, 3, 3, 3)
        self.stars.loop('stun')
        self.pelvis = self.getPart('torso')
        self.pelvisForwardHpr = VBase3(0, 0, 0)
        self.pelvisReversedHpr = VBase3(-180, 0, 0)
        self.neck = self.getPart('head')
        self.neckForwardHpr = VBase3(0, 0, 0)
        self.neckReversedHpr = VBase3(0, -540, 0)
        self.axle = self.find('**/joint_axle')
        self.doorA = self._BossCog__setupDoor('**/joint_doorFront', 'doorA', self.doorACallback, VBase3(0, 0, 0), VBase3(0, 0, 80), CollisionPolygon(Point3(5, -4, 0.32000000000000001), Point3(0, -4, 0), Point3(0, 4, 0), Point3(5, 4, 0.32000000000000001)))
        self.doorB = self._BossCog__setupDoor('**/joint_doorRear', 'doorB', self.doorBCallback, VBase3(0, 0, 0), VBase3(0, 0, -80), CollisionPolygon(Point3(-5, 4, 0.83999999999999997), Point3(0, 4, 0), Point3(0, -4, 0), Point3(-5, -4, 0.83999999999999997)))
        treadsModel = loader.loadModel('%s-treads' % filePrefix)
        treadsModel.reparentTo(self.axle)
        self.treadsLeft = treadsModel.find('**/right_tread')
        self.treadsRight = treadsModel.find('**/left_tread')
        self.doorA.request('closed')
        self.doorB.request('closed')

    
    def getShadowJoint(self):
        return self.getGeomNode()

    
    def getNametagJoints(self):
        return []

    
    def getDialogueArray(self):
        return self.dialogArray

    
    def doorACallback(self, isOpen):
        pass

    
    def doorBCallback(self, isOpen):
        pass

    
    def _BossCog__rollTreadsInterval(self, object, start = 0, duration = 0, rate = 1):
        
        def rollTexMatrix(t, node = object.node()):
            txa = TexMatrixAttrib.make(Mat4.translateMat(t, 0, 0))
            node.setAttrib(txa)

        return LerpFunctionInterval(rollTexMatrix, fromData = start, toData = start + rate * duration, duration = duration)

    
    def rollLeftTreads(self, duration, rate):
        start = self.treadsLeftPos
        self.treadsLeftPos += duration * rate
        return self._BossCog__rollTreadsInterval(self.treadsLeft, start = start, duration = duration, rate = rate)

    
    def rollRightTreads(self, duration, rate):
        start = self.treadsRightPos
        self.treadsRightPos += duration * rate
        return self._BossCog__rollTreadsInterval(self.treadsRight, start = start, duration = duration, rate = rate)

    
    def _BossCog__setupDoor(self, jointName, name, callback, openedHpr, closedHpr, cPoly):
        joint = self.find(jointName)
        children = joint.getChildren()
        animate = joint.attachNewNode(name)
        children.reparentTo(animate)
        cnode = CollisionNode('BossZap')
        cnode.setCollideMask(ToontownGlobals.PieBitmask | ToontownGlobals.WallBitmask)
        cnode.addSolid(cPoly)
        animate.attachNewNode(cnode)
        openSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_door_open.mp3')
        closeSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_door_close.mp3')
        animate.openedHpr = openedHpr
        animate.closedHpr = closedHpr
        animate.openSfx = openSfx
        animate.closeSfx = closeSfx
        animate.callback = callback
        fsm = ClassicFSM.ClassicFSM(name, [
            State.State('open', Functor(self.enterDoorOpen, animate), Functor(self.exitDoorOpen, animate), [
                'opened',
                'close',
                'closed']),
            State.State('opened', Functor(self.enterDoorOpened, animate), Functor(self.exitDoorOpened, animate), [
                'close',
                'closed']),
            State.State('close', Functor(self.enterDoorClose, animate), Functor(self.exitDoorClose, animate), [
                'open',
                'opened',
                'closed']),
            State.State('closed', Functor(self.enterDoorClosed, animate), Functor(self.exitDoorClosed, animate), [
                'open',
                'opened']),
            State.State('off', Functor(self.enterDoorOff, animate), Functor(self.exitDoorOff, animate))], 'off', 'off', onUndefTransition = ClassicFSM.ClassicFSM.DISALLOW)
        fsm.enterInitialState()
        return fsm

    
    def enterDoorOpen(self, animate):
        intervalName = self.uniqueName('open-%s' % animate.getName())
        animate.callback(0)
        ival = Parallel(SoundInterval(animate.openSfx, node = animate, volume = 0.20000000000000001), animate.hprInterval(1, animate.openedHpr, blendType = 'easeInOut'), Sequence(Wait(0.20000000000000001), Func(animate.callback, 1)), name = intervalName)
        ival.start()
        animate.ival = ival

    
    def exitDoorOpen(self, animate):
        animate.ival.pause()
        animate.ival = None

    
    def enterDoorOpened(self, animate):
        animate.setHpr(animate.openedHpr)
        animate.callback(1)

    
    def exitDoorOpened(self, animate):
        pass

    
    def enterDoorClose(self, animate):
        intervalName = self.uniqueName('close-%s' % animate.getName())
        animate.callback(1)
        ival = Parallel(SoundInterval(animate.closeSfx, node = animate, volume = 0.20000000000000001), animate.hprInterval(1, animate.closedHpr, blendType = 'easeInOut'), Sequence(Wait(0.80000000000000004), Func(animate.callback, 0)), name = intervalName)
        ival.start()
        animate.ival = ival

    
    def exitDoorClose(self, animate):
        animate.ival.pause()
        animate.ival = None

    
    def enterDoorClosed(self, animate):
        animate.setHpr(animate.closedHpr)
        animate.callback(0)

    
    def exitDoorClosed(self, animate):
        pass

    
    def enterDoorOff(self, animate):
        pass

    
    def exitDoorOff(self, animate):
        pass

    
    def doAnimate(self, anim = None, now = 0, queueNeutral = 1, raised = None, forward = None, happy = None):
        if now:
            self.stopAnimate()
        
        if raised == None:
            raised = self.raised
        
        if forward == None:
            forward = self.forward
        
        if happy == None:
            happy = self.happy
        
        if now:
            self.raised = raised
            self.forward = forward
            self.happy = happy
        
        if self.currentAnimIval == None:
            self.accept(self.animDoneEvent, self._BossCog__getNextAnim)
        else:
            queueNeutral = 0
        (ival, changed) = self._BossCog__getAnimIval(anim, raised, forward, happy)
        if changed or queueNeutral:
            self.queuedAnimIvals.append((ival, self.raised, self.forward, self.happy))
            if self.currentAnimIval == None:
                self._BossCog__getNextAnim()
            
        

    
    def stopAnimate(self):
        self.ignore(self.animDoneEvent)
        self.queuedAnimIvals = []
        if self.currentAnimIval:
            self.currentAnimIval.setDoneEvent('')
            self.currentAnimIval.finish()
            self.currentAnimIval = None
        
        self.raised = self.nowRaised
        self.forward = self.nowForward
        self.happy = self.nowHappy

    
    def _BossCog__getNextAnim(self):
        if self.queuedAnimIvals:
            (ival, raised, forward, happy) = self.queuedAnimIvals[0]
            del self.queuedAnimIvals[0]
        else:
            (ival, changed) = self._BossCog__getAnimIval(None, self.raised, self.forward, self.happy)
            raised = self.raised
            forward = self.forward
            happy = self.happy
        if self.currentAnimIval:
            self.currentAnimIval.setDoneEvent('')
            self.currentAnimIval.finish()
        
        self.currentAnimIval = ival
        self.currentAnimIval.start()
        self.nowRaised = raised
        self.nowForward = forward
        self.nowHappy = happy

    
    def _BossCog__getAnimIval(self, anim, raised, forward, happy):
        (ival, changed) = self._BossCog__doGetAnimIval(anim, raised, forward, happy)
        seq = Sequence(ival, name = self.animIvalName)
        seq.setDoneEvent(self.animDoneEvent)
        return (seq, changed)

    
    def _BossCog__doGetAnimIval(self, anim, raised, forward, happy):
        if raised == self.raised and forward == self.forward and happy == self.happy:
            return (self.getAnim(anim), anim != None)
        
        startsHappy = self.happy
        endsHappy = self.happy
        ival = Sequence()
        if raised and not (self.raised):
            if self.happy:
                upIval = Sequence(Func(self.neck.setHpr, self.neckReversedHpr), ActorInterval(self, 'Fb_down2Up'), Func(self.neck.setHpr, self.neckForwardHpr))
            else:
                upIval = ActorInterval(self, 'Fb_down2Up')
            if self.forward:
                ival = upIval
            else:
                ival = Sequence(Func(self.pelvis.setHpr, self.pelvisReversedHpr), upIval, Func(self.pelvis.setHpr, self.pelvisForwardHpr))
            ival = Parallel(SoundInterval(self.upSfx, node = self), ival)
        
        if forward != self.forward:
            if forward:
                animName = 'Bb2Ff_spin'
            else:
                animName = 'Ff2Bb_spin'
            ival = Sequence(ival, ActorInterval(self, animName))
            startsHappy = 1
            endsHappy = 1
        
        startNeckHpr = self.neckForwardHpr
        endNeckHpr = self.neckForwardHpr
        if self.happy != startsHappy:
            startNeckHpr = self.neckReversedHpr
        
        if happy != endsHappy:
            endNeckHpr = self.neckReversedHpr
        
        if startNeckHpr != endNeckHpr:
            ival = Sequence(Func(self.neck.setHpr, startNeckHpr), ParallelEndTogether(ival, Sequence(self.neck.hprInterval(0.5, endNeckHpr, startHpr = startNeckHpr, blendType = 'easeInOut'), Func(self.neck.setHpr, self.neckForwardHpr))))
        elif endNeckHpr != self.neckForwardHpr:
            ival = Sequence(Func(self.neck.setHpr, startNeckHpr), ival, Func(self.neck.setHpr, self.neckForwardHpr))
        
        if not raised and self.raised:
            if happy:
                downIval = Sequence(Func(self.neck.setHpr, self.neckReversedHpr), ActorInterval(self, 'Fb_down2Up', playRate = -1), Func(self.neck.setHpr, self.neckForwardHpr))
            else:
                downIval = ActorInterval(self, 'Fb_down2Up', playRate = -1)
            if forward:
                ival = Sequence(ival, downIval)
            else:
                ival = Sequence(ival, Func(self.pelvis.setHpr, self.pelvisReversedHpr), downIval, Func(self.pelvis.setHpr, self.pelvisForwardHpr))
            ival = Parallel(SoundInterval(self.downSfx, node = self), ival)
        
        self.raised = raised
        self.forward = forward
        self.happy = happy
        if anim != None:
            ival = Sequence(ival, self.getAnim(anim))
        
        return (ival, 1)

    
    def setDizzy(self, dizzy):
        if dizzy and not (self.dizzy):
            base.playSfx(self.dizzyAlert)
        
        self.dizzy = dizzy
        if dizzy:
            self.stars.reparentTo(self.neck)
            base.playSfx(self.birdsSfx, looping = 1)
        else:
            self.stars.detachNode()
            self.birdsSfx.stop()

    
    def getAnim(self, anim):
        ival = None
        if anim == None:
            partName = None
            if self.happy:
                animName = 'Ff_neutral'
            else:
                animName = 'Fb_neutral'
            if self.raised:
                ival = ActorInterval(self, animName)
            else:
                ival = Parallel(ActorInterval(self, animName, partName = [
                    'torso',
                    'head']), ActorInterval(self, 'Fb_downNeutral', partName = 'legs'))
            if not (self.forward):
                ival = Sequence(Func(self.pelvis.setHpr, self.pelvisReversedHpr), ival, Func(self.pelvis.setHpr, self.pelvisForwardHpr))
            
        elif anim == 'down2Up':
            if self.happy:
                ival = Sequence(Func(self.neck.setHpr, self.neckReversedHpr), ActorInterval(self, 'Fb_down2Up'), Func(self.neck.setHpr, self.neckForwardHpr))
            else:
                ival = ActorInterval(self, 'Fb_down2Up')
            ival = Parallel(SoundInterval(self.upSfx, node = self), ival)
            self.raised = 1
        elif anim == 'up2Down':
            if self.happy:
                ival = Sequence(Func(self.neck.setHpr, self.neckReversedHpr), ActorInterval(self, 'Fb_down2Up', playRate = -1), Func(self.neck.setHpr, self.neckForwardHpr))
            else:
                ival = ActorInterval(self, 'Fb_down2Up', playRate = -1)
            ival = Parallel(SoundInterval(self.downSfx, node = self), ival)
            self.raised = 0
        elif anim == 'throw':
            self.doAnimate(None, raised = 1, happy = 0, queueNeutral = 0)
            ival = ActorInterval(self, 'Fb_UpThrow')
            ival = Parallel(SoundInterval(self.throwSfx, node = self), ival)
        elif anim == 'hit':
            if self.raised:
                self.raised = 0
                ival = ActorInterval(self, 'Fb_firstHit')
            else:
                ival = ActorInterval(self, 'Fb_downHit')
            if self.happy:
                ival = Sequence(Func(self.neck.setHpr, self.neckReversedHpr), ival, Func(self.neck.setHpr, self.neckForwardHpr))
            
            ival = Parallel(SoundInterval(self.reelSfx, node = self), ival)
        elif anim == 'ltSwing' or anim == 'rtSwing':
            self.doAnimate(None, raised = 0, happy = 0, queueNeutral = 0)
            if anim == 'ltSwing':
                ival = Sequence(Track((0, ActorInterval(self, 'Fb_downLtSwing')), (0.90000000000000002, SoundInterval(self.swingSfx, node = self)), (1, Func(self.bubbleL.unstash))), Func(self.bubbleL.stash))
            else:
                ival = Sequence(Track((0, ActorInterval(self, 'Fb_downRtSwing')), (0.90000000000000002, SoundInterval(self.swingSfx, node = self)), (1, Func(self.bubbleR.unstash))), Func(self.bubbleR.stash))
        elif anim == 'frontAttack':
            self.doAnimate(None, raised = 1, happy = 0, queueNeutral = 0)
            pe = BattleParticles.loadParticleFile('bossCogFrontAttack.ptf')
            ival = Sequence(Func(self.neck.setHpr, self.neckReversedHpr), ActorInterval(self, 'Bb2Ff_spin'), Func(self.neck.setHpr, self.neckForwardHpr))
            if self.forward:
                ival = Sequence(Func(self.pelvis.setHpr, self.pelvisReversedHpr), ParallelEndTogether(ival, self.pelvis.hprInterval(0.5, self.pelvisForwardHpr, blendType = 'easeInOut')))
            
            ival = Sequence(Track((0, ival), (0, SoundInterval(self.spinSfx, node = self)), (0.90000000000000002, Parallel(SoundInterval(self.rainGearsSfx, node = self), ParticleInterval(pe, self.frontAttack, worldRelative = 0, duration = 1.5), duration = 0)), (1.8999999999999999, Func(self.bubbleF.unstash))), Func(self.bubbleF.stash))
            self.forward = 1
            self.happy = 0
            self.raised = 1
        elif anim == 'areaAttack':
            self.doAnimate(None, raised = 1, happy = 0, queueNeutral = 0)
            ival = Parallel(ActorInterval(self, 'Fb_jump'), Sequence(SoundInterval(self.swishSfx, duration = 1.1000000000000001, node = self), SoundInterval(self.boomSfx, duration = 1.8999999999999999)), Sequence(Wait(1.21), Func(self.announceAreaAttack)))
            self.happy = 0
            self.raised = 1
        elif anim == 'Fb_fall':
            ival = Parallel(ActorInterval(self, 'Fb_fall'), Sequence(SoundInterval(self.reelSfx, node = self), SoundInterval(self.deathSfx)))
        elif isinstance(anim, types.StringType):
            ival = ActorInterval(self, anim)
        else:
            ival = anim
        return ival


