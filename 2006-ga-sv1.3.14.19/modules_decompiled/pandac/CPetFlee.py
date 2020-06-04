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

class CPetFlee(CImpulse.CImpulse, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libotpDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CPetFlee__overloaded_constructor_ptrNodePath_float_float(self, chaser, maxDist, moveAngle):
        self.this = libtoontown._inPWst6jt8E(chaser.this, maxDist, moveAngle)
        self.userManagesMemory = 1

    
    def _CPetFlee__overloaded_constructor_ptrNodePath_float(self, chaser, maxDist):
        self.this = libtoontown._inPWst6_ZKe(chaser.this, maxDist)
        self.userManagesMemory = 1

    
    def _CPetFlee__overloaded_constructor_ptrNodePath(self, chaser):
        self.this = libtoontown._inPWst6SUJ9(chaser.this)
        self.userManagesMemory = 1

    
    def _CPetFlee__overloaded_constructor(self):
        self.this = libtoontown._inPWst6DOPZ()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libtoontown._inPWst6PvOg()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setChaser(self, chaser):
        returnValue = libtoontown._inPWst6tL1S(self.this, chaser.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CPetFlee__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._CPetFlee__overloaded_constructor_ptrNodePath(*_args)
        elif numArgs == 2:
            return self._CPetFlee__overloaded_constructor_ptrNodePath_float(*_args)
        elif numArgs == 3:
            return self._CPetFlee__overloaded_constructor_ptrNodePath_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '


