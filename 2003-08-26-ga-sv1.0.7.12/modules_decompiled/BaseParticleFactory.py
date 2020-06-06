# File: B (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount

class BaseParticleFactory(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
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
        if libpandaphysics and libpandaphysics._inPKBUATTlV:
            libpandaphysics._inPKBUATTlV(self.this)
        

    
    def setLifespanBase(self, lb):
        returnValue = libpandaphysics._inPKBUAiQuU(self.this, lb)
        return returnValue

    
    def setLifespanSpread(self, ls):
        returnValue = libpandaphysics._inPKBUAdQHH(self.this, ls)
        return returnValue

    
    def setMassBase(self, mb):
        returnValue = libpandaphysics._inPKBUAYu3l(self.this, mb)
        return returnValue

    
    def setMassSpread(self, ms):
        returnValue = libpandaphysics._inPKBUANeQM(self.this, ms)
        return returnValue

    
    def setTerminalVelocityBase(self, tvb):
        returnValue = libpandaphysics._inPKBUAWNEZ(self.this, tvb)
        return returnValue

    
    def setTerminalVelocitySpread(self, tvs):
        returnValue = libpandaphysics._inPKBUAANWX(self.this, tvs)
        return returnValue

    
    def getLifespanBase(self):
        returnValue = libpandaphysics._inPKBUAigu1(self.this)
        return returnValue

    
    def getLifespanSpread(self):
        returnValue = libpandaphysics._inPKBUA_9k2(self.this)
        return returnValue

    
    def getMassBase(self):
        returnValue = libpandaphysics._inPKBUA2EQT(self.this)
        return returnValue

    
    def getMassSpread(self):
        returnValue = libpandaphysics._inPKBUA_lih(self.this)
        return returnValue

    
    def getTerminalVelocityBase(self):
        returnValue = libpandaphysics._inPKBUACoqe(self.this)
        return returnValue

    
    def getTerminalVelocitySpread(self):
        returnValue = libpandaphysics._inPKBUAl_x2(self.this)
        return returnValue

    
    def allocParticle(self):
        returnValue = libpandaphysics._inPKBUAsnkF(self.this)
        import BaseParticle
        returnObject = BaseParticle.BaseParticle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def populateParticle(self, bp):
        returnValue = libpandaphysics._inPKBUAxNK_(self.this, bp.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaphysics._inPKBUANcSl(self.this, out.this)
        return returnValue

    
    def _BaseParticleFactory__overloaded_write_ptrConstBaseParticleFactory_ptrOstream_int(self, out, indent):
        returnValue = libpandaphysics._inPKBUAtDsB(self.this, out.this, indent)
        return returnValue

    
    def _BaseParticleFactory__overloaded_write_ptrConstBaseParticleFactory_ptrOstream(self, out):
        returnValue = libpandaphysics._inPKBUAEUOn(self.this, out.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._BaseParticleFactory__overloaded_write_ptrConstBaseParticleFactory_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._BaseParticleFactory__overloaded_write_ptrConstBaseParticleFactory_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


