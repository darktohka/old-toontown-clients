# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNANode

class DNAWall(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DNAWall__overloaded_constructor_ptrConstDNAWall(self, wall):
        self.this = libtoontown._inPet4y1GQk(wall.this)
        self.userManagesMemory = 1

    
    def _DNAWall__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPet4yDZcm(initialName)
        self.userManagesMemory = 1

    
    def _DNAWall__overloaded_constructor(self):
        self.this = libtoontown._inPet4yFhBi()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4yhHbW:
            libtoontown._inPet4yhHbW(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPet4yKSbO()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPet4yBfAr(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPet4y_IPi(self.this)
        return returnValue

    
    def setHeight(self, height):
        returnValue = libtoontown._inPet4yLVdS(self.this, height)
        return returnValue

    
    def getHeight(self):
        returnValue = libtoontown._inPet4yuHve(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPet4y0Rvm(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPet4yC2JF(self.this)
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
            return self._DNAWall__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNAWall__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], DNAWall):
                return self._DNAWall__overloaded_constructor_ptrConstDNAWall(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAWall> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


