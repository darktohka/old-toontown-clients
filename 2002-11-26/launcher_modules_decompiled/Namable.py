# File: N (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class Namable(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Namable__overloaded_constructor_ptrConstNamable(self, copy):
        self.this = libpandaexpress._inPJoxtwaR_(copy.this)
        self.userManagesMemory = 1

    
    def _Namable__overloaded_constructor_atomicstring(self, initialName):
        self.this = libpandaexpress._inPJoxtYXC2(initialName)
        self.userManagesMemory = 1

    
    def _Namable__overloaded_constructor(self):
        self.this = libpandaexpress._inPJoxtBFnx()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtgzYG:
            libpandaexpress._inPJoxtgzYG(self.this)
        

    
    def getClassType():
        returnValue = libpandaexpress._inPJoxt4mnx()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, other):
        returnValue = libpandaexpress._inPJoxtp1bI(self.this, other.this)
        returnObject = Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setName(self, name):
        returnValue = libpandaexpress._inPJoxtLNBW(self.this, name)
        return returnValue

    
    def clearName(self):
        returnValue = libpandaexpress._inPJoxtavUl(self.this)
        return returnValue

    
    def hasName(self):
        returnValue = libpandaexpress._inPJoxtYjhC(self.this)
        return returnValue

    
    def getName(self):
        returnValue = libpandaexpress._inPJoxtfARN(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPJoxtvz7q(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Namable__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Namable__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], Namable):
                return self._Namable__overloaded_constructor_ptrConstNamable(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Namable> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


