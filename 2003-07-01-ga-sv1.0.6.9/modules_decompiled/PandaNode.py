# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPkJyomVfc(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyo3yAx:
            libpanda._inPkJyo3yAx(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPkJyo7Ap_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def copySubgraph(self):
        returnValue = libpanda._inPkJyoGYnx(self.this)
        returnObject = PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumParents(self):
        returnValue = libpanda._inPkJyoI9bH(self.this)
        return returnValue

    
    def getParent(self, n):
        returnValue = libpanda._inPkJyoh0xF(self.this, n)
        returnObject = PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findParent(self, node):
        returnValue = libpanda._inPkJyoNWG_(self.this, node.this)
        return returnValue

    
    def getNumChildren(self):
        returnValue = libpanda._inPkJyo68Bo(self.this)
        return returnValue

    
    def getChild(self, n):
        returnValue = libpanda._inPkJyonZg9(self.this, n)
        returnObject = PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getChildSort(self, n):
        returnValue = libpanda._inPkJyoMzeG(self.this, n)
        return returnValue

    
    def findChild(self, node):
        returnValue = libpanda._inPkJyoKHuN(self.this, node.this)
        return returnValue

    
    def _PandaNode__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        returnValue = libpanda._inPkJyoA9tQ(self.this, childNode.this, sort)
        return returnValue

    
    def _PandaNode__overloaded_addChild_ptrPandaNode_ptrPandaNode(self, childNode):
        returnValue = libpanda._inPkJyo37ri(self.this, childNode.this)
        return returnValue

    
    def _PandaNode__overloaded_removeChild_ptrPandaNode_ptrPandaNode(self, childNode):
        returnValue = libpanda._inPkJyozFZb(self.this, childNode.this)
        return returnValue

    
    def _PandaNode__overloaded_removeChild_ptrPandaNode_int(self, n):
        returnValue = libpanda._inPkJyoCqN1(self.this, n)
        return returnValue

    
    def replaceChild(self, origChild, newChild):
        returnValue = libpanda._inPkJyogW5Y(self.this, origChild.this, newChild.this)
        return returnValue

    
    def _PandaNode__overloaded_stashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        returnValue = libpanda._inPkJyokC1w(self.this, childNode.this)
        return returnValue

    
    def _PandaNode__overloaded_stashChild_ptrPandaNode_int(self, childIndex):
        returnValue = libpanda._inPkJyoqWqz(self.this, childIndex)
        return returnValue

    
    def _PandaNode__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        returnValue = libpanda._inPkJyoqJGM(self.this, childNode.this)
        return returnValue

    
    def _PandaNode__overloaded_unstashChild_ptrPandaNode_int(self, stashedIndex):
        returnValue = libpanda._inPkJyoeWxF(self.this, stashedIndex)
        return returnValue

    
    def getNumStashed(self):
        returnValue = libpanda._inPkJyoPR8_(self.this)
        return returnValue

    
    def getStashed(self, n):
        returnValue = libpanda._inPkJyol8qw(self.this, n)
        returnObject = PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getStashedSort(self, n):
        returnValue = libpanda._inPkJyoE1FX(self.this, n)
        return returnValue

    
    def findStashed(self, node):
        returnValue = libpanda._inPkJyoyw9C(self.this, node.this)
        return returnValue

    
    def _PandaNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        returnValue = libpanda._inPkJyoQQ0n(self.this, childNode.this, sort)
        return returnValue

    
    def _PandaNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode(self, childNode):
        returnValue = libpanda._inPkJyoswLI(self.this, childNode.this)
        return returnValue

    
    def removeStashed(self, n):
        returnValue = libpanda._inPkJyoYHe7(self.this, n)
        return returnValue

    
    def removeAllChildren(self):
        returnValue = libpanda._inPkJyoayap(self.this)
        return returnValue

    
    def stealChildren(self, other):
        returnValue = libpanda._inPkJyoignr(self.this, other.this)
        return returnValue

    
    def copyChildren(self, other):
        returnValue = libpanda._inPkJyohfED(self.this, other.this)
        return returnValue

    
    def _PandaNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(self, attrib, override):
        returnValue = libpanda._inPkJyo48Bd(self.this, attrib.this, override)
        return returnValue

    
    def _PandaNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(self, attrib):
        returnValue = libpanda._inPkJyoAD5k(self.this, attrib.this)
        return returnValue

    
    def getAttrib(self, type):
        returnValue = libpanda._inPkJyoaDfJ(self.this, type.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasAttrib(self, type):
        returnValue = libpanda._inPkJyo2W_P(self.this, type.this)
        return returnValue

    
    def clearAttrib(self, type):
        returnValue = libpanda._inPkJyoCSEu(self.this, type.this)
        return returnValue

    
    def setEffect(self, effect):
        returnValue = libpanda._inPkJyoKWvI(self.this, effect.this)
        return returnValue

    
    def getEffect(self, type):
        returnValue = libpanda._inPkJyo17Hl(self.this, type.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasEffect(self, type):
        returnValue = libpanda._inPkJyoJ1nr(self.this, type.this)
        return returnValue

    
    def clearEffect(self, type):
        returnValue = libpanda._inPkJyoOUJ2(self.this, type.this)
        return returnValue

    
    def setState(self, state):
        returnValue = libpanda._inPkJyoGDjV(self.this, state.this)
        return returnValue

    
    def getState(self):
        returnValue = libpanda._inPkJyoIocj(self.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearState(self):
        returnValue = libpanda._inPkJyotySF(self.this)
        return returnValue

    
    def setEffects(self, effects):
        returnValue = libpanda._inPkJyo2lpj(self.this, effects.this)
        return returnValue

    
    def getEffects(self):
        returnValue = libpanda._inPkJyo1WLf(self.this)
        import RenderEffects
        returnObject = RenderEffects.RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearEffects(self):
        returnValue = libpanda._inPkJyo6yPH(self.this)
        return returnValue

    
    def setTransform(self, transform):
        returnValue = libpanda._inPkJyo_5Ti(self.this, transform.this)
        return returnValue

    
    def getTransform(self):
        returnValue = libpanda._inPkJyo1dH2(self.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearTransform(self):
        returnValue = libpanda._inPkJyoHjK_(self.this)
        return returnValue

    
    def setDrawMask(self, mask):
        returnValue = libpanda._inPkJyoSSGr(self.this, mask.this)
        return returnValue

    
    def getDrawMask(self):
        returnValue = libpanda._inPkJyoWJXI(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNetCollideMask(self):
        returnValue = libpanda._inPkJyo4l_T(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libpanda._inPkJyoW23T(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPkJyoSz8K(self.this, out.this, indentLevel)
        return returnValue

    
    def ls(self, out, indentLevel):
        returnValue = libpanda._inPkJyouBSg(self.this, out.this, indentLevel)
        return returnValue

    
    def _PandaNode__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(self, type):
        returnValue = libpanda._inPkJyond5g(self.this, type)
        return returnValue

    
    def _PandaNode__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(self, volume):
        returnValue = libpanda._inPkJyo7Bq1(self.this, volume.this)
        return returnValue

    
    def getBound(self):
        returnValue = libpanda._inPkJyohf0y(self.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getInternalBound(self):
        returnValue = libpanda._inPkJyoI_J4(self.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def upcastToNamable(self):
        returnValue = libpanda._inPkJyojprb(self.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToBoundedObject(self):
        returnValue = libpanda._inPkJyo8YS5(self.this)
        import BoundedObject
        returnObject = BoundedObject.BoundedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        returnValue = libpanda._inPkJyogdrc(self.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
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
        returnValue = libpandaexpress._inPJoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtmFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtkXzz(upcastSelf.this, handle.this)
        return returnValue

    
    def assign(self, other):
        upcastSelf = self
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
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtavUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtfARN(upcastSelf.this)
        return returnValue

    
    def markBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPG4uI(upcastSelf.this)
        return returnValue

    
    def forceBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPi1Pw(upcastSelf.this)
        return returnValue

    
    def isBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPjac5(upcastSelf.this)
        return returnValue

    
    def setFinal(self, flag):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPy9vH(upcastSelf.this, flag)
        return returnValue

    
    def isFinal(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPUuL4(upcastSelf.this)
        return returnValue

    
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

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import BoundingVolume
            if isinstance(_args[0], types.IntType):
                return self._PandaNode__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(_args[0])
            elif isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._PandaNode__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], PandaNode):
                return self._PandaNode__overloaded_addChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode> '
        elif numArgs == 2:
            if isinstance(_args[0], PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._PandaNode__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def unstashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._PandaNode__overloaded_unstashChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode):
                return self._PandaNode__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addStashed(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], PandaNode):
                return self._PandaNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode> '
        elif numArgs == 2:
            if isinstance(_args[0], PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._PandaNode__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def removeChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._PandaNode__overloaded_removeChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode):
                return self._PandaNode__overloaded_removeChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def stashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._PandaNode__overloaded_stashChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode):
                return self._PandaNode__overloaded_stashChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                return self._PandaNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 2:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                if isinstance(_args[1], types.IntType):
                    return self._PandaNode__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


