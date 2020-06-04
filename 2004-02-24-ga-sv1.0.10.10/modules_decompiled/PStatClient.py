# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class PStatClient(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
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
        if libpanda and libpanda._inPiqKx_6DX:
            libpanda._inPiqKx_6DX(self.this)
        

    
    def _PStatClient__overloaded_connect_atomicstring_int(parameter0, parameter1):
        returnValue = libpanda._inPiqKxcCtG(parameter0, parameter1)
        return returnValue

    _PStatClient__overloaded_connect_atomicstring_int = staticmethod(_PStatClient__overloaded_connect_atomicstring_int)
    
    def _PStatClient__overloaded_connect_atomicstring(parameter0):
        returnValue = libpanda._inPiqKxKb_Y(parameter0)
        return returnValue

    _PStatClient__overloaded_connect_atomicstring = staticmethod(_PStatClient__overloaded_connect_atomicstring)
    
    def _PStatClient__overloaded_connect():
        returnValue = libpanda._inPiqKxcnwA()
        return returnValue

    _PStatClient__overloaded_connect = staticmethod(_PStatClient__overloaded_connect)
    
    def disconnect():
        returnValue = libpanda._inPiqKxGM4i()
        return returnValue

    disconnect = staticmethod(disconnect)
    
    def isConnected():
        returnValue = libpanda._inPiqKxnHkh()
        return returnValue

    isConnected = staticmethod(isConnected)
    
    def resumeAfterPause():
        returnValue = libpanda._inPiqKx8MTf()
        return returnValue

    resumeAfterPause = staticmethod(resumeAfterPause)
    
    def connect(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return PStatClient._PStatClient__overloaded_connect()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return PStatClient._PStatClient__overloaded_connect_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return PStatClient._PStatClient__overloaded_connect_atomicstring_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    connect = staticmethod(connect)

