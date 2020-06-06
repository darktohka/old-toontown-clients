# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionHandlerEvent

class CollisionHandlerPhysical(CollisionHandlerEvent.CollisionHandlerEvent, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaT4lv:
            libpanda._inPHwcaT4lv(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaMl13()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def addColliderDrive(self, node, driveInterface):
        returnValue = libpanda._inPHwca78SS(self.this, node.this, driveInterface.this)
        return returnValue

    
    def addColliderNode(self, node, target):
        returnValue = libpanda._inPHwcap48k(self.this, node.this, target.this)
        return returnValue

    
    def removeCollider(self, node):
        returnValue = libpanda._inPHwca6VCL(self.this, node.this)
        return returnValue

    
    def hasCollider(self, node):
        returnValue = libpanda._inPHwcae_P4(self.this, node.this)
        return returnValue

    
    def clearColliders(self):
        returnValue = libpanda._inPHwcaVoUz(self.this)
        return returnValue


