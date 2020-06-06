# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

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
        
        apply(self.constructor, _args)

    
    def _NodePath__overloaded_constructor(self):
        self.this = libpanda._inPkJyoex9g()
        self.userManagesMemory = 1

    
    def _NodePath__overloaded_constructor_ptrConstNodePath(self, copy):
        self.this = libpanda._inPkJyoWaJj(copy.this)
        self.userManagesMemory = 1

    
    def _NodePath__overloaded_constructor_ptrConstNodePath_ptrPandaNode(self, parent, childNode):
        self.this = libpanda._inPkJyoYAhm(parent.this, childNode.this)
        self.userManagesMemory = 1

    
    def _NodePath__overloaded_constructor_ptrPandaNode(self, node):
        self.this = libpanda._inPkJyoH4wM(node.this)
        self.userManagesMemory = 1

    
    def _NodePath__overloaded_constructor_atomicstring(self, topNodeName):
        self.this = libpanda._inPkJyoH_EQ(topNodeName)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyofXq7:
            libpanda._inPkJyofXq7(self.this)
        

    
    def anyPath(node):
        returnValue = libpanda._inPkJyooGNf(node.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    anyPath = staticmethod(anyPath)
    
    def notFound():
        returnValue = libpanda._inPkJyoH6GR()
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    notFound = staticmethod(notFound)
    
    def removed():
        returnValue = libpanda._inPkJyocqkY()
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    removed = staticmethod(removed)
    
    def fail():
        returnValue = libpanda._inPkJyoLvgx()
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    fail = staticmethod(fail)
    
    def setMaxSearchDepth(maxSearchDepth):
        returnValue = libpanda._inPkJyoF4FI(maxSearchDepth)
        return returnValue

    setMaxSearchDepth = staticmethod(setMaxSearchDepth)
    
    def getMaxSearchDepth():
        returnValue = libpanda._inPkJyojBwf()
        return returnValue

    getMaxSearchDepth = staticmethod(getMaxSearchDepth)
    
    def getClassType():
        returnValue = libpanda._inPkJyos3wh()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpanda._inPkJyooj60(self.this, copy.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isEmpty(self):
        returnValue = libpanda._inPkJyo6BVO(self.this)
        return returnValue

    
    def isSingleton(self):
        returnValue = libpanda._inPkJyomHP3(self.this)
        return returnValue

    
    def getNumNodes(self):
        returnValue = libpanda._inPkJyoLbn0(self.this)
        return returnValue

    
    def getNode(self, index):
        returnValue = libpanda._inPkJyoGNz9(self.this, index)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getErrorType(self):
        returnValue = libpanda._inPkJyo17Vc(self.this)
        return returnValue

    
    def getTopNode(self):
        returnValue = libpanda._inPkJyoCGOI(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def node(self):
        returnValue = libpanda._inPkJyoC92U(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getKey(self):
        returnValue = libpanda._inPkJyotmo_(self.this)
        return returnValue

    
    def getChildren(self):
        returnValue = libpanda._inPkJyogb8V(self.this)
        import NodePathCollection
        returnObject = NodePathCollection.NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumChildren(self):
        returnValue = libpanda._inPkJyoTTCh(self.this)
        return returnValue

    
    def getChild(self, n):
        returnValue = libpanda._inPkJyoaFtX(self.this, n)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasParent(self):
        returnValue = libpanda._inPkJyogc1w(self.this)
        return returnValue

    
    def getParent(self):
        returnValue = libpanda._inPkJyoDcoI(self.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def find(self, path):
        returnValue = libpanda._inPkJyoO9_b(self.this, path)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findPathTo(self, node):
        returnValue = libpanda._inPkJyoRFrr(self.this, node.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findAllMatches(self, path):
        returnValue = libpanda._inPkJyoupHP(self.this, path)
        import NodePathCollection
        returnObject = NodePathCollection.NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findAllPathsTo(self, node):
        returnValue = libpanda._inPkJyoP6Sn(self.this, node.this)
        import NodePathCollection
        returnObject = NodePathCollection.NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_reparentTo_ptrNodePath_ptrConstNodePath_int(self, other, sort):
        returnValue = libpanda._inPkJyo4WHK(self.this, other.this, sort)
        return returnValue

    
    def _NodePath__overloaded_reparentTo_ptrNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyozsyP(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath_int(self, other, sort):
        returnValue = libpanda._inPkJyokn7s(self.this, other.this, sort)
        return returnValue

    
    def _NodePath__overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyowFTN(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath_int(self, other, sort):
        returnValue = libpanda._inPkJyo1Mo6(self.this, other.this, sort)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoTlPD(self.this, other.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_instanceUnderNode_ptrConstNodePath_ptrConstNodePath_atomicstring_int(self, other, name, sort):
        returnValue = libpanda._inPkJyoHSFZ(self.this, other.this, name, sort)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_instanceUnderNode_ptrConstNodePath_ptrConstNodePath_atomicstring(self, other, name):
        returnValue = libpanda._inPkJyocsm_(self.this, other.this, name)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_copyTo_ptrConstNodePath_ptrConstNodePath_int(self, other, sort):
        returnValue = libpanda._inPkJyoxTlc(self.this, other.this, sort)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_copyTo_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoqI_l(self.this, other.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_attachNewNode_ptrConstNodePath_ptrPandaNode_int(self, node, sort):
        returnValue = libpanda._inPkJyonUwe(self.this, node.this, sort)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_attachNewNode_ptrConstNodePath_ptrPandaNode(self, node):
        returnValue = libpanda._inPkJyo9EWP(self.this, node.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_attachNewNode_ptrConstNodePath_atomicstring_int(self, name, sort):
        returnValue = libpanda._inPkJyomodl(self.this, name, sort)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_attachNewNode_ptrConstNodePath_atomicstring(self, name):
        returnValue = libpanda._inPkJyo_rj7(self.this, name)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def removeNode(self):
        returnValue = libpanda._inPkJyoliuR(self.this)
        return returnValue

    
    def detachNode(self):
        returnValue = libpanda._inPkJyojfzy(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPkJyooCbM(self.this, out.this)
        return returnValue

    
    def _NodePath__overloaded_ls_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyovoLL(self.this)
        return returnValue

    
    def _NodePath__overloaded_ls_ptrConstNodePath_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPkJyo1zyE(self.this, out.this, indentLevel)
        return returnValue

    
    def _NodePath__overloaded_ls_ptrConstNodePath_ptrOstream(self, out):
        returnValue = libpanda._inPkJyou02a(self.this, out.this)
        return returnValue

    
    def _NodePath__overloaded_getState_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoNd52(self.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_getState_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyou5LY(self.this, other.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setState_ptrConstNodePath_ptrConstNodePath_ptrConstRenderState(self, other, state):
        returnValue = libpanda._inPkJyoVxuD(self.this, other.this, state.this)
        return returnValue

    
    def _NodePath__overloaded_setState_ptrConstNodePath_ptrConstRenderState(self, state):
        returnValue = libpanda._inPkJyoLBDo(self.this, state.this)
        return returnValue

    
    def getNetState(self):
        returnValue = libpanda._inPkJyoxk0S(self.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_getTransform_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoaFez(self.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_getTransform_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyo25iF(self.this, other.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setTransform_ptrConstNodePath_ptrConstNodePath_ptrConstTransformState(self, other, transform):
        returnValue = libpanda._inPkJyoaNiA(self.this, other.this, transform.this)
        return returnValue

    
    def _NodePath__overloaded_setTransform_ptrConstNodePath_ptrConstTransformState(self, transform):
        returnValue = libpanda._inPkJyoSSPr(self.this, transform.this)
        return returnValue

    
    def getNetTransform(self):
        returnValue = libpanda._inPkJyocCm_(self.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setPos_ptrNodePath_ptrConstLVecBase3f(self, pos):
        returnValue = libpanda._inPkJyouVV9(self.this, pos.this)
        return returnValue

    
    def _NodePath__overloaded_setPos_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, pos):
        returnValue = libpanda._inPkJyo3got(self.this, other.this, pos.this)
        return returnValue

    
    def _NodePath__overloaded_setPos_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
        returnValue = libpanda._inPkJyo1iUk(self.this, other.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_setPos_ptrNodePath_float_float_float(self, x, y, z):
        returnValue = libpanda._inPkJyoc4_K(self.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_setX_ptrNodePath_ptrConstNodePath_float(self, other, x):
        returnValue = libpanda._inPkJyoRez_(self.this, other.this, x)
        return returnValue

    
    def _NodePath__overloaded_setX_ptrNodePath_float(self, x):
        returnValue = libpanda._inPkJyocaZh(self.this, x)
        return returnValue

    
    def _NodePath__overloaded_setY_ptrNodePath_ptrConstNodePath_float(self, other, y):
        returnValue = libpanda._inPkJyozKzv(self.this, other.this, y)
        return returnValue

    
    def _NodePath__overloaded_setY_ptrNodePath_float(self, y):
        returnValue = libpanda._inPkJyo2gZR(self.this, y)
        return returnValue

    
    def _NodePath__overloaded_setZ_ptrNodePath_ptrConstNodePath_float(self, other, z):
        returnValue = libpanda._inPkJyoU5zf(self.this, other.this, z)
        return returnValue

    
    def _NodePath__overloaded_setZ_ptrNodePath_float(self, z):
        returnValue = libpanda._inPkJyoYzZB(self.this, z)
        return returnValue

    
    def _NodePath__overloaded_getPos_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoOo4T(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getPos_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoFfLu(self.this, other.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getX_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyo1lol(self.this)
        return returnValue

    
    def _NodePath__overloaded_getX_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyorQU6(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getY_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoaSpV(self.this)
        return returnValue

    
    def _NodePath__overloaded_getY_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoJEUq(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getZ_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoxcoF(self.this)
        return returnValue

    
    def _NodePath__overloaded_getZ_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoo5Ua(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_setHpr_ptrNodePath_ptrConstLVecBase3f(self, hpr):
        returnValue = libpanda._inPkJyoEdk4(self.this, hpr.this)
        return returnValue

    
    def _NodePath__overloaded_setHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, hpr):
        returnValue = libpanda._inPkJyoJo3o(self.this, other.this, hpr.this)
        return returnValue

    
    def _NodePath__overloaded_setHpr_ptrNodePath_ptrConstNodePath_float_float_float(self, other, h, p, r):
        returnValue = libpanda._inPkJyoablf(self.this, other.this, h, p, r)
        return returnValue

    
    def _NodePath__overloaded_setHpr_ptrNodePath_float_float_float(self, h, p, r):
        returnValue = libpanda._inPkJyoGhOG(self.this, h, p, r)
        return returnValue

    
    def _NodePath__overloaded_setH_ptrNodePath_ptrConstNodePath_float(self, other, h):
        returnValue = libpanda._inPkJyo1Wu_(self.this, other.this, h)
        return returnValue

    
    def _NodePath__overloaded_setH_ptrNodePath_float(self, h):
        returnValue = libpanda._inPkJyo4SUh(self.this, h)
        return returnValue

    
    def _NodePath__overloaded_setP_ptrNodePath_ptrConstNodePath_float(self, other, p):
        returnValue = libpanda._inPkJyoDyw_(self.this, other.this, p)
        return returnValue

    
    def _NodePath__overloaded_setP_ptrNodePath_float(self, p):
        returnValue = libpanda._inPkJyou_Xh(self.this, p)
        return returnValue

    
    def _NodePath__overloaded_setR_ptrNodePath_ptrConstNodePath_float(self, other, r):
        returnValue = libpanda._inPkJyoGVwf(self.this, other.this, r)
        return returnValue

    
    def _NodePath__overloaded_setR_ptrNodePath_float(self, r):
        returnValue = libpanda._inPkJyoqXXB(self.this, r)
        return returnValue

    
    def _NodePath__overloaded_getHpr_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyokhJP(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getHpr_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyofUap(self.this, other.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getHpr_ptrConstNodePath_ptrConstNodePath_float(self, other, roll):
        returnValue = libpanda._inPkJyo_Eqn(self.this, other.this, roll)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getHpr_ptrConstNodePath_float(self, roll):
        returnValue = libpanda._inPkJyovgkH(self.this, roll)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getH_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoRtjl(self.this)
        return returnValue

    
    def _NodePath__overloaded_getH_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoHZP6(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getP_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoDJll(self.this)
        return returnValue

    
    def _NodePath__overloaded_getP_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoV1R6(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getR_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoHwlF(self.this)
        return returnValue

    
    def _NodePath__overloaded_getR_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoWcRa(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_setQuat_ptrNodePath_ptrConstLQuaternionf(self, quat):
        returnValue = libpanda._inPkJyowJgI(self.this, quat.this)
        return returnValue

    
    def _NodePath__overloaded_setQuat_ptrNodePath_ptrConstNodePath_ptrConstLQuaternionf(self, other, quat):
        returnValue = libpanda._inPkJyoJI60(self.this, other.this, quat.this)
        return returnValue

    
    def _NodePath__overloaded_getQuat_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyowDPW(self.this)
        import Quat
        returnObject = Quat.Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getQuat_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoCURf(self.this, other.this)
        import Quat
        returnObject = Quat.Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_setScale_ptrNodePath_ptrConstLVecBase3f(self, scale):
        returnValue = libpanda._inPkJyoYaRp(self.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, scale):
        returnValue = libpanda._inPkJyouef1(self.this, other.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setScale_ptrNodePath_ptrConstNodePath_float_float_float(self, other, sx, sy, sz):
        returnValue = libpanda._inPkJyoyK_k(self.this, other.this, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setScale_ptrNodePath_float(self, scale):
        returnValue = libpanda._inPkJyouTLn(self.this, scale)
        return returnValue

    
    def _NodePath__overloaded_setScale_ptrNodePath_float_float_float(self, sx, sy, sz):
        returnValue = libpanda._inPkJyoMsGl(self.this, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setSx_ptrNodePath_ptrConstNodePath_float(self, other, sx):
        returnValue = libpanda._inPkJyopi3_(self.this, other.this, sx)
        return returnValue

    
    def _NodePath__overloaded_setSx_ptrNodePath_float(self, sx):
        returnValue = libpanda._inPkJyoFtIx(self.this, sx)
        return returnValue

    
    def _NodePath__overloaded_setSy_ptrNodePath_ptrConstNodePath_float(self, other, sy):
        returnValue = libpanda._inPkJyohVB_(self.this, other.this, sy)
        return returnValue

    
    def _NodePath__overloaded_setSy_ptrNodePath_float(self, sy):
        returnValue = libpanda._inPkJyodaRx(self.this, sy)
        return returnValue

    
    def _NodePath__overloaded_setSz_ptrNodePath_ptrConstNodePath_float(self, other, sz):
        returnValue = libpanda._inPkJyo5EL_(self.this, other.this, sz)
        return returnValue

    
    def _NodePath__overloaded_setSz_ptrNodePath_float(self, sz):
        returnValue = libpanda._inPkJyoVLbx(self.this, sz)
        return returnValue

    
    def _NodePath__overloaded_getScale_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyo5djS(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getScale_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyobm1z(self.this, other.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getSx_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyon63U(self.this)
        return returnValue

    
    def _NodePath__overloaded_getSx_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoDXrr(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getSy_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyovrBV(self.this)
        return returnValue

    
    def _NodePath__overloaded_getSy_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoLE1r(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_getSz_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoXULV(self.this)
        return returnValue

    
    def _NodePath__overloaded_getSz_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyoT18r(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(self, pos, hpr):
        returnValue = libpanda._inPkJyo_KIO(self.this, pos.this, hpr.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other, pos, hpr):
        returnValue = libpanda._inPkJyobgSC(self.this, other.this, pos.this, hpr.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float(self, other, x, y, z, h, p, r):
        returnValue = libpanda._inPkJyogbI1(self.this, other.this, x, y, z, h, p, r)
        return returnValue

    
    def _NodePath__overloaded_setPosHpr_ptrNodePath_float_float_float_float_float_float(self, x, y, z, h, p, r):
        returnValue = libpanda._inPkJyoFbxa(self.this, x, y, z, h, p, r)
        return returnValue

    
    def _NodePath__overloaded_setHprScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(self, hpr, scale):
        returnValue = libpanda._inPkJyoeWuA(self.this, hpr.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setHprScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other, hpr, scale):
        returnValue = libpanda._inPkJyoSEr7(self.this, other.this, hpr.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setHprScale_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float(self, other, h, p, r, sx, sy, sz):
        returnValue = libpanda._inPkJyo4kfC(self.this, other.this, h, p, r, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setHprScale_ptrNodePath_float_float_float_float_float_float(self, h, p, r, sx, sy, sz):
        returnValue = libpanda._inPkJyoXIYi(self.this, h, p, r, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(self, pos, hpr, scale):
        returnValue = libpanda._inPkJyoWLWQ(self.this, pos.this, hpr.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other, pos, hpr, scale):
        returnValue = libpanda._inPkJyo6XbK(self.this, other.this, pos.this, hpr.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float_float_float_float(self, other, x, y, z, h, p, r, sx, sy, sz):
        returnValue = libpanda._inPkJyoVHTJ(self.this, other.this, x, y, z, h, p, r, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setPosHprScale_ptrNodePath_float_float_float_float_float_float_float_float_float(self, x, y, z, h, p, r, sx, sy, sz):
        returnValue = libpanda._inPkJyog3Bw(self.this, x, y, z, h, p, r, sx, sy, sz)
        return returnValue

    
    def _NodePath__overloaded_setPosQuatScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f(self, pos, quat, scale):
        returnValue = libpanda._inPkJyolcNQ(self.this, pos.this, quat.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setPosQuatScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f(self, other, pos, quat, scale):
        returnValue = libpanda._inPkJyoAbZX(self.this, other.this, pos.this, quat.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setMat_ptrNodePath_ptrConstLMatrix4f(self, mat):
        returnValue = libpanda._inPkJyo6Rbe(self.this, mat.this)
        return returnValue

    
    def _NodePath__overloaded_setMat_ptrNodePath_ptrConstNodePath_ptrConstLMatrix4f(self, other, mat):
        returnValue = libpanda._inPkJyoe6vZ(self.this, other.this, mat.this)
        return returnValue

    
    def clearMat(self):
        returnValue = libpanda._inPkJyoZ8BU(self.this)
        return returnValue

    
    def hasMat(self):
        returnValue = libpanda._inPkJyovM1u(self.this)
        return returnValue

    
    def _NodePath__overloaded_getMat_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoIMoG(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NodePath__overloaded_getMat_ptrConstNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyo8p5g(self.this, other.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasColorScale(self):
        returnValue = libpanda._inPkJyoi9q2(self.this)
        return returnValue

    
    def clearColorScale(self):
        returnValue = libpanda._inPkJyoKGLo(self.this)
        return returnValue

    
    def _NodePath__overloaded_setColorScale_ptrNodePath_ptrConstLVecBase4f(self, scale):
        returnValue = libpanda._inPkJyoiG1C(self.this, scale.this)
        return returnValue

    
    def _NodePath__overloaded_setColorScale_ptrNodePath_float_float_float_float(self, sx, sy, sz, sa):
        returnValue = libpanda._inPkJyoUFGH(self.this, sx, sy, sz, sa)
        return returnValue

    
    def setSr(self, sr):
        returnValue = libpanda._inPkJyoVANw(self.this, sr)
        return returnValue

    
    def setSg(self, sg):
        returnValue = libpanda._inPkJyoNqiu(self.this, sg)
        return returnValue

    
    def setSb(self, sb):
        returnValue = libpanda._inPkJyoV_xt(self.this, sb)
        return returnValue

    
    def setSa(self, sa):
        returnValue = libpanda._inPkJyodBnt(self.this, sa)
        return returnValue

    
    def getColorScale(self):
        returnValue = libpanda._inPkJyoH9dO(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getSr(self):
        returnValue = libpanda._inPkJyoXd9T(self.this)
        return returnValue

    
    def getSg(self):
        returnValue = libpanda._inPkJyo_7RS(self.this)
        return returnValue

    
    def getSb(self):
        returnValue = libpanda._inPkJyoXPhR(self.this)
        return returnValue

    
    def getSa(self):
        returnValue = libpanda._inPkJyoveXR(self.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, point, up):
        returnValue = libpanda._inPkJyovdrT(self.this, point.this, up.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstLPoint3f(self, point):
        returnValue = libpanda._inPkJyoOO_M(self.this, point.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, other, point, up):
        returnValue = libpanda._inPkJyoCkNd(self.this, other.this, point.this, up.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(self, other, point):
        returnValue = libpanda._inPkJyosdPC(self.this, other.this, point.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyo72Ls(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
        returnValue = libpanda._inPkJyovoUy(self.this, other.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_lookAt_ptrNodePath_float_float_float(self, x, y, z):
        returnValue = libpanda._inPkJyoTR_Y(self.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, point, up):
        returnValue = libpanda._inPkJyo45wG(self.this, point.this, up.this)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstLPoint3f(self, point):
        returnValue = libpanda._inPkJyoJ5su(self.this, point.this)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, other, point, up):
        returnValue = libpanda._inPkJyoA0_3(self.this, other.this, point.this, up.this)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(self, other, point):
        returnValue = libpanda._inPkJyo1SnX(self.this, other.this, point.this)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath(self, other):
        returnValue = libpanda._inPkJyowIWV(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
        returnValue = libpanda._inPkJyozOob(self.this, other.this, x, y, z)
        return returnValue

    
    def _NodePath__overloaded_headsUp_ptrNodePath_float_float_float(self, x, y, z):
        returnValue = libpanda._inPkJyoeJov(self.this, x, y, z)
        return returnValue

    
    def getRelativePoint(self, other, point):
        returnValue = libpanda._inPkJyoA3Mh(self.this, other.this, point.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRelativeVector(self, other, vec):
        returnValue = libpanda._inPkJyojxa9(self.this, other.this, vec.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getDistance(self, other):
        returnValue = libpanda._inPkJyogctf(self.this, other.this)
        return returnValue

    
    def _NodePath__overloaded_setColor_ptrNodePath_ptrConstLVecBase4f_int(self, color, priority):
        returnValue = libpanda._inPkJyobdvm(self.this, color.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setColor_ptrNodePath_ptrConstLVecBase4f(self, color):
        returnValue = libpanda._inPkJyoU3Zs(self.this, color.this)
        return returnValue

    
    def _NodePath__overloaded_setColor_ptrNodePath_float_float_float_float_int(self, r, g, b, a, priority):
        returnValue = libpanda._inPkJyo366r(self.this, r, g, b, a, priority)
        return returnValue

    
    def _NodePath__overloaded_setColor_ptrNodePath_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPkJyoxcaQ(self.this, r, g, b, a)
        return returnValue

    
    def _NodePath__overloaded_setColor_ptrNodePath_float_float_float(self, r, g, b):
        returnValue = libpanda._inPkJyoQ4OM(self.this, r, g, b)
        return returnValue

    
    def _NodePath__overloaded_setColorOff_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPkJyox27z(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setColorOff_ptrNodePath(self):
        returnValue = libpanda._inPkJyoE1gC(self.this)
        return returnValue

    
    def clearColor(self):
        returnValue = libpanda._inPkJyo2mr9(self.this)
        return returnValue

    
    def hasColor(self):
        returnValue = libpanda._inPkJyoYz4h(self.this)
        return returnValue

    
    def getColor(self):
        returnValue = libpanda._inPkJyolzr5(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_setBin_ptrNodePath_atomicstring_int_int(self, binName, drawOrder, priority):
        returnValue = libpanda._inPkJyoxqDK(self.this, binName, drawOrder, priority)
        return returnValue

    
    def _NodePath__overloaded_setBin_ptrNodePath_atomicstring_int(self, binName, drawOrder):
        returnValue = libpanda._inPkJyoZBGG(self.this, binName, drawOrder)
        return returnValue

    
    def clearBin(self):
        returnValue = libpanda._inPkJyobzEW(self.this)
        return returnValue

    
    def hasBin(self):
        returnValue = libpanda._inPkJyoTmsC(self.this)
        return returnValue

    
    def getBinName(self):
        returnValue = libpanda._inPkJyoKAFg(self.this)
        return returnValue

    
    def getBinDrawOrder(self):
        returnValue = libpanda._inPkJyo3Nw9(self.this)
        return returnValue

    
    def _NodePath__overloaded_setTexture_ptrNodePath_ptrTexture_int(self, tex, priority):
        returnValue = libpanda._inPkJyoEEvx(self.this, tex.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setTexture_ptrNodePath_ptrTexture(self, tex):
        returnValue = libpanda._inPkJyodhTm(self.this, tex.this)
        return returnValue

    
    def _NodePath__overloaded_setTextureOff_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPkJyow4bU(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setTextureOff_ptrNodePath(self):
        returnValue = libpanda._inPkJyo_4vA(self.this)
        return returnValue

    
    def clearTexture(self):
        returnValue = libpanda._inPkJyoMNBp(self.this)
        return returnValue

    
    def hasTexture(self):
        returnValue = libpanda._inPkJyoqlwf(self.this)
        return returnValue

    
    def hasTextureOff(self):
        returnValue = libpanda._inPkJyoyE64(self.this)
        return returnValue

    
    def getTexture(self):
        returnValue = libpanda._inPkJyoMll3(self.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findTexture(self, name):
        returnValue = libpanda._inPkJyoj98A(self.this, name)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_findAllTextures_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyo_z1D(self.this)
        import TextureCollection
        returnObject = TextureCollection.TextureCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_findAllTextures_ptrConstNodePath_atomicstring(self, name):
        returnValue = libpanda._inPkJyoEW3S(self.this, name)
        import TextureCollection
        returnObject = TextureCollection.TextureCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_setMaterial_ptrNodePath_ptrMaterial_int(self, tex, priority):
        returnValue = libpanda._inPkJyocZam(self.this, tex.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setMaterial_ptrNodePath_ptrMaterial(self, tex):
        returnValue = libpanda._inPkJyo3Xcl(self.this, tex.this)
        return returnValue

    
    def _NodePath__overloaded_setMaterialOff_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPkJyogcpR(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setMaterialOff_ptrNodePath(self):
        returnValue = libpanda._inPkJyo_bEb(self.this)
        return returnValue

    
    def clearMaterial(self):
        returnValue = libpanda._inPkJyoOVUw(self.this)
        return returnValue

    
    def hasMaterial(self):
        returnValue = libpanda._inPkJyoW_e6(self.this)
        return returnValue

    
    def getMaterial(self):
        returnValue = libpanda._inPkJyor_RS(self.this)
        import Material
        returnObject = Material.Material(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setFog_ptrNodePath_ptrFog_int(self, fog, priority):
        returnValue = libpanda._inPkJyomIDI(self.this, fog.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setFog_ptrNodePath_ptrFog(self, fog):
        returnValue = libpanda._inPkJyovA0X(self.this, fog.this)
        return returnValue

    
    def _NodePath__overloaded_setFogOff_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPkJyo_qa5(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setFogOff_ptrNodePath(self):
        returnValue = libpanda._inPkJyoegI_(self.this)
        return returnValue

    
    def clearFog(self):
        returnValue = libpanda._inPkJyoOL5h(self.this)
        return returnValue

    
    def hasFog(self):
        returnValue = libpanda._inPkJyoK3dh(self.this)
        return returnValue

    
    def hasFogOff(self):
        returnValue = libpanda._inPkJyoQW1z(self.this)
        return returnValue

    
    def getFog(self):
        returnValue = libpanda._inPkJyoX3Q5(self.this)
        import Fog
        returnObject = Fog.Fog(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def _NodePath__overloaded_setRenderModeWireframe_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPkJyo3mJB(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setRenderModeWireframe_ptrNodePath(self):
        returnValue = libpanda._inPkJyoF5Vy(self.this)
        return returnValue

    
    def _NodePath__overloaded_setRenderModeFilled_ptrNodePath_int(self, priority):
        returnValue = libpanda._inPkJyoFdFx(self.this, priority)
        return returnValue

    
    def _NodePath__overloaded_setRenderModeFilled_ptrNodePath(self):
        returnValue = libpanda._inPkJyoMX6K(self.this)
        return returnValue

    
    def clearRenderMode(self):
        returnValue = libpanda._inPkJyo65TZ(self.this)
        return returnValue

    
    def hasRenderMode(self):
        returnValue = libpanda._inPkJyonDaf(self.this)
        return returnValue

    
    def _NodePath__overloaded_setTwoSided_ptrNodePath_bool_int(self, twoSided, priority):
        returnValue = libpanda._inPkJyoVKd_(self.this, twoSided, priority)
        return returnValue

    
    def _NodePath__overloaded_setTwoSided_ptrNodePath_bool(self, twoSided):
        returnValue = libpanda._inPkJyo_M_e(self.this, twoSided)
        return returnValue

    
    def clearTwoSided(self):
        returnValue = libpanda._inPkJyooJBF(self.this)
        return returnValue

    
    def hasTwoSided(self):
        returnValue = libpanda._inPkJyootTb(self.this)
        return returnValue

    
    def getTwoSided(self):
        returnValue = libpanda._inPkJyoGtGz(self.this)
        return returnValue

    
    def _NodePath__overloaded_setDepthTest_ptrNodePath_bool_int(self, depthTest, priority):
        returnValue = libpanda._inPkJyoY7DP(self.this, depthTest, priority)
        return returnValue

    
    def _NodePath__overloaded_setDepthTest_ptrNodePath_bool(self, depthTest):
        returnValue = libpanda._inPkJyo3UQ_(self.this, depthTest)
        return returnValue

    
    def clearDepthTest(self):
        returnValue = libpanda._inPkJyoDMNz(self.this)
        return returnValue

    
    def hasDepthTest(self):
        returnValue = libpanda._inPkJyogl7H(self.this)
        return returnValue

    
    def getDepthTest(self):
        returnValue = libpanda._inPkJyoNiuf(self.this)
        return returnValue

    
    def _NodePath__overloaded_setDepthWrite_ptrNodePath_bool_int(self, depthWrite, priority):
        returnValue = libpanda._inPkJyoUxkt(self.this, depthWrite, priority)
        return returnValue

    
    def _NodePath__overloaded_setDepthWrite_ptrNodePath_bool(self, depthWrite):
        returnValue = libpanda._inPkJyoDDOz(self.this, depthWrite)
        return returnValue

    
    def clearDepthWrite(self):
        returnValue = libpanda._inPkJyowNqE(self.this)
        return returnValue

    
    def hasDepthWrite(self):
        returnValue = libpanda._inPkJyoQs8G(self.this)
        return returnValue

    
    def getDepthWrite(self):
        returnValue = libpanda._inPkJyoTsve(self.this)
        return returnValue

    
    def doBillboardAxis(self, camera, offset):
        returnValue = libpanda._inPkJyoPIal(self.this, camera.this, offset)
        return returnValue

    
    def doBillboardPointEye(self, camera, offset):
        returnValue = libpanda._inPkJyoUkbl(self.this, camera.this, offset)
        return returnValue

    
    def doBillboardPointWorld(self, camera, offset):
        returnValue = libpanda._inPkJyoXJcU(self.this, camera.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardAxis_ptrNodePath_ptrConstNodePath_float(self, camera, offset):
        returnValue = libpanda._inPkJyonoHV(self.this, camera.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardAxis_ptrNodePath_float(self, offset):
        returnValue = libpanda._inPkJyoMHYU(self.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardAxis_ptrNodePath(self):
        returnValue = libpanda._inPkJyowiDy(self.this)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointEye_ptrNodePath_ptrConstNodePath_float(self, camera, offset):
        returnValue = libpanda._inPkJyo3opV(self.this, camera.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointEye_ptrNodePath_float(self, offset):
        returnValue = libpanda._inPkJyog0MU(self.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointEye_ptrNodePath(self):
        returnValue = libpanda._inPkJyoXCeP(self.this)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointWorld_ptrNodePath_ptrConstNodePath_float(self, camera, offset):
        returnValue = libpanda._inPkJyogjg2(self.this, camera.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointWorld_ptrNodePath_float(self, offset):
        returnValue = libpanda._inPkJyoOaqP(self.this, offset)
        return returnValue

    
    def _NodePath__overloaded_setBillboardPointWorld_ptrNodePath(self):
        returnValue = libpanda._inPkJyoKJae(self.this)
        return returnValue

    
    def clearBillboard(self):
        returnValue = libpanda._inPkJyobATv(self.this)
        return returnValue

    
    def hasBillboard(self):
        returnValue = libpanda._inPkJyo0oWg(self.this)
        return returnValue

    
    def _NodePath__overloaded_setCompass_ptrNodePath_ptrConstNodePath(self, reference):
        returnValue = libpanda._inPkJyoMfMs(self.this, reference.this)
        return returnValue

    
    def _NodePath__overloaded_setCompass_ptrNodePath(self):
        returnValue = libpanda._inPkJyomaNt(self.this)
        return returnValue

    
    def clearCompass(self):
        returnValue = libpanda._inPkJyoS898(self.this)
        return returnValue

    
    def hasCompass(self):
        returnValue = libpanda._inPkJyopX5i(self.this)
        return returnValue

    
    def _NodePath__overloaded_setTransparency_ptrNodePath_bool_int(self, transparency, priority):
        returnValue = libpanda._inPkJyoC6cb(self.this, transparency, priority)
        return returnValue

    
    def _NodePath__overloaded_setTransparency_ptrNodePath_bool(self, transparency):
        returnValue = libpanda._inPkJyo_3BQ(self.this, transparency)
        return returnValue

    
    def clearTransparency(self):
        returnValue = libpanda._inPkJyocU7Z(self.this)
        return returnValue

    
    def hasTransparency(self):
        returnValue = libpanda._inPkJyofD3E(self.this)
        return returnValue

    
    def getTransparency(self):
        returnValue = libpanda._inPkJyo4Coc(self.this)
        return returnValue

    
    def adjustAllPriorities(self, adjustment):
        returnValue = libpanda._inPkJyoYlUl(self.this, adjustment)
        return returnValue

    
    def _NodePath__overloaded_show_ptrNodePath(self):
        returnValue = libpanda._inPkJyoAwv_(self.this)
        return returnValue

    
    def _NodePath__overloaded_show_ptrNodePath_ptrBitMask32(self, cameraMask):
        returnValue = libpanda._inPkJyo5Srv(self.this, cameraMask.this)
        return returnValue

    
    def _NodePath__overloaded_hide_ptrNodePath(self):
        returnValue = libpanda._inPkJyooDIm(self.this)
        return returnValue

    
    def _NodePath__overloaded_hide_ptrNodePath_ptrBitMask32(self, cameraMask):
        returnValue = libpanda._inPkJyonwFX(self.this, cameraMask.this)
        return returnValue

    
    def _NodePath__overloaded_isHidden_ptrConstNodePath_ptrBitMask32(self, cameraMask):
        returnValue = libpanda._inPkJyo9FXE(self.this, cameraMask.this)
        return returnValue

    
    def _NodePath__overloaded_isHidden_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoYTUU(self.this)
        return returnValue

    
    def _NodePath__overloaded_getHiddenAncestor_ptrConstNodePath_ptrBitMask32(self, cameraMask):
        returnValue = libpanda._inPkJyonaCb(self.this, cameraMask.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePath__overloaded_getHiddenAncestor_ptrConstNodePath(self):
        returnValue = libpanda._inPkJyoICma(self.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def stash(self):
        returnValue = libpanda._inPkJyoinzQ(self.this)
        return returnValue

    
    def unstash(self):
        returnValue = libpanda._inPkJyoNkf6(self.this)
        return returnValue

    
    def isStashed(self):
        returnValue = libpanda._inPkJyo_PEj(self.this)
        return returnValue

    
    def getStashedAncestor(self):
        returnValue = libpanda._inPkJyoZTAQ(self.this)
        returnObject = NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def eq(self, other):
        returnValue = libpanda._inPkJyoyIl9(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPkJyoQOU9(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPkJyoP90s(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpanda._inPkJyoGPj2(self.this, other.this)
        return returnValue

    
    def verifyComplete(self):
        returnValue = libpanda._inPkJyoUqrp(self.this)
        return returnValue

    
    def _NodePath__overloaded_prepareScene_ptrNodePath_ptrGraphicsStateGuardianBase_bool(self, gsg, forceRetainedMode):
        returnValue = libpanda._inPkJyoe_I2(self.this, gsg.this, forceRetainedMode)
        return returnValue

    
    def _NodePath__overloaded_prepareScene_ptrNodePath_ptrGraphicsStateGuardianBase(self, gsg):
        returnValue = libpanda._inPkJyo1HH0(self.this, gsg.this)
        return returnValue

    
    def showBounds(self):
        returnValue = libpanda._inPkJyo1psR(self.this)
        return returnValue

    
    def hideBounds(self):
        returnValue = libpanda._inPkJyo1fG5(self.this)
        return returnValue

    
    def getBounds(self):
        returnValue = libpanda._inPkJyopOSR(self.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def forceRecomputeBounds(self):
        returnValue = libpanda._inPkJyotE3U(self.this)
        return returnValue

    
    def writeBounds(self, out):
        returnValue = libpanda._inPkJyo2vwc(self.this, out.this)
        return returnValue

    
    def calcTightBounds(self, minPoint, maxPoint):
        returnValue = libpanda._inPkJyoopR_(self.this, minPoint.this, maxPoint.this)
        return returnValue

    
    def flattenLight(self):
        returnValue = libpanda._inPkJyoznLC(self.this)
        return returnValue

    
    def flattenMedium(self):
        returnValue = libpanda._inPkJyotVep(self.this)
        return returnValue

    
    def flattenStrong(self):
        returnValue = libpanda._inPkJyogdaT(self.this)
        return returnValue

    
    def writeBamFile(self, filename):
        returnValue = libpanda._inPkJyoDjrd(self.this, filename)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_constructor()
        elif numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.StringType):
                return self._NodePath__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._NodePath__overloaded_constructor_ptrPandaNode(_args[0])
            elif isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_constructor_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <PandaNode.PandaNode> <NodePath> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                import PandaNode
                if isinstance(_args[1], PandaNode.PandaNode):
                    return self._NodePath__overloaded_constructor_ptrConstNodePath_ptrPandaNode(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <PandaNode.PandaNode> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def setPosQuatScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                import Quat
                if isinstance(_args[1], Quat.Quat):
                    import VBase3
                    if isinstance(_args[2], VBase3.VBase3):
                        return self._NodePath__overloaded_setPosQuatScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Quat.Quat> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 4:
            if isinstance(_args[0], NodePath):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    import Quat
                    if isinstance(_args[2], Quat.Quat):
                        import VBase3
                        if isinstance(_args[3], VBase3.VBase3):
                            return self._NodePath__overloaded_setPosQuatScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLQuaternionf_ptrConstLVecBase3f(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Quat.Quat> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

    
    def getHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getHpr_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_getHpr_ptrConstNodePath_float(_args[0])
            elif isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getHpr_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <NodePath> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_getHpr_ptrConstNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def setTexture(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Texture
            if isinstance(_args[0], Texture.Texture):
                return self._NodePath__overloaded_setTexture_ptrNodePath_ptrTexture(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Texture.Texture> '
        elif numArgs == 2:
            import Texture
            if isinstance(_args[0], Texture.Texture):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setTexture_ptrNodePath_ptrTexture_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Texture.Texture> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getPos_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getPos_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def show(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_show_ptrNodePath()
        elif numArgs == 1:
            import BitMask32
            if isinstance(_args[0], BitMask32.BitMask32):
                return self._NodePath__overloaded_show_ptrNodePath_ptrBitMask32(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <BitMask32.BitMask32> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setTransform(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import TransformState
            if isinstance(_args[0], TransformState.TransformState):
                return self._NodePath__overloaded_setTransform_ptrConstNodePath_ptrConstTransformState(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <TransformState.TransformState> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                import TransformState
                if isinstance(_args[1], TransformState.TransformState):
                    return self._NodePath__overloaded_setTransform_ptrConstNodePath_ptrConstNodePath_ptrConstTransformState(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <TransformState.TransformState> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._NodePath__overloaded_setHpr_ptrNodePath_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._NodePath__overloaded_setHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._NodePath__overloaded_setHpr_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._NodePath__overloaded_setHpr_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def setScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setScale_ptrNodePath_float(_args[0])
            elif isinstance(_args[0], VBase3.VBase3):
                return self._NodePath__overloaded_setScale_ptrNodePath_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._NodePath__overloaded_setScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._NodePath__overloaded_setScale_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._NodePath__overloaded_setScale_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def getX(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getX_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getX_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def instanceTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def reparentTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_reparentTo_ptrNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_reparentTo_ptrNodePath_ptrConstNodePath_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def wrtReparentTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def lookAt(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstLPoint3f(_args[0])
            elif isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
        elif numArgs == 2:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                import Vec3
                if isinstance(_args[1], Vec3.Vec3):
                    return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
            elif isinstance(_args[0], NodePath):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._NodePath__overloaded_lookAt_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            elif isinstance(_args[0], NodePath):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    import Vec3
                    if isinstance(_args[2], Vec3.Vec3):
                        return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <NodePath> '
        elif numArgs == 4:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._NodePath__overloaded_lookAt_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def headsUp(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstLPoint3f(_args[0])
            elif isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
        elif numArgs == 2:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                import Vec3
                if isinstance(_args[1], Vec3.Vec3):
                    return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
            elif isinstance(_args[0], NodePath):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._NodePath__overloaded_headsUp_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            elif isinstance(_args[0], NodePath):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    import Vec3
                    if isinstance(_args[2], Vec3.Vec3):
                        return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <NodePath> '
        elif numArgs == 4:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._NodePath__overloaded_headsUp_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def setFog(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Fog
            if isinstance(_args[0], Fog.Fog):
                return self._NodePath__overloaded_setFog_ptrNodePath_ptrFog(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Fog.Fog> '
        elif numArgs == 2:
            import Fog
            if isinstance(_args[0], Fog.Fog):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setFog_ptrNodePath_ptrFog_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Fog.Fog> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getP(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getP_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getP_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setPosHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], NodePath):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[2], VBase3.VBase3):
                        return self._NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 6:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    return self._NodePath__overloaded_setPosHpr_ptrNodePath_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 7:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        return self._NodePath__overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6])
                                    else:
                                        raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 6 7 '

    
    def getR(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getR_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getR_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setState(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import RenderState
            if isinstance(_args[0], RenderState.RenderState):
                return self._NodePath__overloaded_setState_ptrConstNodePath_ptrConstRenderState(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderState.RenderState> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                import RenderState
                if isinstance(_args[1], RenderState.RenderState):
                    return self._NodePath__overloaded_setState_ptrConstNodePath_ptrConstNodePath_ptrConstRenderState(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <RenderState.RenderState> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setMat(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4
            if isinstance(_args[0], Mat4.Mat4):
                return self._NodePath__overloaded_setMat_ptrNodePath_ptrConstLMatrix4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4.Mat4> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                import Mat4
                if isinstance(_args[1], Mat4.Mat4):
                    return self._NodePath__overloaded_setMat_ptrNodePath_ptrConstNodePath_ptrConstLMatrix4f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Mat4.Mat4> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getTransform(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getTransform_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getTransform_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setBin(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setBin_ptrNodePath_atomicstring_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._NodePath__overloaded_setBin_ptrNodePath_atomicstring_int_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def getZ(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getZ_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getZ_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setMaterial(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Material
            if isinstance(_args[0], Material.Material):
                return self._NodePath__overloaded_setMaterial_ptrNodePath_ptrMaterial(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Material.Material> '
        elif numArgs == 2:
            import Material
            if isinstance(_args[0], Material.Material):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setMaterial_ptrNodePath_ptrMaterial_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Material.Material> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setQuat(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Quat
            if isinstance(_args[0], Quat.Quat):
                return self._NodePath__overloaded_setQuat_ptrNodePath_ptrConstLQuaternionf(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Quat.Quat> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                import Quat
                if isinstance(_args[1], Quat.Quat):
                    return self._NodePath__overloaded_setQuat_ptrNodePath_ptrConstNodePath_ptrConstLQuaternionf(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Quat.Quat> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setDepthTest(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setDepthTest_ptrNodePath_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setDepthTest_ptrNodePath_bool_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def findAllTextures(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_findAllTextures_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._NodePath__overloaded_findAllTextures_ptrConstNodePath_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setHprScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._NodePath__overloaded_setHprScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], NodePath):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[2], VBase3.VBase3):
                        return self._NodePath__overloaded_setHprScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 6:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    return self._NodePath__overloaded_setHprScale_ptrNodePath_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 7:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        return self._NodePath__overloaded_setHprScale_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6])
                                    else:
                                        raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 6 7 '

    
    def copyTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_copyTo_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_copyTo_ptrConstNodePath_ptrConstNodePath_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def ls(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_ls_ptrConstNodePath()
        elif numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._NodePath__overloaded_ls_ptrConstNodePath_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_ls_ptrConstNodePath_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def setDepthWrite(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setDepthWrite_ptrNodePath_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setDepthWrite_ptrNodePath_bool_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCompass(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setCompass_ptrNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_setCompass_ptrNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def isHidden(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_isHidden_ptrConstNodePath()
        elif numArgs == 1:
            import BitMask32
            if isinstance(_args[0], BitMask32.BitMask32):
                return self._NodePath__overloaded_isHidden_ptrConstNodePath_ptrBitMask32(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <BitMask32.BitMask32> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def attachNewNode(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.StringType):
                return self._NodePath__overloaded_attachNewNode_ptrConstNodePath_atomicstring(_args[0])
            elif isinstance(_args[0], PandaNode.PandaNode):
                return self._NodePath__overloaded_attachNewNode_ptrConstNodePath_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <PandaNode.PandaNode> '
        elif numArgs == 2:
            import PandaNode
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_attachNewNode_ptrConstNodePath_atomicstring_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            elif isinstance(_args[0], PandaNode.PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_attachNewNode_ptrConstNodePath_ptrPandaNode_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setColorScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._NodePath__overloaded_setColorScale_ptrNodePath_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._NodePath__overloaded_setColorScale_ptrNodePath_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def getState(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getState_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getState_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setSx(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setSx_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setSx_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setSy(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setSy_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setSy_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setSz(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setSz_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setSz_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setMaterialOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setMaterialOff_ptrNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setMaterialOff_ptrNodePath_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setH(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setH_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setH_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setBillboardPointWorld(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setBillboardPointWorld_ptrNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setBillboardPointWorld_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setBillboardPointWorld_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def setP(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setP_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setP_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setTransparency(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setTransparency_ptrNodePath_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setTransparency_ptrNodePath_bool_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setR(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setR_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setR_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setColorOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setColorOff_ptrNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setColorOff_ptrNodePath_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setBillboardPointEye(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setBillboardPointEye_ptrNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setBillboardPointEye_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setBillboardPointEye_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def hide(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_hide_ptrNodePath()
        elif numArgs == 1:
            import BitMask32
            if isinstance(_args[0], BitMask32.BitMask32):
                return self._NodePath__overloaded_hide_ptrNodePath_ptrBitMask32(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <BitMask32.BitMask32> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getScale_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getScale_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setRenderModeWireframe(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setRenderModeWireframe_ptrNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setRenderModeWireframe_ptrNodePath_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setX(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setX_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setX_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setY(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setY_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setY_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setZ(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setZ_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setZ_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._NodePath__overloaded_setColor_ptrNodePath_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 2:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setColor_ptrNodePath_ptrConstLVecBase4f_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._NodePath__overloaded_setColor_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._NodePath__overloaded_setColor_ptrNodePath_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 5:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.IntType):
                                return self._NodePath__overloaded_setColor_ptrNodePath_float_float_float_float_int(_args[0], _args[1], _args[2], _args[3], _args[4])
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 5 '

    
    def getSx(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getSx_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getSx_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getSy(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getSy_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getSy_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getSz(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getSz_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getSz_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def instanceUnderNode(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.StringType):
                    return self._NodePath__overloaded_instanceUnderNode_ptrConstNodePath_ptrConstNodePath_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 3:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.IntType):
                        return self._NodePath__overloaded_instanceUnderNode_ptrConstNodePath_ptrConstNodePath_atomicstring_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setTextureOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setTextureOff_ptrNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setTextureOff_ptrNodePath_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getQuat(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getQuat_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getQuat_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getY(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getY_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getY_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._NodePath__overloaded_setPos_ptrNodePath_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._NodePath__overloaded_setPos_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._NodePath__overloaded_setPos_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._NodePath__overloaded_setPos_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def setBillboardAxis(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setBillboardAxis_ptrNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setBillboardAxis_ptrNodePath_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setBillboardAxis_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def prepareScene(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import GraphicsStateGuardianBase
            if isinstance(_args[0], GraphicsStateGuardianBase.GraphicsStateGuardianBase):
                return self._NodePath__overloaded_prepareScene_ptrNodePath_ptrGraphicsStateGuardianBase(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <GraphicsStateGuardianBase.GraphicsStateGuardianBase> '
        elif numArgs == 2:
            import GraphicsStateGuardianBase
            if isinstance(_args[0], GraphicsStateGuardianBase.GraphicsStateGuardianBase):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_prepareScene_ptrNodePath_ptrGraphicsStateGuardianBase_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <GraphicsStateGuardianBase.GraphicsStateGuardianBase> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getHiddenAncestor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getHiddenAncestor_ptrConstNodePath()
        elif numArgs == 1:
            import BitMask32
            if isinstance(_args[0], BitMask32.BitMask32):
                return self._NodePath__overloaded_getHiddenAncestor_ptrConstNodePath_ptrBitMask32(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <BitMask32.BitMask32> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setRenderModeFilled(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setRenderModeFilled_ptrNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setRenderModeFilled_ptrNodePath_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setFogOff(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_setFogOff_ptrNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setFogOff_ptrNodePath_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getH(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getH_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getH_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getMat(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePath__overloaded_getMat_ptrConstNodePath()
        elif numArgs == 1:
            if isinstance(_args[0], NodePath):
                return self._NodePath__overloaded_getMat_ptrConstNodePath_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setPosHprScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[2], VBase3.VBase3):
                        return self._NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 4:
            if isinstance(_args[0], NodePath):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[2], VBase3.VBase3):
                        import VBase3
                        if isinstance(_args[3], VBase3.VBase3):
                            return self._NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        elif numArgs == 9:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                            if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                return self._NodePath__overloaded_setPosHprScale_ptrNodePath_float_float_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8])
                                            else:
                                                raise TypeError, 'Invalid argument 8, expected one of: <types.FloatType> '
                                        else:
                                            raise TypeError, 'Invalid argument 7, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 10:
            if isinstance(_args[0], NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                            if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                if isinstance(_args[9], types.FloatType) or isinstance(_args[9], types.IntType):
                                                    return self._NodePath__overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8], _args[9])
                                                else:
                                                    raise TypeError, 'Invalid argument 9, expected one of: <types.FloatType> '
                                            else:
                                                raise TypeError, 'Invalid argument 8, expected one of: <types.FloatType> '
                                        else:
                                            raise TypeError, 'Invalid argument 7, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 9 10 '

    
    def setTwoSided(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NodePath__overloaded_setTwoSided_ptrNodePath_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._NodePath__overloaded_setTwoSided_ptrNodePath_bool_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def id(self):
        
        try:
            return self.arc()
        except:
            return self.getKey()


    
    def getName(self):
        node = self.node()
        if hasattr(node, 'getName'):
            return node.getName()
        
        return '<noname>'

    
    def setName(self, name = '<noname>'):
        node = self.node()
        if hasattr(node, 'setName'):
            node.setName(name)
        

    
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

    
    def reversels(self):
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
        import Point3
        v1 = Point3.Point3(0)
        v2 = Point3.Point3(0)
        self.calcTightBounds(v1, v2)
        return (v1, v2)

    
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

    
    def _NodePath__getBlend(self, blendType):
        import LerpBlendHelpers
        if blendType == 'easeIn':
            return LerpBlendHelpers.easeIn
        elif blendType == 'easeOut':
            return LerpBlendHelpers.easeOut
        elif blendType == 'easeInOut':
            return LerpBlendHelpers.easeInOut
        elif blendType == 'noBlend':
            return LerpBlendHelpers.noBlend
        else:
            raise Exception('Error: NodePath.__getBlend: Unknown blend type')

    
    def _NodePath__lerp(self, functorFunc, duration, blendType, taskName = None):
        import Task
        taskMgr = taskMgr
        import TaskManagerGlobal
        
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
            import Lerp
            ClockObject = ClockObject
            import ClockObject
            Task = Task
            cont = cont
            done = done
            import Task
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
        lerpTask.blendType = self._NodePath__getBlend(blendType)
        lerpTask.uponDeath = lerpUponDeath
        if taskName == None:
            return lerpTask
        else:
            taskMgr.add(lerpTask, taskName)
            return lerpTask

    
    def _NodePath__autoLerp(self, functorFunc, time, blendType, taskName):
        import AutonomousLerp
        functor = functorFunc()
        lerp = AutonomousLerp.AutonomousLerp(functor, time, self._NodePath__getBlend(blendType), base.eventHandler)
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
            import ColorLerpFunctor
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
            import ColorLerpFunctor
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
            import ColorLerpFunctor
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
            import ColorLerpFunctor
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
            import ColorScaleLerpFunctor
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
            import ColorScaleLerpFunctor
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
            import ColorScaleLerpFunctor
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
            import ColorScaleLerpFunctor
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
            import HprLerpFunctor
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
            import HprLerpFunctor
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
            import PosLerpFunctor
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
            import PosLerpFunctor
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
            import PosHprLerpFunctor
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
            import PosHprLerpFunctor
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
            import PosHprScaleLerpFunctor
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
            import ScaleLerpFunctor
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
            import ScaleLerpFunctor
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
        base.startTk()
        base.startDirect()
        import Placer
        return Placer.place(self)

    
    def explore(self):
        base.startTk()
        base.startDirect()
        import SceneGraphExplorer
        return SceneGraphExplorer.explore(self)

    
    def rgbPanel(self, cb = None):
        base.startTk()
        import Slider
        return Slider.rgbPanel(self, cb)

    
    def select(self):
        base.startTk()
        base.startDirect()
        direct.select(self)

    
    def deselect(self):
        base.startTk()
        base.startDirect()
        direct.deselect(self)

    
    def setAlphaScale(self, alpha):
        self.setColorScale(1, 1, 1, alpha)

    
    def setAllColorScale(self, color):
        self.setColorScale(color, color, color, 1)

    
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
        import LerpInterval
        return LerpInterval.LerpPosInterval(self, *args, **args)

    
    def hprInterval(self, *args, **kw):
        import LerpInterval
        return LerpInterval.LerpHprInterval(self, *args, **args)

    
    def scaleInterval(self, *args, **kw):
        import LerpInterval
        return LerpInterval.LerpScaleInterval(self, *args, **args)

    
    def posHprInterval(self, *args, **kw):
        import LerpInterval
        return LerpInterval.LerpPosHprInterval(self, *args, **args)

    
    def hprScaleInterval(self, *args, **kw):
        import LerpInterval
        return LerpInterval.LerpHprScaleInterval(self, *args, **args)

    
    def posHprScaleInterval(self, *args, **kw):
        import LerpInterval
        return LerpInterval.LerpPosHprScaleInterval(self, *args, **args)

    
    def colorInterval(self, *args, **kw):
        import LerpInterval
        return LerpInterval.LerpColorInterval(self, *args, **args)

    
    def colorScaleInterval(self, *args, **kw):
        import LerpInterval
        return LerpInterval.LerpColorScaleInterval(self, *args, **args)


