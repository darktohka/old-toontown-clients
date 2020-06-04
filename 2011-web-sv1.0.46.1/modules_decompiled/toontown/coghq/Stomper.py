# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\Stomper.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from direct.showbase.PythonUtil import lerp
from direct.fsm import StateData
import math

class Stomper(StateData.StateData, NodePath):
    __module__ = __name__
    SerialNum = 0
    MotionLinear = 0
    MotionSinus = 1
    MotionHalfSinus = 2
    DefaultStompSound = 'phase_5/audio/sfx/AA_drop_safe.mp3'

    def __init__(self, model, range=5.0, period=1.0, phaseShift=0.0, zOffset=0.0, motionType=None, shadow=None, sound=None, soundLen=None):
        StateData.StateData.__init__(self, 'StomperDone')
        self.SerialNum = Stomper.SerialNum
        Stomper.SerialNum += 1
        self.sound = sound
        self.soundLen = soundLen
        if self.sound is not None:
            self.sound = base.loadSfx(sound)
        self.motionType = motionType
        if self.motionType is None:
            self.motionType = Stomper.MotionSinus
        node = hidden.attachNewNode('Stomper%s' % self.SerialNum)
        NodePath.__init__(self, node)
        self.model = model.copyTo(self)
        self.shadow = shadow
        if shadow is not None:
            self.shadow = shadow.copyTo(self)
            self.shadow.setPos(0, 0, 0.2)
        self.TaskName = 'Stomper%sTask' % self.SerialNum
        self.range = range
        self.zOffset = zOffset
        self.period = period
        self.phaseShift = phaseShift
        return

    def destroy(self):
        self.removeNode()

    def enter(self, startTime):
        if self.motionType is Stomper.MotionLinear:
            motionIval = Sequence(LerpPosInterval(self.model, self.period / 2.0, Point3(0, 0, self.zOffset + self.range), startPos=Point3(0, 0, self.zOffset)), WaitInterval(self.period / 4.0), LerpPosInterval(self.model, self.period / 4.0, Point3(0, 0, self.zOffset), startPos=Point3(0, 0, self.zOffset + self.range)))
        elif self.motionType is Stomper.MotionSinus:

            def sinusFunc(t, self=self):
                theta = math.pi + t * 2.0 * math.pi
                c = math.cos(theta)
                self.model.setZ(self.zOffset + (0.5 + c * 0.5) * self.range)

            motionIval = Sequence(LerpFunctionInterval(sinusFunc, duration=self.period))
        elif self.motionType is Stomper.MotionHalfSinus:

            def halfSinusFunc(t, self=self):
                self.model.setZ(self.zOffset + math.sin(t * math.pi) * self.range)

            motionIval = Sequence(LerpFunctionInterval(halfSinusFunc, duration=self.period))
        self.ival = Parallel(motionIval, name='Stomper%s' % self.SerialNum)
        if self.sound is not None:
            if self.soundLen is None:
                sndDur = motionIval.getDuration()
            else:
                sndDur = min(self.soundLen, motionIval.getDuration())
            self.ival.append(SoundInterval(self.sound, duration=sndDur, node=self))
        if self.shadow is not None:

            def adjustShadowScale(t, self=self):
                modelZ = self.model.getZ()
                a = modelZ / self.range
                self.shadow.setScale(lerp(0.7, 1.0, 1.0 - a))

            self.ival.append(LerpFunctionInterval(adjustShadowScale, duration=self.period))
        self.ival.loop()
        self.ival.setT(globalClock.getFrameTime() - startTime + self.period * self.phaseShift)
        return

    def exit(self):
        self.ival.finish()
        del self.ival