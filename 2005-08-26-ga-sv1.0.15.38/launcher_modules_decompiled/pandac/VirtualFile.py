# File: V (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class VirtualFile(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtfhDj:
            libpandaexpress._inPKoxtfhDj(self.this)
        

    
    def getClassType():
        returnValue = libpandaexpress._inPKoxt1f88()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getFileSystem(self):
        returnValue = libpandaexpress._inPKoxtWaEw(self.this)
        import VirtualFileSystem
        returnObject = VirtualFileSystem.VirtualFileSystem(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getFilename(self):
        returnValue = libpandaexpress._inPKoxt7aYo(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def isDirectory(self):
        returnValue = libpandaexpress._inPKoxt3gtu(self.this)
        return returnValue

    
    def isRegularFile(self):
        returnValue = libpandaexpress._inPKoxtxCeS(self.this)
        return returnValue

    
    def scanDirectory(self):
        returnValue = libpandaexpress._inPKoxt4egf(self.this)
        import VirtualFileList
        returnObject = VirtualFileList.VirtualFileList(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtJKgU(self.this, out.this)
        return returnValue

    
    def _VirtualFile__overloaded_ls_ptrConstVirtualFile_ptrOstream(self, out):
        returnValue = libpandaexpress._inPKoxtkWDV(self.this, out.this)
        return returnValue

    
    def _VirtualFile__overloaded_ls_ptrConstVirtualFile(self):
        returnValue = libpandaexpress._inPKoxt42an(self.this)
        return returnValue

    
    def _VirtualFile__overloaded_lsAll_ptrConstVirtualFile_ptrOstream(self, out):
        returnValue = libpandaexpress._inPKoxtlJmn(self.this, out.this)
        return returnValue

    
    def _VirtualFile__overloaded_lsAll_ptrConstVirtualFile(self):
        returnValue = libpandaexpress._inPKoxt_9x0(self.this)
        return returnValue

    
    def readFile(self):
        returnValue = libpandaexpress._inPKoxthdoM(self.this)
        return returnValue

    
    def openReadFile(self):
        returnValue = libpandaexpress._inPKoxtqeIl(self.this)
        import Istream
        returnObject = Istream.Istream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def closeReadFile(self, stream):
        returnValue = libpandaexpress._inPKoxtUTlQ(self.this, stream.this)
        return returnValue

    
    def getFileSize(self, stream):
        returnValue = libpandaexpress._inPKoxtklGA(self.this, stream.this)
        return returnValue

    
    def lsAll(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VirtualFile__overloaded_lsAll_ptrConstVirtualFile(*_args)
        elif numArgs == 1:
            return self._VirtualFile__overloaded_lsAll_ptrConstVirtualFile_ptrOstream(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def ls(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VirtualFile__overloaded_ls_ptrConstVirtualFile(*_args)
        elif numArgs == 1:
            return self._VirtualFile__overloaded_ls_ptrConstVirtualFile_ptrOstream(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


