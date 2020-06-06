# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer

class DownloadForceAcknowledge:
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.dialog = None

    
    def enter(self, phase):
        doneStatus = { }
        if not launcher:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [
                doneStatus])
        elif launcher.getPhaseComplete(phase):
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [
                doneStatus])
        else:
            
            try:
                base.localAvatar.b_setAnimState('neutral', 1)
            except:
                pass

            doneStatus['mode'] = 'incomplete'
            self.doneStatus = doneStatus
            percentComplete = base.launcher.getPercentPhaseComplete(phase)
            phaseName = TTLocalizer.LauncherPhaseNames[phase]
            msg = TTLocalizer.DownloadForceAcknowledgeMsg % {
                'phase': phaseName,
                'percent': percentComplete }
            self.dialog = TTDialog.TTDialog(text = msg, command = self.handleOk, style = TTDialog.Acknowledge)
            self.dialog.show()

    
    def exit(self):
        if self.dialog:
            self.dialog.hide()
            self.dialog.cleanup()
            self.dialog = None
        

    
    def handleOk(self, value):
        messenger.send(self.doneEvent, [
            self.doneStatus])


