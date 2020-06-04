# File: F (Python 2.2)

from DirectGui import *
import FishPokerBase
import FishGlobals
import Localizer
import ToontownGlobals

class FishPokerCard(DirectFrame):
    UnlockedColor = Vec4(*ToontownGlobals.GlobalDialogColor)
    LockedColor = Vec4(0.80000000000000004, 0.40000000000000002, 0.40000000000000002, 1)
    
    def __init__(self, index, lockCallback, **kw):
        optiondefs = (('relief', None, None), ('image', getDefaultDialogGeom(), None), ('image_color', ToontownGlobals.GlobalDialogColor, None), ('image_scale', (0.34999999999999998, 1, 0.45000000000000001), None), ('text', '', None), ('text_scale', 0.059999999999999998, None), ('text_fg', (0, 0, 0, 1), None), ('text_pos', (0, 0.34999999999999998, 0), None), ('text_font', ToontownGlobals.getInterfaceFont(), None), ('text_wordwrap', 13.5, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self)
        self.initialiseoptions(FishPokerCard)
        self.index = index
        self.fish = None
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.lockCallback = lockCallback
        self.lockButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = 1, text = Localizer.FishPokerLock, text_scale = 0.059999999999999998, textMayChange = 1, pos = (0, 0, 0.20000000000000001), command = self.toggleLock)
        self.fishFrame = DirectFrame(parent = self, relief = None, text = '', text_scale = 0.050000000000000003, pos = (0, 0, -0.20000000000000001))
        guiButton.removeNode()

    
    def toggleLock(self):
        self.lockCallback(self.index)

    
    def update(self, fish, lockedStatus):
        self.fish = fish
        if self.fish:
            self.lockButton['state'] = NORMAL
            self.fishFrame['text'] = fish.getGenusName()
        else:
            self.lockButton['state'] = DISABLED
            self.fishFrame['text'] = ''
        self.setLockStatus(lockedStatus)
        return None

    
    def setLockStatus(self, lockStatus):
        if lockStatus:
            self.lockButton['text'] = Localizer.FishPokerUnlock
            self['image_color'] = self.LockedColor
        else:
            self.lockButton['text'] = Localizer.FishPokerLock
            self['image_color'] = self.UnlockedColor
        return None

    
    def clear(self):
        self.update(None, 0)
        return None



class FishPokerGui(FishPokerBase.FishPokerBase, DirectFrame):
    
    def __init__(self, lockCallback, cashInCallback):
        DirectFrame.__init__(self, relief = None)
        self.initialiseoptions(FishPokerGui)
        self.setPos(0, 0, 0.80000000000000004)
        self.setScale(0.69999999999999996)
        self.lockCallback = lockCallback
        self.cashInCallback = cashInCallback
        self._FishPokerGui__cardGuis = { }
        for i in range(self.NumSlots):
            card = FishPokerCard(i, self.toggleLock)
            card.reparentTo(self)
            card.setPos(-0.80000000000000004 + i * 0.40000000000000002, 0, 0)
            self._FishPokerGui__cardGuis[i] = card
        
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.cashInButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = 1.1499999999999999, text = Localizer.FishPokerCashIn % (0, ''), text_scale = 0.059999999999999998, pos = (0, 0, -0.29999999999999999), command = self.cashIn)
        guiButton.removeNode()
        FishPokerBase.FishPokerBase.__init__(self)

    
    def updateCashIn(self):
        (value, handName) = self.getCurrentValue()
        self.cashInButton['text'] = Localizer.FishPokerCashIn % (handName, value)

    
    def cashIn(self):
        result = FishPokerBase.FishPokerBase.cashIn(self)
        self.cashInCallback()
        return result

    
    def toggleLock(self, index):
        if self.isLocked(index):
            self.setLockStatus(index, 0)
        else:
            self.setLockStatus(index, 1)

    
    def setLockStatus(self, index, lockStatus):
        result = FishPokerBase.FishPokerBase.setLockStatus(self, index, lockStatus)
        self._FishPokerGui__cardGuis[index].setLockStatus(lockStatus)
        self.lockCallback(index, lockStatus)
        return result

    
    def drawCard(self, card):
        index = FishPokerBase.FishPokerBase.drawCard(self, card)
        if index != -1:
            self._FishPokerGui__cardGuis[index].update(card, 0)
        
        self.updateCashIn()
        return index

    
    def clear(self):
        FishPokerBase.FishPokerBase.clear(self)
        for cardGui in self._FishPokerGui__cardGuis.values():
            cardGui.clear()
        
        self.updateCashIn()


