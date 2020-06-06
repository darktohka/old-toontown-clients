# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import GraphicsStateGuardianBase

class GraphicsStateGuardian(GraphicsStateGuardianBase.GraphicsStateGuardianBase, FFIExternalObject.FFIExternalObject):
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
        returnValue = libpanda._inPO9cYX9JS()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def releaseAllTextures(self):
        returnValue = libpanda._inPO9cYNhtg(self.this)
        return returnValue

    
    def releaseAllGeoms(self):
        returnValue = libpanda._inPO9cYtq2Y(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libpanda._inPO9cY41Tn(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libpanda._inPO9cYWMEv(self.this)
        return returnValue

    
    def getProperties(self):
        returnValue = libpanda._inPO9cYS5Ul(self.this)
        import FrameBufferProperties
        returnObject = FrameBufferProperties.FrameBufferProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getPipe(self):
        returnValue = libpanda._inPO9cYXe8K(self.this)
        import GraphicsPipe
        returnObject = GraphicsPipe.GraphicsPipe(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getEngine(self):
        returnValue = libpanda._inPO9cYG5DS(self.this)
        import GraphicsEngine
        returnObject = GraphicsEngine.GraphicsEngine(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getThreadingModel(self):
        returnValue = libpanda._inPO9cYax_q(self.this)
        import GraphicsThreadingModel
        returnObject = GraphicsThreadingModel.GraphicsThreadingModel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getMaxTextureStages(self):
        returnValue = libpanda._inPO9cYuf8m(self.this)
        return returnValue

    
    def getCopyTextureInverted(self):
        returnValue = libpanda._inPO9cY4Ta6(self.this)
        return returnValue

    
    def getSupportsGenerateMipmap(self):
        returnValue = libpanda._inPO9cY9xp9(self.this)
        return returnValue


