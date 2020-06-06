# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ReferenceCount

class NurbsSurfaceEvaluator(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPHc9WPTGr()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHc9W2VdL:
            libpanda._inPHc9W2VdL(self.this)
        

    
    def setUOrder(self, uOrder):
        returnValue = libpanda._inPHc9WU5Cj(self.this, uOrder)
        return returnValue

    
    def getUOrder(self):
        returnValue = libpanda._inPHc9Wr6rC(self.this)
        return returnValue

    
    def setVOrder(self, vOrder):
        returnValue = libpanda._inPHc9Wi46T(self.this, vOrder)
        return returnValue

    
    def getVOrder(self):
        returnValue = libpanda._inPHc9WS6jz(self.this)
        return returnValue

    
    def reset(self, numUVertices, numVVertices):
        returnValue = libpanda._inPHc9WR8n7(self.this, numUVertices, numVVertices)
        return returnValue

    
    def getNumUVertices(self):
        returnValue = libpanda._inPHc9WSVa7(self.this)
        return returnValue

    
    def getNumVVertices(self):
        returnValue = libpanda._inPHc9WR1di(self.this)
        return returnValue

    
    def _NurbsSurfaceEvaluator__overloaded_setVertex_ptrNurbsSurfaceEvaluator_int_int_ptrConstLVecBase3f_float(self, ui, vi, vertex, weight):
        returnValue = libpanda._inPHc9W_QQa(self.this, ui, vi, vertex.this, weight)
        return returnValue

    
    def _NurbsSurfaceEvaluator__overloaded_setVertex_ptrNurbsSurfaceEvaluator_int_int_ptrConstLVecBase3f(self, ui, vi, vertex):
        returnValue = libpanda._inPHc9WgFq4(self.this, ui, vi, vertex.this)
        return returnValue

    
    def _NurbsSurfaceEvaluator__overloaded_setVertex_ptrNurbsSurfaceEvaluator_int_int_ptrConstLVecBase4f(self, ui, vi, vertex):
        returnValue = libpanda._inPHc9WpOqU(self.this, ui, vi, vertex.this)
        return returnValue

    
    def _NurbsSurfaceEvaluator__overloaded_getVertex_ptrConstNurbsSurfaceEvaluator_int_int(self, ui, vi):
        returnValue = libpanda._inPHc9WO2eA(self.this, ui, vi)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NurbsSurfaceEvaluator__overloaded_getVertex_ptrConstNurbsSurfaceEvaluator_int_int_ptrConstNodePath(self, ui, vi, relTo):
        returnValue = libpanda._inPHc9Wf6Jc(self.this, ui, vi, relTo.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NurbsSurfaceEvaluator__overloaded_setVertexSpace_ptrNurbsSurfaceEvaluator_int_int_ptrConstNodePath(self, ui, vi, space):
        returnValue = libpanda._inPHc9W2rJC(self.this, ui, vi, space.this)
        return returnValue

    
    def _NurbsSurfaceEvaluator__overloaded_setVertexSpace_ptrNurbsSurfaceEvaluator_int_int_atomicstring(self, ui, vi, space):
        returnValue = libpanda._inPHc9Wklv_(self.this, ui, vi, space)
        return returnValue

    
    def getVertexSpace(self, ui, vi, relTo):
        returnValue = libpanda._inPHc9WHN7J(self.this, ui, vi, relTo.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setExtendedVertex(self, ui, vi, d, value):
        returnValue = libpanda._inPHc9Wow1w(self.this, ui, vi, d, value)
        return returnValue

    
    def getExtendedVertex(self, ui, vi, d):
        returnValue = libpanda._inPHc9WrTUV(self.this, ui, vi, d)
        return returnValue

    
    def getNumUKnots(self):
        returnValue = libpanda._inPHc9WRhHW(self.this)
        return returnValue

    
    def setUKnot(self, i, knot):
        returnValue = libpanda._inPHc9W8ALf(self.this, i, knot)
        return returnValue

    
    def getUKnot(self, i):
        returnValue = libpanda._inPHc9WQ_JQ(self.this, i)
        return returnValue

    
    def normalizeUKnots(self):
        returnValue = libpanda._inPHc9Wkyv3(self.this)
        return returnValue

    
    def getNumVKnots(self):
        returnValue = libpanda._inPHc9WRBK9(self.this)
        return returnValue

    
    def setVKnot(self, i, knot):
        returnValue = libpanda._inPHc9WyADQ(self.this, i, knot)
        return returnValue

    
    def getVKnot(self, i):
        returnValue = libpanda._inPHc9Wm_BB(self.this, i)
        return returnValue

    
    def normalizeVKnots(self):
        returnValue = libpanda._inPHc9W14vv(self.this)
        return returnValue

    
    def getNumUSegments(self):
        returnValue = libpanda._inPHc9WfAIa(self.this)
        return returnValue

    
    def getNumVSegments(self):
        returnValue = libpanda._inPHc9WghMB(self.this)
        return returnValue

    
    def _NurbsSurfaceEvaluator__overloaded_evaluate_ptrConstNurbsSurfaceEvaluator_ptrConstNodePath(self, relTo):
        returnValue = libpanda._inPHc9WKtCQ(self.this, relTo.this)
        import NurbsSurfaceResult
        returnObject = NurbsSurfaceResult.NurbsSurfaceResult(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NurbsSurfaceEvaluator__overloaded_evaluate_ptrConstNurbsSurfaceEvaluator(self):
        returnValue = libpanda._inPHc9WNggZ(self.this)
        import NurbsSurfaceResult
        returnObject = NurbsSurfaceResult.NurbsSurfaceResult(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libpanda._inPHc9Wz87T(self.this, out.this)
        return returnValue

    
    def evaluate(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NurbsSurfaceEvaluator__overloaded_evaluate_ptrConstNurbsSurfaceEvaluator(*_args)
        elif numArgs == 1:
            return self._NurbsSurfaceEvaluator__overloaded_evaluate_ptrConstNurbsSurfaceEvaluator_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setVertex(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    import VBase4
                    if isinstance(_args[2], VBase4.VBase4):
                        return self._NurbsSurfaceEvaluator__overloaded_setVertex_ptrNurbsSurfaceEvaluator_int_int_ptrConstLVecBase4f(*_args)
                    
                    import VBase3
                    if isinstance(_args[2], VBase3.VBase3):
                        return self._NurbsSurfaceEvaluator__overloaded_setVertex_ptrNurbsSurfaceEvaluator_int_int_ptrConstLVecBase3f(*_args)
                    
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 4:
            return self._NurbsSurfaceEvaluator__overloaded_setVertex_ptrNurbsSurfaceEvaluator_int_int_ptrConstLVecBase3f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

    
    def setVertexSpace(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    if isinstance(_args[2], types.StringType):
                        return self._NurbsSurfaceEvaluator__overloaded_setVertexSpace_ptrNurbsSurfaceEvaluator_int_int_atomicstring(*_args)
                    
                    import NodePath
                    if isinstance(_args[2], NodePath.NodePath):
                        return self._NurbsSurfaceEvaluator__overloaded_setVertexSpace_ptrNurbsSurfaceEvaluator_int_int_ptrConstNodePath(*_args)
                    
                    raise TypeError, 'Invalid argument 2, expected one of: <types.StringType> <NodePath.NodePath> '
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 '

    
    def getVertex(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NurbsSurfaceEvaluator__overloaded_getVertex_ptrConstNurbsSurfaceEvaluator_int_int(*_args)
        elif numArgs == 3:
            return self._NurbsSurfaceEvaluator__overloaded_getVertex_ptrConstNurbsSurfaceEvaluator_int_int_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def getUKnots(self):
        knots = []
        for i in range(self.getNumUKnots()):
            knots.append(self.getUKnot(i))
        
        return knots

    
    def getVKnots(self):
        knots = []
        for i in range(self.getNumVKnots()):
            knots.append(self.getVKnot(i))
        
        return knots

    
    def getVertices(self, relTo = None):
        verts = []
        for ui in range(self.getNumUVertices()):
            v = []
            if relTo:
                for vi in range(self.getNumVVertices()):
                    v.append(self.getVertex(ui, vi, relTo))
                
            else:
                for vi in range(self.getNumVVertices()):
                    v.append(self.getVertex(ui, vi))
                
            verts.append(v)
        
        return verts


