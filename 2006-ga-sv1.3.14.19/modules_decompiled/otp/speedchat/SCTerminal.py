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
        

    
    def onMouseClick(self, event):
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
        


