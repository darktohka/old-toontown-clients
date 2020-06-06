# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DNAGroup

class DNAWindows(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNAWindows__overloaded_constructor_ptrConstDNAWindows(self, window):
        self.this = libtoontown._inPdt4y_7zm(window.this)
        self.userManagesMemory = 1

    
    def _DNAWindows__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPdt4yyGfX(initialName)
        self.userManagesMemory = 1

    
    def _DNAWindows__overloaded_constructor(self):
        self.this = libtoontown._inPdt4ymEp4()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yyy0V:
            libtoontown._inPdt4yyy0V(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4yhbQb()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPdt4yGboO(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPdt4ylHl1(self.this)
        return returnValue

    
    def setWindowCount(self, count):
        returnValue = libtoontown._inPdt4y5sAX(self.this, count)
        return returnValue

    
    def getWindowCount(self):
        returnValue = libtoontown._inPdt4yLEzi(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPdt4yPZaL(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPdt4ybJYq(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNAWindows__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNAWindows__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DNAWindows):
                return self._DNAWindows__overloaded_constructor_ptrConstDNAWindows(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAWindows> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


