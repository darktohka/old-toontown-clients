# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\classicchars\DistributedWesternPluto.py
from pandac.PandaModules import *
import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from toontown.classicchars import DistributedPluto
import CharStateDatas
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import DistributedCCharBase

class DistributedWesternPluto(DistributedPluto.DistributedPluto):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedWesternPluto')

    def __init__(self, cr):
        try:
            self.DistributedPluto_initialized
        except:
            self.DistributedPluto_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr, TTLocalizer.WesternPluto, 'wp')
            self.fsm = ClassicFSM.ClassicFSM('DistributedWesternPluto', [
             State.State('Off', self.enterOff, self.exitOff, [
              'Neutral']),
             State.State('Neutral', self.enterNeutral, self.exitNeutral, [
              'Walk']),
             State.State('Walk', self.enterWalk, self.exitWalk, [
              'Neutral'])], 'Off', 'Off')
            self.fsm.enterInitialState()
            self.nametag.setName(TTLocalizer.Pluto)

    def walkSpeed(self):
        return ToontownGlobals.WesternPlutoSpeed