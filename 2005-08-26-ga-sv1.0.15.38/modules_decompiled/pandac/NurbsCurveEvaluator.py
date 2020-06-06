# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ReferenceCount

class NurbsCurveEvaluator(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPHc9WoL16()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHc9WE_D9:
            libpanda._inPHc9WE_D9(self.this)
        

    
    def setOrder(self, order):
        returnValue = libpanda._inPHc9W59cz(self.this, order)
        return returnValue

    
    def getOrder(self):
        returnValue = libpanda._inPHc9WyKq4(self.this)
        return returnValue

    
    def reset(self, numVertices):
        returnValue = libpanda._inPHc9Wc62C(self.this, numVertices)
        return returnValue

    
    def getNumVertices(self):
        returnValue = libpanda._inPHc9WWeXN(self.this)
        return returnValue

    
    def _NurbsCurveEvaluator__overloaded_setVertex_ptrNurbsCurveEvaluator_int_ptrConstLVecBase3f_float(self, i, vertex, weight):
        returnValue = libpanda._inPHc9WJSId(self.this, i, vertex.this, weight)
        return returnValue

    
    def _NurbsCurveEvaluator__overloaded_setVertex_ptrNurbsCurveEvaluator_int_ptrConstLVecBase3f(self, i, vertex):
        returnValue = libpanda._inPHc9WTeoz(self.this, i, vertex.this)
        return returnValue

    
    def _NurbsCurveEvaluator__overloaded_setVertex_ptrNurbsCurveEvaluator_int_ptrConstLVecBase4f(self, i, vertex):
        returnValue = libpanda._inPHc9WTmY9(self.this, i, vertex.this)
        return returnValue

    
    def _NurbsCurveEvaluator__overloaded_getVertex_ptrConstNurbsCurveEvaluator_int(self, i):
        returnValue = libpanda._inPHc9WPRq2(self.this, i)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NurbsCurveEvaluator__overloaded_getVertex_ptrConstNurbsCurveEvaluator_int_ptrConstNodePath(self, i, relTo):
        returnValue = libpanda._inPHc9WcIW3(self.this, i, relTo.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NurbsCurveEvaluator__overloaded_setVertexSpace_ptrNurbsCurveEvaluator_int_ptrConstNodePath(self, i, space):
        returnValue = libpanda._inPHc9WweNU(self.this, i, space.this)
        return returnValue

    
    def _NurbsCurveEvaluator__overloaded_setVertexSpace_ptrNurbsCurveEvaluator_int_atomicstring(self, i, space):
        returnValue = libpanda._inPHc9WyxIB(self.this, i, space)
        return returnValue

    
    def getVertexSpace(self, i, relTo):
        returnValue = libpanda._inPHc9WNK37(self.this, i, relTo.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setExtendedVertex(self, i, d, value):
        returnValue = libpanda._inPHc9WnasG(self.this, i, d, value)
        return returnValue

    
    def getExtendedVertex(self, i, d):
        returnValue = libpanda._inPHc9WKQQ_(self.this, i, d)
        return returnValue

    
    def getNumKnots(self):
        returnValue = libpanda._inPHc9W8dL4(self.this)
        return returnValue

    
    def setKnot(self, i, knot):
        returnValue = libpanda._inPHc9Wxjj1(self.this, i, knot)
        return returnValue

    
    def getKnot(self, i):
        returnValue = libpanda._inPHc9WuP1P(self.this, i)
        return returnValue

    
    def normalizeKnots(self):
        returnValue = libpanda._inPHc9Wmh_4(self.this)
        return returnValue

    
    def getNumSegments(self):
        returnValue = libpanda._inPHc9WEL14(self.this)
        return returnValue

    
    def _NurbsCurveEvaluator__overloaded_evaluate_ptrConstNurbsCurveEvaluator_ptrConstNodePath(self, relTo):
        returnValue = libpanda._inPHc9WApE_(self.this, relTo.this)
        import NurbsCurveResult
        returnObject = NurbsCurveResult.NurbsCurveResult(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NurbsCurveEvaluator__overloaded_evaluate_ptrConstNurbsCurveEvaluator(self):
        returnValue = libpanda._inPHc9W2r74(self.this)
        import NurbsCurveResult
        returnObject = NurbsCurveResult.NurbsCurveResult(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NurbsCurveEvaluator__overloaded_evaluate_ptrConstNurbsCurveEvaluator_ptrConstNodePath_ptrConstLMatrix4f(self, relTo, mat):
        returnValue = libpanda._inPHc9WWA8J(self.this, relTo.this, mat.this)
        import NurbsCurveResult
        returnObject = NurbsCurveResult.NurbsCurveResult(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libpanda._inPHc9Wh3t0(self.this, out.this)
        return returnValue

    
    def evaluate(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NurbsCurveEvaluator__overloaded_evaluate_ptrConstNurbsCurveEvaluator(*_args)
        elif numArgs == 1:
            return self._NurbsCurveEvaluator__overloaded_evaluate_ptrConstNurbsCurveEvaluator_ptrConstNodePath(*_args)
        elif numArgs == 2:
            return self._NurbsCurveEvaluator__overloaded_evaluate_ptrConstNurbsCurveEvaluator_ptrConstNodePath_ptrConstLMatrix4f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def setVertex(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase4
                if isinstance(_args[1], VBase4.VBase4):
                    return self._NurbsCurveEvaluator__overloaded_setVertex_ptrNurbsCurveEvaluator_int_ptrConstLVecBase4f(*_args)
                
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._NurbsCurveEvaluator__overloaded_setVertex_ptrNurbsCurveEvaluator_int_ptrConstLVecBase3f(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 3:
            return self._NurbsCurveEvaluator__overloaded_setVertex_ptrNurbsCurveEvaluator_int_ptrConstLVecBase3f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setVertexSpace(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                if isinstance(_args[1], types.StringType):
                    return self._NurbsCurveEvaluator__overloaded_setVertexSpace_ptrNurbsCurveEvaluator_int_atomicstring(*_args)
                
                import NodePath
                if isinstance(_args[1], NodePath.NodePath):
                    return self._NurbsCurveEvaluator__overloaded_setVertexSpace_ptrNurbsCurveEvaluator_int_ptrConstNodePath(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> <NodePath.NodePath> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def getVertex(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NurbsCurveEvaluator__overloaded_getVertex_ptrConstNurbsCurveEvaluator_int(*_args)
        elif numArgs == 2:
            return self._NurbsCurveEvaluator__overloaded_getVertex_ptrConstNurbsCurveEvaluator_int_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getKnots(self):
        knots = []
        for i in range(self.getNumKnots()):
            knots.append(self.getKnot(i))
        
        return knots

    
    def getVertices(self, relTo = None):
        verts = []
        if relTo:
            for i in range(self.getNumVertices()):
                verts.append(self.getVertex(i, relTo))
            
        else:
            for i in range(self.getNumVertices()):
                verts.append(self.getVertex(i))
            
        return verts


