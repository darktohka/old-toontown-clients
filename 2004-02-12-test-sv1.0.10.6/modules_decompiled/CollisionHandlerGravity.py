# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionHandlerPhysical

class CollisionHandlerGravity(CollisionHandlerPhysical.CollisionHandlerPhysical, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPHwcay_jT()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaT4lv:
            libpanda._inPHwcaT4lv(self.this)
        

    
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

    
    def getAirborneHeight(self):
        returnValue = libpanda._inPHwcakkVy(self.this)
        return returnValue

    
    def isOnGround(self):
        returnValue = libpanda._inPHwcaL07o(self.this)
        return returnValue

    
    def isInOuterSpace(self):
        returnValue = libpanda._inPHwcaPiDH(self.this)
        return returnValue

    
    def getImpactVelocity(self):
        returnValue = libpanda._inPHwcabFxY(self.this)
        return returnValue

    
    def addVelocity(self, velocity):
        returnValue = libpanda._inPHwcazddg(self.this, velocity)
        return returnValue

    
    def setVelocity(self, velocity):
        returnValue = libpanda._inPHwcaXI_M(self.this, velocity)
        return returnValue

    
    def getVelocity(self):
        returnValue = libpanda._inPHwcarnWU(self.this)
        return returnValue

    
    def setGravity(self, gravity):
        returnValue = libpanda._inPHwca5WBh(self.this, gravity)
        return returnValue

    
    def getGravity(self):
        returnValue = libpanda._inPHwcapZKk(self.this)
        return returnValue

    
    def setMaxVelocity(self, maxVel):
        returnValue = libpanda._inPHwcang9z(self.this, maxVel)
        return returnValue

    
    def getMaxVelocity(self):
        returnValue = libpanda._inPHwcalxjB(self.this)
        return returnValue


