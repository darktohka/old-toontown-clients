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
    
    def _CollisionHandlerPhysical__overloaded_addCollider_ptrCollisionHandlerPhysical_ptrConstNodePath_ptrConstNodePath(self, collider, target):
        returnValue = libpanda._inPHwcaHz2x(self.this, collider.this, target.this)
        return returnValue

    
    def _CollisionHandlerPhysical__overloaded_addCollider_ptrCollisionHandlerPhysical_ptrConstNodePath_ptrConstNodePath_ptrDriveInterface(self, collider, target, driveInterface):
        returnValue = libpanda._inPHwcajnQs(self.this, collider.this, target.this, driveInterface.this)
        return returnValue

    
    def removeCollider(self, collider):
        returnValue = libpanda._inPHwca9hFg(self.this, collider.this)
        return returnValue

    
    def hasCollider(self, collider):
        returnValue = libpanda._inPHwcatNFK(self.this, collider.this)
        return returnValue

    
    def clearColliders(self):
        returnValue = libpanda._inPHwcaVoUz(self.this)
        return returnValue

    
    def setCenter(self, center):
        returnValue = libpanda._inPHwca9CVE(self.this, center.this)
        return returnValue

    
    def clearCenter(self):
        returnValue = libpanda._inPHwcaRo9a(self.this)
        return returnValue

    
    def getCenter(self):
        returnValue = libpanda._inPHwca_dUV(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasCenter(self):
        returnValue = libpanda._inPHwcaf3XJ(self.this)
        return returnValue

    
    def addCollider(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import NodePath
                if isinstance(_args[1], NodePath.NodePath):
                    return self._CollisionHandlerPhysical__overloaded_addCollider_ptrCollisionHandlerPhysical_ptrConstNodePath_ptrConstNodePath(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <NodePath.NodePath> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        elif numArgs == 3:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import NodePath
                if isinstance(_args[1], NodePath.NodePath):
                    import DriveInterface
                    if isinstance(_args[2], DriveInterface.DriveInterface):
                        return self._CollisionHandlerPhysical__overloaded_addCollider_ptrCollisionHandlerPhysical_ptrConstNodePath_ptrConstNodePath_ptrDriveInterface(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <DriveInterface.DriveInterface> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <NodePath.NodePath> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


