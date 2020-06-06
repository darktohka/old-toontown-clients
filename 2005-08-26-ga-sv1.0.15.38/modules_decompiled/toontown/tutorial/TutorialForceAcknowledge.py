# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer

class TutorialForceAcknowledge:
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.dialog = None
        return None

    
    def enter(self):
        base.localAvatar.loop('neutral')
        self.doneStatus = {
            'mode': 'incomplete' }
        msg = TTLocalizer.TutorialForceAcknowledgeMessage
        self.dialog = TTDialog.TTDialog(text = msg, command = self.handleOk, style = TTDialog.Acknowledge)
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


