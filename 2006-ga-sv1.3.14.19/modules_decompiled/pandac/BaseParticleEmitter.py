# File: B (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ReferenceCount

class BaseParticleEmitter(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    ETCUSTOM = 2
    ETEXPLICIT = 0
    ETRADIATE = 1
    
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
        if libpandaphysics and libpandaphysics._inPKBUAg60H:
            libpandaphysics._inPKBUAg60H(self.this)
        

    
    def makeCopy(self):
        returnValue = libpandaphysics._inPKBUAq9K2(self.this)
        returnObject = BaseParticleEmitter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def generate(self, pos, vel):
        returnValue = libpandaphysics._inPKBUAQvUs(self.this, pos.this, vel.this)
        return returnValue

    
    def setEmissionType(self, et):
        returnValue = libpandaphysics._inPKBUAvAPb(self.this, et)
        return returnValue

    
    def setAmplitude(self, a):
        returnValue = libpandaphysics._inPKBUA014P(self.this, a)
        return returnValue

    
    def setAmplitudeSpread(self, as):
        returnValue = libpandaphysics._inPKBUAGfat(self.this, as)
        return returnValue

    
    def setOffsetForce(self, of):
        returnValue = libpandaphysics._inPKBUAJolc(self.this, of.this)
        return returnValue

    
    def setExplicitLaunchVector(self, elv):
        returnValue = libpandaphysics._inPKBUA4_f_(self.this, elv.this)
        return returnValue

    
    def setRadiateOrigin(self, ro):
        returnValue = libpandaphysics._inPKBUAegGF(self.this, ro.this)
        return returnValue

    
    def getEmissionType(self):
        returnValue = libpandaphysics._inPKBUA_Hj6(self.this)
        return returnValue

    
    def getAmplitude(self):
        returnValue = libpandaphysics._inPKBUAyJT9(self.this)
        return returnValue

    
    def getAmplitudeSpread(self):
        returnValue = libpandaphysics._inPKBUA_DLN(self.this)
        return returnValue

    
    def getOffsetForce(self):
        returnValue = libpandaphysics._inPKBUAgc7B(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getExplicitLaunchVector(self):
        returnValue = libpandaphysics._inPKBUASHW0(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRadiateOrigin(self):
        returnValue = libpandaphysics._inPKBUAvPd8(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libpandaphysics._inPKBUAKdyZ(self.this, out.this)
        return returnValue

    
    def _BaseParticleEmitter__overloaded_write_ptrConstBaseParticleEmitter_ptrOstream_int(self, out, indent):
        returnValue = libpandaphysics._inPKBUAkUM2(self.this, out.this, indent)
        return returnValue

    
    def _BaseParticleEmitter__overloaded_write_ptrConstBaseParticleEmitter_ptrOstream(self, out):
        returnValue = libpandaphysics._inPKBUAWxub(self.this, out.this)
        return returnValue

    
    def upcastToReferenceCount(self):
        returnValue = libpandaphysics._inPKBUAtTF9(self.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
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

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._BaseParticleEmitter__overloaded_write_ptrConstBaseParticleEmitter_ptrOstream(*_args)
        elif numArgs == 2:
            return self._BaseParticleEmitter__overloaded_write_ptrConstBaseParticleEmitter_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


