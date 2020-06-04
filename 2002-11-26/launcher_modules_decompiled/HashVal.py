# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class HashVal(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _HashVal__overloaded_constructor(self):
        self.this = libpandaexpress._inPJoxtI_Ud()
        self.userManagesMemory = 1

    
    def _HashVal__overloaded_constructor_ptrConstHashVal(self, copy):
        self.this = libpandaexpress._inPJoxtH_4C(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtzpzW:
            libpandaexpress._inPJoxtzpzW(self.this)
        

    
    def eq(self, other):
        returnValue = libpandaexpress._inPJoxtnq7I(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPJoxt7G7E(self.this, other.this)
        return returnValue

    
    def getValue(self, val):
        returnValue = libpandaexpress._inPJoxtE8pN(self.this, val)
        return returnValue

    
    def setValue(self, val, hash):
        returnValue = libpandaexpress._inPJoxtsUy6(self.this, val, hash)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPJoxtM3Nu(self.this, out.this)
        return returnValue

    
    def asString(self):
        returnValue = libpandaexpress._inPJoxtjkYT(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._HashVal__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], HashVal):
                return self._HashVal__overloaded_constructor_ptrConstHashVal(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <HashVal> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


