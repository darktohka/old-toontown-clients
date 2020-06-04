# File: l (Python 2.2)

import types
import libpanda
import ImageBuffer
import ReferenceCount
import WritableConfigurable
import Namable
import TypedWritableReferenceCount
import PandaNode
import BoundedObject
import TextFont
import TextNode
import TextEncoder
import TextProperties
import MouseWatcherRegion
import GraphicsOutput
import DrawableRegion
import DisplayRegion
import MouseWatcher
import MouseWatcherGroup
import PGMouseWatcherParameter
import MouseWatcherParameter
import DynamicTextFont
import FreetypeFont
import DDrawable
import NurbsCurve
import NurbsCurveInterface
import CollisionSolid
import AnimGroup
import PartBundle
import AnimControlCollection
import PartGroup
import LightNode
import LightLensNode
import LensNode
import MouseRecorder
import RecorderBase

def downcastToImageBufferFromReferenceCount(this):
    returnValue = libpanda._inPMAKPDiCH(this.this)
    import ImageBuffer
    returnObject = ImageBuffer.ImageBuffer(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToImageBufferFromWritableConfigurable(this):
    returnValue = libpanda._inPMAKP4XnT(this.this)
    import ImageBuffer
    returnObject = ImageBuffer.ImageBuffer(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToImageBufferFromNamable(this):
    returnValue = libpanda._inPMAKPjT5f(this.this)
    import ImageBuffer
    returnObject = ImageBuffer.ImageBuffer(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToTypedWritableReferenceCountFromReferenceCount(this):
    returnValue = libpanda._inPflboGHue(this.this)
    import TypedWritableReferenceCount
    returnObject = TypedWritableReferenceCount.TypedWritableReferenceCount(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToPandaNodeFromNamable(this):
    returnValue = libpanda._inPnJyoPzAU(this.this)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToPandaNodeFromBoundedObject(this):
    returnValue = libpanda._inPnJyo9jJK(this.this)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToTextFontFromNamable(this):
    returnValue = libpanda._inPpUk_5Y1p(this.this)
    import TextFont
    returnObject = TextFont.TextFont(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToTextNodeFromTextEncoder(this):
    returnValue = libpanda._inPpUk_tPjp(this.this)
    import TextNode
    returnObject = TextNode.TextNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToTextNodeFromTextProperties(this):
    returnValue = libpanda._inPpUk_zq3d(this.this)
    import TextNode
    returnObject = TextNode.TextNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToMouseWatcherRegionFromNamable(this):
    returnValue = libpanda._inPyiw57Z9h(this.this)
    import MouseWatcherRegion
    returnObject = MouseWatcherRegion.MouseWatcherRegion(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToGraphicsOutputFromDrawableRegion(this):
    returnValue = libpanda._inPO9cYuJDd(this.this)
    import GraphicsOutput
    returnObject = GraphicsOutput.GraphicsOutput(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToDisplayRegionFromDrawableRegion(this):
    returnValue = libpanda._inPO9cYWozv(this.this)
    import DisplayRegion
    returnObject = DisplayRegion.DisplayRegion(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToMouseWatcherFromMouseWatcherGroup(this):
    returnValue = libpanda._inPyiw5k8r2(this.this)
    import MouseWatcher
    returnObject = MouseWatcher.MouseWatcher(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToPGMouseWatcherParameterFromMouseWatcherParameter(this):
    returnValue = libpanda._inPVvimmaZS(this.this)
    import PGMouseWatcherParameter
    returnObject = PGMouseWatcherParameter.PGMouseWatcherParameter(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToDynamicTextFontFromFreetypeFont(this):
    returnValue = libpanda._inPpUk_HtRh(this.this)
    import DynamicTextFont
    returnObject = DynamicTextFont.DynamicTextFont(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToDDrawableFromReferenceCount(this):
    returnValue = libpanda._inPMAKP_2h2(this.this)
    import DDrawable
    returnObject = DDrawable.DDrawable(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToDDrawableFromWritableConfigurable(this):
    returnValue = libpanda._inPMAKPruev(this.this)
    import DDrawable
    returnObject = DDrawable.DDrawable(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToDDrawableFromBoundedObject(this):
    returnValue = libpanda._inPMAKP_tIx(this.this)
    import DDrawable
    returnObject = DDrawable.DDrawable(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToNurbsCurveFromNurbsCurveInterface(this):
    returnValue = libpanda._inPHc9WQN7l(this.this)
    import NurbsCurve
    returnObject = NurbsCurve.NurbsCurve(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToCollisionSolidFromBoundedObject(this):
    returnValue = libpanda._inPHwcaTioU(this.this)
    import CollisionSolid
    returnObject = CollisionSolid.CollisionSolid(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToAnimGroupFromNamable(this):
    returnValue = libpanda._inPn9gM4p9k(this.this)
    import AnimGroup
    returnObject = AnimGroup.AnimGroup(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToPartBundleFromAnimControlCollection(this):
    returnValue = libpanda._inPn9gMaJ3p(this.this)
    import PartBundle
    returnObject = PartBundle.PartBundle(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToPartGroupFromNamable(this):
    returnValue = libpanda._inPn9gMoV3X(this.this)
    import PartGroup
    returnObject = PartGroup.PartGroup(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToLightNodeFromPandaNode(this):
    returnValue = libpanda._inPnJyowkdW(this.this)
    import LightNode
    returnObject = LightNode.LightNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToLightLensNodeFromLensNode(this):
    returnValue = libpanda._inPnJyos_CG(this.this)
    import LightLensNode
    returnObject = LightLensNode.LightLensNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToMouseRecorderFromRecorderBase(this):
    returnValue = libpanda._inPc5FLAqBt(this.this)
    import MouseRecorder
    returnObject = MouseRecorder.MouseRecorder(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject

