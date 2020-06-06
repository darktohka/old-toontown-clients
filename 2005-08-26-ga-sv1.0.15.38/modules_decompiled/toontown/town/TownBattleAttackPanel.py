# File: T (Python 2.2)

from direct.showbase.DirectObject import *
from direct.showbase.ShowBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
import string
from direct.fsm import StateData
AttackPanelHidden = 0

def hideAttackPanel(flag):
    global AttackPanelHidden
    AttackPanelHidden = flag
    messenger.send('hide-attack-panel')


class TownBattleAttackPanel(StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        return None

    
    def load(self):
        StateData.StateData.load(self)

    
    def unload(self):
        StateData.StateData.unload(self)

    
    def enter(self):
        StateData.StateData.enter(self)
        if not AttackPanelHidden:
            base.localAvatar.inventory.show()
        
        self.accept('inventory-selection', self._TownBattleAttackPanel__handleInventory)
        self.accept('inventory-run', self._TownBattleAttackPanel__handleRun)
        self.accept('inventory-sos', self._TownBattleAttackPanel__handleSOS)
        self.accept('inventory-pass', self._TownBattleAttackPanel__handlePass)
        self.accept('hide-attack-panel', self._TownBattleAttackPanel__handleHide)
        return None

    
    def exit(self):
        StateData.StateData.exit(self)
        self.ignore('inventory-selection')
        self.ignore('inventory-run')
        self.ignore('inventory-sos')
        self.ignore('inventory-pass')
        self.ignore('hide-attack-panel')
        base.localAvatar.inventory.hide()
        return None

    
    def _TownBattleAttackPanel__handleRun(self):
        doneStatus = {
            'mode': 'Run' }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def _TownBattleAttackPanel__handleSOS(self):
        doneStatus = {
            'mode': 'SOS' }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def _TownBattleAttackPanel__handlePass(self):
        doneStatus = {
            'mode': 'Pass' }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def _TownBattleAttackPanel__handleInventory(self, track, level):
        if base.localAvatar.inventory.numItem(track, level) > 0:
            doneStatus = { }
            doneStatus['mode'] = 'Inventory'
            doneStatus['track'] = track
            doneStatus['level'] = level
            messenger.send(self.doneEvent, [
                doneStatus])
        else:
            self.notify.error("An item we don't have: track %s level %s was selected." % [
                track,
                level])
        return None

    
    def _TownBattleAttackPanel__handleHide(self):
        if AttackPanelHidden:
            base.localAvatar.inventory.hide()
        else:
            base.localAvatar.inventory.show()
        return None


