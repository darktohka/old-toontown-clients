# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DNADoor

class DNAFlatDoor(DNADoor.DNADoor, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNAFlatDoor__overloaded_constructor_ptrConstDNAFlatDoor(self, door):
        self.this = libtoontown._inPdt4yk_L2(door.this)
        self.userManagesMemory = 1

    
    def _DNAFlatDoor__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPdt4yd2xd(initialName)
        self.userManagesMemory = 1

    
    def _DNAFlatDoor__overloaded_constructor(self):
        self.this = libtoontown._inPdt4y3kUU()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yD0kH:
            libtoontown._inPdt4yD0kH(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4ywULa()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNAFlatDoor__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNAFlatDoor__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DNAFlatDoor):
                return self._DNAFlatDoor__overloaded_constructor_ptrConstDNAFlatDoor(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAFlatDoor> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


