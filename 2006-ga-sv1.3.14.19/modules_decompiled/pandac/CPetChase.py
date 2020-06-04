# File: C (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libotp
import libotpDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CImpulse

class CPetChase(CImpulse.CImpulse, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libotpDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CPetChase__overloaded_constructor_ptrNodePath_float_float(self, target, minDist, moveAngle):
        self.this = libtoontown._inPWst68Ddg(target.this, minDist, moveAngle)
        self.userManagesMemory = 1

    
    def _CPetChase__overloaded_constructor_ptrNodePath_float(self, target, minDist):
        self.this = libtoontown._inPWst6GfWU(target.this, minDist)
        self.userManagesMemory = 1

    
    def _CPetChase__overloaded_constructor_ptrNodePath(self, target):
        self.this = libtoontown._inPWst6LE_g(target.this)
        self.userManagesMemory = 1

    
    def _CPetChase__overloaded_constructor(self):
        self.this = libtoontown._inPWst6bF3y()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libtoontown._inPWst65x_E()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setTarget(self, target):
        returnValue = libtoontown._inPWst6SKEc(self.this, target.this)
        return returnValue

    
    def getTarget(self):
        returnValue = libtoontown._inPWst6RLNO(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setMinDist(self, minDist):
        returnValue = libtoontown._inPWst6Cr69(self.this, minDist)
        return returnValue

    
    def getMinDist(self):
        returnValue = libtoontown._inPWst6ngYb(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CPetChase__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._CPetChase__overloaded_constructor_ptrNodePath(*_args)
        elif numArgs == 2:
            return self._CPetChase__overloaded_constructor_ptrNodePath_float(*_args)
        elif numArgs == 3:
            return self._CPetChase__overloaded_constructor_ptrNodePath_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '


