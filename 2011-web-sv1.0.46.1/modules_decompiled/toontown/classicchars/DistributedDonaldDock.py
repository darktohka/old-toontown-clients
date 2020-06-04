# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\classicchars\DistributedDonaldDock.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from toontown.toonbase import ToontownGlobals
import CharStateDatas
from direct.fsm import StateData
from direct.task import Task
from toontown.toonbase import TTLocalizer

class DistributedDonaldDock(DistributedCCharBase.DistributedCCharBase):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDonaldDock')

    def __init__(self, cr):
        try:
            self.DistributedDonaldDock_initialized
        except:
            self.DistributedDonaldDock_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr, TTLocalizer.DonaldDock, 'dw')
            self.fsm = ClassicFSM.ClassicFSM('DistributedDonaldDock', [
             State.State('Off', self.enterOff, self.exitOff, [
              'Neutral']),
             State.State('Neutral', self.enterNeutral, self.exitNeutral, [
              'Off'])], 'Off', 'Off')
            self.fsm.enterInitialState()
            self.nametag.setName(TTLocalizer.Donald)
            self.handleHolidays()

    def disable(self):
        self.fsm.requestFinalState()
        DistributedCCharBase.DistributedCCharBase.disable(self)
        taskMgr.remove('enterNeutralTask')
        del self.neutralDoneEvent
        del self.neutral
        self.fsm.requestFinalState()

    def delete(self):
        try:
            self.DistributedDonaldDock_deleted
        except:
            self.DistributedDonaldDock_deleted = 1
            del self.fsm
            DistributedCCharBase.DistributedCCharBase.delete(self)

    def generate(self):
        DistributedCCharBase.DistributedCCharBase.generate(self)
        boat = base.cr.playGame.hood.loader.boat
        self.setPos(0, -1, 3.95)
        self.reparentTo(boat)
        self.neutralDoneEvent = self.taskName('DonaldDock-neutral-done')
        self.neutral = CharStateDatas.CharNeutralState(self.neutralDoneEvent, self)
        self.fsm.request('Neutral')

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterNeutral(self):
        self.notify.debug('Neutral ' + self.getName() + '...')
        self.neutral.enter()
        self.acceptOnce(self.neutralDoneEvent, self.__decideNextState)

    def exitNeutral(self):
        self.ignore(self.neutralDoneEvent)
        self.neutral.exit()

    def __decideNextState(self, doneStatus):
        self.fsm.request('Neutral')