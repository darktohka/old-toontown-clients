# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PandaNode

class GeomNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPkJyo3eFF(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyo3yAx:
            libpanda._inPkJyo3yAx(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPkJyomVK5()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getNumGeoms(self):
        returnValue = libpanda._inPkJyoJ0Ys(self.this)
        return returnValue

    
    def getGeom(self, n):
        returnValue = libpanda._inPkJyoAgFb(self.this, n)
        import Geom
        returnObject = Geom.Geom(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getGeomState(self, n):
        returnValue = libpanda._inPkJyoeIGG(self.this, n)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setGeomState(self, n, state):
        returnValue = libpanda._inPkJyotNIz(self.this, n, state.this)
        return returnValue

    
    def _GeomNode__overloaded_addGeom_ptrGeomNode_ptrGeom_ptrConstRenderState(self, geom, state):
        returnValue = libpanda._inPkJyoB4ql(self.this, geom.this, state.this)
        return returnValue

    
    def _GeomNode__overloaded_addGeom_ptrGeomNode_ptrGeom(self, geom):
        returnValue = libpanda._inPkJyog1uL(self.this, geom.this)
        return returnValue

    
    def addGeomsFrom(self, other):
        returnValue = libpanda._inPkJyo36du(self.this, other.this)
        return returnValue

    
    def removeGeom(self, n):
        returnValue = libpanda._inPkJyoW9b7(self.this, n)
        return returnValue

    
    def removeAllGeoms(self):
        returnValue = libpanda._inPkJyo_NLA(self.this)
        return returnValue

    
    def writeGeoms(self, out, indentLevel):
        returnValue = libpanda._inPkJyoZbSk(self.this, out.this, indentLevel)
        return returnValue

    
    def writeVerbose(self, out, indentLevel):
        returnValue = libpanda._inPkJyoSkiE(self.this, out.this, indentLevel)
        return returnValue

    
    def addGeom(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Geom
            if isinstance(_args[0], Geom.Geom):
                return self._GeomNode__overloaded_addGeom_ptrGeomNode_ptrGeom(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Geom.Geom> '
        elif numArgs == 2:
            import Geom
            if isinstance(_args[0], Geom.Geom):
                import RenderState
                if isinstance(_args[1], RenderState.RenderState):
                    return self._GeomNode__overloaded_addGeom_ptrGeomNode_ptrGeom_ptrConstRenderState(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <RenderState.RenderState> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Geom.Geom> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


