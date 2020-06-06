# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritable
import Namable
import BoundedObject
import ReferenceCount

class PandaNode(TypedWritable.TypedWritable, Namable.Namable, BoundedObject.BoundedObject, ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyomVfc(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyo0yAx:
            libpanda._inPnJyo0yAx(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyo6Ap_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def copySubgraph(self):
        returnValue = libpanda._inPnJyoFYnx(self.this)
        returnObject = PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumParents(self):
        returnValue = libpanda._inPnJyoI9bH(self.this)
        return returnValue

    
    def getParent(self, n):
        returnValue = libpanda._inPnJyoh0xF(self.this, n)
        returnObject = PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findParent(self, node):
        returnValue = libpanda._inPnJyoMWG_(self.this, node.this)
        return returnValue

    
    def getNumChildren(self):
        returnValue = libpanda._inPnJyo78Bo(self.this)
        return returnValue

    
    def getChild(self, n):
        returnValue = libpanda._inPnJyokZg9(self.this, n)
        returnObject = PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getChildSort(self, n):
        returnValue = libpanda._inPnJyoMzeG(self.this, n)
        return returnValue

    
    def findChild(self, node):
        returnValue = libpanda._inPnJyoKHuN(self.this, node.this)
        return returnValue

    
    def _PandaNode__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        returnValue = libpanda._inPnJyoA9tQ(self.this, childNode.this, sort)
        return returnValue

    
    def _PandaNode__overloaded_addChild_ptrPandaNode_ptrPandaNode(self, childNode):
        returnValue = libpanda._inPnJyo27ri(self.this, childNode.this)
        return returnValue

    
    def _PandaNode__overloaded_removeChild_ptrPandaNode_ptrPandaNode(self, childNode):
        returnValue = libpanda._inPnJyozFZb(self.this, childNode.this)
        return returnValue

    
    def _PandaNode__overloaded_removeChild_ptrPandaNode_int(self, n):
        returnValue = libpanda._inPnJyoDqN1(self.this, n)
        return returnValue

    
    def replaceChild(self, origChild, newChild):
        returnValue = libpanda._inPnJyogW5Y(self.this, origChild.this, newChild.this)
        return returnValue

    
    def _PandaNode__overloaded_stashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        returnValue = libpanda._inPnJyojC1w(self.this, childNode.this)
        return returnValue

    
    def _PandaNode__overloaded_stashChild_ptrPandaNode_int(self, childIndex):
        returnValue = libpanda._inPnJyorWqz(self.this, childIndex)
        return returnValue

    
    def _PandaNode__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        returnValue = libpanda._inPnJyoqJGM(self.this, childNode.this)
        return returnValue

    
    def _PandaNode__overloaded_unstashChild_ptrPandaNode_int(self, stashedIndex):
        returnValue = libpanda._inPnJyoeWxF(self.this, stashedIndex)
        return returnValue

    
    def getNumStashed(self):
        returnValue = libpanda._inPnJyoOR8_(self.this)
        return returnValue

    
    def getStashed(self, n):
        returnValue = libpanda._inPnJyok8qw(self.this, n)
        returnObject = PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getStashedSort(self, n):
        returnValue = libpanda._inPnJyoE1FX(self.this, n)
        return returnValue

    
    def findStashed(self, node):
        returnValue = libpanda._inPnJyoyw9C(self.this, node.this)
        return returnValue

    
    def _PandaNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        returnValue = libpanda._inPnJyoXQ0n(self.this, childNode.this, sort)
        return returnValue

    
    def _PandaNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode(self, childNode):
        returnValue = libpanda._inPnJyoswLI(self.this, childNode.this)
        return returnValue

    
    def removeStashed(self, n):
        returnValue = libpanda._inPnJyoZHe7(self.this, n)
        return returnValue

    
    def removeAllChildren(self):
        returnValue = libpanda._inPnJyobyap(self.this)
        return returnValue

    
    def stealChildren(self, other):
        returnValue = libpanda._inPnJyojgnr(self.this, other.this)
        return returnValue

    
    def copyChildren(self, other):
        returnValue = libpanda._inPnJyohfED(self.this, other.this)
        return returnValue

    
    def _PandaNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(self, attrib, override):
        returnValue = libpanda._inPnJyo48Bd(self.this, attrib.this, override)
        return returnValue

    
    def _PandaNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(self, attrib):
        returnValue = libpanda._inPnJyoDD5k(self.this, attrib.this)
        return returnValue

    
    def getAttrib(self, type):
        returnValue = libpanda._inPnJyoaDfJ(self.this, type.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasAttrib(self, type):
        returnValue = libpanda._inPnJyo2W_P(self.this, type.this)
        return returnValue

    
    def clearAttrib(self, type):
        returnValue = libpanda._inPnJyoDSEu(self.this, type.this)
        return returnValue

    
    def setEffect(self, effect):
        returnValue = libpanda._inPnJyoKWvI(self.this, effect.this)
        return returnValue

    
    def getEffect(self, type):
        returnValue = libpanda._inPnJyo07Hl(self.this, type.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasEffect(self, type):
        returnValue = libpanda._inPnJyoI1nr(self.this, type.this)
        return returnValue

    
    def clearEffect(self, type):
        returnValue = libpanda._inPnJyoNUJ2(self.this, type.this)
        return returnValue

    
    def setState(self, state):
        returnValue = libpanda._inPnJyoGDjV(self.this, state.this)
        return returnValue

    
    def getState(self):
        returnValue = libpanda._inPnJyoJocj(self.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearState(self):
        returnValue = libpanda._inPnJyotySF(self.this)
        return returnValue

    
    def setEffects(self, effects):
        returnValue = libpanda._inPnJyoxlpj(self.this, effects.this)
        return returnValue

    
    def getEffects(self):
        returnValue = libpanda._inPnJyo1WLf(self.this)
        import RenderEffects
        returnObject = RenderEffects.RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearEffects(self):
        returnValue = libpanda._inPnJyo6yPH(self.this)
        return returnValue

    
    def setTransform(self, transform):
        returnValue = libpanda._inPnJyo55Ti(self.this, transform.this)
        return returnValue

    
    def getTransform(self):
        returnValue = libpanda._inPnJyoydH2(self.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearTransform(self):
        returnValue = libpanda._inPnJyoEjK_(self.this)
        return returnValue

    
    def setPrevTransform(self, transform):
        returnValue = libpanda._inPnJyo_3nJ(self.this, transform.this)
        return returnValue

    
    def getPrevTransform(self):
        returnValue = libpanda._inPnJyor3cO(self.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def resetPrevTransform(self):
        returnValue = libpanda._inPnJyoGfcO(self.this)
        return returnValue

    
    def setTag(self, key, value):
        returnValue = libpanda._inPnJyoTNEJ(self.this, key, value)
        return returnValue

    
    def getTag(self, key):
        returnValue = libpanda._inPnJyo5tVl(self.this, key)
        return returnValue

    
    def hasTag(self, key):
        returnValue = libpanda._inPnJyote2r(self.this, key)
        return returnValue

    
    def clearTag(self, key):
        returnValue = libpanda._inPnJyoiRPE(self.this, key)
        return returnValue

    
    def copyTags(self, other):
        returnValue = libpanda._inPnJyoxMQi(self.this, other.this)
        return returnValue

    
    def _PandaNode__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(self, out, separator):
        returnValue = libpanda._inPnJyo3itg(self.this, out.this, separator)
        return returnValue

    
    def _PandaNode__overloaded_listTags_ptrConstPandaNode_ptrOstream(self, out):
        returnValue = libpanda._inPnJyocRES(self.this, out.this)
        return returnValue

    
    def setDrawMask(self, mask):
        returnValue = libpanda._inPnJyofzL6(self.this, mask.this)
        return returnValue

    
    def getDrawMask(self):
        returnValue = libpanda._inPnJyoWJXI(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setIntoCollideMask(self, mask):
        returnValue = libpanda._inPnJyoK9VT(self.this, mask.this)
        return returnValue

    
    def getIntoCollideMask(self):
        returnValue = libpanda._inPnJyoc3Cf(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getLegalCollideMask(self):
        returnValue = libpanda._inPnJyotnOA(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNetCollideMask(self):
        returnValue = libpanda._inPnJyo4l_T(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libpanda._inPnJyoW23T(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPnJyoSz8K(self.this, out.this, indentLevel)
        return returnValue

    
    def ls(self, out, indentLevel):
        returnValue = libpanda._inPnJyopBSg(self.this, out.this, indentLevel)
        return returnValue

    
    def _PandaNode__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(self, type):
        returnValue = libpanda._inPnJyomd5g(self.this, type)
        return returnValue

    
    def _PandaNode__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(self, volume):
        returnValue = libpanda._inPnJyo4Bq1(self.this, volume.this)
        return returnValue

    
    def getBound(self):
        returnValue = libpanda._inPnJyoif0y(self.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getInternalBound(self):
        returnValue = libpanda._inPnJyoJ_J4(self.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def isGeomNode(self):
        returnValue = libpanda._inPnJyoxAx3(self.this)
        return returnValue

    
    def isLodNode(self):
        returnValue = libpanda._inPnJyohW8z(self.this)
        return returnValue

    
    def asLight(self):
        returnValue = libpanda._inPnJyobCbs(self.this)
        import Light
        returnObject = Light.Light(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToNamable(self):
        returnValue = libpanda._inPnJyojprb(self.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToBoundedObject(self):
        returnValue = libpanda._inPnJyo7YS5(self.this)
        import BoundedObject
        returnObject = BoundedObject.BoundedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        returnValue = libpanda._inPnJyogdrc(self.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
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
        returnValue = libpandaexpress._inPKoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtnFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt7Xzz(upcastSelf.this, handle.this)
        return returnValue

    
    def assign(self, other):
        upcastSelf = self
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
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtZvUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPKoxtfARN(upcastSelf.this)
        return returnValue

    
    def markBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPG4uI(upcastSelf.this)
        return returnValue

    
    def forceBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPj1Pw(upcastSelf.this)
        return returnValue

    
    def isBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPkac5(upcastSelf.this)
        return returnValue

    
    def setFinal(self, flag):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPy9vH(upcastSelf.this, flag)
        return returnValue

    
    def isFinal(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPbuL4(upcastSelf.this)
        return returnValue

    
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

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._PandaNode__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(*_args)
            
            import BoundingVolume
            if isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._PandaNode__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PandaNode__overloaded_addChild_ptrPandaNode_ptrPandaNode(*_args)
        elif numArgs == 2:
            return self._PandaNode__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def unstashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._PandaNode__overloaded_unstashChild_ptrPandaNode_int(*_args)
            
            if isinstance(_args[0], PandaNode):
                return self._PandaNode__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def listTags(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PandaNode__overloaded_listTags_ptrConstPandaNode_ptrOstream(*_args)
        elif numArgs == 2:
            return self._PandaNode__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PandaNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(*_args)
        elif numArgs == 2:
            return self._PandaNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def stashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._PandaNode__overloaded_stashChild_ptrPandaNode_int(*_args)
            
            if isinstance(_args[0], PandaNode):
                return self._PandaNode__overloaded_stashChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def removeChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._PandaNode__overloaded_removeChild_ptrPandaNode_int(*_args)
            
            if isinstance(_args[0], PandaNode):
                return self._PandaNode__overloaded_removeChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addStashed(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PandaNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode(*_args)
        elif numArgs == 2:
            return self._PandaNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


