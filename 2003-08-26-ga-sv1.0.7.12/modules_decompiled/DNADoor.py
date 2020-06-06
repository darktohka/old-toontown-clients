# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNAGroup

class DNADoor(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DNADoor__overloaded_constructor_ptrConstDNADoor(self, door):
        self.this = libtoontown._inPet4yc9GJ(door.this)
        self.userManagesMemory = 1

    
    def _DNADoor__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPet4yTHFL(initialName)
        self.userManagesMemory = 1

    
    def _DNADoor__overloaded_constructor(self):
        self.this = libtoontown._inPet4yIlrG()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4ytrhA:
            libtoontown._inPet4ytrhA(self.this)
        

    
    def setupDoor(doorNodePath, parent, doorOrigin, store, block, color):
        returnValue = libtoontown._inPet4ykSvf(doorNodePath.this, parent.this, doorOrigin.this, store.this, block, color.this)
        return returnValue

    setupDoor = staticmethod(setupDoor)
    
    def getClassType():
        returnValue = libtoontown._inPet4y5LO9()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPet4y0J0Z(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPet4yxcDR(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPet4yjDjV(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPet4ySh9z(self.this)
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
            return self._DNADoor__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNADoor__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], DNADoor):
                return self._DNADoor__overloaded_constructor_ptrConstDNADoor(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNADoor> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


