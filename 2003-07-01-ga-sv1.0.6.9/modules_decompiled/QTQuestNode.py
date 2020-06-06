# File: Q (Python 2.2)

import ToontownGlobals
import types
import QTNode
import Localizer
import Quests
from DirectGui import *

def decodeQTQuestMsg(msg):
    if len(msg) == 0:
        return Localizer.QTQuestNodeNeedATask
    
    if len(msg) != 4:
        return None
    
    (questId, toNpcId, toonProgress, index) = msg
    quest = Quests.getQuest(questId)
    if not quest:
        return None
    
    msgs = quest.getQTStrings(toNpcId, toonProgress)
    if type(msgs) != type([]):
        msgs = [
            msgs]
    
    if index >= len(msgs):
        return None
    
    return msgs[index]


class QTQuestNode(QTNode.QTNode, PandaObject.PandaObject):
    
    def __init__(self, name, questRoot = 1):
        QTNode.QTNode.__init__(self, name)
        self.encodedMsgList = []
        self.questRoot = questRoot
        if self.questRoot:
            self.accept('questsChanged', self._QTQuestNode__questsChanged)
            self._QTQuestNode__questsChanged()
        

    
    def destroy(self):
        self.ignoreAll()
        QTNode.QTNode.destroy(self)

    
    def __setitem__(self, key, value):
        raise RuntimeError, 'cannot __setitem__ on a QTQuestNode'

    
    def addMenu(self, key, value, type = None):
        raise RuntimeError, 'cannot addMenu on a QTQuestNode'

    
    def getPhrase(self, index):
        raise RuntimeError, 'cannot getPhrase on a QTQuestNode'

    
    def isTerminal(self):
        if not self == QTQuestSend:
            pass
        return QTNode.QTNode.isTerminal(self)

    
    def getEncodedMsg(self, i):
        return self.encodedMsgList[i]

    
    def _QTQuestNode__questsChanged(self):
        
        try:
            lt = toonbase.localToon
        except:
            return None

        self.phraseList = []
        self.encodedMsgList = []
        
        def addMsg(msg, packet):
            for phrase in self.phraseList:
                if msg == phrase[0]:
                    return None
                
            
            self.phraseList.append([
                msg,
                QTQuestSend,
                QTNode.QT_TEXT_NODE])
            self.encodedMsgList.append(packet)

        for quest in lt.quests:
            (questId, fromNpcId, toNpcId, rewardId, toonProgress) = quest
            q = Quests.getQuest(questId)
            if q is None:
                continue
            
            msgs = q.getQTStrings(toNpcId, toonProgress)
            if type(msgs) != type([]):
                msgs = [
                    msgs]
            
            for i in xrange(len(msgs)):
                addMsg(msgs[i], [
                    questId,
                    toNpcId,
                    toonProgress,
                    i])
            
        
        needToontask = 1
        
        try:
            needToontask = len(lt.quests) != lt.questCarryLimit
        except:
            pass

        if needToontask:
            addMsg(Localizer.QTQuestNodeNeedATask, [])
        
        self.createMenu()


QTQuestSend = QTQuestNode('questSend', questRoot = 0)
