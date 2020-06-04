# File: D (Python 2.2)

from ShowBaseGlobal import *
import ToontownDialog
import Localizer

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
                toonbase.localToon.b_setAnimState('neutral', 1)
            except:
                pass

            doneStatus['mode'] = 'incomplete'
            self.doneStatus = doneStatus
            percentComplete = base.launcher.getPercentPhaseComplete(phase)
            phaseName = Localizer.LauncherPhaseNames[phase]
            msg = Localizer.DownloadForceAcknowledgeMsg % {
                'phase': phaseName,
                'percent': percentComplete }
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


