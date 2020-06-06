# File: G (Python 2.2)

from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
import FishBase
import FishGlobals
import FishPhoto

class GenusPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('GenusPanel')
    
    def __init__(self, genus = None, itemIndex = 0, *extraArgs):
        fishingGui = loader.loadModelOnce('phase_3.5/models/gui/fishingBook')
        albumGui = fishingGui.find('**/photo_frame1').copyTo(hidden)
        albumGui.find('**/picture_frame').reparentTo(albumGui, -1)
        albumGui.find('**/arrows').removeNode()
        optiondefs = (('relief', None, None), ('state', NORMAL, None), ('image', albumGui, None), ('image_scale', (0.025000000000000001, 0.025000000000000001, 0.025000000000000001), None), ('image_pos', (0, 1, 0), None), ('text', TTLocalizer.UnknownFish, None), ('text_scale', 0.065000000000000002, None), ('text_fg', (0.20000000000000001, 0.10000000000000001, 0.0, 1), None), ('text_pos', (-0.5, -0.34000000000000002), None), ('text_font', ToontownGlobals.getInterfaceFont(), None), ('text_wordwrap', 13.5, None), ('text_align', TextNode.ALeft, None))
        self.defineoptions({ }, optiondefs)
        DirectFrame.__init__(self)
        self.initialiseoptions(GenusPanel)
        self.fishPanel = None
        self.genus = None
        self.setGenus(int(genus))
        self.setScale(1.2)
        albumGui.removeNode()

    
    def destroy(self):
        if self.fishPanel:
            self.fishPanel.destroy()
            del self.fishPanel
        
        DirectFrame.destroy(self)

    
    def load(self):
        pass

    
    def setGenus(self, genus):
        if self.genus == genus:
            return None
        
        self.genus = genus
        if self.genus != None:
            if self.fishPanel:
                self.fishPanel.destroy()
            
            f = FishBase.FishBase(self.genus, 0, 0)
            self.fishPanel = FishPhoto.FishPhoto(fish = f, parent = self)
            self.fishPanel.setPos(-0.23000000000000001, 1, -0.01)
            self.fishPanel.setSwimBounds(-0.24610000000000001, 0.23669999999999999, -0.20699999999999999, 0.26640000000000003)
            self.fishPanel.setSwimColor(0.46999999999999997, 1.0, 0.98999999999999999, 1.0)
            speciesList = FishGlobals.getSpecies(self.genus)
            self.speciesLabels = []
            offset = 0.074999999999999997
            startPos = (len(speciesList) / 2) * offset
            if not (len(speciesList) % 2):
                startPos -= offset / 2
            
            for species in range(len(speciesList)):
                label = DirectLabel(parent = self, relief = None, state = NORMAL, pos = (0.059999999999999998, 0, startPos - species * offset), text = TTLocalizer.UnknownFish, text_fg = (0.20000000000000001, 0.10000000000000001, 0.0, 1), text_scale = 0.044999999999999998, text_align = TextNode.ALeft, text_font = ToontownGlobals.getInterfaceFont())
                self.speciesLabels.append(label)
            
        

    
    def show(self):
        self.update()
        DirectFrame.show(self)

    
    def hide(self):
        if self.fishPanel is not None:
            self.fishPanel.hide()
        
        DirectFrame.hide(self)

    
    def update(self):
        if base.localAvatar.fishCollection.hasGenus(self.genus) and self.fishPanel is not None:
            self.fishPanel.show(showBackground = 1)
            self['text'] = TTLocalizer.FishGenusNames[self.genus]
        
        for species in range(len(FishGlobals.getSpecies(self.genus))):
            if base.localAvatar.fishCollection.hasFish(self.genus, species):
                self.speciesLabels[species]['text'] = TTLocalizer.FishSpeciesNames[self.genus][species]
            
        


