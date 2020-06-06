# File: Q (Python 2.2)

import ToontownGlobals
import types
import QTNode
import Localizer
from DirectGui import *

def decodeQTCustomMsg(messageIndex):
    return Localizer.CustomQTStrings.get(messageIndex, None)


class QTCustomNode(QTNode.QTNode, PandaObject.PandaObject):
    
    def __init__(self, name, customRoot = 1):
        QTNode.QTNode.__init__(self, name)
        self.encodedMsgList = []
        self.customRoot = customRoot
        if self.customRoot:
            self.accept('customMessagesChanged', self._QTCustomNode__customMessagesChanged)
            self._QTCustomNode__customMessagesChanged()
        

    
    def destroy(self):
        self.ignoreAll()
        QTNode.QTNode.destroy(self)

    
    def __setitem__(self, key, value):
        raise RuntimeError, 'cannot __setitem__ on a QTCustomNode'

    
    def addMenu(self, key, value, type = None):
        raise RuntimeError, 'cannot addMenu on a QTCustomNode'

    
    def getPhrase(self, index):
        raise RuntimeError, 'cannot getPhrase on a QTCustomNode'

    
    def isTerminal(self):
        if not self == QTCustomSend:
            pass
        return QTNode.QTNode.isTerminal(self)

    
    def getEncodedMsg(self, i):
        return self.encodedMsgList[i]

    
    def _QTCustomNode__customMessagesChanged(self):
        
        try:
            lt = toonbase.localToon
        except:
            return None

        self.phraseList = []
        self.encodedMsgList = []
        
        def addMsg(msg, index):
            for phrase in self.phraseList:
                if msg == phrase[0]:
                    return None
                
            
            self.phraseList.append([
                msg,
                QTCustomSend,
                QTNode.QT_TEXT_NODE])
            self.encodedMsgList.append(index)

        for messageIndex in lt.customMessages:
            message = Localizer.CustomQTStrings.get(messageIndex, None)
            if message:
                addMsg(message, messageIndex)
            
        
        self.createMenu()


QTCustomSend = QTCustomNode('customSend', customRoot = 0)
