# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
from direct.ffi import FFIExternalObject

class EggRenderMode(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts]
    AMBinary = 7
    AMUnspecified = 0
    AMBlendNoOcclude = 4
    AMOn = 2
    AMMsMask = 6
    AMOff = 1
    AMBlend = 3
    AMMs = 5
    AMDual = 8
    DWMOn = 2
    DWMOff = 1
    DWMUnspecified = 0
    DTMUnspecified = 0
    DTMOff = 1
    DTMOn = 2
    VMUnspecified = 0
    VMHidden = 1
    VMNormal = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggRenderMode__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMTDmL()
        self.userManagesMemory = 1

    
    def _EggRenderMode__overloaded_constructor_ptrConstEggRenderMode(self, copy):
        self.this = libpandaegg._inPkAOMD72v(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMNIlB:
            libpandaegg._inPkAOMNIlB(self.this)
        

    
    def stringAlphaMode(cString):
        returnValue = libpandaegg._inPkAOMX3lo(cString)
        return returnValue

    stringAlphaMode = staticmethod(stringAlphaMode)
    
    def stringDepthWriteMode(cString):
        returnValue = libpandaegg._inPkAOMj8l7(cString)
        return returnValue

    stringDepthWriteMode = staticmethod(stringDepthWriteMode)
    
    def stringDepthTestMode(cString):
        returnValue = libpandaegg._inPkAOMecqF(cString)
        return returnValue

    stringDepthTestMode = staticmethod(stringDepthTestMode)
    
    def stringVisibilityMode(cString):
        returnValue = libpandaegg._inPkAOMMsGH(cString)
        return returnValue

    stringVisibilityMode = staticmethod(stringVisibilityMode)
    
    def getClassType():
        returnValue = libpandaegg._inPkAOMYBRs()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMr5z0(self.this, copy.this)
        returnObject = EggRenderMode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def write(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMtH5E(self.this, out.this, indentLevel)
        return returnValue

    
    def setAlphaMode(self, mode):
        returnValue = libpandaegg._inPkAOM7kse(self.this, mode)
        return returnValue

    
    def getAlphaMode(self):
        returnValue = libpandaegg._inPkAOM3t3A(self.this)
        return returnValue

    
    def setDepthWriteMode(self, mode):
        returnValue = libpandaegg._inPkAOMCEUa(self.this, mode)
        return returnValue

    
    def getDepthWriteMode(self):
        returnValue = libpandaegg._inPkAOMaHHZ(self.this)
        return returnValue

    
    def setDepthTestMode(self, mode):
        returnValue = libpandaegg._inPkAOMOa7S(self.this, mode)
        return returnValue

    
    def getDepthTestMode(self):
        returnValue = libpandaegg._inPkAOMkkuX(self.this)
        return returnValue

    
    def setVisibilityMode(self, mode):
        returnValue = libpandaegg._inPkAOMreNq(self.this, mode)
        return returnValue

    
    def getVisibilityMode(self):
        returnValue = libpandaegg._inPkAOMta47(self.this)
        return returnValue

    
    def setDrawOrder(self, order):
        returnValue = libpandaegg._inPkAOM1SSq(self.this, order)
        return returnValue

    
    def getDrawOrder(self):
        returnValue = libpandaegg._inPkAOMY4RM(self.this)
        return returnValue

    
    def hasDrawOrder(self):
        returnValue = libpandaegg._inPkAOMV5rc(self.this)
        return returnValue

    
    def clearDrawOrder(self):
        returnValue = libpandaegg._inPkAOMgDCN(self.this)
        return returnValue

    
    def setBin(self, bin):
        returnValue = libpandaegg._inPkAOMOpBx(self.this, bin)
        return returnValue

    
    def getBin(self):
        returnValue = libpandaegg._inPkAOMtssd(self.this)
        return returnValue

    
    def hasBin(self):
        returnValue = libpandaegg._inPkAOM6rGu(self.this)
        return returnValue

    
    def clearBin(self):
        returnValue = libpandaegg._inPkAOMlrzU(self.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpandaegg._inPkAOMpyzm(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaegg._inPkAOMV_Rm(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaegg._inPkAOMT1ZU(self.this, other.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggRenderMode__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._EggRenderMode__overloaded_constructor_ptrConstEggRenderMode(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


