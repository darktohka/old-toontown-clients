# File: P (Python 2.2)

from toontown.toonbase.ToontownBattleGlobals import *
from toontown.toonbase import ToontownGlobals
from direct.fsm import StateData
from toontown.shtiker.PurchaseManagerConstants import *
from direct.gui.DirectGui import *
from direct.task import Task
from direct.fsm import State
from direct.fsm import ClassicFSM
from direct.distributed import DelayDelete
from toontown.toonbase import TTLocalizer

class PurchaseBase(StateData.StateData):
    activateMode = 'purchase'
    
    def __init__(self, toon, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.toon = toon
        self.fsm = ClassicFSM.ClassicFSM('Purchase', [
            State.State('purchase', self.enterPurchase, self.exitPurchase, [
                'done']),
            State.State('done', self.enterDone, self.exitDone, [
                'purchase'])], 'done', 'done')
        self.fsm.enterInitialState()
        return None

    
    def load(self, purchaseModels = None):
        if purchaseModels == None:
            purchaseModels = loader.loadModel('phase_4/models/gui/purchase_gui')
        
        self.music = base.loadMusic('phase_4/audio/bgm/FF_safezone.mid')
        self.jarImage = purchaseModels.find('**/Jar')
        self.jarImage.reparentTo(hidden)
        self.frame = DirectFrame(relief = None)
        self.frame.hide()
        self.title = DirectLabel(parent = self.frame, relief = None, pos = (0.0, 0.0, 0.82999999999999996), scale = 1.2, image = purchaseModels.find('**/Goofys_Sign'), text = TTLocalizer.GagShopName, text_fg = (0.59999999999999998, 0.20000000000000001, 0, 1), text_scale = 0.089999999999999997, text_wordwrap = 10, text_pos = (0, 0.025000000000000001, 0), text_font = ToontownGlobals.getSignFont())
        self.pointDisplay = DirectLabel(parent = self.frame, relief = None, pos = (-1.0800000000000001, 0.0, 0.16), text = str(self.toon.getMoney()), text_scale = 0.20000000000000001, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_pos = (0, -0.10000000000000001, 0), image = self.jarImage, text_font = ToontownGlobals.getSignFont())
        self.statusLabel = DirectLabel(parent = self.frame, relief = None, pos = (-0.25, 0, 0.625), text = TTLocalizer.GagShopYouHave % self.toon.getMoney(), text_scale = 0.080000000000000002, text_fg = (0.050000000000000003, 0.14000000000000001, 0.40000000000000002, 1))
        if self.toon.getMoney() == 1:
            self.statusLabel['text'] = TTLocalizer.GagShopYouHaveOne
        
        self.isBroke = 0
        return None

    
    def unload(self):
        self.jarImage.removeNode()
        del self.jarImage
        self.frame.destroy()
        del self.frame
        del self.title
        del self.pointDisplay
        del self.statusLabel
        del self.music
        del self.fsm
        return None

    
    def _PurchaseBase__handleSelection(self, track, level):
        self.handlePurchase(track, level)

    
    def handlePurchase(self, track, level):
        if self.toon.getMoney() <= 0:
            return None
        
        ret = self.toon.inventory.addItem(track, level)
        if ret == -2:
            text = TTLocalizer.GagShopTooManyProps
        elif ret == -1:
            text = TTLocalizer.GagShopTooManyOfThatGag % TTLocalizer.BattleGlobalAvPropStringsPlural[track][level]
        elif ret == 0:
            text = TTLocalizer.GagShopInsufficientSkill
        else:
            text = TTLocalizer.GagShopYouPurchased % TTLocalizer.BattleGlobalAvPropStringsSingular[track][level]
            self.toon.inventory.updateGUI(track, level)
            self.toon.setMoney(self.toon.getMoney() - 1)
            messenger.send('boughtGag')
        self.showStatusText(text)
        return None

    
    def showStatusText(self, text):
        self.statusLabel['text'] = text
        taskMgr.remove('resetStatusText')
        taskMgr.doMethodLater(2.0, self.resetStatusText, 'resetStatusText')
        return None

    
    def resetStatusText(self, task):
        self.statusLabel['text'] = ''
        return Task.done

    
    def checkForBroke(self):
        money = self.toon.getMoney()
        self.pointDisplay['text'] = str(money)
        if money == 0:
            if not (self.isBroke):
                self.toon.inventory.setActivateModeBroke()
                taskMgr.doMethodLater(2.25, self.showBrokeMsg, 'showBrokeMsgTask')
                self.isBroke = 1
            
        elif self.isBroke:
            self.toon.inventory.setActivateMode(self.activateMode)
            taskMgr.remove('showBrokeMsgTask')
            self.isBroke = 0
        
        if money == 1:
            self.statusLabel['text'] = TTLocalizer.GagShopYouHaveOne
        else:
            self.statusLabel['text'] = TTLocalizer.GagShopYouHave % money
        return None

    
    def showBrokeMsg(self, task):
        self.statusLabel['text'] = TTLocalizer.GagShopOutOfJellybeans
        return Task.done

    
    def handleDone(self, playAgain):
        messenger.send(self.doneEvent)

    
    def enter(self):
        self.fsm.request('purchase')

    
    def exit(self):
        self.music.stop()
        self.fsm.request('done')

    
    def enterPurchase(self):
        self.frame.show()
        self.toon.inventory.show()
        self.toon.inventory.reparentTo(self.frame)
        self.toon.inventory.setActivateMode(self.activateMode)
        self.checkForBroke()
        self.acceptOnce('purchaseOver', self.handleDone)
        self.accept('inventory-selection', self._PurchaseBase__handleSelection)
        self.accept(self.toon.uniqueName('moneyChange'), self._PurchaseBase__moneyChange)
        return None

    
    def exitPurchase(self):
        self.frame.hide()
        self.toon.inventory.reparentTo(hidden)
        self.toon.inventory.hide()
        self.ignore('purchaseOver')
        self.ignore('inventory-selection')
        self.ignore(self.toon.uniqueName('moneyChange'))
        taskMgr.remove('resetStatusText')
        taskMgr.remove('showBrokeMsgTask')
        return None

    
    def _PurchaseBase__moneyChange(self, money):
        self.checkForBroke()

    
    def enterDone(self):
        pass

    
    def exitDone(self):
        pass


