# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\town\TownBattleAttackPanel.py
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
import string
from direct.fsm import StateData
from toontown.toontowngui.TeaserPanel import TeaserPanel
from toontown.toonbase.ToontownBattleGlobals import gagIsPaidOnly
AttackPanelHidden = 0

def hideAttackPanel(flag):
    global AttackPanelHidden
    AttackPanelHidden = flag
    messenger.send('hide-attack-panel')


class TownBattleAttackPanel(StateData.StateData):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattleAttackPanel')

    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)

    def load(self):
        StateData.StateData.load(self)

    def unload(self):
        StateData.StateData.unload(self)

    def enter(self):
        StateData.StateData.enter(self)
        self._teaserPanel = None
        if not AttackPanelHidden:
            base.localAvatar.inventory.show()
        self.accept('inventory-selection', self.__handleInventory)
        self.accept('inventory-run', self.__handleRun)
        self.accept('inventory-sos', self.__handleSOS)
        self.accept('inventory-pass', self.__handlePass)
        self.accept('inventory-fire', self.__handleFire)
        self.accept('hide-attack-panel', self.__handleHide)
        return

    def exit(self):
        StateData.StateData.exit(self)
        self.ignore('inventory-selection')
        self.ignore('inventory-run')
        self.ignore('inventory-sos')
        self.ignore('inventory-pass')
        self.ignore('inventory-fire')
        self.ignore('hide-attack-panel')
        base.localAvatar.inventory.hide()
        if self._teaserPanel:
            self._teaserPanel.destroy()
            del self._teaserPanel

    def __handleRun(self):
        doneStatus = {'mode': 'Run'}
        messenger.send(self.doneEvent, [doneStatus])

    def __handleSOS(self):
        doneStatus = {'mode': 'SOS'}
        messenger.send(self.doneEvent, [doneStatus])

    def __handlePass(self):
        doneStatus = {'mode': 'Pass'}
        messenger.send(self.doneEvent, [doneStatus])

    def __handleFire(self):
        doneStatus = {'mode': 'Fire'}
        messenger.send(self.doneEvent, [doneStatus])

    def __handleInventory(self, track, level):
        if not base.cr.isPaid() and gagIsPaidOnly(track, level):
            self._teaserPanel = TeaserPanel(pageName='useGags')
            return
        if base.localAvatar.inventory.numItem(track, level) > 0:
            doneStatus = {}
            doneStatus['mode'] = 'Inventory'
            doneStatus['track'] = track
            doneStatus['level'] = level
            messenger.send(self.doneEvent, [doneStatus])
        else:
            self.notify.error("An item we don't have: track %s level %s was selected." % [track, level])

    def __handleHide(self):
        if AttackPanelHidden:
            base.localAvatar.inventory.hide()
        else:
            base.localAvatar.inventory.show()