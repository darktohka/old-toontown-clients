# File: M (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Ostream

class MultiplexStream(Ostream.Ostream, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpandaexpress._inP2KOdYfxv()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdlnO7:
            libpandaexpress._inP2KOdlnO7(self.this)
        

    
    def _MultiplexStream__overloaded_addOstream_ptrMultiplexStream_ptrOstream_bool(self, out, deleteLater):
        returnValue = libpandaexpress._inP2KOdWXC6(self.this, out.this, deleteLater)
        return returnValue

    
    def _MultiplexStream__overloaded_addOstream_ptrMultiplexStream_ptrOstream(self, out):
        returnValue = libpandaexpress._inP2KOdaq5z(self.this, out.this)
        return returnValue

    
    def addStdioFile(self, file, closeWhenDone):
        returnValue = libpandaexpress._inP2KOdGGvk(self.this, file.this, closeWhenDone)
        return returnValue

    
    def addStandardOutput(self):
        returnValue = libpandaexpress._inP2KOdl5Dq(self.this)
        return returnValue

    
    def addFile(self, file):
        returnValue = libpandaexpress._inP2KOdrLNF(self.this, file.this)
        return returnValue

    
    def addSystemDebug(self):
        returnValue = libpandaexpress._inP2KOdJUTf(self.this)
        return returnValue

    
    def flush(self):
        returnValue = libpandaexpress._inP2KOdKH3n(self.this)
        return returnValue

    
    def addOstream(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._MultiplexStream__overloaded_addOstream_ptrMultiplexStream_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._MultiplexStream__overloaded_addOstream_ptrMultiplexStream_ptrOstream_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


