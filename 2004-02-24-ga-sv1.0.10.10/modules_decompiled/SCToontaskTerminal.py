# File: S (Python 2.2)

from SCTerminal import *
import Quests
import NPCToons
SCToontaskMsgEvent = 'SCToontaskMsg'

def decodeSCToontaskMsg(taskId, toNpcId, toonProgress, msgIndex):
    q = Quests.getQuest(taskId)
    if q is None:
        return None
    
    name = NPCToons.getNPCName(toNpcId)
    if name is None:
        return None
    
    msgs = q.getSCStrings(toNpcId, toonProgress)
    if type(msgs) != type([]):
        msgs = [
            msgs]
    
    if msgIndex >= len(msgs):
        return None
    
    return msgs[msgIndex]


class SCToontaskTerminal(SCTerminal):
    
    def __init__(self, msg, taskId, toNpcId, toonProgress, msgIndex):
        SCTerminal.__init__(self)
        self.msg = msg
        self.taskId = taskId
        self.toNpcId = toNpcId
        self.toonProgress = toonProgress
        self.msgIndex = msgIndex

    
    def getDisplayText(self):
        return self.msg

    
    def handleSelect(self):
        SCTerminal.handleSelect(self)
        messenger.send(self.getEventName(SCToontaskMsgEvent), [
            self.taskId,
            self.toNpcId,
            self.toonProgress,
            self.msgIndex])


