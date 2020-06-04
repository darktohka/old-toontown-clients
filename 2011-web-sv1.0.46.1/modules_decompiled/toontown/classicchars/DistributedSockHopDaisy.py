# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\classicchars\DistributedSockHopDaisy.py
from direct.showbase.ShowBaseGlobal import *
import DistributedCCharBase, DistributedDaisy
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
import CharStateDatas
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.hood import TTHood

class DistributedSockHopDaisy(DistributedDaisy.DistributedDaisy):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSockHopDaisy')

    def __init__(self, cr):
        try:
            self.DistributedSockHopDaisy_initialized
        except:
            self.DistributedSockHopDaisy_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr, TTLocalizer.SockHopDaisy, 'shdd')
            self.fsm = ClassicFSM.ClassicFSM(self.getName(), [
             State.State('Off', self.enterOff, self.exitOff, [
              'Neutral']),
             State.State('Neutral', self.enterNeutral, self.exitNeutral, [
              'Walk']),
             State.State('Walk', self.enterWalk, self.exitWalk, [
              'Neutral'])], 'Off', 'Off')
            self.fsm.enterInitialState()
            self.nametag.setName(TTLocalizer.Daisy)
            self.handleHolidays()