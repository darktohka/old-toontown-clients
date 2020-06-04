# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DNAGroup

class DNADoor(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNADoor__overloaded_constructor_ptrConstDNADoor(self, door):
        self.this = libtoontown._inPdt4yc9GJ(door.this)
        self.userManagesMemory = 1

    
    def _DNADoor__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPdt4yTHFL(initialName)
        self.userManagesMemory = 1

    
    def _DNADoor__overloaded_constructor(self):
        self.this = libtoontown._inPdt4yIlrG()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4ytrhA:
            libtoontown._inPdt4ytrhA(self.this)
        

    
    def setupDoor(doorNodePath, parent, doorOrigin, store, block, color):
        returnValue = libtoontown._inPdt4ykSvf(doorNodePath.this, parent.this, doorOrigin.this, store.this, block, color.this)
        return returnValue

    setupDoor = staticmethod(setupDoor)
    
    def getClassType():
        returnValue = libtoontown._inPdt4y4LO9()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPdt4y0J0Z(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPdt4yxcDR(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPdt4yjDjV(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPdt4yTh9z(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNADoor__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNADoor__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DNADoor):
                return self._DNADoor__overloaded_constructor_ptrConstDNADoor(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNADoor> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


