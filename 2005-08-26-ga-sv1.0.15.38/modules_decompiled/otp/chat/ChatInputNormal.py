# File: C (Python 2.2)

from direct.showbase import PandaObject
from otp.otpbase import OTPGlobals
import sys
from direct.gui.DirectGui import *
from otp.otpbase import OTPLocalizer

class ChatInputNormal(PandaObject.PandaObject):
    ExecNamespace = None
    
    def __init__(self, chatMgr):
        self.chatMgr = chatMgr
        self.whisperAvatarName = None
        self.whisperAvatarId = None

    
    def typeCallback(self, extraArgs):
        messenger.send('enterNormalChat')

    
    def delete(self):
        self.chatFrame.destroy()
        del self.chatFrame
        del self.chatButton
        del self.cancelButton
        del self.chatEntry
        del self.whisperLabel
        del self.chatMgr

    
    def show(self, whisperAvatarName = None, whisperAvatarId = None):
        self.whisperAvatarName = whisperAvatarName
        self.whisperAvatarId = whisperAvatarId
        if self.whisperAvatarId:
            self.chatFrame.setPos(0.0, 0, 0.70999999999999996)
            self.whisperLabel['text'] = OTPLocalizer.ChatInputWhisperLabel % self.whisperAvatarName
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
        base.win.closeIme()
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
                    base.localAvatar.setChatAbsolute(text, CFSpeech | CFTimeout)
                    return None
                
            
            self.chatMgr.sendChatString(text)
        
        return None

    
    def chatOverflow(self, overflowText):
        self.sendChat(self.chatEntry.get())
        return None

    
    def _ChatInputNormal__execMessage(self, message):
        if not (ChatInputNormal.ExecNamespace):
            ChatInputNormal.ExecNamespace = { }
            exec 'from direct.showbase.ShowBaseGlobal import *' in globals(), self.ExecNamespace
            self.importExecNamespace()
        
        
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


    
    def cancelButtonPressed(self):
        self.chatEntry.set('')
        self.chatMgr.fsm.request('mainMenu')
        return None

    
    def chatButtonPressed(self):
        self.sendChat(self.chatEntry.get())
        return None

    
    def importExecNamespace(self):
        pass


