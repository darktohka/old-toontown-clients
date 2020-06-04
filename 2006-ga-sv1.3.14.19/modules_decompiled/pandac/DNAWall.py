# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DNANode

class DNAWall(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNAWall__overloaded_constructor_ptrConstDNAWall(self, wall):
        self.this = libtoontown._inPdt4y0GQk(wall.this)
        self.userManagesMemory = 1

    
    def _DNAWall__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPdt4yCZcm(initialName)
        self.userManagesMemory = 1

    
    def _DNAWall__overloaded_constructor(self):
        self.this = libtoontown._inPdt4yGhBi()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yhHbW:
            libtoontown._inPdt4yhHbW(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4yKSbO()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPdt4yAfAr(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPdt4y9IPi(self.this)
        return returnValue

    
    def setHeight(self, height):
        returnValue = libtoontown._inPdt4yLVdS(self.this, height)
        return returnValue

    
    def getHeight(self):
        returnValue = libtoontown._inPdt4yuHve(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPdt4yzRvm(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPdt4yC2JF(self.this)
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
            return self._DNAWall__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNAWall__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DNAWall):
                return self._DNAWall__overloaded_constructor_ptrConstDNAWall(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAWall> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


