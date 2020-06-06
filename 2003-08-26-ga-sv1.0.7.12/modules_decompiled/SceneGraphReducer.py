# File: S (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class SceneGraphReducer(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    TTColorScale = 4
    TTColor = 2
    TTTexMatrix = 8
    TTOther = 16
    TTTransform = 1
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPkJyoZ4fC()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyo36ol:
            libpanda._inPkJyo36ol(self.this)
        

    
    def _SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode_ptrConstAccumulatedAttribs_int_ptrGeomTransformer(self, node, attribs, attribTypes, transformer):
        returnValue = libpanda._inPkJyo8UjV(self.this, node.this, attribs.this, attribTypes, transformer.this)
        return returnValue

    
    def _SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode_int(self, node, attribTypes):
        returnValue = libpanda._inPkJyoTFiF(self.this, node.this, attribTypes)
        return returnValue

    
    def _SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode(self, node):
        returnValue = libpanda._inPkJyoVc_G(self.this, node.this)
        return returnValue

    
    def flatten(self, root, combineSiblings):
        returnValue = libpanda._inPkJyocktX(self.this, root.this, combineSiblings)
        return returnValue

    
    def applyAttribs(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self._SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        elif numArgs == 2:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                if isinstance(_args[1], types.IntType):
                    return self._SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        elif numArgs == 4:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                import AccumulatedAttribs
                if isinstance(_args[1], AccumulatedAttribs.AccumulatedAttribs):
                    if isinstance(_args[2], types.IntType):
                        import GeomTransformer
                        if isinstance(_args[3], GeomTransformer.GeomTransformer):
                            return self._SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode_ptrConstAccumulatedAttribs_int_ptrGeomTransformer(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <GeomTransformer.GeomTransformer> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <AccumulatedAttribs.AccumulatedAttribs> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 4 '


