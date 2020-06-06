# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ConfigVariable

class ConfigVariableDouble(ConfigVariable.ConfigVariable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ConfigVariableDouble__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaexpress._inPKoxtCK_u(name)
        self.userManagesMemory = 1

    
    def _ConfigVariableDouble__overloaded_constructor_atomicstring_atomicstring_atomicstring_int(self, name, defaultValue, description, flags):
        self.this = libpandaexpress._inPKoxtVT_M(name, defaultValue, description, flags)
        self.userManagesMemory = 1

    
    def _ConfigVariableDouble__overloaded_constructor_atomicstring_atomicstring_atomicstring(self, name, defaultValue, description):
        self.this = libpandaexpress._inPKoxtcCSY(name, defaultValue, description)
        self.userManagesMemory = 1

    
    def _ConfigVariableDouble__overloaded_constructor_atomicstring_atomicstring(self, name, defaultValue):
        self.this = libpandaexpress._inPKoxtEDCV(name, defaultValue)
        self.userManagesMemory = 1

    
    def _ConfigVariableDouble__overloaded_constructor_atomicstring_double_atomicstring_int(self, name, defaultValue, description, flags):
        self.this = libpandaexpress._inPKoxtAhLa(name, defaultValue, description, flags)
        self.userManagesMemory = 1

    
    def _ConfigVariableDouble__overloaded_constructor_atomicstring_double_atomicstring(self, name, defaultValue, description):
        self.this = libpandaexpress._inPKoxtWBUH(name, defaultValue, description)
        self.userManagesMemory = 1

    
    def _ConfigVariableDouble__overloaded_constructor_atomicstring_double(self, name, defaultValue):
        self.this = libpandaexpress._inPKoxtYBO6(name, defaultValue)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtObmc:
            libpandaexpress._inPKoxtObmc(self.this)
        

    
    def assign(self, value):
        returnValue = libpandaexpress._inPKoxt9oaH(self.this, value)
        returnObject = ConfigVariableDouble(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def size(self):
        returnValue = libpandaexpress._inPKoxtiiNw(self.this)
        return returnValue

    
    def __getitem__(self, n):
        returnValue = libpandaexpress._inPKoxtLoN2(self.this, n)
        return returnValue

    
    def setValue(self, value):
        returnValue = libpandaexpress._inPKoxtjhoa(self.this, value)
        return returnValue

    
    def getValue(self):
        returnValue = libpandaexpress._inPKoxtbA6h(self.this)
        return returnValue

    
    def getDefaultValue(self):
        returnValue = libpandaexpress._inPKoxtFMO4(self.this)
        return returnValue

    
    def getWord(self, n):
        returnValue = libpandaexpress._inPKoxtHfdb(self.this, n)
        return returnValue

    
    def setWord(self, n, value):
        returnValue = libpandaexpress._inPKoxtTUh2(self.this, n, value)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ConfigVariableDouble__overloaded_constructor_atomicstring(*_args)
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.FloatType) and isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return self._ConfigVariableDouble__overloaded_constructor_atomicstring_double(*_args)
                
                if isinstance(_args[1], types.StringType):
                    return self._ConfigVariableDouble__overloaded_constructor_atomicstring_atomicstring(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> <types.StringType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.FloatType) and isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return self._ConfigVariableDouble__overloaded_constructor_atomicstring_double_atomicstring(*_args)
                
                if isinstance(_args[1], types.StringType):
                    return self._ConfigVariableDouble__overloaded_constructor_atomicstring_atomicstring_atomicstring(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> <types.StringType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.FloatType) and isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return self._ConfigVariableDouble__overloaded_constructor_atomicstring_double_atomicstring_int(*_args)
                
                if isinstance(_args[1], types.StringType):
                    return self._ConfigVariableDouble__overloaded_constructor_atomicstring_atomicstring_atomicstring_int(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> <types.StringType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def __getitem__(self, n):
        if n < 0 or n >= self.getNumWords():
            raise IndexError
        
        return self.getWord(n)


