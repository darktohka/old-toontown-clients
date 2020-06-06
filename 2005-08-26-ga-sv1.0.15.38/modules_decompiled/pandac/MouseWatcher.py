# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
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
        
        self.constructor(*_args)

    
    def _MouseWatcher__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPyiw5cC1c(name)
        self.userManagesMemory = 1

    
    def _MouseWatcher__overloaded_constructor(self):
        self.this = libpanda._inPyiw5a1_K()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPyiw5yEfY:
            libpanda._inPyiw5yEfY(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPyiw5fzXa()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def removeRegion(self, region):
        returnValue = libpanda._inPyiw5NVgH(self.this, region.this)
        return returnValue

    
    def hasMouse(self):
        returnValue = libpanda._inPyiw5NnfE(self.this)
        return returnValue

    
    def isMouseOpen(self):
        returnValue = libpanda._inPyiw5Iirl(self.this)
        return returnValue

    
    def getMouse(self):
        returnValue = libpanda._inPyiw5P88Z(self.this)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getMouseX(self):
        returnValue = libpanda._inPyiw5Y5e7(self.this)
        return returnValue

    
    def getMouseY(self):
        returnValue = libpanda._inPyiw5hnf7(self.this)
        return returnValue

    
    def _MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher(self):
        returnValue = libpanda._inPyiw5cWJO(self.this)
        return returnValue

    
    def _MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher_ptrConstLPoint2f(self, pos):
        returnValue = libpanda._inPyiw5voLV(self.this, pos.this)
        return returnValue

    
    def _MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher_float_float(self, x, y):
        returnValue = libpanda._inPyiw5O62h(self.this, x, y)
        return returnValue

    
    def _MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher(self):
        returnValue = libpanda._inPyiw5eZEz(self.this)
        import MouseWatcherRegion
        returnObject = MouseWatcherRegion.MouseWatcherRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher_ptrConstLPoint2f(self, pos):
        returnValue = libpanda._inPyiw5g7zU(self.this, pos.this)
        import MouseWatcherRegion
        returnObject = MouseWatcherRegion.MouseWatcherRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher_float_float(self, x, y):
        returnValue = libpanda._inPyiw5wQqr(self.this, x, y)
        import MouseWatcherRegion
        returnObject = MouseWatcherRegion.MouseWatcherRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setButtonDownPattern(self, pattern):
        returnValue = libpanda._inPyiw5cEcO(self.this, pattern)
        return returnValue

    
    def getButtonDownPattern(self):
        returnValue = libpanda._inPyiw5ht1B(self.this)
        return returnValue

    
    def setButtonUpPattern(self, pattern):
        returnValue = libpanda._inPyiw5m2Gd(self.this, pattern)
        return returnValue

    
    def getButtonUpPattern(self):
        returnValue = libpanda._inPyiw5i4be(self.this)
        return returnValue

    
    def setEnterPattern(self, pattern):
        returnValue = libpanda._inPyiw5Yndk(self.this, pattern)
        return returnValue

    
    def getEnterPattern(self):
        returnValue = libpanda._inPyiw5AuR6(self.this)
        return returnValue

    
    def setLeavePattern(self, pattern):
        returnValue = libpanda._inPyiw5HX33(self.this, pattern)
        return returnValue

    
    def getLeavePattern(self):
        returnValue = libpanda._inPyiw5WyqN(self.this)
        return returnValue

    
    def setWithinPattern(self, pattern):
        returnValue = libpanda._inPyiw5lQGQ(self.this, pattern)
        return returnValue

    
    def getWithinPattern(self):
        returnValue = libpanda._inPyiw5tUxJ(self.this)
        return returnValue

    
    def setWithoutPattern(self, pattern):
        returnValue = libpanda._inPyiw5q8_O(self.this, pattern)
        return returnValue

    
    def getWithoutPattern(self):
        returnValue = libpanda._inPyiw5a5mF(self.this)
        return returnValue

    
    def setGeometry(self, node):
        returnValue = libpanda._inPyiw5CINK(self.this, node.this)
        return returnValue

    
    def hasGeometry(self):
        returnValue = libpanda._inPyiw5nnGj(self.this)
        return returnValue

    
    def getGeometry(self):
        returnValue = libpanda._inPyiw5gJl4(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearGeometry(self):
        returnValue = libpanda._inPyiw5alHk(self.this)
        return returnValue

    
    def setExtraHandler(self, eh):
        returnValue = libpanda._inPyiw5T4a_(self.this, eh.this)
        return returnValue

    
    def getExtraHandler(self):
        returnValue = libpanda._inPyiw5pC6_(self.this)
        import EventHandler
        returnObject = EventHandler.EventHandler(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def setModifierButtons(self, mods):
        returnValue = libpanda._inPyiw5tFyZ(self.this, mods.this)
        return returnValue

    
    def getModifierButtons(self):
        returnValue = libpanda._inPyiw5I0bg(self.this)
        import ModifierButtons
        returnObject = ModifierButtons.ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setDisplayRegion(self, dr):
        returnValue = libpanda._inPyiw5in8K(self.this, dr.this)
        return returnValue

    
    def clearDisplayRegion(self):
        returnValue = libpanda._inPyiw51V8S(self.this)
        return returnValue

    
    def getDisplayRegion(self):
        returnValue = libpanda._inPyiw5bAU7(self.this)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasDisplayRegion(self):
        returnValue = libpanda._inPyiw5Zp2l(self.this)
        return returnValue

    
    def upcastToMouseWatcherGroup(self):
        returnValue = libpanda._inPyiw5LdxH(self.this)
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
        returnValue = libpanda._inPSLSeUk5z(upcastSelf.this, out.this)
        return returnValue

    
    def writeConnections(self, out):
        upcastSelf = self
        returnValue = libpanda._inPSLSeUqT4(upcastSelf.this, out.this)
        return returnValue

    
    def copySubgraph(self):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyoI9bH(upcastSelf.this)
        return returnValue

    
    def getParent(self, n):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyoMWG_(upcastSelf.this, node.this)
        return returnValue

    
    def getNumChildren(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyo78Bo(upcastSelf.this)
        return returnValue

    
    def getChild(self, n):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyoMzeG(upcastSelf.this, n)
        return returnValue

    
    def findChild(self, node):
        upcastSelf = self
        returnValue = libpanda._inPnJyoKHuN(upcastSelf.this, node.this)
        return returnValue

    
    def _MouseWatcher__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        returnValue = libpanda._inPnJyoA9tQ(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _MouseWatcher__overloaded_addChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPnJyo27ri(upcastSelf.this, childNode.this)
        return returnValue

    
    def _MouseWatcher__overloaded_removeChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPnJyozFZb(upcastSelf.this, childNode.this)
        return returnValue

    
    def _MouseWatcher__overloaded_removeChild_ptrPandaNode_int(self, n):
        upcastSelf = self
        returnValue = libpanda._inPnJyoDqN1(upcastSelf.this, n)
        return returnValue

    
    def replaceChild(self, origChild, newChild):
        upcastSelf = self
        returnValue = libpanda._inPnJyogW5Y(upcastSelf.this, origChild.this, newChild.this)
        return returnValue

    
    def _MouseWatcher__overloaded_stashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPnJyojC1w(upcastSelf.this, childNode.this)
        return returnValue

    
    def _MouseWatcher__overloaded_stashChild_ptrPandaNode_int(self, childIndex):
        upcastSelf = self
        returnValue = libpanda._inPnJyorWqz(upcastSelf.this, childIndex)
        return returnValue

    
    def _MouseWatcher__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPnJyoqJGM(upcastSelf.this, childNode.this)
        return returnValue

    
    def _MouseWatcher__overloaded_unstashChild_ptrPandaNode_int(self, stashedIndex):
        upcastSelf = self
        returnValue = libpanda._inPnJyoeWxF(upcastSelf.this, stashedIndex)
        return returnValue

    
    def getNumStashed(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoOR8_(upcastSelf.this)
        return returnValue

    
    def getStashed(self, n):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyoE1FX(upcastSelf.this, n)
        return returnValue

    
    def findStashed(self, node):
        upcastSelf = self
        returnValue = libpanda._inPnJyoyw9C(upcastSelf.this, node.this)
        return returnValue

    
    def _MouseWatcher__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        returnValue = libpanda._inPnJyoXQ0n(upcastSelf.this, childNode.this, sort)
        return returnValue

    
    def _MouseWatcher__overloaded_addStashed_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        returnValue = libpanda._inPnJyoswLI(upcastSelf.this, childNode.this)
        return returnValue

    
    def removeStashed(self, n):
        upcastSelf = self
        returnValue = libpanda._inPnJyoZHe7(upcastSelf.this, n)
        return returnValue

    
    def removeAllChildren(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyobyap(upcastSelf.this)
        return returnValue

    
    def stealChildren(self, other):
        upcastSelf = self
        returnValue = libpanda._inPnJyojgnr(upcastSelf.this, other.this)
        return returnValue

    
    def copyChildren(self, other):
        upcastSelf = self
        returnValue = libpanda._inPnJyohfED(upcastSelf.this, other.this)
        return returnValue

    
    def _MouseWatcher__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(self, attrib, override):
        upcastSelf = self
        returnValue = libpanda._inPnJyo48Bd(upcastSelf.this, attrib.this, override)
        return returnValue

    
    def _MouseWatcher__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(self, attrib):
        upcastSelf = self
        returnValue = libpanda._inPnJyoDD5k(upcastSelf.this, attrib.this)
        return returnValue

    
    def getAttrib(self, type):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyo2W_P(upcastSelf.this, type.this)
        return returnValue

    
    def clearAttrib(self, type):
        upcastSelf = self
        returnValue = libpanda._inPnJyoDSEu(upcastSelf.this, type.this)
        return returnValue

    
    def setEffect(self, effect):
        upcastSelf = self
        returnValue = libpanda._inPnJyoKWvI(upcastSelf.this, effect.this)
        return returnValue

    
    def getEffect(self, type):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyoI1nr(upcastSelf.this, type.this)
        return returnValue

    
    def clearEffect(self, type):
        upcastSelf = self
        returnValue = libpanda._inPnJyoNUJ2(upcastSelf.this, type.this)
        return returnValue

    
    def setState(self, state):
        upcastSelf = self
        returnValue = libpanda._inPnJyoGDjV(upcastSelf.this, state.this)
        return returnValue

    
    def getState(self):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyotySF(upcastSelf.this)
        return returnValue

    
    def setEffects(self, effects):
        upcastSelf = self
        returnValue = libpanda._inPnJyoxlpj(upcastSelf.this, effects.this)
        return returnValue

    
    def getEffects(self):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyo6yPH(upcastSelf.this)
        return returnValue

    
    def setTransform(self, transform):
        upcastSelf = self
        returnValue = libpanda._inPnJyo55Ti(upcastSelf.this, transform.this)
        return returnValue

    
    def getTransform(self):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyoEjK_(upcastSelf.this)
        return returnValue

    
    def setPrevTransform(self, transform):
        upcastSelf = self
        returnValue = libpanda._inPnJyo_3nJ(upcastSelf.this, transform.this)
        return returnValue

    
    def getPrevTransform(self):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyoGfcO(upcastSelf.this)
        return returnValue

    
    def setTag(self, key, value):
        upcastSelf = self
        returnValue = libpanda._inPnJyoTNEJ(upcastSelf.this, key, value)
        return returnValue

    
    def getTag(self, key):
        upcastSelf = self
        returnValue = libpanda._inPnJyo5tVl(upcastSelf.this, key)
        return returnValue

    
    def hasTag(self, key):
        upcastSelf = self
        returnValue = libpanda._inPnJyote2r(upcastSelf.this, key)
        return returnValue

    
    def clearTag(self, key):
        upcastSelf = self
        returnValue = libpanda._inPnJyoiRPE(upcastSelf.this, key)
        return returnValue

    
    def copyTags(self, other):
        upcastSelf = self
        returnValue = libpanda._inPnJyoxMQi(upcastSelf.this, other.this)
        return returnValue

    
    def _MouseWatcher__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(self, out, separator):
        upcastSelf = self
        returnValue = libpanda._inPnJyo3itg(upcastSelf.this, out.this, separator)
        return returnValue

    
    def _MouseWatcher__overloaded_listTags_ptrConstPandaNode_ptrOstream(self, out):
        upcastSelf = self
        returnValue = libpanda._inPnJyocRES(upcastSelf.this, out.this)
        return returnValue

    
    def setDrawMask(self, mask):
        upcastSelf = self
        returnValue = libpanda._inPnJyofzL6(upcastSelf.this, mask.this)
        return returnValue

    
    def getDrawMask(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoWJXI(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setIntoCollideMask(self, mask):
        upcastSelf = self
        returnValue = libpanda._inPnJyoK9VT(upcastSelf.this, mask.this)
        return returnValue

    
    def getIntoCollideMask(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyoc3Cf(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getLegalCollideMask(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyotnOA(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNetCollideMask(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyo4l_T(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        upcastSelf = self
        returnValue = libpanda._inPnJyoW23T(upcastSelf.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        upcastSelf = self
        returnValue = libpanda._inPnJyoSz8K(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def ls(self, out, indentLevel):
        upcastSelf = self
        returnValue = libpanda._inPnJyopBSg(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def _MouseWatcher__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        returnValue = libpanda._inPnJyomd5g(upcastSelf.this, type)
        return returnValue

    
    def _MouseWatcher__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        returnValue = libpanda._inPnJyo4Bq1(upcastSelf.this, volume.this)
        return returnValue

    
    def getBound(self):
        upcastSelf = self
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
        returnValue = libpanda._inPnJyoxAx3(upcastSelf.this)
        return returnValue

    
    def isLodNode(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyohW8z(upcastSelf.this)
        return returnValue

    
    def asLight(self):
        upcastSelf = self
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
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._MouseWatcher__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(*_args)
            
            import BoundingVolume
            if isinstance(_args[0], BoundingVolume.BoundingVolume):
                return self._MouseWatcher__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._MouseWatcher__overloaded_addChild_ptrPandaNode_ptrPandaNode(*_args)
        elif numArgs == 2:
            return self._MouseWatcher__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def unstashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._MouseWatcher__overloaded_unstashChild_ptrPandaNode_int(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._MouseWatcher__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def listTags(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._MouseWatcher__overloaded_listTags_ptrConstPandaNode_ptrOstream(*_args)
        elif numArgs == 2:
            return self._MouseWatcher__overloaded_listTags_ptrConstPandaNode_ptrOstream_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._MouseWatcher__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(*_args)
        elif numArgs == 2:
            return self._MouseWatcher__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def stashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._MouseWatcher__overloaded_stashChild_ptrPandaNode_int(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._MouseWatcher__overloaded_stashChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def removeChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._MouseWatcher__overloaded_removeChild_ptrPandaNode_int(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._MouseWatcher__overloaded_removeChild_ptrPandaNode_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addStashed(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._MouseWatcher__overloaded_addStashed_ptrPandaNode_ptrPandaNode(*_args)
        elif numArgs == 2:
            return self._MouseWatcher__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def upcastToNamable(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyojprb(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToBoundedObject(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyo7YS5(upcastSelf.this)
        import BoundedObject
        returnObject = BoundedObject.BoundedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpanda._inPnJyogdrc(upcastSelf.this)
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

    
    def addRegion(self, region):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        returnValue = libpanda._inPyiw5xUMA(upcastSelf.this, region.this)
        return returnValue

    
    def hasRegion(self, region):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        returnValue = libpanda._inPyiw575tC(upcastSelf.this, region.this)
        return returnValue

    
    def findRegion(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        returnValue = libpanda._inPyiw52SzS(upcastSelf.this, name)
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
        returnValue = libpanda._inPyiw59D_y(upcastSelf.this)
        return returnValue

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        returnValue = libpanda._inPyiw5XWnS(upcastSelf.this)
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
        returnValue = libpandaexpress._inPKoxtP11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtaS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtwyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToMouseWatcherGroup()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtvpj2(upcastSelf.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._MouseWatcher__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._MouseWatcher__overloaded_constructor_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getOverRegion(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher(*_args)
        elif numArgs == 1:
            return self._MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher_ptrConstLPoint2f(*_args)
        elif numArgs == 2:
            return self._MouseWatcher__overloaded_getOverRegion_ptrConstMouseWatcher_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def isOverRegion(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher(*_args)
        elif numArgs == 1:
            return self._MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher_ptrConstLPoint2f(*_args)
        elif numArgs == 2:
            return self._MouseWatcher__overloaded_isOverRegion_ptrConstMouseWatcher_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


