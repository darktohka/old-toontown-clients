# File: M (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Ostream

class MultiplexStream(Ostream.Ostream, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaexpress._inP2KOdZfxv()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdknO7:
            libpandaexpress._inP2KOdknO7(self.this)
        

    
    def _MultiplexStream__overloaded_addOstream_ptrMultiplexStream_ptrOstream_bool(self, out, deleteLater):
        returnValue = libpandaexpress._inP2KOdZXC6(self.this, out.this, deleteLater)
        return returnValue

    
    def _MultiplexStream__overloaded_addOstream_ptrMultiplexStream_ptrOstream(self, out):
        returnValue = libpandaexpress._inP2KOddq5z(self.this, out.this)
        return returnValue

    
    def addStdioFile(self, file, closeWhenDone):
        returnValue = libpandaexpress._inP2KOdFGvk(self.this, file.this, closeWhenDone)
        return returnValue

    
    def addStandardOutput(self):
        returnValue = libpandaexpress._inP2KOdk5Dq(self.this)
        return returnValue

    
    def addFile(self, file):
        returnValue = libpandaexpress._inP2KOdrLNF(self.this, file.this)
        return returnValue

    
    def addSystemDebug(self):
        returnValue = libpandaexpress._inP2KOdJUTf(self.this)
        return returnValue

    
    def flush(self):
        returnValue = libpandaexpress._inP2KOdJH3n(self.this)
        return returnValue

    
    def addOstream(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._MultiplexStream__overloaded_addOstream_ptrMultiplexStream_ptrOstream(*_args)
        elif numArgs == 2:
            return self._MultiplexStream__overloaded_addOstream_ptrMultiplexStream_ptrOstream_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


