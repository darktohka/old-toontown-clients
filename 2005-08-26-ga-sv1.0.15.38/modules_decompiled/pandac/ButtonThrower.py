# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DataNode

class ButtonThrower(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPyiw5k4xy(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPyiw5mOhU()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setPrefix(self, prefix):
        returnValue = libpanda._inPyiw58tb8(self.this, prefix)
        return returnValue

    
    def hasPrefix(self):
        returnValue = libpanda._inPyiw5ynYr(self.this)
        return returnValue

    
    def getPrefix(self):
        returnValue = libpanda._inPyiw53m_a(self.this)
        return returnValue

    
    def setTimeFlag(self, timeFlag):
        returnValue = libpanda._inPyiw5Y3F7(self.this, timeFlag)
        return returnValue

    
    def getTimeFlag(self):
        returnValue = libpanda._inPyiw5WTVj(self.this)
        return returnValue

    
    def addParameter(self, obj):
        returnValue = libpanda._inPyiw5HaR_(self.this, obj.this)
        return returnValue

    
    def getNumParameters(self):
        returnValue = libpanda._inPyiw5bj99(self.this)
        return returnValue

    
    def getParameter(self, n):
        returnValue = libpanda._inPyiw5amFl(self.this, n)
        import EventParameter
        returnObject = EventParameter.EventParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getModifierButtons(self):
        returnValue = libpanda._inPyiw5GlsX(self.this)
        import ModifierButtons
        returnObject = ModifierButtons.ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setModifierButtons(self, mods):
        returnValue = libpanda._inPyiw57l_D(self.this, mods.this)
        return returnValue

    
    def setThrowButtonsActive(self, flag):
        returnValue = libpanda._inPyiw5uTqR(self.this, flag)
        return returnValue

    
    def getThrowButtonsActive(self):
        returnValue = libpanda._inPyiw55I8a(self.this)
        return returnValue

    
    def addThrowButton(self, mods, button):
        returnValue = libpanda._inPyiw5Ji9T(self.this, mods.this, button.this)
        return returnValue

    
    def removeThrowButton(self, mods, button):
        returnValue = libpanda._inPyiw5psxI(self.this, mods.this, button.this)
        return returnValue

    
    def _ButtonThrower__overloaded_hasThrowButton_ptrConstButtonThrower_ptrConstButtonHandle(self, button):
        returnValue = libpanda._inPyiw5UvSd(self.this, button.this)
        return returnValue

    
    def _ButtonThrower__overloaded_hasThrowButton_ptrConstButtonThrower_ptrConstModifierButtons_ptrConstButtonHandle(self, mods, button):
        returnValue = libpanda._inPyiw5cX_g(self.this, mods.this, button.this)
        return returnValue

    
    def clearThrowButtons(self):
        returnValue = libpanda._inPyiw5MSSv(self.this)
        return returnValue

    
    def hasThrowButton(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ButtonThrower__overloaded_hasThrowButton_ptrConstButtonThrower_ptrConstButtonHandle(*_args)
        elif numArgs == 2:
            return self._ButtonThrower__overloaded_hasThrowButton_ptrConstButtonThrower_ptrConstModifierButtons_ptrConstButtonHandle(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


