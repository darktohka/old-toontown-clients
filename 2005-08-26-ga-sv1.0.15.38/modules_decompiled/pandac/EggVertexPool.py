# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggNode

class EggVertexPool(EggNode.EggNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggVertexPool__overloaded_constructor_ptrConstEggVertexPool(self, copy):
        self.this = libpandaegg._inPkAOMBdMA(copy.this)
        self.userManagesMemory = 1

    
    def _EggVertexPool__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOMY_4J(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMKmaF:
            libpandaegg._inPkAOMKmaF(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMOYkz()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def hasVertex(self, index):
        returnValue = libpandaegg._inPkAOMrRQ_(self.this, index)
        return returnValue

    
    def hasForwardVertices(self):
        returnValue = libpandaegg._inPkAOMKc1J(self.this)
        return returnValue

    
    def hasDefinedVertices(self):
        returnValue = libpandaegg._inPkAOMsCOx(self.this)
        return returnValue

    
    def getVertex(self, index):
        returnValue = libpandaegg._inPkAOM_O2t(self.this, index)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def __getitem__(self, index):
        returnValue = libpandaegg._inPkAOMGe06(self.this, index)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getForwardVertex(self, index):
        returnValue = libpandaegg._inPkAOMB8Di(self.this, index)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getHighestIndex(self):
        returnValue = libpandaegg._inPkAOMX2qU(self.this)
        return returnValue

    
    def _EggVertexPool__overloaded_addVertex_ptrEggVertexPool_ptrEggVertex_int(self, vertex, index):
        returnValue = libpandaegg._inPkAOMG7Zj(self.this, vertex.this, index)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggVertexPool__overloaded_addVertex_ptrEggVertexPool_ptrEggVertex(self, vertex):
        returnValue = libpandaegg._inPkAOMiMXH(self.this, vertex.this)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggVertexPool__overloaded_makeNewVertex_ptrEggVertexPool(self):
        returnValue = libpandaegg._inPkAOMPbgz(self.this)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggVertexPool__overloaded_makeNewVertex_ptrEggVertexPool_ptrConstLPoint2d(self, pos):
        returnValue = libpandaegg._inPkAOMmAmN(self.this, pos.this)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggVertexPool__overloaded_makeNewVertex_ptrEggVertexPool_ptrConstLPoint3d(self, pos):
        returnValue = libpandaegg._inPkAOM_DGR(self.this, pos.this)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggVertexPool__overloaded_makeNewVertex_ptrEggVertexPool_ptrConstLPoint4d(self, pos):
        returnValue = libpandaegg._inPkAOMUCmU(self.this, pos.this)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggVertexPool__overloaded_makeNewVertex_ptrEggVertexPool_double(self, pos):
        returnValue = libpandaegg._inPkAOMqB5d(self.this, pos)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def createUniqueVertex(self, copy):
        returnValue = libpandaegg._inPkAOM6VIP(self.this, copy.this)
        import EggVertex
        returnObject = EggVertex.EggVertex(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeVertex(self, vertex):
        returnValue = libpandaegg._inPkAOMJ0C_(self.this, vertex.this)
        return returnValue

    
    def removeUnusedVertices(self):
        returnValue = libpandaegg._inPkAOMrkZg(self.this)
        return returnValue

    
    def transform(self, mat):
        returnValue = libpandaegg._inPkAOMh7hw(self.this, mat.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggVertexPool__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggVertexPool):
                return self._EggVertexPool__overloaded_constructor_ptrConstEggVertexPool(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggVertexPool> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def makeNewVertex(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggVertexPool__overloaded_makeNewVertex_ptrEggVertexPool(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._EggVertexPool__overloaded_makeNewVertex_ptrEggVertexPool_double(*_args)
            
            import Point4D
            if isinstance(_args[0], Point4D.Point4D):
                return self._EggVertexPool__overloaded_makeNewVertex_ptrEggVertexPool_ptrConstLPoint4d(*_args)
            
            import Point3D
            if isinstance(_args[0], Point3D.Point3D):
                return self._EggVertexPool__overloaded_makeNewVertex_ptrEggVertexPool_ptrConstLPoint3d(*_args)
            
            import Point2D
            if isinstance(_args[0], Point2D.Point2D):
                return self._EggVertexPool__overloaded_makeNewVertex_ptrEggVertexPool_ptrConstLPoint2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Point4D.Point4D> <Point3D.Point3D> <Point2D.Point2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def addVertex(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggVertexPool__overloaded_addVertex_ptrEggVertexPool_ptrEggVertex(*_args)
        elif numArgs == 2:
            return self._EggVertexPool__overloaded_addVertex_ptrEggVertexPool_ptrEggVertex_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


