# File: N (Python 2.2)

from ShowBaseGlobal import *
import ToontownDialog
import Localizer
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
            if toonbase.localToon.quests[0][4] >= 1:
                icon = render.find('**/*landmark_hqTT_DNARoot*')
                msg = Localizer.NPCForceAcknowledgeMessage2
                pos = (0, 0, -0.27500000000000002)
                h = 45.0
                scale = 0.0054999999999999997
            else:
                icon = render.find('**/prop_trolley_station_DNARoot/trolley_car')
                msg = Localizer.NPCForceAcknowledgeMessage
                pos = (0, 0, -0.12)
                h = 70.0
                scale = 0.0152
            self.dialog = ToontownDialog.ToontownDialog(text = msg, command = self.handleOk, style = ToontownDialog.Acknowledge)
            if not icon.isEmpty():
                iconCopy = icon.copyTo(self.dialog)
                iconCopy.setPosHprScale(pos[0], pos[1], pos[2], h, 0, 0, scale, scale, scale)
                iconCopy.setDepthTest(1)
                iconCopy.setDepthWrite(1)
            

    
    def exit(self):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        
        return None

    
    def handleOk(self, value):
        messenger.send(self.doneEvent, [
            self.doneStatus])
        return None


