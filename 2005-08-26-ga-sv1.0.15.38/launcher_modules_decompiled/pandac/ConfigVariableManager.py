# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class ConfigVariableManager(FFIExternalObject.FFIExternalObject):
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
        

    
    def getGlobalPtr():
        returnValue = libpandaexpress._inPKoxtBx3a()
        returnObject = ConfigVariableManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalPtr = staticmethod(getGlobalPtr)
    
    def makeVariable(self, name):
        returnValue = libpandaexpress._inPKoxtbUoR(self.this, name)
        import ConfigVariableCore
        returnObject = ConfigVariableCore.ConfigVariableCore(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _ConfigVariableManager__overloaded_makeVariableTemplate_ptrConfigVariableManager_atomicstring___enum__ValueType_atomicstring_atomicstring_int(self, pattern, type, defaultValue, description, flags):
        returnValue = libpandaexpress._inPKoxtICHW(self.this, pattern, type, defaultValue, description, flags)
        import ConfigVariableCore
        returnObject = ConfigVariableCore.ConfigVariableCore(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _ConfigVariableManager__overloaded_makeVariableTemplate_ptrConfigVariableManager_atomicstring___enum__ValueType_atomicstring_atomicstring(self, pattern, type, defaultValue, description):
        returnValue = libpandaexpress._inPKoxtv8JU(self.this, pattern, type, defaultValue, description)
        import ConfigVariableCore
        returnObject = ConfigVariableCore.ConfigVariableCore(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _ConfigVariableManager__overloaded_makeVariableTemplate_ptrConfigVariableManager_atomicstring___enum__ValueType_atomicstring(self, pattern, type, defaultValue):
        returnValue = libpandaexpress._inPKoxtfBGQ(self.this, pattern, type, defaultValue)
        import ConfigVariableCore
        returnObject = ConfigVariableCore.ConfigVariableCore(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumVariables(self):
        returnValue = libpandaexpress._inPKoxtvzyQ(self.this)
        return returnValue

    
    def getVariable(self, n):
        returnValue = libpandaexpress._inPKoxt2qFF(self.this, n)
        import ConfigVariableCore
        returnObject = ConfigVariableCore.ConfigVariableCore(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getVariableName(self, n):
        returnValue = libpandaexpress._inPKoxtuDAj(self.this, n)
        return returnValue

    
    def isVariableUsed(self, n):
        returnValue = libpandaexpress._inPKoxtp8_h(self.this, n)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtfFtp(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpandaexpress._inPKoxtH7se(self.this, out.this)
        return returnValue

    
    def listUnusedVariables(self):
        returnValue = libpandaexpress._inPKoxtKzQG(self.this)
        return returnValue

    
    def listVariables(self):
        returnValue = libpandaexpress._inPKoxtngxf(self.this)
        return returnValue

    
    def listDynamicVariables(self):
        returnValue = libpandaexpress._inPKoxt0fM_(self.this)
        return returnValue

    
    def makeVariableTemplate(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            return self._ConfigVariableManager__overloaded_makeVariableTemplate_ptrConfigVariableManager_atomicstring___enum__ValueType_atomicstring(*_args)
        elif numArgs == 4:
            return self._ConfigVariableManager__overloaded_makeVariableTemplate_ptrConfigVariableManager_atomicstring___enum__ValueType_atomicstring_atomicstring(*_args)
        elif numArgs == 5:
            return self._ConfigVariableManager__overloaded_makeVariableTemplate_ptrConfigVariableManager_atomicstring___enum__ValueType_atomicstring_atomicstring_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 5 '


