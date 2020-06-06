# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Physical

class ParticleSystem(Physical.Physical, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ParticleSystem__overloaded_constructor_ptrConstParticleSystem(self, copy):
        self.this = libpandaphysics._inPKBUA07Eu(copy.this)
        self.userManagesMemory = 1

    
    def _ParticleSystem__overloaded_constructor_int(self, poolSize):
        self.this = libpandaphysics._inPKBUA_wz4(poolSize)
        self.userManagesMemory = 1

    
    def _ParticleSystem__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAlHaR()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def setPoolSize(self, size):
        returnValue = libpandaphysics._inPKBUApvqS(self.this, size)
        return returnValue

    
    def setBirthRate(self, newBr):
        returnValue = libpandaphysics._inPKBUABtuQ(self.this, newBr)
        return returnValue

    
    def setLitterSize(self, newLs):
        returnValue = libpandaphysics._inPKBUAURZZ(self.this, newLs)
        return returnValue

    
    def setLitterSpread(self, newLs):
        returnValue = libpandaphysics._inPKBUAHkGy(self.this, newLs)
        return returnValue

    
    def setLocalVelocityFlag(self, lv):
        returnValue = libpandaphysics._inPKBUASAZN(self.this, lv)
        return returnValue

    
    def setSystemGrowsOlderFlag(self, sgo):
        returnValue = libpandaphysics._inPKBUABOU3(self.this, sgo)
        return returnValue

    
    def setSystemLifespan(self, sl):
        returnValue = libpandaphysics._inPKBUA_Iib(self.this, sl)
        return returnValue

    
    def setSystemAge(self, age):
        returnValue = libpandaphysics._inPKBUA4GAU(self.this, age)
        return returnValue

    
    def setActiveSystemFlag(self, a):
        returnValue = libpandaphysics._inPKBUAlTf6(self.this, a)
        return returnValue

    
    def setSpawnOnDeathFlag(self, sod):
        returnValue = libpandaphysics._inPKBUA3lKx(self.this, sod)
        return returnValue

    
    def setSpawnRenderNode(self, node):
        returnValue = libpandaphysics._inPKBUATlYr(self.this, node.this)
        return returnValue

    
    def setTemplateSystemFlag(self, tsf):
        returnValue = libpandaphysics._inPKBUADbaK(self.this, tsf)
        return returnValue

    
    def setRenderParent(self, node):
        returnValue = libpandaphysics._inPKBUAoYFU(self.this, node.this)
        return returnValue

    
    def setRenderer(self, r):
        returnValue = libpandaphysics._inPKBUA_bAc(self.this, r.this)
        return returnValue

    
    def setEmitter(self, e):
        returnValue = libpandaphysics._inPKBUAP6z6(self.this, e.this)
        return returnValue

    
    def setFactory(self, f):
        returnValue = libpandaphysics._inPKBUAa_iU(self.this, f.this)
        return returnValue

    
    def setFloorZ(self, z):
        returnValue = libpandaphysics._inPKBUA7S5e(self.this, z)
        return returnValue

    
    def clearFloorZ(self):
        returnValue = libpandaphysics._inPKBUA1_VC(self.this)
        return returnValue

    
    def getPoolSize(self):
        returnValue = libpandaphysics._inPKBUAXT57(self.this)
        return returnValue

    
    def getBirthRate(self):
        returnValue = libpandaphysics._inPKBUAq_T_(self.this)
        return returnValue

    
    def getLitterSize(self):
        returnValue = libpandaphysics._inPKBUAY2Tr(self.this)
        return returnValue

    
    def getLitterSpread(self):
        returnValue = libpandaphysics._inPKBUA31vh(self.this)
        return returnValue

    
    def getLocalVelocityFlag(self):
        returnValue = libpandaphysics._inPKBUAvd6d(self.this)
        return returnValue

    
    def getSystemGrowsOlderFlag(self):
        returnValue = libpandaphysics._inPKBUAmbbN(self.this)
        return returnValue

    
    def getSystemLifespan(self):
        returnValue = libpandaphysics._inPKBUAPFTz(self.this)
        return returnValue

    
    def getSystemAge(self):
        returnValue = libpandaphysics._inPKBUASLlC(self.this)
        return returnValue

    
    def getActiveSystemFlag(self):
        returnValue = libpandaphysics._inPKBUA7pRo(self.this)
        return returnValue

    
    def getSpawnOnDeathFlag(self):
        returnValue = libpandaphysics._inPKBUAysrB(self.this)
        return returnValue

    
    def getSpawnRenderNode(self):
        returnValue = libpandaphysics._inPKBUA3D5l(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getIWasSpawnedFlag(self):
        returnValue = libpandaphysics._inPKBUA4RPW(self.this)
        return returnValue

    
    def getLivingParticles(self):
        returnValue = libpandaphysics._inPKBUAAtRp(self.this)
        return returnValue

    
    def getRenderParent(self):
        returnValue = libpandaphysics._inPKBUAQX9q(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getRenderer(self):
        returnValue = libpandaphysics._inPKBUAWWmZ(self.this)
        import BaseParticleRenderer
        returnObject = BaseParticleRenderer.BaseParticleRenderer(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getEmitter(self):
        returnValue = libpandaphysics._inPKBUAgwSc(self.this)
        import BaseParticleEmitter
        returnObject = BaseParticleEmitter.BaseParticleEmitter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getFactory(self):
        returnValue = libpandaphysics._inPKBUAW2Vl(self.this)
        import BaseParticleFactory
        returnObject = BaseParticleFactory.BaseParticleFactory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getFloorZ(self):
        returnValue = libpandaphysics._inPKBUAw7_3(self.this)
        return returnValue

    
    def addSpawnTemplate(self, ps):
        returnValue = libpandaphysics._inPKBUAL_37(self.this, ps.this)
        return returnValue

    
    def clearSpawnTemplates(self):
        returnValue = libpandaphysics._inPKBUAf6XZ(self.this)
        return returnValue

    
    def render(self):
        returnValue = libpandaphysics._inPKBUAzbqe(self.this)
        return returnValue

    
    def induceLabor(self):
        returnValue = libpandaphysics._inPKBUA3z9v(self.this)
        return returnValue

    
    def update(self, dt):
        returnValue = libpandaphysics._inPKBUA2i2m(self.this, dt)
        return returnValue

    
    def _ParticleSystem__overloaded_writeFreeParticleFifo_ptrConstParticleSystem_ptrOstream_int(self, out, indent):
        returnValue = libpandaphysics._inPKBUA_rSe(self.this, out.this, indent)
        return returnValue

    
    def _ParticleSystem__overloaded_writeFreeParticleFifo_ptrConstParticleSystem_ptrOstream(self, out):
        returnValue = libpandaphysics._inPKBUA0ytn(self.this, out.this)
        return returnValue

    
    def _ParticleSystem__overloaded_writeSpawnTemplates_ptrConstParticleSystem_ptrOstream_int(self, out, indent):
        returnValue = libpandaphysics._inPKBUAgE38(self.this, out.this, indent)
        return returnValue

    
    def _ParticleSystem__overloaded_writeSpawnTemplates_ptrConstParticleSystem_ptrOstream(self, out):
        returnValue = libpandaphysics._inPKBUApNQ_(self.this, out.this)
        return returnValue

    
    def _ParticleSystem__overloaded_write_ptrConstParticleSystem_ptrOstream_int(self, out, indent):
        returnValue = libpandaphysics._inPKBUALxhQ(self.this, out.this, indent)
        return returnValue

    
    def _ParticleSystem__overloaded_write_ptrConstParticleSystem_ptrOstream(self, out):
        returnValue = libpandaphysics._inPKBUAY_Tj(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ParticleSystem__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._ParticleSystem__overloaded_constructor_int(*_args)
            
            if isinstance(_args[0], ParticleSystem):
                return self._ParticleSystem__overloaded_constructor_ptrConstParticleSystem(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <ParticleSystem> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ParticleSystem__overloaded_write_ptrConstParticleSystem_ptrOstream(*_args)
        elif numArgs == 2:
            return self._ParticleSystem__overloaded_write_ptrConstParticleSystem_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writeFreeParticleFifo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ParticleSystem__overloaded_writeFreeParticleFifo_ptrConstParticleSystem_ptrOstream(*_args)
        elif numArgs == 2:
            return self._ParticleSystem__overloaded_writeFreeParticleFifo_ptrConstParticleSystem_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writeSpawnTemplates(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ParticleSystem__overloaded_writeSpawnTemplates_ptrConstParticleSystem_ptrOstream(*_args)
        elif numArgs == 2:
            return self._ParticleSystem__overloaded_writeSpawnTemplates_ptrConstParticleSystem_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


