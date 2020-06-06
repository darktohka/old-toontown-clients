# File: M (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ReferenceCount

class Multifile(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaexpress._inPKoxtwqaa()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtOYoW:
            libpandaexpress._inPKoxtOYoW(self.this)
        

    
    def openRead(self, multifileName):
        returnValue = libpandaexpress._inPKoxt9Q56(self.this, multifileName.this)
        return returnValue

    
    def openWrite(self, multifileName):
        returnValue = libpandaexpress._inPKoxtfyBJ(self.this, multifileName.this)
        return returnValue

    
    def openReadWrite(self, multifileName):
        returnValue = libpandaexpress._inPKoxtIEQv(self.this, multifileName.this)
        return returnValue

    
    def close(self):
        returnValue = libpandaexpress._inPKoxtMa18(self.this)
        return returnValue

    
    def getMultifileName(self):
        returnValue = libpandaexpress._inPKoxtit0K(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isReadValid(self):
        returnValue = libpandaexpress._inPKoxtbS6p(self.this)
        return returnValue

    
    def isWriteValid(self):
        returnValue = libpandaexpress._inPKoxtpFGO(self.this)
        return returnValue

    
    def needsRepack(self):
        returnValue = libpandaexpress._inPKoxt0bT4(self.this)
        return returnValue

    
    def setScaleFactor(self, scaleFactor):
        returnValue = libpandaexpress._inPKoxt2jcN(self.this, scaleFactor)
        return returnValue

    
    def getScaleFactor(self):
        returnValue = libpandaexpress._inPKoxtWN1X(self.this)
        return returnValue

    
    def setEncryptionFlag(self, flag):
        returnValue = libpandaexpress._inPKoxta6QQ(self.this, flag)
        return returnValue

    
    def getEncryptionFlag(self):
        returnValue = libpandaexpress._inPKoxtDazL(self.this)
        return returnValue

    
    def setEncryptionPassword(self, password):
        returnValue = libpandaexpress._inPKoxt7mjs(self.this, password)
        return returnValue

    
    def getEncryptionPassword(self):
        returnValue = libpandaexpress._inPKoxtSjUj(self.this)
        return returnValue

    
    def addSubfile(self, subfileName, filename, compressionLevel):
        returnValue = libpandaexpress._inPKoxtDhxy(self.this, subfileName, filename.this, compressionLevel)
        return returnValue

    
    def updateSubfile(self, subfileName, filename, compressionLevel):
        returnValue = libpandaexpress._inPKoxtz3H7(self.this, subfileName, filename.this, compressionLevel)
        return returnValue

    
    def flush(self):
        returnValue = libpandaexpress._inPKoxt7cnZ(self.this)
        return returnValue

    
    def repack(self):
        returnValue = libpandaexpress._inPKoxthLqr(self.this)
        return returnValue

    
    def getNumSubfiles(self):
        returnValue = libpandaexpress._inPKoxtCa0B(self.this)
        return returnValue

    
    def findSubfile(self, subfileName):
        returnValue = libpandaexpress._inPKoxtAvHU(self.this, subfileName)
        return returnValue

    
    def hasDirectory(self, subfileName):
        returnValue = libpandaexpress._inPKoxt_fnT(self.this, subfileName)
        return returnValue

    
    def scanDirectory(self, contents, subfileName):
        returnValue = libpandaexpress._inPKoxtC9bD(self.this, contents.this, subfileName)
        return returnValue

    
    def removeSubfile(self, index):
        returnValue = libpandaexpress._inPKoxtyAb8(self.this, index)
        return returnValue

    
    def getSubfileName(self, index):
        returnValue = libpandaexpress._inPKoxtUz_f(self.this, index)
        return returnValue

    
    def getSubfileLength(self, index):
        returnValue = libpandaexpress._inPKoxteCrf(self.this, index)
        return returnValue

    
    def isSubfileCompressed(self, index):
        returnValue = libpandaexpress._inPKoxtYA9O(self.this, index)
        return returnValue

    
    def isSubfileEncrypted(self, index):
        returnValue = libpandaexpress._inPKoxtlEUv(self.this, index)
        return returnValue

    
    def getSubfileInternalLength(self, index):
        returnValue = libpandaexpress._inPKoxtqvJ_(self.this, index)
        return returnValue

    
    def readSubfile(self, index):
        returnValue = libpandaexpress._inPKoxtNjWf(self.this, index)
        return returnValue

    
    def openReadSubfile(self, index):
        returnValue = libpandaexpress._inPKoxtGXxf(self.this, index)
        import Istream
        returnObject = Istream.Istream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def extractSubfile(self, index, filename):
        returnValue = libpandaexpress._inPKoxtxPcf(self.this, index, filename.this)
        return returnValue

    
    def compareSubfile(self, index, filename):
        returnValue = libpandaexpress._inPKoxt0DCF(self.this, index, filename.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtHX_Y(self.this, out.this)
        return returnValue

    
    def _Multifile__overloaded_ls_ptrConstMultifile_ptrOstream(self, out):
        returnValue = libpandaexpress._inPKoxt_Zzn(self.this, out.this)
        return returnValue

    
    def _Multifile__overloaded_ls_ptrConstMultifile(self):
        returnValue = libpandaexpress._inPKoxthACw(self.this)
        return returnValue

    
    def ls(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Multifile__overloaded_ls_ptrConstMultifile(*_args)
        elif numArgs == 1:
            return self._Multifile__overloaded_ls_ptrConstMultifile_ptrOstream(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


