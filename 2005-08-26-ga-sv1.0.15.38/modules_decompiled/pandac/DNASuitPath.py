# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class DNASuitPath(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNASuitPath__overloaded_constructor(self):
        self.this = libtoontown._inPdt4yvZAe()
        self.userManagesMemory = 1

    
    def _DNASuitPath__overloaded_constructor_ptrConstDNASuitPath(self, path):
        self.this = libtoontown._inPdt4y7m9i(path.this)
        self.userManagesMemory = 1

    
    def _DNASuitPath__overloaded_constructor_int(self, reserveLength):
        self.this = libtoontown._inPdt4ydMnK(reserveLength)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4y2tdl:
            libtoontown._inPdt4y2tdl(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4yjaRl()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getNumPoints(self):
        returnValue = libtoontown._inPdt4ysfvS(self.this)
        return returnValue

    
    def copy(self, path):
        returnValue = libtoontown._inPdt4yhz46(self.this, path.this)
        return returnValue

    
    def getPointIndex(self, i):
        returnValue = libtoontown._inPdt4yzh4X(self.this, i)
        return returnValue

    
    def output(self, out):
        returnValue = libtoontown._inPdt4yOK18(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNASuitPath__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._DNASuitPath__overloaded_constructor_int(*_args)
            
            if isinstance(_args[0], DNASuitPath):
                return self._DNASuitPath__overloaded_constructor_ptrConstDNASuitPath(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <DNASuitPath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


