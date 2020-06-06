# File: S (Python 2.2)

from direct.gui.DirectGui import *
from SCTerminal import SCTerminal
from otp.otpbase.OTPLocalizer import EmoteList, EmoteWhispers
from otp.avatar import Emote
SCEmoteMsgEvent = 'SCEmoteMsg'
SCEmoteNoAccessEvent = 'SCEmoteNoAccess'

def decodeSCEmoteWhisperMsg(emoteId, avName):
    if emoteId >= len(EmoteWhispers):
        return None
    
    return EmoteWhispers[emoteId] % avName


class SCEmoteTerminal(SCTerminal):
    
    def __init__(self, emoteId):
        SCTerminal.__init__(self)
        self.emoteId = emoteId
        if not self._SCEmoteTerminal__ltHasAccess():
            self.text = '?'
        else:
            self.text = EmoteList[self.emoteId]

    
    def _SCEmoteTerminal__ltHasAccess(self):
        
        try:
            lt = base.localAvatar
            return lt.emoteAccess[self.emoteId]
        except:
            return 0


    
    def _SCEmoteTerminal__emoteEnabled(self):
        if self.isWhispering():
            return 1
        
        return Emote.globalEmote.isEnabled(self.emoteId)

    
    def finalize(self, dbArgs = { }):
        if not self.isDirty():
            return None
        
        args = { }
        if not self._SCEmoteTerminal__ltHasAccess() or not self._SCEmoteTerminal__emoteEnabled():
            args.update({
                'rolloverColor': (0, 0, 0, 0),
                'pressedColor': (0, 0, 0, 0),
                'rolloverSound': None,
                'text_fg': self.getColorScheme().getTextDisabledColor() + (1,) })
        
        if not self._SCEmoteTerminal__ltHasAccess():
            args.update({
                'text_align': TextNode.ACenter })
        elif not self._SCEmoteTerminal__emoteEnabled():
            args.update({
                'clickSound': None })
        
        self.lastEmoteEnableState = self._SCEmoteTerminal__emoteEnabled()
        args.update(dbArgs)
        SCTerminal.finalize(self, dbArgs = args)

    
    def _SCEmoteTerminal__emoteEnableStateChanged(self):
        if self.isDirty():
            self.notify.info("skipping __emoteEnableStateChanged; we're marked as dirty")
            return None
        elif not hasattr(self, 'button'):
            self.notify.error('SCEmoteTerminal is not marked as dirty, but has no button!')
        
        btn = self.button
        if self._SCEmoteTerminal__emoteEnabled():
            rolloverColor = self.getColorScheme().getRolloverColor() + (1,)
            pressedColor = self.getColorScheme().getPressedColor() + (1,)
            btn.frameStyle[BUTTON_ROLLOVER_STATE].setColor(*rolloverColor)
            btn.frameStyle[BUTTON_DEPRESSED_STATE].setColor(*pressedColor)
            btn.updateFrameStyle()
            btn['text_fg'] = self.getColorScheme().getTextColor() + (1,)
            btn['rolloverSound'] = getDefaultRolloverSound()
            btn['clickSound'] = getDefaultClickSound()
        else:
            btn.frameStyle[BUTTON_ROLLOVER_STATE].setColor(0, 0, 0, 0)
            btn.frameStyle[BUTTON_DEPRESSED_STATE].setColor(0, 0, 0, 0)
            btn.updateFrameStyle()
            btn['text_fg'] = self.getColorScheme().getTextDisabledColor() + (1,)
            btn['rolloverSound'] = None
            btn['clickSound'] = None

    
    def enterVisible(self):
        SCTerminal.enterVisible(self)
        if self._SCEmoteTerminal__ltHasAccess():
            if hasattr(self, 'lastEmoteEnableState'):
                if self.lastEmoteEnableState != self._SCEmoteTerminal__emoteEnabled():
                    self.invalidate()
                
            
            if not self.isWhispering():
                self.accept(Emote.globalEmote.EmoteEnableStateChanged, self._SCEmoteTerminal__emoteEnableStateChanged)
            
        

    
    def exitVisible(self):
        SCTerminal.exitVisible(self)
        self.ignore(Emote.globalEmote.EmoteEnableStateChanged)

    
    def handleSelect(self):
        if not self._SCEmoteTerminal__ltHasAccess():
            messenger.send(self.getEventName(SCEmoteNoAccessEvent))
        elif self._SCEmoteTerminal__emoteEnabled():
            SCTerminal.handleSelect(self)
            messenger.send(self.getEventName(SCEmoteMsgEvent), [
                self.emoteId])
        


