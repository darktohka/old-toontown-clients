# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggGroupNode

class EggTable(EggGroupNode.EggGroupNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    TTInvalid = 0
    TTBundle = 2
    TTTable = 1
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggTable__overloaded_constructor_ptrConstEggTable(self, copy):
        self.this = libpandaegg._inPkAOM4E8v(copy.this)
        self.userManagesMemory = 1

    
    def _EggTable__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOMTQ_y(name)
        self.userManagesMemory = 1

    
    def _EggTable__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMSp2D()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMNvwz:
            libpandaegg._inPkAOMNvwz(self.this)
        

    
    def stringTableType(cString):
        returnValue = libpandaegg._inPkAOMg8gw(cString)
        return returnValue

    stringTableType = staticmethod(stringTableType)
    
    def getClassType():
        returnValue = libpandaegg._inPkAOMS_i1()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMxP6Z(self.this, copy.this)
        returnObject = EggTable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setTableType(self, type):
        returnValue = libpandaegg._inPkAOM_8_9(self.this, type)
        return returnValue

    
    def getTableType(self):
        returnValue = libpandaegg._inPkAOMaj1_(self.this)
        return returnValue

    
    def hasTransform(self):
        returnValue = libpandaegg._inPkAOMZ_ev(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggTable__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggTable__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggTable):
                return self._EggTable__overloaded_constructor_ptrConstEggTable(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggTable> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


