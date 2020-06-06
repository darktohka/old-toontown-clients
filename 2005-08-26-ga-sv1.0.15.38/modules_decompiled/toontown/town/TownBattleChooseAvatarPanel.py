# File: T (Python 2.2)

from pandac.PandaModules import *
from toontown.toonbase.ToontownBattleGlobals import *
from toontown.toonbase import ToontownGlobals
from direct.fsm import StateData
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import BattleBase
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer

class TownBattleChooseAvatarPanel(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('ChooseAvatarPanel')
    
    def __init__(self, doneEvent, toon):
        self.notify.info('Init choose panel...')
        StateData.StateData.__init__(self, doneEvent)
        self.numAvatars = 0
        self.chosenAvatar = 0
        self.toon = toon
        return None

    
    def load(self):
        gui = loader.loadModelOnce('phase_3.5/models/gui/battle_gui')
        self.frame = DirectFrame(relief = None, image = gui.find('**/BtlPick_TAB'), image_color = Vec4(1, 0.20000000000000001, 0.20000000000000001, 1))
        self.frame.hide()
        self.statusFrame = DirectFrame(parent = self.frame, relief = None, image = gui.find('**/ToonBtl_Status_BG'), image_color = Vec4(0.5, 0.90000000000000002, 0.5, 1), pos = (0.61099999999999999, 0, 0))
        self.textFrame = DirectFrame(parent = self.frame, relief = None, image = gui.find('**/PckMn_Select_Tab'), image_color = Vec4(1, 1, 0, 1), text = '', text_fg = Vec4(0, 0, 0, 1), text_pos = (0, -0.025000000000000001, 0), text_scale = 0.080000000000000002, pos = (-0.012999999999999999, 0, 0.012999999999999999))
        if self.toon:
            self.textFrame['text'] = TTLocalizer.TownBattleChooseAvatarToonTitle
        else:
            self.textFrame['text'] = TTLocalizer.TownBattleChooseAvatarCogTitle
        self.avatarButtons = []
        for i in range(4):
            button = DirectButton(parent = self.frame, relief = None, image = (gui.find('**/PckMn_Arrow_Up'), gui.find('**/PckMn_Arrow_Dn'), gui.find('**/PckMn_Arrow_Rlvr')), command = self._TownBattleChooseAvatarPanel__handleAvatar, extraArgs = [
                i])
            if self.toon:
                button.setScale(1, 1, -1)
                button.setPos(0, 0, -0.20000000000000001)
            else:
                button.setScale(1, 1, 1)
                button.setPos(0, 0, 0.20000000000000001)
            self.avatarButtons.append(button)
        
        self.backButton = DirectButton(parent = self.frame, relief = None, image = (gui.find('**/PckMn_BackBtn'), gui.find('**/PckMn_BackBtn_Dn'), gui.find('**/PckMn_BackBtn_Rlvr')), pos = (-0.64700000000000002, 0, 0.0060000000000000001), scale = 1.05, text = TTLocalizer.TownBattleChooseAvatarBack, text_scale = 0.050000000000000003, text_pos = (0.01, -0.012), text_fg = Vec4(0, 0, 0.80000000000000004, 1), command = self._TownBattleChooseAvatarPanel__handleBack)
        gui.removeNode()
        return None

    
    def unload(self):
        self.frame.destroy()
        del self.frame
        del self.statusFrame
        del self.textFrame
        del self.avatarButtons
        del self.backButton
        return None

    
    def enter(self, numAvatars, localNum = None, luredIndices = None, trappedIndices = None, track = None):
        self.frame.show()
        invalidTargets = []
        if not (self.toon):
            if len(luredIndices) > 0:
                if track == BattleBase.TRAP or track == BattleBase.LURE:
                    invalidTargets += luredIndices
                
            
            if len(trappedIndices) > 0:
                if track == BattleBase.TRAP:
                    invalidTargets += trappedIndices
                
            
        
        self._TownBattleChooseAvatarPanel__placeButtons(numAvatars, invalidTargets, localNum)
        return None

    
    def exit(self):
        self.frame.hide()
        return None

    
    def _TownBattleChooseAvatarPanel__handleBack(self):
        doneStatus = {
            'mode': 'Back' }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def _TownBattleChooseAvatarPanel__handleAvatar(self, avatar):
        doneStatus = {
            'mode': 'Avatar',
            'avatar': avatar }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def adjustCogs(self, numAvatars, luredIndices, trappedIndices, track):
        invalidTargets = []
        if len(luredIndices) > 0:
            if track == BattleBase.TRAP or track == BattleBase.LURE:
                invalidTargets += luredIndices
            
        
        if len(trappedIndices) > 0:
            if track == BattleBase.TRAP:
                invalidTargets += trappedIndices
            
        
        self._TownBattleChooseAvatarPanel__placeButtons(numAvatars, invalidTargets, None)
        return None

    
    def adjustToons(self, numToons, localNum):
        self._TownBattleChooseAvatarPanel__placeButtons(numToons, [], localNum)
        return None

    
    def _TownBattleChooseAvatarPanel__placeButtons(self, numAvatars, invalidTargets, localNum):
        for i in range(4):
            if numAvatars > i and i not in invalidTargets and i != localNum:
                self.avatarButtons[i].show()
            else:
                self.avatarButtons[i].hide()
        
        if numAvatars == 1:
            self.avatarButtons[0].setX(0)
        elif numAvatars == 2:
            self.avatarButtons[0].setX(0.20000000000000001)
            self.avatarButtons[1].setX(-0.20000000000000001)
        elif numAvatars == 3:
            self.avatarButtons[0].setX(0.40000000000000002)
            self.avatarButtons[1].setX(0.0)
            self.avatarButtons[2].setX(-0.40000000000000002)
        elif numAvatars == 4:
            self.avatarButtons[0].setX(0.59999999999999998)
            self.avatarButtons[1].setX(0.20000000000000001)
            self.avatarButtons[2].setX(-0.20000000000000001)
            self.avatarButtons[3].setX(-0.59999999999999998)
        else:
            self.notify.error('Invalid number of avatars: %s' % numAvatars)
        return None


