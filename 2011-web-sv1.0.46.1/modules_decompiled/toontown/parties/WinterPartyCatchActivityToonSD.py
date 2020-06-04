# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\parties\WinterPartyCatchActivityToonSD.py
import PartyCatchActivityToonSD
from pandac.PandaModules import Vec4
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Sequence, Parallel, Wait, Func
from direct.interval.IntervalGlobal import LerpColorScaleInterval
from direct.interval.IntervalGlobal import WaitInterval, ActorInterval, FunctionInterval
from direct.fsm import ClassicFSM, State

class WinterPartyCatchActivityToonSD(PartyCatchActivityToonSD.PartyCatchActivityToonSD):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('PartyCatchActivityToonSD')

    def __init__(self, avId, activity):
        WinterPartyCatchActivityToonSD.notify.debug('init : avId = %s, activity = %s ' % (avId, activity))
        PartyCatchActivityToonSD.PartyCatchActivityToonSD.__init__(self, avId, activity)

    def enterEatFruit(self, fruitModel, handNode):
        self.notify.debug('enterEatFruit')
        if self.isLocal:
            self.activity.orthoWalk.start()
        self.setAnimState('Catching', 1.0)
        self.fruitModel = fruitModel
        renderScale = fruitModel.getScale(render)
        fruitModel.reparentTo(handNode)
        fruitModel.setScale(render, renderScale)
        fruitModel.setTransparency(1)
        duration = self.toon.getDuration('catch-eatneutral')
        self.eatIval = Sequence(Parallel(WaitInterval(duration), Sequence(LerpColorScaleInterval(fruitModel, duration / 2.0, Vec4(1.0, 1.0, 1.0, 0.0)))), Func(self.fsm.request, 'normal'), name=self.toon.uniqueName('eatingIval'))
        self.eatIval.start()

    def exitEatFruit(self):
        self.eatIval.pause()
        del self.eatIval
        self.fruitModel.reparentTo(hidden)
        self.fruitModel.removeNode()
        del self.fruitModel
        self.setAnimState('off', 1.0)
        if self.isLocal:
            self.activity.orthoWalk.stop()