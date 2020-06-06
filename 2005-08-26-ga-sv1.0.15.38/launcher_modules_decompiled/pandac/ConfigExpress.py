# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class ConfigExpress(FFIExternalObject.FFIExternalObject):
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
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxt3IYn:
            libpandaexpress._inPKoxt3IYn(self.this)
        

    
    def _ConfigExpress__overloaded_GetBool_atomicstring_bool(sym, _def):
        returnValue = libpandaexpress._inPKoxt9Nre(sym, _def)
        return returnValue

    _ConfigExpress__overloaded_GetBool_atomicstring_bool = staticmethod(_ConfigExpress__overloaded_GetBool_atomicstring_bool)
    
    def _ConfigExpress__overloaded_GetBool_atomicstring(sym):
        returnValue = libpandaexpress._inPKoxtI2PZ(sym)
        return returnValue

    _ConfigExpress__overloaded_GetBool_atomicstring = staticmethod(_ConfigExpress__overloaded_GetBool_atomicstring)
    
    def _ConfigExpress__overloaded_GetInt_atomicstring_int(sym, _def):
        returnValue = libpandaexpress._inPKoxtCvWF(sym, _def)
        return returnValue

    _ConfigExpress__overloaded_GetInt_atomicstring_int = staticmethod(_ConfigExpress__overloaded_GetInt_atomicstring_int)
    
    def _ConfigExpress__overloaded_GetInt_atomicstring(sym):
        returnValue = libpandaexpress._inPKoxtR2ZD(sym)
        return returnValue

    _ConfigExpress__overloaded_GetInt_atomicstring = staticmethod(_ConfigExpress__overloaded_GetInt_atomicstring)
    
    def _ConfigExpress__overloaded_GetFloat_atomicstring_float(sym, _def):
        returnValue = libpandaexpress._inPKoxt4GUj(sym, _def)
        return returnValue

    _ConfigExpress__overloaded_GetFloat_atomicstring_float = staticmethod(_ConfigExpress__overloaded_GetFloat_atomicstring_float)
    
    def _ConfigExpress__overloaded_GetFloat_atomicstring(sym):
        returnValue = libpandaexpress._inPKoxtzb6c(sym)
        return returnValue

    _ConfigExpress__overloaded_GetFloat_atomicstring = staticmethod(_ConfigExpress__overloaded_GetFloat_atomicstring)
    
    def _ConfigExpress__overloaded_GetDouble_atomicstring_double(sym, _def):
        returnValue = libpandaexpress._inPKoxtYb57(sym, _def)
        return returnValue

    _ConfigExpress__overloaded_GetDouble_atomicstring_double = staticmethod(_ConfigExpress__overloaded_GetDouble_atomicstring_double)
    
    def _ConfigExpress__overloaded_GetDouble_atomicstring(sym):
        returnValue = libpandaexpress._inPKoxtrfMQ(sym)
        return returnValue

    _ConfigExpress__overloaded_GetDouble_atomicstring = staticmethod(_ConfigExpress__overloaded_GetDouble_atomicstring)
    
    def _ConfigExpress__overloaded_GetString_atomicstring_atomicstring(sym, _def):
        returnValue = libpandaexpress._inPKoxtQcsP(sym, _def)
        return returnValue

    _ConfigExpress__overloaded_GetString_atomicstring_atomicstring = staticmethod(_ConfigExpress__overloaded_GetString_atomicstring_atomicstring)
    
    def _ConfigExpress__overloaded_GetString_atomicstring(sym):
        returnValue = libpandaexpress._inPKoxt2SjW(sym)
        return returnValue

    _ConfigExpress__overloaded_GetString_atomicstring = staticmethod(_ConfigExpress__overloaded_GetString_atomicstring)
    
    def GetInt(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return ConfigExpress._ConfigExpress__overloaded_GetInt_atomicstring(*_args)
        elif numArgs == 2:
            return ConfigExpress._ConfigExpress__overloaded_GetInt_atomicstring_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    GetInt = staticmethod(GetInt)
    
    def GetFloat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return ConfigExpress._ConfigExpress__overloaded_GetFloat_atomicstring(*_args)
        elif numArgs == 2:
            return ConfigExpress._ConfigExpress__overloaded_GetFloat_atomicstring_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    GetFloat = staticmethod(GetFloat)
    
    def GetBool(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return ConfigExpress._ConfigExpress__overloaded_GetBool_atomicstring(*_args)
        elif numArgs == 2:
            return ConfigExpress._ConfigExpress__overloaded_GetBool_atomicstring_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    GetBool = staticmethod(GetBool)
    
    def GetDouble(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return ConfigExpress._ConfigExpress__overloaded_GetDouble_atomicstring(*_args)
        elif numArgs == 2:
            return ConfigExpress._ConfigExpress__overloaded_GetDouble_atomicstring_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    GetDouble = staticmethod(GetDouble)
    
    def GetString(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return ConfigExpress._ConfigExpress__overloaded_GetString_atomicstring(*_args)
        elif numArgs == 2:
            return ConfigExpress._ConfigExpress__overloaded_GetString_atomicstring_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    GetString = staticmethod(GetString)

