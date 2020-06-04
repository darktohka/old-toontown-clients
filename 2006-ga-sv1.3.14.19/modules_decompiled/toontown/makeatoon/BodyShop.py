# File: B (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase import PandaObject
from toontown.toon import ToonDNA
from direct.fsm import StateData
from direct.gui.DirectGui import *
from MakeAToonGlobals import *
import whrandom
import random
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal

class BodyShop(PandaObject.PandaObject, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('BodyShop')
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.toon = None
        self.torsoChoice = 0
        self.legChoice = 0
        self.headChoice = 0

    
    def enter(self, toon, shopsVisited = []):
        base.disableMouse()
        self.toon = toon
        self.dna = self.toon.getStyle()
        gender = self.toon.style.getGender()
        if BODYSHOP not in shopsVisited:
            self.headLButton['state'] = DISABLED
            self.torsoLButton['state'] = DISABLED
            self.legLButton['state'] = DISABLED
            self.headStart = ToonDNA.toonHeadTypes.index(self.dna.head)
            self.torsoStart = ToonDNA.toonTorsoTypes.index(self.dna.torso)
            self.legStart = ToonDNA.toonLegTypes.index(self.dna.legs)
            self.headChoice = self.headStart
            self.torsoChoice = self.torsoStart % 3
            self.legChoice = self.legStart
        else:
            self.headChoice = ToonDNA.toonHeadTypes.index(self.dna.head)
            self.torsoChoice = ToonDNA.toonTorsoTypes.index(self.dna.torso) % 3
            self.legChoice = ToonDNA.toonLegTypes.index(self.dna.legs)
        if CLOTHESSHOP in shopsVisited:
            self.clothesPicked = 1
        else:
            self.clothesPicked = 0
        if len(self.dna.torso) != 1:
            if gender == 'm' or ToonDNA.GirlBottoms[self.dna.botTex][1] == ToonDNA.SHORTS:
                torsoStyle = 's'
            else:
                torsoStyle = 'd'
            self._BodyShop__swapTorso(0)
            self._BodyShop__swapHead(0)
        
        self.acceptOnce('last', self._BodyShop__handleBackward)
        self.acceptOnce('next', self._BodyShop__handleForward)

    
    def showButtons(self):
        self.headLButton.show()
        self.headRButton.show()
        self.torsoLButton.show()
        self.torsoRButton.show()
        self.legLButton.show()
        self.legRButton.show()

    
    def hideButtons(self):
        self.headLButton.hide()
        self.headRButton.hide()
        self.torsoLButton.hide()
        self.torsoRButton.hide()
        self.legLButton.hide()
        self.legRButton.hide()

    
    def exit(self):
        
        try:
            del self.toon
        except:
            self.notify.warning('BodyShop: toon not found')

        self.hideButtons()
        self.ignore('last')
        self.ignore('next')
        self.ignore('enter')

    
    def load(self):
        self.gui = loader.loadModelOnce('phase_3/models/gui/create_a_toon_gui')
        guiRArrowDown = self.gui.find('**/CrtATn_R_Arrow_DN')
        guiRArrowRollover = self.gui.find('**/CrtATn_R_Arrow_RLVR')
        guiRArrowUp = self.gui.find('**/CrtATn_R_Arrow_UP')
        self.headLButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image_scale = (-1, 1, 1), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), pos = (-0.90000000000000002, 0, 0.29999999999999999), text = TTLocalizer.BodyShopHead, text_scale = 0.0625, text_pos = (0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), command = self._BodyShop__swapHead, extraArgs = [
            -1])
        self.headRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = TTLocalizer.BodyShopHead, text_scale = 0.0625, text_pos = (-0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (0, 0, 0.29999999999999999), command = self._BodyShop__swapHead, extraArgs = [
            1])
        self.torsoLButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image_scale = (-1, 1, 1), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = TTLocalizer.BodyShopBody, text_scale = 0.0625, text_pos = (0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (-0.90000000000000002, 0, -0.10000000000000001), command = self._BodyShop__swapTorso, extraArgs = [
            -1])
        self.torsoRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = TTLocalizer.BodyShopBody, text_scale = 0.0625, text_pos = (-0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (0, 0, -0.10000000000000001), command = self._BodyShop__swapTorso, extraArgs = [
            1])
        self.legLButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image_scale = (-1, 1, 1), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = TTLocalizer.BodyShopLegs, text_scale = 0.0625, text_pos = (0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (-0.90000000000000002, 0, -0.5), command = self._BodyShop__swapLegs, extraArgs = [
            -1])
        self.legRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover, guiRArrowUp), image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = TTLocalizer.BodyShopLegs, text_scale = 0.0625, text_pos = (-0.025000000000000001, 0), text_fg = (0.80000000000000004, 0.10000000000000001, 0, 1), pos = (0, 0, -0.5), command = self._BodyShop__swapLegs, extraArgs = [
            1])
        self.headLButton.hide()
        self.headRButton.hide()
        self.torsoLButton.hide()
        self.torsoRButton.hide()
        self.legLButton.hide()
        self.legRButton.hide()

    
    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.headLButton.destroy()
        self.headRButton.destroy()
        self.torsoLButton.destroy()
        self.torsoRButton.destroy()
        self.legLButton.destroy()
        self.legRButton.destroy()
        del self.headLButton
        del self.headRButton
        del self.torsoLButton
        del self.torsoRButton
        del self.legLButton
        del self.legRButton

    
    def _BodyShop__swapTorso(self, offset):
        gender = self.toon.style.getGender()
        if not (self.clothesPicked):
            length = len(ToonDNA.toonTorsoTypes[6:])
            torsoOffset = 6
        elif gender == 'm':
            length = len(ToonDNA.toonTorsoTypes[:3])
            torsoOffset = 0
            if self.dna.armColor not in ToonDNA.defaultBoyColorList:
                self.dna.armColor = ToonDNA.defaultBoyColorList[0]
            
            if self.dna.legColor not in ToonDNA.defaultBoyColorList:
                self.dna.legColor = ToonDNA.defaultBoyColorList[0]
            
            if self.dna.headColor not in ToonDNA.defaultBoyColorList:
                self.dna.headColor = ToonDNA.defaultBoyColorList[0]
            
            if self.toon.style.topTex not in ToonDNA.MakeAToonBoyShirts:
                randomShirt = ToonDNA.getRandomTop(gender, ToonDNA.MAKE_A_TOON)
                (shirtTex, shirtColor, sleeveTex, sleeveColor) = randomShirt
                self.toon.style.topTex = shirtTex
                self.toon.style.topTexColor = shirtColor
                self.toon.style.sleeveTex = sleeveTex
                self.toon.style.sleeveTexColor = sleeveColor
            
            if self.toon.style.botTex not in ToonDNA.MakeAToonBoyBottoms:
                (botTex, botTexColor) = ToonDNA.getRandomBottom(gender, ToonDNA.MAKE_A_TOON)
                self.toon.style.botTex = botTex
                self.toon.style.botTexColor = botTexColor
            
        else:
            length = len(ToonDNA.toonTorsoTypes[3:6])
            if self.toon.style.torso[1] == 'd':
                torsoOffset = 3
            else:
                torsoOffset = 0
            if self.dna.armColor not in ToonDNA.defaultGirlColorList:
                self.dna.armColor = ToonDNA.defaultGirlColorList[0]
            
            if self.dna.legColor not in ToonDNA.defaultGirlColorList:
                self.dna.legColor = ToonDNA.defaultGirlColorList[0]
            
            if self.dna.headColor not in ToonDNA.defaultGirlColorList:
                self.dna.headColor = ToonDNA.defaultGirlColorList[0]
            
            if self.toon.style.topTex not in ToonDNA.MakeAToonGirlShirts:
                randomShirt = ToonDNA.getRandomTop(gender, ToonDNA.MAKE_A_TOON)
                (shirtTex, shirtColor, sleeveTex, sleeveColor) = randomShirt
                self.toon.style.topTex = shirtTex
                self.toon.style.topTexColor = shirtColor
                self.toon.style.sleeveTex = sleeveTex
                self.toon.style.sleeveTexColor = sleeveColor
            
            if self.toon.style.botTex not in ToonDNA.MakeAToonGirlBottoms:
                if self.toon.style.torso[1] == 'd':
                    (botTex, botTexColor) = ToonDNA.getRandomBottom(gender, ToonDNA.MAKE_A_TOON, girlBottomType = ToonDNA.SKIRT)
                    self.toon.style.botTex = botTex
                    self.toon.style.botTexColor = botTexColor
                    torsoOffset = 3
                else:
                    (botTex, botTexColor) = ToonDNA.getRandomBottom(gender, ToonDNA.MAKE_A_TOON, girlBottomType = ToonDNA.SHORTS)
                    self.toon.style.botTex = botTex
                    self.toon.style.botTexColor = botTexColor
                    torsoOffset = 0
            
        self.torsoChoice = (self.torsoChoice + offset) % length
        self._BodyShop__updateScrollButtons(self.torsoChoice, length, self.torsoStart, self.torsoLButton, self.torsoRButton)
        torso = ToonDNA.toonTorsoTypes[torsoOffset + self.torsoChoice]
        self.dna.torso = torso
        self.toon.swapToonTorso(torso)
        self.toon.loop('neutral', 0)
        self.toon.swapToonColor(self.dna)

    
    def _BodyShop__swapLegs(self, offset):
        length = len(ToonDNA.toonLegTypes)
        self.legChoice = (self.legChoice + offset) % length
        self._BodyShop__updateScrollButtons(self.legChoice, length, self.legStart, self.legLButton, self.legRButton)
        newLeg = ToonDNA.toonLegTypes[self.legChoice]
        self.dna.legs = newLeg
        self.toon.swapToonLegs(newLeg)
        self.toon.loop('neutral', 0)
        self.toon.swapToonColor(self.dna)

    
    def _BodyShop__swapHead(self, offset):
        length = len(ToonDNA.toonHeadTypes)
        self.headChoice = (self.headChoice + offset) % length
        self._BodyShop__updateScrollButtons(self.headChoice, length, self.headStart, self.headLButton, self.headRButton)
        newHead = ToonDNA.toonHeadTypes[self.headChoice]
        self.dna.head = newHead
        self.toon.swapToonHead(newHead)
        self.toon.loop('neutral', 0)
        self.toon.swapToonColor(self.dna)

    
    def _BodyShop__updateScrollButtons(self, choice, length, start, lButton, rButton):
        if choice == (start - 1) % length:
            rButton['state'] = DISABLED
        elif choice == (start - 2) % length:
            rButton['state'] = NORMAL
        
        if choice == start % length:
            lButton['state'] = DISABLED
        elif choice == (start + 1) % length:
            lButton['state'] = NORMAL
        

    
    def _BodyShop__handleForward(self):
        self.doneStatus = 'next'
        messenger.send(self.doneEvent)

    
    def _BodyShop__handleBackward(self):
        self.doneStatus = 'last'
        messenger.send(self.doneEvent)


