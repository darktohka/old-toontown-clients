# File: S (Python 2.2)

from SCElement import SCElement
from SCObject import SCObject
from SCMenu import SCMenu
from otp.avatar import Emote
SCTerminalSelectedEvent = 'SCTerminalSelected'
SCTerminalLinkedEmoteEvent = 'SCTerminalLinkedEmoteEvent'
SCWhisperModeChangeEvent = 'SCWhisperModeChange'

class SCTerminal(SCElement):
    
    def __init__(self, linkedEmote = None):
        SCElement.__init__(self)
        self.setLinkedEmote(linkedEmote)
        scGui = loader.loadModelOnce(SCMenu.GuiModelName)
        self.emotionIcon = scGui.find('**/emotionIcon')
        self.setDisabled(False)
        self._SCTerminal__numCharges = -1

    
    def destroy(self):
        SCElement.destroy(self)

    
    def handleSelect(self):
        messenger.send(self.getEventName(SCTerminalSelectedEvent))
        if self.hasLinkedEmote() and self.linkedEmoteEnabled():
            messenger.send(self.getEventName(SCTerminalLinkedEmoteEvent), [
                self.linkedEmote])
        

    
    def getLinkedEmote(self):
        return self.linkedEmote

    
    def setLinkedEmote(self, linkedEmote):
        self.linkedEmote = linkedEmote
        self.invalidate()

    
    def hasLinkedEmote(self):
        return self.linkedEmote is not None

    
    def linkedEmoteEnabled(self):
        if Emote.globalEmote:
            return Emote.globalEmote.isEnabled(self.linkedEmote)
        

    
    def getCharges(self):
        return self._SCTerminal__numCharges

    
    def setCharges(self, nCharges):
        self._SCTerminal__numCharges = nCharges
        if nCharges is 0:
            self.setDisabled(True)
        

    
    def isDisabled(self):
        return self._SCTerminal__disabled

    
    def setDisabled(self, bDisabled):
        self._SCTerminal__disabled = bDisabled

    
    def onMouseClick(self, event):
        if not self.isDisabled():
            SCElement.onMouseClick(self, event)
            self.handleSelect()
        

    
    def getMinDimensions(self):
        (width, height) = SCElement.getMinDimensions(self)
        if self.hasLinkedEmote():
            width += 1.3
        
        return (width, height)

    
    def finalize(self, dbArgs = { }):
        if not self.isDirty():
            return None
        
        args = { }
        if self.hasLinkedEmote():
            self.lastEmoteIconColor = self.getEmoteIconColor()
            self.emotionIcon.setColorScale(*self.lastEmoteIconColor)
            args.update({
                'image': self.emotionIcon,
                'image_pos': (self.width - 0.59999999999999998, 0, -(self.height) * 0.5) })
        
        if self.isDisabled():
            args.update({
                'rolloverColor': (0, 0, 0, 0),
                'pressedColor': (0, 0, 0, 0),
                'rolloverSound': None,
                'clickSound': None,
                'text_fg': self.getColorScheme().getTextDisabledColor() + (1,) })
        
        args.update(dbArgs)
        SCElement.finalize(self, dbArgs = args)

    
    def getEmoteIconColor(self):
        if self.linkedEmoteEnabled() and not self.isWhispering():
            (r, g, b) = self.getColorScheme().getEmoteIconColor()
        else:
            (r, g, b) = self.getColorScheme().getEmoteIconDisabledColor()
        return (r, g, b, 1)

    
    def updateEmoteIcon(self):
        if hasattr(self, 'button'):
            self.lastEmoteIconColor = self.getEmoteIconColor()
            for i in range(self.button['numStates']):
                self.button['image%s_image' % i].setColorScale(*self.lastEmoteIconColor)
            
        else:
            self.invalidate()

    
    def enterVisible(self):
        SCElement.enterVisible(self)
        if hasattr(self, 'lastEmoteIconColor'):
            if self.getEmoteIconColor() != self.lastEmoteIconColor:
                self.invalidate()
            
        
        
        def handleWhisperModeChange(whisperMode, self = self):
            if self.hasLinkedEmote():
                if self.isVisible() and not self.isWhispering():
                    self.updateEmoteIcon()
                
            

        self.accept(self.getEventName(SCWhisperModeChangeEvent), handleWhisperModeChange)
        
        def handleEmoteEnableStateChange(self = self):
            if self.hasLinkedEmote():
                if self.isVisible() and not self.isWhispering():
                    self.updateEmoteIcon()
                
            

        if self.hasLinkedEmote():
            if Emote.globalEmote:
                self.accept(Emote.globalEmote.EmoteEnableStateChanged, handleEmoteEnableStateChange)
            
        

    
    def exitVisible(self):
        SCElement.exitVisible(self)
        self.ignore(self.getEventName(SCWhisperModeChangeEvent))
        if Emote.globalEmote:
            self.ignore(Emote.globalEmote.EmoteEnableStateChanged)
        

    
    def getDisplayText(self):
        if self.getCharges() is not -1:
            return self.text + ' (%s)' % self.getCharges()
        else:
            return self.text


