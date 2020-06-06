# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggObject
import Namable

class EggNamedObject(EggObject.EggObject, Namable.Namable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggNamedObject__overloaded_constructor_ptrConstEggNamedObject(self, copy):
        self.this = libpandaegg._inPkAOMzuI5(copy.this)
        self.userManagesMemory = 1

    
    def _EggNamedObject__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOM1nQw(name)
        self.userManagesMemory = 1

    
    def _EggNamedObject__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMFcLP()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMpgi_:
            libpandaegg._inPkAOMpgi_(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMcBDe()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMgt6J(self.this, copy.this)
        returnObject = EggNamedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def output(self, out):
        returnValue = libpandaegg._inPkAOMjJfG(self.this, out.this)
        return returnValue

    
    def upcastToNamable(self):
        returnValue = libpandaegg._inPkAOMQtFW(self.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setUserData(self, userData):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMi4s0(upcastSelf.this, userData.this)
        return returnValue

    
    def getUserData(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMWm2j(upcastSelf.this)
        import EggUserData
        returnObject = EggUserData.EggUserData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggNamedObject__overloaded_hasUserData_ptrConstEggObject(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMibXq(upcastSelf.this)
        return returnValue

    
    def _EggNamedObject__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(self, type):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMvhRl(upcastSelf.this, type.this)
        return returnValue

    
    def clearUserData(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM0OqA(upcastSelf.this)
        return returnValue

    
    def hasUserData(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggNamedObject__overloaded_hasUserData_ptrConstEggObject(*_args)
        elif numArgs == 1:
            return self._EggNamedObject__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtKE8f(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtnFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt7Xzz(upcastSelf.this, handle.this)
        return returnValue

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtP11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtaS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtwyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtvpj2(upcastSelf.this)
        return returnValue

    
    def setName(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtZvUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtfARN(upcastSelf.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggNamedObject__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggNamedObject__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggNamedObject):
                return self._EggNamedObject__overloaded_constructor_ptrConstEggNamedObject(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggNamedObject> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


