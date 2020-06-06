# File: C (Python 2.2)

from PythonUtil import Functor
from DirectGui import *
import ClothesGUI
import ClosetGlobals
import Localizer
import ToontownGlobals
import ToontownDialog
import Localizer

class ClosetGUI(ClothesGUI.ClothesGUI):
    notify = directNotify.newCategory('ClosetGUI')
    
    def __init__(self, isOwner, doneEvent, cancelEvent, swapEvent, deleteEvent, topList = None, botList = None):
        ClothesGUI.ClothesGUI.__init__(self, ClothesGUI.CLOTHES_CLOSET, doneEvent, swapEvent)
        self.toon = None
        self.topsList = topList
        self.bottomsList = botList
        self.isOwner = isOwner
        self.deleteEvent = deleteEvent
        self.cancelEvent = cancelEvent
        self.genderChange = 0
        self.verify = None

    
    def load(self):
        ClothesGUI.ClothesGUI.load(self)
        self.cancelButton = DirectButton(relief = None, image = (self.gui.find('**/CrtAtoon_Btn2_UP'), self.gui.find('**/CrtAtoon_Btn2_DOWN'), self.gui.find('**/CrtAtoon_Btn2_RLLVR')), pos = (0.14999999999999999, 0, -0.84999999999999998), command = self._ClosetGUI__handleCancel, text = ('', Localizer.MakeAToonCancel, Localizer.MakeAToonCancel), text_font = ToontownGlobals.getInterfaceFont(), text_scale = 0.080000000000000002, text_pos = (0, -0.029999999999999999), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.cancelButton.hide()
        if self.isOwner:
            trashcanGui = loader.loadModel('phase_3/models/gui/trashcan_gui.bam')
            trashImage = (trashcanGui.find('**/TrashCan_CLSD'), trashcanGui.find('**/TrashCan_OPEN'), trashcanGui.find('**/TrashCan_RLVR'))
            self.trashPanel = DirectFrame(parent = aspect2d, image = getDefaultDialogGeom(), image_color = (1, 1, 0.75, 0.80000000000000004), image_scale = (0.35999999999999999, 0, 0.75), pos = (-0.85999999999999999, 0, -0.050000000000000003), relief = None)
            self.topTrashButton = DirectButton(parent = self.trashPanel, image = trashImage, relief = None, pos = (-0.089999999999999997, 0, 0.20000000000000001), command = self._ClosetGUI__handleDelete, extraArgs = [
                ClosetGlobals.SHIRT], scale = (0.5, 0.5, 0.5), text = Localizer.ClosetDeleteShirt, text_font = ToontownGlobals.getInterfaceFont(), text_scale = 0.12, text_pos = (0.29999999999999999, 0), text_fg = (0.80000000000000004, 0.20000000000000001, 0.20000000000000001, 1), text_shadow = (0, 0, 0, 1), textMayChange = 0)
            self.bottomTrashButton = DirectButton(parent = self.trashPanel, image = trashImage, relief = None, textMayChange = 1, pos = (-0.089999999999999997, 0, -0.20000000000000001), command = self._ClosetGUI__handleDelete, extraArgs = [
                ClosetGlobals.SHORTS], scale = (0.5, 0.5, 0.5), text = Localizer.ClosetDeleteShorts, text_font = ToontownGlobals.getInterfaceFont(), text_scale = 0.12, text_pos = (0.29999999999999999, 0), text_fg = (0.80000000000000004, 0.20000000000000001, 0.20000000000000001, 1), text_shadow = (0, 0, 0, 1))
            self.button = DirectButton(relief = None, image = (self.gui.find('**/CrtAtoon_Btn1_UP'), self.gui.find('**/CrtAtoon_Btn1_DOWN'), self.gui.find('**/CrtAtoon_Btn1_RLLVR')), pos = (-0.14999999999999999, 0, -0.84999999999999998), command = self._ClosetGUI__handleButton, text = ('', Localizer.MakeAToonDone, Localizer.MakeAToonDone), text_font = ToontownGlobals.getInterfaceFont(), text_scale = 0.080000000000000002, text_pos = (0, -0.029999999999999999), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
            trashcanGui.removeNode()
        

    
    def unload(self):
        self.ignore('verifyDone')
        ClothesGUI.ClothesGUI.unload(self)
        self.cancelButton.destroy()
        del self.cancelButton
        if self.isOwner:
            self.topTrashButton.destroy()
            self.bottomTrashButton.destroy()
            self.button.destroy()
            del self.topTrashButton
            del self.bottomTrashButton
            del self.button
            self.trashPanel.destroy()
            del self.trashPanel
        
        if self.verify:
            self.verify.cleanup()
            del self.verify
        

    
    def showButtons(self):
        ClothesGUI.ClothesGUI.showButtons(self)
        self.cancelButton.show()
        if self.isOwner:
            self.topTrashButton.show()
            self.bottomTrashButton.show()
            self.button.show()
        

    
    def hideButtons(self):
        ClothesGUI.ClothesGUI.hideButtons(self)
        self.cancelButton.hide()
        if self.isOwner:
            self.topTrashButton.hide()
            self.bottomTrashButton.hide()
            self.button.hide()
        

    
    def setupScrollInterface(self):
        self.notify.debug('setupScrollInterface')
        self.dna = self.toon.getStyle()
        self.gender = self.dna.getGender()
        self.swappedTorso = 0
        if self.topsList == None:
            self.topsList = self.toon.getClothesTopsList()
        
        if self.bottomsList == None:
            self.bottomsList = self.toon.getClothesBottomsList()
        
        self.tops = []
        self.bottoms = []
        self.tops.append([
            self.dna.topTex,
            self.dna.topTexColor,
            self.dna.sleeveTex,
            self.dna.sleeveTexColor])
        self.bottoms.append([
            self.dna.botTex,
            self.dna.botTexColor])
        i = 0
        while i < len(self.topsList):
            self.tops.append([
                self.topsList[i],
                self.topsList[i + 1],
                self.topsList[i + 2],
                self.topsList[i + 3]])
            i = i + 4
        i = 0
        while i < len(self.bottomsList):
            self.bottoms.append([
                self.bottomsList[i],
                self.bottomsList[i + 1]])
            i = i + 2
        self.topChoice = 0
        self.bottomChoice = 0
        self.swapTop(0)
        self.swapBottom(0)
        if self.isOwner:
            self.updateTrashButtons()
        
        self.setupButtons()

    
    def updateTrashButtons(self):
        if len(self.tops) < 2:
            self.topTrashButton['state'] = DISABLED
        else:
            self.topTrashButton['state'] = NORMAL
        if len(self.bottoms) < 2:
            self.bottomTrashButton['state'] = DISABLED
        else:
            self.bottomTrashButton['state'] = NORMAL
        if self.toon:
            if self.toon.style.torso[1] == 'd':
                self.bottomTrashButton['text'] = Localizer.ClosetDeleteSkirt
            else:
                self.bottomTrashButton['text'] = Localizer.ClosetDeleteShorts
        

    
    def setGender(self, gender):
        self.ownerGender = gender
        self.genderChange = 1

    
    def swapBottom(self, offset):
        length = len(self.bottoms)
        self.bottomChoice += offset
        if self.bottomChoice <= 0:
            self.bottomChoice = 0
        
        self.updateScrollButtons(self.bottomChoice, length, 0, self.bottomLButton, self.bottomRButton)
        if self.bottomChoice < 0 and self.bottomChoice >= len(self.bottoms) or len(self.bottoms[self.bottomChoice]) != 2:
            self.notify.warning('bottomChoice index is out of range!')
            return None
        
        self.toon.style.botTex = self.bottoms[self.bottomChoice][0]
        self.toon.style.botTexColor = self.bottoms[self.bottomChoice][1]
        if self.genderChange == 1:
            if self.bottomChoice > 0:
                self._ClosetGUI__handleGenderBender(1)
            else:
                self._ClosetGUI__handleGenderBender(0)
        
        if self.toon.generateToonClothes() == 1:
            self.toon.loop('neutral', 0)
            self.swappedTorso = 1
        
        if self.isOwner:
            self.updateTrashButtons()
        
        if self.swapEvent != None:
            messenger.send(self.swapEvent)
        

    
    def _ClosetGUI__handleGenderBender(self, type):
        if type == 1:
            if self.toon.style.gender != self.ownerGender and self.toon.style.gender == 'f':
                self.toon.swapToonTorso(self.toon.style.torso[0] + 's', genClothes = 0)
                self.toon.loop('neutral', 0)
                self.swappedTorso = 1
            
            self.toon.style.gender = self.ownerGender
        else:
            self.toon.style.gender = self.gender
            if self.toon.style.gender != self.ownerGender and self.toon.style.gender == 'm':
                self.toon.swapToonTorso(self.toon.style.torso[0] + 's', genClothes = 0)
                self.toon.loop('neutral', 0)
                self.swappedTorso = 1
            

    
    def removeTop(self, index):
        listLen = len(self.tops)
        if index < listLen:
            del self.tops[index]
            if self.topChoice > index:
                self.topChoice -= 1
            elif self.topChoice == index:
                self.topChoice = 0
            
            return 1
        
        return 0

    
    def removeBottom(self, index):
        listLen = len(self.bottoms)
        if index < listLen:
            del self.bottoms[index]
            if self.bottomChoice > index:
                self.bottomChoice -= 1
            elif self.bottomChoice == index:
                self.bottomChoice = 0
            
            return 1
        
        return 0

    
    def _ClosetGUI__handleButton(self):
        self.doneStatus = 'next'
        messenger.send(self.doneEvent)

    
    def _ClosetGUI__handleCancel(self):
        messenger.send(self.cancelEvent)

    
    def _ClosetGUI__handleDelete(self, t_or_b):
        if t_or_b == ClosetGlobals.SHIRT:
            item = Localizer.ClosetShirt
        elif self.toon.style.torso[1] == 'd':
            item = Localizer.ClosetSkirt
        else:
            item = Localizer.ClosetShorts
        self.verify = ToontownDialog.GlobalDialog(doneEvent = 'verifyDone', message = Localizer.ClosetVerifyDelete % item, style = ToontownDialog.TwoChoice)
        self.verify.show()
        self.accept('verifyDone', Functor(self._ClosetGUI__handleVerifyDelete, t_or_b))

    
    def _ClosetGUI__handleVerifyDelete(self, t_or_b):
        status = self.verify.doneStatus
        self.ignore('verifyDone')
        self.verify.cleanup()
        del self.verify
        self.verify = None
        if status == 'ok':
            messenger.send(self.deleteEvent, [
                t_or_b])
        


