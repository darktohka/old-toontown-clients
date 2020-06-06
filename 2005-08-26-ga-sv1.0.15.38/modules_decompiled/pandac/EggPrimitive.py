# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggNode
import EggAttributes
import EggRenderMode

class EggPrimitive(EggNode.EggNode, EggAttributes.EggAttributes, EggRenderMode.EggRenderMode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
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
        if libpandaegg and libpandaegg._inPkAOMkVr4:
            libpandaegg._inPkAOMkVr4(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOM2RY6()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMhJqk(self.this, copy.this)
        returnObject = EggPrimitive(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def determineAlphaMode(self):
        returnValue = libpandaegg._inPkAOM70HD(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDepthWriteMode(self):
        returnValue = libpandaegg._inPkAOM6tkm(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDepthTestMode(self):
        returnValue = libpandaegg._inPkAOMIAv2(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineVisibilityMode(self):
        returnValue = libpandaegg._inPkAOMUKF_(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineDrawOrder(self):
        returnValue = libpandaegg._inPkAOMJZ7Z(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def determineBin(self):
        returnValue = libpandaegg._inPkAOMSQGc(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setTexture(self, texture):
        returnValue = libpandaegg._inPkAOMxMIe(self.this, texture.this)
        return returnValue

    
    def _EggPrimitive__overloaded_hasTexture_ptrConstEggPrimitive(self):
        returnValue = libpandaegg._inPkAOMCDRS(self.this)
        return returnValue

    
    def _EggPrimitive__overloaded_hasTexture_ptrConstEggPrimitive_ptrEggTexture(self, texture):
        returnValue = libpandaegg._inPkAOMnWlz(self.this, texture.this)
        return returnValue

    
    def _EggPrimitive__overloaded_getTexture_ptrConstEggPrimitive(self):
        returnValue = libpandaegg._inPkAOM2fun(self.this)
        import EggTexture
        returnObject = EggTexture.EggTexture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggPrimitive__overloaded_getTexture_ptrConstEggPrimitive_int(self, n):
        returnValue = libpandaegg._inPkAOMoFbC(self.this, n)
        import EggTexture
        returnObject = EggTexture.EggTexture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def addTexture(self, texture):
        returnValue = libpandaegg._inPkAOMf0zv(self.this, texture.this)
        return returnValue

    
    def clearTexture(self):
        returnValue = libpandaegg._inPkAOMhV0K(self.this)
        return returnValue

    
    def getNumTextures(self):
        returnValue = libpandaegg._inPkAOML1FR(self.this)
        return returnValue

    
    def setMaterial(self, material):
        returnValue = libpandaegg._inPkAOMLGBt(self.this, material.this)
        return returnValue

    
    def clearMaterial(self):
        returnValue = libpandaegg._inPkAOM4kT7(self.this)
        return returnValue

    
    def getMaterial(self):
        returnValue = libpandaegg._inPkAOMElax(self.this)
        import EggMaterial
        returnObject = EggMaterial.EggMaterial(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasMaterial(self):
        returnValue = libpandaegg._inPkAOMYE8b(self.this)
        return returnValue

    
    def setBfaceFlag(self, flag):
        returnValue = libpandaegg._inPkAOMeofj(self.this, flag)
        return returnValue

    
    def getBfaceFlag(self):
        returnValue = libpandaegg._inPkAOMcCgN(self.this)
        return returnValue

    
    def copyAttributes(self, other):
        returnValue = libpandaegg._inPkAOMLo5X(self.this, other.this)
        return returnValue

    
    def hasVertexNormal(self):
        returnValue = libpandaegg._inPkAOMgHBP(self.this)
        return returnValue

    
    def hasVertexColor(self):
        returnValue = libpandaegg._inPkAOMzlJw(self.this)
        return returnValue

    
    def reverseVertexOrdering(self):
        returnValue = libpandaegg._inPkAOMGw4a(self.this)
        return returnValue

    
    def cleanup(self):
        returnValue = libpandaegg._inPkAOM0Gh8(self.this)
        return returnValue

    
    def removeDoubledVerts(self, closed):
        returnValue = libpandaegg._inPkAOMwSZ1(self.this, closed)
        return returnValue

    
    def removeNonuniqueVerts(self):
        returnValue = libpandaegg._inPkAOMIS4T(self.this)
        return returnValue

    
    def hasPrimitives(self):
        returnValue = libpandaegg._inPkAOMrzxk(self.this)
        return returnValue

    
    def jointHasPrimitives(self):
        returnValue = libpandaegg._inPkAOMXSfa(self.this)
        return returnValue

    
    def hasNormals(self):
        returnValue = libpandaegg._inPkAOMF6tl(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpandaegg._inPkAOMctoR(self.this)
        return returnValue

    
    def addVertex(self, vertex):
        returnValue = libpandaegg._inPkAOMW8_c(self.this, vertex.this)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeVertex(self, vertex):
        returnValue = libpandaegg._inPkAOM7qsK(self.this, vertex.this)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def copyVertices(self, other):
        returnValue = libpandaegg._inPkAOM_m4j(self.this, other.this)
        return returnValue

    
    def getNumVertices(self):
        returnValue = libpandaegg._inPkAOMkeY6(self.this)
        return returnValue

    
    def setVertex(self, index, vertex):
        returnValue = libpandaegg._inPkAOM5Wo7(self.this, index, vertex.this)
        return returnValue

    
    def getVertex(self, index):
        returnValue = libpandaegg._inPkAOMFsKW(self.this, index)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getPool(self):
        returnValue = libpandaegg._inPkAOMm7xE(self.this)
        import EggVertexPool
        returnObject = EggVertexPool.EggVertexPool(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def testVrefIntegrity(self):
        returnValue = libpandaegg._inPkAOMG9YA(self.this)
        return returnValue

    
    def upcastToEggAttributes(self):
        returnValue = libpandaegg._inPkAOM6ts2(self.this)
        import EggAttributes
        returnObject = EggAttributes.EggAttributes(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToEggRenderMode(self):
        returnValue = libpandaegg._inPkAOM9Jj3(self.this)
        import EggRenderMode
        returnObject = EggRenderMode.EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
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

    
    def isJoint(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMHHnM(upcastSelf.this)
        return returnValue

    
    def isAnimMatrix(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM82MW(upcastSelf.this)
        return returnValue

    
    def determineIndexed(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOM6Ucg(upcastSelf.this)
        return returnValue

    
    def write(self, out, indentLevel):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMIrWM(upcastSelf.this, out.this, indentLevel)
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

    
    def _EggPrimitive__overloaded_hasUserData_ptrConstEggObject(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMibXq(upcastSelf.this)
        return returnValue

    
    def _EggPrimitive__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(self, type):
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
            return self._EggPrimitive__overloaded_hasUserData_ptrConstEggObject(*_args)
        elif numArgs == 1:
            return self._EggPrimitive__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(*_args)
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

    
    def hasNormal(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMw9Eb(upcastSelf.this)
        return returnValue

    
    def getNormal(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMVCpK(upcastSelf.this)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setNormal(self, normal):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMpRK6(upcastSelf.this, normal.this)
        return returnValue

    
    def clearNormal(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMS6MT(upcastSelf.this)
        return returnValue

    
    def hasColor(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMKFjr(upcastSelf.this)
        return returnValue

    
    def getColor(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMXGJb(upcastSelf.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setColor(self, color):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMFNlA(upcastSelf.this, color.this)
        return returnValue

    
    def clearColor(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMfqMj(upcastSelf.this)
        return returnValue

    
    def write(self, out, indentLevel):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMgbBE(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def sortsLessThan(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMOpUR(upcastSelf.this, other.this)
        return returnValue

    
    def transform(self, mat):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggAttributes()
        returnValue = libpandaegg._inPkAOMZnUo(upcastSelf.this, mat.this)
        return returnValue

    
    def write(self, out, indentLevel):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToEggRenderMode()
        returnValue = libpandaegg._inPkAOMtH5E(upcastSelf.this, out.this, indentLevel)
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

    
    def hasTexture(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggPrimitive__overloaded_hasTexture_ptrConstEggPrimitive(*_args)
        elif numArgs == 1:
            return self._EggPrimitive__overloaded_hasTexture_ptrConstEggPrimitive_ptrEggTexture(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getTexture(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggPrimitive__overloaded_getTexture_ptrConstEggPrimitive(*_args)
        elif numArgs == 1:
            return self._EggPrimitive__overloaded_getTexture_ptrConstEggPrimitive_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getVertices(self):
        result = []
        for i in range(self.getNumVertices()):
            result.append(self.getVertex(i))
        
        return result


