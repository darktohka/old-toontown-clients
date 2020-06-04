# File: M (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class Multifile(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpandaexpress._inPJoxtwqaa()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtOYoW:
            libpandaexpress._inPJoxtOYoW(self.this)
        

    
    def openRead(self, multifileName):
        returnValue = libpandaexpress._inPJoxt_Q56(self.this, multifileName.this)
        return returnValue

    
    def openWrite(self, multifileName):
        returnValue = libpandaexpress._inPJoxtfyBJ(self.this, multifileName.this)
        return returnValue

    
    def openReadWrite(self, multifileName):
        returnValue = libpandaexpress._inPJoxtJEQv(self.this, multifileName.this)
        return returnValue

    
    def close(self):
        returnValue = libpandaexpress._inPJoxtNa18(self.this)
        return returnValue

    
    def getMultifileName(self):
        returnValue = libpandaexpress._inPJoxtit0K(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isReadValid(self):
        returnValue = libpandaexpress._inPJoxtaS6p(self.this)
        return returnValue

    
    def isWriteValid(self):
        returnValue = libpandaexpress._inPJoxtpFGO(self.this)
        return returnValue

    
    def needsRepack(self):
        returnValue = libpandaexpress._inPJoxt1bT4(self.this)
        return returnValue

    
    def setScaleFactor(self, scaleFactor):
        returnValue = libpandaexpress._inPJoxt2jcN(self.this, scaleFactor)
        return returnValue

    
    def getScaleFactor(self):
        returnValue = libpandaexpress._inPJoxtWN1X(self.this)
        return returnValue

    
    def addSubfile(self, subfileName, filename, compressionLevel):
        returnValue = libpandaexpress._inPJoxtAhxy(self.this, subfileName, filename.this, compressionLevel)
        return returnValue

    
    def flush(self):
        returnValue = libpandaexpress._inPJoxt7cnZ(self.this)
        return returnValue

    
    def repack(self):
        returnValue = libpandaexpress._inPJoxtmLqr(self.this)
        return returnValue

    
    def getNumSubfiles(self):
        returnValue = libpandaexpress._inPJoxtCa0B(self.this)
        return returnValue

    
    def findSubfile(self, subfileName):
        returnValue = libpandaexpress._inPJoxtAvHU(self.this, subfileName)
        return returnValue

    
    def hasDirectory(self, subfileName):
        returnValue = libpandaexpress._inPJoxt_fnT(self.this, subfileName)
        return returnValue

    
    def scanDirectory(self, contents, subfileName):
        returnValue = libpandaexpress._inPJoxtC9bD(self.this, contents.this, subfileName)
        return returnValue

    
    def removeSubfile(self, index):
        returnValue = libpandaexpress._inPJoxtxAb8(self.this, index)
        return returnValue

    
    def getSubfileName(self, index):
        returnValue = libpandaexpress._inPJoxtUz_f(self.this, index)
        return returnValue

    
    def getSubfileLength(self, index):
        returnValue = libpandaexpress._inPJoxteCrf(self.this, index)
        return returnValue

    
    def isSubfileCompressed(self, index):
        returnValue = libpandaexpress._inPJoxtYA9O(self.this, index)
        return returnValue

    
    def getSubfileCompressedLength(self, index):
        returnValue = libpandaexpress._inPJoxtHAV2(self.this, index)
        return returnValue

    
    def readSubfile(self, index):
        returnValue = libpandaexpress._inPJoxtNjWf(self.this, index)
        return returnValue

    
    def openReadSubfile(self, index):
        returnValue = libpandaexpress._inPJoxtGXxf(self.this, index)
        import Istream
        returnObject = Istream.Istream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def extractSubfile(self, index, filename):
        returnValue = libpandaexpress._inPJoxtxPcf(self.this, index, filename.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPJoxtHX_Y(self.this, out.this)
        return returnValue

    
    def _Multifile__overloaded_ls_ptrConstMultifile_ptrOstream(self, out):
        returnValue = libpandaexpress._inPJoxt_Zzn(self.this, out.this)
        return returnValue

    
    def _Multifile__overloaded_ls_ptrConstMultifile(self):
        returnValue = libpandaexpress._inPJoxteBCw(self.this)
        return returnValue

    
    def ls(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Multifile__overloaded_ls_ptrConstMultifile()
        elif numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Multifile__overloaded_ls_ptrConstMultifile_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


