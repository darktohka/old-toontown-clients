# File: V (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class VirtualFileSystem(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    MFReadOnly = 2
    MFOwnsPointer = 1
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpandaexpress._inPJoxtFd6o()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtO7Vu:
            libpandaexpress._inPJoxtO7Vu(self.this)
        

    
    def getGlobalPtr():
        returnValue = libpandaexpress._inPJoxt_zcf()
        returnObject = VirtualFileSystem(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalPtr = staticmethod(getGlobalPtr)
    
    def _VirtualFileSystem__overloaded_mount_ptrVirtualFileSystem_ptrConstFilename_atomicstring_int(self, physicalFilename, mountPoint, flags):
        returnValue = libpandaexpress._inPJoxt0Y1P(self.this, physicalFilename.this, mountPoint, flags)
        return returnValue

    
    def _VirtualFileSystem__overloaded_mount_ptrVirtualFileSystem_ptrMultifile_atomicstring_int(self, multifile, mountPoint, flags):
        returnValue = libpandaexpress._inPJoxtcQsl(self.this, multifile.this, mountPoint, flags)
        return returnValue

    
    def _VirtualFileSystem__overloaded_unmount_ptrVirtualFileSystem_ptrConstFilename(self, physicalFilename):
        returnValue = libpandaexpress._inPJoxt_kpP(self.this, physicalFilename.this)
        return returnValue

    
    def _VirtualFileSystem__overloaded_unmount_ptrVirtualFileSystem_ptrMultifile(self, multifile):
        returnValue = libpandaexpress._inPJoxtz9Qn(self.this, multifile.this)
        return returnValue

    
    def unmountPoint(self, mountPoint):
        returnValue = libpandaexpress._inPJoxtgppP(self.this, mountPoint)
        return returnValue

    
    def unmountAll(self):
        returnValue = libpandaexpress._inPJoxtatSe(self.this)
        return returnValue

    
    def chdir(self, newDirectory):
        returnValue = libpandaexpress._inPJoxt9T4X(self.this, newDirectory)
        return returnValue

    
    def getCwd(self):
        returnValue = libpandaexpress._inPJoxtDRrG(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getFile(self, filename):
        returnValue = libpandaexpress._inPJoxtt3zk(self.this, filename.this)
        import VirtualFile
        returnObject = VirtualFile.VirtualFile(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findFile(self, filename, searchpath):
        returnValue = libpandaexpress._inPJoxt_oz3(self.this, filename.this, searchpath.this)
        import VirtualFile
        returnObject = VirtualFile.VirtualFile(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _VirtualFileSystem__overloaded_resolveFilename_ptrConstVirtualFileSystem_ptrFilename_ptrConstDSearchPath_atomicstring(self, filename, searchpath, defaultExtension):
        returnValue = libpandaexpress._inPJoxt_tIn(self.this, filename.this, searchpath.this, defaultExtension)
        return returnValue

    
    def _VirtualFileSystem__overloaded_resolveFilename_ptrConstVirtualFileSystem_ptrFilename_ptrConstDSearchPath(self, filename, searchpath):
        returnValue = libpandaexpress._inPJoxtqRwJ(self.this, filename.this, searchpath.this)
        return returnValue

    
    def findAllFiles(self, filename, searchpath, results):
        returnValue = libpandaexpress._inPJoxtoy79(self.this, filename.this, searchpath.this, results.this)
        return returnValue

    
    def exists(self, filename):
        returnValue = libpandaexpress._inPJoxtFDjI(self.this, filename.this)
        return returnValue

    
    def isDirectory(self, filename):
        returnValue = libpandaexpress._inPJoxtpcNJ(self.this, filename.this)
        return returnValue

    
    def isRegularFile(self, filename):
        returnValue = libpandaexpress._inPJoxtlO_z(self.this, filename.this)
        return returnValue

    
    def ls(self, filename):
        returnValue = libpandaexpress._inPJoxt7Fxl(self.this, filename)
        return returnValue

    
    def lsAll(self, filename):
        returnValue = libpandaexpress._inPJoxtIQxJ(self.this, filename)
        return returnValue

    
    def write(self, out):
        returnValue = libpandaexpress._inPJoxtGxed(self.this, out.this)
        return returnValue

    
    def readFile(self, filename):
        returnValue = libpandaexpress._inPJoxtsdz8(self.this, filename.this)
        return returnValue

    
    def openReadFile(self, filename):
        returnValue = libpandaexpress._inPJoxtGAnH(self.this, filename.this)
        import Istream
        returnObject = Istream.Istream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def mount(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            import Multifile
            import Filename
            if isinstance(_args[0], Multifile.Multifile):
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.IntType):
                        return self._VirtualFileSystem__overloaded_mount_ptrVirtualFileSystem_ptrMultifile_atomicstring_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            elif isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.IntType):
                        return self._VirtualFileSystem__overloaded_mount_ptrVirtualFileSystem_ptrConstFilename_atomicstring_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Multifile.Multifile> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 '

    
    def unmount(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Multifile
            import Filename
            if isinstance(_args[0], Multifile.Multifile):
                return self._VirtualFileSystem__overloaded_unmount_ptrVirtualFileSystem_ptrMultifile(_args[0])
            elif isinstance(_args[0], Filename.Filename):
                return self._VirtualFileSystem__overloaded_unmount_ptrVirtualFileSystem_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Multifile.Multifile> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def resolveFilename(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                import DSearchPath
                if isinstance(_args[1], DSearchPath.DSearchPath):
                    return self._VirtualFileSystem__overloaded_resolveFilename_ptrConstVirtualFileSystem_ptrFilename_ptrConstDSearchPath(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <DSearchPath.DSearchPath> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 3:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                import DSearchPath
                if isinstance(_args[1], DSearchPath.DSearchPath):
                    if isinstance(_args[2], types.StringType):
                        return self._VirtualFileSystem__overloaded_resolveFilename_ptrConstVirtualFileSystem_ptrFilename_ptrConstDSearchPath_atomicstring(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <DSearchPath.DSearchPath> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


