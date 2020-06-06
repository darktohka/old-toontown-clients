# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PGItem

class PGWaitBar(PGItem.PGItem, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PGWaitBar__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPVvim3gol(name)
        self.userManagesMemory = 1

    
    def _PGWaitBar__overloaded_constructor(self):
        self.this = libpanda._inPVvimBDaN()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPVvimqfJI()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setup(self, width, height, range):
        returnValue = libpanda._inPVvimeliW(self.this, width, height, range)
        return returnValue

    
    def setRange(self, range):
        returnValue = libpanda._inPVvimqD51(self.this, range)
        return returnValue

    
    def getRange(self):
        returnValue = libpanda._inPVvim0i4i(self.this)
        return returnValue

    
    def setValue(self, value):
        returnValue = libpanda._inPVvimMBDg(self.this, value)
        return returnValue

    
    def getValue(self):
        returnValue = libpanda._inPVvimTfCN(self.this)
        return returnValue

    
    def getPercent(self):
        returnValue = libpanda._inPVvimnaCx(self.this)
        return returnValue

    
    def setBarStyle(self, style):
        returnValue = libpanda._inPVvimsJct(self.this, style.this)
        return returnValue

    
    def getBarStyle(self):
        returnValue = libpanda._inPVvimAw4C(self.this)
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
            return self._PGWaitBar__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PGWaitBar__overloaded_constructor_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


