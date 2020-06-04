# File: S (Python 2.2)

from PythonUtil import boolEqual
from SpeedChatTypes import *
from SCSettings import SCSettings
from SCTerminal import SCWhisperModeChangeEvent
import Localizer

class SpeedChat(SCMenu):
    
    def __init__(self, name = '', structure = None):
        SCMenu.__init__(self)
        self.name = name
        self.settings = SCSettings(eventPrefix = self.name)
        self.privSetSettingsRef(self.settings)
        if structure is not None:
            self.privConstruct(structure)
        

    
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

    
    def privConstruct(self, structure):
        
        def addChildren(menu, childList):
            for child in childList:
                emote = None
                if type(child) == type({ }):
                    item = child.keys()[0]
                    emote = child[item]
                    child = item
                
                
                def addTerminal(terminal, menu = menu, emote = emote):
                    if emote is not None:
                        terminal.setLinkedEmote(emote)
                    
                    menu.append(terminal)

                if type(child) == type(0):
                    addTerminal(SCStaticTextTerminal(child))
                elif type(child) == type([]):
                    if type(child[0]) == type(''):
                        holderTitle = child[0]
                        subMenu = SCMenu()
                        subMenuChildren = child[1:]
                    else:
                        (menuType, holderTitle) = (child[0], child[1])
                        subMenu = menuType()
                        subMenuChildren = child[2:]
                    if emote:
                        print 'warning: tried to link emote %s to a menu holder' % emote
                    
                    holder = SCMenuHolder(holderTitle, menu = subMenu)
                    menu.append(holder)
                    addChildren(subMenu, subMenuChildren)
                else:
                    raise 'error parsing speedchat structure. invalid child: %s' % child
            

        addChildren(self, structure)


