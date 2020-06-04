# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class GraphicsChannel(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
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
        

    
    def getClassType():
        returnValue = libpanda._inPO9cYkR3A()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _GraphicsChannel__overloaded_makeLayer_ptrGraphicsChannel_int(self, sort):
        returnValue = libpanda._inPO9cYTgeC(self.this, sort)
        import GraphicsLayer
        returnObject = GraphicsLayer.GraphicsLayer(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _GraphicsChannel__overloaded_makeLayer_ptrGraphicsChannel(self):
        returnValue = libpanda._inPO9cYXEYv(self.this)
        import GraphicsLayer
        returnObject = GraphicsLayer.GraphicsLayer(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeLayer(self, layer):
        returnValue = libpanda._inPO9cYxD5N(self.this, layer.this)
        return returnValue

    
    def moveLayer(self, layer, sort):
        returnValue = libpanda._inPO9cYx6ja(self.this, layer.this, sort)
        return returnValue

    
    def getNumLayers(self):
        returnValue = libpanda._inPO9cYpjyB(self.this)
        return returnValue

    
    def getLayer(self, index):
        returnValue = libpanda._inPO9cYntbt(self.this, index)
        import GraphicsLayer
        returnObject = GraphicsLayer.GraphicsLayer(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getWindow(self):
        returnValue = libpanda._inPO9cYUob5(self.this)
        import GraphicsOutput
        returnObject = GraphicsOutput.GraphicsOutput(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getPipe(self):
        returnValue = libpanda._inPO9cYknwJ(self.this)
        import GraphicsPipe
        returnObject = GraphicsPipe.GraphicsPipe(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def setActive(self, active):
        returnValue = libpanda._inPO9cYuvNq(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libpanda._inPO9cYtMTC(self.this)
        return returnValue

    
    def makeLayer(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._GraphicsChannel__overloaded_makeLayer_ptrGraphicsChannel(*_args)
        elif numArgs == 1:
            return self._GraphicsChannel__overloaded_makeLayer_ptrGraphicsChannel_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


