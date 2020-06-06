# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount
import BoundedObject

class CollisionSolid(TypedWritableReferenceCount.TypedWritableReferenceCount, BoundedObject.BoundedObject, FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPHwca2uHD:
            libpanda._inPHwca2uHD(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaLN1N()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setTangible(self, tangible):
        returnValue = libpanda._inPHwcaXfKF(self.this, tangible)
        return returnValue

    
    def isTangible(self):
        returnValue = libpanda._inPHwcaPJ9V(self.this)
        return returnValue

    
    def setEffectiveNormal(self, effectiveNormal):
        returnValue = libpanda._inPHwcaXl2n(self.this, effectiveNormal.this)
        return returnValue

    
    def clearEffectiveNormal(self):
        returnValue = libpanda._inPHwcaMg6D(self.this)
        return returnValue

    
    def hasEffectiveNormal(self):
        returnValue = libpanda._inPHwcaUtHP(self.this)
        return returnValue

    
    def getEffectiveNormal(self):
        returnValue = libpanda._inPHwca8DHC(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setRespectEffectiveNormal(self, respectEffectiveNormal):
        returnValue = libpanda._inPHwcaBuoM(self.this, respectEffectiveNormal)
        return returnValue

    
    def getRespectEffectiveNormal(self):
        returnValue = libpanda._inPHwcaGbQo(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPHwcadFP2(self.this, out.this)
        return returnValue

    
    def _CollisionSolid__overloaded_write_ptrConstCollisionSolid_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPHwcatNak(self.this, out.this, indentLevel)
        return returnValue

    
    def _CollisionSolid__overloaded_write_ptrConstCollisionSolid_ptrOstream(self, out):
        returnValue = libpanda._inPHwcaSwM3(self.this, out.this)
        return returnValue

    
    def upcastToBoundedObject(self):
        returnValue = libpanda._inPHwcaztHB(self.this)
        import BoundedObject
        returnObject = BoundedObject.BoundedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpanda._inPflbokcf_(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtnFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt7Xzz(upcastSelf.this, handle.this)
        return returnValue

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtP11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtaS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtwyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtvpj2(upcastSelf.this)
        return returnValue

    
    def _CollisionSolid__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPC76J(upcastSelf.this, type)
        return returnValue

    
    def _CollisionSolid__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPUVRr(upcastSelf.this, volume.this)
        return returnValue

    
    def getBound(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPtOIb(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def markBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPG4uI(upcastSelf.this)
        return returnValue

    
    def forceBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPj1Pw(upcastSelf.this)
        return returnValue

    
    def isBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPkac5(upcastSelf.this)
        return returnValue

    
    def setFinal(self, flag):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPy9vH(upcastSelf.this, flag)
        return returnValue

    
    def isFinal(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPbuL4(upcastSelf.this)
        return returnValue

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._CollisionSolid__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(*_args)
            
            import BoundingVolume
            if isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._CollisionSolid__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CollisionSolid__overloaded_write_ptrConstCollisionSolid_ptrOstream(*_args)
        elif numArgs == 2:
            return self._CollisionSolid__overloaded_write_ptrConstCollisionSolid_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


