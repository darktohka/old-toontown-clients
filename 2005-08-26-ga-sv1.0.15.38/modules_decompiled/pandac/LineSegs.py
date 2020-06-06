# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Namable

class LineSegs(Namable.Namable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LineSegs__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPXs2xcyYH(name)
        self.userManagesMemory = 1

    
    def _LineSegs__overloaded_constructor(self):
        self.this = libpanda._inPXs2xWNQY()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPXs2xeDuo:
            libpanda._inPXs2xeDuo(self.this)
        

    
    def reset(self):
        returnValue = libpanda._inPXs2xgqmq(self.this)
        return returnValue

    
    def _LineSegs__overloaded_setColor_ptrLineSegs_ptrConstLVecBase4f(self, color):
        returnValue = libpanda._inPXs2x0j3d(self.this, color.this)
        return returnValue

    
    def _LineSegs__overloaded_setColor_ptrLineSegs_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPXs2xoG3B(self.this, r, g, b, a)
        return returnValue

    
    def _LineSegs__overloaded_setColor_ptrLineSegs_float_float_float(self, r, g, b):
        returnValue = libpanda._inPXs2xIOs9(self.this, r, g, b)
        return returnValue

    
    def setThickness(self, thick):
        returnValue = libpanda._inPXs2xJ0o7(self.this, thick)
        return returnValue

    
    def _LineSegs__overloaded_moveTo_ptrLineSegs_ptrConstLVecBase3f(self, v):
        returnValue = libpanda._inPXs2x8wH1(self.this, v.this)
        return returnValue

    
    def _LineSegs__overloaded_moveTo_ptrLineSegs_float_float_float(self, x, y, z):
        returnValue = libpanda._inPXs2xrLxC(self.this, x, y, z)
        return returnValue

    
    def _LineSegs__overloaded_drawTo_ptrLineSegs_ptrConstLVecBase3f(self, v):
        returnValue = libpanda._inPXs2xq1dS(self.this, v.this)
        return returnValue

    
    def _LineSegs__overloaded_drawTo_ptrLineSegs_float_float_float(self, x, y, z):
        returnValue = libpanda._inPXs2x8oGg(self.this, x, y, z)
        return returnValue

    
    def getCurrentPosition(self):
        returnValue = libpanda._inPXs2xHil_(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isEmpty(self):
        returnValue = libpanda._inPXs2xBf1p(self.this)
        return returnValue

    
    def _LineSegs__overloaded_create_ptrLineSegs_ptrGeomNode_bool(self, previous, frameAccurate):
        returnValue = libpanda._inPXs2xZFoc(self.this, previous.this, frameAccurate)
        import GeomNode
        returnObject = GeomNode.GeomNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _LineSegs__overloaded_create_ptrLineSegs_ptrGeomNode(self, previous):
        returnValue = libpanda._inPXs2x_ama(self.this, previous.this)
        import GeomNode
        returnObject = GeomNode.GeomNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _LineSegs__overloaded_create_ptrLineSegs_bool(self, frameAccurate):
        returnValue = libpanda._inPXs2xDS3i(self.this, frameAccurate)
        import GeomNode
        returnObject = GeomNode.GeomNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _LineSegs__overloaded_create_ptrLineSegs(self):
        returnValue = libpanda._inPXs2xt4D_(self.this)
        import GeomNode
        returnObject = GeomNode.GeomNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumVertices(self):
        returnValue = libpanda._inPXs2xLyjT(self.this)
        return returnValue

    
    def getVertex(self, vertex):
        returnValue = libpanda._inPXs2x62YQ(self.this, vertex)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _LineSegs__overloaded_setVertex_ptrLineSegs_int_ptrConstLPoint3f(self, vertex, vert):
        returnValue = libpanda._inPXs2xMZV4(self.this, vertex, vert.this)
        return returnValue

    
    def _LineSegs__overloaded_setVertex_ptrLineSegs_int_float_float_float(self, vertex, x, y, z):
        returnValue = libpanda._inPXs2xx0WV(self.this, vertex, x, y, z)
        return returnValue

    
    def getVertexColor(self, vertex):
        returnValue = libpanda._inPXs2x6Cje(self.this, vertex)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _LineSegs__overloaded_setVertexColor_ptrLineSegs_int_ptrConstLVecBase4f(self, vertex, color):
        returnValue = libpanda._inPXs2xzZOI(self.this, vertex, color.this)
        return returnValue

    
    def _LineSegs__overloaded_setVertexColor_ptrLineSegs_int_float_float_float_float(self, vertex, r, g, b, a):
        returnValue = libpanda._inPXs2xP_Xd(self.this, vertex, r, g, b, a)
        return returnValue

    
    def _LineSegs__overloaded_setVertexColor_ptrLineSegs_int_float_float_float(self, vertex, r, g, b):
        returnValue = libpanda._inPXs2xFwym(self.this, vertex, r, g, b)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LineSegs__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._LineSegs__overloaded_constructor_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def moveTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._LineSegs__overloaded_moveTo_ptrLineSegs_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._LineSegs__overloaded_moveTo_ptrLineSegs_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setVertex(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._LineSegs__overloaded_setVertex_ptrLineSegs_int_ptrConstLPoint3f(*_args)
        elif numArgs == 4:
            return self._LineSegs__overloaded_setVertex_ptrLineSegs_int_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

    
    def setColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._LineSegs__overloaded_setColor_ptrLineSegs_ptrConstLVecBase4f(*_args)
        elif numArgs == 3:
            return self._LineSegs__overloaded_setColor_ptrLineSegs_float_float_float(*_args)
        elif numArgs == 4:
            return self._LineSegs__overloaded_setColor_ptrLineSegs_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 4 '

    
    def create(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LineSegs__overloaded_create_ptrLineSegs(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._LineSegs__overloaded_create_ptrLineSegs_bool(*_args)
            
            import GeomNode
            if isinstance(_args[0], GeomNode.GeomNode):
                return self._LineSegs__overloaded_create_ptrLineSegs_ptrGeomNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <GeomNode.GeomNode> '
        elif numArgs == 2:
            return self._LineSegs__overloaded_create_ptrLineSegs_ptrGeomNode_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def drawTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._LineSegs__overloaded_drawTo_ptrLineSegs_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._LineSegs__overloaded_drawTo_ptrLineSegs_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setVertexColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._LineSegs__overloaded_setVertexColor_ptrLineSegs_int_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._LineSegs__overloaded_setVertexColor_ptrLineSegs_int_float_float_float(*_args)
        elif numArgs == 5:
            return self._LineSegs__overloaded_setVertexColor_ptrLineSegs_int_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 5 '


