# File: C (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import FFIExternalObject

class ConfigConfigureGetConfigConfigShowbase(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inPL4GTSvPT:
            libdirect._inPL4GTSvPT(self.this)
        

    
    def _ConfigConfigureGetConfigConfigShowbase__overloaded_GetBool_atomicstring_bool(sym, _def):
        returnValue = libdirect._inPL4GTpkh_(sym, _def)
        return returnValue

    _ConfigConfigureGetConfigConfigShowbase__overloaded_GetBool_atomicstring_bool = staticmethod(_ConfigConfigureGetConfigConfigShowbase__overloaded_GetBool_atomicstring_bool)
    
    def _ConfigConfigureGetConfigConfigShowbase__overloaded_GetBool_atomicstring(sym):
        returnValue = libdirect._inPL4GTFBgQ(sym)
        return returnValue

    _ConfigConfigureGetConfigConfigShowbase__overloaded_GetBool_atomicstring = staticmethod(_ConfigConfigureGetConfigConfigShowbase__overloaded_GetBool_atomicstring)
    
    def _ConfigConfigureGetConfigConfigShowbase__overloaded_GetInt_atomicstring_int(sym, _def):
        returnValue = libdirect._inPL4GTvpTV(sym, _def)
        return returnValue

    _ConfigConfigureGetConfigConfigShowbase__overloaded_GetInt_atomicstring_int = staticmethod(_ConfigConfigureGetConfigConfigShowbase__overloaded_GetInt_atomicstring_int)
    
    def _ConfigConfigureGetConfigConfigShowbase__overloaded_GetInt_atomicstring(sym):
        returnValue = libdirect._inPL4GTO3AW(sym)
        return returnValue

    _ConfigConfigureGetConfigConfigShowbase__overloaded_GetInt_atomicstring = staticmethod(_ConfigConfigureGetConfigConfigShowbase__overloaded_GetInt_atomicstring)
    
    def _ConfigConfigureGetConfigConfigShowbase__overloaded_GetFloat_atomicstring_float(sym, _def):
        returnValue = libdirect._inPL4GTMv9T(sym, _def)
        return returnValue

    _ConfigConfigureGetConfigConfigShowbase__overloaded_GetFloat_atomicstring_float = staticmethod(_ConfigConfigureGetConfigConfigShowbase__overloaded_GetFloat_atomicstring_float)
    
    def _ConfigConfigureGetConfigConfigShowbase__overloaded_GetFloat_atomicstring(sym):
        returnValue = libdirect._inPL4GTK7VG(sym)
        return returnValue

    _ConfigConfigureGetConfigConfigShowbase__overloaded_GetFloat_atomicstring = staticmethod(_ConfigConfigureGetConfigConfigShowbase__overloaded_GetFloat_atomicstring)
    
    def _ConfigConfigureGetConfigConfigShowbase__overloaded_GetDouble_atomicstring_double(sym, _def):
        returnValue = libdirect._inPL4GTGCam(sym, _def)
        return returnValue

    _ConfigConfigureGetConfigConfigShowbase__overloaded_GetDouble_atomicstring_double = staticmethod(_ConfigConfigureGetConfigConfigShowbase__overloaded_GetDouble_atomicstring_double)
    
    def _ConfigConfigureGetConfigConfigShowbase__overloaded_GetDouble_atomicstring(sym):
        returnValue = libdirect._inPL4GT_PRv(sym)
        return returnValue

    _ConfigConfigureGetConfigConfigShowbase__overloaded_GetDouble_atomicstring = staticmethod(_ConfigConfigureGetConfigConfigShowbase__overloaded_GetDouble_atomicstring)
    
    def _ConfigConfigureGetConfigConfigShowbase__overloaded_GetString_atomicstring_atomicstring(sym, _def):
        returnValue = libdirect._inPL4GTjFEi(sym, _def)
        return returnValue

    _ConfigConfigureGetConfigConfigShowbase__overloaded_GetString_atomicstring_atomicstring = staticmethod(_ConfigConfigureGetConfigConfigShowbase__overloaded_GetString_atomicstring_atomicstring)
    
    def _ConfigConfigureGetConfigConfigShowbase__overloaded_GetString_atomicstring(sym):
        returnValue = libdirect._inPL4GTz6I6(sym)
        return returnValue

    _ConfigConfigureGetConfigConfigShowbase__overloaded_GetString_atomicstring = staticmethod(_ConfigConfigureGetConfigConfigShowbase__overloaded_GetString_atomicstring)
    
    def GetInt(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return ConfigConfigureGetConfigConfigShowbase._ConfigConfigureGetConfigConfigShowbase__overloaded_GetInt_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return ConfigConfigureGetConfigConfigShowbase._ConfigConfigureGetConfigConfigShowbase__overloaded_GetInt_atomicstring_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    GetInt = staticmethod(GetInt)
    
    def GetFloat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return ConfigConfigureGetConfigConfigShowbase._ConfigConfigureGetConfigConfigShowbase__overloaded_GetFloat_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return ConfigConfigureGetConfigConfigShowbase._ConfigConfigureGetConfigConfigShowbase__overloaded_GetFloat_atomicstring_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    GetFloat = staticmethod(GetFloat)
    
    def GetBool(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return ConfigConfigureGetConfigConfigShowbase._ConfigConfigureGetConfigConfigShowbase__overloaded_GetBool_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return ConfigConfigureGetConfigConfigShowbase._ConfigConfigureGetConfigConfigShowbase__overloaded_GetBool_atomicstring_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    GetBool = staticmethod(GetBool)
    
    def GetDouble(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return ConfigConfigureGetConfigConfigShowbase._ConfigConfigureGetConfigConfigShowbase__overloaded_GetDouble_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return ConfigConfigureGetConfigConfigShowbase._ConfigConfigureGetConfigConfigShowbase__overloaded_GetDouble_atomicstring_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    GetDouble = staticmethod(GetDouble)
    
    def GetString(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return ConfigConfigureGetConfigConfigShowbase._ConfigConfigureGetConfigConfigShowbase__overloaded_GetString_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.StringType):
                    return ConfigConfigureGetConfigConfigShowbase._ConfigConfigureGetConfigConfigShowbase__overloaded_GetString_atomicstring_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    GetString = staticmethod(GetString)

