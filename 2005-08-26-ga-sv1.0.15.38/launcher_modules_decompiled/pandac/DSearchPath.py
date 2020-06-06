# File: D (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class DSearchPath(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DSearchPath__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtxUgk()
        self.userManagesMemory = 1

    
    def _DSearchPath__overloaded_constructor_ptrConstDSearchPath(self, copy):
        self.this = libpandaexpress._inPKoxtzohW(copy.this)
        self.userManagesMemory = 1

    
    def _DSearchPath__overloaded_constructor_atomicstring_atomicstring(self, path, separator):
        self.this = libpandaexpress._inPKoxttuI2(path, separator)
        self.userManagesMemory = 1

    
    def _DSearchPath__overloaded_constructor_atomicstring(self, path):
        self.this = libpandaexpress._inPKoxtbE_t(path)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtkXuT:
            libpandaexpress._inPKoxtkXuT(self.this)
        

    
    def _DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring_atomicstring(filename, path, separator):
        returnValue = libpandaexpress._inPKoxtgvcZ(filename.this, path, separator)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring_atomicstring = staticmethod(_DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring_atomicstring)
    
    def _DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring(filename, path):
        returnValue = libpandaexpress._inPKoxtFJd4(filename.this, path)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring = staticmethod(_DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring)
    
    def assign(self, copy):
        returnValue = libpandaexpress._inPKoxt4_r9(self.this, copy.this)
        returnObject = DSearchPath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clear(self):
        returnValue = libpandaexpress._inPKoxt_ecb(self.this)
        return returnValue

    
    def appendDirectory(self, directory):
        returnValue = libpandaexpress._inPKoxtdvve(self.this, directory.this)
        return returnValue

    
    def prependDirectory(self, directory):
        returnValue = libpandaexpress._inPKoxtSYWa(self.this, directory.this)
        return returnValue

    
    def _DSearchPath__overloaded_appendPath_ptrDSearchPath_ptrConstDSearchPath(self, path):
        returnValue = libpandaexpress._inPKoxtAcLB(self.this, path.this)
        return returnValue

    
    def _DSearchPath__overloaded_appendPath_ptrDSearchPath_atomicstring_atomicstring(self, path, separator):
        returnValue = libpandaexpress._inPKoxtwDyg(self.this, path, separator)
        return returnValue

    
    def _DSearchPath__overloaded_appendPath_ptrDSearchPath_atomicstring(self, path):
        returnValue = libpandaexpress._inPKoxtufoY(self.this, path)
        return returnValue

    
    def prependPath(self, path):
        returnValue = libpandaexpress._inPKoxtihym(self.this, path.this)
        return returnValue

    
    def isEmpty(self):
        returnValue = libpandaexpress._inPKoxtbEii(self.this)
        return returnValue

    
    def getNumDirectories(self):
        returnValue = libpandaexpress._inPKoxtQk9K(self.this)
        return returnValue

    
    def getDirectory(self, n):
        returnValue = libpandaexpress._inPKoxteLbZ(self.this, n)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def findFile(self, filename):
        returnValue = libpandaexpress._inPKoxt86AY(self.this, filename.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findAllFiles(self, filename, results):
        returnValue = libpandaexpress._inPKoxtOBvK(self.this, filename.this, results.this)
        return returnValue

    
    def _DSearchPath__overloaded_output_ptrConstDSearchPath_ptrOstream_atomicstring(self, out, separator):
        returnValue = libpandaexpress._inPKoxtfyrW(self.this, out.this, separator)
        return returnValue

    
    def _DSearchPath__overloaded_output_ptrConstDSearchPath_ptrOstream(self, out):
        returnValue = libpandaexpress._inPKoxtx5QI(self.this, out.this)
        return returnValue

    
    def _DSearchPath__overloaded_write_ptrConstDSearchPath_ptrOstream_int(self, out, indentLevel):
        returnValue = libpandaexpress._inPKoxtGTuw(self.this, out.this, indentLevel)
        return returnValue

    
    def _DSearchPath__overloaded_write_ptrConstDSearchPath_ptrOstream(self, out):
        returnValue = libpandaexpress._inPKoxtIVg1(self.this, out.this)
        return returnValue

    
    def searchPath(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return DSearchPath._DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring(*_args)
        elif numArgs == 3:
            return DSearchPath._DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    searchPath = staticmethod(searchPath)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DSearchPath__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DSearchPath__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DSearchPath):
                return self._DSearchPath__overloaded_constructor_ptrConstDSearchPath(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DSearchPath> '
        elif numArgs == 2:
            return self._DSearchPath__overloaded_constructor_atomicstring_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DSearchPath__overloaded_write_ptrConstDSearchPath_ptrOstream(*_args)
        elif numArgs == 2:
            return self._DSearchPath__overloaded_write_ptrConstDSearchPath_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def output(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DSearchPath__overloaded_output_ptrConstDSearchPath_ptrOstream(*_args)
        elif numArgs == 2:
            return self._DSearchPath__overloaded_output_ptrConstDSearchPath_ptrOstream_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def appendPath(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DSearchPath__overloaded_appendPath_ptrDSearchPath_atomicstring(*_args)
            
            if isinstance(_args[0], DSearchPath):
                return self._DSearchPath__overloaded_appendPath_ptrDSearchPath_ptrConstDSearchPath(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DSearchPath> '
        elif numArgs == 2:
            return self._DSearchPath__overloaded_appendPath_ptrDSearchPath_atomicstring_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


