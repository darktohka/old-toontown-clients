# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNANode

class DNAFlatBuilding(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DNAFlatBuilding__overloaded_constructor_ptrConstDNAFlatBuilding(self, building):
        self.this = libtoontown._inPet4y2FIO(building.this)
        self.userManagesMemory = 1

    
    def _DNAFlatBuilding__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPet4ycl4a(initialName)
        self.userManagesMemory = 1

    
    def _DNAFlatBuilding__overloaded_constructor(self):
        self.this = libtoontown._inPet4ydUKf()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4y95QK:
            libtoontown._inPet4y95QK(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPet4y8O0g()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setWidth(self, width):
        returnValue = libtoontown._inPet4yv2r5(self.this, width)
        return returnValue

    
    def getWidth(self):
        returnValue = libtoontown._inPet4yQbr5(self.this)
        return returnValue

    
    def getCurrentWallHeight(self):
        returnValue = libtoontown._inPet4yTVhS(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNAFlatBuilding__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNAFlatBuilding__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], DNAFlatBuilding):
                return self._DNAFlatBuilding__overloaded_constructor_ptrConstDNAFlatBuilding(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAFlatBuilding> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


