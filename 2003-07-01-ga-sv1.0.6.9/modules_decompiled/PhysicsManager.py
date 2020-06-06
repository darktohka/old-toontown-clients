# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import FFIExternalObject

class PhysicsManager(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpandaphysics._inP9fJJPQAe()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inP9fJJjT2P:
            libpandaphysics._inP9fJJjT2P(self.this)
        

    
    def attachLinearIntegrator(self, i):
        returnValue = libpandaphysics._inP9fJJ42XZ(self.this, i.this)
        return returnValue

    
    def attachAngularIntegrator(self, i):
        returnValue = libpandaphysics._inP9fJJwg3X(self.this, i.this)
        return returnValue

    
    def attachPhysical(self, p):
        returnValue = libpandaphysics._inP9fJJXVm7(self.this, p.this)
        return returnValue

    
    def attachPhysicalnode(self, p):
        returnValue = libpandaphysics._inP9fJJAiJv(self.this, p.this)
        return returnValue

    
    def addLinearForce(self, f):
        returnValue = libpandaphysics._inP9fJJCQEN(self.this, f.this)
        return returnValue

    
    def addAngularForce(self, f):
        returnValue = libpandaphysics._inP9fJJILwm(self.this, f.this)
        return returnValue

    
    def clearLinearForces(self):
        returnValue = libpandaphysics._inP9fJJuFDw(self.this)
        return returnValue

    
    def clearAngularForces(self):
        returnValue = libpandaphysics._inP9fJJbGDA(self.this)
        return returnValue

    
    def clearPhysicals(self):
        returnValue = libpandaphysics._inP9fJJL5GU(self.this)
        return returnValue

    
    def removePhysical(self, p):
        returnValue = libpandaphysics._inP9fJJR29e(self.this, p.this)
        return returnValue

    
    def removeLinearForce(self, f):
        returnValue = libpandaphysics._inP9fJJ_0ov(self.this, f.this)
        return returnValue

    
    def removeAngularForce(self, f):
        returnValue = libpandaphysics._inP9fJJgZkY(self.this, f.this)
        return returnValue

    
    def doPhysics(self, dt):
        returnValue = libpandaphysics._inP9fJJWoJp(self.this, dt)
        return returnValue


