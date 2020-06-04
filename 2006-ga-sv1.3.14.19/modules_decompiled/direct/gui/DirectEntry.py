# File: D (Python 2.2)

from DirectFrame import *
ENTRY_FOCUS_STATE = PGEntry.SFocus
ENTRY_NO_FOCUS_STATE = PGEntry.SNoFocus
ENTRY_INACTIVE_STATE = PGEntry.SInactive

class DirectEntry(DirectFrame):
    
    def __init__(self, parent = None, **kw):
        optiondefs = (('pgFunc', PGEntry, None), ('numStates', 3, None), ('state', NORMAL, None), ('entryFont', None, INITOPT), ('width', 10, self.setup), ('numLines', 5, self.setup), ('focus', 0, self.setFocus), ('cursorKeys', 0, self.setCursorKeysActive), ('obscured', 0, self.setObscureMode), ('backgroundFocus', 0, self.setBackgroundFocus), ('initialText', '', INITOPT), ('command', None, None), ('extraArgs', [], None), ('focusInCommand', None, None), ('focusInExtraArgs', [], None), ('focusOutCommand', None, None), ('focusOutExtraArgs', [], None), ('rolloverSound', getDefaultRolloverSound(), self.setRolloverSound), ('clickSound', getDefaultClickSound(), self.setClickSound))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        if self['entryFont'] == None:
            font = getDefaultFont()
        else:
            font = self['entryFont']
        self.onscreenText = self.createcomponent('text', (), None, OnscreenText, (), parent = hidden, text = '', align = TextNode.ALeft, font = font, scale = 1, mayChange = 1)
        self.onscreenText.removeNode()
        self.bind(ACCEPT, self.commandFunc)
        self.accept(self.guiItem.getFocusInEvent(), self.focusInCommandFunc)
        self.accept(self.guiItem.getFocusOutEvent(), self.focusOutCommandFunc)
        self.initialiseoptions(DirectEntry)
        for i in range(self['numStates']):
            self.guiItem.setTextDef(i, self.onscreenText.textNode)
        
        if self['initialText']:
            self.set(self['initialText'])
        

    
    def destroy(self):
        self.ignore(self.guiItem.getFocusInEvent())
        self.ignore(self.guiItem.getFocusOutEvent())
        DirectFrame.destroy(self)

    
    def setup(self):
        self.node().setup(self['width'], self['numLines'])

    
    def setFocus(self):
        PGEntry.setFocus(self.guiItem, self['focus'])

    
    def setCursorKeysActive(self):
        PGEntry.setCursorKeysActive(self.guiItem, self['cursorKeys'])

    
    def setObscureMode(self):
        PGEntry.setObscureMode(self.guiItem, self['obscured'])

    
    def setBackgroundFocus(self):
        PGEntry.setBackgroundFocus(self.guiItem, self['backgroundFocus'])

    
    def setRolloverSound(self):
        rolloverSound = self['rolloverSound']
        if rolloverSound:
            self.guiItem.setSound(ENTER + self.guiId, rolloverSound)
        else:
            self.guiItem.clearSound(ENTER + self.guiId)

    
    def setClickSound(self):
        clickSound = self['clickSound']
        if clickSound:
            self.guiItem.setSound(ACCEPT + self.guiId, clickSound)
        else:
            self.guiItem.clearSound(ACCEPT + self.guiId)

    
    def commandFunc(self, event):
        if self['command']:
            apply(self['command'], [
                self.get()] + self['extraArgs'])
        

    
    def focusInCommandFunc(self):
        if self['focusInCommand']:
            apply(self['focusInCommand'], self['focusInExtraArgs'])
        

    
    def focusOutCommandFunc(self):
        if self['focusOutCommand']:
            apply(self['focusOutCommand'], self['focusOutExtraArgs'])
        

    
    def set(self, text):
        self.guiItem.setText(text)

    
    def get(self):
        return self.guiItem.getText()

    
    def setCursorPosition(self, pos):
        if pos < 0:
            self.guiItem.setCursorPosition(len(self.get()) + pos)
        else:
            self.guiItem.setCursorPosition(pos)

    
    def enterText(self, text):
        self.set(text)
        self.setCursorPosition(len(self.get()))


