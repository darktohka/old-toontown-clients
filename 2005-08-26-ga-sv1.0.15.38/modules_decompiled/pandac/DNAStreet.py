# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DNANode

class DNAStreet(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNAStreet__overloaded_constructor_ptrConstDNAStreet(self, street):
        self.this = libtoontown._inPdt4yOIML(street.this)
        self.userManagesMemory = 1

    
    def _DNAStreet__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPdt4y_FMW(initialName)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yuiq2:
            libtoontown._inPdt4yuiq2(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPdt4yWNtw()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCode(self, code):
        returnValue = libtoontown._inPdt4ySmTO(self.this, code)
        return returnValue

    
    def getCode(self):
        returnValue = libtoontown._inPdt4yEQjL(self.this)
        return returnValue

    
    def setStreetTexture(self, streetTexture):
        returnValue = libtoontown._inPdt4yGReL(self.this, streetTexture)
        return returnValue

    
    def getStreetTexture(self):
        returnValue = libtoontown._inPdt4yzYQY(self.this)
        return returnValue

    
    def setSidewalkTexture(self, sidewalkTexture):
        returnValue = libtoontown._inPdt4yh0_l(self.this, sidewalkTexture)
        return returnValue

    
    def getSidewalkTexture(self):
        returnValue = libtoontown._inPdt4ykRke(self.this)
        return returnValue

    
    def setCurbTexture(self, curbTexture):
        returnValue = libtoontown._inPdt4yMv8z(self.this, curbTexture)
        return returnValue

    
    def getCurbTexture(self):
        returnValue = libtoontown._inPdt4ykZkz(self.this)
        return returnValue

    
    def setStreetColor(self, color):
        returnValue = libtoontown._inPdt4ys3vt(self.this, color.this)
        return returnValue

    
    def getStreetColor(self):
        returnValue = libtoontown._inPdt4yxIQg(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setSidewalkColor(self, color):
        returnValue = libtoontown._inPdt4yKrjL(self.this, color.this)
        return returnValue

    
    def getSidewalkColor(self):
        returnValue = libtoontown._inPdt4ymnCn(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCurbColor(self, color):
        returnValue = libtoontown._inPdt4y_ayL(self.this, color.this)
        return returnValue

    
    def getCurbColor(self):
        returnValue = libtoontown._inPdt4yD3B7(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNAStreet__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DNAStreet):
                return self._DNAStreet__overloaded_constructor_ptrConstDNAStreet(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAStreet> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


