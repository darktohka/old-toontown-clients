# File: C (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase import PandaObject
from toontown.toon import ToonDNA
from direct.fsm import StateData
from direct.gui.DirectGui import *
from MakeAToonGlobals import *
import whrandom
from toontown.toonbase import TTLocalizer

class ColorShop(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.toon = None
        self.colorAll = 1
        return None

    
    def getGenderColorList(self, dna):
        if self.dna.getGender() == 'm':
            return ToonDNA.defaultBoyColorList
        else:
            return ToonDNA.defaultGirlColorList

    
    def enter(self, toon, shopsVisited = []):
        base.disableMouse()
        self.toon = toon
        self.dna = toon.getStyle()
        colorList = self.getGenderColorList(self.dna)
        if COLORSHOP not in shopsVisited:
            self.headChoice = whrandom.choice(colorList)
            self.armChoice = self.headChoice
            self.legChoice = self.headChoice
            self.startColor = self.headChoice
            self._ColorShop__swapHeadColor(0)
            self._ColorShop__swapArmColor(0)
            self._ColorShop__swapLegColor(0)
            self.allLButton['state'] = DISABLED
            self.headLButton['state'] = DISABLED
            self.armLButton['state'] = DISABLED
            self.legLButton['state'] = DISABLED
        else:
            
            try:
                self.headChoice = colorList.index(self.dna.headColor)
                self.armChoice = colorList.index(self.dna.armColor)
                self.legChoice = colorList.index(self.dna.legColor)
            except:
                self.headChoice = whrandom.choice(colorList)
                self.armChoice = self.headChoice
                self.legChoice = self.headChoice
                self._ColorShop__swapHeadColor(0)
                self._ColorShop__swapArmColor(0)
                self._ColorShop__swapLegColor(0)

        self.acceptOnce('last', self._ColorShop__handleBackward)
        self.acceptOnce('next', self._ColorShop__handleForward)
        return None

    
    def showButtons(self):
        if self.colorAll:
            self.allLButton.show()
            self.allRButton.show()
            self.headLButton.hide()
            self.headRButton.hide()
            self.armLButton.hide()
            self.armRButton.hide()
            self.legLButton.hide()
            self.legRButton.hide()
        else:
            self.allLButton.hide()
            self.allRButton.hide()
            self.headLButton.show()
            self.headRButton.show()
            self.armLButton.show()
            self.armRButton.show()
            self.legLButton.show()
            self.legRButton.show()
        self.toggleAllButton.show()
        return None

    
    def hideButtons(self):
        self.allLButton.hide()
        self.allRButton.hide()
        self.headLButton.hide()
        self.headRButton.hide()
        self.armLButton.hide()
        self.armRButton.hide()
        self.legLButton.hide()
        self.legRButton.hide()
        self.toggleAllButton.hide()

    
    def exit(self):
        self.ignore('last')
        self.ignore('next')
        self.ignore('enter')
        
        try:
            del self.toon
        except:
            print 'ColorShop: toon not found'

        self.hideButtons()
        return None

    
    def load(self):
        self.gui = loader.loadModelOnce('phase_3/models/gui/create_a_toon_gui')
        guiRArrowDown = self.gui.find('**/CrtATn_R_Arrow_DN')
        guiRArrowRollover = self.gui.find('**/CrtATn_R_Arrow_RLVR')
        guiRArrowUp = self.gui.find('**/CrtATn_R_Arrow_UP')
        self.headLButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), image_scale = (-1, 1, 1), text = TTLocalizer.ColorShopHead, text_scale = 0.0625, text_pos = (0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (-0.90000000000000002, 0, 0.29999999999999999), command = self._ColorShop__swapHeadColor, extraArgs = [
            -1])
        self.headRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = TTLocalizer.ColorShopHead, text_scale = 0.0625, text_pos = (-0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (0, 0, 0.29999999999999999), command = self._ColorShop__swapHeadColor, extraArgs = [
            1])
        self.armLButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), image_scale = (-1, 1, 1), text = TTLocalizer.ColorShopBody, text_scale = 0.0625, text_pos = (0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (-0.90000000000000002, 0, -0.10000000000000001), command = self._ColorShop__swapArmColor, extraArgs = [
            -1])
        self.armRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = TTLocalizer.ColorShopBody, text_scale = 0.0625, text_pos = (-0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (0, 0, -0.10000000000000001), command = self._ColorShop__swapArmColor, extraArgs = [
            1])
        self.allLButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), image_scale = (-1, 1, 1), text = TTLocalizer.ColorShopToon, text_scale = 0.0625, text_pos = (0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (-0.90000000000000002, 0, -0.10000000000000001), command = self._ColorShop__swapAllColor, extraArgs = [
            -1])
        self.allRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = TTLocalizer.ColorShopToon, text_scale = 0.0625, text_pos = (-0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (0, 0, -0.10000000000000001), command = self._ColorShop__swapAllColor, extraArgs = [
            1])
        self.legLButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), image_scale = (-1, 1, 1), text = TTLocalizer.ColorShopLegs, text_scale = 0.0625, text_pos = (0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (-0.90000000000000002, 0, -0.5), command = self._ColorShop__swapLegColor, extraArgs = [
            -1])
        self.legRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = TTLocalizer.ColorShopLegs, text_scale = 0.0625, text_pos = (-0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (0, 0, -0.5), command = self._ColorShop__swapLegColor, extraArgs = [
            1])
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.toggleAllButton = DirectButton(parent = aspect2d, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.80000000000000004, 1.1000000000000001, 1.1000000000000001), pos = (-0.10000000000000001, 0, 0.55000000000000004), text = TTLocalizer.ColorShopParts, text_scale = 0.059999999999999998, text_pos = (0.0, -0.02), command = self._ColorShop__toggleAllColor)
        guiButton.removeNode()
        self.headLButton.hide()
        self.headRButton.hide()
        self.armLButton.hide()
        self.armRButton.hide()
        self.legLButton.hide()
        self.legRButton.hide()
        self.allLButton.hide()
        self.allRButton.hide()
        self.toggleAllButton.hide()
        return None

    
    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.headLButton.destroy()
        self.headRButton.destroy()
        self.armLButton.destroy()
        self.armRButton.destroy()
        self.legLButton.destroy()
        self.legRButton.destroy()
        self.allLButton.destroy()
        self.allRButton.destroy()
        self.toggleAllButton.destroy()
        del self.headLButton
        del self.headRButton
        del self.armLButton
        del self.armRButton
        del self.legLButton
        del self.legRButton
        del self.allLButton
        del self.allRButton
        del self.toggleAllButton
        return None

    
    def _ColorShop__toggleAllColor(self):
        if self.colorAll:
            self.colorAll = 0
            self.toggleAllButton['text'] = TTLocalizer.ColorShopAll
        else:
            self.colorAll = 1
            self.toggleAllButton['text'] = TTLocalizer.ColorShopParts
            self.legChoice = self.headChoice
            self.armChoice = self.headChoice
            self._ColorShop__swapAllColor(0)
        self.showButtons()

    
    def _ColorShop__swapAllColor(self, offset):
        colorList = self.getGenderColorList(self.dna)
        length = len(colorList)
        choice = (self.headChoice + offset) % length
        self._ColorShop__updateScrollButtons(choice, length, self.allLButton, self.allRButton)
        self._ColorShop__swapHeadColor(offset)
        self._ColorShop__swapArmColor(offset)
        self._ColorShop__swapLegColor(offset)

    
    def _ColorShop__swapHeadColor(self, offset):
        colorList = self.getGenderColorList(self.dna)
        length = len(colorList)
        self.headChoice = (self.headChoice + offset) % length
        self._ColorShop__updateScrollButtons(self.headChoice, length, self.headLButton, self.headRButton)
        newColor = colorList[self.headChoice]
        self.dna.headColor = newColor
        self.toon.swapToonColor(self.dna)

    
    def _ColorShop__swapArmColor(self, offset):
        colorList = self.getGenderColorList(self.dna)
        length = len(colorList)
        self.armChoice = (self.armChoice + offset) % length
        self._ColorShop__updateScrollButtons(self.armChoice, length, self.armLButton, self.armRButton)
        newColor = colorList[self.armChoice]
        self.dna.armColor = newColor
        self.toon.swapToonColor(self.dna)

    
    def _ColorShop__swapLegColor(self, offset):
        colorList = self.getGenderColorList(self.dna)
        length = len(colorList)
        self.legChoice = (self.legChoice + offset) % length
        self._ColorShop__updateScrollButtons(self.legChoice, length, self.legLButton, self.legRButton)
        newColor = colorList[self.legChoice]
        self.dna.legColor = newColor
        self.toon.swapToonColor(self.dna)

    
    def _ColorShop__updateScrollButtons(self, choice, length, lButton, rButton):
        if choice == (self.startColor - 1) % length:
            rButton['state'] = DISABLED
        else:
            rButton['state'] = NORMAL
        if choice == self.startColor % length:
            lButton['state'] = DISABLED
        else:
            lButton['state'] = NORMAL

    
    def _ColorShop__handleForward(self):
        self.doneStatus = 'next'
        messenger.send(self.doneEvent)

    
    def _ColorShop__handleBackward(self):
        self.doneStatus = 'last'
        messenger.send(self.doneEvent)


