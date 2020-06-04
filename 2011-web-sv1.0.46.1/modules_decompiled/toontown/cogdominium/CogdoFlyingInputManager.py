# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\CogdoFlyingInputManager.py
from pandac.PandaModules import CollisionSphere, CollisionNode, BitMask32, CollisionHandlerEvent, CollisionRay
from toontown.minigame import ArrowKeys

class CogdoFlyingInputManager:
    __module__ = __name__

    def __init__(self):
        self.arrowKeys = ArrowKeys.ArrowKeys()
        self.arrowKeys.disable()

    def enable(self):
        self.arrowKeys.setPressHandlers([self.__upArrowPressed, self.__downArrowPressed, self.__leftArrowPressed, self.__rightArrowPressed, self.__controlPressed])
        self.arrowKeys.enable()

    def disable(self):
        self.arrowKeys.clearPressHandlers()
        self.arrowKeys.disable()

    def destroy(self):
        self.disable()
        self.arrowKeys.destroy()
        self.arrowKeys = None
        self.refuelLerp = None
        return

    def __upArrowPressed(self):
        pass

    def __downArrowPressed(self):
        pass

    def __leftArrowPressed(self):
        pass

    def __rightArrowPressed(self):
        pass

    def __controlPressed(self):
        pass