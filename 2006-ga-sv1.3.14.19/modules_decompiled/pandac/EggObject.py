# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class EggObject(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggObject__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMc5tZ()
        self.userManagesMemory = 1

    
    def _EggObject__overloaded_constructor_ptrConstEggObject(self, copy):
        self.this = libpandaegg._inPkAOM6VZo(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOML1Gc()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOM43pX(self.this, copy.this)
        returnObject = EggObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setUserData(self, userData):
        returnValue = libpandaegg._inPkAOMi4s0(self.this, userData.this)
        return returnValue

    
    def getUserData(self):
        returnValue = libpandaegg._inPkAOMWm2j(self.this)
        import EggUserData
        returnObject = EggUserData.EggUserData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggObject__overloaded_hasUserData_ptrConstEggObject(self):
        returnValue = libpandaegg._inPkAOMibXq(self.this)
        return returnValue

    
    def _EggObject__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(self, type):
        returnValue = libpandaegg._inPkAOMvhRl(self.this, type.this)
        return returnValue

    
    def clearUserData(self):
        returnValue = libpandaegg._inPkAOM0OqA(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggObject__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._EggObject__overloaded_constructor_ptrConstEggObject(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def hasUserData(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggObject__overloaded_hasUserData_ptrConstEggObject(*_args)
        elif numArgs == 1:
            return self._EggObject__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


