# File: N (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase import PandaObject
from otp.avatar import Avatar
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.fsm import StateData
import whrandom
from direct.task import Task
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.distributed.PyDatagram import PyDatagram
from direct.gui import OnscreenText
from otp.distributed import PotentialAvatar
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLocalizer
from otp.namepanel import NameCheck
from otp.namepanel import NameTumbler
import re
import string
MAX_NAME_WIDTH = 8

class NamePanel(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, listOfNames, doneEvent, usedNames):
        StateData.StateData.__init__(self, doneEvent)
        self.listOfNames = listOfNames
        self.doneEvent = doneEvent
        self.avId = -1
        self.tumblerList = { }
        self.usedNames = usedNames
        self.interfaceFont = OTPGlobals.getInterfaceFont()
        self.signFont = OTPGlobals.getSignFont()
        self.nameEntryFont = OTPGlobals.getInterfaceFont()
        self.name = ''
        self.nameIsChecked = 0
        self.nameAction = 0
        self.fsm = ClassicFSM.ClassicFSM('NameShop', [
            State.State('Init', self.enterInit, self.exitInit, [
                'PickAName']),
            State.State('PickAName', self.enterPickANameState, self.exitPickANameState, [
                'TypeAName',
                'Done']),
            State.State('TypeAName', self.enterTypeANameState, self.exitTypeANameState, [
                'PickAName',
                'Done']),
            State.State('Done', self.enterDone, self.exitDone, [
                'Init'])], 'Init', 'Done')
        return None

    
    def start(self):
        self.avExists = 0
        self.loadInterfaceGUI()
        self.accept('CheckTumblerPriority', self._NamePanel__checkPriority)
        self.accept('CheckTumblerLinkage', self._NamePanel__checkLinkage)
        self.accept('updateNameResult', self._NamePanel__updateNameResult)
        self.fsm.enterInitialState()
        self.fsm.request('PickAName')

    
    def exit(self):
        self.ignore('CheckTumblerPriority')
        self.ignore('CheckTumblerLinkage')
        self.ignore('updateNameResult')
        self.ignore('rejectDone')
        self.unloadInterfaceGUI()

    
    def loadInterfaceGUI(self):
        self.interface = DirectFrame(parent = aspect2d, relief = 'flat', scale = 0.90000000000000002, state = 'disabled', frameColor = (1, 1, 1, 0), pos = (0, 0, 0))
        self.PickAName = DirectFrame(parent = aspect2d, relief = 'flat', scale = 0.90000000000000002, state = 'disabled', frameColor = (1, 1, 1, 0), pos = (0, 0, 0))
        self.PickAName.reparentTo(self.interface)
        self.TypeAName = DirectFrame(parent = aspect2d, relief = 'flat', scale = 0.90000000000000002, state = 'disabled', frameColor = (1, 1, 1, 0), pos = (0, 0, 0))
        self.TypeAName.reparentTo(self.interface)
        nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        gui = loader.loadModelOnce('phase_3/models/gui/nameshop_gui')
        typePanel = gui.find('**/typeNamePanel')
        self.randomButton = DirectButton(parent = aspect2d, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1, 1, 1), scale = (1, 1, 1), pos = (0.01, 0, -0.40000000000000002), text = OTPLocalizer.RandomButton, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self.randomName)
        self.randomButton.reparentTo(self.PickAName)
        self.typeANameButton = DirectButton(parent = aspect2d, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1, 1, 1), pos = (0.01, 0, -0.55000000000000004), scale = (1, 1, 1), text = OTPLocalizer.TypeANameButton, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self.toggleNameMode)
        self.typeANameButton.reparentTo(self.interface)
        self.nameResult = DirectLabel(parent = aspect2d, relief = None, scale = 0.12, pos = (0, 0, 0.59999999999999998), text = ' \n ', text_scale = 0.80000000000000004, text_align = TextNode.ACenter, text_wordwrap = MAX_NAME_WIDTH)
        self.nameResult.reparentTo(self.PickAName)
        for i in range(len(self.listOfNames)):
            tPos = (i * 0.40000000000000002 - (len(self.listOfNames) / 2.0) * 0.40000000000000002) + 0.80000000000000004
            self.tumblerList[i] = NameTumbler.NameTumbler((tPos, 0, -0.10000000000000001), self.listOfNames[i][0], self.listOfNames[i][1], self.listOfNames[i][2], self.listOfNames[i][3], (1, 0.80000000000000004, 0.80000000000000004, 1))
            self.tumblerList[i].tumbler.reparentTo(self.PickAName)
        
        self.nameLabel = OnscreenText.OnscreenText(OTPLocalizer.PleaseTypeName, parent = aspect2d, style = OnscreenText.ScreenPrompt, pos = (0, 0.53000000000000003))
        self.nameLabel.reparentTo(self.TypeAName)
        self.typeNotification = OnscreenText.OnscreenText(OTPLocalizer.AllNewNames, parent = aspect2d, style = OnscreenText.ScreenPrompt, pos = (0, 0.14999999999999999))
        self.typeNotification.reparentTo(self.TypeAName)
        self.nameEntry = DirectEntry(parent = aspect2d, relief = None, scale = 0.080000000000000002, entryFont = self.nameEntryFont, width = MAX_NAME_WIDTH, numLines = 2, focus = 0, cursorKeys = 1, pos = (0.0, 0.0, 0.39000000000000001), text_align = TextNode.ACenter, command = self.toggleNameMode)
        self.nameEntry.reparentTo(self.TypeAName)
        self.submitButton = DirectButton(parent = aspect2d, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1.2, 0, 1.1000000000000001), pos = (-0.01, 0, -0.25), text = OTPLocalizer.NameShopSubmitButton, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self.submitName)
        self.submitButton.reparentTo(self.TypeAName)
        gui.removeNode()
        nameBalloon.removeNode()
        self.randomName()
        return None

    
    def unloadInterfaceGUI(self):
        for i in range(len(self.tumblerList)):
            self.tumblerList[i].unloadTumblerGUI()
            del self.tumblerList[i]
        
        self.randomButton.destroy()
        del self.randomButton
        self.typeANameButton.destroy()
        del self.typeANameButton
        self.nameResult.destroy()
        del self.nameResult
        self.nameLabel.destroy()
        del self.nameLabel
        self.typeNotification.destroy()
        del self.typeNotification
        self.nameEntry.destroy()
        del self.nameEntry
        self.submitButton.destroy()
        del self.submitButton
        self.PickAName.destroy()
        del self.PickAName
        self.TypeAName.destroy()
        del self.TypeAName
        self.interface.destroy()
        del self.interface

    
    def toggleNameMode(self):
        if self.fsm.getCurrentState().getName() == 'TypeAName':
            self.typeANameButton['text'] = OTPLocalizer.TypeANameButton
            self.fsm.request('PickAName')
        else:
            self.typeANameButton['text'] = OTPLocalizer.PickANameButton
            self.fsm.request('TypeAName')

    
    def randomName(self):
        for i in range(len(self.tumblerList)):
            self.tumblerList[i].getRandomResult()
        
        self._NamePanel__updateNameResult()

    
    def _NamePanel__updateNameResult(self):
        self.nameResult['text'] = ''
        for i in range(len(self.tumblerList)):
            self.nameResult['text'] += self.tumblerList[i].getName()
            if i != len(self.tumblerList) and self.listOfNames[i][3] <= 0:
                self.nameResult['text'] += ' '
            
        
        self.name = self.nameResult['text']

    
    def _NamePanel__checkPriority(self, category):
        value = 0
        for i in self.tumblerList:
            if self.tumblerList[i].priority == 1:
                value += self.tumblerList[i].isActive
            
        
        if value > 1:
            for i in self.tumblerList:
                if self.tumblerList[i].priority == 1 and category == self.tumblerList[i].category:
                    self.tumblerList[i].deactivateTumbler()
                
            
        

    
    def _NamePanel__checkLinkage(self, category):
        linkageValue = 0
        isActive = 0
        for i in self.tumblerList:
            if category == self.tumblerList[i].category:
                linkageValue = self.tumblerList[i].linkage
                isActive = self.tumblerList[i].isActive
            
        
        for i in self.tumblerList:
            if self.tumblerList[i].linkage == linkageValue:
                if isActive:
                    self.tumblerList[i].activateTumbler()
                else:
                    self.tumblerList[i].deactivateTumbler()
            
        

    
    def submitName(self, *args):
        self.notify.debug('__submitName')
        self.nameEntry['focus'] = 0
        self.nameIsChecked = 1
        name = self.nameEntry.get()
        self.nameEntry.enterText(name.strip())
        problem = self.nameIsValid(self.nameEntry.get())
        if problem:
            self.rejectName(problem)
            return None
        
        if not (self.avExists):
            self.nameAction = 2
            messenger.send('namePanel-Done')
        else:
            self.checkNameTyped()

    
    def nameIsValid(self, name):
        self.notify.debug('nameIsValid')
        if name in self.usedNames:
            return OTPLocalizer.ToonAlreadyExists % name
        
        problem = NameCheck.checkName(name)
        if problem:
            return problem
        
        return None

    
    def rejectName(self, str):
        self.notify.debug('rejectName')
        self.name = ''
        self.nameIsChecked = 0
        self.acceptOnce('rejectDone', self._NamePanel__handleReject)

    
    def _NamePanel__handleReject(self):
        self.rejectDialog.cleanup()
        self.nameEntry['focus'] = 1

    
    def enterInit(self):
        self.notify.debug('enterInit')
        self.TypeAName.hide()
        self.PickAName.hide()

    
    def exitInit(self):
        pass

    
    def enterPickANameState(self):
        self.notify.debug('enterPickANameState')
        self.nameAction = 1
        self.PickAName.show()
        self.randomName()

    
    def exitPickANameState(self):
        self.PickAName.hide()

    
    def enterTypeANameState(self):
        self.notify.debug('enterTypeANameState')
        self.TypeAName.show()
        self.nameEntry.set('')
        self.nameEntry['focus'] = 1

    
    def exitTypeANameState(self):
        self.TypeAName.hide()

    
    def enterDone(self):
        self.notify.debug('enterDone')
        return None

    
    def exitDone(self):
        return None


