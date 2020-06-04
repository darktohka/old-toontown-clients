# File: N (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Nametag
import PandaNode

class Nametag3d(Nametag.Nametag, PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts,
        libpandaDowncasts]
    
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
        if libtoontown and libtoontown._inPPj7b4h7N:
            libtoontown._inPPj7b4h7N(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPPj7bnUgM()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setBillboardOffset(self, billboardOffset):
        returnValue = libtoontown._inPPj7bL3Hg(self.this, billboardOffset)
        return returnValue

    
    def getBillboardOffset(self):
        returnValue = libtoontown._inPPj7bX7Do(self.this)
        return returnValue

    
    def upcastToPandaNode(self):
        returnValue = libtoontown._inPPj7bQj3s(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setContents(self, flags):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bLEaT(upcastSelf.this, flags)
        return returnValue

    
    def getContents(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bJEgG(upcastSelf.this)
        return returnValue

    
    def setActive(self, active):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bSryD(upcastSelf.this, active)
        return returnValue

    
    def isActive(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7brM1i(upcastSelf.this)
        return returnValue

    
    def displayAsActive(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bLRcp(upcastSelf.this)
        return returnValue

    
    def hasGroup(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bTIee(upcastSelf.this)
        return returnValue

    
    def getGroup(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bajNp(upcastSelf.this)
        import NametagGroup
        returnObject = NametagGroup.NametagGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setDrawOrder(self, drawOrder):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bhTHf(upcastSelf.this, drawOrder)
        return returnValue

    
    def clearDrawOrder(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7b5yp7(upcastSelf.this)
        return returnValue

    
    def setChatWordwrap(self, wordwrap):
        upcastSelf = self
        returnValue = libtoontown._inPPj7b980k(upcastSelf.this, wordwrap)
        return returnValue

    
    def getChatWordwrap(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bidZX(upcastSelf.this)
        return returnValue

    
    def setAvatar(self, node):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bdwUo(upcastSelf.this, node.this)
        return returnValue

    
    def clearAvatar(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bkVEl(upcastSelf.this)
        return returnValue

    
    def getAvatar(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bA2vB(upcastSelf.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bSdXg(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7bngq5(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToClickablePopup(self):
        upcastSelf = self
        returnValue = libtoontown._inPPj7buut_(upcastSelf.this)
        import ClickablePopup
        returnObject = ClickablePopup.ClickablePopup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtM11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtVS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtzyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtupj2(upcastSelf.this)
        return returnValue

    
    def copySubgraph(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoGYnx(upcastSelf.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumParents(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoI9bH(upcastSelf.this)
        return returnValue

    
    def getParent(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoh0xF(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findParent(self, node):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoNWG_(upcastSelf.this, node.this)
        return returnValue

    
    def getNumChildren(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo68Bo(upcastSelf.this)
        return returnValue

    
    def getChild(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyonZg9(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getChildSort(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoMzeG(upcastSelf.this, n)
        return returnValue

    
    def findChild(self, node):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoKHuN(upcastSelf.this, node.this)
        return returnValue

    
    def _Nametag3d__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoA9tQ(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _Nametag3d__overloaded_addChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo37ri(upcastSelf.this, childNode.this)
        return returnValue

    
    def _Nametag3d__overloaded_removeChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyozFZb(upcastSelf.this, childNode.this)
        return returnValue

    
    def _Nametag3d__overloaded_removeChild_ptrPandaNode_int(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoCqN1(upcastSelf.this, n)
        return returnValue

    
    def replaceChild(self, origChild, newChild):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyogW5Y(upcastSelf.this, origChild.this, newChild.this)
        return returnValue

    
    def _Nametag3d__overloaded_stashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyokC1w(upcastSelf.this, childNode.this)
        return returnValue

    
    def _Nametag3d__overloaded_stashChild_ptrPandaNode_int(self, childIndex):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoqWqz(upcastSelf.this, childIndex)
        return returnValue

    
    def _Nametag3d__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoqJGM(upcastSelf.this, childNode.this)
        return returnValue

    
    def _Nametag3d__overloaded_unstashChild_ptrPandaNode_int(self, stashedIndex):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoeWxF(upcastSelf.this, stashedIndex)
        return returnValue

    
    def getNumStashed(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoPR8_(upcastSelf.this)
        return returnValue

    
    def getStashed(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyol8qw(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getStashedSort(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoE1FX(upcastSelf.this, n)
        return returnValue

    
    def findStashed(self, node):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoyw9C(upcastSelf.this, node.this)
        return returnValue

    
    def _Nametag3d__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoQQ0n(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _Nametag3d__overloaded_addStashed_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoswLI(upcastSelf.this, childNode.this)
        return returnValue

    
    def removeStashed(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoYHe7(upcastSelf.this, n)
        return returnValue

    
    def removeAllChildren(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoayap(upcastSelf.this)
        return returnValue

    
    def stealChildren(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoignr(upcastSelf.this, other.this)
        return returnValue

    
    def copyChildren(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyohfED(upcastSelf.this, other.this)
        return returnValue

    
    def _Nametag3d__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(self, attrib, override):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo48Bd(upcastSelf.this, attrib.this, override)
        return returnValue

    
    def _Nametag3d__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(self, attrib):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoAD5k(upcastSelf.this, attrib.this)
        return returnValue

    
    def getAttrib(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoaDfJ(upcastSelf.this, type.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasAttrib(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo2W_P(upcastSelf.this, type.this)
        return returnValue

    
    def clearAttrib(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoCSEu(upcastSelf.this, type.this)
        return returnValue

    
    def setEffect(self, effect):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoKWvI(upcastSelf.this, effect.this)
        return returnValue

    
    def getEffect(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo17Hl(upcastSelf.this, type.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasEffect(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoJ1nr(upcastSelf.this, type.this)
        return returnValue

    
    def clearEffect(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoOUJ2(upcastSelf.this, type.this)
        return returnValue

    
    def setState(self, state):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoGDjV(upcastSelf.this, state.this)
        return returnValue

    
    def getState(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoIocj(upcastSelf.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearState(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyotySF(upcastSelf.this)
        return returnValue

    
    def setEffects(self, effects):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo2lpj(upcastSelf.this, effects.this)
        return returnValue

    
    def getEffects(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo1WLf(upcastSelf.this)
        import RenderEffects
        returnObject = RenderEffects.RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearEffects(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo6yPH(upcastSelf.this)
        return returnValue

    
    def setTransform(self, transform):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo_5Ti(upcastSelf.this, transform.this)
        return returnValue

    
    def getTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo1dH2(upcastSelf.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoHjK_(upcastSelf.this)
        return returnValue

    
    def setPrevTransform(self, transform):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo_3nJ(upcastSelf.this, transform.this)
        return returnValue

    
    def getPrevTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyor3cO(upcastSelf.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def resetPrevTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoGfcO(upcastSelf.this)
        return returnValue

    
    def setTag(self, key, value):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoTNEJ(upcastSelf.this, key, value)
        return returnValue

    
    def getTag(self, key):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo6tVl(upcastSelf.this, key)
        return returnValue

    
    def hasTag(self, key):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoue2r(upcastSelf.this, key)
        return returnValue

    
    def clearTag(self, key):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoiRPE(upcastSelf.this, key)
        return returnValue

    
    def copyTags(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoyMQi(upcastSelf.this, other.this)
        return returnValue

    
    def _Nametag3d__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(self, out, separator):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo2itg(upcastSelf.this, out.this, separator)
        return returnValue

    
    def _Nametag3d__overloaded_listTags_ptrConstPandaNode_ptrOstream(self, out):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyocRES(upcastSelf.this, out.this)
        return returnValue

    
    def setDrawMask(self, mask):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoezL6(upcastSelf.this, mask.this)
        return returnValue

    
    def getDrawMask(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoWJXI(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNetCollideMask(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo4l_T(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoW23T(upcastSelf.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoSz8K(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def ls(self, out, indentLevel):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyouBSg(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def _Nametag3d__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyond5g(upcastSelf.this, type)
        return returnValue

    
    def _Nametag3d__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo7Bq1(upcastSelf.this, volume.this)
        return returnValue

    
    def getBound(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyohf0y(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getInternalBound(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoI_J4(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def isGeomNode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoyAx3(upcastSelf.this)
        return returnValue

    
    def asLight(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyoaCbs(upcastSelf.this)
        import Light
        returnObject = Light.Light(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import BoundingVolume
            if isinstance(_args[0], types.IntType):
                return self._Nametag3d__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(_args[0])
            elif isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._Nametag3d__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._Nametag3d__overloaded_addChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        elif numArgs == 2:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._Nametag3d__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def unstashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self._Nametag3d__overloaded_unstashChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._Nametag3d__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def listTags(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Nametag3d__overloaded_listTags_ptrConstPandaNode_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.StringType):
                    return self._Nametag3d__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                return self._Nametag3d__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 2:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                if isinstance(_args[1], types.IntType):
                    return self._Nametag3d__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def stashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self._Nametag3d__overloaded_stashChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._Nametag3d__overloaded_stashChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def removeChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self._Nametag3d__overloaded_removeChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._Nametag3d__overloaded_removeChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addStashed(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._Nametag3d__overloaded_addStashed_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        elif numArgs == 2:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._Nametag3d__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def upcastToNamable(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyojprb(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToBoundedObject(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyo8YS5(upcastSelf.this)
        import BoundedObject
        returnObject = BoundedObject.BoundedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPkJyogdrc(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpandaexpress._inPJoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpandaexpress._inPJoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpandaexpress._inPJoxtmFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpandaexpress._inPJoxtkXzz(upcastSelf.this, handle.this)
        return returnValue

    
    def assign(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtp1bI(upcastSelf.this, other.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setName(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtavUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtfARN(upcastSelf.this)
        return returnValue

    
    def markBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPG4uI(upcastSelf.this)
        return returnValue

    
    def forceBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPi1Pw(upcastSelf.this)
        return returnValue

    
    def isBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPjac5(upcastSelf.this)
        return returnValue

    
    def setFinal(self, flag):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPy9vH(upcastSelf.this, flag)
        return returnValue

    
    def isFinal(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPUuL4(upcastSelf.this)
        return returnValue

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtM11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtVS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtzyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtupj2(upcastSelf.this)
        return returnValue


