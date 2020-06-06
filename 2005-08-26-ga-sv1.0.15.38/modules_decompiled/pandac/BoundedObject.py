# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class BoundedObject(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    BVTDynamicSphere = 1
    BVTStatic = 0
    
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
        if libpanda and libpanda._inPMAKPcJrv:
            libpanda._inPMAKPcJrv(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPMAKPGV7v()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _BoundedObject__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(self, type):
        returnValue = libpanda._inPMAKPC76J(self.this, type)
        return returnValue

    
    def _BoundedObject__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(self, volume):
        returnValue = libpanda._inPMAKPUVRr(self.this, volume.this)
        return returnValue

    
    def getBound(self):
        returnValue = libpanda._inPMAKPtOIb(self.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def markBoundStale(self):
        returnValue = libpanda._inPMAKPG4uI(self.this)
        return returnValue

    
    def forceBoundStale(self):
        returnValue = libpanda._inPMAKPj1Pw(self.this)
        return returnValue

    
    def isBoundStale(self):
        returnValue = libpanda._inPMAKPkac5(self.this)
        return returnValue

    
    def setFinal(self, flag):
        returnValue = libpanda._inPMAKPy9vH(self.this, flag)
        return returnValue

    
    def isFinal(self):
        returnValue = libpanda._inPMAKPbuL4(self.this)
        return returnValue

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._BoundedObject__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(*_args)
            
            import BoundingVolume
            if isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._BoundedObject__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


