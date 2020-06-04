# File: G (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase import PandaObject
from direct.fsm import StateData
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer

class GenderShop(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.shopsVisited = []
        self.toon = None
        self.gender = 'm'
        return None

    
    def enter(self):
        base.disableMouse()
        return None

    
    def showButtons(self):
        return None

    
    def exit(self):
        return None

    
    def load(self):
        return None

    
    def unload(self):
        return None

    
    def setGender(self, choice):
        self._GenderShop__setGender(choice)

    
    def _GenderShop__setGender(self, choice):
        if choice == -1:
            self.gender = 'm'
        else:
            self.gender = 'f'
        messenger.send(self.doneEvent)


