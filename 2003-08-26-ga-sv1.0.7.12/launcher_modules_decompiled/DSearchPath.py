# File: D (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class DSearchPath(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DSearchPath__overloaded_constructor(self):
        self.this = libpandaexpress._inPJoxtwUgk()
        self.userManagesMemory = 1

    
    def _DSearchPath__overloaded_constructor_ptrConstDSearchPath(self, copy):
        self.this = libpandaexpress._inPJoxtzohW(copy.this)
        self.userManagesMemory = 1

    
    def _DSearchPath__overloaded_constructor_atomicstring_atomicstring(self, path, delimiters):
        self.this = libpandaexpress._inPJoxtuuI2(path, delimiters)
        self.userManagesMemory = 1

    
    def _DSearchPath__overloaded_constructor_atomicstring(self, path):
        self.this = libpandaexpress._inPJoxtYE_t(path)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtkXuT:
            libpandaexpress._inPJoxtkXuT(self.this)
        

    
    def _DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring_atomicstring(filename, path, delimiters):
        returnValue = libpandaexpress._inPJoxtgvcZ(filename.this, path, delimiters)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring_atomicstring = staticmethod(_DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring_atomicstring)
    
    def _DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring(filename, path):
        returnValue = libpandaexpress._inPJoxtaJd4(filename.this, path)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring = staticmethod(_DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring)
    
    def assign(self, copy):
        returnValue = libpandaexpress._inPJoxt7_r9(self.this, copy.this)
        returnObject = DSearchPath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clear(self):
        returnValue = libpandaexpress._inPJoxt_ecb(self.this)
        return returnValue

    
    def appendDirectory(self, directory):
        returnValue = libpandaexpress._inPJoxtdvve(self.this, directory.this)
        return returnValue

    
    def prependDirectory(self, directory):
        returnValue = libpandaexpress._inPJoxtSYWa(self.this, directory.this)
        return returnValue

    
    def _DSearchPath__overloaded_appendPath_ptrDSearchPath_ptrConstDSearchPath(self, path):
        returnValue = libpandaexpress._inPJoxtAcLB(self.this, path.this)
        return returnValue

    
    def _DSearchPath__overloaded_appendPath_ptrDSearchPath_atomicstring_atomicstring(self, path, delimiters):
        returnValue = libpandaexpress._inPJoxtzDyg(self.this, path, delimiters)
        return returnValue

    
    def _DSearchPath__overloaded_appendPath_ptrDSearchPath_atomicstring(self, path):
        returnValue = libpandaexpress._inPJoxtufoY(self.this, path)
        return returnValue

    
    def prependPath(self, path):
        returnValue = libpandaexpress._inPJoxtlhym(self.this, path.this)
        return returnValue

    
    def isEmpty(self):
        returnValue = libpandaexpress._inPJoxtaEii(self.this)
        return returnValue

    
    def getNumDirectories(self):
        returnValue = libpandaexpress._inPJoxtQk9K(self.this)
        return returnValue

    
    def getDirectory(self, n):
        returnValue = libpandaexpress._inPJoxteLbZ(self.this, n)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def findFile(self, filename):
        returnValue = libpandaexpress._inPJoxt86AY(self.this, filename.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findAllFiles(self, filename, results):
        returnValue = libpandaexpress._inPJoxtOBvK(self.this, filename.this, results.this)
        return returnValue

    
    def _DSearchPath__overloaded_output_ptrConstDSearchPath_ptrOstream_atomicstring(self, out, separator):
        returnValue = libpandaexpress._inPJoxtfyrW(self.this, out.this, separator)
        return returnValue

    
    def _DSearchPath__overloaded_output_ptrConstDSearchPath_ptrOstream(self, out):
        returnValue = libpandaexpress._inPJoxtx5QI(self.this, out.this)
        return returnValue

    
    def _DSearchPath__overloaded_write_ptrConstDSearchPath_ptrOstream_int(self, out, indentLevel):
        returnValue = libpandaexpress._inPJoxtFTuw(self.this, out.this, indentLevel)
        return returnValue

    
    def _DSearchPath__overloaded_write_ptrConstDSearchPath_ptrOstream(self, out):
        returnValue = libpandaexpress._inPJoxtJVg1(self.this, out.this)
        return returnValue

    
    def searchPath(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.StringType):
                    return DSearchPath._DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 3:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.StringType):
                        return DSearchPath._DSearchPath__overloaded_searchPath_ptrConstFilename_atomicstring_atomicstring(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    searchPath = staticmethod(searchPath)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DSearchPath__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DSearchPath__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], DSearchPath):
                return self._DSearchPath__overloaded_constructor_ptrConstDSearchPath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DSearchPath> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.StringType):
                    return self._DSearchPath__overloaded_constructor_atomicstring_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._DSearchPath__overloaded_write_ptrConstDSearchPath_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._DSearchPath__overloaded_write_ptrConstDSearchPath_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def output(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._DSearchPath__overloaded_output_ptrConstDSearchPath_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.StringType):
                    return self._DSearchPath__overloaded_output_ptrConstDSearchPath_ptrOstream_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def appendPath(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DSearchPath__overloaded_appendPath_ptrDSearchPath_atomicstring(_args[0])
            elif isinstance(_args[0], DSearchPath):
                return self._DSearchPath__overloaded_appendPath_ptrDSearchPath_ptrConstDSearchPath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DSearchPath> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.StringType):
                    return self._DSearchPath__overloaded_appendPath_ptrDSearchPath_atomicstring_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


