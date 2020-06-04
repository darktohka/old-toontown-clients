# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import FFIExternalObject

class DCFile(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libdirect._inP5HfQM0cB()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inP5HfQpmvv:
            libdirect._inP5HfQpmvv(self.this)
        

    
    def _DCFile__overloaded_read_ptrDCFile_ptrFilename(self, filename):
        returnValue = libdirect._inP5HfQEDwK(self.this, filename.this)
        return returnValue

    
    def _DCFile__overloaded_read_ptrDCFile_ptrIstream_atomicstring(self, _in, filename):
        returnValue = libdirect._inP5HfQRI_H(self.this, _in.this, filename)
        return returnValue

    
    def _DCFile__overloaded_read_ptrDCFile_ptrIstream(self, _in):
        returnValue = libdirect._inP5HfQsrn_(self.this, _in.this)
        return returnValue

    
    def _DCFile__overloaded_write_ptrConstDCFile_ptrFilename_bool(self, filename, brief):
        returnValue = libdirect._inP5HfQIISH(self.this, filename.this, brief)
        return returnValue

    
    def _DCFile__overloaded_write_ptrConstDCFile_ptrOstream_bool(self, out, brief):
        returnValue = libdirect._inP5HfQ4v0f(self.this, out.this, brief)
        return returnValue

    
    def getNumClasses(self):
        returnValue = libdirect._inP5HfQjNAi(self.this)
        return returnValue

    
    def getClass(self, n):
        returnValue = libdirect._inP5HfQgF38(self.this, n)
        import DCClass
        returnObject = DCClass.DCClass(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getClassByName(self, name):
        returnValue = libdirect._inP5HfQ0NPb(self.this, name)
        import DCClass
        returnObject = DCClass.DCClass(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getHash(self):
        returnValue = libdirect._inP5HfQXMzc(self.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import Ostream
            import Filename
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._DCFile__overloaded_write_ptrConstDCFile_ptrOstream_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            elif isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._DCFile__overloaded_write_ptrConstDCFile_ptrFilename_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def read(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Istream
            import Filename
            if isinstance(_args[0], Istream.Istream):
                return self._DCFile__overloaded_read_ptrDCFile_ptrIstream(_args[0])
            elif isinstance(_args[0], Filename.Filename):
                return self._DCFile__overloaded_read_ptrDCFile_ptrFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
        elif numArgs == 2:
            import Istream
            if isinstance(_args[0], Istream.Istream):
                if isinstance(_args[1], types.StringType):
                    return self._DCFile__overloaded_read_ptrDCFile_ptrIstream_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


