# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggObject
import EggAttributes

class EggVertex(EggObject.EggObject, EggAttributes.EggAttributes, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggVertex__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMtjbY()
        self.userManagesMemory = 1

    
    def _EggVertex__overloaded_constructor_ptrConstEggVertex(self, copy):
        self.this = libpandaegg._inPkAOMbgja(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMkOIb:
            libpandaegg._inPkAOMkOIb(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMGT9t()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMmaUY(self.this, copy.this)
        returnObject = EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getPool(self):
        returnValue = libpandaegg._inPkAOMz9Ky(self.this)
        import EggVertexPool
        returnObject = EggVertexPool.EggVertexPool(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def isForwardReference(self):
        returnValue = libpandaegg._inPkAOMp_H_(self.this)
        return returnValue

    
    def _EggVertex__overloaded_setPos_ptrEggVertex_ptrConstLPoint2d(self, pos):
        returnValue = libpandaegg._inPkAOM2yZs(self.this, pos.this)
        return returnValue

    
    def _EggVertex__overloaded_setPos_ptrEggVertex_ptrConstLPoint3d(self, pos):
        returnValue = libpandaegg._inPkAOMW1At(self.this, pos.this)
        return returnValue

    
    def _EggVertex__overloaded_setPos_ptrEggVertex_ptrConstLPoint4d(self, pos):
        returnValue = libpandaegg._inPkAOM25nt(self.this, pos.this)
        return returnValue

    
    def _EggVertex__overloaded_setPos_ptrEggVertex_double(self, pos):
        returnValue = libpandaegg._inPkAOMZ6NP(self.this, pos)
        return returnValue

    
    def setPos4(self, pos):
        returnValue = libpandaegg._inPkAOMPMSb(self.this, pos.this)
        return returnValue

    
    def getNumDimensions(self):
        returnValue = libpandaegg._inPkAOMO31_(self.this)
        return returnValue

    
    def getPos1(self):
        returnValue = libpandaegg._inPkAOMJIBG(self.this)
        return returnValue

    
    def getPos2(self):
        returnValue = libpandaegg._inPkAOMbHBN(self.this)
        import Point2D
        returnObject = Point2D.Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getPos3(self):
        returnValue = libpandaegg._inPkAOMtGBU(self.this)
        import Point3D
        returnObject = Point3D.Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getPos4(self):
        returnValue = libpandaegg._inPkAOM_FBb(self.this)
        import Point4D
        returnObject = Point4D.Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _EggVertex__overloaded_hasUv_ptrConstEggVertex(self):
        returnValue = libpandaegg._inPkAOMmIlN(self.this)
        return returnValue

    
    def _EggVertex__overloaded_hasUv_ptrConstEggVertex_atomicstring(self, name):
        returnValue = libpandaegg._inPkAOMKQRh(self.this, name)
        return returnValue

    
    def _EggVertex__overloaded_getUv_ptrConstEggVertex(self):
        returnValue = libpandaegg._inPkAOMaaFH(self.this)
        import Point2D
        returnObject = Point2D.Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _EggVertex__overloaded_getUv_ptrConstEggVertex_atomicstring(self, name):
        returnValue = libpandaegg._inPkAOM_Bxa(self.this, name)
        import Point2D
        returnObject = Point2D.Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _EggVertex__overloaded_setUv_ptrEggVertex_ptrConstLPoint2d(self, texCoord):
        returnValue = libpandaegg._inPkAOMAFVN(self.this, texCoord.this)
        return returnValue

    
    def _EggVertex__overloaded_setUv_ptrEggVertex_atomicstring_ptrConstLPoint2d(self, name, texCoord):
        returnValue = libpandaegg._inPkAOMs1Zd(self.this, name, texCoord.this)
        return returnValue

    
    def _EggVertex__overloaded_clearUv_ptrEggVertex(self):
        returnValue = libpandaegg._inPkAOMqW8Y(self.this)
        return returnValue

    
    def _EggVertex__overloaded_clearUv_ptrEggVertex_atomicstring(self, name):
        returnValue = libpandaegg._inPkAOMBuq9(self.this, name)
        return returnValue

    
    def getUvObj(self, name):
        returnValue = libpandaegg._inPkAOM_lz7(self.this, name)
        import EggVertexUV
        returnObject = EggVertexUV.EggVertexUV(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setUvObj(self, vertexUv):
        returnValue = libpandaegg._inPkAOM37Oi(self.this, vertexUv.this)
        return returnValue

    
    def getIndex(self):
        returnValue = libpandaegg._inPkAOMPXw_(self.this)
        return returnValue

    
    def setExternalIndex(self, externalIndex):
        returnValue = libpandaegg._inPkAOMRa07(self.this, externalIndex)
        return returnValue

    
    def getExternalIndex(self):
        returnValue = libpandaegg._inPkAOMlfWC(self.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOM3GP5(self.this, out.this, indentLevel)
        return returnValue

    
    def sortsLessThan(self, other):
        returnValue = libpandaegg._inPkAOMBgJ_(self.this, other.this)
        return returnValue

    
    def getNumLocalCoord(self):
        returnValue = libpandaegg._inPkAOMQ2Pa(self.this)
        return returnValue

    
    def getNumGlobalCoord(self):
        returnValue = libpandaegg._inPkAOMTVqu(self.this)
        return returnValue

    
    def transform(self, mat):
        returnValue = libpandaegg._inPkAOMHCW9(self.this, mat.this)
        return returnValue

    
    def hasGref(self, group):
        returnValue = libpandaegg._inPkAOMZsOw(self.this, group.this)
        return returnValue

    
    def copyGrefsFrom(self, other):
        returnValue = libpandaegg._inPkAOM2kRg(self.this, other.this)
        return returnValue

    
    def clearGrefs(self):
        returnValue = libpandaegg._inPkAOM1JbX(self.this)
        return returnValue

    
    def hasPref(self, prim):
        returnValue = libpandaegg._inPkAOMk0J_(self.this, prim.this)
        return returnValue

    
    def testGrefIntegrity(self):
        returnValue = libpandaegg._inPkAOMgTDr(self.this)
        return returnValue

    
    def testPrefIntegrity(self):
        returnValue = libpandaegg._inPkAOMhP_W(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaegg._inPkAOMOrKC(self.this, out.this)
        return returnValue

    
    def upcastToEggAttributes(self):
        returnValue = libpandaegg._inPkAOModNS(self.this)
        import EggAttributes
        returnObject = EggAttributes.EggAttributes(None)
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

    
    def _EggVertex__overloaded_hasUserData_ptrConstEggObject(self):
        upcastSelf = self
        returnValue = libpandaegg._inPkAOMibXq(upcastSelf.this)
        return returnValue

    
    def _EggVertex__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(self, type):
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
            return self._EggVertex__overloaded_hasUserData_ptrConstEggObject(*_args)
        elif numArgs == 1:
            return self._EggVertex__overloaded_hasUserData_ptrConstEggObject_ptrTypeHandle(*_args)
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

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggVertex__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._EggVertex__overloaded_constructor_ptrConstEggVertex(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getUv(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggVertex__overloaded_getUv_ptrConstEggVertex(*_args)
        elif numArgs == 1:
            return self._EggVertex__overloaded_getUv_ptrConstEggVertex_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setUv(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggVertex__overloaded_setUv_ptrEggVertex_ptrConstLPoint2d(*_args)
        elif numArgs == 2:
            return self._EggVertex__overloaded_setUv_ptrEggVertex_atomicstring_ptrConstLPoint2d(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._EggVertex__overloaded_setPos_ptrEggVertex_double(*_args)
            
            import Point4D
            if isinstance(_args[0], Point4D.Point4D):
                return self._EggVertex__overloaded_setPos_ptrEggVertex_ptrConstLPoint4d(*_args)
            
            import Point3D
            if isinstance(_args[0], Point3D.Point3D):
                return self._EggVertex__overloaded_setPos_ptrEggVertex_ptrConstLPoint3d(*_args)
            
            import Point2D
            if isinstance(_args[0], Point2D.Point2D):
                return self._EggVertex__overloaded_setPos_ptrEggVertex_ptrConstLPoint2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Point4D.Point4D> <Point3D.Point3D> <Point2D.Point2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def hasUv(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggVertex__overloaded_hasUv_ptrConstEggVertex(*_args)
        elif numArgs == 1:
            return self._EggVertex__overloaded_hasUv_ptrConstEggVertex_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def clearUv(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggVertex__overloaded_clearUv_ptrEggVertex(*_args)
        elif numArgs == 1:
            return self._EggVertex__overloaded_clearUv_ptrEggVertex_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


