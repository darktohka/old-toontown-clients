# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount

class Material(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Material__overloaded_constructor(self):
        self.this = libpanda._inPMAKP__MD()
        self.userManagesMemory = 1

    
    def _Material__overloaded_constructor_ptrConstMaterial(self, copy):
        self.this = libpanda._inPMAKPGQ_b(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPMAKPc7AP()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpanda._inPMAKP9ooi(self.this, copy.this)
        returnObject = Material(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasAmbient(self):
        returnValue = libpanda._inPMAKP7f5w(self.this)
        return returnValue

    
    def getAmbient(self):
        returnValue = libpanda._inPMAKPZcqI(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setAmbient(self, color):
        returnValue = libpanda._inPMAKP34VB(self.this, color.this)
        return returnValue

    
    def clearAmbient(self):
        returnValue = libpanda._inPMAKPefxD(self.this)
        return returnValue

    
    def hasDiffuse(self):
        returnValue = libpanda._inPMAKPUInK(self.this)
        return returnValue

    
    def getDiffuse(self):
        returnValue = libpanda._inPMAKP7Iai(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setDiffuse(self, color):
        returnValue = libpanda._inPMAKPZ0Eb(self.this, color.this)
        return returnValue

    
    def clearDiffuse(self):
        returnValue = libpanda._inPMAKPAqqE(self.this)
        return returnValue

    
    def hasSpecular(self):
        returnValue = libpanda._inPMAKPW6_3(self.this)
        return returnValue

    
    def getSpecular(self):
        returnValue = libpanda._inPMAKP8lwP(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setSpecular(self, color):
        returnValue = libpanda._inPMAKPdfyI(self.this, color.this)
        return returnValue

    
    def clearSpecular(self):
        returnValue = libpanda._inPMAKPcNUr(self.this)
        return returnValue

    
    def hasEmission(self):
        returnValue = libpanda._inPMAKP03rd(self.this)
        return returnValue

    
    def getEmission(self):
        returnValue = libpanda._inPMAKPb2c1(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setEmission(self, color):
        returnValue = libpanda._inPMAKPwIeu(self.this, color.this)
        return returnValue

    
    def clearEmission(self):
        returnValue = libpanda._inPMAKPjKsu(self.this)
        return returnValue

    
    def getShininess(self):
        returnValue = libpanda._inPMAKP8cpp(self.this)
        return returnValue

    
    def setShininess(self, shininess):
        returnValue = libpanda._inPMAKP_D1v(self.this, shininess)
        return returnValue

    
    def getLocal(self):
        returnValue = libpanda._inPMAKPGt_1(self.this)
        return returnValue

    
    def setLocal(self, local):
        returnValue = libpanda._inPMAKP9DMm(self.this, local)
        return returnValue

    
    def getTwoside(self):
        returnValue = libpanda._inPMAKPJTRL(self.this)
        return returnValue

    
    def setTwoside(self, twoside):
        returnValue = libpanda._inPMAKP06bF(self.this, twoside)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPMAKPNdw5(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPMAKPvnf5(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPMAKPwWha(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpanda._inPMAKPlFQk(self.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPMAKPhHq5(self.this, out.this)
        return returnValue

    
    def write(self, out, indent):
        returnValue = libpanda._inPMAKPO3W7(self.this, out.this, indent)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Material__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._Material__overloaded_constructor_ptrConstMaterial(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


