# File: B (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAg60H:
            libpandaphysics._inPKBUAg60H(self.this)
        

    
    def makeCopy(self):
        returnValue = libpandaphysics._inPKBUAr9K2(self.this)
        returnObject = BaseParticleEmitter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def generate(self, pos, vel):
        returnValue = libpandaphysics._inPKBUAXvUs(self.this, pos.this, vel.this)
        return returnValue

    
    def setEmissionType(self, et):
        returnValue = libpandaphysics._inPKBUAvAPb(self.this, et)
        return returnValue

    
    def setAmplitude(self, a):
        returnValue = libpandaphysics._inPKBUA014P(self.this, a)
        return returnValue

    
    def setAmplitudeSpread(self, as):
        returnValue = libpandaphysics._inPKBUAHfat(self.this, as)
        return returnValue

    
    def setOffsetForce(self, of):
        returnValue = libpandaphysics._inPKBUAJolc(self.this, of.this)
        return returnValue

    
    def setExplicitLaunchVector(self, elv):
        returnValue = libpandaphysics._inPKBUA7_f_(self.this, elv.this)
        return returnValue

    
    def setRadiateOrigin(self, ro):
        returnValue = libpandaphysics._inPKBUAegGF(self.this, ro.this)
        return returnValue

    
    def getEmissionType(self):
        returnValue = libpandaphysics._inPKBUA_Hj6(self.this)
        return returnValue

    
    def getAmplitude(self):
        returnValue = libpandaphysics._inPKBUAzJT9(self.this)
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
        returnValue = libpandaphysics._inPKBUATHW0(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRadiateOrigin(self):
        returnValue = libpandaphysics._inPKBUAuPd8(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject


