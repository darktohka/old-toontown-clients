# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class MultitexReducer(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPXs2xwAX5()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPXs2xKjI_:
            libpanda._inPXs2xKjI_(self.this)
        

    
    def clear(self):
        returnValue = libpanda._inPXs2xDQSi(self.this)
        return returnValue

    
    def _MultitexReducer__overloaded_scan_ptrMultitexReducer_ptrConstNodePath(self, node):
        returnValue = libpanda._inPXs2xEInR(self.this, node.this)
        return returnValue

    
    def _MultitexReducer__overloaded_scan_ptrMultitexReducer_ptrConstNodePath_ptrConstNodePath(self, node, stateFrom):
        returnValue = libpanda._inPXs2xqawa(self.this, node.this, stateFrom.this)
        return returnValue

    
    def _MultitexReducer__overloaded_scan_ptrMultitexReducer_ptrPandaNode_ptrConstRenderState_ptrConstTransformState(self, node, state, transform):
        returnValue = libpanda._inPXs2xcyhS(self.this, node.this, state.this, transform.this)
        return returnValue

    
    def setTarget(self, stage):
        returnValue = libpanda._inPXs2xjnJP(self.this, stage.this)
        return returnValue

    
    def setUseGeom(self, useGeom):
        returnValue = libpanda._inPXs2xl_cC(self.this, useGeom)
        return returnValue

    
    def setAllowTexMat(self, allowTexMat):
        returnValue = libpanda._inPXs2xhlww(self.this, allowTexMat)
        return returnValue

    
    def flatten(self, window):
        returnValue = libpanda._inPXs2xq9Y9(self.this, window.this)
        return returnValue

    
    def scan(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._MultitexReducer__overloaded_scan_ptrMultitexReducer_ptrConstNodePath(*_args)
        elif numArgs == 2:
            return self._MultitexReducer__overloaded_scan_ptrMultitexReducer_ptrConstNodePath_ptrConstNodePath(*_args)
        elif numArgs == 3:
            return self._MultitexReducer__overloaded_scan_ptrMultitexReducer_ptrPandaNode_ptrConstRenderState_ptrConstTransformState(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '


