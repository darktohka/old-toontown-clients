# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Light
import PandaNode

class LightNode(Light.Light, PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoE4i1:
            libpanda._inPnJyoE4i1(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyo6xST()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def output(self, out):
        returnValue = libpanda._inPnJyoNkgn(self.this, out.this)
        return returnValue

    
    def _LightNode__overloaded_write_ptrConstLightNode_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPnJyozDle(self.this, out.this, indentLevel)
        return returnValue

    
    def _LightNode__overloaded_write_ptrConstLightNode_ptrOstream(self, out):
        returnValue = libpanda._inPnJyoSZ_n(self.this, out.this)
        return returnValue

    
    def upcastToPandaNode(self):
        returnValue = libpanda._inPnJyo0Doz(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def asNode(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoOU8w(upcastSelf.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getColor(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyolF_a(upcastSelf.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setColor(self, color):
        upcastSelf = self
        returnValue = libpanda._inPnJyo7_hL(upcastSelf.this, color.this)
        return returnValue

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoqIAk(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtP11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtaS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtwyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtvpj2(upcastSelf.this)
        return returnValue

    
    def copySubgraph(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoFYnx(upcastSelf.this)
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
        returnValue = libpanda._inPnJyoI9bH(upcastSelf.this)
        return returnValue

    
    def getParent(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoh0xF(upcastSelf.this, n)
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
        returnValue = libpanda._inPnJyoMWG_(upcastSelf.this, node.this)
        return returnValue

    
    def getNumChildren(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo78Bo(upcastSelf.this)
        return returnValue

    
    def getChild(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyokZg9(upcastSelf.this, n)
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
        returnValue = libpanda._inPnJyoMzeG(upcastSelf.this, n)
        return returnValue

    
    def findChild(self, node):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoKHuN(upcastSelf.this, node.this)
        return returnValue

    
    def _LightNode__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoA9tQ(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _LightNode__overloaded_addChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo27ri(upcastSelf.this, childNode.this)
        return returnValue

    
    def _LightNode__overloaded_removeChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyozFZb(upcastSelf.this, childNode.this)
        return returnValue

    
    def _LightNode__overloaded_removeChild_ptrPandaNode_int(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoDqN1(upcastSelf.this, n)
        return returnValue

    
    def replaceChild(self, origChild, newChild):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyogW5Y(upcastSelf.this, origChild.this, newChild.this)
        return returnValue

    
    def _LightNode__overloaded_stashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyojC1w(upcastSelf.this, childNode.this)
        return returnValue

    
    def _LightNode__overloaded_stashChild_ptrPandaNode_int(self, childIndex):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyorWqz(upcastSelf.this, childIndex)
        return returnValue

    
    def _LightNode__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoqJGM(upcastSelf.this, childNode.this)
        return returnValue

    
    def _LightNode__overloaded_unstashChild_ptrPandaNode_int(self, stashedIndex):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoeWxF(upcastSelf.this, stashedIndex)
        return returnValue

    
    def getNumStashed(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoOR8_(upcastSelf.this)
        return returnValue

    
    def getStashed(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyok8qw(upcastSelf.this, n)
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
        returnValue = libpanda._inPnJyoE1FX(upcastSelf.this, n)
        return returnValue

    
    def findStashed(self, node):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoyw9C(upcastSelf.this, node.this)
        return returnValue

    
    def _LightNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoXQ0n(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _LightNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoswLI(upcastSelf.this, childNode.this)
        return returnValue

    
    def removeStashed(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoZHe7(upcastSelf.this, n)
        return returnValue

    
    def removeAllChildren(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyobyap(upcastSelf.this)
        return returnValue

    
    def stealChildren(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyojgnr(upcastSelf.this, other.this)
        return returnValue

    
    def copyChildren(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyohfED(upcastSelf.this, other.this)
        return returnValue

    
    def _LightNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(self, attrib, override):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo48Bd(upcastSelf.this, attrib.this, override)
        return returnValue

    
    def _LightNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(self, attrib):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoDD5k(upcastSelf.this, attrib.this)
        return returnValue

    
    def getAttrib(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoaDfJ(upcastSelf.this, type.this)
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
        returnValue = libpanda._inPnJyo2W_P(upcastSelf.this, type.this)
        return returnValue

    
    def clearAttrib(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoDSEu(upcastSelf.this, type.this)
        return returnValue

    
    def setEffect(self, effect):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoKWvI(upcastSelf.this, effect.this)
        return returnValue

    
    def getEffect(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo07Hl(upcastSelf.this, type.this)
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
        returnValue = libpanda._inPnJyoI1nr(upcastSelf.this, type.this)
        return returnValue

    
    def clearEffect(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoNUJ2(upcastSelf.this, type.this)
        return returnValue

    
    def setState(self, state):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoGDjV(upcastSelf.this, state.this)
        return returnValue

    
    def getState(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoJocj(upcastSelf.this)
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
        returnValue = libpanda._inPnJyotySF(upcastSelf.this)
        return returnValue

    
    def setEffects(self, effects):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoxlpj(upcastSelf.this, effects.this)
        return returnValue

    
    def getEffects(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo1WLf(upcastSelf.this)
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
        returnValue = libpanda._inPnJyo6yPH(upcastSelf.this)
        return returnValue

    
    def setTransform(self, transform):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo55Ti(upcastSelf.this, transform.this)
        return returnValue

    
    def getTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoydH2(upcastSelf.this)
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
        returnValue = libpanda._inPnJyoEjK_(upcastSelf.this)
        return returnValue

    
    def setPrevTransform(self, transform):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo_3nJ(upcastSelf.this, transform.this)
        return returnValue

    
    def getPrevTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyor3cO(upcastSelf.this)
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
        returnValue = libpanda._inPnJyoGfcO(upcastSelf.this)
        return returnValue

    
    def setTag(self, key, value):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoTNEJ(upcastSelf.this, key, value)
        return returnValue

    
    def getTag(self, key):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo5tVl(upcastSelf.this, key)
        return returnValue

    
    def hasTag(self, key):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyote2r(upcastSelf.this, key)
        return returnValue

    
    def clearTag(self, key):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoiRPE(upcastSelf.this, key)
        return returnValue

    
    def copyTags(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoxMQi(upcastSelf.this, other.this)
        return returnValue

    
    def _LightNode__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(self, out, separator):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo3itg(upcastSelf.this, out.this, separator)
        return returnValue

    
    def _LightNode__overloaded_listTags_ptrConstPandaNode_ptrOstream(self, out):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyocRES(upcastSelf.this, out.this)
        return returnValue

    
    def setDrawMask(self, mask):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyofzL6(upcastSelf.this, mask.this)
        return returnValue

    
    def getDrawMask(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoWJXI(upcastSelf.this)
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
        returnValue = libpanda._inPnJyo4l_T(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def ls(self, out, indentLevel):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyopBSg(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def _LightNode__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyomd5g(upcastSelf.this, type)
        return returnValue

    
    def _LightNode__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo4Bq1(upcastSelf.this, volume.this)
        return returnValue

    
    def getBound(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyoif0y(upcastSelf.this)
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
        returnValue = libpanda._inPnJyoJ_J4(upcastSelf.this)
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
        returnValue = libpanda._inPnJyoxAx3(upcastSelf.this)
        return returnValue

    
    def asLight(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyobCbs(upcastSelf.this)
        import Light
        returnObject = Light.Light(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._LightNode__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(*_args)
            
            import BoundingVolume
            if isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._LightNode__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._LightNode__overloaded_addChild_ptrPandaNode_ptrPandaNode(*_args)
        elif numArgs == 2:
            return self._LightNode__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def unstashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._LightNode__overloaded_unstashChild_ptrPandaNode_int(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._LightNode__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def listTags(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._LightNode__overloaded_listTags_ptrConstPandaNode_ptrOstream(*_args)
        elif numArgs == 2:
            return self._LightNode__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._LightNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(*_args)
        elif numArgs == 2:
            return self._LightNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def stashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._LightNode__overloaded_stashChild_ptrPandaNode_int(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._LightNode__overloaded_stashChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def removeChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._LightNode__overloaded_removeChild_ptrPandaNode_int(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._LightNode__overloaded_removeChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addStashed(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._LightNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode(*_args)
        elif numArgs == 2:
            return self._LightNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def upcastToNamable(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyojprb(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToBoundedObject(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyo7YS5(upcastSelf.this)
        import BoundedObject
        returnObject = BoundedObject.BoundedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpanda._inPnJyogdrc(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpandaexpress._inPKoxt1uxI(upcastSelf.this)
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
        returnValue = libpandaexpress._inPKoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpandaexpress._inPKoxtnFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        returnValue = libpandaexpress._inPKoxt7Xzz(upcastSelf.this, handle.this)
        return returnValue

    
    def assign(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtp1bI(upcastSelf.this, other.this)
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
        returnValue = libpandaexpress._inPKoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtZvUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtfARN(upcastSelf.this)
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
        returnValue = libpanda._inPMAKPj1Pw(upcastSelf.this)
        return returnValue

    
    def isBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPkac5(upcastSelf.this)
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
        returnValue = libpanda._inPMAKPbuL4(upcastSelf.this)
        return returnValue

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtP11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtaS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtwyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToPandaNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtvpj2(upcastSelf.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._LightNode__overloaded_write_ptrConstLightNode_ptrOstream(*_args)
        elif numArgs == 2:
            return self._LightNode__overloaded_write_ptrConstLightNode_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


