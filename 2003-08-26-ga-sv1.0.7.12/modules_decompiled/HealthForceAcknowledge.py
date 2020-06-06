# File: H (Python 2.2)

from ShowBaseGlobal import *
import ToontownDialog
import Localizer

class HealthForceAcknowledge:
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.dialog = None

    
    def enter(self, hpLevel):
        doneStatus = { }
        toonHp = toonbase.localToon.getHp()
        if toonHp >= hpLevel:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [
                doneStatus])
        else:
            toonbase.localToon.b_setAnimState('neutral', 1)
            doneStatus['mode'] = 'incomplete'
            self.doneStatus = doneStatus
            msg = Localizer.HealthForceAcknowledgeMessage
            self.dialog = ToontownDialog.ToontownDialog(text = msg, command = self.handleOk, style = ToontownDialog.Acknowledge)

    
    def exit(self):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        
        return None

    
    def handleOk(self, value):
        messenger.send(self.doneEvent, [
            self.doneStatus])
        return None


