# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class ConfigPage(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
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
        

    
    def getDefaultPage():
        returnValue = libpandaexpress._inPKoxtPGVr()
        returnObject = ConfigPage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getDefaultPage = staticmethod(getDefaultPage)
    
    def getLocalPage():
        returnValue = libpandaexpress._inPKoxtL7Gu()
        returnObject = ConfigPage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getLocalPage = staticmethod(getLocalPage)
    
    def getName(self):
        returnValue = libpandaexpress._inPKoxtUNsX(self.this)
        return returnValue

    
    def isSpecial(self):
        returnValue = libpandaexpress._inPKoxtJyhA(self.this)
        return returnValue

    
    def isImplicit(self):
        returnValue = libpandaexpress._inPKoxteRrb(self.this)
        return returnValue

    
    def getPageSeq(self):
        returnValue = libpandaexpress._inPKoxtKe18(self.this)
        return returnValue

    
    def getTrustLevel(self):
        returnValue = libpandaexpress._inPKoxtK7vW(self.this)
        return returnValue

    
    def getSignature(self):
        returnValue = libpandaexpress._inPKoxtobQg(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpandaexpress._inPKoxtp8Hx(self.this)
        return returnValue

    
    def readPrc(self, _in):
        returnValue = libpandaexpress._inPKoxtX8QI(self.this, _in.this)
        return returnValue

    
    def _ConfigPage__overloaded_makeDeclaration_ptrConfigPage_ptrConfigVariableCore_atomicstring(self, variable, value):
        returnValue = libpandaexpress._inPKoxtbnS0(self.this, variable.this, value)
        import ConfigDeclaration
        returnObject = ConfigDeclaration.ConfigDeclaration(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _ConfigPage__overloaded_makeDeclaration_ptrConfigPage_atomicstring_atomicstring(self, variable, value):
        returnValue = libpandaexpress._inPKoxta0Ry(self.this, variable, value)
        import ConfigDeclaration
        returnObject = ConfigDeclaration.ConfigDeclaration(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def deleteDeclaration(self, decl):
        returnValue = libpandaexpress._inPKoxtUNQd(self.this, decl.this)
        return returnValue

    
    def getNumDeclarations(self):
        returnValue = libpandaexpress._inPKoxt4OlT(self.this)
        return returnValue

    
    def getDeclaration(self, n):
        returnValue = libpandaexpress._inPKoxtLiqb(self.this, n)
        import ConfigDeclaration
        returnObject = ConfigDeclaration.ConfigDeclaration(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVariableName(self, n):
        returnValue = libpandaexpress._inPKoxtvsYV(self.this, n)
        return returnValue

    
    def getStringValue(self, n):
        returnValue = libpandaexpress._inPKoxtTmDS(self.this, n)
        return returnValue

    
    def isVariableUsed(self, n):
        returnValue = libpandaexpress._inPKoxtt4Y8(self.this, n)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtouea(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpandaexpress._inPKoxtMy5p(self.this, out.this)
        return returnValue

    
    def makeDeclaration(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.StringType):
                return self._ConfigPage__overloaded_makeDeclaration_ptrConfigPage_atomicstring_atomicstring(*_args)
            
            import ConfigVariableCore
            if isinstance(_args[0], ConfigVariableCore.ConfigVariableCore):
                return self._ConfigPage__overloaded_makeDeclaration_ptrConfigPage_ptrConfigVariableCore_atomicstring(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <ConfigVariableCore.ConfigVariableCore> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


