# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class BamFile(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPkJyocXSJ()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyoHgJT:
            libpanda._inPkJyoHgJT(self.this)
        

    
    def _BamFile__overloaded_openRead_ptrBamFile_ptrConstFilename_bool(self, filename, reportErrors):
        returnValue = libpanda._inPkJyoZ5gF(self.this, filename.this, reportErrors)
        return returnValue

    
    def _BamFile__overloaded_openRead_ptrBamFile_ptrConstFilename(self, filename):
        returnValue = libpanda._inPkJyozHfD(self.this, filename.this)
        return returnValue

    
    def readObject(self):
        returnValue = libpanda._inPkJyoFRNy(self.this)
        import TypedWritable
        returnObject = TypedWritable.TypedWritable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def isEof(self):
        returnValue = libpanda._inPkJyoyZvF(self.this)
        return returnValue

    
    def resolve(self):
        returnValue = libpanda._inPkJyoxWXF(self.this)
        return returnValue

    
    def _BamFile__overloaded_openWrite_ptrBamFile_ptrConstFilename_bool(self, filename, reportErrors):
        returnValue = libpanda._inPkJyoXyE3(self.this, filename.this, reportErrors)
        return returnValue

    
    def _BamFile__overloaded_openWrite_ptrBamFile_ptrConstFilename(self, filename):
        returnValue = libpanda._inPkJyoBij1(self.this, filename.this)
        return returnValue

    
    def writeObject(self, object):
        returnValue = libpanda._inPkJyos9v_(self.this, object.this)
        return returnValue

    
    def close(self):
        returnValue = libpanda._inPkJyo4bSi(self.this)
        return returnValue

    
    def isValidRead(self):
        returnValue = libpanda._inPkJyoSD_c(self.this)
        return returnValue

    
    def isValidWrite(self):
        returnValue = libpanda._inPkJyoYb0C(self.this)
        return returnValue

    
    def getFileMajorVer(self):
        returnValue = libpanda._inPkJyoV3p0(self.this)
        return returnValue

    
    def getFileMinorVer(self):
        returnValue = libpanda._inPkJyoJw61(self.this)
        return returnValue

    
    def getCurrentMajorVer(self):
        returnValue = libpanda._inPkJyomKS_(self.this)
        return returnValue

    
    def getCurrentMinorVer(self):
        returnValue = libpanda._inPkJyoOdy5(self.this)
        return returnValue

    
    def openRead(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._BamFile__overloaded_openRead_ptrBamFile_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._BamFile__overloaded_openRead_ptrBamFile_ptrConstFilename_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def openWrite(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._BamFile__overloaded_openWrite_ptrBamFile_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._BamFile__overloaded_openWrite_ptrBamFile_ptrConstFilename_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


