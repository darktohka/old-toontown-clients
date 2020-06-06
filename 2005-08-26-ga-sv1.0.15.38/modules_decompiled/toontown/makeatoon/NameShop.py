# File: N (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.task.TaskManagerGlobal import *
from direct.gui.DirectGui import *
from toontown.distributed.ToontownMsgTypes import *
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import PandaObject
from direct.gui import OnscreenText
from otp.avatar import Avatar
from otp.chat import ChatManager
from direct.fsm import StateData
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.toontowngui import TTDialog
import re
import string
from toontown.toonbase import TTLocalizer
import NameGenerator
import whrandom
from otp.distributed import PotentialAvatar
import NameCheck
from toontown.toontowngui import TeaserPanel
from direct.distributed.PyDatagram import PyDatagram
MAX_NAME_WIDTH = 7.5
ServerDialogTimeout = 3.0

class NameShop(PandaObject.PandaObject, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('NameShop')
    notify.setDebug(True)
    
    def __init__(self, parentFSM, doneEvent, avList, index, isPaid):
        StateData.StateData.__init__(self, doneEvent)
        self.isPaid = isPaid
        self.avList = avList
        self.index = index
        self.shopsVisited = []
        self.avId = -1
        self.avExists = 0
        self.names = [
            '',
            '',
            '',
            '']
        self.toon = None
        self.boy = 0
        self.girl = 0
        self.allTitles = []
        self.allFirsts = []
        self.allPrefixes = []
        self.allSuffixes = []
        self.titleIndex = 0
        self.firstIndex = 0
        self.prefixIndex = 0
        self.suffixIndex = 0
        self.titleActive = 0
        self.firstActive = 0
        self.lastActive = 0
        self.quickFind = 0
        self.listsLoaded = 0
        self.addedGenderSpecific = 0
        self.chastise = 0
        self.nameIndices = [
            -1,
            -1,
            -1,
            -1]
        self.nameFlags = [
            1,
            1,
            1,
            0]
        self.dummyReturn = 2
        self.nameAction = 0
        self.pickANameGUIElements = []
        self.typeANameGUIElements = []
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.90000000000000002, 1, 1)
        self.textDisabledColor = Vec4(0.40000000000000002, 0.80000000000000004, 0.40000000000000002, 1)
        self.fsm = ClassicFSM.ClassicFSM('NameShop', [
            State.State('Init', self.enterInit, self.exitInit, [
                'PayState']),
            State.State('PayState', self.enterPayState, self.exitPayState, [
                'PickAName']),
            State.State('PickAName', self.enterPickANameState, self.exitPickANameState, [
                'TypeAName',
                'Done']),
            State.State('TypeAName', self.enterTypeANameState, self.exitTypeANameState, [
                'PickAName',
                'Approval',
                'Accepted',
                'Rejected']),
            State.State('Approval', self.enterApprovalState, self.exitApprovalState, [
                'PickAName',
                'Done']),
            State.State('Accepted', self.enterAcceptedState, self.exitAcceptedState, [
                'Done']),
            State.State('Rejected', self.enterRejectedState, self.exitRejectedState, [
                'TypeAName']),
            State.State('Done', self.enterDone, self.exitDone, [
                'Init'])], 'Init', 'Done')
        self.parentFSM = parentFSM
        self.parentFSM.getStateNamed('NameShop').addChild(self.fsm)
        self.nameGen = NameGenerator.NameGenerator()
        self.fsm.enterInitialState()
        return None

    
    def makeLabel(self, te, index, others):
        alig = others[0]
        listName = others[1]
        if alig == TextNode.ARight:
            newpos = (0.44, 0, 0)
        elif alig == TextNode.ALeft:
            newpos = (0, 0, 0)
        else:
            newpos = (0.20000000000000001, 0, 0)
        df = DirectFrame(state = 'normal', relief = None, text = te, text_scale = 0.10000000000000001, text_pos = newpos, text_align = alig, textMayChange = 0)
        df.bind(B1PRESS, lambda x, df = df: self.nameClickedOn(listName, index))
        return df

    
    def nameClickedOn(self, listType, index):
        if listType == 'title':
            self.titleIndex = index
        elif listType == 'first':
            self.firstIndex = index
        elif listType == 'prefix':
            self.prefixIndex = index
        else:
            self.suffixIndex = index
        self.updateLists()
        self._NameShop__listsChanged()

    
    def enter(self, toon, usedNames, warp):
        self.notify.debug('enter')
        self.newwarp = warp
        self.avExists = warp
        if self.avExists:
            for g in self.avList:
                if g.position == self.index:
                    self.avId = g.id
                
            
        
        if toon == None:
            return None
        else:
            self.toon = toon
            if self.toon.style.gender == 'm':
                self.boy = 1
                self.girl = 0
            else:
                self.boy = 0
                self.girl = 1
        self.usedNames = usedNames
        if not (self.addedGenderSpecific) or self.oldBoy != self.boy:
            self.oldBoy = self.boy
            self.listsLoaded = 0
            self.allTitles = [
                ' '] + [
                ' '] + self.nameGen.boyTitles * self.boy + self.nameGen.girlTitles * self.girl + self.nameGen.neutralTitles
            self.allTitles.sort()
            self.allTitles += [
                ' '] + [
                ' ']
            self.allFirsts = [
                ' '] + [
                ' '] + self.nameGen.boyFirsts * self.boy + self.nameGen.girlFirsts * self.girl + self.nameGen.neutralFirsts
            self.allFirsts.sort()
            self.allFirsts += [
                ' '] + [
                ' ']
            
            try:
                k = self.allFirsts.index('Von')
                self.allFirsts[k] = 'von'
            except:
                print "NameShop: Couldn't find von"

            self.pickANameGUIElements.remove(self.titleScrollList)
            self.pickANameGUIElements.remove(self.firstnameScrollList)
            self.titleScrollList.destroy()
            self.firstnameScrollList.destroy()
            nameShopGui = loader.loadModelOnce('phase_3/models/gui/nameshop_gui')
            self.titleScrollList = self.makeScrollList(nameShopGui, (-0.59999999999999998, 0, 0.20000000000000001), (1, 0.80000000000000004, 0.80000000000000004, 1), self.allTitles, self.makeLabel, [
                TextNode.ACenter,
                'title'])
            self.firstnameScrollList = self.makeScrollList(nameShopGui, (-0.20000000000000001, 0, 0.20000000000000001), (0.80000000000000004, 1, 0.80000000000000004, 1), self.allFirsts, self.makeLabel, [
                TextNode.ACenter,
                'first'])
            self.pickANameGUIElements.append(self.titleScrollList)
            self.pickANameGUIElements.append(self.firstnameScrollList)
            self.pickANameGUIElements.remove(self.titleHigh)
            self.pickANameGUIElements.remove(self.firstHigh)
            self.titleHigh.destroy()
            self.firstHigh.destroy()
            self.titleHigh = self.makeHighlight((-0.71036699999999997, 0.0, 0.12296700000000001))
            self.firstHigh = self.makeHighlight((-0.310367, 0.0, 0.12296700000000001))
            self.pickANameGUIElements.append(self.titleHigh)
            self.pickANameGUIElements.append(self.firstHigh)
            panel = nameShopGui.find('**/namePanel')
            self.namePanel = DirectFrame(parent = aspect2d, image = panel, relief = 'flat', scale = (0.75, 0.69999999999999996, 0.69999999999999996), state = 'disabled', pos = (-0.016333299999999999, 0, 0.103267), frameColor = (1, 1, 1, 0))
            self.pickANameGUIElements.append(self.namePanel)
            self.nameResult.reparentTo(self.namePanel)
            self.circle = nameShopGui.find('**/namePanelCircle')
            self.titleCheck = self.makeCheckBox((-0.61699999999999999, 0, 0.374), TTLocalizer.TitleCheckBox, (0, 0.25, 0.5, 1), self.titleToggle)
            self.firstCheck = self.makeCheckBox((-0.22800000000000001, 0, 0.374), TTLocalizer.FirstCheckBox, (0, 0.25, 0.5, 1), self.firstToggle)
            self.lastCheck = self.makeCheckBox((0.38200000000000001, 0, 0.374), TTLocalizer.LastCheckBox, (0, 0.25, 0.5, 1), self.lastToggle)
            del self.circle
            self.pickANameGUIElements.append(self.titleCheck)
            self.pickANameGUIElements.append(self.firstCheck)
            self.pickANameGUIElements.append(self.lastCheck)
            self.titleCheck.wrtReparentTo(self.namePanel)
            self.firstCheck.wrtReparentTo(self.namePanel)
            self.lastCheck.wrtReparentTo(self.namePanel)
            self.titleScrollList.decButton.wrtReparentTo(self.namePanel)
            self.firstnameScrollList.decButton.wrtReparentTo(self.namePanel)
            self.lastsuffixScrollList.decButton.wrtReparentTo(self.namePanel)
            self.lastprefixScrollList.decButton.wrtReparentTo(self.namePanel)
            self.titleScrollList.incButton.wrtReparentTo(self.namePanel)
            self.firstnameScrollList.incButton.wrtReparentTo(self.namePanel)
            self.lastsuffixScrollList.incButton.wrtReparentTo(self.namePanel)
            self.lastprefixScrollList.incButton.wrtReparentTo(self.namePanel)
            self.randomButton.reparentTo(self.namePanel)
            self.typeANameButton.reparentTo(self.namePanel)
            nameShopGui.removeNode()
            self.listsLoaded = 1
            self.addedGenderSpecific = 1
            self._NameShop__randomName()
        
        self.typeANameButton['text'] = TTLocalizer.TypeANameButton
        if self.isLoaded == 0:
            self.load()
        
        self.ubershow(self.pickANameGUIElements)
        self.acceptOnce('next', self._NameShop__createAvatar)
        self.acceptOnce('last', self._NameShop__handleBackward)
        self._NameShop__listsChanged()
        self.fsm.request('PayState')
        return None

    
    def _NameShop__overflowNameInput(self):
        self.rejectName(TTLocalizer.NameTooLong)

    
    def exit(self):
        self.notify.debug('exit')
        if self.isLoaded == 0:
            return None
        
        self.ignore('next')
        self.ignore('last')
        self.hideAll()
        return None

    
    def _NameShop__listsChanged(self):
        newname = ''
        if self.listsLoaded:
            if self.titleActive:
                self.showList(self.titleScrollList)
                self.titleHigh.show()
                newtitle = self.titleScrollList['items'][self.titleScrollList.index + 2]['text']
                self.nameIndices[0] = self.nameGen.returnUniqueID(newtitle, 0)
                newname += newtitle + ' '
            else:
                self.nameIndices[0] = -1
                self.stealth(self.titleScrollList)
                self.titleHigh.hide()
            if self.firstActive:
                self.showList(self.firstnameScrollList)
                self.firstHigh.show()
                newfirst = self.firstnameScrollList['items'][self.firstnameScrollList.index + 2]['text']
                if newfirst == 'von':
                    nt = 'Von'
                else:
                    nt = newfirst
                self.nameIndices[1] = self.nameGen.returnUniqueID(nt, 1)
                if not (self.titleActive) and newfirst == 'von':
                    newfirst = 'Von'
                    newname += newfirst
                else:
                    newname += newfirst
                if newfirst == 'von':
                    self.nameFlags[1] = 0
                else:
                    self.nameFlags[1] = 1
                if self.lastActive:
                    newname += ' '
                
            else:
                self.firstHigh.hide()
                self.stealth(self.firstnameScrollList)
                self.nameIndices[1] = -1
            if self.lastActive:
                self.showList(self.lastprefixScrollList)
                self.showList(self.lastsuffixScrollList)
                self.prefixHigh.show()
                self.suffixHigh.show()
                lp = self.lastprefixScrollList['items'][self.lastprefixScrollList.index + 2]['text']
                ls = self.lastsuffixScrollList['items'][self.lastsuffixScrollList.index + 2]['text']
                self.nameIndices[2] = self.nameGen.returnUniqueID(lp, 2)
                self.nameIndices[3] = self.nameGen.returnUniqueID(ls, 3)
                newname += lp
                if lp in self.nameGen.capPrefixes:
                    ls = ls.capitalize()
                    self.nameFlags[3] = 1
                else:
                    self.nameFlags[3] = 0
                newname += ls
            else:
                self.stealth(self.lastprefixScrollList)
                self.stealth(self.lastsuffixScrollList)
                self.prefixHigh.hide()
                self.suffixHigh.hide()
                self.nameIndices[2] = -1
                self.nameIndices[3] = -1
            self.titleIndex = self.titleScrollList.index + 2
            self.firstIndex = self.firstnameScrollList.index + 2
            self.prefixIndex = self.lastprefixScrollList.index + 2
            self.suffixIndex = self.lastsuffixScrollList.index + 2
            self.nameResult['text'] = newname
            self.names[0] = newname
        

    
    def makeScrollList(self, gui, ipos, mcolor, nitems, nitemMakeFunction, nitemMakeExtraArgs):
        self.notify.debug('makeScrollList - items %s' % str(nitems))
        it = nitems[:]
        ds = DirectScrolledList(items = it, itemMakeFunction = nitemMakeFunction, itemMakeExtraArgs = nitemMakeExtraArgs, parent = aspect2d, relief = None, command = self._NameShop__listsChanged, pos = ipos, scale = 0.59999999999999998, incButton_image = (gui.find('**/triangleButtonUp'), gui.find('**/triangleButtonDwn'), gui.find('**/triangleButtonRllvr'), gui.find('**/triangleButtonUp')), incButton_relief = None, incButton_scale = (1.2, 1.2, -1.2), incButton_pos = (0, 0, -0.54500000000000004), incButton_image0_color = mcolor, incButton_image1_color = mcolor, incButton_image2_color = mcolor, incButton_image3_color = Vec4(1, 1, 1, 0), decButton_image = (gui.find('**/triangleButtonUp'), gui.find('**/triangleButtonDwn'), gui.find('**/triangleButtonRllvr'), gui.find('**/triangleButtonUp')), decButton_relief = None, decButton_scale = (1.2, 1.2, 1.2), decButton_pos = (0, 0, 0.19500000000000001), decButton_image0_color = mcolor, decButton_image1_color = mcolor, decButton_image2_color = mcolor, decButton_image3_color = Vec4(1, 1, 1, 0), itemFrame_pos = (-0.20000000000000001, 0, 0.028000000000000001), itemFrame_scale = 1.0, itemFrame_relief = RAISED, itemFrame_frameSize = (-0.050000000000000003, 0.47999999999999998, -0.5, 0.10000000000000001), itemFrame_frameColor = mcolor, itemFrame_borderWidth = (0.01, 0.01), numItemsVisible = 5)
        return ds

    
    def makeCheckBox(self, npos, ntex, ntexcolor, comm):
        return DirectCheckButton(parent = aspect2d, relief = None, scale = 0.10000000000000001, boxBorder = 0.080000000000000002, boxImage = self.circle, boxImageScale = 4, boxImageColor = VBase4(0, 0.25, 0.5, 1), boxRelief = None, pos = npos, text = ntex, text_fg = ntexcolor, text_scale = 0.80000000000000004, text_pos = (0.20000000000000001, 0), indicator_pos = (-0.56666700000000003, 0, -0.044999999999999998), indicator_image_pos = (-0.26000000000000001, 0, 0.074999999999999997), command = comm, text_align = TextNode.ALeft)

    
    def makeHighlight(self, npos):
        return DirectFrame(parent = aspect2d, relief = 'flat', scale = (0.55200000000000005, 0, 0.11), state = 'disabled', frameSize = (-0.050000000000000003, 0.47999999999999998, -0.5, 0.10000000000000001), borderWidth = (0.01, 0.01), pos = npos, frameColor = (1, 0, 1, 0.40000000000000002))

    
    def titleToggle(self, value):
        self.titleActive = self.titleCheck['indicatorValue']
        if not self.titleActive and self.firstActive:
            pass
        if not (self.lastActive):
            self.titleActive = 1
        
        self._NameShop__listsChanged()
        if self.titleActive:
            self.titleScrollList.refresh()
        
        self.updateCheckBoxes()

    
    def firstToggle(self, value):
        self.firstActive = self.firstCheck['indicatorValue']
        if self.chastise == 2:
            messenger.send('NameShop-mickeyChange', [
                [
                    TTLocalizer.ApprovalForName1,
                    TTLocalizer.ApprovalForName2]])
            self.chastise = 0
        
        if not self.firstActive:
            pass
        if not (self.lastActive):
            self.firstActive = 1
            messenger.send('NameShop-mickeyChange', [
                [
                    TTLocalizer.MustHaveAFirstOrLast1,
                    TTLocalizer.MustHaveAFirstOrLast2]])
            self.chastise = 1
        
        self._NameShop__listsChanged()
        if self.firstActive:
            self.firstnameScrollList.refresh()
        
        self.updateCheckBoxes()

    
    def lastToggle(self, value):
        self.lastActive = self.lastCheck['indicatorValue']
        if self.chastise == 1:
            messenger.send('NameShop-mickeyChange', [
                [
                    TTLocalizer.ApprovalForName1,
                    TTLocalizer.ApprovalForName2]])
            self.chastise = 0
        
        if not self.firstActive:
            pass
        if not (self.lastActive):
            self.lastActive = 1
            messenger.send('NameShop-mickeyChange', [
                [
                    TTLocalizer.MustHaveAFirstOrLast1,
                    TTLocalizer.MustHaveAFirstOrLast2]])
            self.chastise = 2
        
        self._NameShop__listsChanged()
        if self.lastActive:
            self.lastprefixScrollList.refresh()
            self.lastsuffixScrollList.refresh()
        
        self.updateCheckBoxes()

    
    def updateCheckBoxes(self):
        self.titleCheck['indicatorValue'] = self.titleActive
        self.titleCheck.setIndicatorValue()
        self.firstCheck['indicatorValue'] = self.firstActive
        self.firstCheck.setIndicatorValue()
        self.lastCheck['indicatorValue'] = self.lastActive
        self.lastCheck.setIndicatorValue()

    
    def load(self):
        self.notify.debug('load')
        if self.isLoaded == 1:
            return None
        
        nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        gui = loader.loadModelOnce('phase_3/models/gui/nameshop_gui')
        typePanel = gui.find('**/typeNamePanel')
        self.typeNamePanel = DirectFrame(parent = aspect2d, image = typePanel, relief = 'flat', scale = (0.75, 0.69999999999999996, 0.69999999999999996), state = 'disabled', pos = (-0.016333299999999999, 0, 0.074999999999999997), frameColor = (1, 1, 1, 0))
        self.typeANameGUIElements.append(self.typeNamePanel)
        self.nameLabel = OnscreenText.OnscreenText(TTLocalizer.PleaseTypeName, parent = aspect2d, style = OnscreenText.ScreenPrompt, pos = (0, 0.53000000000000003))
        self.typeANameGUIElements.append(self.nameLabel)
        self.typeNotification = OnscreenText.OnscreenText(TTLocalizer.AllNewNames, parent = aspect2d, style = OnscreenText.ScreenPrompt, pos = (0, 0.14999999999999999))
        self.typeANameGUIElements.append(self.typeNotification)
        self.nameEntry = DirectEntry(parent = aspect2d, relief = None, scale = 0.080000000000000002, entryFont = getToonFont(), width = MAX_NAME_WIDTH, numLines = 2, focus = 0, cursorKeys = 1, pos = (0.0, 0.0, 0.39000000000000001), text_align = TextNode.ACenter, command = self._NameShop__typedAName)
        self.typeANameGUIElements.append(self.nameEntry)
        self.submitButton = DirectButton(parent = aspect2d, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1.2, 0, 1.1000000000000001), pos = (-0.01, 0, -0.25), text = TTLocalizer.NameShopSubmitButton, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._NameShop__typedAName)
        self.typeANameGUIElements.append(self.submitButton)
        self.randomButton = DirectButton(parent = aspect2d, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1.1499999999999999, 1.1000000000000001, 1.1000000000000001), scale = (1.3999999999999999, 1, 1.3999999999999999), pos = (0.01, 0, -0.5), text = TTLocalizer.RandomButton, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._NameShop__randomName)
        self.pickANameGUIElements.append(self.randomButton)
        self.typeANameButton = DirectButton(parent = aspect2d, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1, 1.1000000000000001, 0.90000000000000002), pos = (0.01, 0, -0.69499999999999995), scale = (1.6000000000000001, 1, 1.7), text = TTLocalizer.TypeANameButton, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._NameShop__typeAName)
        if base.cr.productName == 'Terra-DMC':
            self.typeANameButton.hide()
        
        self.pickANameGUIElements.append(self.typeANameButton)
        self.nameResult = DirectLabel(parent = aspect2d, relief = None, scale = 0.12, pos = (0.040000000000000001, 0, 0.69999999999999996), text = ' \n ', text_align = TextNode.ACenter, text_wordwrap = MAX_NAME_WIDTH)
        self.pickANameGUIElements.append(self.nameResult)
        self.allPrefixes = self.nameGen.lastPrefixes[:]
        self.allSuffixes = self.nameGen.lastSuffixes[:]
        self.allPrefixes.sort()
        self.allSuffixes.sort()
        self.allPrefixes = [
            ' '] + [
            ' '] + self.allPrefixes + [
            ' '] + [
            ' ']
        self.allSuffixes = [
            ' '] + [
            ' '] + self.allSuffixes + [
            ' '] + [
            ' ']
        self.titleScrollList = self.makeScrollList(gui, (-0.59999999999999998, 0, 0.20000000000000001), (1, 0.80000000000000004, 0.80000000000000004, 1), self.allTitles, self.makeLabel, [
            TextNode.ACenter,
            'title'])
        self.firstnameScrollList = self.makeScrollList(gui, (-0.20000000000000001, 0, 0.20000000000000001), (0.80000000000000004, 1, 0.80000000000000004, 1), self.allFirsts, self.makeLabel, [
            TextNode.ACenter,
            'first'])
        self.lastprefixScrollList = self.makeScrollList(gui, (0.20000000000000001, 0, 0.20000000000000001), (0.80000000000000004, 0.80000000000000004, 1, 1), self.allPrefixes, self.makeLabel, [
            TextNode.ARight,
            'prefix'])
        self.lastsuffixScrollList = self.makeScrollList(gui, (0.55000000000000004, 0, 0.20000000000000001), (0.80000000000000004, 0.80000000000000004, 1, 1), self.allSuffixes, self.makeLabel, [
            TextNode.ALeft,
            'suffix'])
        gui.removeNode()
        self.pickANameGUIElements.append(self.lastprefixScrollList)
        self.pickANameGUIElements.append(self.lastsuffixScrollList)
        self.pickANameGUIElements.append(self.titleScrollList)
        self.pickANameGUIElements.append(self.firstnameScrollList)
        self.titleHigh = self.makeHighlight((-0.71036699999999997, 0.0, 0.12296700000000001))
        self.firstHigh = self.makeHighlight((-0.310367, 0.0, 0.12296700000000001))
        self.pickANameGUIElements.append(self.titleHigh)
        self.pickANameGUIElements.append(self.firstHigh)
        self.prefixHigh = self.makeHighlight((0.089999999999999997, 0.0, 0.12296700000000001))
        self.suffixHigh = self.makeHighlight((0.44, 0.0, 0.12296700000000001))
        self.pickANameGUIElements.append(self.prefixHigh)
        self.pickANameGUIElements.append(self.suffixHigh)
        nameBalloon.removeNode()
        imageList = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
        buttonImage = [
            imageList,
            imageList]
        buttonText = [
            TTLocalizer.NameShopPay,
            TTLocalizer.NameShopPlay]
        self.payDialog = DirectDialog(dialogName = 'paystate', topPad = 0, fadeScreen = 0.20000000000000001, pos = (0, 0.10000000000000001, 0.10000000000000001), button_relief = None, text_align = TextNode.ACenter, text = TTLocalizer.NameShopOnlyPaid, buttonTextList = buttonText, buttonImageList = buttonImage, image_color = GlobalDialogColor, buttonValueList = [
            1,
            0], command = self.payAction)
        self.payDialog.buttonList[0].setPos(0, 0, -0.27000000000000002)
        self.payDialog.buttonList[1].setPos(0, 0, -0.40000000000000002)
        self.payDialog.buttonList[0]['image_scale'] = (1.2, 1, 1.1000000000000001)
        self.payDialog.buttonList[1]['image_scale'] = (1.2, 1, 1.1000000000000001)
        self.payDialog['image_scale'] = (0.80000000000000004, 1, 0.77000000000000002)
        self.payDialog.buttonList[0]['text_pos'] = (0, -0.02)
        self.payDialog.buttonList[1]['text_pos'] = (0, -0.02)
        self.payDialog.hide()
        buttonText = [
            TTLocalizer.NameShopContinueSubmission,
            TTLocalizer.NameShopChooseAnother]
        self.approvalDialog = DirectDialog(dialogName = 'approvalstate', topPad = 0, fadeScreen = 0.20000000000000001, pos = (0, 0.10000000000000001, 0.10000000000000001), button_relief = None, image_color = GlobalDialogColor, text_align = TextNode.ACenter, text = TTLocalizer.NameShopToonCouncil, buttonTextList = buttonText, buttonImageList = buttonImage, buttonValueList = [
            1,
            0], command = self.approvalAction)
        self.approvalDialog.buttonList[0].setPos(0, 0, -0.29999999999999999)
        self.approvalDialog.buttonList[1].setPos(0, 0, -0.42999999999999999)
        self.approvalDialog['image_scale'] = (0.80000000000000004, 1, 0.77000000000000002)
        for x in range(0, 2):
            self.approvalDialog.buttonList[x]['text_pos'] = (0, -0.01)
            self.approvalDialog.buttonList[x]['text_scale'] = (0.040000000000000001, 0.059990000000000002)
            self.approvalDialog.buttonList[x].setScale(1.2, 1, 1)
        
        self.approvalDialog.hide()
        guiButton.removeNode()
        self.uberhide(self.typeANameGUIElements)
        self.uberhide(self.pickANameGUIElements)
        self.isLoaded = 1
        return None

    
    def ubershow(self, guiObjectsToShow):
        self.notify.debug('ubershow %s' % str(guiObjectsToShow))
        for x in guiObjectsToShow:
            
            try:
                x.show()
            except:
                print 'NameShop: Tried to show already removed object'

        
        if base.cr.productName == 'Terra-DMC':
            self.typeANameButton.hide()
        

    
    def hideAll(self):
        self.uberhide(self.pickANameGUIElements)
        self.uberhide(self.typeANameGUIElements)

    
    def uberhide(self, guiObjectsToHide):
        self.notify.debug('uberhide %s' % str(guiObjectsToHide))
        for x in guiObjectsToHide:
            
            try:
                x.hide()
            except:
                print 'NameShop: Tried to hide already removed object'

        

    
    def uberdestroy(self, guiObjectsToDestroy):
        self.notify.debug('uberdestroy %s' % str(guiObjectsToDestroy))
        for x in guiObjectsToDestroy:
            
            try:
                x.destroy()
                del x
            except:
                print 'NameShop: Tried to destroy already removed object'

        

    
    def getNameIndices(self):
        return self.nameIndices

    
    def getNameFlags(self):
        return self.nameFlags

    
    def getNameAction(self):
        return self.nameAction

    
    def unload(self):
        self.notify.debug('unload')
        if self.isLoaded == 0:
            return None
        
        self.exit()
        cleanupDialog('globalDialog')
        self.uberdestroy(self.pickANameGUIElements)
        self.uberdestroy(self.typeANameGUIElements)
        del self.toon
        self.payDialog.cleanup()
        self.approvalDialog.cleanup()
        del self.payDialog
        del self.approvalDialog
        self.parentFSM.getStateNamed('NameShop').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.ignoreAll()
        self.isLoaded = 0
        return None

    
    def nameIsValid(self, name):
        self.notify.debug('nameIsValid')
        if name in self.usedNames:
            return TTLocalizer.ToonAlreadyExists % name
        
        problem = NameCheck.checkName(name)
        if problem:
            return problem
        
        return None

    
    def setShopsVisited(self, list):
        self.shopsVisited = list

    
    def _NameShop__handleBackward(self):
        self.doneStatus = 'last'
        messenger.send(self.doneEvent)

    
    def _NameShop__handleChastised(self):
        self.chastiseDialog.cleanup()

    
    def _NameShop__createAvatar(self, *args):
        self.notify.debug('__createAvatar')
        if self.fsm.getCurrentState().getName() == 'TypeAName':
            self._NameShop__typedAName()
            return None
        
        if not (self.avExists):
            self.serverCreateAvatar()
        elif self.names[0] == '':
            self.rejectName(TTLocalizer.EmptyNameError)
        elif self.avId == 'deleteMe':
            self.serverCreateAvatar()
        else:
            rejectReason = self.nameIsValid(self.names[0])
            if rejectReason != None:
                self.rejectName(rejectReason)
            else:
                self.checkNamePattern()

    
    def acceptName(self):
        self.notify.debug('acceptName')
        self.toon.setName(self.names[0])
        self.doneStatus = 'done'
        messenger.send(self.doneEvent)

    
    def rejectName(self, str):
        self.notify.debug('rejectName')
        self.names[0] = ''
        self.rejectDialog = TTDialog.TTGlobalDialog(doneEvent = 'rejectDone', message = str, style = TTDialog.Acknowledge)
        self.rejectDialog.show()
        self.acceptOnce('rejectDone', self._NameShop__handleReject)

    
    def _NameShop__handleReject(self):
        self.rejectDialog.cleanup()
        self.nameEntry['focus'] = 1
        self.acceptOnce('next', self._NameShop__createAvatar)

    
    def restoreIndexes(self, oi):
        self.titleIndex = oi[0]
        self.firstIndex = oi[1]
        self.prefixIndex = oi[2]
        self.suffixIndex = oi[3]

    
    def stealth(self, listToDo):
        listToDo.decButton['state'] = 'disabled'
        listToDo.incButton['state'] = 'disabled'
        for item in listToDo['items']:
            if item.__class__.__name__ != 'str':
                item.hide()
            
        

    
    def showList(self, listToDo):
        listToDo.show()
        listToDo.decButton['state'] = 'normal'
        listToDo.incButton['state'] = 'normal'

    
    def updateLists(self):
        oldindex = [
            self.titleIndex,
            self.firstIndex,
            self.prefixIndex,
            self.suffixIndex]
        self.titleScrollList.scrollTo(self.titleIndex - 2)
        self.restoreIndexes(oldindex)
        self.firstnameScrollList.scrollTo(self.firstIndex - 2)
        self.restoreIndexes(oldindex)
        self.lastprefixScrollList.scrollTo(self.prefixIndex - 2)
        self.restoreIndexes(oldindex)
        self.lastsuffixScrollList.scrollTo(self.suffixIndex - 2)
        self.restoreIndexes(oldindex)

    
    def _NameShop__randomName(self):
        self.notify.debug('Finding random name')
        uberReturn = self.nameGen.randomNameMoreinfo(self.boy, self.girl)
        self.names[0] = uberReturn[len(uberReturn) - 1]
        self.titleActive = 0
        self.firstActive = 0
        self.lastActive = 0
        if uberReturn[0]:
            self.titleActive = 1
        
        if uberReturn[1]:
            self.firstActive = 1
        
        if uberReturn[2]:
            self.lastActive = 1
        
        
        try:
            self.titleIndex = self.allTitles.index(uberReturn[3])
            self.nameIndices[0] = self.nameGen.returnUniqueID(uberReturn[3], 0)
            self.nameFlags[0] = 1
        except:
            print 'NameShop : Should have found title, uh oh!'
            print uberReturn

        
        try:
            self.firstIndex = self.allFirsts.index(uberReturn[4])
            self.nameIndices[1] = self.nameGen.returnUniqueID(uberReturn[4], 1)
            self.nameFlags[1] = 1
        except:
            print 'NameShop : Should have found first name, uh oh!'
            print uberReturn

        
        try:
            self.prefixIndex = self.allPrefixes.index(uberReturn[5])
            self.suffixIndex = self.allSuffixes.index(uberReturn[6].lower())
            self.nameIndices[2] = self.nameGen.returnUniqueID(uberReturn[5], 2)
            self.nameIndices[3] = self.nameGen.returnUniqueID(uberReturn[6].lower(), 3)
            if uberReturn[5] in self.nameGen.capPrefixes:
                self.nameFlags[3] = 1
            else:
                self.nameFlags[3] = 0
        except:
            print 'NameShop : Some part of last name not found, uh oh!'
            print uberReturn

        self.updateCheckBoxes()
        self.updateLists()
        self.nameResult['text'] = self.names[0]

    
    def findTempName(self):
        colorstring = TTLocalizer.NumToColor[self.toon.style.headColor]
        animaltype = TTLocalizer.AnimalToSpecies[self.toon.style.getAnimal()]
        tempname = colorstring + ' ' + animaltype
        self.names[0] = tempname
        tempname = '"' + tempname + '"'
        return tempname

    
    def enterInit(self):
        self.notify.debug('enterInit')

    
    def exitInit(self):
        pass

    
    def enterPayState(self):
        self.notify.debug('enterPayState')
        if base.cr.allowFreeNames() or self.isPaid:
            self.fsm.request('PickAName')
        else:
            tempname = self.findTempName()
            self.payDialog['text'] = TTLocalizer.NameShopOnlyPaid + tempname
            self.payDialog.show()

    
    def exitPayState(self):
        pass

    
    def payAction(self, value):
        self.notify.debug('payAction')
        self.payDialog.hide()
        if value:
            self.doneStatus = 'paynow'
            messenger.send(self.doneEvent)
        else:
            self.nameAction = 0
            self._NameShop__createAvatar()

    
    def enterPickANameState(self):
        self.notify.debug('enterPickANameState')
        self.ubershow(self.pickANameGUIElements)
        self.nameAction = 1
        self._NameShop__listsChanged()

    
    def exitPickANameState(self):
        self.uberhide(self.pickANameGUIElements)

    
    def enterTypeANameState(self):
        self.notify.debug('enterTypeANameState')
        self.ubershow(self.typeANameGUIElements)
        self.typeANameButton.show()
        self.nameEntry.set('')
        self.nameEntry['focus'] = 1

    
    def _NameShop__typeAName(self):
        if base.restrictTrialers:
            if not base.cr.isPaid():
                dialog = TeaserPanel.TeaserPanel(pageName = 'typeAName')
                return None
            
        
        if self.fsm.getCurrentState().getName() == 'TypeAName':
            self.typeANameButton['text'] = TTLocalizer.TypeANameButton
            self.typeANameButton.wrtReparentTo(self.namePanel)
            self.fsm.request('PickAName')
        else:
            self.typeANameButton['text'] = TTLocalizer.PickANameButton
            self.typeANameButton.wrtReparentTo(aspect2d)
            self.typeANameButton.show()
            self.fsm.request('TypeAName')

    
    def _NameShop__typedAName(self, *args):
        self.notify.debug('__typedAName')
        self.nameEntry['focus'] = 0
        name = self.nameEntry.get()
        self.nameEntry.enterText(name.strip())
        problem = self.nameIsValid(self.nameEntry.get())
        if problem:
            self.rejectName(problem)
            return None
        
        if not (self.avExists):
            self.nameAction = 2
            self.serverCreateAvatar()
        else:
            self.checkNameTyped()

    
    def exitTypeANameState(self):
        self.uberhide(self.typeANameGUIElements)

    
    def enterApprovalState(self):
        self.notify.debug('enterApprovalState')
        tempname = self.findTempName()
        self.approvalDialog['text'] = TTLocalizer.NameShopToonCouncil + tempname
        self.approvalDialog.show()

    
    def approvalAction(self, value):
        self.notify.debug('approvalAction')
        self.approvalDialog.hide()
        if value:
            self.doneStatus = 'done'
            messenger.send(self.doneEvent)
        elif self.avExists and not (self.newwarp):
            self.avExists = 0
            self.sendDeleteAvatarMsgCancelStyle(self.avId)
            for x in self.avList:
                if x.id == self.avId:
                    self.avList.remove(x)
                
            
        else:
            datagram = PyDatagram()
            datagram.addUint16(CLIENT_SET_WISHNAME_CLEAR)
            datagram.addUint32(self.avId)
            datagram.addUint8(0)
            messenger.send('nameShopPost', [
                datagram])
        self.typeANameButton['text'] = TTLocalizer.TypeANameButton
        self.fsm.request('PickAName')

    
    def sendDeleteAvatarMsgCancelStyle(self, avId):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_DELETE_AVATAR)
        datagram.addUint32(avId)
        messenger.send('nameShopPost', [
            datagram])
        return None

    
    def exitApprovalState(self):
        pass

    
    def enterAcceptedState(self):
        self.notify.debug('enterAcceptedState')
        self.acceptedDialog = TTDialog.TTGlobalDialog(doneEvent = 'acceptedDone', message = TTLocalizer.NameShopNameAccepted, style = TTDialog.Acknowledge)
        self.acceptedDialog.show()
        self.acceptOnce('acceptedDone', self._NameShop__handleAccepted)

    
    def _NameShop__handleAccepted(self):
        self.acceptedDialog.cleanup()
        self.doneStatus = 'done'
        messenger.send(self.doneEvent)

    
    def exitAcceptedState(self):
        pass

    
    def enterRejectedState(self):
        self.notify.debug('enterRejectedState')
        self.rejectedDialog = TTDialog.TTGlobalDialog(doneEvent = 'rejectedDone', message = TTLocalizer.NameShopNameRejected, style = TTDialog.Acknowledge)
        self.rejectedDialog.show()
        self.acceptOnce('rejectedDone', self._NameShop__handleRejected)

    
    def _NameShop__handleRejected(self):
        self.rejectedDialog.cleanup()
        self.fsm.request('TypeAName')

    
    def exitRejectedState(self):
        pass

    
    def enterDone(self):
        self.notify.debug('enterDone')
        return None

    
    def exitDone(self):
        return None

    
    def nameShopHandler(self, msgType, di):
        self.notify.debug('nameShopHandler')
        if msgType == CLIENT_CREATE_AVATAR_RESP:
            self.handleCreateAvatarResponseMsg(di)
        elif msgType == CLIENT_SET_NAME_PATTERN_ANSWER:
            self.handleSetNamePatternAnswerMsg(di)
        elif msgType == CLIENT_SET_WISHNAME_RESP:
            self.handleSetNameTypedAnswerMsg(di)
        
        return None

    
    def checkNamePattern(self):
        self.notify.debug('checkNamePattern')
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_NAME_PATTERN)
        datagram.addUint32(self.avId)
        datagram.addUint16(self.nameIndices[0])
        datagram.addUint16(self.nameFlags[0])
        datagram.addUint16(self.nameIndices[1])
        datagram.addUint16(self.nameFlags[1])
        datagram.addUint16(self.nameIndices[2])
        datagram.addUint16(self.nameFlags[2])
        datagram.addUint16(self.nameIndices[3])
        datagram.addUint16(self.nameFlags[3])
        messenger.send('nameShopPost', [
            datagram])
        self.waitForServer()

    
    def handleSetNamePatternAnswerMsg(self, di):
        self.notify.debug('handleSetNamePatternAnswerMsg')
        self.cleanupWaitForServer()
        newavId = di.getUint32()
        if newavId != self.avId:
            self.notify.debug("doid's don't match up!")
            self.rejectName(TTLocalizer.NameError)
        
        returnCode = di.getUint8()
        if returnCode == 0:
            style = self.toon.getStyle()
            avDNA = style.makeNetString()
            self.notify.debug('pattern name accepted')
            newPotAv = PotentialAvatar.PotentialAvatar(newavId, self.names, avDNA, self.index, 0)
            self.avList.append(newPotAv)
            self.doneStatus = 'done'
            messenger.send(self.doneEvent)
        else:
            self.notify.debug('name pattern rejected')
            self.rejectName(TTLocalizer.NameError)
        return None

    
    def checkNameTyped(self):
        self.notify.debug('checkNameTyped')
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_WISHNAME)
        datagram.addUint32(self.avId)
        datagram.addString(self.nameEntry.get())
        messenger.send('nameShopPost', [
            datagram])
        self.waitForServer()

    
    def handleSetNameTypedAnswerMsg(self, di):
        self.notify.debug('handleSetNameTypedAnswerMsg')
        self.cleanupWaitForServer()
        newavId = di.getUint32()
        if newavId != self.avId:
            self.notify.debug("doid's don't match up!")
            self.rejectName(TTLocalizer.NameError)
        
        returnCode = di.getUint16()
        if returnCode == 0:
            wishname = di.getString()
            approvedname = di.getString()
            rejectedname = di.getString()
            if approvedname != '':
                style = self.toon.getStyle()
                avDNA = style.makeNetString()
                self.names[0] = self.nameEntry.get()
                self.notify.debug('typed name accepted')
                newPotAv = PotentialAvatar.PotentialAvatar(newavId, self.names, avDNA, self.index, 0)
                self.avList.append(newPotAv)
                self.fsm.request('Accepted')
            elif wishname != '':
                style = self.toon.getStyle()
                avDNA = style.makeNetString()
                self.names[1] = self.nameEntry.get()
                self.notify.debug('typed name needs approval')
                newPotAv = PotentialAvatar.PotentialAvatar(newavId, self.names, avDNA, self.index, 1)
                if not (self.newwarp):
                    self.avList.append(newPotAv)
                
                self.fsm.request('Approval')
            elif rejectedname != '':
                self.fsm.request('Rejected')
            else:
                self.notify.debug("name typed accepted but didn't fill any return fields")
                self.rejectName(TTLocalizer.NameError)
        else:
            self.notify.debug('name typed rejected')
            self.rejectName(TTLocalizer.NameError)
        return None

    
    def serverCreateAvatar(self):
        self.notify.debug('serverCreateAvatar')
        style = self.toon.getStyle()
        self.newDNA = style.makeNetString()
        messenger.send('nameShopCreateAvatar', [
            style,
            '',
            self.index])

    
    def handleCreateAvatarResponseMsg(self, di):
        self.notify.debug('handleCreateAvatarResponseMsg')
        echoContext = di.getUint16()
        returnCode = di.getUint8()
        if returnCode == 0:
            self.notify.debug('avatar with default name accepted')
            self.avId = di.getUint32()
            self.avExists = 1
            if self.nameAction == 0:
                self.toon.setName(self.names[0])
                newPotAv = PotentialAvatar.PotentialAvatar(self.avId, self.names, self.newDNA, self.index, 1)
                self.avList.append(newPotAv)
                self.doneStatus = 'done'
                messenger.send(self.doneEvent)
            elif self.nameAction == 1:
                self.checkNamePattern()
            elif self.nameAction == 2:
                self.checkNameTyped()
            else:
                self.notify.debug('avatar invalid nameAction')
                self.rejectName(TTLocalizer.NameError)
        else:
            self.notify.debug('avatar rejected')
            self.rejectName(TTLocalizer.NameError)
        return None

    
    def waitForServer(self):
        self.waitForServerDialog = TTDialog.TTDialog(text = TTLocalizer.WaitingForNameSubmission, style = TTDialog.NoButtons)
        self.waitForServerDialog.show()

    
    def cleanupWaitForServer(self):
        if self.waitForServerDialog != None:
            self.waitForServerDialog.cleanup()
            self.waitForServerDialog = None
        


