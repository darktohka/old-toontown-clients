# File: Q (Python 2.2)

import ToontownGlobals
import types
import QTNode
import Localizer
from PythonUtil import Functor
import Emote
from DirectGui import *
import string

def inBadState(toon):
    if toon.playingAnim in [
        'run',
        'swim',
        'jump',
        'sad',
        'teleport',
        'openBook',
        'closeBook',
        'readBook'] or toon.hp <= 0:
        return 1
    else:
        return 0


def doEmote(index, extraFunc = None):
    
    try:
        lt = toonbase.localToon
    except:
        return None

    if not (toonbase.emotionsEnabled) or not Emote.IsEnabled(index):
        return None
    
    lt.b_setEmoteState(index, animMultiplier = lt.animMultiplier)


class QTEmoteNode(QTNode.QTNode, PandaObject.PandaObject):
    
    def __init__(self, emoteIndex = 0, emoteRoot = None, speaking = 0, emoteAnim = None):
        QTNode.QTNode.__init__(self, 'emoteNode')
        self.emoteRoot = emoteRoot
        self.emoteIndex = emoteIndex
        self.emoteAnim = emoteAnim
        self.speaking = speaking
        if self.emoteRoot != None:
            self.accept('emotesChanged', self._QTEmoteNode__createEmoteMenu)
        
        if self.emoteRoot == None:
            self.callback = self.getEmoteCallback()
        

    
    def destroy(self):
        self.ignoreAll()
        QTNode.QTNode.destroy(self)

    
    def __setitem__(self, key, value):
        raise RuntimeError, 'cannot __setitem__ on a QTEmoteNode'

    
    def getEmoteCallback(self):
        return Functor(doEmote, self.emoteIndex)

    
    def isTerminal(self):
        if not self == QTEmoteSend and self.emoteRoot == None:
            pass
        return QTNode.QTNode.isTerminal(self)

    
    def _QTEmoteNode__createEmoteMenu(self):
        
        try:
            lt = toonbase.localToon
        except:
            return None

        self.phraseList = []
        self.actionList = []
        
        def addMsg(msg, index = None):
            for phrase in self.phraseList:
                if msg == phrase[0]:
                    return None
                
            
            if index != None:
                emoteIndex = index
            else:
                emoteIndex = self.emoteIndex
            nodeType = QTNode.QT_TEXT_NODE
            self.phraseList.append([
                msg,
                QTEmoteNode(emoteIndex, speaking = self.speaking),
                nodeType])

        
        def addTease():
            msg = '   ?   '
            nodeType = QTNode.QT_DISABLED_NODE
            self.phraseList.append([
                msg,
                QTNode.QTSend,
                nodeType])

        if not (self.speaking) and lt.emoteAccess != None:
            for i in range(len(lt.emoteAccess)):
                if lt.emoteAccess[i]:
                    addMsg(Localizer.EmoteList[i], i)
                else:
                    addTease()
            
        else:
            for key in self.emoteRoot:
                addMsg(key)
            
        self.createMenu()


QTEmoteSend = QTEmoteNode('emoteSend', speaking = 1)
