# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount

class CollisionEntry(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
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
        if libpanda and libpanda._inPHwcatQwG:
            libpanda._inPHwcatQwG(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaSIuZ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getFrom(self):
        returnValue = libpanda._inPHwcaGwYK(self.this)
        import CollisionSolid
        returnObject = CollisionSolid.CollisionSolid(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasInto(self):
        returnValue = libpanda._inPHwcauTcn(self.this)
        return returnValue

    
    def getInto(self):
        returnValue = libpanda._inPHwcaGQba(self.this)
        import CollisionSolid
        returnObject = CollisionSolid.CollisionSolid(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getFromNode(self):
        returnValue = libpanda._inPHwcae4xC(self.this)
        import CollisionNode
        returnObject = CollisionNode.CollisionNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getIntoNode(self):
        returnValue = libpanda._inPHwca_40S(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getFromNodePath(self):
        returnValue = libpanda._inPHwcacMQX(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getIntoNodePath(self):
        returnValue = libpanda._inPHwca83Sn(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRespectPrevTransform(self):
        returnValue = libpanda._inPHwcaRUDs(self.this)
        return returnValue

    
    def setSurfacePoint(self, point):
        returnValue = libpanda._inPHwcahJuh(self.this, point.this)
        return returnValue

    
    def setSurfaceNormal(self, normal):
        returnValue = libpanda._inPHwcaSvQs(self.this, normal.this)
        return returnValue

    
    def setInteriorPoint(self, point):
        returnValue = libpanda._inPHwcaIgiu(self.this, point.this)
        return returnValue

    
    def hasSurfacePoint(self):
        returnValue = libpanda._inPHwcaIa3H(self.this)
        return returnValue

    
    def hasSurfaceNormal(self):
        returnValue = libpanda._inPHwcaX6_A(self.this)
        return returnValue

    
    def hasInteriorPoint(self):
        returnValue = libpanda._inPHwcaoXP3(self.this)
        return returnValue

    
    def getSurfacePoint(self, space):
        returnValue = libpanda._inPHwcahuLD(self.this, space.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getSurfaceNormal(self, space):
        returnValue = libpanda._inPHwcab0T_(self.this, space.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getInteriorPoint(self, space):
        returnValue = libpanda._inPHwcaBjl0(self.this, space.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getAll(self, space, surfacePoint, surfaceNormal, interiorPoint):
        returnValue = libpanda._inPHwca_a_e(self.this, space.this, surfacePoint.this, surfaceNormal.this, interiorPoint.this)
        return returnValue

    
    def hasIntoIntersectionPoint(self):
        returnValue = libpanda._inPHwcaY_Lr(self.this)
        return returnValue

    
    def getIntoIntersectionPoint(self):
        returnValue = libpanda._inPHwcawULe(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasFromIntersectionPoint(self):
        returnValue = libpanda._inPHwca4yGb(self.this)
        return returnValue

    
    def getFromIntersectionPoint(self):
        returnValue = libpanda._inPHwcaQUGO(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasIntoSurfaceNormal(self):
        returnValue = libpanda._inPHwcaSFZi(self.this)
        return returnValue

    
    def getIntoSurfaceNormal(self):
        returnValue = libpanda._inPHwcaq_WV(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasFromSurfaceNormal(self):
        returnValue = libpanda._inPHwcayPUS(self.this)
        return returnValue

    
    def getFromSurfaceNormal(self):
        returnValue = libpanda._inPHwcaqoVF(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasIntoDepth(self):
        returnValue = libpanda._inPHwcaS8Ls(self.this)
        return returnValue

    
    def getIntoDepth(self):
        returnValue = libpanda._inPHwcaqbLf(self.this)
        return returnValue

    
    def hasFromDepth(self):
        returnValue = libpanda._inPHwcayjIc(self.this)
        return returnValue

    
    def getFromDepth(self):
        returnValue = libpanda._inPHwcaqGIP(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPHwcawXJC(self.this, out.this)
        return returnValue

    
    def _CollisionEntry__overloaded_write_ptrConstCollisionEntry_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPHwca2JVw(self.this, out.this, indentLevel)
        return returnValue

    
    def _CollisionEntry__overloaded_write_ptrConstCollisionEntry_ptrOstream(self, out):
        returnValue = libpanda._inPHwcaJrFD(self.this, out.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CollisionEntry__overloaded_write_ptrConstCollisionEntry_ptrOstream(*_args)
        elif numArgs == 2:
            return self._CollisionEntry__overloaded_write_ptrConstCollisionEntry_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


