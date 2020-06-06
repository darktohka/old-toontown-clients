# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DataNode
import MouseWatcherGroup

class MouseWatcher(DataNode.DataNode, MouseWatcherGroup.MouseWatcherGroup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _MouseWatcher__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPziw5cC1c(name)
        self.userManagesMemory = 1

    
    def _MouseWatcher__overloaded_constructor(self):
        self.this = libpanda._inPziw5a1_K()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPziw5yEfY:
            libpanda._inPziw5yEfY(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPziw5fzXa()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def removeRegion(self, region):
        returnValue = libpanda._inPziw5NVgH(self.this, region.this)
        return returnValue

    
    def hasMouse(self):
        returnValue = libpanda._inPziw5NnfE(self.this)
        return returnValue

    
    def isMouseOpen(self):
        returnValue = libpanda._inPziw5Jirl(self.this)
        return returnValue

    
    def getMouse(self):
        returnValue = libpanda._inPziw5P88Z(self.this)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getMouseX(self):
        returnValue = libpanda._inPziw5X5e7(self.this)
        return returnValue

    
    def getMouseY(self):
        returnValue = libpanda._inPziw5unf7(self.this)
        return returnValue

    
    def _MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher(self):
        returnValue = libpanda._inPziw5cWJO(self.this)
        return returnValue

    
    def _MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher_ptrConstLPoint2f(self, pos):
        returnValue = libpanda._inPziw5voLV(self.this, pos.this)
        return returnValue

    
    def _MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher_float_float(self, x, y):
        returnValue = libpanda._inPziw5P62h(self.this, x, y)
        return returnValue

    
    def _MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher(self):
        returnValue = libpanda._inPziw5fZEz(self.this)
        import MouseWatcherRegion
        returnObject = MouseWatcherRegion.MouseWatcherRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher_ptrConstLPoint2f(self, pos):
        returnValue = libpanda._inPziw5g7zU(self.this, pos.this)
        import MouseWatcherRegion
        returnObject = MouseWatcherRegion.MouseWatcherRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher_float_float(self, x, y):
        returnValue = libpanda._inPziw5zQqr(self.this, x, y)
        import MouseWatcherRegion
        returnObject = MouseWatcherRegion.MouseWatcherRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setButtonDownPattern(self, pattern):
        returnValue = libpanda._inPziw5cEcO(self.this, pattern)
        return returnValue

    
    def getButtonDownPattern(self):
        returnValue = libpanda._inPziw5ht1B(self.this)
        return returnValue

    
    def setButtonUpPattern(self, pattern):
        returnValue = libpanda._inPziw5m2Gd(self.this, pattern)
        return returnValue

    
    def getButtonUpPattern(self):
        returnValue = libpanda._inPziw5i4be(self.this)
        return returnValue

    
    def setEnterPattern(self, pattern):
        returnValue = libpanda._inPziw5Zndk(self.this, pattern)
        return returnValue

    
    def getEnterPattern(self):
        returnValue = libpanda._inPziw5BuR6(self.this)
        return returnValue

    
    def setLeavePattern(self, pattern):
        returnValue = libpanda._inPziw5GX33(self.this, pattern)
        return returnValue

    
    def getLeavePattern(self):
        returnValue = libpanda._inPziw5WyqN(self.this)
        return returnValue

    
    def setWithinPattern(self, pattern):
        returnValue = libpanda._inPziw5lQGQ(self.this, pattern)
        return returnValue

    
    def getWithinPattern(self):
        returnValue = libpanda._inPziw5tUxJ(self.this)
        return returnValue

    
    def setWithoutPattern(self, pattern):
        returnValue = libpanda._inPziw5q8_O(self.this, pattern)
        return returnValue

    
    def getWithoutPattern(self):
        returnValue = libpanda._inPziw5a5mF(self.this)
        return returnValue

    
    def setGeometry(self, node):
        returnValue = libpanda._inPziw5CINK(self.this, node.this)
        return returnValue

    
    def hasGeometry(self):
        returnValue = libpanda._inPziw5knGj(self.this)
        return returnValue

    
    def getGeometry(self):
        returnValue = libpanda._inPziw5vJl4(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearGeometry(self):
        returnValue = libpanda._inPziw5blHk(self.this)
        return returnValue

    
    def setExtraHandler(self, eh):
        returnValue = libpanda._inPziw5S4a_(self.this, eh.this)
        return returnValue

    
    def getExtraHandler(self):
        returnValue = libpanda._inPziw5oC6_(self.this)
        import EventHandler
        returnObject = EventHandler.EventHandler(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def setModifierButtons(self, mods):
        returnValue = libpanda._inPziw5tFyZ(self.this, mods.this)
        return returnValue

    
    def getModifierButtons(self):
        returnValue = libpanda._inPziw5L0bg(self.this)
        import ModifierButtons
        returnObject = ModifierButtons.ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def upcastToMouseWatcherGroup(self):
        returnValue = libpanda._inPziw5LdxH(self.this)
        import MouseWatcherGroup
        returnObject = MouseWatcherGroup.MouseWatcherGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def writeInputs(self, out):
        upcastSelf = self
        returnValue = libpanda._inPSLSe4fqQ(upcastSelf.this, out.this)
        return returnValue

    
    def writeOutputs(self, out):
        upcastSelf = self
        returnValue = libpanda._inPSLSeVk5z(upcastSelf.this, out.this)
        return returnValue

    
    def writeConnections(self, out):
        upcastSelf = self
        returnValue = libpanda._inPSLSeXqT4(upcastSelf.this, out.this)
        return returnValue

    
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

    
    def _MouseWatcher__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        returnValue = libpanda._inPkJyoA9tQ(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _MouseWatcher__overloaded_addChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyo37ri(upcastSelf.this, childNode.this)
        return returnValue

    
    def _MouseWatcher__overloaded_removeChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyozFZb(upcastSelf.this, childNode.this)
        return returnValue

    
    def _MouseWatcher__overloaded_removeChild_ptrPandaNode_int(self, n):
        upcastSelf = self
        returnValue = libpanda._inPkJyoCqN1(upcastSelf.this, n)
        return returnValue

    
    def replaceChild(self, origChild, newChild):
        upcastSelf = self
        returnValue = libpanda._inPkJyogW5Y(upcastSelf.this, origChild.this, newChild.this)
        return returnValue

    
    def _MouseWatcher__overloaded_stashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyokC1w(upcastSelf.this, childNode.this)
        return returnValue

    
    def _MouseWatcher__overloaded_stashChild_ptrPandaNode_int(self, childIndex):
        upcastSelf = self
        returnValue = libpanda._inPkJyoqWqz(upcastSelf.this, childIndex)
        return returnValue

    
    def _MouseWatcher__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPkJyoqJGM(upcastSelf.this, childNode.this)
        return returnValue

    
    def _MouseWatcher__overloaded_unstashChild_ptrPandaNode_int(self, stashedIndex):
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

    
    def _MouseWatcher__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        returnValue = libpanda._inPkJyoQQ0n(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _MouseWatcher__overloaded_addStashed_ptrPandaNode_ptrPandaNode(self, childNode):
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

    
    def _MouseWatcher__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(self, attrib, override):
        upcastSelf = self
        returnValue = libpanda._inPkJyo48Bd(upcastSelf.this, attrib.this, override)
        return returnValue

    
    def _MouseWatcher__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(self, attrib):
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

    
    def setTag(self, key, value):
        upcastSelf = self
        returnValue = libpanda._inPkJyoTNEJ(upcastSelf.this, key, value)
        return returnValue

    
    def getTag(self, key):
        upcastSelf = self
        returnValue = libpanda._inPkJyo6tVl(upcastSelf.this, key)
        return returnValue

    
    def hasTag(self, key):
        upcastSelf = self
        returnValue = libpanda._inPkJyoue2r(upcastSelf.this, key)
        return returnValue

    
    def clearTag(self, key):
        upcastSelf = self
        returnValue = libpanda._inPkJyoiRPE(upcastSelf.this, key)
        return returnValue

    
    def copyTags(self, other):
        upcastSelf = self
        returnValue = libpanda._inPkJyoyMQi(upcastSelf.this, other.this)
        return returnValue

    
    def _MouseWatcher__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(self, out, separator):
        upcastSelf = self
        returnValue = libpanda._inPkJyo2itg(upcastSelf.this, out.this, separator)
        return returnValue

    
    def _MouseWatcher__overloaded_listTags_ptrConstPandaNode_ptrOstream(self, out):
        upcastSelf = self
        returnValue = libpanda._inPkJyocRES(upcastSelf.this, out.this)
        return returnValue

    
    def setDrawMask(self, mask):
        upcastSelf = self
        returnValue = libpanda._inPkJyoezL6(upcastSelf.this, mask.this)
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

    
    def setVelocity(self, velocity):
        upcastSelf = self
        returnValue = libpanda._inPkJyoDKry(upcastSelf.this, velocity.this)
        return returnValue

    
    def clearVelocity(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoVb0l(upcastSelf.this)
        return returnValue

    
    def hasVelocity(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoIl5F(upcastSelf.this)
        return returnValue

    
    def getVelocity(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyo0sZ_(upcastSelf.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
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

    
    def _MouseWatcher__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        returnValue = libpanda._inPkJyond5g(upcastSelf.this, type)
        return returnValue

    
    def _MouseWatcher__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(self, volume):
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

    
    def isGeomNode(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoyAx3(upcastSelf.this)
        return returnValue

    
    def asLight(self):
        upcastSelf = self
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
                return self._MouseWatcher__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(_args[0])
            elif isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._MouseWatcher__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._MouseWatcher__overloaded_addChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        elif numArgs == 2:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._MouseWatcher__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
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
                return self._MouseWatcher__overloaded_unstashChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._MouseWatcher__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def listTags(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._MouseWatcher__overloaded_listTags_ptrConstPandaNode_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.StringType):
                    return self._MouseWatcher__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(_args[0], _args[1])
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
                return self._MouseWatcher__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 2:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                if isinstance(_args[1], types.IntType):
                    return self._MouseWatcher__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(_args[0], _args[1])
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
                return self._MouseWatcher__overloaded_stashChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._MouseWatcher__overloaded_stashChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def removeChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self._MouseWatcher__overloaded_removeChild_ptrPandaNode_int(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._MouseWatcher__overloaded_removeChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addStashed(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._MouseWatcher__overloaded_addStashed_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        elif numArgs == 2:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._MouseWatcher__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
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

    
    def _MouseWatcher__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPC76J(upcastSelf.this, type)
        return returnValue

    
    def _MouseWatcher__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(self, volume):
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
                return self._MouseWatcher__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(_args[0])
            elif isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._MouseWatcher__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(_args[0])
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

    
    def addRegion(self, region):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        returnValue = libpanda._inPziw5xUMA(upcastSelf.this, region.this)
        return returnValue

    
    def hasRegion(self, region):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        returnValue = libpanda._inPziw575tC(upcastSelf.this, region.this)
        return returnValue

    
    def findRegion(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        returnValue = libpanda._inPziw52SzS(upcastSelf.this, name)
        import MouseWatcherRegion
        returnObject = MouseWatcherRegion.MouseWatcherRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearRegions(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        returnValue = libpanda._inPziw58D_y(upcastSelf.this)
        return returnValue

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        returnValue = libpanda._inPziw5XWnS(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtM11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtVS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtzyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtupj2(upcastSelf.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._MouseWatcher__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._MouseWatcher__overloaded_constructor_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getOverRegion(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher()
        elif numArgs == 1:
            import Point2
            if isinstance(_args[0], Point2.Point2):
                return self._MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher_ptrConstLPoint2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point2.Point2> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def isOverRegion(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher()
        elif numArgs == 1:
            import Point2
            if isinstance(_args[0], Point2.Point2):
                return self._MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher_ptrConstLPoint2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point2.Point2> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


