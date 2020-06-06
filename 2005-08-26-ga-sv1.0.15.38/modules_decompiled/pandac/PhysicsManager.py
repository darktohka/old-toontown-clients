# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
from direct.ffi import FFIExternalObject

class PhysicsManager(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
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
        returnValue = libpandaphysics._inP9fJJWVm7(self.this, p.this)
        return returnValue

    
    def attachPhysicalnode(self, p):
        returnValue = libpandaphysics._inP9fJJBiJv(self.this, p.this)
        return returnValue

    
    def attachPhysicalNode(self, p):
        returnValue = libpandaphysics._inP9fJJTnRZ(self.this, p.this)
        return returnValue

    
    def addLinearForce(self, f):
        returnValue = libpandaphysics._inP9fJJCQEN(self.this, f.this)
        return returnValue

    
    def addAngularForce(self, f):
        returnValue = libpandaphysics._inP9fJJLLwm(self.this, f.this)
        return returnValue

    
    def clearLinearForces(self):
        returnValue = libpandaphysics._inP9fJJpFDw(self.this)
        return returnValue

    
    def clearAngularForces(self):
        returnValue = libpandaphysics._inP9fJJbGDA(self.this)
        return returnValue

    
    def clearPhysicals(self):
        returnValue = libpandaphysics._inP9fJJL5GU(self.this)
        return returnValue

    
    def setViscosity(self, viscosity):
        returnValue = libpandaphysics._inP9fJJNgcX(self.this, viscosity)
        return returnValue

    
    def getViscosity(self):
        returnValue = libpandaphysics._inP9fJJ_DJO(self.this)
        return returnValue

    
    def removePhysical(self, p):
        returnValue = libpandaphysics._inP9fJJR29e(self.this, p.this)
        return returnValue

    
    def removePhysicalNode(self, p):
        returnValue = libpandaphysics._inP9fJJQym8(self.this, p.this)
        return returnValue

    
    def removeLinearForce(self, f):
        returnValue = libpandaphysics._inP9fJJ_0ov(self.this, f.this)
        return returnValue

    
    def removeAngularForce(self, f):
        returnValue = libpandaphysics._inP9fJJgZkY(self.this, f.this)
        return returnValue

    
    def doPhysics(self, dt):
        returnValue = libpandaphysics._inP9fJJRoJp(self.this, dt)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaphysics._inP9fJJiQi_(self.this, out.this)
        return returnValue

    
    def _PhysicsManager__overloaded_writePhysicals_ptrConstPhysicsManager_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJHsEB(self.this, out.this, indent)
        return returnValue

    
    def _PhysicsManager__overloaded_writePhysicals_ptrConstPhysicsManager_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJGCw4(self.this, out.this)
        return returnValue

    
    def _PhysicsManager__overloaded_writeLinearForces_ptrConstPhysicsManager_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJJKvl(self.this, out.this, indent)
        return returnValue

    
    def _PhysicsManager__overloaded_writeLinearForces_ptrConstPhysicsManager_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJqHRR(self.this, out.this)
        return returnValue

    
    def _PhysicsManager__overloaded_writeAngularForces_ptrConstPhysicsManager_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJAG8W(self.this, out.this, indent)
        return returnValue

    
    def _PhysicsManager__overloaded_writeAngularForces_ptrConstPhysicsManager_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJ_gRG(self.this, out.this)
        return returnValue

    
    def _PhysicsManager__overloaded_write_ptrConstPhysicsManager_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJKfjR(self.this, out.this, indent)
        return returnValue

    
    def _PhysicsManager__overloaded_write_ptrConstPhysicsManager_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJble_(self.this, out.this)
        return returnValue

    
    def _PhysicsManager__overloaded_debugOutput_ptrConstPhysicsManager_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJM4Pj(self.this, out.this, indent)
        return returnValue

    
    def _PhysicsManager__overloaded_debugOutput_ptrConstPhysicsManager_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJ3rbp(self.this, out.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PhysicsManager__overloaded_write_ptrConstPhysicsManager_ptrOstream(*_args)
        elif numArgs == 2:
            return self._PhysicsManager__overloaded_write_ptrConstPhysicsManager_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writeLinearForces(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PhysicsManager__overloaded_writeLinearForces_ptrConstPhysicsManager_ptrOstream(*_args)
        elif numArgs == 2:
            return self._PhysicsManager__overloaded_writeLinearForces_ptrConstPhysicsManager_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writeAngularForces(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PhysicsManager__overloaded_writeAngularForces_ptrConstPhysicsManager_ptrOstream(*_args)
        elif numArgs == 2:
            return self._PhysicsManager__overloaded_writeAngularForces_ptrConstPhysicsManager_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def debugOutput(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PhysicsManager__overloaded_debugOutput_ptrConstPhysicsManager_ptrOstream(*_args)
        elif numArgs == 2:
            return self._PhysicsManager__overloaded_debugOutput_ptrConstPhysicsManager_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writePhysicals(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PhysicsManager__overloaded_writePhysicals_ptrConstPhysicsManager_ptrOstream(*_args)
        elif numArgs == 2:
            return self._PhysicsManager__overloaded_writePhysicals_ptrConstPhysicsManager_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


