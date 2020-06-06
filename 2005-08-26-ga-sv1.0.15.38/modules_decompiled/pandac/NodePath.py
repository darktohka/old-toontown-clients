# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class NodePath(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    ETRemoved = 2
    ETNotFound = 1
    ETOk = 0
    ETFail = 3
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _NodePath__overloaded_constructor(self):
        self.this = libpanda._inPnJyodx9g()
        self.userManagesMemory = 1

    
    def _NodePath__overloaded_constructor_ptrConstNodePath(self, copy):
        self.this = libpanda._inPnJyoJaJj(copy.this)
        self.userManagesMemory = 1

    
    def _NodePath__overloaded_constructor_ptrConstNodePath_ptrPandaNode(self, parent, childNode):
        self.this = libpanda._inPnJyonAhm(parent.this, childNode.this)
        self.userManagesMemory = 1

    
    def _NodePath__overloaded_constructor_ptrPandaNode(self, node):
        self.this = libpanda._inPnJyoH4wM(node.this)
        self.userManagesMemory = 1

    
    def _NodePath__overloaded_constructor_atomicstring(self, topNodeName):
        self.this = libpanda._inPnJyoH_EQ(topNodeName)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoeXq7:
            libpanda._inPnJyoeXq7(self.this)
        

    
    def anyPath(node):
        returnValue = libpanda._inPnJyooGNf(node.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    anyPath = staticmethod(anyPath)
    
    def notFound():
        returnValue = libpanda._inPnJyoH6GR()
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    notFound = staticmethod(notFound)
    
    def removed():
        returnValue = libpanda._inPnJyocqkY()
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    removed = staticmethod(removed)
    
    def fail():
        returnValue = libpanda._inPnJyoKvgx()
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    fail = staticmethod(fail)
    
    def setMaxSearchDepth(maxSearchDepth):
        returnValue = libpanda._inPnJyoF4FI(maxSearchDepth)
        return returnValue

    setMaxSearchDepth = staticmethod(setMaxSearchDepth)
    
    def getMaxSearchDepth():
        returnValue = libpanda._inPnJyojBwf()
        return returnValue

    getMaxSearchDepth = staticmethod(getMaxSearchDepth)
    
    def getClassType():
        returnValue = libpanda._inPnJyot3wh()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpanda._inPnJyorj60(self.this, copy.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isEmpty(self):
        returnValue = libpanda._inPnJyo6BVO(self.this)
        return returnValue

    
    def isSingleton(self):
        returnValue = libpanda._inPnJyonHP3(self.this)
        return returnValue

    
    def getNumNodes(self):
        returnValue = libpanda._inPnJyoMbn0(self.this)
        return returnValue

    
    def getNode(self, index):
        returnValue = libpanda._inPnJyo5Kz9(self.this, index)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getErrorType(self):
        returnValue = libpanda._inPnJyo17Vc(self.this)
        return returnValue

    
    def getTopNode(self):
        returnValue = libpanda._inPnJyoCGOI(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getTop(self):
        returnValue = libpanda._inPnJyoHiQF(self.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def node(self):
        returnValue = libpanda._inPnJyoC92U(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getKey(self):
        returnValue = libpanda._inPnJyoumo_(self.this)
        return returnValue

    
    def isSameGraph(self, other):
        returnValue = libpanda._inPnJyoRlGb(self.this, other.this)
        return returnValue

    
    def getChildren(self):
        returnValue = libpanda._inPnJyogb8V(self.this)
        import NodePathCollection
        returnObject = NodePathCollection.NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumChildren(self):
        returnValue = libpanda._inPnJyoSTCh(self.this)
        return returnValue

    
    def getChild(self, n):
        returnValue = libpanda._inPnJyoaFtX(self.this, n)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getStashedChildren(self):
        returnValue = libpanda._inPnJyowedS(self.this)
        import NodePathCollection
        returnObject = NodePathCollection.NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasParent(self):
        returnValue = libpanda._inPnJyohc1w(self.this)
        return returnValue

    
    def getParent(self):
        returnValue = libpanda._inPnJyoDcoI(self.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getSort(self):
        returnValue = libpanda._inPnJyoFeVI(self.this)
        return returnValue

    
    def find(self, path):
        returnValue = libpanda._inPnJyoO9_b(self.this, path)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findPathTo(self, node):
        returnValue = libpanda._inPnJyoQFrr(self.this, node.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findAllMatches(self, path):
        returnValue = libpanda._inPnJyoupHP(self.this, path)
        import NodePathCollection
        returnObject = NodePathCollection.NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findAllPathsTo(self, node):
        returnValue = libpanda._inPnJyoO6Sn(self.this, node.this)
        import NodePathCollection
        returnObject = NodePathCollection.NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_reparentTo_ptrNodePath_ptrConstNodePath_int(self, other, sort):
        returnValue = libpanda._inPnJyo4WHK(self.this, other.this, sort)
        return returnValue

    
    def _NodePath__overloaded_reparentTo_ptrNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyozsyP(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath_int(self, other, sort):
        returnValue = libpanda._inPnJyoln7s(self.this, other.this, sort)
        return returnValue

    
    def _NodePath__overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyowFTN(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath_int(self, other, sort):
        returnValue = libpanda._inPnJyo2Mo6(self.this, other.this, sort)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoTlPD(self.this, other.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_instanceUnderNode_ptrConstNodePath_ptrConstNodePath_atomicstring_int(self, other, name, sort):
        returnValue = libpanda._inPnJyoHSFZ(self.this, other.this, name, sort)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_instanceUnderNode_ptrConstNodePath_ptrConstNodePath_atomicstring(self, other, name):
        returnValue = libpanda._inPnJyofsm_(self.this, other.this, name)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_copyTo_ptrConstNodePath_ptrConstNodePath_int(self, other, sort):
        returnValue = libpanda._inPnJyoxTlc(self.this, other.this, sort)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_copyTo_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyotI_l(self.this, other.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_attachNewNode_ptrConstNodePath_ptrPandaNode_int(self, node, sort):
        returnValue = libpanda._inPnJyonUwe(self.this, node.this, sort)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_attachNewNode_ptrConstNodePath_ptrPandaNode(self, node):
        returnValue = libpanda._inPnJyo9EWP(self.this, node.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_attachNewNode_ptrConstNodePath_atomicstring_int(self, name, sort):
        returnValue = libpanda._inPnJyolodl(self.this, name, sort)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_attachNewNode_ptrConstNodePath_atomicstring(self, name):
        returnValue = libpanda._inPnJyo8rj7(self.this, name)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def removeNode(self):
        returnValue = libpanda._inPnJyoliuR(self.this)
        return returnValue

    
    def detachNode(self):
        returnValue = libpanda._inPnJyogfzy(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPnJyooCbM(self.this, out.this)
        return returnValue

    
    def _NodePath__overloaded_ls_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyovoLL(self.this)
        return returnValue

    
    def _NodePath__overloaded_ls_ptrConstNodePath_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPnJyo1zyE(self.this, out.this, indentLevel)
        return returnValue

    
    def _NodePath__overloaded_ls_ptrConstNodePath_ptrOstream(self, out):
        returnValue = libpanda._inPnJyou02a(self.this, out.this)
        return returnValue

    
    def _NodePath__overloaded_reverseLs_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoh7pG(self.this)
        return returnValue

    
    def _NodePath__overloaded_reverseLs_ptrConstNodePath_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPnJyotiSZ(self.this, out.this, indentLevel)
        return returnValue

    
    def _NodePath__overloaded_reverseLs_ptrConstNodePath_ptrOstream(self, out):
        returnValue = libpanda._inPnJyo4b6h(self.this, out.this)
        return returnValue

    
    def _NodePath__overloaded_getState_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoMd52(self.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_getState_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyou5LY(self.this, other.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setState_ptrNodePath_ptrConstNodePath_ptrConstRenderState(self, other, state):
        returnValue = libpanda._inPnJyoojNF(self.this, other.this, state.this)
        return returnValue

    
    def _NodePath__overloaded_setState_ptrNodePath_ptrConstRenderState(self, state):
        returnValue = libpanda._inPnJyoYTbI(self.this, state.this)
        return returnValue

    
    def getNetState(self):
        returnValue = libpanda._inPnJyoxk0S(self.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_getTransform_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyobFez(self.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_getTransform_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyo25iF(self.this, other.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_clearTransform_ptrNodePath(self):
        returnValue = libpanda._inPnJyoH5x7(self.this)
        return returnValue

    
    def _NodePath__overloaded_clearTransform_ptrNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoQssv(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_setTransform_ptrNodePath_ptrConstNodePath_ptrConstTransformState(self, other, transform):
        returnValue = libpanda._inPnJyoOC4G(self.this, other.this, transform.this)
        return returnValue

    
    def _NodePath__overloaded_setTransform_ptrNodePath_ptrConstTransformState(self, transform):
        returnValue = libpanda._inPnJyoOl1c(self.this, transform.this)
        return returnValue

    
    def getNetTransform(self):
        returnValue = libpanda._inPnJyodCm_(self.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_getPrevTransform_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoaXOe(self.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_getPrevTransform_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoIeYC(self.this, other.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setPrevTransform_ptrNodePath_ptrConstNodePath_ptrConstTransformState(self, other, transform):
        returnValue = libpanda._inPnJyoKELE(self.this, other.this, transform.this)
        return returnValue

    
    def _NodePath__overloaded_setPrevTransform_ptrNodePath_ptrConstTransformState(self, transform):
        returnValue = libpanda._inPnJyogmBw(self.this, transform.this)
        return returnValue

    
    def getNetPrevTransform(self):
        returnValue = libpanda._inPnJyoq_Pd(self.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setPos_ptrNodePath_ptrConstLVecBase3f(self, pos):
        returnValue = libpanda._inPnJyotVV9(self.this, pos.this)
        return returnValue

    
    def _NodePath__overloaded_setPos_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, pos):
        returnValue = libpanda._inPnJyowgot(self.this, other.this, pos.this)
        return returnValue

    
    def _NodePath__overloaded_setPos_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
        returnValue = libpanda._inPnJyo0iUk(self.this, other.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_setPos_ptrNodePath_float_float_float(self, x, y, z):
        returnValue = libpanda._inPnJyoc4_K(self.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_setX_ptrNodePath_ptrConstNodePath_float(self, other, x):
        returnValue = libpanda._inPnJyoQez_(self.this, other.this, x)
        return returnValue

    
    def _NodePath__overloaded_setX_ptrNodePath_float(self, x):
        returnValue = libpanda._inPnJyodaZh(self.this, x)
        return returnValue

    
    def _NodePath__overloaded_setY_ptrNodePath_ptrConstNodePath_float(self, other, y):
        returnValue = libpanda._inPnJyoyKzv(self.this, other.this, y)
        return returnValue

    
    def _NodePath__overloaded_setY_ptrNodePath_float(self, y):
        returnValue = libpanda._inPnJyo2gZR(self.this, y)
        return returnValue

    
    def _NodePath__overloaded_setZ_ptrNodePath_ptrConstNodePath_float(self, other, z):
        returnValue = libpanda._inPnJyoU5zf(self.this, other.this, z)
        return returnValue

    
    def _NodePath__overloaded_setZ_ptrNodePath_float(self, z):
        returnValue = libpanda._inPnJyoYzZB(self.this, z)
        return returnValue

    
    def _NodePath__overloaded_setFluidPos_ptrNodePath_ptrConstLVecBase3f(self, pos):
        returnValue = libpanda._inPnJyoiI31(self.this, pos.this)
        return returnValue

    
    def _NodePath__overloaded_setFluidPos_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, pos):
        returnValue = libpanda._inPnJyoQamK(self.this, other.this, pos.this)
        return returnValue

    
    def _NodePath__overloaded_setFluidPos_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
        returnValue = libpanda._inPnJyojpk5(self.this, other.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_setFluidPos_ptrNodePath_float_float_float(self, x, y, z):
        returnValue = libpanda._inPnJyoDckh(self.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_setFluidX_ptrNodePath_ptrConstNodePath_float(self, other, x):
        returnValue = libpanda._inPnJyomNMV(self.this, other.this, x)
        return returnValue

    
    def _NodePath__overloaded_setFluidX_ptrNodePath_float(self, x):
        returnValue = libpanda._inPnJyoFku5(self.this, x)
        return returnValue

    
    def _NodePath__overloaded_setFluidY_ptrNodePath_ptrConstNodePath_float(self, other, y):
        returnValue = libpanda._inPnJyoWvfV(self.this, other.this, y)
        return returnValue

    
    def _NodePath__overloaded_setFluidY_ptrNodePath_float(self, y):
        returnValue = libpanda._inPnJyoVKB6(self.this, y)
        return returnValue

    
    def _NodePath__overloaded_setFluidZ_ptrNodePath_ptrConstNodePath_float(self, other, z):
        returnValue = libpanda._inPnJyoGBzV(self.this, other.this, z)
        return returnValue

    
    def _NodePath__overloaded_setFluidZ_ptrNodePath_float(self, z):
        returnValue = libpanda._inPnJyolrV6(self.this, z)
        return returnValue

    
    def _NodePath__overloaded_getPos_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoOo4T(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getPos_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoCfLu(self.this, other.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getX_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyo0lol(self.this)
        return returnValue

    
    def _NodePath__overloaded_getX_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyosQU6(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getY_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoaSpV(self.this)
        return returnValue

    
    def _NodePath__overloaded_getY_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoKEUq(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getZ_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoxcoF(self.this)
        return returnValue

    
    def _NodePath__overloaded_getZ_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoo5Ua(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getPosDelta_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyodM8H(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getPosDelta_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyojYBa(self.this, other.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_setHpr_ptrNodePath_ptrConstLVecBase3f(self, hpr):
        returnValue = libpanda._inPnJyoHdk4(self.this, hpr.this)
        return returnValue

    
    def _NodePath__overloaded_setHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, hpr):
        returnValue = libpanda._inPnJyoOo3o(self.this, other.this, hpr.this)
        return returnValue

    
    def _NodePath__overloaded_setHpr_ptrNodePath_ptrConstNodePath_float_float_float(self, other, h, p, r):
        returnValue = libpanda._inPnJyoablf(self.this, other.this, h, p, r)
        return returnValue

    
    def _NodePath__overloaded_setHpr_ptrNodePath_float_float_float(self, h, p, r):
        returnValue = libpanda._inPnJyoGhOG(self.this, h, p, r)
        return returnValue

    
    def _NodePath__overloaded_setH_ptrNodePath_ptrConstNodePath_float(self, other, h):
        returnValue = libpanda._inPnJyo0Wu_(self.this, other.this, h)
        return returnValue

    
    def _NodePath__overloaded_setH_ptrNodePath_float(self, h):
        returnValue = libpanda._inPnJyo5SUh(self.this, h)
        return returnValue

    
    def _NodePath__overloaded_setP_ptrNodePath_ptrConstNodePath_float(self, other, p):
        returnValue = libpanda._inPnJyoCyw_(self.this, other.this, p)
        return returnValue

    
    def _NodePath__overloaded_setP_ptrNodePath_float(self, p):
        returnValue = libpanda._inPnJyov_Xh(self.this, p)
        return returnValue

    
    def _NodePath__overloaded_setR_ptrNodePath_ptrConstNodePath_float(self, other, r):
        returnValue = libpanda._inPnJyoGVwf(self.this, other.this, r)
        return returnValue

    
    def _NodePath__overloaded_setR_ptrNodePath_float(self, r):
        returnValue = libpanda._inPnJyoqXXB(self.this, r)
        return returnValue

    
    def _NodePath__overloaded_getHpr_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyokhJP(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getHpr_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoYUap(self.this, other.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getH_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoQtjl(self.this)
        return returnValue

    
    def _NodePath__overloaded_getH_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoAZP6(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getP_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoCJll(self.this)
        return returnValue

    
    def _NodePath__overloaded_getP_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoS1R6(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getR_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoHwlF(self.this)
        return returnValue

    
    def _NodePath__overloaded_getR_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoWcRa(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_setQuat_ptrNodePath_ptrConstLQuaternionf(self, quat):
        returnValue = libpanda._inPnJyowJgI(self.this, quat.this)
        return returnValue

    
    def _NodePath__overloaded_setQuat_ptrNodePath_ptrConstNodePath_ptrConstLQuaternionf(self, other, quat):
        returnValue = libpanda._inPnJyoKI60(self.this, other.this, quat.this)
        return returnValue

    
    def _NodePath__overloaded_getQuat_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyowDPW(self.this)
        import Quat
        returnObject = Quat.Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getQuat_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoCURf(self.this, other.this)
        import Quat
        returnObject = Quat.Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_setScale_ptrNodePath_ptrConstLVecBase3f(self, scale):
        returnValue = libpanda._inPnJyoZaRp(self.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, scale):
        returnValue = libpanda._inPnJyopef1(self.this, other.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setScale_ptrNodePath_ptrConstNodePath_float(self, other, scale):
        returnValue = libpanda._inPnJyo_9Ct(self.this, other.this, scale)
        return returnValue

    
    def _NodePath__overloaded_setScale_ptrNodePath_ptrConstNodePath_float_float_float(self, other, sx, sy, sz):
        returnValue = libpanda._inPnJyoxK_k(self.this, other.this, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setScale_ptrNodePath_float(self, scale):
        returnValue = libpanda._inPnJyotTLn(self.this, scale)
        return returnValue

    
    def _NodePath__overloaded_setScale_ptrNodePath_float_float_float(self, sx, sy, sz):
        returnValue = libpanda._inPnJyoNsGl(self.this, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setSx_ptrNodePath_ptrConstNodePath_float(self, other, sx):
        returnValue = libpanda._inPnJyooi3_(self.this, other.this, sx)
        return returnValue

    
    def _NodePath__overloaded_setSx_ptrNodePath_float(self, sx):
        returnValue = libpanda._inPnJyoEtIx(self.this, sx)
        return returnValue

    
    def _NodePath__overloaded_setSy_ptrNodePath_ptrConstNodePath_float(self, other, sy):
        returnValue = libpanda._inPnJyogVB_(self.this, other.this, sy)
        return returnValue

    
    def _NodePath__overloaded_setSy_ptrNodePath_float(self, sy):
        returnValue = libpanda._inPnJyocaRx(self.this, sy)
        return returnValue

    
    def _NodePath__overloaded_setSz_ptrNodePath_ptrConstNodePath_float(self, other, sz):
        returnValue = libpanda._inPnJyo4EL_(self.this, other.this, sz)
        return returnValue

    
    def _NodePath__overloaded_setSz_ptrNodePath_float(self, sz):
        returnValue = libpanda._inPnJyoULbx(self.this, sz)
        return returnValue

    
    def _NodePath__overloaded_getScale_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyo5djS(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getScale_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoam1z(self.this, other.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getSx_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyon63U(self.this)
        return returnValue

    
    def _NodePath__overloaded_getSx_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoCXrr(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getSy_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyovrBV(self.this)
        return returnValue

    
    def _NodePath__overloaded_getSy_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoKE1r(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getSz_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoXULV(self.this)
        return returnValue

    
    def _NodePath__overloaded_getSz_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoS18r(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_setShear_ptrNodePath_ptrConstLVecBase3f(self, shear):
        returnValue = libpanda._inPnJyosuKi(self.this, shear.this)
        return returnValue

    
    def _NodePath__overloaded_setShear_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, shear):
        returnValue = libpanda._inPnJyoiMYu(self.this, other.this, shear.this)
        return returnValue

    
    def _NodePath__overloaded_setShear_ptrNodePath_ptrConstNodePath_float_float_float(self, other, shxy, shxz, shyz):
        returnValue = libpanda._inPnJyoOe2d(self.this, other.this, shxy, shxz, shyz)
        return returnValue

    
    def _NodePath__overloaded_setShear_ptrNodePath_float_float_float(self, shxy, shxz, shyz):
        returnValue = libpanda._inPnJyofHAe(self.this, shxy, shxz, shyz)
        return returnValue

    
    def _NodePath__overloaded_setShxy_ptrNodePath_ptrConstNodePath_float(self, other, shxy):
        returnValue = libpanda._inPnJyoUJVV(self.this, other.this, shxy)
        return returnValue

    
    def _NodePath__overloaded_setShxy_ptrNodePath_float(self, shxy):
        returnValue = libpanda._inPnJyo7PKV(self.this, shxy)
        return returnValue

    
    def _NodePath__overloaded_setShxz_ptrNodePath_ptrConstNodePath_float(self, other, shxz):
        returnValue = libpanda._inPnJyoaJjx(self.this, other.this, shxz)
        return returnValue

    
    def _NodePath__overloaded_setShxz_ptrNodePath_float(self, shxz):
        returnValue = libpanda._inPnJyolPYx(self.this, shxz)
        return returnValue

    
    def _NodePath__overloaded_setShyz_ptrNodePath_ptrConstNodePath_float(self, other, shyz):
        returnValue = libpanda._inPnJyoatc2(self.this, other.this, shyz)
        return returnValue

    
    def _NodePath__overloaded_setShyz_ptrNodePath_float(self, shyz):
        returnValue = libpanda._inPnJyolrR2(self.this, shyz)
        return returnValue

    
    def _NodePath__overloaded_getShear_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoyRcL(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getShear_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoXxss(self.this, other.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getShxy_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyo5jpx(self.this)
        return returnValue

    
    def _NodePath__overloaded_getShxy_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyobLq6(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getShxz_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyo8j3N(self.this)
        return returnValue

    
    def _NodePath__overloaded_getShxz_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoWL4W(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getShyz_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyo8PuS(self.this)
        return returnValue

    
    def _NodePath__overloaded_getShyz_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyoWXwb(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(self, pos, hpr):
        returnValue = libpanda._inPnJyo_KIO(self.this, pos.this, hpr.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other, pos, hpr):
        returnValue = libpanda._inPnJyobgSC(self.this, other.this, pos.this, hpr.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float(self, other, x, y, z, h, p, r):
        returnValue = libpanda._inPnJyohbI1(self.this, other.this, x, y, z, h, p, r)
        return returnValue

    
    def _NodePath__overloaded_setPosHpr_ptrNodePath_float_float_float_float_float_float(self, x, y, z, h, p, r):
        returnValue = libpanda._inPnJyoFbxa(self.this, x, y, z, h, p, r)
        return returnValue

    
    def _NodePath__overloaded_setPosQuat_ptrNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf(self, pos, quat):
        returnValue = libpanda._inPnJyoPEZ1(self.this, pos.this, quat.this)
        return returnValue

    
    def _NodePath__overloaded_setPosQuat_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf(self, other, pos, quat):
        returnValue = libpanda._inPnJyogdNI(self.this, other.this, pos.this, quat.this)
        return returnValue

    
    def _NodePath__overloaded_setHprScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(self, hpr, scale):
        returnValue = libpanda._inPnJyoeWuA(self.this, hpr.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setHprScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other, hpr, scale):
        returnValue = libpanda._inPnJyoTEr7(self.this, other.this, hpr.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setHprScale_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float(self, other, h, p, r, sx, sy, sz):
        returnValue = libpanda._inPnJyo4kfC(self.this, other.this, h, p, r, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setHprScale_ptrNodePath_float_float_float_float_float_float(self, h, p, r, sx, sy, sz):
        returnValue = libpanda._inPnJyoWIYi(self.this, h, p, r, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setQuatScale_ptrNodePath_ptrConstLQuaternionf_ptrConstLVecBase3f(self, quat, scale):
        returnValue = libpanda._inPnJyoxukU(self.this, quat.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setQuatScale_ptrNodePath_ptrConstNodePath_ptrConstLQuaternionf_ptrConstLVecBase3f(self, other, quat, scale):
        returnValue = libpanda._inPnJyo9poi(self.this, other.this, quat.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(self, pos, hpr, scale):
        returnValue = libpanda._inPnJyoWLWQ(self.this, pos.this, hpr.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other, pos, hpr, scale):
        returnValue = libpanda._inPnJyo6XbK(self.this, other.this, pos.this, hpr.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float_float_float_float(self, other, x, y, z, h, p, r, sx, sy, sz):
        returnValue = libpanda._inPnJyoVHTJ(self.this, other.this, x, y, z, h, p, r, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setPosHprScale_ptrNodePath_float_float_float_float_float_float_float_float_float(self, x, y, z, h, p, r, sx, sy, sz):
        returnValue = libpanda._inPnJyoh3Bw(self.this, x, y, z, h, p, r, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setPosQuatScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f(self, pos, quat, scale):
        returnValue = libpanda._inPnJyolcNQ(self.this, pos.this, quat.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setPosQuatScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f(self, other, pos, quat, scale):
        returnValue = libpanda._inPnJyoAbZX(self.this, other.this, pos.this, quat.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHprScaleShear_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(self, pos, hpr, scale, shear):
        returnValue = libpanda._inPnJyo9p1n(self.this, pos.this, hpr.this, scale.this, shear.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHprScaleShear_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other, pos, hpr, scale, shear):
        returnValue = libpanda._inPnJyoyreF(self.this, other.this, pos.this, hpr.this, scale.this, shear.this)
        return returnValue

    
    def _NodePath__overloaded_setPosQuatScaleShear_ptrNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f_ptrConstLVecBase3f(self, pos, quat, scale, shear):
        returnValue = libpanda._inPnJyoFwaK(self.this, pos.this, quat.this, scale.this, shear.this)
        return returnValue

    
    def _NodePath__overloaded_setPosQuatScaleShear_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other, pos, quat, scale, shear):
        returnValue = libpanda._inPnJyoSPDh(self.this, other.this, pos.this, quat.this, scale.this, shear.this)
        return returnValue

    
    def _NodePath__overloaded_setMat_ptrNodePath_ptrConstLMatrix4f(self, mat):
        returnValue = libpanda._inPnJyo6Rbe(self.this, mat.this)
        return returnValue

    
    def _NodePath__overloaded_setMat_ptrNodePath_ptrConstNodePath_ptrConstLMatrix4f(self, other, mat):
        returnValue = libpanda._inPnJyoe6vZ(self.this, other.this, mat.this)
        return returnValue

    
    def clearMat(self):
        returnValue = libpanda._inPnJyoZ8BU(self.this)
        return returnValue

    
    def hasMat(self):
        returnValue = libpanda._inPnJyouM1u(self.this)
        return returnValue

    
    def _NodePath__overloaded_getMat_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoIMoG(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NodePath__overloaded_getMat_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyo_p5g(self.this, other.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, point, up):
        returnValue = libpanda._inPnJyovdrT(self.this, point.this, up.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstLPoint3f(self, point):
        returnValue = libpanda._inPnJyoOO_M(self.this, point.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, other, point, up):
        returnValue = libpanda._inPnJyoCkNd(self.this, other.this, point.this, up.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(self, other, point):
        returnValue = libpanda._inPnJyosdPC(self.this, other.this, point.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyo62Ls(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
        returnValue = libpanda._inPnJyoooUy(self.this, other.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_float_float_float(self, x, y, z):
        returnValue = libpanda._inPnJyoTR_Y(self.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, point, up):
        returnValue = libpanda._inPnJyo45wG(self.this, point.this, up.this)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstLPoint3f(self, point):
        returnValue = libpanda._inPnJyoK5su(self.this, point.this)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, other, point, up):
        returnValue = libpanda._inPnJyo_0_3(self.this, other.this, point.this, up.this)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(self, other, point):
        returnValue = libpanda._inPnJyo1SnX(self.this, other.this, point.this)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPnJyowIWV(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
        returnValue = libpanda._inPnJyozOob(self.this, other.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_float_float_float(self, x, y, z):
        returnValue = libpanda._inPnJyodJov(self.this, x, y, z)
        return returnValue

    
    def getRelativePoint(self, other, point):
        returnValue = libpanda._inPnJyoOttf(self.this, other.this, point.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRelativeVector(self, other, vec):
        returnValue = libpanda._inPnJyojeSO(self.this, other.this, vec.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getDistance(self, other):
        returnValue = libpanda._inPnJyogctf(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_setColor_ptrNodePath_ptrConstLVecBase4f_int(self, color, priority):
        returnValue = libpanda._inPnJyoadvm(self.this, color.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setColor_ptrNodePath_ptrConstLVecBase4f(self, color):
        returnValue = libpanda._inPnJyoV3Zs(self.this, color.this)
        return returnValue

    
    def _NodePath__overloaded_setColor_ptrNodePath_float_float_float_float_int(self, r, g, b, a, priority):
        returnValue = libpanda._inPnJyo066r(self.this, r, g, b, a, priority)
        return returnValue

    
    def _NodePath__overloaded_setColor_ptrNodePath_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPnJyoxcaQ(self.this, r, g, b, a)
        return returnValue

    
    def _NodePath__overloaded_setColor_ptrNodePath_float_float_float(self, r, g, b):
        returnValue = libpanda._inPnJyoQ4OM(self.this, r, g, b)
        return returnValue

    
    def _NodePath__overloaded_setColorOff_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPnJyow27z(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setColorOff_ptrNodePath(self):
        returnValue = libpanda._inPnJyoE1gC(self.this)
        return returnValue

    
    def clearColor(self):
        returnValue = libpanda._inPnJyo1mr9(self.this)
        return returnValue

    
    def hasColor(self):
        returnValue = libpanda._inPnJyobz4h(self.this)
        return returnValue

    
    def getColor(self):
        returnValue = libpanda._inPnJyokzr5(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasColorScale(self):
        returnValue = libpanda._inPnJyoh9q2(self.this)
        return returnValue

    
    def clearColorScale(self):
        returnValue = libpanda._inPnJyoNGLo(self.this)
        return returnValue

    
    def _NodePath__overloaded_setColorScale_ptrNodePath_ptrConstLVecBase4f_int(self, scale, priority):
        returnValue = libpanda._inPnJyo5CtZ(self.this, scale.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setColorScale_ptrNodePath_ptrConstLVecBase4f(self, scale):
        returnValue = libpanda._inPnJyoiG1C(self.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setColorScale_ptrNodePath_float_float_float_float_int(self, sx, sy, sz, sa, priority):
        returnValue = libpanda._inPnJyoO7kn(self.this, sx, sy, sz, sa, priority)
        return returnValue

    
    def _NodePath__overloaded_setColorScale_ptrNodePath_float_float_float_float(self, sx, sy, sz, sa):
        returnValue = libpanda._inPnJyoUFGH(self.this, sx, sy, sz, sa)
        return returnValue

    
    def _NodePath__overloaded_setColorScaleOff_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPnJyohzGl(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setColorScaleOff_ptrNodePath(self):
        returnValue = libpanda._inPnJyoPZ4L(self.this)
        return returnValue

    
    def _NodePath__overloaded_setAlphaScale_ptrNodePath_float_int(self, scale, priority):
        returnValue = libpanda._inPnJyor8w8(self.this, scale, priority)
        return returnValue

    
    def _NodePath__overloaded_setAlphaScale_ptrNodePath_float(self, scale):
        returnValue = libpanda._inPnJyou4Ux(self.this, scale)
        return returnValue

    
    def _NodePath__overloaded_setAllColorScale_ptrNodePath_float_int(self, scale, priority):
        returnValue = libpanda._inPnJyoFCj2(self.this, scale, priority)
        return returnValue

    
    def _NodePath__overloaded_setAllColorScale_ptrNodePath_float(self, scale):
        returnValue = libpanda._inPnJyoWf2B(self.this, scale)
        return returnValue

    
    def setSr(self, sr):
        returnValue = libpanda._inPnJyoUANw(self.this, sr)
        return returnValue

    
    def setSg(self, sg):
        returnValue = libpanda._inPnJyoMqiu(self.this, sg)
        return returnValue

    
    def setSb(self, sb):
        returnValue = libpanda._inPnJyoU_xt(self.this, sb)
        return returnValue

    
    def setSa(self, sa):
        returnValue = libpanda._inPnJyocBnt(self.this, sa)
        return returnValue

    
    def getColorScale(self):
        returnValue = libpanda._inPnJyoH9dO(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getSr(self):
        returnValue = libpanda._inPnJyoXd9T(self.this)
        return returnValue

    
    def getSg(self):
        returnValue = libpanda._inPnJyo_7RS(self.this)
        return returnValue

    
    def getSb(self):
        returnValue = libpanda._inPnJyoXPhR(self.this)
        return returnValue

    
    def getSa(self):
        returnValue = libpanda._inPnJyoveXR(self.this)
        return returnValue

    
    def _NodePath__overloaded_setLight_ptrNodePath_ptrConstNodePath_int(self, light, priority):
        returnValue = libpanda._inPnJyoOmzA(self.this, light.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setLight_ptrNodePath_ptrConstNodePath(self, light):
        returnValue = libpanda._inPnJyoVcVg(self.this, light.this)
        return returnValue

    
    def _NodePath__overloaded_setLightOff_ptrNodePath_ptrConstNodePath_int(self, light, priority):
        returnValue = libpanda._inPnJyomGGU(self.this, light.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setLightOff_ptrNodePath_ptrConstNodePath(self, light):
        returnValue = libpanda._inPnJyos0Fm(self.this, light.this)
        return returnValue

    
    def _NodePath__overloaded_setLightOff_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPnJyo3hHT(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setLightOff_ptrNodePath(self):
        returnValue = libpanda._inPnJyo8iuh(self.this)
        return returnValue

    
    def _NodePath__overloaded_clearLight_ptrNodePath(self):
        returnValue = libpanda._inPnJyo_y39(self.this)
        return returnValue

    
    def _NodePath__overloaded_clearLight_ptrNodePath_ptrConstNodePath(self, light):
        returnValue = libpanda._inPnJyoF_28(self.this, light.this)
        return returnValue

    
    def hasLight(self, light):
        returnValue = libpanda._inPnJyoLCWi(self.this, light.this)
        return returnValue

    
    def _NodePath__overloaded_hasLightOff_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoKg80(self.this)
        return returnValue

    
    def _NodePath__overloaded_hasLightOff_ptrConstNodePath_ptrConstNodePath(self, light):
        returnValue = libpanda._inPnJyo3UBH(self.this, light.this)
        return returnValue

    
    def _NodePath__overloaded_setBin_ptrNodePath_atomicstring_int_int(self, binName, drawOrder, priority):
        returnValue = libpanda._inPnJyoxqDK(self.this, binName, drawOrder, priority)
        return returnValue

    
    def _NodePath__overloaded_setBin_ptrNodePath_atomicstring_int(self, binName, drawOrder):
        returnValue = libpanda._inPnJyoZBGG(self.this, binName, drawOrder)
        return returnValue

    
    def clearBin(self):
        returnValue = libpanda._inPnJyobzEW(self.this)
        return returnValue

    
    def hasBin(self):
        returnValue = libpanda._inPnJyoTmsC(self.this)
        return returnValue

    
    def getBinName(self):
        returnValue = libpanda._inPnJyoLAFg(self.this)
        return returnValue

    
    def getBinDrawOrder(self):
        returnValue = libpanda._inPnJyo2Nw9(self.this)
        return returnValue

    
    def _NodePath__overloaded_setTexture_ptrNodePath_ptrTexture_int(self, tex, priority):
        returnValue = libpanda._inPnJyoFEvx(self.this, tex.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setTexture_ptrNodePath_ptrTexture(self, tex):
        returnValue = libpanda._inPnJyochTm(self.this, tex.this)
        return returnValue

    
    def _NodePath__overloaded_setTexture_ptrNodePath_ptrTextureStage_ptrTexture_int(self, stage, tex, priority):
        returnValue = libpanda._inPnJyogM3e(self.this, stage.this, tex.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setTexture_ptrNodePath_ptrTextureStage_ptrTexture(self, stage, tex):
        returnValue = libpanda._inPnJyotHou(self.this, stage.this, tex.this)
        return returnValue

    
    def _NodePath__overloaded_setTextureOff_ptrNodePath_ptrTextureStage_int(self, stage, priority):
        returnValue = libpanda._inPnJyoHq1d(self.this, stage.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setTextureOff_ptrNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyowSb0(self.this, stage.this)
        return returnValue

    
    def _NodePath__overloaded_setTextureOff_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPnJyow4bU(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setTextureOff_ptrNodePath(self):
        returnValue = libpanda._inPnJyo_4vA(self.this)
        return returnValue

    
    def _NodePath__overloaded_clearTexture_ptrNodePath(self):
        returnValue = libpanda._inPnJyoNNBp(self.this)
        return returnValue

    
    def _NodePath__overloaded_clearTexture_ptrNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyocr3x(self.this, stage.this)
        return returnValue

    
    def _NodePath__overloaded_hasTexture_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoqlwf(self.this)
        return returnValue

    
    def _NodePath__overloaded_hasTexture_ptrConstNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyoCNaQ(self.this, stage.this)
        return returnValue

    
    def _NodePath__overloaded_hasTextureOff_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoxE64(self.this)
        return returnValue

    
    def _NodePath__overloaded_hasTextureOff_ptrConstNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyoL45P(self.this, stage.this)
        return returnValue

    
    def _NodePath__overloaded_getTexture_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoPll3(self.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_getTexture_ptrConstNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyohMNo(self.this, stage.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setTexTransform_ptrNodePath_ptrConstNodePath_ptrTextureStage_ptrConstTransformState(self, other, stage, transform):
        returnValue = libpanda._inPnJyoM5dH(self.this, other.this, stage.this, transform.this)
        return returnValue

    
    def _NodePath__overloaded_setTexTransform_ptrNodePath_ptrTextureStage_ptrConstTransformState(self, stage, transform):
        returnValue = libpanda._inPnJyo7rVh(self.this, stage.this, transform.this)
        return returnValue

    
    def _NodePath__overloaded_clearTexTransform_ptrNodePath(self):
        returnValue = libpanda._inPnJyoPvbV(self.this)
        return returnValue

    
    def _NodePath__overloaded_clearTexTransform_ptrNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyo7hmM(self.this, stage.this)
        return returnValue

    
    def hasTexTransform(self, stage):
        returnValue = libpanda._inPnJyoW20G(self.this, stage.this)
        return returnValue

    
    def _NodePath__overloaded_getTexTransform_ptrConstNodePath_ptrConstNodePath_ptrTextureStage(self, other, stage):
        returnValue = libpanda._inPnJyokXI_(self.this, other.this, stage.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_getTexTransform_ptrConstNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyoz2ne(self.this, stage.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setTexOffset_ptrNodePath_ptrConstNodePath_ptrTextureStage_ptrConstLVecBase2f(self, other, stage, uv):
        returnValue = libpanda._inPnJyodjnO(self.this, other.this, stage.this, uv.this)
        return returnValue

    
    def _NodePath__overloaded_setTexOffset_ptrNodePath_ptrConstNodePath_ptrTextureStage_float_float(self, other, stage, u, v):
        returnValue = libpanda._inPnJyowlj_(self.this, other.this, stage.this, u, v)
        return returnValue

    
    def _NodePath__overloaded_setTexOffset_ptrNodePath_ptrTextureStage_ptrConstLVecBase2f(self, stage, uv):
        returnValue = libpanda._inPnJyoD4GX(self.this, stage.this, uv.this)
        return returnValue

    
    def _NodePath__overloaded_setTexOffset_ptrNodePath_ptrTextureStage_float_float(self, stage, u, v):
        returnValue = libpanda._inPnJyoO2Fz(self.this, stage.this, u, v)
        return returnValue

    
    def _NodePath__overloaded_setTexRotate_ptrNodePath_ptrConstNodePath_ptrTextureStage_float(self, other, stage, r):
        returnValue = libpanda._inPnJyoa1iX(self.this, other.this, stage.this, r)
        return returnValue

    
    def _NodePath__overloaded_setTexRotate_ptrNodePath_ptrTextureStage_float(self, stage, r):
        returnValue = libpanda._inPnJyoTo9d(self.this, stage.this, r)
        return returnValue

    
    def _NodePath__overloaded_setTexScale_ptrNodePath_ptrConstNodePath_ptrTextureStage_ptrConstLVecBase2f(self, other, stage, scale):
        returnValue = libpanda._inPnJyoKMt1(self.this, other.this, stage.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setTexScale_ptrNodePath_ptrConstNodePath_ptrTextureStage_float_float(self, other, stage, su, sv):
        returnValue = libpanda._inPnJyom0Lh(self.this, other.this, stage.this, su, sv)
        return returnValue

    
    def _NodePath__overloaded_setTexScale_ptrNodePath_ptrTextureStage_ptrConstLVecBase2f(self, stage, scale):
        returnValue = libpanda._inPnJyoNnAk(self.this, stage.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setTexScale_ptrNodePath_ptrTextureStage_float_float(self, stage, su, sv):
        returnValue = libpanda._inPnJyosV2O(self.this, stage.this, su, sv)
        return returnValue

    
    def _NodePath__overloaded_getTexOffset_ptrConstNodePath_ptrConstNodePath_ptrTextureStage(self, other, stage):
        returnValue = libpanda._inPnJyotMN_(self.this, other.this, stage.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getTexOffset_ptrConstNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyoOSVy(self.this, stage.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getTexRotate_ptrConstNodePath_ptrConstNodePath_ptrTextureStage(self, other, stage):
        returnValue = libpanda._inPnJyogsWE(self.this, other.this, stage.this)
        return returnValue

    
    def _NodePath__overloaded_getTexRotate_ptrConstNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyoF4f4(self.this, stage.this)
        return returnValue

    
    def _NodePath__overloaded_getTexScale_ptrConstNodePath_ptrConstNodePath_ptrTextureStage(self, other, stage):
        returnValue = libpanda._inPnJyohlUo(self.this, other.this, stage.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getTexScale_ptrConstNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyo6J_f(self.this, stage.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_setTexGen_ptrNodePath_ptrTextureStage___enum__Mode_int(self, stage, mode, priority):
        returnValue = libpanda._inPnJyorzJW(self.this, stage.this, mode, priority)
        return returnValue

    
    def _NodePath__overloaded_setTexGen_ptrNodePath_ptrTextureStage___enum__Mode(self, stage, mode):
        returnValue = libpanda._inPnJyoxyHo(self.this, stage.this, mode)
        return returnValue

    
    def _NodePath__overloaded_clearTexGen_ptrNodePath(self):
        returnValue = libpanda._inPnJyoiojB(self.this)
        return returnValue

    
    def _NodePath__overloaded_clearTexGen_ptrNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyoY_YK(self.this, stage.this)
        return returnValue

    
    def hasTexGen(self, stage):
        returnValue = libpanda._inPnJyoePbA(self.this, stage.this)
        return returnValue

    
    def getTexGen(self, stage):
        returnValue = libpanda._inPnJyo7MOY(self.this, stage.this)
        return returnValue

    
    def setTexProjector(self, stage, _from, to):
        returnValue = libpanda._inPnJyovD7f(self.this, stage.this, _from.this, to.this)
        return returnValue

    
    def _NodePath__overloaded_clearTexProjector_ptrNodePath(self):
        returnValue = libpanda._inPnJyofHQL(self.this)
        return returnValue

    
    def _NodePath__overloaded_clearTexProjector_ptrNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyoYLcC(self.this, stage.this)
        return returnValue

    
    def hasTexProjector(self, stage):
        returnValue = libpanda._inPnJyomg0n(self.this, stage.this)
        return returnValue

    
    def getTexProjectorFrom(self, stage):
        returnValue = libpanda._inPnJyoqz7d(self.this, stage.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTexProjectorTo(self, stage):
        returnValue = libpanda._inPnJyoQ1wy(self.this, stage.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def projectTexture(self, stage, tex, projector):
        returnValue = libpanda._inPnJyoyMJ7(self.this, stage.this, tex.this, projector.this)
        return returnValue

    
    def clearProjectTexture(self, stage):
        returnValue = libpanda._inPnJyofb_F(self.this, stage.this)
        return returnValue

    
    def _NodePath__overloaded_findTexture_ptrConstNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyolksv(self.this, stage.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_findTexture_ptrConstNodePath_atomicstring(self, name):
        returnValue = libpanda._inPnJyoj98A(self.this, name)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_findAllTextures_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyo_z1D(self.this)
        import TextureCollection
        returnObject = TextureCollection.TextureCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_findAllTextures_ptrConstNodePath_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyoZ8Sw(self.this, stage.this)
        import TextureCollection
        returnObject = TextureCollection.TextureCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_findAllTextures_ptrConstNodePath_atomicstring(self, name):
        returnValue = libpanda._inPnJyoEW3S(self.this, name)
        import TextureCollection
        returnObject = TextureCollection.TextureCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findTextureStage(self, name):
        returnValue = libpanda._inPnJyoLz_1(self.this, name)
        import TextureStage
        returnObject = TextureStage.TextureStage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_findAllTextureStages_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyocefu(self.this)
        import TextureStageCollection
        returnObject = TextureStageCollection.TextureStageCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_findAllTextureStages_ptrConstNodePath_atomicstring(self, name):
        returnValue = libpanda._inPnJyovG20(self.this, name)
        import TextureStageCollection
        returnObject = TextureStageCollection.TextureStageCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def unifyTextureStages(self, stage):
        returnValue = libpanda._inPnJyoPvtN(self.this, stage.this)
        return returnValue

    
    def _NodePath__overloaded_setMaterial_ptrNodePath_ptrMaterial_int(self, tex, priority):
        returnValue = libpanda._inPnJyofZam(self.this, tex.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setMaterial_ptrNodePath_ptrMaterial(self, tex):
        returnValue = libpanda._inPnJyo2Xcl(self.this, tex.this)
        return returnValue

    
    def _NodePath__overloaded_setMaterialOff_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPnJyogcpR(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setMaterialOff_ptrNodePath(self):
        returnValue = libpanda._inPnJyo_bEb(self.this)
        return returnValue

    
    def clearMaterial(self):
        returnValue = libpanda._inPnJyoBVUw(self.this)
        return returnValue

    
    def hasMaterial(self):
        returnValue = libpanda._inPnJyoV_e6(self.this)
        return returnValue

    
    def getMaterial(self):
        returnValue = libpanda._inPnJyor_RS(self.this)
        import Material
        returnObject = Material.Material(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setFog_ptrNodePath_ptrFog_int(self, fog, priority):
        returnValue = libpanda._inPnJyomIDI(self.this, fog.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setFog_ptrNodePath_ptrFog(self, fog):
        returnValue = libpanda._inPnJyovA0X(self.this, fog.this)
        return returnValue

    
    def _NodePath__overloaded_setFogOff_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPnJyo9qa5(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setFogOff_ptrNodePath(self):
        returnValue = libpanda._inPnJyofgI_(self.this)
        return returnValue

    
    def clearFog(self):
        returnValue = libpanda._inPnJyoPL5h(self.this)
        return returnValue

    
    def hasFog(self):
        returnValue = libpanda._inPnJyoJ3dh(self.this)
        return returnValue

    
    def hasFogOff(self):
        returnValue = libpanda._inPnJyoXW1z(self.this)
        return returnValue

    
    def getFog(self):
        returnValue = libpanda._inPnJyoW3Q5(self.this)
        import Fog
        returnObject = Fog.Fog(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setRenderModeWireframe_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPnJyo3mJB(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setRenderModeWireframe_ptrNodePath(self):
        returnValue = libpanda._inPnJyoE5Vy(self.this)
        return returnValue

    
    def _NodePath__overloaded_setRenderModeFilled_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPnJyoGdFx(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setRenderModeFilled_ptrNodePath(self):
        returnValue = libpanda._inPnJyoMX6K(self.this)
        return returnValue

    
    def clearRenderMode(self):
        returnValue = libpanda._inPnJyo65TZ(self.this)
        return returnValue

    
    def hasRenderMode(self):
        returnValue = libpanda._inPnJyonDaf(self.this)
        return returnValue

    
    def _NodePath__overloaded_setTwoSided_ptrNodePath_bool_int(self, twoSided, priority):
        returnValue = libpanda._inPnJyoUKd_(self.this, twoSided, priority)
        return returnValue

    
    def _NodePath__overloaded_setTwoSided_ptrNodePath_bool(self, twoSided):
        returnValue = libpanda._inPnJyo_M_e(self.this, twoSided)
        return returnValue

    
    def clearTwoSided(self):
        returnValue = libpanda._inPnJyooJBF(self.this)
        return returnValue

    
    def hasTwoSided(self):
        returnValue = libpanda._inPnJyootTb(self.this)
        return returnValue

    
    def getTwoSided(self):
        returnValue = libpanda._inPnJyoFtGz(self.this)
        return returnValue

    
    def _NodePath__overloaded_setDepthTest_ptrNodePath_bool_int(self, depthTest, priority):
        returnValue = libpanda._inPnJyoY7DP(self.this, depthTest, priority)
        return returnValue

    
    def _NodePath__overloaded_setDepthTest_ptrNodePath_bool(self, depthTest):
        returnValue = libpanda._inPnJyo2UQ_(self.this, depthTest)
        return returnValue

    
    def clearDepthTest(self):
        returnValue = libpanda._inPnJyoMMNz(self.this)
        return returnValue

    
    def hasDepthTest(self):
        returnValue = libpanda._inPnJyogl7H(self.this)
        return returnValue

    
    def getDepthTest(self):
        returnValue = libpanda._inPnJyoNiuf(self.this)
        return returnValue

    
    def _NodePath__overloaded_setDepthWrite_ptrNodePath_bool_int(self, depthWrite, priority):
        returnValue = libpanda._inPnJyorwkt(self.this, depthWrite, priority)
        return returnValue

    
    def _NodePath__overloaded_setDepthWrite_ptrNodePath_bool(self, depthWrite):
        returnValue = libpanda._inPnJyoADOz(self.this, depthWrite)
        return returnValue

    
    def clearDepthWrite(self):
        returnValue = libpanda._inPnJyowNqE(self.this)
        return returnValue

    
    def hasDepthWrite(self):
        returnValue = libpanda._inPnJyoQs8G(self.this)
        return returnValue

    
    def getDepthWrite(self):
        returnValue = libpanda._inPnJyoTsve(self.this)
        return returnValue

    
    def doBillboardAxis(self, camera, offset):
        returnValue = libpanda._inPnJyoOIal(self.this, camera.this, offset)
        return returnValue

    
    def doBillboardPointEye(self, camera, offset):
        returnValue = libpanda._inPnJyobkbl(self.this, camera.this, offset)
        return returnValue

    
    def doBillboardPointWorld(self, camera, offset):
        returnValue = libpanda._inPnJyoXJcU(self.this, camera.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardAxis_ptrNodePath_ptrConstNodePath_float(self, camera, offset):
        returnValue = libpanda._inPnJyonoHV(self.this, camera.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardAxis_ptrNodePath_float(self, offset):
        returnValue = libpanda._inPnJyoMHYU(self.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardAxis_ptrNodePath(self):
        returnValue = libpanda._inPnJyoxiDy(self.this)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointEye_ptrNodePath_ptrConstNodePath_float(self, camera, offset):
        returnValue = libpanda._inPnJyo3opV(self.this, camera.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointEye_ptrNodePath_float(self, offset):
        returnValue = libpanda._inPnJyog0MU(self.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointEye_ptrNodePath(self):
        returnValue = libpanda._inPnJyoXCeP(self.this)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointWorld_ptrNodePath_ptrConstNodePath_float(self, camera, offset):
        returnValue = libpanda._inPnJyonjg2(self.this, camera.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointWorld_ptrNodePath_float(self, offset):
        returnValue = libpanda._inPnJyoOaqP(self.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointWorld_ptrNodePath(self):
        returnValue = libpanda._inPnJyoKJae(self.this)
        return returnValue

    
    def clearBillboard(self):
        returnValue = libpanda._inPnJyoaATv(self.this)
        return returnValue

    
    def hasBillboard(self):
        returnValue = libpanda._inPnJyo3oWg(self.this)
        return returnValue

    
    def _NodePath__overloaded_setCompass_ptrNodePath_ptrConstNodePath(self, reference):
        returnValue = libpanda._inPnJyoLfMs(self.this, reference.this)
        return returnValue

    
    def _NodePath__overloaded_setCompass_ptrNodePath(self):
        returnValue = libpanda._inPnJyopaNt(self.this)
        return returnValue

    
    def clearCompass(self):
        returnValue = libpanda._inPnJyoT898(self.this)
        return returnValue

    
    def hasCompass(self):
        returnValue = libpanda._inPnJyoqX5i(self.this)
        return returnValue

    
    def _NodePath__overloaded_setTransparency_ptrNodePath_bool_int(self, transparency, priority):
        returnValue = libpanda._inPnJyoC6cb(self.this, transparency, priority)
        return returnValue

    
    def _NodePath__overloaded_setTransparency_ptrNodePath_bool(self, transparency):
        returnValue = libpanda._inPnJyo_3BQ(self.this, transparency)
        return returnValue

    
    def clearTransparency(self):
        returnValue = libpanda._inPnJyocU7Z(self.this)
        return returnValue

    
    def hasTransparency(self):
        returnValue = libpanda._inPnJyofD3E(self.this)
        return returnValue

    
    def getTransparency(self):
        returnValue = libpanda._inPnJyo4Coc(self.this)
        return returnValue

    
    def adjustAllPriorities(self, adjustment):
        returnValue = libpanda._inPnJyoblUl(self.this, adjustment)
        return returnValue

    
    def _NodePath__overloaded_show_ptrNodePath(self):
        returnValue = libpanda._inPnJyoDwv_(self.this)
        return returnValue

    
    def _NodePath__overloaded_show_ptrNodePath_ptrBitMask32(self, cameraMask):
        returnValue = libpanda._inPnJyocfbj(self.this, cameraMask.this)
        return returnValue

    
    def _NodePath__overloaded_hide_ptrNodePath(self):
        returnValue = libpanda._inPnJyorDIm(self.this)
        return returnValue

    
    def _NodePath__overloaded_hide_ptrNodePath_ptrBitMask32(self, cameraMask):
        returnValue = libpanda._inPnJyocq1K(self.this, cameraMask.this)
        return returnValue

    
    def _NodePath__overloaded_isHidden_ptrConstNodePath_ptrBitMask32(self, cameraMask):
        returnValue = libpanda._inPnJyomQR5(self.this, cameraMask.this)
        return returnValue

    
    def _NodePath__overloaded_isHidden_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoYTUU(self.this)
        return returnValue

    
    def _NodePath__overloaded_getHiddenAncestor_ptrConstNodePath_ptrBitMask32(self, cameraMask):
        returnValue = libpanda._inPnJyoAHru(self.this, cameraMask.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getHiddenAncestor_ptrConstNodePath(self):
        returnValue = libpanda._inPnJyoICma(self.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_stash_ptrNodePath_int(self, sort):
        returnValue = libpanda._inPnJyo2Ms1(self.this, sort)
        return returnValue

    
    def _NodePath__overloaded_stash_ptrNodePath(self):
        returnValue = libpanda._inPnJyoinzQ(self.this)
        return returnValue

    
    def _NodePath__overloaded_unstash_ptrNodePath_int(self, sort):
        returnValue = libpanda._inPnJyobNQv(self.this, sort)
        return returnValue

    
    def _NodePath__overloaded_unstash_ptrNodePath(self):
        returnValue = libpanda._inPnJyoMkf6(self.this)
        return returnValue

    
    def unstashAll(self):
        returnValue = libpanda._inPnJyow2AF(self.this)
        return returnValue

    
    def isStashed(self):
        returnValue = libpanda._inPnJyo_PEj(self.this)
        return returnValue

    
    def getStashedAncestor(self):
        returnValue = libpanda._inPnJyoZTAQ(self.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCollideMask(self):
        returnValue = libpanda._inPnJyoBdNw(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_setCollideMask_ptrNodePath_ptrBitMask32_ptrBitMask32_ptrTypeHandle(self, newMask, bitsToChange, nodeType):
        returnValue = libpanda._inPnJyoDLwz(self.this, newMask.this, bitsToChange.this, nodeType.this)
        return returnValue

    
    def _NodePath__overloaded_setCollideMask_ptrNodePath_ptrBitMask32_ptrBitMask32(self, newMask, bitsToChange):
        returnValue = libpanda._inPnJyo7FaZ(self.this, newMask.this, bitsToChange.this)
        return returnValue

    
    def _NodePath__overloaded_setCollideMask_ptrNodePath_ptrBitMask32(self, newMask):
        returnValue = libpanda._inPnJyo_La2(self.this, newMask.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPnJyozIl9(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPnJyoROU9(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPnJyoM90s(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpanda._inPnJyoHPj2(self.this, other.this)
        return returnValue

    
    def verifyComplete(self):
        returnValue = libpanda._inPnJyoTqrp(self.this)
        return returnValue

    
    def prepareScene(self, gsg):
        returnValue = libpanda._inPnJyo0HH0(self.this, gsg.this)
        return returnValue

    
    def showBounds(self):
        returnValue = libpanda._inPnJyo1psR(self.this)
        return returnValue

    
    def hideBounds(self):
        returnValue = libpanda._inPnJyo0fG5(self.this)
        return returnValue

    
    def getBounds(self):
        returnValue = libpanda._inPnJyopOSR(self.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def forceRecomputeBounds(self):
        returnValue = libpanda._inPnJyotE3U(self.this)
        return returnValue

    
    def writeBounds(self, out):
        returnValue = libpanda._inPnJyo2vwc(self.this, out.this)
        return returnValue

    
    def calcTightBounds(self, minPoint, maxPoint):
        returnValue = libpanda._inPnJyovpR_(self.this, minPoint.this, maxPoint.this)
        return returnValue

    
    def flattenLight(self):
        returnValue = libpanda._inPnJyoznLC(self.this)
        return returnValue

    
    def flattenMedium(self):
        returnValue = libpanda._inPnJyoqVep(self.this)
        return returnValue

    
    def flattenStrong(self):
        returnValue = libpanda._inPnJyogdaT(self.this)
        return returnValue

    
    def setTag(self, key, value):
        returnValue = libpanda._inPnJyoBD_p(self.this, key, value)
        return returnValue

    
    def getTag(self, key):
        returnValue = libpanda._inPnJyozT5q(self.this, key)
        return returnValue

    
    def hasTag(self, key):
        returnValue = libpanda._inPnJyoWQGT(self.this, key)
        return returnValue

    
    def clearTag(self, key):
        returnValue = libpanda._inPnJyoHk6_(self.this, key)
        return returnValue

    
    def getNetTag(self, key):
        returnValue = libpanda._inPnJyo4VAu(self.this, key)
        return returnValue

    
    def hasNetTag(self, key):
        returnValue = libpanda._inPnJyobVNW(self.this, key)
        return returnValue

    
    def findNetTag(self, key):
        returnValue = libpanda._inPnJyopJhq(self.this, key)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setName(self, name):
        returnValue = libpanda._inPnJyo2Rjw(self.this, name)
        return returnValue

    
    def getName(self):
        returnValue = libpanda._inPnJyobkeW(self.this)
        return returnValue

    
    def writeBamFile(self, filename):
        returnValue = libpanda._inPnJyoDjrd(self.this, filename)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._NodePath__overloaded_constructor_atomicstring(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._NodePath__overloaded_constructor_ptrPandaNode(*_args)
            
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_constructor_ptrConstNodePath(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <PandaNode.PandaNode> <NodePath> '
        elif numArgs == 2:
            return self._NodePath__overloaded_constructor_ptrConstNodePath_ptrPandaNode(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def getH(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getH_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getH_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setDepthTest(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setDepthTest_ptrNodePath_bool(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setDepthTest_ptrNodePath_bool_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setR(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setR_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setR_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getTexture(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getTexture_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getTexture_ptrConstNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getTexScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_getTexScale_ptrConstNodePath_ptrTextureStage(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_getTexScale_ptrConstNodePath_ptrConstNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setTexTransform(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_setTexTransform_ptrNodePath_ptrTextureStage_ptrConstTransformState(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setTexTransform_ptrNodePath_ptrConstNodePath_ptrTextureStage_ptrConstTransformState(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setHpr_ptrNodePath_ptrConstLVecBase3f(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setHpr_ptrNodePath_float_float_float(*_args)
        elif numArgs == 4:
            return self._NodePath__overloaded_setHpr_ptrNodePath_ptrConstNodePath_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def setPosHprScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            return self._NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 4:
            return self._NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 9:
            return self._NodePath__overloaded_setPosHprScale_ptrNodePath_float_float_float_float_float_float_float_float_float(*_args)
        elif numArgs == 10:
            return self._NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 9 10 '

    
    def reparentTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_reparentTo_ptrNodePath_ptrConstNodePath(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_reparentTo_ptrNodePath_ptrConstNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setShear(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setShear_ptrNodePath_ptrConstLVecBase3f(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setShear_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setShear_ptrNodePath_float_float_float(*_args)
        elif numArgs == 4:
            return self._NodePath__overloaded_setShear_ptrNodePath_ptrConstNodePath_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def getMat(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getMat_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getMat_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def headsUp(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstLPoint3f(*_args)
            
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
        elif numArgs == 2:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(*_args)
            
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._NodePath__overloaded_headsUp_ptrNodePath_float_float_float(*_args)
            
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <NodePath> '
        elif numArgs == 4:
            return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def setFog(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setFog_ptrNodePath_ptrFog(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setFog_ptrNodePath_ptrFog_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getShear(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getShear_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getShear_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def instanceTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def clearTexProjector(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_clearTexProjector_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_clearTexProjector_ptrNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getScale_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getScale_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setTexOffset(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_setTexOffset_ptrNodePath_ptrTextureStage_ptrConstLVecBase2f(*_args)
        elif numArgs == 3:
            import TextureStage
            if isinstance(_args[0], TextureStage.TextureStage):
                return self._NodePath__overloaded_setTexOffset_ptrNodePath_ptrTextureStage_float_float(*_args)
            
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_setTexOffset_ptrNodePath_ptrConstNodePath_ptrTextureStage_ptrConstLVecBase2f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <TextureStage.TextureStage> <NodePath> '
        elif numArgs == 4:
            return self._NodePath__overloaded_setTexOffset_ptrNodePath_ptrConstNodePath_ptrTextureStage_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '

    
    def setShyz(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setShyz_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setShyz_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setX(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setX_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setX_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setBillboardPointWorld(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setBillboardPointWorld_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_setBillboardPointWorld_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setBillboardPointWorld_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def show(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_show_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_show_ptrNodePath_ptrBitMask32(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getShxz(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getShxz_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getShxz_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def ls(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_ls_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_ls_ptrConstNodePath_ptrOstream(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_ls_ptrConstNodePath_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def setCompass(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setCompass_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_setCompass_ptrNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def isHidden(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_isHidden_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_isHidden_ptrConstNodePath_ptrBitMask32(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def attachNewNode(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._NodePath__overloaded_attachNewNode_ptrConstNodePath_atomicstring(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._NodePath__overloaded_attachNewNode_ptrConstNodePath_ptrPandaNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <PandaNode.PandaNode> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                return self._NodePath__overloaded_attachNewNode_ptrConstNodePath_atomicstring_int(*_args)
            
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._NodePath__overloaded_attachNewNode_ptrConstNodePath_ptrPandaNode_int(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def hasLightOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_hasLightOff_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_hasLightOff_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getState(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getState_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getState_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setLight(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setLight_ptrNodePath_ptrConstNodePath(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setLight_ptrNodePath_ptrConstNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setSy(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setSy_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setSy_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setSz(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setSz_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setSz_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._NodePath__overloaded_setScale_ptrNodePath_float(*_args)
            
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._NodePath__overloaded_setScale_ptrNodePath_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) and isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return self._NodePath__overloaded_setScale_ptrNodePath_ptrConstNodePath_float(*_args)
                
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._NodePath__overloaded_setScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> <VBase3.VBase3> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 3:
            return self._NodePath__overloaded_setScale_ptrNodePath_float_float_float(*_args)
        elif numArgs == 4:
            return self._NodePath__overloaded_setScale_ptrNodePath_ptrConstNodePath_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def clearLight(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_clearLight_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_clearLight_ptrNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setBillboardPointEye(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setBillboardPointEye_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_setBillboardPointEye_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setBillboardPointEye_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def setTexGen(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_setTexGen_ptrNodePath_ptrTextureStage___enum__Mode(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setTexGen_ptrNodePath_ptrTextureStage___enum__Mode_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def getPosDelta(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getPosDelta_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getPosDelta_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getTexRotate(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_getTexRotate_ptrConstNodePath_ptrTextureStage(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_getTexRotate_ptrConstNodePath_ptrConstNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setQuatScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_setQuatScale_ptrNodePath_ptrConstLQuaternionf_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setQuatScale_ptrNodePath_ptrConstNodePath_ptrConstLQuaternionf_ptrConstLVecBase3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def instanceUnderNode(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_instanceUnderNode_ptrConstNodePath_ptrConstNodePath_atomicstring(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_instanceUnderNode_ptrConstNodePath_ptrConstNodePath_atomicstring_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setTextureOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setTextureOff_ptrNodePath(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._NodePath__overloaded_setTextureOff_ptrNodePath_int(*_args)
            
            import TextureStage
            if isinstance(_args[0], TextureStage.TextureStage):
                return self._NodePath__overloaded_setTextureOff_ptrNodePath_ptrTextureStage(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <TextureStage.TextureStage> '
        elif numArgs == 2:
            return self._NodePath__overloaded_setTextureOff_ptrNodePath_ptrTextureStage_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def getQuat(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getQuat_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getQuat_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setAlphaScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setAlphaScale_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setAlphaScale_ptrNodePath_float_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setPos_ptrNodePath_ptrConstLVecBase3f(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setPos_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setPos_ptrNodePath_float_float_float(*_args)
        elif numArgs == 4:
            return self._NodePath__overloaded_setPos_ptrNodePath_ptrConstNodePath_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def setBillboardAxis(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setBillboardAxis_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_setBillboardAxis_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setBillboardAxis_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def getZ(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getZ_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getZ_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getTexTransform(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_getTexTransform_ptrConstNodePath_ptrTextureStage(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_getTexTransform_ptrConstNodePath_ptrConstNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setRenderModeFilled(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setRenderModeFilled_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_setRenderModeFilled_ptrNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setMaterialOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setMaterialOff_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_setMaterialOff_ptrNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setSx(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setSx_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setSx_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setPosQuatScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            return self._NodePath__overloaded_setPosQuatScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f(*_args)
        elif numArgs == 4:
            return self._NodePath__overloaded_setPosQuatScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

    
    def setTexture(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setTexture_ptrNodePath_ptrTexture(*_args)
        elif numArgs == 2:
            import TextureStage
            if isinstance(_args[0], TextureStage.TextureStage):
                return self._NodePath__overloaded_setTexture_ptrNodePath_ptrTextureStage_ptrTexture(*_args)
            
            import Texture
            if isinstance(_args[0], Texture.Texture):
                return self._NodePath__overloaded_setTexture_ptrNodePath_ptrTexture_int(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <TextureStage.TextureStage> <Texture.Texture> '
        elif numArgs == 3:
            return self._NodePath__overloaded_setTexture_ptrNodePath_ptrTextureStage_ptrTexture_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def getPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getPos_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getPos_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def clearTexture(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_clearTexture_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_clearTexture_ptrNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getShxy(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getShxy_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getShxy_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setColorScaleOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setColorScaleOff_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_setColorScaleOff_ptrNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def hasTextureOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_hasTextureOff_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_hasTextureOff_ptrConstNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def findAllTextureStages(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_findAllTextureStages_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_findAllTextureStages_ptrConstNodePath_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getX(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getX_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getX_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setPrevTransform(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setPrevTransform_ptrNodePath_ptrConstTransformState(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setPrevTransform_ptrNodePath_ptrConstNodePath_ptrConstTransformState(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getHiddenAncestor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getHiddenAncestor_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getHiddenAncestor_ptrConstNodePath_ptrBitMask32(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def lookAt(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstLPoint3f(*_args)
            
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
        elif numArgs == 2:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(*_args)
            
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._NodePath__overloaded_lookAt_ptrNodePath_float_float_float(*_args)
            
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <NodePath> '
        elif numArgs == 4:
            return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def getPrevTransform(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getPrevTransform_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getPrevTransform_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def wrtReparentTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setPosHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 6:
            return self._NodePath__overloaded_setPosHpr_ptrNodePath_float_float_float_float_float_float(*_args)
        elif numArgs == 7:
            return self._NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 6 7 '

    
    def setRenderModeWireframe(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setRenderModeWireframe_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_setRenderModeWireframe_ptrNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getR(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getR_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getR_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setState(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setState_ptrNodePath_ptrConstRenderState(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setState_ptrNodePath_ptrConstNodePath_ptrConstRenderState(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setColorScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setColorScale_ptrNodePath_ptrConstLVecBase4f(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setColorScale_ptrNodePath_ptrConstLVecBase4f_int(*_args)
        elif numArgs == 4:
            return self._NodePath__overloaded_setColorScale_ptrNodePath_float_float_float_float(*_args)
        elif numArgs == 5:
            return self._NodePath__overloaded_setColorScale_ptrNodePath_float_float_float_float_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 4 5 '

    
    def hide(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_hide_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_hide_ptrNodePath_ptrBitMask32(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setBin(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_setBin_ptrNodePath_atomicstring_int(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setBin_ptrNodePath_atomicstring_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setTwoSided(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setTwoSided_ptrNodePath_bool(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setTwoSided_ptrNodePath_bool_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def clearTexGen(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_clearTexGen_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_clearTexGen_ptrNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setMaterial(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setMaterial_ptrNodePath_ptrMaterial(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setMaterial_ptrNodePath_ptrMaterial_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setFluidX(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setFluidX_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setFluidX_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setQuat(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setQuat_ptrNodePath_ptrConstLQuaternionf(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setQuat_ptrNodePath_ptrConstNodePath_ptrConstLQuaternionf(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def hasTexture(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_hasTexture_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_hasTexture_ptrConstNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def findAllTextures(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_findAllTextures_ptrConstNodePath(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._NodePath__overloaded_findAllTextures_ptrConstNodePath_atomicstring(*_args)
            
            import TextureStage
            if isinstance(_args[0], TextureStage.TextureStage):
                return self._NodePath__overloaded_findAllTextures_ptrConstNodePath_ptrTextureStage(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <TextureStage.TextureStage> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setPosQuatScaleShear(self, *_args):
        numArgs = len(_args)
        if numArgs == 4:
            return self._NodePath__overloaded_setPosQuatScaleShear_ptrNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 5:
            return self._NodePath__overloaded_setPosQuatScaleShear_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 4 5 '

    
    def setHprScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_setHprScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setHprScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 6:
            return self._NodePath__overloaded_setHprScale_ptrNodePath_float_float_float_float_float_float(*_args)
        elif numArgs == 7:
            return self._NodePath__overloaded_setHprScale_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 6 7 '

    
    def copyTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_copyTo_ptrConstNodePath_ptrConstNodePath(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_copyTo_ptrConstNodePath_ptrConstNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCollideMask(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setCollideMask_ptrNodePath_ptrBitMask32(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setCollideMask_ptrNodePath_ptrBitMask32_ptrBitMask32(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setCollideMask_ptrNodePath_ptrBitMask32_ptrBitMask32_ptrTypeHandle(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def setDepthWrite(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setDepthWrite_ptrNodePath_bool(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setDepthWrite_ptrNodePath_bool_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setFogOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setFogOff_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_setFogOff_ptrNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setMat(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setMat_ptrNodePath_ptrConstLMatrix4f(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setMat_ptrNodePath_ptrConstNodePath_ptrConstLMatrix4f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getP(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getP_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getP_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def unstash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_unstash_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_unstash_ptrNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def reverseLs(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_reverseLs_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_reverseLs_ptrConstNodePath_ptrOstream(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_reverseLs_ptrConstNodePath_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def setAllColorScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setAllColorScale_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setAllColorScale_ptrNodePath_float_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def clearTexTransform(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_clearTexTransform_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_clearTexTransform_ptrNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setH(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setH_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setH_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setFluidZ(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setFluidZ_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setFluidZ_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getShyz(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getShyz_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getShyz_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setPosQuat(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_setPosQuat_ptrNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setPosQuat_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setP(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setP_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setP_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setPosHprScaleShear(self, *_args):
        numArgs = len(_args)
        if numArgs == 4:
            return self._NodePath__overloaded_setPosHprScaleShear_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 5:
            return self._NodePath__overloaded_setPosHprScaleShear_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 4 5 '

    
    def setColorOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setColorOff_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_setColorOff_ptrNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setLightOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setLightOff_ptrNodePath(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._NodePath__overloaded_setLightOff_ptrNodePath_int(*_args)
            
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_setLightOff_ptrNodePath_ptrConstNodePath(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <NodePath> '
        elif numArgs == 2:
            return self._NodePath__overloaded_setLightOff_ptrNodePath_ptrConstNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def getTransform(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getTransform_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getTransform_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setTransform(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setTransform_ptrNodePath_ptrConstTransformState(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setTransform_ptrNodePath_ptrConstNodePath_ptrConstTransformState(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setShxz(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setShxz_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setShxz_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setY(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setY_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setY_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setZ(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setZ_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setZ_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setShxy(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setShxy_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setShxy_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getSx(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getSx_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getSx_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getSy(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getSy_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getSy_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getSz(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getSz_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getSz_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setTexScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_setTexScale_ptrNodePath_ptrTextureStage_ptrConstLVecBase2f(*_args)
        elif numArgs == 3:
            import TextureStage
            if isinstance(_args[0], TextureStage.TextureStage):
                return self._NodePath__overloaded_setTexScale_ptrNodePath_ptrTextureStage_float_float(*_args)
            
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_setTexScale_ptrNodePath_ptrConstNodePath_ptrTextureStage_ptrConstLVecBase2f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <TextureStage.TextureStage> <NodePath> '
        elif numArgs == 4:
            return self._NodePath__overloaded_setTexScale_ptrNodePath_ptrConstNodePath_ptrTextureStage_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '

    
    def setColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setColor_ptrNodePath_ptrConstLVecBase4f(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setColor_ptrNodePath_ptrConstLVecBase4f_int(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setColor_ptrNodePath_float_float_float(*_args)
        elif numArgs == 4:
            return self._NodePath__overloaded_setColor_ptrNodePath_float_float_float_float(*_args)
        elif numArgs == 5:
            return self._NodePath__overloaded_setColor_ptrNodePath_float_float_float_float_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 5 '

    
    def findTexture(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._NodePath__overloaded_findTexture_ptrConstNodePath_atomicstring(*_args)
            
            import TextureStage
            if isinstance(_args[0], TextureStage.TextureStage):
                return self._NodePath__overloaded_findTexture_ptrConstNodePath_ptrTextureStage(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <TextureStage.TextureStage> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setTexRotate(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NodePath__overloaded_setTexRotate_ptrNodePath_ptrTextureStage_float(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setTexRotate_ptrNodePath_ptrConstNodePath_ptrTextureStage_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def getHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getHpr_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getHpr_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def stash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_stash_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_stash_ptrNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getY(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getY_ptrConstNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_getY_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setFluidY(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setFluidY_ptrNodePath_float(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setFluidY_ptrNodePath_ptrConstNodePath_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getTexOffset(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_getTexOffset_ptrConstNodePath_ptrTextureStage(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_getTexOffset_ptrConstNodePath_ptrConstNodePath_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def clearTransform(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_clearTransform_ptrNodePath(*_args)
        elif numArgs == 1:
            return self._NodePath__overloaded_clearTransform_ptrNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setFluidPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setFluidPos_ptrNodePath_ptrConstLVecBase3f(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setFluidPos_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._NodePath__overloaded_setFluidPos_ptrNodePath_float_float_float(*_args)
        elif numArgs == 4:
            return self._NodePath__overloaded_setFluidPos_ptrNodePath_ptrConstNodePath_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def setTransparency(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePath__overloaded_setTransparency_ptrNodePath_bool(*_args)
        elif numArgs == 2:
            return self._NodePath__overloaded_setTransparency_ptrNodePath_bool_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def id(self):
        return self.getKey()

    
    def __hash__(self):
        return self.getKey()

    
    def getChildrenAsList(self):
        return self.getChildren().asList()

    
    def printChildren(self):
        for child in self.getChildrenAsList():
            print child.getName()
        

    
    def removeChildren(self):
        for child in self.getChildrenAsList():
            child.removeNode()
        

    
    def toggleVis(self):
        if self.isHidden():
            self.show()
            return 1
        else:
            self.hide()
            return 0

    
    def showSiblings(self):
        for sib in self.getParent().getChildrenAsList():
            if sib.node() != self.node():
                sib.show()
            
        

    
    def hideSiblings(self):
        for sib in self.getParent().getChildrenAsList():
            if sib.node() != self.node():
                sib.hide()
            
        

    
    def showAllDescendants(self):
        self.show()
        for child in self.getChildrenAsList():
            child.showAllDescendants()
        

    
    def isolate(self):
        self.showAllDescendants()
        self.hideSiblings()

    
    def remove(self):
        messenger.send('preRemoveNodePath', [
            self])
        self.removeNode()

    
    def lsNames(self):
        if self.isEmpty():
            print '(empty)'
        else:
            type = self.node().getType().getName()
            name = self.getName()
            print type + '  ' + name
            self.lsNamesRecurse()

    
    def lsNamesRecurse(self, indentString = ' '):
        for nodePath in self.getChildrenAsList():
            type = nodePath.node().getType().getName()
            name = nodePath.getName()
            print indentString + type + '  ' + name
            nodePath.lsNamesRecurse(indentString + ' ')
        

    
    def reverseLsNames(self):
        ancestry = self.getAncestry()
        indentString = ''
        for nodePath in ancestry:
            type = nodePath.node().getType().getName()
            name = nodePath.getName()
            print indentString + type + '  ' + name
            indentString = indentString + ' '
        

    
    def getAncestry(self):
        node = self.node()
        if self.hasParent():
            ancestry = self.getParent().getAncestry()
            ancestry.append(self)
            return ancestry
        else:
            return [
                self]

    
    def getTightBounds(self):
        Point3 = Point3
        import pandac
        v1 = Point3.Point3(0)
        v2 = Point3.Point3(0)
        self.calcTightBounds(v1, v2)
        return (v1, v2)

    
    def pPrintString(self, other = None):
        pass

    
    def printPos(self, other = None, sd = 2):
        formatString = '%0.' + '%d' % sd + 'f'
        if other:
            pos = self.getPos(other)
            otherString = other.getName() + ', '
        else:
            pos = self.getPos()
            otherString = ''
        print self.getName() + '.setPos(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ')\n'

    
    def printHpr(self, other = None, sd = 2):
        formatString = '%0.' + '%d' % sd + 'f'
        if other:
            hpr = self.getHpr(other)
            otherString = other.getName() + ', '
        else:
            hpr = self.getHpr()
            otherString = ''
        print self.getName() + '.setHpr(' + otherString + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ')\n'

    
    def printScale(self, other = None, sd = 2):
        formatString = '%0.' + '%d' % sd + 'f'
        if other:
            scale = self.getScale(other)
            otherString = other.getName() + ', '
        else:
            scale = self.getScale()
            otherString = ''
        print self.getName() + '.setScale(' + otherString + formatString % scale[0] + ', ' + formatString % scale[1] + ', ' + formatString % scale[2] + ')\n'

    
    def printPosHpr(self, other = None, sd = 2):
        formatString = '%0.' + '%d' % sd + 'f'
        if other:
            pos = self.getPos(other)
            hpr = self.getHpr(other)
            otherString = other.getName() + ', '
        else:
            pos = self.getPos()
            hpr = self.getHpr()
            otherString = ''
        print self.getName() + '.setPosHpr(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ', ' + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ')\n'

    
    def printPosHprScale(self, other = None, sd = 2):
        formatString = '%0.' + '%d' % sd + 'f'
        if other:
            pos = self.getPos(other)
            hpr = self.getHpr(other)
            scale = self.getScale(other)
            otherString = other.getName() + ', '
        else:
            pos = self.getPos()
            hpr = self.getHpr()
            scale = self.getScale()
            otherString = ''
        print self.getName() + '.setPosHprScale(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ', ' + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ', ' + formatString % scale[0] + ', ' + formatString % scale[1] + ', ' + formatString % scale[2] + ')\n'

    
    def iPos(self, other = None):
        if other:
            self.setPos(other, 0, 0, 0)
        else:
            self.setPos(0, 0, 0)

    
    def iHpr(self, other = None):
        if other:
            self.setHpr(other, 0, 0, 0)
        else:
            self.setHpr(0, 0, 0)

    
    def iScale(self, other = None):
        if other:
            self.setScale(other, 1, 1, 1)
        else:
            self.setScale(1, 1, 1)

    
    def iPosHpr(self, other = None):
        if other:
            self.setPosHpr(other, 0, 0, 0, 0, 0, 0)
        else:
            self.setPosHpr(0, 0, 0, 0, 0, 0)

    
    def iPosHprScale(self, other = None):
        if other:
            self.setPosHprScale(other, 0, 0, 0, 0, 0, 0, 1, 1, 1)
        else:
            self.setPosHprScale(0, 0, 0, 0, 0, 0, 1, 1, 1)

    
    def _NodePath__lerp(self, functorFunc, duration, blendType, taskName = None):
        Task = Task
        import direct.task
        LerpBlendHelpers = LerpBlendHelpers
        import direct.showbase
        taskMgr = taskMgr
        import direct.task.TaskManagerGlobal
        
        def lerpUponDeath(task):
            
            try:
                del task.functorFunc
            except:
                pass

            
            try:
                del task.lerp
            except:
                pass


        
        def lerpTaskFunc(task):
            Lerp = Lerp
            import pandac.Lerp
            ClockObject = ClockObject
            import pandac.ClockObject
            Task = Task
            cont = cont
            done = done
            import direct.task.Task
            if task.init == 1:
                functor = task.functorFunc()
                task.lerp = Lerp(functor, task.duration, task.blendType)
                task.init = 0
            
            dt = globalClock.getDt()
            task.lerp.setStepSize(dt)
            task.lerp.step()
            if task.lerp.isDone():
                task.init = 1
                return done
            else:
                return cont

        lerpTask = Task.Task(lerpTaskFunc)
        lerpTask.init = 1
        lerpTask.functorFunc = functorFunc
        lerpTask.duration = duration
        lerpTask.blendType = LerpBlendHelpers.getBlend(blendType)
        lerpTask.uponDeath = lerpUponDeath
        if taskName == None:
            return lerpTask
        else:
            taskMgr.add(lerpTask, taskName)
            return lerpTask

    
    def _NodePath__autoLerp(self, functorFunc, time, blendType, taskName):
        AutonomousLerp = AutonomousLerp
        import pandac
        LerpBlendHelpers = LerpBlendHelpers
        import direct.showbase
        functor = functorFunc()
        lerp = AutonomousLerp.AutonomousLerp(functor, time, LerpBlendHelpers.getBlend(blendType), base.eventHandler)
        lerp.start()
        return lerp

    
    def lerpColor(self, *posArgs, **keyArgs):
        if len(posArgs) == 2:
            return apply(self.lerpColorVBase4, posArgs, keyArgs)
        elif len(posArgs) == 3:
            return apply(self.lerpColorVBase4VBase4, posArgs, keyArgs)
        elif len(posArgs) == 5:
            return apply(self.lerpColorRGBA, posArgs, keyArgs)
        elif len(posArgs) == 9:
            return apply(self.lerpColorRGBARGBA, posArgs, keyArgs)
        else:
            raise Exception('Error: NodePath.lerpColor: bad number of args')

    
    def lerpColorRGBA(self, r, g, b, a, time, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, r = r, g = g, b = b, a = a):
            ColorLerpFunctor = ColorLerpFunctor
            import pandac
            startColor = self.getColor()
            functor = ColorLerpFunctor.ColorLerpFunctor(self, startColor[0], startColor[1], startColor[2], startColor[3], r, g, b, a)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpColorRGBARGBA(self, sr, sg, sb, sa, er, eg, eb, ea, time, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, sr = sr, sg = sg, sb = sb, sa = sa, er = er, eg = eg, eb = eb, ea = ea):
            ColorLerpFunctor = ColorLerpFunctor
            import pandac
            functor = ColorLerpFunctor.ColorLerpFunctor(self, sr, sg, sb, sa, er, eg, eb, ea)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpColorVBase4(self, endColor, time, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, endColor = endColor):
            ColorLerpFunctor = ColorLerpFunctor
            import pandac
            startColor = self.getColor()
            functor = ColorLerpFunctor.ColorLerpFunctor(self, startColor, endColor)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpColorVBase4VBase4(self, startColor, endColor, time, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, startColor = startColor, endColor = endColor):
            ColorLerpFunctor = ColorLerpFunctor
            import pandac
            functor = ColorLerpFunctor.ColorLerpFunctor(self, startColor, endColor)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpColorScale(self, *posArgs, **keyArgs):
        if len(posArgs) == 2:
            return apply(self.lerpColorScaleVBase4, posArgs, keyArgs)
        elif len(posArgs) == 3:
            return apply(self.lerpColorScaleVBase4VBase4, posArgs, keyArgs)
        elif len(posArgs) == 5:
            return apply(self.lerpColorScaleRGBA, posArgs, keyArgs)
        elif len(posArgs) == 9:
            return apply(self.lerpColorScaleRGBARGBA, posArgs, keyArgs)
        else:
            raise Exception('Error: NodePath.lerpColorScale: bad number of args')

    
    def lerpColorScaleRGBA(self, r, g, b, a, time, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, r = r, g = g, b = b, a = a):
            ColorScaleLerpFunctor = ColorScaleLerpFunctor
            import pandac
            startColor = self.getColor()
            functor = ColorScaleLerpFunctor.ColorScaleLerpFunctor(self, startColor[0], startColor[1], startColor[2], startColor[3], r, g, b, a)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpColorScaleRGBARGBA(self, sr, sg, sb, sa, er, eg, eb, ea, time, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, sr = sr, sg = sg, sb = sb, sa = sa, er = er, eg = eg, eb = eb, ea = ea):
            ColorScaleLerpFunctor = ColorScaleLerpFunctor
            import pandac
            functor = ColorScaleLerpFunctor.ColorScaleLerpFunctor(self, sr, sg, sb, sa, er, eg, eb, ea)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpColorScaleVBase4(self, endColor, time, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, endColor = endColor):
            ColorScaleLerpFunctor = ColorScaleLerpFunctor
            import pandac
            startColor = self.getColor()
            functor = ColorScaleLerpFunctor.ColorScaleLerpFunctor(self, startColor, endColor)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpColorScaleVBase4VBase4(self, startColor, endColor, time, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, startColor = startColor, endColor = endColor):
            ColorScaleLerpFunctor = ColorScaleLerpFunctor
            import pandac
            functor = ColorScaleLerpFunctor.ColorScaleLerpFunctor(self, startColor, endColor)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpHpr(self, *posArgs, **keyArgs):
        if len(posArgs) == 4:
            return apply(self.lerpHprHPR, posArgs, keyArgs)
        elif len(posArgs) == 2:
            return apply(self.lerpHprVBase3, posArgs, keyArgs)
        else:
            raise Exception('Error: NodePath.lerpHpr: bad number of args')

    
    def lerpHprHPR(self, h, p, r, time, other = None, blendType = 'noBlend', auto = None, task = None, shortest = 1):
        
        def functorFunc(self = self, h = h, p = p, r = r, other = other, shortest = shortest):
            HprLerpFunctor = HprLerpFunctor
            import pandac
            if other != None:
                startHpr = self.getHpr(other)
                functor = HprLerpFunctor.HprLerpFunctor(self, startHpr[0], startHpr[1], startHpr[2], h, p, r, other)
                if shortest:
                    functor.takeShortest()
                
            else:
                startHpr = self.getHpr()
                functor = HprLerpFunctor.HprLerpFunctor(self, startHpr[0], startHpr[1], startHpr[2], h, p, r)
                if shortest:
                    functor.takeShortest()
                
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpHprVBase3(self, hpr, time, other = None, blendType = 'noBlend', auto = None, task = None, shortest = 1):
        
        def functorFunc(self = self, hpr = hpr, other = other, shortest = shortest):
            HprLerpFunctor = HprLerpFunctor
            import pandac
            if other != None:
                functor = HprLerpFunctor.HprLerpFunctor(self, self.getHpr(other), hpr, other)
                if shortest:
                    functor.takeShortest()
                
            else:
                functor = HprLerpFunctor.HprLerpFunctor(self, self.getHpr(), hpr)
                if shortest:
                    functor.takeShortest()
                
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpPos(self, *posArgs, **keyArgs):
        if len(posArgs) == 4:
            return apply(self.lerpPosXYZ, posArgs, keyArgs)
        elif len(posArgs) == 2:
            return apply(self.lerpPosPoint3, posArgs, keyArgs)
        else:
            raise Exception('Error: NodePath.lerpPos: bad number of args')

    
    def lerpPosXYZ(self, x, y, z, time, other = None, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, x = x, y = y, z = z, other = other):
            PosLerpFunctor = PosLerpFunctor
            import pandac
            if other != None:
                startPos = self.getPos(other)
                functor = PosLerpFunctor.PosLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z, other)
            else:
                startPos = self.getPos()
                functor = PosLerpFunctor.PosLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpPosPoint3(self, pos, time, other = None, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, pos = pos, other = other):
            PosLerpFunctor = PosLerpFunctor
            import pandac
            if other != None:
                functor = PosLerpFunctor.PosLerpFunctor(self, self.getPos(other), pos, other)
            else:
                functor = PosLerpFunctor.PosLerpFunctor(self, self.getPos(), pos)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpPosHpr(self, *posArgs, **keyArgs):
        if len(posArgs) == 7:
            return apply(self.lerpPosHprXYZHPR, posArgs, keyArgs)
        elif len(posArgs) == 3:
            return apply(self.lerpPosHprPoint3VBase3, posArgs, keyArgs)
        else:
            raise Exception('Error: NodePath.lerpPosHpr: bad number of args')

    
    def lerpPosHprPoint3VBase3(self, pos, hpr, time, other = None, blendType = 'noBlend', auto = None, task = None, shortest = 1):
        
        def functorFunc(self = self, pos = pos, hpr = hpr, other = other, shortest = shortest):
            PosHprLerpFunctor = PosHprLerpFunctor
            import pandac
            if other != None:
                startPos = self.getPos(other)
                startHpr = self.getHpr(other)
                functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos, pos, startHpr, hpr, other)
                if shortest:
                    functor.takeShortest()
                
            else:
                startPos = self.getPos()
                startHpr = self.getHpr()
                functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos, pos, startHpr, hpr)
                if shortest:
                    functor.takeShortest()
                
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpPosHprXYZHPR(self, x, y, z, h, p, r, time, other = None, blendType = 'noBlend', auto = None, task = None, shortest = 1):
        
        def functorFunc(self = self, x = x, y = y, z = z, h = h, p = p, r = r, other = other, shortest = shortest):
            PosHprLerpFunctor = PosHprLerpFunctor
            import pandac
            if other != None:
                startPos = self.getPos(other)
                startHpr = self.getHpr(other)
                functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z, startHpr[0], startHpr[1], startHpr[2], h, p, r, other)
                if shortest:
                    functor.takeShortest()
                
            else:
                startPos = self.getPos()
                startHpr = self.getHpr()
                functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z, startHpr[0], startHpr[1], startHpr[2], h, p, r)
                if shortest:
                    functor.takeShortest()
                
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpPosHprScale(self, pos, hpr, scale, time, other = None, blendType = 'noBlend', auto = None, task = None, shortest = 1):
        
        def functorFunc(self = self, pos = pos, hpr = hpr, scale = scale, other = other, shortest = shortest):
            PosHprScaleLerpFunctor = PosHprScaleLerpFunctor
            import pandac
            if other != None:
                startPos = self.getPos(other)
                startHpr = self.getHpr(other)
                startScale = self.getScale(other)
                functor = PosHprScaleLerpFunctor.PosHprScaleLerpFunctor(self, startPos, pos, startHpr, hpr, startScale, scale, other)
                if shortest:
                    functor.takeShortest()
                
            else:
                startPos = self.getPos()
                startHpr = self.getHpr()
                startScale = self.getScale()
                functor = PosHprScaleLerpFunctor.PosHprScaleLerpFunctor(self, startPos, pos, startHpr, hpr, startScale, scale)
                if shortest:
                    functor.takeShortest()
                
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpScale(self, *posArgs, **keyArgs):
        if len(posArgs) == 4:
            return apply(self.lerpScaleXYZ, posArgs, keyArgs)
        elif len(posArgs) == 2:
            return apply(self.lerpScaleVBase3, posArgs, keyArgs)
        else:
            raise Exception('Error: NodePath.lerpScale: bad number of args')

    
    def lerpScaleVBase3(self, scale, time, other = None, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, scale = scale, other = other):
            ScaleLerpFunctor = ScaleLerpFunctor
            import pandac
            if other != None:
                functor = ScaleLerpFunctor.ScaleLerpFunctor(self, self.getScale(other), scale, other)
            else:
                functor = ScaleLerpFunctor.ScaleLerpFunctor(self, self.getScale(), scale)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def lerpScaleXYZ(self, sx, sy, sz, time, other = None, blendType = 'noBlend', auto = None, task = None):
        
        def functorFunc(self = self, sx = sx, sy = sy, sz = sz, other = other):
            ScaleLerpFunctor = ScaleLerpFunctor
            import pandac
            if other != None:
                startScale = self.getScale(other)
                functor = ScaleLerpFunctor.ScaleLerpFunctor(self, startScale[0], startScale[1], startScale[2], sx, sy, sz, other)
            else:
                startScale = self.getScale()
                functor = ScaleLerpFunctor.ScaleLerpFunctor(self, startScale[0], startScale[1], startScale[2], sx, sy, sz)
            return functor

        if auto != None:
            return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
        elif task != None:
            return self._NodePath__lerp(functorFunc, time, blendType, task)
        else:
            return self._NodePath__lerp(functorFunc, time, blendType)

    
    def place(self):
        base.startDirect(fWantTk = 1)
        Placer = Placer
        import direct.tkpanels
        return Placer.place(self)

    
    def explore(self):
        base.startDirect(fWantTk = 1)
        SceneGraphExplorer = SceneGraphExplorer
        import direct.tkwidgets
        return SceneGraphExplorer.explore(self)

    
    def rgbPanel(self, cb = None):
        base.startTk()
        Slider = Slider
        import direct.tkwidgets
        return Slider.rgbPanel(self, cb)

    
    def select(self):
        base.startDirect(fWantTk = 0)
        direct.select(self)

    
    def deselect(self):
        base.startDirect(fWantTk = 0)
        direct.deselect(self)

    
    def showCS(self, mask = None):
        npc = self.findAllMatches('**/+CollisionNode')
        for p in range(0, npc.getNumPaths()):
            np = npc[p]
            if mask == None or (np.node().getIntoCollideMask() & mask).getWord():
                np.show()
            
        

    
    def hideCS(self, mask = None):
        npc = self.findAllMatches('**/+CollisionNode')
        for p in range(0, npc.getNumPaths()):
            np = npc[p]
            if mask == None or (np.node().getIntoCollideMask() & mask).getWord():
                np.hide()
            
        

    
    def posInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpPosInterval(self, *args, **args)

    
    def hprInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpHprInterval(self, *args, **args)

    
    def quatInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpQuatInterval(self, *args, **args)

    
    def scaleInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpScaleInterval(self, *args, **args)

    
    def shearInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpShearInterval(self, *args, **args)

    
    def posHprInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpPosHprInterval(self, *args, **args)

    
    def posQuatInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpPosQuatInterval(self, *args, **args)

    
    def hprScaleInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpHprScaleInterval(self, *args, **args)

    
    def quatScaleInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpQuatScaleInterval(self, *args, **args)

    
    def posHprScaleInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpPosHprScaleInterval(self, *args, **args)

    
    def posQuatScaleInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpPosQuatScaleInterval(self, *args, **args)

    
    def posHprScaleShearInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpPosHprScaleShearInterval(self, *args, **args)

    
    def posQuatScaleShearInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpPosQuatScaleShearInterval(self, *args, **args)

    
    def colorInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpColorInterval(self, *args, **args)

    
    def colorScaleInterval(self, *args, **kw):
        LerpInterval = LerpInterval
        import direct.interval
        return LerpInterval.LerpColorScaleInterval(self, *args, **args)

    
    def attachCollisionSphere(self, name, cx, cy, cz, r, fromCollide, intoCollide):
        CollisionSphere = CollisionSphere
        import pandac
        CollisionNode = CollisionNode
        import pandac
        coll = CollisionSphere.CollisionSphere(cx, cy, cz, r)
        collNode = CollisionNode.CollisionNode(name)
        collNode.addSolid(coll)
        collNode.setFromCollideMask(fromCollide)
        collNode.setIntoCollideMask(intoCollide)
        collNodePath = self.attachNewNode(collNode)
        return collNodePath

    
    def attachCollisionSegment(self, name, ax, ay, az, bx, by, bz, fromCollide, intoCollide):
        CollisionSegment = CollisionSegment
        import pandac
        CollisionNode = CollisionNode
        import pandac
        coll = CollisionSegment.CollisionSegment(ax, ay, az, bx, by, bz)
        collNode = CollisionNode.CollisionNode(name)
        collNode.addSolid(coll)
        collNode.setFromCollideMask(fromCollide)
        collNode.setIntoCollideMask(intoCollide)
        collNodePath = self.attachNewNode(collNode)
        return collNodePath

    
    def attachCollisionRay(self, name, ox, oy, oz, dx, dy, dz, fromCollide, intoCollide):
        CollisionRay = CollisionRay
        import pandac
        CollisionNode = CollisionNode
        import pandac
        coll = CollisionRay.CollisionRay(ox, oy, oz, dx, dy, dz)
        collNode = CollisionNode.CollisionNode(name)
        collNode.addSolid(coll)
        collNode.setFromCollideMask(fromCollide)
        collNode.setIntoCollideMask(intoCollide)
        collNodePath = self.attachNewNode(collNode)
        return collNodePath

    
    def flattenMultitex(self, stateFrom = None, target = None, useGeom = 0, allowTexMat = 0, win = None):
        MultitexReducer = MultitexReducer
        import pandac
        mr = MultitexReducer.MultitexReducer()
        if target != None:
            mr.setTarget(target)
        
        mr.setUseGeom(useGeom)
        mr.setAllowTexMat(allowTexMat)
        if win == None:
            win = base.win
        
        if stateFrom == None:
            mr.scan(self)
        else:
            mr.scan(self, stateFrom)
        mr.flatten(win)


