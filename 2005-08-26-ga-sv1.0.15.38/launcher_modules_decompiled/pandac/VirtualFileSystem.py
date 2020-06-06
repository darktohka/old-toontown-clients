# File: V (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class VirtualFileSystem(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    MFReadOnly = 2
    MFOwnsPointer = 1
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaexpress._inPKoxtEd6o()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtx7Vu:
            libpandaexpress._inPKoxtx7Vu(self.this)
        

    
    def getGlobalPtr():
        returnValue = libpandaexpress._inPKoxt_zcf()
        returnObject = VirtualFileSystem(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalPtr = staticmethod(getGlobalPtr)
    
    def _VirtualFileSystem__overloaded_mount_ptrVirtualFileSystem_ptrConstFilename_atomicstring_int_atomicstring(self, physicalFilename, mountPoint, flags, password):
        returnValue = libpandaexpress._inPKoxtdT4R(self.this, physicalFilename.this, mountPoint, flags, password)
        return returnValue

    
    def _VirtualFileSystem__overloaded_mount_ptrVirtualFileSystem_ptrConstFilename_atomicstring_int(self, physicalFilename, mountPoint, flags):
        returnValue = libpandaexpress._inPKoxt0Y1P(self.this, physicalFilename.this, mountPoint, flags)
        return returnValue

    
    def _VirtualFileSystem__overloaded_mount_ptrVirtualFileSystem_ptrMultifile_atomicstring_int(self, multifile, mountPoint, flags):
        returnValue = libpandaexpress._inPKoxtfQsl(self.this, multifile.this, mountPoint, flags)
        return returnValue

    
    def _VirtualFileSystem__overloaded_unmount_ptrVirtualFileSystem_ptrConstFilename(self, physicalFilename):
        returnValue = libpandaexpress._inPKoxt_kpP(self.this, physicalFilename.this)
        return returnValue

    
    def _VirtualFileSystem__overloaded_unmount_ptrVirtualFileSystem_ptrMultifile(self, multifile):
        returnValue = libpandaexpress._inPKoxty9Qn(self.this, multifile.this)
        return returnValue

    
    def unmountPoint(self, mountPoint):
        returnValue = libpandaexpress._inPKoxtgppP(self.this, mountPoint)
        return returnValue

    
    def unmountAll(self):
        returnValue = libpandaexpress._inPKoxtatSe(self.this)
        return returnValue

    
    def chdir(self, newDirectory):
        returnValue = libpandaexpress._inPKoxt9T4X(self.this, newDirectory)
        return returnValue

    
    def getCwd(self):
        returnValue = libpandaexpress._inPKoxtDRrG(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getFile(self, filename):
        returnValue = libpandaexpress._inPKoxty3zk(self.this, filename.this)
        import VirtualFile
        returnObject = VirtualFile.VirtualFile(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findFile(self, filename, searchpath):
        returnValue = libpandaexpress._inPKoxt9oz3(self.this, filename.this, searchpath.this)
        import VirtualFile
        returnObject = VirtualFile.VirtualFile(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _VirtualFileSystem__overloaded_resolveFilename_ptrConstVirtualFileSystem_ptrFilename_ptrConstDSearchPath_atomicstring(self, filename, searchpath, defaultExtension):
        returnValue = libpandaexpress._inPKoxtgtIn(self.this, filename.this, searchpath.this, defaultExtension)
        return returnValue

    
    def _VirtualFileSystem__overloaded_resolveFilename_ptrConstVirtualFileSystem_ptrFilename_ptrConstDSearchPath(self, filename, searchpath):
        returnValue = libpandaexpress._inPKoxtqRwJ(self.this, filename.this, searchpath.this)
        return returnValue

    
    def findAllFiles(self, filename, searchpath, results):
        returnValue = libpandaexpress._inPKoxtvy79(self.this, filename.this, searchpath.this, results.this)
        return returnValue

    
    def exists(self, filename):
        returnValue = libpandaexpress._inPKoxtFDjI(self.this, filename.this)
        return returnValue

    
    def isDirectory(self, filename):
        returnValue = libpandaexpress._inPKoxtpcNJ(self.this, filename.this)
        return returnValue

    
    def isRegularFile(self, filename):
        returnValue = libpandaexpress._inPKoxtkO_z(self.this, filename.this)
        return returnValue

    
    def ls(self, filename):
        returnValue = libpandaexpress._inPKoxt4Fxl(self.this, filename)
        return returnValue

    
    def lsAll(self, filename):
        returnValue = libpandaexpress._inPKoxtIQxJ(self.this, filename)
        return returnValue

    
    def write(self, out):
        returnValue = libpandaexpress._inPKoxtGxed(self.this, out.this)
        return returnValue

    
    def readFile(self, filename):
        returnValue = libpandaexpress._inPKoxtrdz8(self.this, filename.this)
        return returnValue

    
    def openReadFile(self, filename):
        returnValue = libpandaexpress._inPKoxtGAnH(self.this, filename.this)
        import Istream
        returnObject = Istream.Istream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def closeReadFile(self, stream):
        returnValue = libpandaexpress._inPKoxt1PwT(self.this, stream.this)
        return returnValue

    
    def mount(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            import Multifile
            if isinstance(_args[0], Multifile.Multifile):
                return self._VirtualFileSystem__overloaded_mount_ptrVirtualFileSystem_ptrMultifile_atomicstring_int(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._VirtualFileSystem__overloaded_mount_ptrVirtualFileSystem_ptrConstFilename_atomicstring_int(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Multifile.Multifile> <Filename.Filename> '
        elif numArgs == 4:
            return self._VirtualFileSystem__overloaded_mount_ptrVirtualFileSystem_ptrConstFilename_atomicstring_int_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

    
    def unmount(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Multifile
            if isinstance(_args[0], Multifile.Multifile):
                return self._VirtualFileSystem__overloaded_unmount_ptrVirtualFileSystem_ptrMultifile(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._VirtualFileSystem__overloaded_unmount_ptrVirtualFileSystem_ptrConstFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Multifile.Multifile> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def resolveFilename(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._VirtualFileSystem__overloaded_resolveFilename_ptrConstVirtualFileSystem_ptrFilename_ptrConstDSearchPath(*_args)
        elif numArgs == 3:
            return self._VirtualFileSystem__overloaded_resolveFilename_ptrConstVirtualFileSystem_ptrFilename_ptrConstDSearchPath_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


