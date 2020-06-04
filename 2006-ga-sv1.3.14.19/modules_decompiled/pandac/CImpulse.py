# File: C (Python 2.2)

import types
import libotp
import libotpDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class CImpulse(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libotpDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libotp._inPYe454nMJ()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libotp._inPYe45380p()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def process(self, dt):
        returnValue = libotp._inPYe45nedf(self.this, dt)
        return returnValue

    
    def setMover(self, mover):
        returnValue = libotp._inPYe45WdFU(self.this, mover.this)
        return returnValue

    
    def clearMover(self, mover):
        returnValue = libotp._inPYe45TShj(self.this, mover.this)
        return returnValue

    
    def getMover(self):
        returnValue = libotp._inPYe45jia4(self.this)
        import CMover
        returnObject = CMover.CMover(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getNodePath(self):
        returnValue = libotp._inPYe458u3U(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def isCpp(self):
        returnValue = libotp._inPYe45IytT(self.this)
        return returnValue


