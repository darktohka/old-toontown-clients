# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class GeomNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyo3eFF(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyo0yAx:
            libpanda._inPnJyo0yAx(self.this)
        

    
    def getDefaultCollideMask():
        returnValue = libpanda._inPnJyolm7A()
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getDefaultCollideMask = staticmethod(getDefaultCollideMask)
    
    def getClassType():
        returnValue = libpanda._inPnJyonVK5()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getNumGeoms(self):
        returnValue = libpanda._inPnJyoI0Ys(self.this)
        return returnValue

    
    def getGeom(self, n):
        returnValue = libpanda._inPnJyoAgFb(self.this, n)
        import Geom
        returnObject = Geom.Geom(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getUniqueGeom(self, n):
        returnValue = libpanda._inPnJyoiPT0(self.this, n)
        import Geom
        returnObject = Geom.Geom(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getGeomState(self, n):
        returnValue = libpanda._inPnJyoeIGG(self.this, n)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setGeomState(self, n, state):
        returnValue = libpanda._inPnJyoqNIz(self.this, n, state.this)
        return returnValue

    
    def _GeomNode__overloaded_addGeom_ptrGeomNode_ptrGeom_ptrConstRenderState(self, geom, state):
        returnValue = libpanda._inPnJyoA4ql(self.this, geom.this, state.this)
        return returnValue

    
    def _GeomNode__overloaded_addGeom_ptrGeomNode_ptrGeom(self, geom):
        returnValue = libpanda._inPnJyog1uL(self.this, geom.this)
        return returnValue

    
    def addGeomsFrom(self, other):
        returnValue = libpanda._inPnJyo06du(self.this, other.this)
        return returnValue

    
    def removeGeom(self, n):
        returnValue = libpanda._inPnJyoV9b7(self.this, n)
        return returnValue

    
    def removeAllGeoms(self):
        returnValue = libpanda._inPnJyo_NLA(self.this)
        return returnValue

    
    def writeGeoms(self, out, indentLevel):
        returnValue = libpanda._inPnJyoWbSk(self.this, out.this, indentLevel)
        return returnValue

    
    def writeVerbose(self, out, indentLevel):
        returnValue = libpanda._inPnJyoSkiE(self.this, out.this, indentLevel)
        return returnValue

    
    def addGeom(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._GeomNode__overloaded_addGeom_ptrGeomNode_ptrGeom(*_args)
        elif numArgs == 2:
            return self._GeomNode__overloaded_addGeom_ptrGeomNode_ptrGeom_ptrConstRenderState(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


