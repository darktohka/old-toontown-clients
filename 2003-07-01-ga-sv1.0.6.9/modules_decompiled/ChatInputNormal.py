# File: C (Python 2.2)

import PandaObject
import ToontownGlobals
import sys
from DirectGui import *
import Localizer

class ChatInputNormal(PandaObject.PandaObject):
    ExecNamespace = None
    
    def __init__(self, chatMgr):
        self.chatMgr = chatMgr
        self.whisperAvatarName = None
        self.whisperAvatarId = None
        gui = loader.loadModelOnce('phase_3.5/models/gui/chat_input_gui')
        self.chatFrame = DirectFrame(image = gui.find('**/Chat_Bx_FNL'), relief = None, pos = (-1.083, 0, 0.80400000000000005), sortOrder = FOREGROUND_SORT_INDEX)
        self.chatFrame.hide()
        self.chatButton = DirectButton(parent = self.chatFrame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (0.182, 0, -0.087999999999999995), relief = None, text = ('', Localizer.ChatInputNormalSayIt, Localizer.ChatInputNormalSayIt), text_scale = 0.059999999999999998, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, command = self._ChatInputNormal__chatButtonPressed)
        self.cancelButton = DirectButton(parent = self.chatFrame, image = (gui.find('**/CloseBtn_UP'), gui.find('**/CloseBtn_DN'), gui.find('**/CloseBtn_Rllvr')), pos = (-0.151, 0, -0.087999999999999995), relief = None, text = ('', Localizer.ChatInputNormalCancel, Localizer.ChatInputNormalCancel), text_scale = 0.059999999999999998, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, command = self._ChatInputNormal__cancelButtonPressed)
        self.whisperLabel = DirectLabel(parent = self.chatFrame, pos = (0.02, 0, 0.23000000000000001), relief = FLAT, frameColor = (1, 1, 0.5, 1), frameSize = (-0.22, 0.22, -0.070000000000000007, 0.050000000000000003), text = Localizer.ChatInputNormalWhisper, text_scale = 0.050000000000000003, text_fg = Vec4(0, 0, 0, 1), text_wordwrap = 7.5, textMayChange = 1)
        self.whisperLabel.hide()
        self.chatEntry = DirectEntry(parent = self.chatFrame, relief = None, scale = 0.050000000000000003, pos = (-0.20000000000000001, 0, 0.11), entryFont = ToontownGlobals.getToonFont(), width = 8.5999999999999996, numLines = 3, cursorKeys = 0, backgroundFocus = 0, command = self.sendChat)
        self.chatEntry.bind(OVERFLOW, self.chatOverflow)
        self.chatEntry.bind(TYPE, self.typeCallback)
        gui.removeNode()
        return None

    
    def typeCallback(self, extraArgs):
        messenger.send('enterNormalChat')

    
    def delete(self):
        loader.unloadModel('phase_3.5/models/gui/chat_input_gui')
        self.chatFrame.destroy()
        del self.chatFrame
        del self.chatButton
        del self.cancelButton
        del self.chatEntry
        del self.whisperLabel
        return None

    
    def show(self, whisperAvatarName = None, whisperAvatarId = None):
        self.whisperAvatarName = whisperAvatarName
        self.whisperAvatarId = whisperAvatarId
        if self.whisperAvatarId:
            self.chatFrame.setPos(0.0, 0, 0.70999999999999996)
            self.whisperLabel['text'] = Localizer.ChatInputWhisperLabel % self.whisperAvatarName
            self.whisperLabel.show()
        else:
            self.chatFrame.setPos(-1.083, 0, 0.80400000000000005)
            self.whisperLabel.hide()
        self.chatEntry['focus'] = 1
        self.chatFrame.show()
        return None

    
    def hide(self):
        self.chatEntry.set('')
        self.chatEntry['focus'] = 0
        self.chatFrame.hide()
        self.whisperLabel.hide()
        return None

    
    def sendChat(self, text):
        self.hide()
        self.chatMgr.fsm.request('mainMenu')
        if text:
            if self.whisperAvatarId:
                self.chatMgr.sendWhisperString(text, self.whisperAvatarId)
                self.whisperAvatarName = None
                self.whisperAvatarId = None
            elif self.chatMgr.execChat:
                if text[0] == '>':
                    text = self._ChatInputNormal__execMessage(text[1:])
                    toonbase.localToon.setChatAbsolute(text, CFSpeech | CFTimeout)
                    return None
                
            
            self.chatMgr.sendChatString(text)
        
        return None

    
    def chatOverflow(self, overflowText):
        self.sendChat(self.chatEntry.get())
        return None

    
    def _ChatInputNormal__execMessage(self, message):
        if not (ChatInputNormal.ExecNamespace):
            ChatInputNormal.ExecNamespace = { }
            exec 'from ShowBaseGlobal import *' in globals(), ChatInputNormal.ExecNamespace
            exec 'from ToonBaseGlobal import *' in globals(), ChatInputNormal.ExecNamespace
        
        
        try:
            return str(eval(message, globals(), ChatInputNormal.ExecNamespace))
        except SyntaxError:
            
            try:
                exec message in globals(), ChatInputNormal.ExecNamespace
                return 'ok'
            except:
                exception = sys.exc_info()[0]
                extraInfo = sys.exc_info()[1]
                if extraInfo:
                    return str(extraInfo)
                else:
                    return str(exception)

        except:
            exception = sys.exc_info()[0]
            extraInfo = sys.exc_info()[1]
            if extraInfo:
                return str(extraInfo)
            else:
                return str(exception)


    
    def _ChatInputNormal__cancelButtonPressed(self):
        self.chatEntry.set('')
        self.chatMgr.fsm.request('mainMenu')
        return None

    
    def _ChatInputNormal__chatButtonPressed(self):
        self.sendChat(self.chatEntry.get())
        return None


