# File: N (Python 2.2)

from ShowBaseGlobal import *
import ToontownDialog
import Localizer
import DirectLabel
TROLLEY_QUEST = 110

class NPCForceAcknowledge:
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.dialog = None

    
    def enter(self):
        doneStatus = { }
        questHistory = toonbase.localToon.getQuestHistory()
        if questHistory != [] and questHistory != [
            1000] and questHistory != [
            101,
            110]:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [
                doneStatus])
        elif len(toonbase.localToon.quests) > 1 or len(toonbase.localToon.quests) == 0:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [
                doneStatus])
        elif toonbase.localToon.quests[0][0] != TROLLEY_QUEST:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [
                doneStatus])
        else:
            toonbase.localToon.b_setAnimState('neutral', 1)
            doneStatus['mode'] = 'incomplete'
            self.doneStatus = doneStatus
            imageModel = loader.loadModel('phase_4/models/gui/tfa_images')
            if toonbase.localToon.quests[0][4] >= 1:
                imgNodePath = imageModel.find('**/hq-dialog-image')
                imgPos = (0, 0, -0.02)
                msg = Localizer.NPCForceAcknowledgeMessage2
                pos = (0, 0, -0.27500000000000002)
                h = 45.0
                scale = 0.0054999999999999997
            else:
                imgNodePath = imageModel.find('**/trolley-dialog-image')
                imgPos = (0, 0, 0.040000000000000001)
                msg = Localizer.NPCForceAcknowledgeMessage
                pos = (0, 0, -0.12)
                h = 70.0
                scale = 0.0152
            self.dialog = ToontownDialog.ToontownDialog(text = msg, command = self.handleOk, style = ToontownDialog.Acknowledge)
            imgLabel = DirectLabel.DirectLabel(parent = self.dialog, relief = None, pos = imgPos, scale = 1.0, image = imgNodePath, image_scale = 0.25)

    
    def exit(self):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        

    
    def handleOk(self, value):
        messenger.send(self.doneEvent, [
            self.doneStatus])


