# File: C (Python 2.2)

import PandaObject
import QTNode
import QTQuestNode
import QTEmoteNode
import QTCustomNode
import QTTree
import FSM
import State
import Emote
import string
from DirectGui import *
import Localizer

class ChatInputQuickTalker(PandaObject.PandaObject):
    
    def __init__(self, chatMgr):
        self.chatMgr = chatMgr
        self.whisperAvatarId = None
        self.sentenceList = []
        qtGraph = { }
        self.setupQTGraph()
        self.fsm = FSM.FSM('QuickTalker', [
            State.State('Hidden', self._ChatInputQuickTalker__enterHidden, self._ChatInputQuickTalker__exitHidden, [
                'Constructing']),
            State.State('Constructing', self._ChatInputQuickTalker__enterConstructing, self._ChatInputQuickTalker__exitConstructing, [
                'Constructing',
                'SayIt',
                'Hidden']),
            State.State('SayIt', self._ChatInputQuickTalker__enterSayIt, self._ChatInputQuickTalker__exitSayIt, [
                'Hidden'])], 'Hidden', 'Hidden')
        self.fsm.enterInitialState()

    
    def delete(self):
        self.ignoreAll()
        for entry in self.qtGraph.values():
            entry.destroy()
        
        del self.qtGraph
        del self.fsm
        del self.sentenceList

    
    def show(self, whisperAvatarId = None):
        self.whisperAvatarId = whisperAvatarId
        self.curQTnode = self.qtGraph['start']
        if self.whisperAvatarId:
            self.curQTnode.setPos(-0.69999999999999996, 0, 0.94999999999999996)
        else:
            self.curQTnode.setPos(-1.05, 0, 0.92000000000000004)
        self.accept('mouse1', self._ChatInputQuickTalker__cancelButtonPressed)
        self.fsm.request('Constructing')

    
    def hide(self):
        self.fsm.request('Hidden')

    
    def getSentenceCleartext(self):
        sentence = ''
        for entry in self.sentenceList:
            sentence = sentence + entry[0].getPhrase(entry[1])
        
        return sentence

    
    def getSentenceEncoded(self):
        sentence = []
        for entry in self.sentenceList:
            sentence.append(entry[1])
        
        return sentence

    
    def cleanup(self):
        self.ignore('mouse1')
        for entry in self.sentenceList:
            entry[0].nodepath.reparentTo(hidden)
        
        
        try:
            if self.curQTnode.nodepath:
                self.curQTnode.nodepath.reparentTo(hidden)
        except AttributeError:
            pass


    
    def decodeQTMessage(self, msg):
        curNode = self.qtGraph['start']
        for i in range(len(msg) - 1):
            curNode = curNode[msg[i]]
            if curNode == None:
                break
            
        
        return curNode.getPhrase(msg[-1])

    
    def setupQTGraph(self, QTDef = QTTree.QTTree):
        
        def addMenu(graph, menuDef):
            name = menuDef[0]
            if len(menuDef) == 2:
                subMenuName = menuDef[0]
                menuType = menuDef[1]
                if menuType == QTNode.QT_QUEST_ROOT_NODE:
                    menuNode = QTQuestNode.QTQuestNode(name)
                    graph[name] = menuNode
                    return None
                elif menuType == QTNode.QT_CUSTOM_ROOT_NODE:
                    menuNode = QTCustomNode.QTCustomNode(name)
                    graph[name] = menuNode
                    return None
                elif menuType == QTNode.QT_EMOTE_NODE:
                    menuNode = QTEmoteNode.QTEmoteNode(0)
                    graph[name] = menuNode
                    return None
                elif type(menuType) == type(0):
                    menuNode = QTEmoteNode.QTEmoteNode(menuType, speaking = 1)
                    graph[name] = menuNode
                    return None
                
            elif len(menuDef) == 3:
                subMenuName = menuDef[0]
                menuType = menuDef[1]
                menuEntries = menuDef[2]
                if menuType == QTNode.QT_EMOTE_ROOT_NODE:
                    menuNode = QTEmoteNode.QTEmoteNode(0, emoteRoot = menuEntries)
                    graph[name] = menuNode
                    return None
                elif menuType == QTNode.QT_EMOTE_SPEAK_ROOT_NODE:
                    menuNode = QTEmoteNode.QTEmoteNode(Localizer.EmoteFuncDict[string.lower(name)], emoteRoot = menuEntries, speaking = 1, emoteAnim = subMenuName)
                    graph[name] = menuNode
                    return None
                
            
            entries = menuDef[-1]
            menuNode = QTNode.QTNode(name)
            graph[name] = menuNode
            for i in entries:
                if type(i) == type(''):
                    menuNode[i] = QTNode.QTSend
                else:
                    addMenu(graph, i)
                    subMenuName = i[0]
                    graph[name] = menuNode
                    if len(i) == 3:
                        menuNode.addMenu(subMenuName, graph[subMenuName], i[1])
                    elif len(i) == 2 and type(i[1]) == type(0):
                        menuNode.addMenu(subMenuName, graph[subMenuName], QTNode.QT_TEXT_NODE)
                    else:
                        menuNode.addMenu(subMenuName, graph[subMenuName])
            

        self.qtGraph = { }
        tree = [
            'start',
            QTDef]
        addMenu(self.qtGraph, tree)
        self.rebuildMenus()

    
    def rebuildMenus(self):
        for key in self.qtGraph.keys():
            self.qtGraph[key].createMenu()
        

    
    def _ChatInputQuickTalker__selectionMade(self, qtNode, index):
        newNode = qtNode[index]
        oldNode = qtNode.selected
        if qtNode != self.curQTnode or newNode != oldNode:
            found = 0
            newList = []
            for entry in self.sentenceList:
                if entry[0] == qtNode:
                    found = 1
                
                if found:
                    entry[0].selected.nodepath.reparentTo(hidden)
                    entry[0].selected = None
                else:
                    newList.append(entry)
            
            self.sentenceList = newList
        
        self.curQTnode = newNode
        self.sentenceList.append([
            qtNode,
            index])
        if self.curQTnode.callback != None and not (self.whisperAvatarId):
            self.curQTnode.callback()
        
        if self.curQTnode.isTerminal():
            if self.curQTnode.isSpeaking():
                self.fsm.request('SayIt')
            else:
                self.chatMgr.fsm.request('mainMenu')
        else:
            pos = qtNode.getPos()
            scale = 1.0 - len(self.sentenceList) * 0.14000000000000001
            self.curQTnode.nodepath.setColorScale(scale, scale, scale, 1)
            if len(self.sentenceList) == 1:
                offset = 1.0
            else:
                offset = 2.0
            self.curQTnode.setPos(pos[0] + qtNode.width / offset, 0, pos[2] + qtNode.itemHeight * index)
            self.fsm.request('Constructing')

    
    def _ChatInputQuickTalker__cancelButtonPressed(self, event = None):
        self.cleanup()
        self.chatMgr.fsm.request('mainMenu')

    
    def _ChatInputQuickTalker__enterHidden(self):
        self.cleanup()
        self.sentenceList = []

    
    def _ChatInputQuickTalker__exitHidden(self):
        pass

    
    def _ChatInputQuickTalker__enterConstructing(self):
        self.curQTnode.nodepath.reparentTo(aspect2d, FOREGROUND_SORT_INDEX)
        self.accept('QTNode_selected', self._ChatInputQuickTalker__selectionMade)

    
    def _ChatInputQuickTalker__exitConstructing(self):
        self.ignore('QTNode_selected')

    
    def _ChatInputQuickTalker__enterSayIt(self):
        self.cleanup()
        if isinstance(self.curQTnode, QTQuestNode.QTQuestNode):
            finalNode = self.sentenceList[-1][0]
            index = self.sentenceList[-1][1]
            ds = finalNode.getEncodedMsg(index)
            if self.whisperAvatarId:
                self.chatMgr.sendWhisperQTQuestChatMessage(ds, self.whisperAvatarId)
            else:
                self.chatMgr.sendQTQuestChatMessage(ds)
        elif isinstance(self.curQTnode, QTCustomNode.QTCustomNode):
            finalNode = self.sentenceList[-1][0]
            index = self.sentenceList[-1][1]
            ds = finalNode.getEncodedMsg(index)
            if self.whisperAvatarId:
                self.chatMgr.sendWhisperQTCustomChatMessage(ds, self.whisperAvatarId)
            else:
                self.chatMgr.sendQTCustomChatMessage(ds)
        else:
            ds = self.getSentenceEncoded()
            if self.whisperAvatarId:
                self.chatMgr.sendWhisperQTChatMessage(ds, self.whisperAvatarId)
            else:
                self.chatMgr.sendQTChatMessage(ds)
        self.chatMgr.fsm.request('mainMenu')

    
    def _ChatInputQuickTalker__exitSayIt(self):
        pass


