# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount

class NurbsCurveEvaluator(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPHc9WvL16()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHc9WL_D9:
            libpanda._inPHc9WL_D9(self.this)
        

    
    def setOrder(self, order):
        returnValue = libpanda._inPHc9W69cz(self.this, order)
        return returnValue

    
    def getOrder(self):
        returnValue = libpanda._inPHc9WzKq4(self.this)
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
        returnValue = libpanda._inPHc9WQeoz(self.this, i, vertex.this)
        return returnValue

    
    def _NurbsCurveEvaluator__overloaded_setVertex_ptrNurbsCurveEvaluator_int_ptrConstLVecBase4f(self, i, vertex):
        returnValue = libpanda._inPHc9WQmY9(self.this, i, vertex.this)
        return returnValue

    
    def getVertex(self, i):
        returnValue = libpanda._inPHc9WORq2(self.this, i)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NurbsCurveEvaluator__overloaded_setVertexSpace_ptrNurbsCurveEvaluator_int_ptrConstNodePath(self, i, space):
        returnValue = libpanda._inPHc9WweNU(self.this, i, space.this)
        return returnValue

    
    def _NurbsCurveEvaluator__overloaded_setVertexSpace_ptrNurbsCurveEvaluator_int_atomicstring(self, i, space):
        returnValue = libpanda._inPHc9WyxIB(self.this, i, space)
        return returnValue

    
    def getVertexSpace(self, i, relTo):
        returnValue = libpanda._inPHc9WMK37(self.this, i, relTo.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumKnots(self):
        returnValue = libpanda._inPHc9W9dL4(self.this)
        return returnValue

    
    def setKnot(self, i, knot):
        returnValue = libpanda._inPHc9Wyjj1(self.this, i, knot)
        return returnValue

    
    def getKnot(self, i):
        returnValue = libpanda._inPHc9WuP1P(self.this, i)
        return returnValue

    
    def _NurbsCurveEvaluator__overloaded_evaluate_ptrConstNurbsCurveEvaluator_ptrConstNodePath(self, relTo):
        returnValue = libpanda._inPHc9WDpE_(self.this, relTo.this)
        import NurbsCurveResult
        returnObject = NurbsCurveResult.NurbsCurveResult(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NurbsCurveEvaluator__overloaded_evaluate_ptrConstNurbsCurveEvaluator(self):
        returnValue = libpanda._inPHc9W3r74(self.this)
        import NurbsCurveResult
        returnObject = NurbsCurveResult.NurbsCurveResult(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def evaluate(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NurbsCurveEvaluator__overloaded_evaluate_ptrConstNurbsCurveEvaluator()
        elif numArgs == 1:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                return self._NurbsCurveEvaluator__overloaded_evaluate_ptrConstNurbsCurveEvaluator_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setVertex(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase4
                import VBase3
                if isinstance(_args[1], VBase4.VBase4):
                    return self._NurbsCurveEvaluator__overloaded_setVertex_ptrNurbsCurveEvaluator_int_ptrConstLVecBase4f(_args[0], _args[1])
                elif isinstance(_args[1], VBase3.VBase3):
                    return self._NurbsCurveEvaluator__overloaded_setVertex_ptrNurbsCurveEvaluator_int_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._NurbsCurveEvaluator__overloaded_setVertex_ptrNurbsCurveEvaluator_int_ptrConstLVecBase3f_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setVertexSpace(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import NodePath
                if isinstance(_args[1], types.StringType):
                    return self._NurbsCurveEvaluator__overloaded_setVertexSpace_ptrNurbsCurveEvaluator_int_atomicstring(_args[0], _args[1])
                elif isinstance(_args[1], NodePath.NodePath):
                    return self._NurbsCurveEvaluator__overloaded_setVertexSpace_ptrNurbsCurveEvaluator_int_ptrConstNodePath(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> <NodePath.NodePath> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


