# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionHandlerPhysical

class CollisionHandlerGravity(CollisionHandlerPhysical.CollisionHandlerPhysical, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPHwcay_jT()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcac4lv:
            libpanda._inPHwcac4lv(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaJ2aU()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setOffset(self, offset):
        returnValue = libpanda._inPHwca5C9R(self.this, offset)
        return returnValue

    
    def getOffset(self):
        returnValue = libpanda._inPHwcau78c(self.this)
        return returnValue

    
    def setReach(self, reach):
        returnValue = libpanda._inPHwcaV1C6(self.this, reach)
        return returnValue

    
    def getReach(self):
        returnValue = libpanda._inPHwca22RV(self.this)
        return returnValue

    
    def getAirborneHeight(self):
        returnValue = libpanda._inPHwcalkVy(self.this)
        return returnValue

    
    def isOnGround(self):
        returnValue = libpanda._inPHwcaI07o(self.this)
        return returnValue

    
    def getImpactVelocity(self):
        returnValue = libpanda._inPHwcabFxY(self.this)
        return returnValue

    
    def getContactNormal(self):
        returnValue = libpanda._inPHwcaKQo4(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def addVelocity(self, velocity):
        returnValue = libpanda._inPHwcawddg(self.this, velocity)
        return returnValue

    
    def setVelocity(self, velocity):
        returnValue = libpanda._inPHwcaXI_M(self.this, velocity)
        return returnValue

    
    def getVelocity(self):
        returnValue = libpanda._inPHwcarnWU(self.this)
        return returnValue

    
    def setGravity(self, gravity):
        returnValue = libpanda._inPHwcamWBh(self.this, gravity)
        return returnValue

    
    def getGravity(self):
        returnValue = libpanda._inPHwcamZKk(self.this)
        return returnValue

    
    def setMaxVelocity(self, maxVel):
        returnValue = libpanda._inPHwcakg9z(self.this, maxVel)
        return returnValue

    
    def getMaxVelocity(self):
        returnValue = libpanda._inPHwcalxjB(self.this)
        return returnValue


