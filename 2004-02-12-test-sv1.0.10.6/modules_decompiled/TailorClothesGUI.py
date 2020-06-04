# File: T (Python 2.2)

import ClothesGUI
import AvatarDNA

class TailorClothesGUI(ClothesGUI.ClothesGUI):
    notify = directNotify.newCategory('MakeClothesGUI')
    
    def __init__(self, doneEvent, swapEvent, tailorId):
        ClothesGUI.ClothesGUI.__init__(self, ClothesGUI.CLOTHES_TAILOR, doneEvent, swapEvent)
        self.tailorId = tailorId

    
    def setupScrollInterface(self):
        self.dna = self.toon.getStyle()
        gender = self.dna.getGender()
        if self.swapEvent != None:
            self.tops = AvatarDNA.getTops(gender, tailorId = self.tailorId)
            self.bottoms = AvatarDNA.getBottoms(gender, tailorId = self.tailorId)
            self.gender = gender
            self.topChoice = -1
            self.bottomChoice = -1
        
        self.setupButtons()


