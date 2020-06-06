# File: S (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class SceneGraphReducer(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    TTColorScale = 4
    TTColor = 2
    TTTexMatrix = 8
    TTOther = 16
    TTTransform = 1
    CSRecurse = 4
    CSOther = 1
    CSGeomNode = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPnJyoZ4fC()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyo26ol:
            libpanda._inPnJyo26ol(self.this)
        

    
    def _SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode_ptrConstAccumulatedAttribs_int_ptrGeomTransformer(self, node, attribs, attribTypes, transformer):
        returnValue = libpanda._inPnJyo8UjV(self.this, node.this, attribs.this, attribTypes, transformer.this)
        return returnValue

    
    def _SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode_int(self, node, attribTypes):
        returnValue = libpanda._inPnJyoTFiF(self.this, node.this, attribTypes)
        return returnValue

    
    def _SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode(self, node):
        returnValue = libpanda._inPnJyoVc_G(self.this, node.this)
        return returnValue

    
    def flatten(self, root, combineSiblingsBits):
        returnValue = libpanda._inPnJyo_6fT(self.this, root.this, combineSiblingsBits)
        return returnValue

    
    def applyAttribs(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode(*_args)
        elif numArgs == 2:
            return self._SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode_int(*_args)
        elif numArgs == 4:
            return self._SceneGraphReducer__overloaded_applyAttribs_ptrSceneGraphReducer_ptrPandaNode_ptrConstAccumulatedAttribs_int_ptrGeomTransformer(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 4 '


