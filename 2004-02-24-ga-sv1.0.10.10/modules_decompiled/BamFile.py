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
        

    
    def _BamFile__overloaded_openRead_ptrBamFile_ptrConstFilename_bool(self, bamFilename, reportErrors):
        returnValue = libpanda._inPkJyoZ5gF(self.this, bamFilename.this, reportErrors)
        return returnValue

    
    def _BamFile__overloaded_openRead_ptrBamFile_ptrConstFilename(self, bamFilename):
        returnValue = libpanda._inPkJyozHfD(self.this, bamFilename.this)
        return returnValue

    
    def _BamFile__overloaded_openRead_ptrBamFile_ptrIstream_atomicstring_bool(self, _in, bamFilename, reportErrors):
        returnValue = libpanda._inPkJyoWZ_Q(self.this, _in.this, bamFilename, reportErrors)
        return returnValue

    
    def _BamFile__overloaded_openRead_ptrBamFile_ptrIstream_atomicstring(self, _in, bamFilename):
        returnValue = libpanda._inPkJyodf6U(self.this, _in.this, bamFilename)
        return returnValue

    
    def _BamFile__overloaded_openRead_ptrBamFile_ptrIstream(self, _in):
        returnValue = libpanda._inPkJyoJKs6(self.this, _in.this)
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

    
    def _BamFile__overloaded_readNode_ptrBamFile_bool(self, reportErrors):
        returnValue = libpanda._inPkJyoYvGY(self.this, reportErrors)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _BamFile__overloaded_readNode_ptrBamFile(self):
        returnValue = libpanda._inPkJyohEoM(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _BamFile__overloaded_openWrite_ptrBamFile_ptrConstFilename_bool(self, bamFilename, reportErrors):
        returnValue = libpanda._inPkJyoXyE3(self.this, bamFilename.this, reportErrors)
        return returnValue

    
    def _BamFile__overloaded_openWrite_ptrBamFile_ptrConstFilename(self, bamFilename):
        returnValue = libpanda._inPkJyoBij1(self.this, bamFilename.this)
        return returnValue

    
    def _BamFile__overloaded_openWrite_ptrBamFile_ptrOstream_atomicstring_bool(self, out, bamFilename, reportErrors):
        returnValue = libpanda._inPkJyoPGvp(self.this, out.this, bamFilename, reportErrors)
        return returnValue

    
    def _BamFile__overloaded_openWrite_ptrBamFile_ptrOstream_atomicstring(self, out, bamFilename):
        returnValue = libpanda._inPkJyoAPsn(self.this, out.this, bamFilename)
        return returnValue

    
    def _BamFile__overloaded_openWrite_ptrBamFile_ptrOstream(self, out):
        returnValue = libpanda._inPkJyom4Ne(self.this, out.this)
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

    
    def readNode(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._BamFile__overloaded_readNode_ptrBamFile()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._BamFile__overloaded_readNode_ptrBamFile_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def openRead(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Istream
            import Filename
            if isinstance(_args[0], Istream.Istream):
                return self._BamFile__overloaded_openRead_ptrBamFile_ptrIstream(_args[0])
            elif isinstance(_args[0], Filename.Filename):
                return self._BamFile__overloaded_openRead_ptrBamFile_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
        elif numArgs == 2:
            import Istream
            import Filename
            if isinstance(_args[0], Istream.Istream):
                if isinstance(_args[1], types.StringType):
                    return self._BamFile__overloaded_openRead_ptrBamFile_ptrIstream_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            elif isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._BamFile__overloaded_openRead_ptrBamFile_ptrConstFilename_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
        elif numArgs == 3:
            import Istream
            if isinstance(_args[0], Istream.Istream):
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.IntType):
                        return self._BamFile__overloaded_openRead_ptrBamFile_ptrIstream_atomicstring_bool(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def openWrite(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            import Filename
            if isinstance(_args[0], Ostream.Ostream):
                return self._BamFile__overloaded_openWrite_ptrBamFile_ptrOstream(_args[0])
            elif isinstance(_args[0], Filename.Filename):
                return self._BamFile__overloaded_openWrite_ptrBamFile_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
        elif numArgs == 2:
            import Ostream
            import Filename
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.StringType):
                    return self._BamFile__overloaded_openWrite_ptrBamFile_ptrOstream_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            elif isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._BamFile__overloaded_openWrite_ptrBamFile_ptrConstFilename_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
        elif numArgs == 3:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.IntType):
                        return self._BamFile__overloaded_openWrite_ptrBamFile_ptrOstream_atomicstring_bool(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '


