# File: V (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount

class VirtualFile(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtchDj:
            libpandaexpress._inPJoxtchDj(self.this)
        

    
    def getClassType():
        returnValue = libpandaexpress._inPJoxt2f88()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getFileSystem(self):
        returnValue = libpandaexpress._inPJoxtRaEw(self.this)
        import VirtualFileSystem
        returnObject = VirtualFileSystem.VirtualFileSystem(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getFilename(self):
        returnValue = libpandaexpress._inPJoxtkaYo(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def isDirectory(self):
        returnValue = libpandaexpress._inPJoxt2gtu(self.this)
        return returnValue

    
    def isRegularFile(self):
        returnValue = libpandaexpress._inPJoxtxCeS(self.this)
        return returnValue

    
    def scanDirectory(self):
        returnValue = libpandaexpress._inPJoxt4egf(self.this)
        import VirtualFileList
        returnObject = VirtualFileList.VirtualFileList(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def output(self, out):
        returnValue = libpandaexpress._inPJoxtJKgU(self.this, out.this)
        return returnValue

    
    def _VirtualFile__overloaded_ls_ptrConstVirtualFile_ptrOstream(self, out):
        returnValue = libpandaexpress._inPJoxtkWDV(self.this, out.this)
        return returnValue

    
    def _VirtualFile__overloaded_ls_ptrConstVirtualFile(self):
        returnValue = libpandaexpress._inPJoxt52an(self.this)
        return returnValue

    
    def _VirtualFile__overloaded_lsAll_ptrConstVirtualFile_ptrOstream(self, out):
        returnValue = libpandaexpress._inPJoxtqJmn(self.this, out.this)
        return returnValue

    
    def _VirtualFile__overloaded_lsAll_ptrConstVirtualFile(self):
        returnValue = libpandaexpress._inPJoxt89x0(self.this)
        return returnValue

    
    def readFile(self):
        returnValue = libpandaexpress._inPJoxthdoM(self.this)
        return returnValue

    
    def openReadFile(self):
        returnValue = libpandaexpress._inPJoxt1eIl(self.this)
        import Istream
        returnObject = Istream.Istream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def lsAll(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VirtualFile__overloaded_lsAll_ptrConstVirtualFile()
        elif numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._VirtualFile__overloaded_lsAll_ptrConstVirtualFile_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def ls(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VirtualFile__overloaded_ls_ptrConstVirtualFile()
        elif numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._VirtualFile__overloaded_ls_ptrConstVirtualFile_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


