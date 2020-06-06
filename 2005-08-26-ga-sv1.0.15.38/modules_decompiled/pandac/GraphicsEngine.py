# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class GraphicsEngine(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _GraphicsEngine__overloaded_constructor_ptrPipeline(self, pipeline):
        self.this = libpanda._inPO9cYGcAr(pipeline.this)
        self.userManagesMemory = 1

    
    def _GraphicsEngine__overloaded_constructor(self):
        self.this = libpanda._inPO9cY3Xr_()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPO9cY9YNe:
            libpanda._inPO9cY9YNe(self.this)
        

    
    def setFrameBufferProperties(self, properties):
        returnValue = libpanda._inPO9cYhj_X(self.this, properties.this)
        return returnValue

    
    def getFrameBufferProperties(self):
        returnValue = libpanda._inPO9cYTADD(self.this)
        import FrameBufferProperties
        returnObject = FrameBufferProperties.FrameBufferProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setThreadingModel(self, threadingModel):
        returnValue = libpanda._inPO9cYkzZy(self.this, threadingModel.this)
        return returnValue

    
    def getThreadingModel(self):
        returnValue = libpanda._inPO9cY_NLg(self.this)
        import GraphicsThreadingModel
        returnObject = GraphicsThreadingModel.GraphicsThreadingModel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setAutoFlip(self, autoFlip):
        returnValue = libpanda._inPO9cYpnHT(self.this, autoFlip)
        return returnValue

    
    def getAutoFlip(self):
        returnValue = libpanda._inPO9cYdDTb(self.this)
        return returnValue

    
    def setPortalCull(self, value):
        returnValue = libpanda._inPO9cY5bdZ(self.this, value)
        return returnValue

    
    def getPortalCull(self):
        returnValue = libpanda._inPO9cYsi85(self.this)
        return returnValue

    
    def _GraphicsEngine__overloaded_makeGsg_ptrGraphicsEngine_ptrGraphicsPipe(self, pipe):
        returnValue = libpanda._inPO9cYuwfJ(self.this, pipe.this)
        import GraphicsStateGuardian
        returnObject = GraphicsStateGuardian.GraphicsStateGuardian(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _GraphicsEngine__overloaded_makeGsg_ptrGraphicsEngine_ptrGraphicsPipe_ptrConstFrameBufferProperties_ptrGraphicsStateGuardian(self, pipe, properties, shareWith):
        returnValue = libpanda._inPO9cY01oq(self.this, pipe.this, properties.this, shareWith.this)
        import GraphicsStateGuardian
        returnObject = GraphicsStateGuardian.GraphicsStateGuardian(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _GraphicsEngine__overloaded_makeGsg_ptrGraphicsEngine_ptrGraphicsPipe_ptrConstFrameBufferProperties(self, pipe, properties):
        returnValue = libpanda._inPO9cYMY4C(self.this, pipe.this, properties.this)
        import GraphicsStateGuardian
        returnObject = GraphicsStateGuardian.GraphicsStateGuardian(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def makeWindow(self, gsg, name, sort):
        returnValue = libpanda._inPO9cYLYkZ(self.this, gsg.this, name, sort)
        import GraphicsWindow
        returnObject = GraphicsWindow.GraphicsWindow(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def makeBuffer(self, gsg, name, sort, xSize, ySize, wantTexture):
        returnValue = libpanda._inPO9cYrPH4(self.this, gsg.this, name, sort, xSize, ySize, wantTexture)
        import GraphicsOutput
        returnObject = GraphicsOutput.GraphicsOutput(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def makeParasite(self, host, name, sort, xSize, ySize):
        returnValue = libpanda._inPO9cYs8x6(self.this, host.this, name, sort, xSize, ySize)
        import GraphicsOutput
        returnObject = GraphicsOutput.GraphicsOutput(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeWindow(self, window):
        returnValue = libpanda._inPO9cYQEjj(self.this, window.this)
        return returnValue

    
    def removeAllWindows(self):
        returnValue = libpanda._inPO9cYbizP(self.this)
        return returnValue

    
    def resetAllWindows(self, swapchain):
        returnValue = libpanda._inPO9cY7tzD(self.this, swapchain)
        return returnValue

    
    def isEmpty(self):
        returnValue = libpanda._inPO9cYqWta(self.this)
        return returnValue

    
    def getNumWindows(self):
        returnValue = libpanda._inPO9cYxJBp(self.this)
        return returnValue

    
    def getWindow(self, n):
        returnValue = libpanda._inPO9cYLl7l(self.this, n)
        import GraphicsOutput
        returnObject = GraphicsOutput.GraphicsOutput(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def renderFrame(self):
        returnValue = libpanda._inPO9cY4GAK(self.this)
        return returnValue

    
    def openWindows(self):
        returnValue = libpanda._inPO9cYfeD_(self.this)
        return returnValue

    
    def syncFrame(self):
        returnValue = libpanda._inPO9cYNMb_(self.this)
        return returnValue

    
    def flipFrame(self):
        returnValue = libpanda._inPO9cYbWRO(self.this)
        return returnValue

    
    def renderSubframe(self, gsg, dr, cullSorting):
        returnValue = libpanda._inPO9cYvl30(self.this, gsg.this, dr.this, cullSorting)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._GraphicsEngine__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._GraphicsEngine__overloaded_constructor_ptrPipeline(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def makeGsg(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._GraphicsEngine__overloaded_makeGsg_ptrGraphicsEngine_ptrGraphicsPipe(*_args)
        elif numArgs == 2:
            return self._GraphicsEngine__overloaded_makeGsg_ptrGraphicsEngine_ptrGraphicsPipe_ptrConstFrameBufferProperties(*_args)
        elif numArgs == 3:
            return self._GraphicsEngine__overloaded_makeGsg_ptrGraphicsEngine_ptrGraphicsPipe_ptrConstFrameBufferProperties_ptrGraphicsStateGuardian(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '


