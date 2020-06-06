# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class GraphicsEngine(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _GraphicsEngine__overloaded_constructor_ptrPipeline(self, pipeline):
        self.this = libpanda._inPO9cYHcAr(pipeline.this)
        self.userManagesMemory = 1

    
    def _GraphicsEngine__overloaded_constructor(self):
        self.this = libpanda._inPO9cY2Xr_()
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
        returnValue = libpanda._inPO9cYjzZy(self.this, threadingModel.this)
        return returnValue

    
    def getThreadingModel(self):
        returnValue = libpanda._inPO9cY5NLg(self.this)
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

    
    def _GraphicsEngine__overloaded_makeGsg_ptrGraphicsEngine_ptrGraphicsPipe(self, pipe):
        returnValue = libpanda._inPO9cYuwfJ(self.this, pipe.this)
        import GraphicsStateGuardian
        returnObject = GraphicsStateGuardian.GraphicsStateGuardian(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _GraphicsEngine__overloaded_makeGsg_ptrGraphicsEngine_ptrGraphicsPipe_ptrConstFrameBufferProperties_ptrConstGraphicsThreadingModel(self, pipe, properties, threadingModel):
        returnValue = libpanda._inPO9cYTNkx(self.this, pipe.this, properties.this, threadingModel.this)
        import GraphicsStateGuardian
        returnObject = GraphicsStateGuardian.GraphicsStateGuardian(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _GraphicsEngine__overloaded_makeWindow_ptrGraphicsEngine_ptrGraphicsPipe_ptrGraphicsStateGuardian(self, pipe, gsg):
        returnValue = libpanda._inPO9cY57Hy(self.this, pipe.this, gsg.this)
        import GraphicsWindow
        returnObject = GraphicsWindow.GraphicsWindow(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _GraphicsEngine__overloaded_makeWindow_ptrGraphicsEngine_ptrGraphicsPipe_ptrGraphicsStateGuardian_ptrConstGraphicsThreadingModel(self, pipe, gsg, threadingModel):
        returnValue = libpanda._inPO9cYTOlP(self.this, pipe.this, gsg.this, threadingModel.this)
        import GraphicsWindow
        returnObject = GraphicsWindow.GraphicsWindow(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeWindow(self, window):
        returnValue = libpanda._inPO9cYm_3n(self.this, window.this)
        return returnValue

    
    def removeAllWindows(self):
        returnValue = libpanda._inPO9cYbizP(self.this)
        return returnValue

    
    def isEmpty(self):
        returnValue = libpanda._inPO9cYqWta(self.this)
        return returnValue

    
    def renderFrame(self):
        returnValue = libpanda._inPO9cY4GAK(self.this)
        return returnValue

    
    def syncFrame(self):
        returnValue = libpanda._inPO9cYOMb_(self.this)
        return returnValue

    
    def flipFrame(self):
        returnValue = libpanda._inPO9cYbWRO(self.this)
        return returnValue

    
    def renderSubframe(self, gsg, dr, cullSorting):
        returnValue = libpanda._inPO9cYul30(self.this, gsg.this, dr.this, cullSorting)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._GraphicsEngine__overloaded_constructor()
        elif numArgs == 1:
            import Pipeline
            if isinstance(_args[0], Pipeline.Pipeline):
                return self._GraphicsEngine__overloaded_constructor_ptrPipeline(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Pipeline.Pipeline> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def makeWindow(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import GraphicsPipe
            if isinstance(_args[0], GraphicsPipe.GraphicsPipe):
                import GraphicsStateGuardian
                if isinstance(_args[1], GraphicsStateGuardian.GraphicsStateGuardian):
                    return self._GraphicsEngine__overloaded_makeWindow_ptrGraphicsEngine_ptrGraphicsPipe_ptrGraphicsStateGuardian(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <GraphicsStateGuardian.GraphicsStateGuardian> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <GraphicsPipe.GraphicsPipe> '
        elif numArgs == 3:
            import GraphicsPipe
            if isinstance(_args[0], GraphicsPipe.GraphicsPipe):
                import GraphicsStateGuardian
                if isinstance(_args[1], GraphicsStateGuardian.GraphicsStateGuardian):
                    import GraphicsThreadingModel
                    if isinstance(_args[2], GraphicsThreadingModel.GraphicsThreadingModel):
                        return self._GraphicsEngine__overloaded_makeWindow_ptrGraphicsEngine_ptrGraphicsPipe_ptrGraphicsStateGuardian_ptrConstGraphicsThreadingModel(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <GraphicsThreadingModel.GraphicsThreadingModel> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <GraphicsStateGuardian.GraphicsStateGuardian> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <GraphicsPipe.GraphicsPipe> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def makeGsg(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import GraphicsPipe
            if isinstance(_args[0], GraphicsPipe.GraphicsPipe):
                return self._GraphicsEngine__overloaded_makeGsg_ptrGraphicsEngine_ptrGraphicsPipe(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <GraphicsPipe.GraphicsPipe> '
        elif numArgs == 3:
            import GraphicsPipe
            if isinstance(_args[0], GraphicsPipe.GraphicsPipe):
                import FrameBufferProperties
                if isinstance(_args[1], FrameBufferProperties.FrameBufferProperties):
                    import GraphicsThreadingModel
                    if isinstance(_args[2], GraphicsThreadingModel.GraphicsThreadingModel):
                        return self._GraphicsEngine__overloaded_makeGsg_ptrGraphicsEngine_ptrGraphicsPipe_ptrConstFrameBufferProperties_ptrConstGraphicsThreadingModel(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <GraphicsThreadingModel.GraphicsThreadingModel> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <FrameBufferProperties.FrameBufferProperties> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <GraphicsPipe.GraphicsPipe> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


