# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
from direct.ffi import FFIExternalObject

class EggTransform3d(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts]
    CTRotz = 4
    CTRotx = 2
    CTInvalid = 0
    CTRotate = 5
    CTMatrix = 8
    CTTranslate = 1
    CTUniformScale = 7
    CTRoty = 3
    CTScale = 6
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggTransform3d__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMOX5E()
        self.userManagesMemory = 1

    
    def _EggTransform3d__overloaded_constructor_ptrConstEggTransform3d(self, copy):
        self.this = libpandaegg._inPkAOMONa2(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOM2JsJ:
            libpandaegg._inPkAOM2JsJ(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOM52Rw(self.this, copy.this)
        returnObject = EggTransform3d(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clearTransform(self):
        returnValue = libpandaegg._inPkAOMAh3J(self.this)
        return returnValue

    
    def addTranslate(self, translate):
        returnValue = libpandaegg._inPkAOMCLJh(self.this, translate.this)
        return returnValue

    
    def addRotx(self, angle):
        returnValue = libpandaegg._inPkAOMLxrY(self.this, angle)
        return returnValue

    
    def addRoty(self, angle):
        returnValue = libpandaegg._inPkAOMvzrm(self.this, angle)
        return returnValue

    
    def addRotz(self, angle):
        returnValue = libpandaegg._inPkAOMD2r0(self.this, angle)
        return returnValue

    
    def _EggTransform3d__overloaded_addRotate_ptrEggTransform3d_ptrConstLQuaterniond(self, quat):
        returnValue = libpandaegg._inPkAOMf2ja(self.this, quat.this)
        return returnValue

    
    def _EggTransform3d__overloaded_addRotate_ptrEggTransform3d_double_ptrConstLVector3d(self, angle, axis):
        returnValue = libpandaegg._inPkAOMrh6f(self.this, angle, axis.this)
        return returnValue

    
    def addScale(self, scale):
        returnValue = libpandaegg._inPkAOM9KbB(self.this, scale.this)
        return returnValue

    
    def addUniformScale(self, scale):
        returnValue = libpandaegg._inPkAOM7BWv(self.this, scale)
        return returnValue

    
    def addMatrix(self, mat):
        returnValue = libpandaegg._inPkAOMJuAF(self.this, mat.this)
        return returnValue

    
    def hasTransform(self):
        returnValue = libpandaegg._inPkAOMKwxE(self.this)
        return returnValue

    
    def setTransform(self, mat):
        returnValue = libpandaegg._inPkAOMeSHs(self.this, mat.this)
        return returnValue

    
    def getTransform(self):
        returnValue = libpandaegg._inPkAOMVTx3(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def transformIsIdentity(self):
        returnValue = libpandaegg._inPkAOMN3eV(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpandaegg._inPkAOMXPMG(self.this)
        return returnValue

    
    def getComponentType(self, n):
        returnValue = libpandaegg._inPkAOMd1lP(self.this, n)
        return returnValue

    
    def getComponentNumber(self, n):
        returnValue = libpandaegg._inPkAOMR3qK(self.this, n)
        return returnValue

    
    def getComponentVector(self, n):
        returnValue = libpandaegg._inPkAOMCR2C(self.this, n)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getComponentMatrix(self, n):
        returnValue = libpandaegg._inPkAOMTAl3(self.this, n)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def write(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMy0ah(self.this, out.this, indentLevel)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggTransform3d__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._EggTransform3d__overloaded_constructor_ptrConstEggTransform3d(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def addRotate(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggTransform3d__overloaded_addRotate_ptrEggTransform3d_ptrConstLQuaterniond(*_args)
        elif numArgs == 2:
            return self._EggTransform3d__overloaded_addRotate_ptrEggTransform3d_double_ptrConstLVector3d(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


