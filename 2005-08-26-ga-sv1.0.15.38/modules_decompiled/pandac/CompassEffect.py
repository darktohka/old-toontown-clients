# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RenderEffect

class CompassEffect(RenderEffect.RenderEffect, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    PSz = 64
    PScale = 112
    PSx = 16
    PY = 2
    PAll = 127
    PSy = 32
    PZ = 4
    PX = 1
    PRot = 8
    PPos = 7
    
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
        if libpanda and libpanda._inPnJyoI6Wp:
            libpanda._inPnJyoI6Wp(self.this)
        

    
    def _CompassEffect__overloaded_make_ptrConstNodePath_int(reference, properties):
        returnValue = libpanda._inPnJyo1e7i(reference.this, properties)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _CompassEffect__overloaded_make_ptrConstNodePath_int = staticmethod(_CompassEffect__overloaded_make_ptrConstNodePath_int)
    
    def _CompassEffect__overloaded_make_ptrConstNodePath(reference):
        returnValue = libpanda._inPnJyoo3bC(reference.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _CompassEffect__overloaded_make_ptrConstNodePath = staticmethod(_CompassEffect__overloaded_make_ptrConstNodePath)
    
    def getClassType():
        returnValue = libpanda._inPnJyoeHvU()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getReference(self):
        returnValue = libpanda._inPnJyo9Dfu(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getProperties(self):
        returnValue = libpanda._inPnJyoNQdF(self.this)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return CompassEffect._CompassEffect__overloaded_make_ptrConstNodePath(*_args)
        elif numArgs == 2:
            return CompassEffect._CompassEffect__overloaded_make_ptrConstNodePath_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    make = staticmethod(make)

