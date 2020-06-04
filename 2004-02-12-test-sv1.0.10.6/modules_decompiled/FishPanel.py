# File: F (Python 2.2)

import ToontownGlobals
from DirectGui import *
import Localizer
import FishGlobals

class FishPanel(DirectFrame):
    
    def __init__(self, fish = None, parent = aspect2d, doneEvent = None, **kw):
        optiondefs = (('relief', None, None), ('state', NORMAL, None), ('image', getDefaultDialogGeom(), None), ('image_color', ToontownGlobals.GlobalDialogColor, None), ('image_scale', (0.65000000000000002, 1, 0.84999999999999998), None), ('text', '', None), ('text_scale', 0.059999999999999998, None), ('text_fg', (0, 0, 0, 1), None), ('text_pos', (0, 0.34999999999999998, 0), None), ('text_font', ToontownGlobals.getInterfaceFont(), None), ('text_wordwrap', 13.5, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.initialiseoptions(FishPanel)
        self.doneEvent = doneEvent
        self.fish = fish
        self.parent = parent

    
    def destroy(self):
        DirectFrame.destroy(self)

    
    def load(self):
        self.weight = DirectLabel(parent = self, pos = (0, 0, -0.28000000000000003), relief = None, state = NORMAL, text = '', text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_pos = (0, 0.0, 0), text_font = ToontownGlobals.getInterfaceFont(), text_wordwrap = 10.5)
        self.value = DirectLabel(parent = self, pos = (0, 0, -0.34999999999999998), relief = None, state = NORMAL, text = '', text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_pos = (0, 0, 0), text_font = ToontownGlobals.getInterfaceFont(), text_wordwrap = 10.5)
        self.mystery = DirectLabel(parent = self, pos = (-0.025000000000000001, 0, -0.055), relief = None, state = NORMAL, text = '?', text_scale = 0.25, text_fg = (0, 0, 0, 1), text_pos = (0, 0, 0), text_font = ToontownGlobals.getInterfaceFont(), text_wordwrap = 10.5)
        self.extraLabel = DirectLabel(parent = self, relief = None, state = NORMAL, text = '', text_fg = (0.20000000000000001, 0.80000000000000004, 0.40000000000000002, 1), text_font = ToontownGlobals.getSignFont(), text_scale = 0.080000000000000002, pos = (0, 0, 0.26000000000000001))
        self.fishFrame = None
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        self.cancel = DirectButton(parent = self, pos = (0.27500000000000002, 0, -0.375), relief = None, state = NORMAL, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), image_scale = (0.59999999999999998, 1, 0.59999999999999998), command = self.handleCancel)
        buttons.removeNode()
        self.update(self.fish)

    
    def update(self, fish):
        self.fish = fish
        if self.fish == None:
            return None
        
        self['text'] = self.fish.getSpeciesName()
        weight = self.fish.getWeight()
        conv = Localizer.FishPageWeightConversion
        large = weight / conv
        if large == 1:
            largeStr = Localizer.FishPageWeightLargeS % large
        else:
            largeStr = Localizer.FishPageWeightLargeP % large
        small = weight % conv
        if small == 1:
            smallStr = Localizer.FishPageWeightSmallS % small
        else:
            smallStr = Localizer.FishPageWeightSmallP % small
        self.weight['text'] = Localizer.FishPageWeightStr + largeStr + smallStr
        value = self.fish.getValue()
        if value == 1:
            self.value['text'] = Localizer.FishPageValueS % value
        else:
            self.value['text'] = Localizer.FishPageValueP % value

    
    def makeFishFrame(self, actor):
        actor.setDepthTest(1)
        actor.setDepthWrite(1)
        frame = DirectFrame(parent = self, frameSize = (-1.0, 1.0, -1.0, 1.0), relief = None)
        pitch = frame.attachNewNode('pitch')
        rotate = pitch.attachNewNode('rotate')
        scale = rotate.attachNewNode('scale')
        actor.reparentTo(scale)
        (bMin, bMax) = actor.getTightBounds()
        center = (bMin + bMax) / 2.0
        actor.setPos(-center[0], -center[1], -center[2])
        genus = self.fish.getGenus()
        fishInfo = FishGlobals.FishFileDict.get(genus, FishGlobals.FishFileDict[-1])
        fishPos = fishInfo[4]
        if fishPos:
            actor.setPos(fishPos[0], fishPos[1], fishPos[2])
        
        scale.setScale(fishInfo[5])
        rotate.setH(fishInfo[6])
        pitch.setP(fishInfo[7])
        pitch.setY(2)
        actor.loop('swim')
        return frame

    
    def handleCancel(self):
        self.hide()
        if self.doneEvent:
            messenger.send(self.doneEvent)
        

    
    def expand(self):
        self.cancel.show()
        self.value.show()
        self.weight.show()
        self['image_scale'] = VBase3(0.65000000000000002, 1, 0.84999999999999998)
        self['text'] = self.fish.getSpeciesName()

    
    def contract(self):
        self.cancel.hide()
        self.value.hide()
        self.weight.hide()
        self['image_scale'] = VBase3(0.52500000000000002, 1, 0.52500000000000002)
        self['text'] = ''

    
    def showFish(self, code = FishGlobals.FishItem):
        if self.fishFrame:
            self.actor.cleanup()
            self.fishFrame.destroy()
        
        self.actor = self.fish.getActor()
        self.fishFrame = self.makeFishFrame(self.actor)
        self.fishFrame.setX(-0.01)
        self.mystery.hide()
        if code == FishGlobals.FishItem:
            self.extraLabel.hide()
        elif code == FishGlobals.FishItemNewEntry:
            self.extraLabel.show()
            self.extraLabel['text'] = Localizer.FishingNewEntry
            self.extraLabel['text_scale'] = 0.080000000000000002
            self.extraLabel.setPos(0, 0, 0.26000000000000001)
        elif code == FishGlobals.FishItemNewRecord:
            self.extraLabel.show()
            self.extraLabel['text'] = Localizer.FishingNewRecord
        


