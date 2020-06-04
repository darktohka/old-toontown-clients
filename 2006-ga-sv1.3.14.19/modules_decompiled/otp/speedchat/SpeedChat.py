# File: S (Python 2.2)

from direct.showbase.PythonUtil import boolEqual
from SpeedChatTypes import *
from SCSettings import SCSettings
from SCTerminal import SCWhisperModeChangeEvent
from otp.otpbase import OTPLocalizer

class SpeedChat(SCMenu):
    
    def __init__(self, name = '', structure = None, backgroundModelName = None, guiModelName = None):
        SCMenu.BackgroundModelName = backgroundModelName
        SCMenu.GuiModelName = guiModelName
        SCMenu.__init__(self)
        self.name = name
        self.settings = SCSettings(eventPrefix = self.name)
        self.privSetSettingsRef(self.settings)
        if structure is not None:
            self.rebuildFromStructure(structure)
        

    
    def destroy(self):
        SCMenu.destroy(self)

    
    def __str__(self):
        return "%s: '%s'" % (self.__class__.__name__, self.name)

    
    def enter(self):
        self.enterVisible()

    
    def exit(self):
        self.exitVisible()

    
    def setWhisperMode(self, whisperMode):
        if not boolEqual(self.settings.whisperMode, whisperMode):
            self.settings.whisperMode = whisperMode
            messenger.send(self.getEventName(SCWhisperModeChangeEvent), [
                whisperMode])
        

    
    def setColorScheme(self, colorScheme):
        self.settings.colorScheme = colorScheme
        self.invalidateAll()

    
    def setSubmenuOverlap(self, submenuOverlap):
        self.settings.submenuOverlap = submenuOverlap
        self.invalidateAll()

    
    def setTopLevelOverlap(self, topLevelOverlap):
        self.settings.topLevelOverlap = topLevelOverlap
        self.invalidateAll()

    
    def finalizeAll(self):
        self.notify.debug('finalizing entire SpeedChat tree')
        SCMenu.finalizeAll(self)


