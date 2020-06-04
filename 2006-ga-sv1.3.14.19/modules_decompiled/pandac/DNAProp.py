# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DNANode

class DNAProp(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNAProp__overloaded_constructor_ptrConstDNAProp(self, prop):
        self.this = libtoontown._inPdt4yoaqd(prop.this)
        self.userManagesMemory = 1

    
    def _DNAProp__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPdt4yaXqa(initialName)
        self.userManagesMemory = 1

    
    def _DNAProp__overloaded_constructor(self):
        self.this = libtoontown._inPdt4yzpQW()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yoE3M:
            libtoontown._inPdt4yoE3M(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4yXJUZ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPdt4ydY51(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPdt4yYDIt(self.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libtoontown._inPdt4yWUox(self.this, color.this)
        return returnValue

    
    def getColor(self):
        returnValue = libtoontown._inPdt4yFxCQ(self.this)
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
            return self._DNAProp__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNAProp__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DNAProp):
                return self._DNAProp__overloaded_constructor_ptrConstDNAProp(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAProp> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


