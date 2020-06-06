# File: F (Python 2.2)

from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from direct.interval.IntervalGlobal import *
import FishGlobals
import FishPhoto

class FishPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('FishPanel')
    
    def __init__(self, fish = None, parent = aspect2d, doneEvent = None, **kw):
        optiondefs = (('relief', None, None), ('state', DISABLED, None), ('image', getDefaultDialogGeom(), None), ('image_color', ToontownGlobals.GlobalDialogColor, None), ('image_scale', (0.65000000000000002, 1, 0.84999999999999998), None), ('text', '', None), ('text_scale', 0.059999999999999998, None), ('text_fg', (0, 0, 0, 1), None), ('text_pos', (0, 0.34999999999999998, 0), None), ('text_font', ToontownGlobals.getInterfaceFont(), None), ('text_wordwrap', 13.5, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.initialiseoptions(FishPanel)
        self.doneEvent = doneEvent
        self.fish = fish
        self.parent = parent
        self.photo = None

    
    def destroy(self):
        if self.photo:
            self.photo.destroy()
            self.photo = None
        
        self.fish = None
        DirectFrame.destroy(self)

    
    def load(self):
        self.weight = DirectLabel(parent = self, pos = (0, 0, -0.28000000000000003), relief = None, state = NORMAL, text = '', text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_pos = (0, 0.0, 0), text_font = ToontownGlobals.getInterfaceFont(), text_wordwrap = 10.5)
        self.value = DirectLabel(parent = self, pos = (0, 0, -0.34999999999999998), relief = None, state = NORMAL, text = '', text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_pos = (0, 0, 0), text_font = ToontownGlobals.getInterfaceFont(), text_wordwrap = 10.5)
        self.mystery = DirectLabel(parent = self, pos = (-0.025000000000000001, 0, -0.055), relief = None, state = NORMAL, text = '?', text_scale = 0.25, text_fg = (0, 0, 0, 1), text_pos = (0, 0, 0), text_font = ToontownGlobals.getInterfaceFont(), text_wordwrap = 10.5)
        self.extraLabel = DirectLabel(parent = self, relief = None, state = NORMAL, text = '', text_fg = (0.20000000000000001, 0.80000000000000004, 0.40000000000000002, 1), text_font = ToontownGlobals.getSignFont(), text_scale = 0.080000000000000002, pos = (0, 0, 0.26000000000000001))
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        self.cancel = DirectButton(parent = self, pos = (0.27500000000000002, 0, -0.375), relief = None, state = NORMAL, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), image_scale = (0.59999999999999998, 1, 0.59999999999999998), command = self.handleCancel)
        buttons.removeNode()
        self.photo = FishPhoto.FishPhoto(parent = self)
        self.update(self.fish)

    
    def update(self, fish):
        self.fish = fish
        if self.fish == None:
            return None
        
        self['text'] = self.fish.getSpeciesName()
        weight = self.fish.getWeight()
        conv = TTLocalizer.FishPageWeightConversion
        large = weight / conv
        if large == 1:
            largeStr = TTLocalizer.FishPageWeightLargeS % large
        else:
            largeStr = TTLocalizer.FishPageWeightLargeP % large
        small = weight % conv
        if small == 1:
            smallStr = TTLocalizer.FishPageWeightSmallS % small
        else:
            smallStr = TTLocalizer.FishPageWeightSmallP % small
        self.weight['text'] = TTLocalizer.FishPageWeightStr + largeStr + smallStr
        value = self.fish.getValue()
        if value == 1:
            self.value['text'] = TTLocalizer.FishPageValueS % value
        else:
            self.value['text'] = TTLocalizer.FishPageValueP % value
        self.photo.update(fish)

    
    def setSwimBounds(self, *bounds):
        self.swimBounds = bounds

    
    def setSwimColor(self, *colors):
        self.swimColor = colors

    
    def handleCancel(self):
        self.hide()
        if self.doneEvent:
            messenger.send(self.doneEvent)
        

    
    def show(self, code = FishGlobals.FishItem):
        messenger.send('wakeup')
        apply(self.photo.setSwimBounds, self.swimBounds)
        apply(self.photo.setSwimColor, self.swimColor)
        if code == FishGlobals.FishItem:
            self.extraLabel.hide()
        elif code == FishGlobals.FishItemNewEntry:
            self.extraLabel.show()
            self.extraLabel['text'] = TTLocalizer.FishingNewEntry
            self.extraLabel['text_scale'] = 0.080000000000000002
            self.extraLabel.setPos(0, 0, 0.26000000000000001)
        elif code == FishGlobals.FishItemNewRecord:
            self.extraLabel.show()
            self.extraLabel['text'] = TTLocalizer.FishingNewRecord
        
        self.photo.show()
        DirectFrame.show(self)

    
    def hide(self):
        self.photo.hide()
        DirectFrame.hide(self)


