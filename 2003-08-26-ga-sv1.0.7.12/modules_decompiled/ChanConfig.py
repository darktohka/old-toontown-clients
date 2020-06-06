# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class ChanConfig(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _ChanConfig__overloaded_constructor_ptrGraphicsEngine_ptrGraphicsPipe_atomicstring_ptrConstNodePath_ptrChanCfgOverrides(self, engine, pipe, cfg, render, parameter4):
        self.this = libpanda._inPfYohek_C(engine.this, pipe.this, cfg, render.this, parameter4.this)
        self.userManagesMemory = 1

    
    def _ChanConfig__overloaded_constructor_ptrGraphicsEngine_ptrGraphicsPipe_atomicstring_ptrConstNodePath(self, engine, pipe, cfg, render):
        self.this = libpanda._inPfYoht5xL(engine.this, pipe.this, cfg, render.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPfYohUyu_:
            libpanda._inPfYohUyu_(self.this)
        

    
    def getGroupNode(self, nodeIndex):
        returnValue = libpanda._inPfYoh_02t(self.this, nodeIndex)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getGroupMembership(self, drIndex):
        returnValue = libpanda._inPfYohu6Ps(self.this, drIndex)
        return returnValue

    
    def getNumGroups(self):
        returnValue = libpanda._inPfYohogyc(self.this)
        return returnValue

    
    def getNumDrs(self):
        returnValue = libpanda._inPfYoh56Mu(self.this)
        return returnValue

    
    def getDr(self, drIndex):
        returnValue = libpanda._inPfYoh3Vik(self.this, drIndex)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getWin(self):
        returnValue = libpanda._inPfYohR8JL(self.this)
        import GraphicsWindow
        returnObject = GraphicsWindow.GraphicsWindow(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 4:
            import GraphicsEngine
            if isinstance(_args[0], GraphicsEngine.GraphicsEngine):
                import GraphicsPipe
                if isinstance(_args[1], GraphicsPipe.GraphicsPipe):
                    if isinstance(_args[2], types.StringType):
                        import NodePath
                        if isinstance(_args[3], NodePath.NodePath):
                            return self._ChanConfig__overloaded_constructor_ptrGraphicsEngine_ptrGraphicsPipe_atomicstring_ptrConstNodePath(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <NodePath.NodePath> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <GraphicsPipe.GraphicsPipe> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <GraphicsEngine.GraphicsEngine> '
        elif numArgs == 5:
            import GraphicsEngine
            if isinstance(_args[0], GraphicsEngine.GraphicsEngine):
                import GraphicsPipe
                if isinstance(_args[1], GraphicsPipe.GraphicsPipe):
                    if isinstance(_args[2], types.StringType):
                        import NodePath
                        if isinstance(_args[3], NodePath.NodePath):
                            import ChanCfgOverrides
                            if isinstance(_args[4], ChanCfgOverrides.ChanCfgOverrides):
                                return self._ChanConfig__overloaded_constructor_ptrGraphicsEngine_ptrGraphicsPipe_atomicstring_ptrConstNodePath_ptrChanCfgOverrides(_args[0], _args[1], _args[2], _args[3], _args[4])
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <ChanCfgOverrides.ChanCfgOverrides> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <NodePath.NodePath> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <GraphicsPipe.GraphicsPipe> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <GraphicsEngine.GraphicsEngine> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 4 5 '


