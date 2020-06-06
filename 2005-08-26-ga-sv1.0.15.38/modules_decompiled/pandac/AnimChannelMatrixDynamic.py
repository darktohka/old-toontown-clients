# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import AnimChannelACMatrixSwitchType

class AnimChannelMatrixDynamic(AnimChannelACMatrixSwitchType.AnimChannelACMatrixSwitchType, FFIExternalObject.FFIExternalObject):
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
        

    
    def destructor(self):
        if libpanda and libpanda._inPn9gMqIUu:
            libpanda._inPn9gMqIUu(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPn9gMdU9M()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _AnimChannelMatrixDynamic__overloaded_setValue_ptrAnimChannelMatrixDynamic_ptrConstLMatrix4f(self, value):
        returnValue = libpanda._inPn9gMwi1P(self.this, value.this)
        return returnValue

    
    def _AnimChannelMatrixDynamic__overloaded_setValue_ptrAnimChannelMatrixDynamic_ptrConstTransformState(self, value):
        returnValue = libpanda._inPn9gM4XtZ(self.this, value.this)
        return returnValue

    
    def setValueNode(self, node):
        returnValue = libpanda._inPn9gMAd6G(self.this, node.this)
        return returnValue

    
    def setValue(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import TransformState
            if isinstance(_args[0], TransformState.TransformState):
                return self._AnimChannelMatrixDynamic__overloaded_setValue_ptrAnimChannelMatrixDynamic_ptrConstTransformState(*_args)
            
            import Mat4
            if isinstance(_args[0], Mat4.Mat4):
                return self._AnimChannelMatrixDynamic__overloaded_setValue_ptrAnimChannelMatrixDynamic_ptrConstLMatrix4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <TransformState.TransformState> <Mat4.Mat4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


