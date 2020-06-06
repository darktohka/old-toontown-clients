# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import MovingPartMatrix

class CharacterJoint(MovingPartMatrix.MovingPartMatrix, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnRYRj_mB:
            libpanda._inPnRYRj_mB(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnRYRp_fE()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def addNetTransform(self, node):
        returnValue = libpanda._inPnRYR0hP_(self.this, node.this)
        return returnValue

    
    def removeNetTransform(self, node):
        returnValue = libpanda._inPnRYR6yW0(self.this, node.this)
        return returnValue

    
    def hasNetTransform(self, node):
        returnValue = libpanda._inPnRYRHxNe(self.this, node.this)
        return returnValue

    
    def clearNetTransforms(self):
        returnValue = libpanda._inPnRYRLDWU(self.this)
        return returnValue

    
    def addLocalTransform(self, node):
        returnValue = libpanda._inPnRYRDPic(self.this, node.this)
        return returnValue

    
    def removeLocalTransform(self, node):
        returnValue = libpanda._inPnRYRosae(self.this, node.this)
        return returnValue

    
    def hasLocalTransform(self, node):
        returnValue = libpanda._inPnRYRPfag(self.this, node.this)
        return returnValue

    
    def clearLocalTransforms(self):
        returnValue = libpanda._inPnRYRGw1l(self.this)
        return returnValue

    
    def getTransform(self, transform):
        returnValue = libpanda._inPnRYRDAfP(self.this, transform.this)
        return returnValue


