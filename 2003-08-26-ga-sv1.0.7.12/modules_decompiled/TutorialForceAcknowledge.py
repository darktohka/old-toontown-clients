# File: T (Python 2.2)

from ShowBaseGlobal import *
import ToontownDialog
import Localizer

class TutorialForceAcknowledge:
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.dialog = None
        return None

    
    def enter(self):
        toonbase.localToon.loop('neutral')
        self.doneStatus = {
            'mode': 'incomplete' }
        msg = Localizer.TutorialForceAcknowledgeMessage
        self.dialog = ToontownDialog.ToontownDialog(text = msg, command = self.handleOk, style = ToontownDialog.Acknowledge)
        return None

    
    def exit(self):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        
        return None

    
    def handleOk(self, value):
        messenger.send(self.doneEvent, [
            self.doneStatus])
        return None


