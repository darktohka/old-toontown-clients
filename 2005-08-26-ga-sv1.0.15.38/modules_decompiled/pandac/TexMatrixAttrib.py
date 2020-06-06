# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RenderAttrib

class TexMatrixAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
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
        

    
    def _TexMatrixAttrib__overloaded_make():
        returnValue = libpanda._inPnJyoFUDw()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TexMatrixAttrib__overloaded_make = staticmethod(_TexMatrixAttrib__overloaded_make)
    
    def _TexMatrixAttrib__overloaded_make_ptrConstLMatrix4f(mat):
        returnValue = libpanda._inPnJyoiX3D(mat.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TexMatrixAttrib__overloaded_make_ptrConstLMatrix4f = staticmethod(_TexMatrixAttrib__overloaded_make_ptrConstLMatrix4f)
    
    def _TexMatrixAttrib__overloaded_make_ptrTextureStage_ptrConstTransformState(stage, transform):
        returnValue = libpanda._inPnJyoKQGr(stage.this, transform.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TexMatrixAttrib__overloaded_make_ptrTextureStage_ptrConstTransformState = staticmethod(_TexMatrixAttrib__overloaded_make_ptrTextureStage_ptrConstTransformState)
    
    def _TexMatrixAttrib__overloaded_make_ptrConstTransformState(transform):
        returnValue = libpanda._inPnJyo5Nar(transform.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TexMatrixAttrib__overloaded_make_ptrConstTransformState = staticmethod(_TexMatrixAttrib__overloaded_make_ptrConstTransformState)
    
    def getClassType():
        returnValue = libpanda._inPnJyo3OB_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def addStage(self, stage, transform):
        returnValue = libpanda._inPnJyo6Dmh(self.this, stage.this, transform.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeStage(self, stage):
        returnValue = libpanda._inPnJyolqcR(self.this, stage.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def isEmpty(self):
        returnValue = libpanda._inPnJyo6GHq(self.this)
        return returnValue

    
    def hasStage(self, stage):
        returnValue = libpanda._inPnJyoogDz(self.this, stage.this)
        return returnValue

    
    def getNumStages(self):
        returnValue = libpanda._inPnJyoCetZ(self.this)
        return returnValue

    
    def getStage(self, n):
        returnValue = libpanda._inPnJyo8HUI(self.this, n)
        import TextureStage
        returnObject = TextureStage.TextureStage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _TexMatrixAttrib__overloaded_getMat_ptrConstTexMatrixAttrib(self):
        returnValue = libpanda._inPnJyojqir(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _TexMatrixAttrib__overloaded_getMat_ptrConstTexMatrixAttrib_ptrTextureStage(self, stage):
        returnValue = libpanda._inPnJyod7Oo(self.this, stage.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getTransform(self, stage):
        returnValue = libpanda._inPnJyoQoZM(self.this, stage.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return TexMatrixAttrib._TexMatrixAttrib__overloaded_make(*_args)
        elif numArgs == 1:
            import TransformState
            if isinstance(_args[0], TransformState.TransformState):
                return TexMatrixAttrib._TexMatrixAttrib__overloaded_make_ptrConstTransformState(*_args)
            
            import Mat4
            if isinstance(_args[0], Mat4.Mat4):
                return TexMatrixAttrib._TexMatrixAttrib__overloaded_make_ptrConstLMatrix4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <TransformState.TransformState> <Mat4.Mat4> '
        elif numArgs == 2:
            return TexMatrixAttrib._TexMatrixAttrib__overloaded_make_ptrTextureStage_ptrConstTransformState(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    make = staticmethod(make)
    
    def getMat(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TexMatrixAttrib__overloaded_getMat_ptrConstTexMatrixAttrib(*_args)
        elif numArgs == 1:
            return self._TexMatrixAttrib__overloaded_getMat_ptrConstTexMatrixAttrib_ptrTextureStage(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


