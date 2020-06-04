# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PGItem

class PGWaitBar(PGItem.PGItem, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _PGWaitBar__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPWvim2gol(name)
        self.userManagesMemory = 1

    
    def _PGWaitBar__overloaded_constructor(self):
        self.this = libpanda._inPWvimBDaN()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPWvimqfJI()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setup(self, width, height, range):
        returnValue = libpanda._inPWvimeliW(self.this, width, height, range)
        return returnValue

    
    def setRange(self, range):
        returnValue = libpanda._inPWvimlD51(self.this, range)
        return returnValue

    
    def getRange(self):
        returnValue = libpanda._inPWvimzi4i(self.this)
        return returnValue

    
    def setValue(self, value):
        returnValue = libpanda._inPWvimPBDg(self.this, value)
        return returnValue

    
    def getValue(self):
        returnValue = libpanda._inPWvimTfCN(self.this)
        return returnValue

    
    def getPercent(self):
        returnValue = libpanda._inPWvimmaCx(self.this)
        return returnValue

    
    def setBarStyle(self, style):
        returnValue = libpanda._inPWvimtJct(self.this, style.this)
        return returnValue

    
    def getBarStyle(self):
        returnValue = libpanda._inPWvimAw4C(self.this)
        import PGFrameStyle
        returnObject = PGFrameStyle.PGFrameStyle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PGWaitBar__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._PGWaitBar__overloaded_constructor_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


