# File: l (Python 2.2)

import types
import libpandaegg
import EggNamedObject
import Namable
import EggGroup
import EggRenderMode
import EggTransform3d
import EggTexture
import EggPrimitive
import EggAttributes
import EggVertex

def downcastToEggNamedObjectFromNamable(this):
    returnValue = libpandaegg._inPkAOM__2j(this.this)
    import EggNamedObject
    returnObject = EggNamedObject.EggNamedObject(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToEggGroupFromEggRenderMode(this):
    returnValue = libpandaegg._inPkAOMj6hd(this.this)
    import EggGroup
    returnObject = EggGroup.EggGroup(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToEggGroupFromEggTransform3d(this):
    returnValue = libpandaegg._inPkAOM3Uh0(this.this)
    import EggGroup
    returnObject = EggGroup.EggGroup(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToEggTextureFromEggRenderMode(this):
    returnValue = libpandaegg._inPkAOM5AMp(this.this)
    import EggTexture
    returnObject = EggTexture.EggTexture(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToEggPrimitiveFromEggAttributes(this):
    returnValue = libpandaegg._inPkAOMcB04(this.this)
    import EggPrimitive
    returnObject = EggPrimitive.EggPrimitive(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToEggPrimitiveFromEggRenderMode(this):
    returnValue = libpandaegg._inPkAOMZds5(this.this)
    import EggPrimitive
    returnObject = EggPrimitive.EggPrimitive(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToEggVertexFromEggAttributes(this):
    returnValue = libpandaegg._inPkAOMTrUk(this.this)
    import EggVertex
    returnObject = EggVertex.EggVertex(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject

