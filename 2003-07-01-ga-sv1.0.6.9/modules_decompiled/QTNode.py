# File: Q (Python 2.2)

import ToontownGlobals
import types
import Localizer
from DirectGui import *
from IntervalGlobal import *
QT_DISABLED_NODE = 'd'
QT_TEXT_NODE = 't'
QT_MENU_NODE = 'm'
QT_TEXT_MENU_NODE = 'tm'
QT_EMOTE_ROOT_NODE = 'er'
QT_EMOTE_SPEAK_ROOT_NODE = 'es'
QT_EMOTE_NODE = 'e'
QT_QUEST_ROOT_NODE = 'q'
QT_CUSTOM_ROOT_NODE = 'c'
MENU_NODES_LIST = [
    QT_MENU_NODE,
    QT_EMOTE_ROOT_NODE,
    QT_EMOTE_SPEAK_ROOT_NODE]

class QTNode:
    font = ToontownGlobals.getToonFont()
    
    def __init__(self, name):
        self.name = name
        self.width = 0.0
        self.selected = None
        self.itemHeight = 0.0
        self.phraseList = []
        self.nodepath = None
        self.callback = None
        self.speaking = 1
        self.buttons = []
        self.pos = (0, 0, 0)
        self.popupInfo = None

    
    def _QTNode__findPhrasePair(self, key):
        phrasePair = None
        if isinstance(key, types.StringType):
            for pp in self.phraseList:
                if pp[0] == key:
                    phrasePair = pp
                    break
                
            
        elif key < len(self.phraseList):
            phrasePair = self.phraseList[key]
        
        return phrasePair

    
    def __getitem__(self, key):
        phrasePair = self._QTNode__findPhrasePair(key)
        if phrasePair == None:
            return None
        else:
            return phrasePair[1]

    
    def __setitem__(self, key, value):
        phrasePair = self._QTNode__findPhrasePair(key)
        if phrasePair == None:
            self.phraseList.append([
                key,
                value,
                QT_TEXT_NODE])
        else:
            phrasePair[1] = value
            phrasePair[2] = QT_TEXT_NODE

    
    def addMenu(self, key, value, type = QT_MENU_NODE):
        phrasePair = self._QTNode__findPhrasePair(key)
        if phrasePair == None:
            phrasePair = self.phraseList.append([
                key,
                value,
                type])
        else:
            phrasePair[1] = value
            phrasePair[2] = type

    
    def getPhrase(self, index):
        pp = self._QTNode__findPhrasePair(index)
        if pp == None:
            return ''
        elif pp[2] in MENU_NODES_LIST:
            return ''
        else:
            return pp[0]

    
    def _QTNode__createDisplayText(self, phrasePair):
        text = phrasePair[0]
        if phrasePair[2] in MENU_NODES_LIST:
            pass
        1
        if not phrasePair[1].isTerminal():
            text = text + '...'
        
        return text

    
    def isTerminal(self):
        return self == QTSend

    
    def isSpeaking(self):
        return self.speaking

    
    def createMenu(self):
        self.deleteMenu()
        self.nodepath = hidden.attachNewNode('QTNode-' + self.name)
        l = 0
        r = 0
        t = 0
        b = 0
        text = TextNode('qtmenu')
        text.freeze()
        text.setFont(QTNode.font)
        for pp in self.phraseList:
            dText = self._QTNode__createDisplayText(pp)
            text.setText(dText)
            bounds = text.getCardActual()
            if pp[2] in MENU_NODES_LIST:
                arrowPad = 1.0
            else:
                arrowPad = 0.0
            l = min(l, bounds[0])
            r = max(r, bounds[1] + arrowPad)
            b = min(b, bounds[2])
            t = max(t, bounds[3])
        
        del text
        z = 0
        sf = 0.055
        padx = 0.25
        padz = 0.10000000000000001
        self.width = (r + padx) * sf
        self.itemHeight = -(padz + padz + (t - b)) * sf
        dz = -(padz + padz + (t - b)) * sf
        index = 0
        for pp in self.phraseList:
            frameColor = (0.80000000000000004, 0.80000000000000004, 1, 1)
            rolloverColor = (0.90000000000000002, 0.90000000000000002, 1, 1)
            text_fg = (0, 0, 0, 1.0)
            state = NORMAL
            dText = self._QTNode__createDisplayText(pp)
            if pp[2] in MENU_NODES_LIST:
                relief = RAISED
                image = ('phase_3/models/props/page-arrow', 'poly')
                image_pos = (r - padx, 0, (t - b) / 4.0)
            else:
                relief = FLAT
                image = None
                image_pos = (0, 0, 0)
                if pp[2] == QT_DISABLED_NODE:
                    frameColor = ((0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 0.5),)
                    rolloverColor = (0.90000000000000002, 0.90000000000000002, 1, 0.5)
                    text_fg = (0.5, 0.5, 0.5, 1.0)
                    relief = SUNKEN
                
            btn = DirectButton(parent = self.nodepath, state = state, text = dText, image = image, image_pos = image_pos, text_font = QTNode.font, text_align = TextNode.ALeft, textMayChange = 0, frameColor = frameColor, frameSize = (l - padx, r + padx, b - padz, t + padz), relief = relief, pos = (0.0, 0.0, z), text_fg = text_fg, scale = 0.055, extraArgs = [
                index])
            btn.frameStyle[2].setColor(rolloverColor[0], rolloverColor[1], rolloverColor[2], rolloverColor[3])
            btn.updateFrameStyle()
            btn.bind(EXIT, self._QTNode__buttonExited, extraArgs = [
                index,
                pp[2]])
            btn.bind(ENTER, self._QTNode__buttonEntered, extraArgs = [
                index,
                pp[2]])
            btn.bind(B1PRESS, self._QTNode__buttonSelected, extraArgs = [
                index,
                pp[2]])
            self.buttons.append(btn)
            z = z + dz
            index += 1
        

    
    def setPos(self, x, y, z):
        self.pos = Point3(x, y, z)
        self.nodepath.setPos(x, y, z)

    
    def getPos(self):
        return self.pos

    
    def deleteMenu(self):
        for button in self.buttons:
            button.destroy()
        
        self.buttons = []
        if self.nodepath:
            self.nodepath.removeNode()
        
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        

    
    def destroy(self):
        self.deleteMenu()
        del self.buttons
        del self.nodepath

    
    def enterPopupInfo(self):
        if self.popupInfo == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.popupInfo = DirectFrame(parent = hidden, relief = None, state = 'normal', text = Localizer.QTPopupEmoteMessage, frameSize = (-1, 1, -1, 1), geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (0.88, 1, 0.45000000000000001), geom_pos = (0, 0, -0.080000000000000002), text_scale = 0.080000000000000002)
            DirectButton(self.popupInfo, image = okButtonImage, relief = None, text = Localizer.QTPopupEmoteMessageOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.16), command = self._QTNode__handlePopupEmoteMessageOK)
            buttons.removeNode()
        
        self.popupInfo.reparentTo(aspect2d)

    
    def _QTNode__handlePopupEmoteMessageOK(self):
        self.popupInfo.reparentTo(hidden)

    
    def _QTNode__buttonSelected(self, index, type, event):
        if type == QT_DISABLED_NODE:
            self.enterPopupInfo()
            return None
        
        messenger.send('QTNode_selected', [
            self,
            index])
        self.selected = self[index]

    
    def _QTNode__buttonEntered(self, index, type, event):
        if self.selected:
            
            try:
                self.selected.nodepath.reparentTo(hidden)
            except AttributeError:
                pass

        
        if type == QT_DISABLED_NODE:
            pass
        1
        if type != QT_TEXT_NODE:
            self._QTNode__buttonSelected(index, type, event)
        

    
    def _QTNode__buttonExited(self, index, type, event):
        pass


QTSend = QTNode('send')
