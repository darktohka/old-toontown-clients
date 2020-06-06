# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer
from direct.showbase import Transitions
from direct.gui.DirectGui import *
import LaffMeter

class DeathForceAcknowledge:
    
    def __init__(self, doneEvent):
        fadeModel = loader.loadModel('phase_3/models/misc/fade')
        if fadeModel:
            self.fade = DirectFrame(parent = aspect2dp, relief = None, image = fadeModel, image_color = (0, 0, 0, 0.40000000000000002), image_scale = 3.0, state = NORMAL)
            self.fade.reparentTo(aspect2d, FADE_SORT_INDEX)
            fadeModel.removeNode()
        else:
            print 'Problem loading fadeModel.'
            self.fade = None
        self.dialog = TTDialog.TTGlobalDialog(message = TTLocalizer.PlaygroundDeathAckMessage, doneEvent = doneEvent, style = TTDialog.Acknowledge, suppressKeys = True)
        self.dialog['text_pos'] = (-0.26000000000000001, 0.10000000000000001)
        scale = self.dialog.component('image0').getScale()
        scale.setX(scale[0] * 1.3)
        self.dialog.component('image0').setScale(scale)
        av = base.localAvatar
        self.laffMeter = LaffMeter.LaffMeter(av.style, av.hp, av.maxHp)
        self.laffMeter.reparentTo(self.dialog)
        if av.style.getAnimal() == 'monkey':
            self.laffMeter.setPos(-0.46000000000000002, 0, -0.035000000000000003)
            self.laffMeter.setScale(0.085000000000000006)
        else:
            self.laffMeter.setPos(-0.47999999999999998, 0, -0.035000000000000003)
            self.laffMeter.setScale(0.10000000000000001)
        self.laffMeter.start()
        self.dialog.show()

    
    def cleanup(self):
        if self.fade:
            self.fade.destroy()
        
        if self.laffMeter:
            self.laffMeter.destroy()
            del self.laffMeter
        
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        


