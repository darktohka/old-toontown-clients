# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggGroupNode
import EggRenderMode
import EggTransform3d

class EggGroup(EggGroupNode.EggGroupNode, EggRenderMode.EggRenderMode, EggTransform3d.EggTransform3d, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    GTJoint = 2
    GTGroup = 0
    GTInstance = 1
    GTInvalid = -1
    DTNone = 0
    DTNosync = 8
    DTDefault = 12
    DTSync = 4
    DCDefault = 48
    DCLocal = 16
    DCNet = 32
    DCNone = 0
    BTPointCameraRelative = 64
    BTPointWorldRelative = 128
    BTNone = 0
    BTAxis = 32
    CSTSphere = 262144
    CSTTube = 327680
    CSTInvSphere = 393216
    CSTPlane = 65536
    CSTPolygon = 131072
    CSTNone = 0
    CSTPolyset = 196608
    CFTurnstile = 33554432
    CFLevel = 67108864
    CFSolid = 8388608
    CFDescend = 1048576
    CFKeep = 4194304
    CFNone = 0
    CFEvent = 2097152
    CFCenter = 16777216
    CFIntangible = 134217728
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggGroup__overloaded_constructor_ptrConstEggGroup(self, copy):
        self.this = libpandaegg._inPkAOMGDad(copy.this)
        self.userManagesMemory = 1

    
    def _EggGroup__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOMA1nz(name)
        self.userManagesMemory = 1

    
    def _EggGroup__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMo0fE()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMHkbq:
            libpandaegg._inPkAOMHkbq(self.this)
        

    
    def stringGroupType(cString):
        returnValue = libpandaegg._inPkAOM4npg(cString)
        return returnValue

    stringGroupType = staticmethod(stringGroupType)
    
    def stringDartType(cString):
        returnValue = libpandaegg._inPkAOMHRvQ(cString)
        return returnValue

    stringDartType = staticmethod(stringDartType)
    
    def stringDcsType(cString):
        returnValue = libpandaegg._inPkAOMSWba(cString)
        return returnValue

    stringDcsType = staticmethod(stringDcsType)
    
    def stringBillboardType(cString):
        returnValue = libpandaegg._inPkAOM5ugT(cString)
        return returnValue

    stringBillboardType = staticmethod(stringBillboardType)
    
    def stringCsType(cString):
        returnValue = libpandaegg._inPkAOMJTFH(cString)
        return returnValue

    stringCsType = staticmethod(stringCsType)
    
    def stringCollideFlags(cString):
        returnValue = libpandaegg._inPkAOMm6lB(cString)
        return returnValue

    stringCollideFlags = staticmethod(stringCollideFlags)
    
    def getClassType():
        returnValue = libpandaegg._inPkAOMSfTP()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOM4lhn(self.this, copy.this)
        returnObject = EggGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def write(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOM4Dn7(self.this, out.this, indentLevel)
        return returnValue

    
    def writeBillboardFlags(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMn03j(self.this, out.this, indentLevel)
        return returnValue

    
    def writeCollideFlags(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMxbxc(self.this, out.this, indentLevel)
        return returnValue

    
    def writeModelFlags(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMxeV_(self.this, out.this, indentLevel)
        return returnValue

    
    def writeSwitchFlags(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMsgHb(self.this, out.this, indentLevel)
        return returnValue

    
    def writeObjectTypes(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOM0xU5(self.this, out.this, indentLevel)
        return returnValue

    
    def writeDecalFlags(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMIFLx(self.this, out.this, indentLevel)
        return returnValue

    
    def writeTags(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMl6kP(self.this, out.this, indentLevel)
        return returnValue

    
    def writeRenderMode(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMeW5J(self.this, out.this, indentLevel)
        return returnValue

    
    def isJoint(self):
        returnValue = libpandaegg._inPkAOMwL5B(self.this)
        return returnValue

    
    def determineAlphaMode(self):
        returnValue = libpandaegg._inPkAOMBkMb(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDepthWriteMode(self):
        returnValue = libpandaegg._inPkAOMmFzS(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDepthTestMode(self):
        returnValue = libpandaegg._inPkAOMTTlV(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineVisibilityMode(self):
        returnValue = libpandaegg._inPkAOMVd5a(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDrawOrder(self):
        returnValue = libpandaegg._inPkAOM76XI(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineBin(self):
        returnValue = libpandaegg._inPkAOMoQnq(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineIndexed(self):
        returnValue = libpandaegg._inPkAOMJ8J_(self.this)
        return returnValue

    
    def setGroupType(self, type):
        returnValue = libpandaegg._inPkAOM_8Pb(self.this, type)
        return returnValue

    
    def getGroupType(self):
        returnValue = libpandaegg._inPkAOMCug2(self.this)
        return returnValue

    
    def isInstanceType(self):
        returnValue = libpandaegg._inPkAOMrrYW(self.this)
        return returnValue

    
    def setBillboardType(self, type):
        returnValue = libpandaegg._inPkAOMPYft(self.this, type)
        return returnValue

    
    def getBillboardType(self):
        returnValue = libpandaegg._inPkAOMUh7T(self.this)
        return returnValue

    
    def setBillboardCenter(self, billboardCenter):
        returnValue = libpandaegg._inPkAOMVkAl(self.this, billboardCenter.this)
        return returnValue

    
    def clearBillboardCenter(self):
        returnValue = libpandaegg._inPkAOMx2ed(self.this)
        return returnValue

    
    def hasBillboardCenter(self):
        returnValue = libpandaegg._inPkAOMVHfQ(self.this)
        return returnValue

    
    def getBillboardCenter(self):
        returnValue = libpandaegg._inPkAOMyHSo(self.this)
        import Point3D
        returnObject = Point3D.Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setCsType(self, type):
        returnValue = libpandaegg._inPkAOMx6Vi(self.this, type)
        return returnValue

    
    def getCsType(self):
        returnValue = libpandaegg._inPkAOMvaDZ(self.this)
        return returnValue

    
    def setCollideFlags(self, flags):
        returnValue = libpandaegg._inPkAOMGbxk(self.this, flags)
        return returnValue

    
    def getCollideFlags(self):
        returnValue = libpandaegg._inPkAOMB6er(self.this)
        return returnValue

    
    def setCollisionName(self, collisionName):
        returnValue = libpandaegg._inPkAOMf_or(self.this, collisionName)
        return returnValue

    
    def clearCollisionName(self):
        returnValue = libpandaegg._inPkAOM2IvZ(self.this)
        return returnValue

    
    def hasCollisionName(self):
        returnValue = libpandaegg._inPkAOMW1Ru(self.this)
        return returnValue

    
    def getCollisionName(self):
        returnValue = libpandaegg._inPkAOMs1EG(self.this)
        return returnValue

    
    def setDcsType(self, type):
        returnValue = libpandaegg._inPkAOM1BYb(self.this, type)
        return returnValue

    
    def getDcsType(self):
        returnValue = libpandaegg._inPkAOM6COw(self.this)
        return returnValue

    
    def setDartType(self, type):
        returnValue = libpandaegg._inPkAOMf8q2(self.this, type)
        return returnValue

    
    def getDartType(self):
        returnValue = libpandaegg._inPkAOMLvy6(self.this)
        return returnValue

    
    def setSwitchFlag(self, flag):
        returnValue = libpandaegg._inPkAOM41Ux(self.this, flag)
        return returnValue

    
    def getSwitchFlag(self):
        returnValue = libpandaegg._inPkAOM0H1c(self.this)
        return returnValue

    
    def setSwitchFps(self, fps):
        returnValue = libpandaegg._inPkAOMlCF0(self.this, fps)
        return returnValue

    
    def getSwitchFps(self):
        returnValue = libpandaegg._inPkAOM8G_G(self.this)
        return returnValue

    
    def addObjectType(self, objectType):
        returnValue = libpandaegg._inPkAOMAKpq(self.this, objectType)
        return returnValue

    
    def clearObjectTypes(self):
        returnValue = libpandaegg._inPkAOMLFHb(self.this)
        return returnValue

    
    def getNumObjectTypes(self):
        returnValue = libpandaegg._inPkAOMJ86I(self.this)
        return returnValue

    
    def getObjectType(self, index):
        returnValue = libpandaegg._inPkAOMa9XK(self.this, index)
        return returnValue

    
    def hasObjectType(self, objectType):
        returnValue = libpandaegg._inPkAOMZ76F(self.this, objectType)
        return returnValue

    
    def removeObjectType(self, objectType):
        returnValue = libpandaegg._inPkAOMOHD5(self.this, objectType)
        return returnValue

    
    def setModelFlag(self, flag):
        returnValue = libpandaegg._inPkAOMGIqq(self.this, flag)
        return returnValue

    
    def getModelFlag(self):
        returnValue = libpandaegg._inPkAOMT2IL(self.this)
        return returnValue

    
    def setTexlistFlag(self, flag):
        returnValue = libpandaegg._inPkAOMxoGr(self.this, flag)
        return returnValue

    
    def getTexlistFlag(self):
        returnValue = libpandaegg._inPkAOMPvu3(self.this)
        return returnValue

    
    def setNofogFlag(self, flag):
        returnValue = libpandaegg._inPkAOMSunb(self.this, flag)
        return returnValue

    
    def getNofogFlag(self):
        returnValue = libpandaegg._inPkAOMA4F8(self.this)
        return returnValue

    
    def setDecalFlag(self, flag):
        returnValue = libpandaegg._inPkAOM_rVD(self.this, flag)
        return returnValue

    
    def getDecalFlag(self):
        returnValue = libpandaegg._inPkAOMhgzj(self.this)
        return returnValue

    
    def setDirectFlag(self, flag):
        returnValue = libpandaegg._inPkAOM_U5j(self.this, flag)
        return returnValue

    
    def getDirectFlag(self):
        returnValue = libpandaegg._inPkAOMn6bP(self.this)
        return returnValue

    
    def setPortalFlag(self, flag):
        returnValue = libpandaegg._inPkAOMQTF_(self.this, flag)
        return returnValue

    
    def getPortalFlag(self):
        returnValue = libpandaegg._inPkAOMkFnp(self.this)
        return returnValue

    
    def setPolylightFlag(self, flag):
        returnValue = libpandaegg._inPkAOMivYc(self.this, flag)
        return returnValue

    
    def getPolylightFlag(self):
        returnValue = libpandaegg._inPkAOMVOiF(self.this)
        return returnValue

    
    def setIndexedFlag(self, flag):
        returnValue = libpandaegg._inPkAOMeROZ(self.this, flag)
        return returnValue

    
    def clearIndexedFlag(self):
        returnValue = libpandaegg._inPkAOM1pLz(self.this)
        return returnValue

    
    def hasIndexedFlag(self):
        returnValue = libpandaegg._inPkAOM_iEO(self.this)
        return returnValue

    
    def getIndexedFlag(self):
        returnValue = libpandaegg._inPkAOMUi3l(self.this)
        return returnValue

    
    def setCollideMask(self, mask):
        returnValue = libpandaegg._inPkAOMT66j(self.this, mask.this)
        return returnValue

    
    def clearCollideMask(self):
        returnValue = libpandaegg._inPkAOML2rQ(self.this)
        return returnValue

    
    def hasCollideMask(self):
        returnValue = libpandaegg._inPkAOMhy6F(self.this)
        return returnValue

    
    def getCollideMask(self):
        returnValue = libpandaegg._inPkAOMGxtd(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setFromCollideMask(self, mask):
        returnValue = libpandaegg._inPkAOMDPij(self.this, mask.this)
        return returnValue

    
    def clearFromCollideMask(self):
        returnValue = libpandaegg._inPkAOMzsDo(self.this)
        return returnValue

    
    def hasFromCollideMask(self):
        returnValue = libpandaegg._inPkAOMPGMA(self.this)
        return returnValue

    
    def getFromCollideMask(self):
        returnValue = libpandaegg._inPkAOMkHBY(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setIntoCollideMask(self, mask):
        returnValue = libpandaegg._inPkAOM_jzD(self.this, mask.this)
        return returnValue

    
    def clearIntoCollideMask(self):
        returnValue = libpandaegg._inPkAOMnw2o(self.this)
        return returnValue

    
    def hasIntoCollideMask(self):
        returnValue = libpandaegg._inPkAOMFwdg(self.this)
        return returnValue

    
    def getIntoCollideMask(self):
        returnValue = libpandaegg._inPkAOMgwQ4(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setLod(self, lod):
        returnValue = libpandaegg._inPkAOMIRO1(self.this, lod.this)
        return returnValue

    
    def clearLod(self):
        returnValue = libpandaegg._inPkAOMq3tX(self.this)
        return returnValue

    
    def hasLod(self):
        returnValue = libpandaegg._inPkAOMXcWg(self.this)
        return returnValue

    
    def getLod(self):
        returnValue = libpandaegg._inPkAOMKcL4(self.this)
        import EggSwitchCondition
        returnObject = EggSwitchCondition.EggSwitchCondition(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setTag(self, key, value):
        returnValue = libpandaegg._inPkAOMAteX(self.this, key, value)
        return returnValue

    
    def getTag(self, key):
        returnValue = libpandaegg._inPkAOMezZY(self.this, key)
        return returnValue

    
    def hasTag(self, key):
        returnValue = libpandaegg._inPkAOM7ymA(self.this, key)
        return returnValue

    
    def clearTag(self, key):
        returnValue = libpandaegg._inPkAOM6Cat(self.this, key)
        return returnValue

    
    def _EggGroup__overloaded_refVertex_ptrEggGroup_ptrEggVertex_double(self, vert, membership):
        returnValue = libpandaegg._inPkAOMHB62(self.this, vert.this, membership)
        return returnValue

    
    def _EggGroup__overloaded_refVertex_ptrEggGroup_ptrEggVertex(self, vert):
        returnValue = libpandaegg._inPkAOMl5JZ(self.this, vert.this)
        return returnValue

    
    def unrefVertex(self, vert):
        returnValue = libpandaegg._inPkAOMEYVk(self.this, vert.this)
        return returnValue

    
    def unrefAllVertices(self):
        returnValue = libpandaegg._inPkAOM7o8l(self.this)
        return returnValue

    
    def getVertexMembership(self, vert):
        returnValue = libpandaegg._inPkAOMu4_n(self.this, vert.this)
        return returnValue

    
    def setVertexMembership(self, vert, membership):
        returnValue = libpandaegg._inPkAOMcwbO(self.this, vert.this, membership)
        return returnValue

    
    def stealVrefs(self, other):
        returnValue = libpandaegg._inPkAOMuK6m(self.this, other.this)
        return returnValue

    
    def testVrefIntegrity(self):
        returnValue = libpandaegg._inPkAOMhtdv(self.this)
        return returnValue

    
    def upcastToEggRenderMode(self):
        returnValue = libpandaegg._inPkAOMyqbi(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToEggTransform3d(self):
        returnValue = libpandaegg._inPkAOMGRUn(self.this)
        import EggTransform3d
        returnObject = EggTransform3d.EggTransform3d(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def empty(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMRZjf(upcastSelf.this)
        return returnValue

    
    def size(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMn_u7(upcastSelf.this)
        return returnValue

    
    def clear(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMdGRB(upcastSelf.this)
        return returnValue

    
    def getFirstChild(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMWCah(upcastSelf.this)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNextChild(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM7zBu(upcastSelf.this)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def addChild(self, node):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMQ_Zu(upcastSelf.this, node.this)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeChild(self, node):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMKOID(upcastSelf.this, node.this)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def stealChildren(self, other):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM0PPR(upcastSelf.this, other.this)
        return returnValue

    
    def findChild(self, name):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMIxZU(upcastSelf.this, name)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasAbsolutePathnames(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMWpyO(upcastSelf.this)
        return returnValue

    
    def resolveFilenames(self, searchpath):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMQMtA(upcastSelf.this, searchpath.this)
        return returnValue

    
    def forceFilenames(self, directory):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMGIQc(upcastSelf.this, directory.this)
        return returnValue

    
    def reverseVertexOrdering(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM1ZhK(upcastSelf.this)
        return returnValue

    
    def _EggGroup__overloaded_recomputeVertexNormals_ptrEggGroupNode_double___enum__CoordinateSystem(self, threshold, cs):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM_XGy(upcastSelf.this, threshold, cs)
        return returnValue

    
    def _EggGroup__overloaded_recomputeVertexNormals_ptrEggGroupNode_double(self, threshold):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMC1bM(upcastSelf.this, threshold)
        return returnValue

    
    def _EggGroup__overloaded_recomputePolygonNormals_ptrEggGroupNode___enum__CoordinateSystem(self, cs):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMxT4d(upcastSelf.this, cs)
        return returnValue

    
    def _EggGroup__overloaded_recomputePolygonNormals_ptrEggGroupNode(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMb2rf(upcastSelf.this)
        return returnValue

    
    def stripNormals(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMtsfH(upcastSelf.this)
        return returnValue

    
    def triangulatePolygons(self, convexAlso):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM0jm4(upcastSelf.this, convexAlso)
        return returnValue

    
    def removeUnusedVertices(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMZcZ9(upcastSelf.this)
        return returnValue

    
    def removeInvalidPrimitives(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMQsA8(upcastSelf.this)
        return returnValue

    
    def recomputeVertexNormals(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggGroup__overloaded_recomputeVertexNormals_ptrEggGroupNode_double(*_args)
        elif numArgs == 2:
            return self._EggGroup__overloaded_recomputeVertexNormals_ptrEggGroupNode_double___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def recomputePolygonNormals(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggGroup__overloaded_recomputePolygonNormals_ptrEggGroupNode(*_args)
        elif numArgs == 1:
            return self._EggGroup__overloaded_recomputePolygonNormals_ptrEggGroupNode___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getParent(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMcWNY(upcastSelf.this)
        import EggGroupNode
        returnObject = EggGroupNode.EggGroupNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getDepth(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMyhAk(upcastSelf.this)
        return returnValue

    
    def isUnderInstance(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM3MCH(upcastSelf.this)
        return returnValue

    
    def isUnderTransform(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMaghw(upcastSelf.this)
        return returnValue

    
    def isLocalCoord(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMyHkj(upcastSelf.this)
        return returnValue

    
    def getVertexFrame(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMtrwF(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFrame(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMsUiB(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexFrameInv(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMN4KR(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFrameInv(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMv1_V(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexToNode(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMXcNr(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeToVertex(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMNv_a(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexFramePtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMv1HP(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFramePtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM_tqL(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexFrameInvPtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM3nvZ(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeFrameInvPtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMKkmK(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVertexToNodePtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMB_1f(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodeToVertexPtr(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM3soP(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def transform(self, mat):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMoQ8D(upcastSelf.this, mat.this)
        return returnValue

    
    def transformVerticesOnly(self, mat):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM2Yja(upcastSelf.this, mat.this)
        return returnValue

    
    def flattenTransforms(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM7nS3(upcastSelf.this)
        return returnValue

    
    def applyTexmats(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMpzMK(upcastSelf.this)
        return returnValue

    
    def isAnimMatrix(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM82MW(upcastSelf.this)
        return returnValue

    
    def parseEgg(self, eggSyntax):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMZKVQ(upcastSelf.this, eggSyntax)
        return returnValue

    
    def testUnderIntegrity(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMp6_k(upcastSelf.this)
        return returnValue

    
    def output(self, out):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMjJfG(upcastSelf.this, out.this)
        return returnValue

    
    def upcastToNamable(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMQtFW(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setUserData(self, userData):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMi4s0(upcastSelf.this, userData.this)
        return returnValue

    
    def getUserData(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMWm2j(upcastSelf.this)
        import EggUserData
        returnObject = EggUserData.EggUserData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggGroup__overloaded_hasUserData_ptrConstEggObject(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMibXq(upcastSelf.this)
        return returnValue

    
    def _EggGroup__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(self, type):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMvhRl(upcastSelf.this, type.this)
        return returnValue

    
    def clearUserData(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM0OqA(upcastSelf.this)
        return returnValue

    
    def hasUserData(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggGroup__overloaded_hasUserData_ptrConstEggObject(*_args)
        elif numArgs == 1:
            return self._EggGroup__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtKE8f(upcastSelf.this)
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

    
    def setAlphaMode(self, mode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOM7kse(upcastSelf.this, mode)
        return returnValue

    
    def getAlphaMode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOM3t3A(upcastSelf.this)
        return returnValue

    
    def setDepthWriteMode(self, mode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMCEUa(upcastSelf.this, mode)
        return returnValue

    
    def getDepthWriteMode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMaHHZ(upcastSelf.this)
        return returnValue

    
    def setDepthTestMode(self, mode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMOa7S(upcastSelf.this, mode)
        return returnValue

    
    def getDepthTestMode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMkkuX(upcastSelf.this)
        return returnValue

    
    def setVisibilityMode(self, mode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMreNq(upcastSelf.this, mode)
        return returnValue

    
    def getVisibilityMode(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMta47(upcastSelf.this)
        return returnValue

    
    def setDrawOrder(self, order):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOM1SSq(upcastSelf.this, order)
        return returnValue

    
    def getDrawOrder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMY4RM(upcastSelf.this)
        return returnValue

    
    def hasDrawOrder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMV5rc(upcastSelf.this)
        return returnValue

    
    def clearDrawOrder(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMgDCN(upcastSelf.this)
        return returnValue

    
    def setBin(self, bin):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMOpBx(upcastSelf.this, bin)
        return returnValue

    
    def getBin(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMtssd(upcastSelf.this)
        return returnValue

    
    def hasBin(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOM6rGu(upcastSelf.this)
        return returnValue

    
    def clearBin(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMlrzU(upcastSelf.this)
        return returnValue

    
    def eq(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMpyzm(upcastSelf.this, other.this)
        return returnValue

    
    def ne(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMV_Rm(upcastSelf.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMT1ZU(upcastSelf.this, other.this)
        return returnValue

    
    def clearTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMAh3J(upcastSelf.this)
        return returnValue

    
    def addTranslate(self, translate):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMCLJh(upcastSelf.this, translate.this)
        return returnValue

    
    def addRotx(self, angle):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMLxrY(upcastSelf.this, angle)
        return returnValue

    
    def addRoty(self, angle):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMvzrm(upcastSelf.this, angle)
        return returnValue

    
    def addRotz(self, angle):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMD2r0(upcastSelf.this, angle)
        return returnValue

    
    def _EggGroup__overloaded_addRotate_ptrEggTransform3d_ptrConstLQuaterniond(self, quat):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMf2ja(upcastSelf.this, quat.this)
        return returnValue

    
    def _EggGroup__overloaded_addRotate_ptrEggTransform3d_double_ptrConstLVector3d(self, angle, axis):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMrh6f(upcastSelf.this, angle, axis.this)
        return returnValue

    
    def addScale(self, scale):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOM9KbB(upcastSelf.this, scale.this)
        return returnValue

    
    def addUniformScale(self, scale):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOM7BWv(upcastSelf.this, scale)
        return returnValue

    
    def addMatrix(self, mat):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMJuAF(upcastSelf.this, mat.this)
        return returnValue

    
    def hasTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMKwxE(upcastSelf.this)
        return returnValue

    
    def setTransform(self, mat):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMeSHs(upcastSelf.this, mat.this)
        return returnValue

    
    def getTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMVTx3(upcastSelf.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def transformIsIdentity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMN3eV(upcastSelf.this)
        return returnValue

    
    def getNumComponents(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMXPMG(upcastSelf.this)
        return returnValue

    
    def getComponentType(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMd1lP(upcastSelf.this, n)
        return returnValue

    
    def getComponentNumber(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMR3qK(upcastSelf.this, n)
        return returnValue

    
    def getComponentVector(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMCR2C(upcastSelf.this, n)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getComponentMatrix(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggTransform3d()
        returnValue = libpandaegg._inPkAOMTAl3(upcastSelf.this, n)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def addRotate(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggGroup__overloaded_addRotate_ptrEggTransform3d_ptrConstLQuaterniond(*_args)
        elif numArgs == 2:
            return self._EggGroup__overloaded_addRotate_ptrEggTransform3d_double_ptrConstLVector3d(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggGroup__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggGroup__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggGroup):
                return self._EggGroup__overloaded_constructor_ptrConstEggGroup(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggGroup> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def refVertex(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggGroup__overloaded_refVertex_ptrEggGroup_ptrEggVertex(*_args)
        elif numArgs == 2:
            return self._EggGroup__overloaded_refVertex_ptrEggGroup_ptrEggVertex_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


