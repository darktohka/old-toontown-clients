# File: I (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Istream
import Ostream

class Iostream(Istream.Istream, Ostream.Ostream, FFIExternalObject.FFIExternalObject):
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
        if libpandaexpress and libpandaexpress._inPKoxtgjiM:
            libpandaexpress._inPKoxtgjiM(self.this)
        

    
    def flush(self):
        returnValue = libpandaexpress._inPKoxtrDS9(self.this)
        return returnValue

    
    def upcastToOstream(self):
        returnValue = libpandaexpress._inPKoxt7W6h(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def get(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt4uln(upcastSelf.this)
        return returnValue

    
    def put(self, c):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToOstream()
        returnValue = libpandaexpress._inPKoxtiovs(upcastSelf.this, c)
        return returnValue


