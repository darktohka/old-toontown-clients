# File: U (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class UpdateSeq(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _UpdateSeq__overloaded_constructor(self):
        self.this = libpanda._inPflboeAZ3()
        self.userManagesMemory = 1

    
    def _UpdateSeq__overloaded_constructor_ptrConstUpdateSeq(self, copy):
        self.this = libpanda._inPflboTpCm(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPflboJ1Jz:
            libpanda._inPflboJ1Jz(self.this)
        

    
    def initial():
        returnValue = libpanda._inPflboXroR()
        returnObject = UpdateSeq(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    initial = staticmethod(initial)
    
    def old():
        returnValue = libpanda._inPflbonK4u()
        returnObject = UpdateSeq(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    old = staticmethod(old)
    
    def fresh():
        returnValue = libpanda._inPflbo9eRT()
        returnObject = UpdateSeq(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    fresh = staticmethod(fresh)
    
    def assign(self, copy):
        returnValue = libpanda._inPflboGswc(self.this, copy.this)
        returnObject = UpdateSeq(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clear(self):
        returnValue = libpanda._inPflbo0_vY(self.this)
        return returnValue

    
    def isInitial(self):
        returnValue = libpanda._inPflboT1E2(self.this)
        return returnValue

    
    def isOld(self):
        returnValue = libpanda._inPflboLeqi(self.this)
        return returnValue

    
    def isFresh(self):
        returnValue = libpanda._inPflboWsUb(self.this)
        return returnValue

    
    def isSpecial(self):
        returnValue = libpanda._inPflbo6gLj(self.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPflbogvS2(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPflbogevt(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPflboNGO_(self.this, other.this)
        return returnValue

    
    def lessThanOrEqual(self, other):
        returnValue = libpanda._inPflbowJ_1(self.this, other.this)
        return returnValue

    
    def _UpdateSeq__overloaded_increment_ptrUpdateSeq(self):
        returnValue = libpanda._inPflbokAFl(self.this)
        returnObject = UpdateSeq(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _UpdateSeq__overloaded_increment_ptrUpdateSeq_int(self, parameter1):
        returnValue = libpanda._inPflboqToO(self.this, parameter1)
        returnObject = UpdateSeq(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libpanda._inPflboHG_1(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._UpdateSeq__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._UpdateSeq__overloaded_constructor_ptrConstUpdateSeq(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def increment(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._UpdateSeq__overloaded_increment_ptrUpdateSeq(*_args)
        elif numArgs == 1:
            return self._UpdateSeq__overloaded_increment_ptrUpdateSeq_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


