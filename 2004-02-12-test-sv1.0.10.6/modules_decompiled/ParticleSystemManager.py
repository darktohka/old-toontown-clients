# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import FFIExternalObject

class ParticleSystemManager(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _ParticleSystemManager__overloaded_constructor_int(self, everyNthFrame):
        self.this = libpandaphysics._inPKBUAuOfO(everyNthFrame)
        self.userManagesMemory = 1

    
    def _ParticleSystemManager__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAKxoE()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAqqmp:
            libpandaphysics._inPKBUAqqmp(self.this)
        

    
    def setFrameStepping(self, everyNthFrame):
        returnValue = libpandaphysics._inPKBUAhIpF(self.this, everyNthFrame)
        return returnValue

    
    def getFrameStepping(self):
        returnValue = libpandaphysics._inPKBUA3diP(self.this)
        return returnValue

    
    def attachParticlesystem(self, ps):
        returnValue = libpandaphysics._inPKBUAnDR9(self.this, ps.this)
        return returnValue

    
    def removeParticlesystem(self, ps):
        returnValue = libpandaphysics._inPKBUAstvE(self.this, ps.this)
        return returnValue

    
    def clear(self):
        returnValue = libpandaphysics._inPKBUAUEnv(self.this)
        return returnValue

    
    def doParticles(self, dt):
        returnValue = libpandaphysics._inPKBUAnA7I(self.this, dt)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaphysics._inPKBUApHBj(self.this, out.this)
        return returnValue

    
    def _ParticleSystemManager__overloaded_writePsList_ptrConstParticleSystemManager_ptrOstream_int(self, out, indent):
        returnValue = libpandaphysics._inPKBUAaVHd(self.this, out.this, indent)
        return returnValue

    
    def _ParticleSystemManager__overloaded_writePsList_ptrConstParticleSystemManager_ptrOstream(self, out):
        returnValue = libpandaphysics._inPKBUA3VNz(self.this, out.this)
        return returnValue

    
    def _ParticleSystemManager__overloaded_write_ptrConstParticleSystemManager_ptrOstream_int(self, out, indent):
        returnValue = libpandaphysics._inPKBUAhS_E(self.this, out.this, indent)
        return returnValue

    
    def _ParticleSystemManager__overloaded_write_ptrConstParticleSystemManager_ptrOstream(self, out):
        returnValue = libpandaphysics._inPKBUA85AY(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ParticleSystemManager__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._ParticleSystemManager__overloaded_constructor_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._ParticleSystemManager__overloaded_write_ptrConstParticleSystemManager_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._ParticleSystemManager__overloaded_write_ptrConstParticleSystemManager_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writePsList(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._ParticleSystemManager__overloaded_writePsList_ptrConstParticleSystemManager_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._ParticleSystemManager__overloaded_writePsList_ptrConstParticleSystemManager_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


