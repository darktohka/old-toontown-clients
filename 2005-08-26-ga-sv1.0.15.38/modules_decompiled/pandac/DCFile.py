# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject

class DCFile(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libdirect._inP5HfQM0cB()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inP5HfQqmvv:
            libdirect._inP5HfQqmvv(self.this)
        

    
    def clear(self):
        returnValue = libdirect._inP5HfQ3Phn(self.this)
        return returnValue

    
    def readAll(self):
        returnValue = libdirect._inP5HfQcUOF(self.this)
        return returnValue

    
    def _DCFile__overloaded_read_ptrDCFile_ptrFilename(self, filename):
        returnValue = libdirect._inP5HfQEDwK(self.this, filename.this)
        return returnValue

    
    def _DCFile__overloaded_read_ptrDCFile_ptrIstream_atomicstring(self, _in, filename):
        returnValue = libdirect._inP5HfQRI_H(self.this, _in.this, filename)
        return returnValue

    
    def _DCFile__overloaded_read_ptrDCFile_ptrIstream(self, _in):
        returnValue = libdirect._inP5HfQtrn_(self.this, _in.this)
        return returnValue

    
    def _DCFile__overloaded_write_ptrConstDCFile_ptrFilename_bool(self, filename, brief):
        returnValue = libdirect._inP5HfQIISH(self.this, filename.this, brief)
        return returnValue

    
    def _DCFile__overloaded_write_ptrConstDCFile_ptrOstream_bool(self, out, brief):
        returnValue = libdirect._inP5HfQ4v0f(self.this, out.this, brief)
        return returnValue

    
    def getNumClasses(self):
        returnValue = libdirect._inP5HfQ4S8N(self.this)
        return returnValue

    
    def getClass(self, n):
        returnValue = libdirect._inP5HfQEYUl(self.this, n)
        import DCClass
        returnObject = DCClass.DCClass(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getClassByName(self, name):
        returnValue = libdirect._inP5HfQ_5op(self.this, name)
        import DCClass
        returnObject = DCClass.DCClass(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getSwitchByName(self, name):
        returnValue = libdirect._inP5HfQSm8d(self.this, name)
        import DCSwitch
        returnObject = DCSwitch.DCSwitch(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def allObjectsValid(self):
        returnValue = libdirect._inP5HfQuN3i(self.this)
        return returnValue

    
    def getNumImportModules(self):
        returnValue = libdirect._inP5HfQyf1h(self.this)
        return returnValue

    
    def getImportModule(self, n):
        returnValue = libdirect._inP5HfQ7Jiy(self.this, n)
        return returnValue

    
    def getNumImportSymbols(self, n):
        returnValue = libdirect._inP5HfQJagU(self.this, n)
        return returnValue

    
    def getImportSymbol(self, n, i):
        returnValue = libdirect._inP5HfQNoCv(self.this, n, i)
        return returnValue

    
    def getNumTypedefs(self):
        returnValue = libdirect._inP5HfQyp_b(self.this)
        return returnValue

    
    def getTypedef(self, n):
        returnValue = libdirect._inP5HfQqgG_(self.this, n)
        import DCTypedef
        returnObject = DCTypedef.DCTypedef(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getTypedefByName(self, name):
        returnValue = libdirect._inP5HfQN8xh(self.this, name)
        import DCTypedef
        returnObject = DCTypedef.DCTypedef(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getHash(self):
        returnValue = libdirect._inP5HfQXMzc(self.this)
        return returnValue

    
    def read(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Istream
            if isinstance(_args[0], Istream.Istream):
                return self._DCFile__overloaded_read_ptrDCFile_ptrIstream(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._DCFile__overloaded_read_ptrDCFile_ptrFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
        elif numArgs == 2:
            return self._DCFile__overloaded_read_ptrDCFile_ptrIstream_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._DCFile__overloaded_write_ptrConstDCFile_ptrOstream_bool(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._DCFile__overloaded_write_ptrConstDCFile_ptrFilename_bool(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


