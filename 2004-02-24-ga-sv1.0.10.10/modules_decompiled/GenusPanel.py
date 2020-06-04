# File: G (Python 2.2)

import ToontownGlobals
from DirectGui import *
import Localizer
import FishPanel
import FishBase
import FishGlobals

class GenusPanel(DirectFrame):
    
    def __init__(self, genus = None, parent = aspect2d, doneEvent = None, **kw):
        fishingGui = loader.loadModelOnce('phase_3.5/models/gui/fishingBook')
        albumGui = fishingGui.find('**/photo_frame1').copyTo(hidden)
        albumGui.find('**/picture_frame').reparentTo(albumGui, -1)
        albumGui.find('**/arrows').removeNode()
        optiondefs = (('relief', None, None), ('state', NORMAL, None), ('image', albumGui, None), ('image_scale', (0.025000000000000001, 0.025000000000000001, 0.025000000000000001), None), ('image_pos', (0, 1, 0), None), ('text', Localizer.UnknownFish, None), ('text_scale', 0.065000000000000002, None), ('text_fg', (0.20000000000000001, 0.10000000000000001, 0.0, 1), None), ('text_pos', (-0.23000000000000001, -0.34000000000000002), None), ('text_font', ToontownGlobals.getInterfaceFont(), None), ('text_wordwrap', 13.5, None), ('text_align', TextNode.ACenter, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.initialiseoptions(GenusPanel)
        self.doneEvent = doneEvent
        self.parent = parent
        self.fishPanel = None
        self.genus = None
        self.setGenus(genus)
        albumGui.removeNode()

    
    def destroy(self):
        if self.fishPanel:
            self.fishPanel.destroy()
            del self.fishPanel
        
        DirectFrame.destroy(self)

    
    def load(self):
        return None

    
    def setGenus(self, genus):
        if self.genus == genus:
            return None
        
        self.genus = genus
        if self.genus != None:
            if self.fishPanel:
                self.fishPanel.destroy()
            
            f = FishBase.FishBase(self.genus, 0, 0)
            self.fishPanel = FishPanel.FishPanel(fish = f, parent = self, image = None)
            self.fishPanel.load()
            self.fishPanel.contract()
            self.fishPanel.setPos(-0.23000000000000001, 10, -0.01)
            self.fishPanel.setScale(0.90000000000000002)
            speciesList = FishGlobals.getSpecies(self.genus)
            self.speciesLabels = []
            offset = 0.074999999999999997
            startPos = (len(speciesList) / 2) * offset
            if not (len(speciesList) % 2):
                startPos -= offset / 2
            
            for species in range(len(speciesList)):
                label = DirectLabel(parent = self, relief = None, state = NORMAL, pos = (0.059999999999999998, 0, startPos - species * offset), text = Localizer.UnknownFish, text_fg = (0.20000000000000001, 0.10000000000000001, 0.0, 1), text_scale = 0.044999999999999998, text_align = TextNode.ALeft, text_font = ToontownGlobals.getInterfaceFont())
                self.speciesLabels.append(label)
            
        

    
    def show(self):
        self.update()
        DirectFrame.show(self)

    
    def update(self):
        if toonbase.localToon.fishCollection.hasGenus(self.genus):
            self.fishPanel.showFish()
            self['text'] = Localizer.FishGenusNames[self.genus]
        
        for species in range(len(FishGlobals.getSpecies(self.genus))):
            if toonbase.localToon.fishCollection.hasFish(self.genus, species):
                self.speciesLabels[species]['text'] = Localizer.FishSpeciesNames[self.genus][species]
            
        


