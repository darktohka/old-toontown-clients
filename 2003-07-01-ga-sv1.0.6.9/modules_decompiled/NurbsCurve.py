# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PiecewiseCurve
import NurbsCurveInterface

class NurbsCurve(PiecewiseCurve.PiecewiseCurve, NurbsCurveInterface.NurbsCurveInterface, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _NurbsCurve__overloaded_constructor(self):
        self.this = libpanda._inPHc9WMBx5()
        self.userManagesMemory = 1

    
    def _NurbsCurve__overloaded_constructor_ptrConstParametricCurve(self, pc):
        self.this = libpanda._inPHc9WGAYT(pc.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHc9WkrsC:
            libpanda._inPHc9WkrsC(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHc9WH8Ud()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def upcastToNurbsCurveInterface(self):
        returnValue = libpanda._inPHc9WlX1R(self.this)
        import NurbsCurveInterface
        returnObject = NurbsCurveInterface.NurbsCurveInterface(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isValid(self):
        upcastSelf = self
        returnValue = libpanda._inPHc9WhDM7(upcastSelf.this)
        return returnValue

    
    def getMaxT(self):
        upcastSelf = self
        returnValue = libpanda._inPHc9Wan3O(upcastSelf.this)
        return returnValue

    
    def setCurveType(self, type):
        upcastSelf = self
        returnValue = libpanda._inPHc9Wumed(upcastSelf.this, type)
        return returnValue

    
    def getCurveType(self):
        upcastSelf = self
        returnValue = libpanda._inPHc9WuPVX(upcastSelf.this)
        return returnValue

    
    def setNumDimensions(self, num):
        upcastSelf = self
        returnValue = libpanda._inPHc9WKuzT(upcastSelf.this, num)
        return returnValue

    
    def getNumDimensions(self):
        upcastSelf = self
        returnValue = libpanda._inPHc9WiD71(upcastSelf.this)
        return returnValue

    
    def _NurbsCurve__overloaded_calcLength_ptrConstParametricCurve(self):
        upcastSelf = self
        returnValue = libpanda._inPHc9WbQeF(upcastSelf.this)
        return returnValue

    
    def _NurbsCurve__overloaded_calcLength_ptrConstParametricCurve_float_float(self, _from, to):
        upcastSelf = self
        returnValue = libpanda._inPHc9WBINZ(upcastSelf.this, _from, to)
        return returnValue

    
    def findLength(self, startT, lengthOffset):
        upcastSelf = self
        returnValue = libpanda._inPHc9WFyLm(upcastSelf.this, startT, lengthOffset)
        return returnValue

    
    def getPoint(self, t, point):
        upcastSelf = self
        returnValue = libpanda._inPHc9Wo5OE(upcastSelf.this, t, point.this)
        return returnValue

    
    def getTangent(self, t, tangent):
        upcastSelf = self
        returnValue = libpanda._inPHc9WHDs0(upcastSelf.this, t, tangent.this)
        return returnValue

    
    def getPt(self, t, point, tangent):
        upcastSelf = self
        returnValue = libpanda._inPHc9WIOPy(upcastSelf.this, t, point.this, tangent.this)
        return returnValue

    
    def get2ndtangent(self, t, tangent2):
        upcastSelf = self
        returnValue = libpanda._inPHc9WP1ia(upcastSelf.this, t, tangent2.this)
        return returnValue

    
    def adjustPoint(self, t, px, py, pz):
        upcastSelf = self
        returnValue = libpanda._inPHc9W7vVs(upcastSelf.this, t, px, py, pz)
        return returnValue

    
    def adjustTangent(self, t, tx, ty, tz):
        upcastSelf = self
        returnValue = libpanda._inPHc9WjLxE(upcastSelf.this, t, tx, ty, tz)
        return returnValue

    
    def adjustPt(self, t, px, py, pz, tx, ty, tz):
        upcastSelf = self
        returnValue = libpanda._inPHc9WxacM(upcastSelf.this, t, px, py, pz, tx, ty, tz)
        return returnValue

    
    def recompute(self):
        upcastSelf = self
        returnValue = libpanda._inPHc9WkG_o(upcastSelf.this)
        return returnValue

    
    def stitch(self, a, b):
        upcastSelf = self
        returnValue = libpanda._inPHc9WKq7P(upcastSelf.this, a.this, b.this)
        return returnValue

    
    def _NurbsCurve__overloaded_writeEgg_ptrParametricCurve_ptrFilename___enum__CoordinateSystem(self, filename, cs):
        upcastSelf = self
        returnValue = libpanda._inPHc9W_qGa(upcastSelf.this, filename.this, cs)
        return returnValue

    
    def _NurbsCurve__overloaded_writeEgg_ptrParametricCurve_ptrFilename(self, filename):
        upcastSelf = self
        returnValue = libpanda._inPHc9Wx_vA(upcastSelf.this, filename.this)
        return returnValue

    
    def _NurbsCurve__overloaded_writeEgg_ptrParametricCurve_ptrOstream_ptrConstFilename___enum__CoordinateSystem(self, out, filename, cs):
        upcastSelf = self
        returnValue = libpanda._inPHc9WuHju(upcastSelf.this, out.this, filename.this, cs)
        return returnValue

    
    def writeEgg(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._NurbsCurve__overloaded_writeEgg_ptrParametricCurve_ptrFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._NurbsCurve__overloaded_writeEgg_ptrParametricCurve_ptrFilename___enum__CoordinateSystem(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 3:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    if isinstance(_args[2], types.IntType):
                        return self._NurbsCurve__overloaded_writeEgg_ptrParametricCurve_ptrOstream_ptrConstFilename___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def calcLength(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NurbsCurve__overloaded_calcLength_ptrConstParametricCurve()
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NurbsCurve__overloaded_calcLength_ptrConstParametricCurve_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '

    
    def copySubgraph(self):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyoI9bH(upcastSelf.this)
        return returnValue

    
    def getParent(self, n):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyoNWG_(upcastSelf.this, node.this)
        return returnValue

    
    def getNumChildren(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyo68Bo(upcastSelf.this)
        return returnValue

    
    def getChild(self, n):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyoMzeG(upcastSelf.this, n)
        return returnValue

    
    def findChild(self, node):
        upcastSelf = self
        returnValue = libpanda._inPkJyoKHuN(upcastSelf.this, node.this)
        return returnValue

    
    def _NurbsCurve__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        returnValue = libpanda._inPkJyoA9tQ(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _NurbsCurve__overloaded_addChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyo37ri(upcastSelf.this, childNode.this)
        return returnValue

    
    def _NurbsCurve__overloaded_removeChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyozFZb(upcastSelf.this, childNode.this)
        return returnValue

    
    def _NurbsCurve__overloaded_removeChild_ptrPandaNode_int(self, n):
        upcastSelf = self
        returnValue = libpanda._inPkJyoCqN1(upcastSelf.this, n)
        return returnValue

    
    def replaceChild(self, origChild, newChild):
        upcastSelf = self
        returnValue = libpanda._inPkJyogW5Y(upcastSelf.this, origChild.this, newChild.this)
        return returnValue

    
    def _NurbsCurve__overloaded_stashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyokC1w(upcastSelf.this, childNode.this)
        return returnValue

    
    def _NurbsCurve__overloaded_stashChild_ptrPandaNode_int(self, childIndex):
        upcastSelf = self
        returnValue = libpanda._inPkJyoqWqz(upcastSelf.this, childIndex)
        return returnValue

    
    def _NurbsCurve__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyoqJGM(upcastSelf.this, childNode.this)
        return returnValue

    
    def _NurbsCurve__overloaded_unstashChild_ptrPandaNode_int(self, stashedIndex):
        upcastSelf = self
        returnValue = libpanda._inPkJyoeWxF(upcastSelf.this, stashedIndex)
        return returnValue

    
    def getNumStashed(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoPR8_(upcastSelf.this)
        return returnValue

    
    def getStashed(self, n):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyoE1FX(upcastSelf.this, n)
        return returnValue

    
    def findStashed(self, node):
        upcastSelf = self
        returnValue = libpanda._inPkJyoyw9C(upcastSelf.this, node.this)
        return returnValue

    
    def _NurbsCurve__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        returnValue = libpanda._inPkJyoQQ0n(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _NurbsCurve__overloaded_addStashed_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyoswLI(upcastSelf.this, childNode.this)
        return returnValue

    
    def removeStashed(self, n):
        upcastSelf = self
        returnValue = libpanda._inPkJyoYHe7(upcastSelf.this, n)
        return returnValue

    
    def removeAllChildren(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoayap(upcastSelf.this)
        return returnValue

    
    def stealChildren(self, other):
        upcastSelf = self
        returnValue = libpanda._inPkJyoignr(upcastSelf.this, other.this)
        return returnValue

    
    def copyChildren(self, other):
        upcastSelf = self
        returnValue = libpanda._inPkJyohfED(upcastSelf.this, other.this)
        return returnValue

    
    def _NurbsCurve__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(self, attrib, override):
        upcastSelf = self
        returnValue = libpanda._inPkJyo48Bd(upcastSelf.this, attrib.this, override)
        return returnValue

    
    def _NurbsCurve__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(self, attrib):
        upcastSelf = self
        returnValue = libpanda._inPkJyoAD5k(upcastSelf.this, attrib.this)
        return returnValue

    
    def getAttrib(self, type):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyo2W_P(upcastSelf.this, type.this)
        return returnValue

    
    def clearAttrib(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyoCSEu(upcastSelf.this, type.this)
        return returnValue

    
    def setEffect(self, effect):
        upcastSelf = self
        returnValue = libpanda._inPkJyoKWvI(upcastSelf.this, effect.this)
        return returnValue

    
    def getEffect(self, type):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyoJ1nr(upcastSelf.this, type.this)
        return returnValue

    
    def clearEffect(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyoOUJ2(upcastSelf.this, type.this)
        return returnValue

    
    def setState(self, state):
        upcastSelf = self
        returnValue = libpanda._inPkJyoGDjV(upcastSelf.this, state.this)
        return returnValue

    
    def getState(self):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyotySF(upcastSelf.this)
        return returnValue

    
    def setEffects(self, effects):
        upcastSelf = self
        returnValue = libpanda._inPkJyo2lpj(upcastSelf.this, effects.this)
        return returnValue

    
    def getEffects(self):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyo6yPH(upcastSelf.this)
        return returnValue

    
    def setTransform(self, transform):
        upcastSelf = self
        returnValue = libpanda._inPkJyo_5Ti(upcastSelf.this, transform.this)
        return returnValue

    
    def getTransform(self):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyoHjK_(upcastSelf.this)
        return returnValue

    
    def setDrawMask(self, mask):
        upcastSelf = self
        returnValue = libpanda._inPkJyoSSGr(upcastSelf.this, mask.this)
        return returnValue

    
    def getDrawMask(self):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyoW23T(upcastSelf.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        upcastSelf = self
        returnValue = libpanda._inPkJyoSz8K(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def ls(self, out, indentLevel):
        upcastSelf = self
        returnValue = libpanda._inPkJyouBSg(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def _NurbsCurve__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyond5g(upcastSelf.this, type)
        return returnValue

    
    def _NurbsCurve__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        returnValue = libpanda._inPkJyo7Bq1(upcastSelf.this, volume.this)
        return returnValue

    
    def getBound(self):
        upcastSelf = self
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
        returnValue = libpanda._inPkJyoI_J4(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import BoundingVolume
            if isinstance(_args[0], types.IntType):
                return self._NurbsCurve__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(_args[0])
            elif isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._NurbsCurve__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._NurbsCurve__overloaded_addChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        elif numArgs == 2:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._NurbsCurve__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
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
                return self._NurbsCurve__overloaded_unstashChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._NurbsCurve__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addStashed(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._NurbsCurve__overloaded_addStashed_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        elif numArgs == 2:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._NurbsCurve__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def removeChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self._NurbsCurve__overloaded_removeChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._NurbsCurve__overloaded_removeChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def stashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self._NurbsCurve__overloaded_stashChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._NurbsCurve__overloaded_stashChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                return self._NurbsCurve__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 2:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                if isinstance(_args[1], types.IntType):
                    return self._NurbsCurve__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def upcastToNamable(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyojprb(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToBoundedObject(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyo8YS5(upcastSelf.this)
        import BoundedObject
        returnObject = BoundedObject.BoundedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyogdrc(upcastSelf.this)
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

    
    def output(self, out):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtvz7q(upcastSelf.this, out.this)
        return returnValue

    
    def _NurbsCurve__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPC76J(upcastSelf.this, type)
        return returnValue

    
    def _NurbsCurve__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPXVRr(upcastSelf.this, volume.this)
        return returnValue

    
    def getBound(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPtOIb(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
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

    
    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import BoundingVolume
            if isinstance(_args[0], types.IntType):
                return self._NurbsCurve__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(_args[0])
            elif isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._NurbsCurve__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
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

    
    def setOrder(self, order):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WKhK6(upcastSelf.this, order)
        return returnValue

    
    def getOrder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WhPY_(upcastSelf.this)
        return returnValue

    
    def getNumCvs(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WWaqD(upcastSelf.this)
        return returnValue

    
    def getNumKnots(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WPQ5_(upcastSelf.this)
        return returnValue

    
    def insertCv(self, t):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9W8ScU(upcastSelf.this, t)
        return returnValue

    
    def _NurbsCurve__overloaded_appendCv_ptrNurbsCurveInterface_ptrConstLVecBase3f(self, v):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WpfTi(upcastSelf.this, v.this)
        return returnValue

    
    def _NurbsCurve__overloaded_appendCv_ptrNurbsCurveInterface_ptrConstLVecBase4f(self, v):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WhMdi(upcastSelf.this, v.this)
        return returnValue

    
    def _NurbsCurve__overloaded_appendCv_ptrNurbsCurveInterface_float_float_float(self, x, y, z):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WB3ZR(upcastSelf.this, x, y, z)
        return returnValue

    
    def removeCv(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WpA5o(upcastSelf.this, n)
        return returnValue

    
    def removeAllCvs(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9W0Nej(upcastSelf.this)
        return returnValue

    
    def _NurbsCurve__overloaded_setCvPoint_ptrNurbsCurveInterface_int_ptrConstLVecBase3f(self, n, v):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9W13Z_(upcastSelf.this, n, v.this)
        return returnValue

    
    def _NurbsCurve__overloaded_setCvPoint_ptrNurbsCurveInterface_int_float_float_float(self, n, x, y, z):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WvbUc(upcastSelf.this, n, x, y, z)
        return returnValue

    
    def getCvPoint(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WKFJB(upcastSelf.this, n)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCvWeight(self, n, w):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WkgWd(upcastSelf.this, n, w)
        return returnValue

    
    def getCvWeight(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WQgDH(upcastSelf.this, n)
        return returnValue

    
    def setCv(self, n, v):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WvLws(upcastSelf.this, n, v.this)
        return returnValue

    
    def getCv(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9W_TRe(upcastSelf.this, n)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setKnot(self, n, t):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9WCnR8(upcastSelf.this, n, t)
        return returnValue

    
    def getKnot(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9W_MjW(upcastSelf.this, n)
        return returnValue

    
    def writeCv(self, out, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
        returnValue = libpanda._inPHc9W6ybU(upcastSelf.this, out.this, n)
        return returnValue

    
    def setCvPoint(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._NurbsCurve__overloaded_setCvPoint_ptrNurbsCurveInterface_int_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._NurbsCurve__overloaded_setCvPoint_ptrNurbsCurveInterface_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

    
    def appendCv(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            import VBase3
            if isinstance(_args[0], VBase4.VBase4):
                return self._NurbsCurve__overloaded_appendCv_ptrNurbsCurveInterface_ptrConstLVecBase4f(_args[0])
            elif isinstance(_args[0], VBase3.VBase3):
                return self._NurbsCurve__overloaded_appendCv_ptrNurbsCurveInterface_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._NurbsCurve__overloaded_appendCv_ptrNurbsCurveInterface_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NurbsCurve__overloaded_constructor()
        elif numArgs == 1:
            import ParametricCurve
            if isinstance(_args[0], ParametricCurve.ParametricCurve):
                return self._NurbsCurve__overloaded_constructor_ptrConstParametricCurve(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <ParametricCurve.ParametricCurve> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


