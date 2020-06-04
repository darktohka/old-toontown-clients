# File: B (Python 2.2)

from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.task import Task

class BankGui(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('BankGui')
    
    def __init__(self, doneEvent, allowWithdraw = 1):
        DirectFrame.__init__(self, relief = None, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (1.3300000000000001, 1, 1.1000000000000001), pos = (0, 0, 0))
        self.initialiseoptions(BankGui)
        self.doneEvent = doneEvent
        self._BankGui__transactionAmount = 0
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        jarGui = loader.loadModel('phase_3.5/models/gui/jar_gui')
        arrowGui = loader.loadModelOnce('phase_3/models/gui/create_a_toon_gui')
        bankModel = loader.loadModel('phase_5.5/models/estate/jellybeanBank.bam')
        bankModel.find('**/pig').setDepthWrite(1)
        bankModel.find('**/pig').setDepthTest(1)
        okImageList = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        cancelImageList = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
        arrowImageList = (arrowGui.find('**/CrtATn_R_Arrow_UP'), arrowGui.find('**/CrtATn_R_Arrow_DN'), arrowGui.find('**/CrtATn_R_Arrow_RLVR'), arrowGui.find('**/CrtATn_R_Arrow_UP'))
        self.cancelButton = DirectButton(parent = self, relief = None, image = cancelImageList, pos = (-0.20000000000000001, 0, -0.40000000000000002), text = TTLocalizer.BankGuiCancel, text_scale = 0.059999999999999998, text_pos = (0, -0.10000000000000001), command = self._BankGui__cancel)
        self.okButton = DirectButton(parent = self, relief = None, image = okImageList, pos = (0.20000000000000001, 0, -0.40000000000000002), text = TTLocalizer.BankGuiOk, text_scale = 0.059999999999999998, text_pos = (0, -0.10000000000000001), command = self._BankGui__requestTransaction)
        self.jarDisplay = DirectLabel(parent = self, relief = None, pos = (-0.40000000000000002, 0, 0), scale = 0.69999999999999996, text = str(base.localAvatar.getMoney()), text_scale = 0.20000000000000001, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_pos = (0, -0.10000000000000001, 0), image = jarGui.find('**/Jar'), text_font = ToontownGlobals.getSignFont())
        self.bankDisplay = DirectLabel(parent = self, relief = None, pos = (0.40000000000000002, 0, 0), scale = 0.90000000000000002, text = str(base.localAvatar.getBankMoney()), text_scale = 0.20000000000000001, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_pos = (0, -0.10000000000000001, 0), geom = bankModel, geom_scale = 0.080000000000000002, geom_pos = (0, 10, -0.26000000000000001), geom_hpr = (0, 0, 0), text_font = ToontownGlobals.getSignFont())
        self.depositArrow = DirectButton(parent = self, relief = None, image = arrowImageList, image_scale = (1, 1, 1), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.25), pos = (0.01, 0, 0.14999999999999999))
        self.withdrawArrow = DirectButton(parent = self, relief = None, image = arrowImageList, image_scale = (-1, 1, 1), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.25), pos = (-0.01, 0, -0.14999999999999999))
        self.depositArrow.bind(B1PRESS, self._BankGui__depositButtonDown)
        self.depositArrow.bind(B1RELEASE, self._BankGui__depositButtonUp)
        self.withdrawArrow.bind(B1PRESS, self._BankGui__withdrawButtonDown)
        self.withdrawArrow.bind(B1RELEASE, self._BankGui__withdrawButtonUp)
        self.accept(localAvatar.uniqueName('moneyChange'), self._BankGui__moneyChange)
        self.accept(localAvatar.uniqueName('bankMoneyChange'), self._BankGui__bankMoneyChange)
        if allowWithdraw:
            self.depositArrow.setPos(0.01, 0, 0.14999999999999999)
            self.withdrawArrow.setPos(-0.01, 0, -0.14999999999999999)
        else:
            self.depositArrow.setPos(0, 0, 0)
            self.withdrawArrow.hide()
        buttons.removeNode()
        jarGui.removeNode()
        arrowGui.removeNode()
        self._BankGui__updateTransaction(0)

    
    def destroy(self):
        taskMgr.remove(self.taskName('runCounter'))
        self.ignore(localAvatar.uniqueName('moneyChange'))
        self.ignore(localAvatar.uniqueName('bankMoneyChange'))
        DirectFrame.destroy(self)

    
    def _BankGui__cancel(self):
        messenger.send(self.doneEvent, [
            0])

    
    def _BankGui__requestTransaction(self):
        messenger.send(self.doneEvent, [
            self._BankGui__transactionAmount])

    
    def _BankGui__updateTransaction(self, amount):
        hitLimit = 0
        self._BankGui__transactionAmount += amount
        jarMoney = base.localAvatar.getMoney()
        maxJarMoney = base.localAvatar.getMaxMoney()
        bankMoney = base.localAvatar.getBankMoney()
        maxBankMoney = base.localAvatar.getMaxBankMoney()
        self._BankGui__transactionAmount = min(self._BankGui__transactionAmount, jarMoney)
        self._BankGui__transactionAmount = min(self._BankGui__transactionAmount, maxBankMoney - bankMoney)
        self._BankGui__transactionAmount = -min(-(self._BankGui__transactionAmount), maxJarMoney - jarMoney)
        self._BankGui__transactionAmount = -min(-(self._BankGui__transactionAmount), bankMoney)
        newJarMoney = jarMoney - self._BankGui__transactionAmount
        newBankMoney = bankMoney + self._BankGui__transactionAmount
        if newJarMoney <= 0 or newBankMoney >= maxBankMoney:
            self.depositArrow['state'] = DISABLED
            hitLimit = 1
        else:
            self.depositArrow['state'] = NORMAL
        if newBankMoney <= 0 or newJarMoney >= maxJarMoney:
            self.withdrawArrow['state'] = DISABLED
            hitLimit = 1
        else:
            self.withdrawArrow['state'] = NORMAL
        self.jarDisplay['text'] = str(newJarMoney)
        self.bankDisplay['text'] = str(newBankMoney)
        return (hitLimit, newJarMoney, newBankMoney, self._BankGui__transactionAmount)

    
    def _BankGui__runCounter(self, task):
        if task.time - task.prevTime < task.delayTime:
            return Task.cont
        else:
            task.delayTime = max(0.050000000000000003, task.delayTime * 0.75)
            task.prevTime = task.time
            (hitLimit, jar, bank, trans) = self._BankGui__updateTransaction(task.delta)
            if hitLimit:
                return Task.done
            else:
                return Task.cont

    
    def _BankGui__depositButtonUp(self, event):
        taskMgr.remove(self.taskName('runCounter'))

    
    def _BankGui__depositButtonDown(self, event):
        task = Task.Task(self._BankGui__runCounter)
        task.delayTime = 0.40000000000000002
        task.prevTime = 0.0
        task.delta = 1
        (hitLimit, jar, bank, trans) = self._BankGui__updateTransaction(task.delta)
        if not hitLimit:
            taskMgr.add(task, self.taskName('runCounter'))
        

    
    def _BankGui__withdrawButtonUp(self, event):
        taskMgr.remove(self.taskName('runCounter'))

    
    def _BankGui__withdrawButtonDown(self, event):
        task = Task.Task(self._BankGui__runCounter)
        task.delayTime = 0.40000000000000002
        task.prevTime = 0.0
        task.delta = -1
        (hitLimit, jar, bank, trans) = self._BankGui__updateTransaction(task.delta)
        if not hitLimit:
            taskMgr.add(task, self.taskName('runCounter'))
        

    
    def _BankGui__moneyChange(self, money):
        self._BankGui__updateTransaction(0)

    
    def _BankGui__bankMoneyChange(self, bankMoney):
        self._BankGui__updateTransaction(0)


