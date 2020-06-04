# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggAnimData

class EggSAnimData(EggAnimData.EggAnimData, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggSAnimData__overloaded_constructor_ptrConstEggSAnimData(self, copy):
        self.this = libpandaegg._inPkAOMKf_r(copy.this)
        self.userManagesMemory = 1

    
    def _EggSAnimData__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOMaUFB(name)
        self.userManagesMemory = 1

    
    def _EggSAnimData__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMhDOv()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMm0Fq:
            libpandaegg._inPkAOMm0Fq(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMmWjq()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOM9kyZ(self.this, copy.this)
        returnObject = EggSAnimData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumRows(self):
        returnValue = libpandaegg._inPkAOMpyvE(self.this)
        return returnValue

    
    def getValue(self, row):
        returnValue = libpandaegg._inPkAOMtEEc(self.this, row)
        return returnValue

    
    def setValue(self, row, value):
        returnValue = libpandaegg._inPkAOMS9Mu(self.this, row, value)
        return returnValue

    
    def optimize(self):
        returnValue = libpandaegg._inPkAOML8bt(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggSAnimData__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggSAnimData__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggSAnimData):
                return self._EggSAnimData__overloaded_constructor_ptrConstEggSAnimData(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggSAnimData> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


