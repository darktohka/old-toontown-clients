# File: N (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class Namable(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Namable__overloaded_constructor_ptrConstNamable(self, copy):
        self.this = libpandaexpress._inPKoxtxaR_(copy.this)
        self.userManagesMemory = 1

    
    def _Namable__overloaded_constructor_atomicstring(self, initialName):
        self.this = libpandaexpress._inPKoxtZXC2(initialName)
        self.userManagesMemory = 1

    
    def _Namable__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtAFnx()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtgzYG:
            libpandaexpress._inPKoxtgzYG(self.this)
        

    
    def getClassType():
        returnValue = libpandaexpress._inPKoxt_mnx()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, other):
        returnValue = libpandaexpress._inPKoxtp1bI(self.this, other.this)
        returnObject = Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setName(self, name):
        returnValue = libpandaexpress._inPKoxtLNBW(self.this, name)
        return returnValue

    
    def clearName(self):
        returnValue = libpandaexpress._inPKoxtZvUl(self.this)
        return returnValue

    
    def hasName(self):
        returnValue = libpandaexpress._inPKoxtYjhC(self.this)
        return returnValue

    
    def getName(self):
        returnValue = libpandaexpress._inPKoxtfARN(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtoz7q(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Namable__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Namable__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], Namable):
                return self._Namable__overloaded_constructor_ptrConstNamable(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Namable> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


