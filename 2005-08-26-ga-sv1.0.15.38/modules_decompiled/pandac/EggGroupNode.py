# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggNode

class EggGroupNode(EggNode.EggNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggGroupNode__overloaded_constructor_ptrConstEggGroupNode(self, copy):
        self.this = libpandaegg._inPkAOMyaS_(copy.this)
        self.userManagesMemory = 1

    
    def _EggGroupNode__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOM7UZA(name)
        self.userManagesMemory = 1

    
    def _EggGroupNode__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOM0aiu()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMKmaF:
            libpandaegg._inPkAOMKmaF(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMl4Aq()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMsatI(self.this, copy.this)
        returnObject = EggGroupNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def empty(self):
        returnValue = libpandaegg._inPkAOMRZjf(self.this)
        return returnValue

    
    def size(self):
        returnValue = libpandaegg._inPkAOMn_u7(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpandaegg._inPkAOMdGRB(self.this)
        return returnValue

    
    def getFirstChild(self):
        returnValue = libpandaegg._inPkAOMWCah(self.this)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNextChild(self):
        returnValue = libpandaegg._inPkAOM7zBu(self.this)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def addChild(self, node):
        returnValue = libpandaegg._inPkAOMQ_Zu(self.this, node.this)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeChild(self, node):
        returnValue = libpandaegg._inPkAOMKOID(self.this, node.this)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def stealChildren(self, other):
        returnValue = libpandaegg._inPkAOM0PPR(self.this, other.this)
        return returnValue

    
    def findChild(self, name):
        returnValue = libpandaegg._inPkAOMIxZU(self.this, name)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasAbsolutePathnames(self):
        returnValue = libpandaegg._inPkAOMWpyO(self.this)
        return returnValue

    
    def resolveFilenames(self, searchpath):
        returnValue = libpandaegg._inPkAOMQMtA(self.this, searchpath.this)
        return returnValue

    
    def forceFilenames(self, directory):
        returnValue = libpandaegg._inPkAOMGIQc(self.this, directory.this)
        return returnValue

    
    def reverseVertexOrdering(self):
        returnValue = libpandaegg._inPkAOM1ZhK(self.this)
        return returnValue

    
    def _EggGroupNode__overloaded_recomputeVertexNormals_ptrEggGroupNode_double___enum__CoordinateSystem(self, threshold, cs):
        returnValue = libpandaegg._inPkAOM_XGy(self.this, threshold, cs)
        return returnValue

    
    def _EggGroupNode__overloaded_recomputeVertexNormals_ptrEggGroupNode_double(self, threshold):
        returnValue = libpandaegg._inPkAOMC1bM(self.this, threshold)
        return returnValue

    
    def _EggGroupNode__overloaded_recomputePolygonNormals_ptrEggGroupNode___enum__CoordinateSystem(self, cs):
        returnValue = libpandaegg._inPkAOMxT4d(self.this, cs)
        return returnValue

    
    def _EggGroupNode__overloaded_recomputePolygonNormals_ptrEggGroupNode(self):
        returnValue = libpandaegg._inPkAOMb2rf(self.this)
        return returnValue

    
    def stripNormals(self):
        returnValue = libpandaegg._inPkAOMtsfH(self.this)
        return returnValue

    
    def triangulatePolygons(self, convexAlso):
        returnValue = libpandaegg._inPkAOM0jm4(self.this, convexAlso)
        return returnValue

    
    def removeUnusedVertices(self):
        returnValue = libpandaegg._inPkAOMZcZ9(self.this)
        return returnValue

    
    def removeInvalidPrimitives(self):
        returnValue = libpandaegg._inPkAOMQsA8(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggGroupNode__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggGroupNode__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggGroupNode):
                return self._EggGroupNode__overloaded_constructor_ptrConstEggGroupNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggGroupNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def recomputeVertexNormals(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggGroupNode__overloaded_recomputeVertexNormals_ptrEggGroupNode_double(*_args)
        elif numArgs == 2:
            return self._EggGroupNode__overloaded_recomputeVertexNormals_ptrEggGroupNode_double___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def recomputePolygonNormals(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggGroupNode__overloaded_recomputePolygonNormals_ptrEggGroupNode(*_args)
        elif numArgs == 1:
            return self._EggGroupNode__overloaded_recomputePolygonNormals_ptrEggGroupNode___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getChildren(self):
        result = []
        child = self.getFirstChild()
        while child != None:
            result.append(child)
            child = self.getNextChild()
        return result


