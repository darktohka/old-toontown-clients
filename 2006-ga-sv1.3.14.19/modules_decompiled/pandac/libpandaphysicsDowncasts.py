# File: l (Python 2.2)

import types
import libpandaphysics
import BaseParticleEmitter
import ReferenceCount
import BaseParticleFactory
import BaseParticleRenderer

def downcastToBaseParticleEmitterFromReferenceCount(this):
    returnValue = libpandaphysics._inPKBUA_EM5(this.this)
    import BaseParticleEmitter
    returnObject = BaseParticleEmitter.BaseParticleEmitter(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToBaseParticleFactoryFromReferenceCount(this):
    returnValue = libpandaphysics._inPKBUA827J(this.this)
    import BaseParticleFactory
    returnObject = BaseParticleFactory.BaseParticleFactory(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToBaseParticleRendererFromReferenceCount(this):
    returnValue = libpandaphysics._inPKBUAE1d7(this.this)
    import BaseParticleRenderer
    returnObject = BaseParticleRenderer.BaseParticleRenderer(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject

