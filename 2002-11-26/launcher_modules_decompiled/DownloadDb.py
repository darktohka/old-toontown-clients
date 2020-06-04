# File: D (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class DownloadDb(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    StatusDecompressed = 2
    StatusComplete = 1
    StatusIncomplete = 0
    StatusExtracted = 3
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DownloadDb__overloaded_constructor(self):
        self.this = libpandaexpress._inP2KOd_aVY()
        self.userManagesMemory = 1

    
    def _DownloadDb__overloaded_constructor_ptrFilename_ptrFilename(self, serverFile, clientFile):
        self.this = libpandaexpress._inP2KOdW1U1(serverFile.this, clientFile.this)
        self.userManagesMemory = 1

    
    def _DownloadDb__overloaded_constructor_ptrRamfile_ptrFilename(self, serverFile, clientFile):
        self.this = libpandaexpress._inP2KOd5i5v(serverFile.this, clientFile.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOduZlN:
            libpandaexpress._inP2KOduZlN(self.this)
        

    
    def output(self, out):
        returnValue = libpandaexpress._inP2KOdQINq(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpandaexpress._inP2KOd0Ao5(self.this, out.this)
        return returnValue

    
    def writeVersionMap(self, out):
        returnValue = libpandaexpress._inP2KOdV2oK(self.this, out.this)
        return returnValue

    
    def writeClientDb(self, file):
        returnValue = libpandaexpress._inP2KOddnHR(self.this, file.this)
        return returnValue

    
    def writeServerDb(self, file):
        returnValue = libpandaexpress._inP2KOdsu0x(self.this, file.this)
        return returnValue

    
    def getClientNumMultifiles(self):
        returnValue = libpandaexpress._inP2KOde__n(self.this)
        return returnValue

    
    def getServerNumMultifiles(self):
        returnValue = libpandaexpress._inP2KOdWid5(self.this)
        return returnValue

    
    def getClientMultifileName(self, index):
        returnValue = libpandaexpress._inP2KOdC6SH(self.this, index)
        return returnValue

    
    def getServerMultifileName(self, index):
        returnValue = libpandaexpress._inP2KOdtjxY(self.this, index)
        return returnValue

    
    def getClientMultifileSize(self, mfname):
        returnValue = libpandaexpress._inP2KOdQDcT(self.this, mfname)
        return returnValue

    
    def setClientMultifileSize(self, mfname, size):
        returnValue = libpandaexpress._inP2KOd4_ms(self.this, mfname, size)
        return returnValue

    
    def setClientMultifileDeltaSize(self, mfname, size):
        returnValue = libpandaexpress._inP2KOdMBMJ(self.this, mfname, size)
        return returnValue

    
    def getServerMultifileSize(self, mfname):
        returnValue = libpandaexpress._inP2KOdMy7k(self.this, mfname)
        return returnValue

    
    def setServerMultifileSize(self, mfname, size):
        returnValue = libpandaexpress._inP2KOd86E_(self.this, mfname, size)
        return returnValue

    
    def getClientMultifilePhase(self, mfname):
        returnValue = libpandaexpress._inP2KOdxAuk(self.this, mfname)
        return returnValue

    
    def getServerMultifilePhase(self, mfname):
        returnValue = libpandaexpress._inP2KOd3HN2(self.this, mfname)
        return returnValue

    
    def setClientMultifileIncomplete(self, mfname):
        returnValue = libpandaexpress._inP2KOdcYJ4(self.this, mfname)
        return returnValue

    
    def setClientMultifileComplete(self, mfname):
        returnValue = libpandaexpress._inP2KOd0bjV(self.this, mfname)
        return returnValue

    
    def setClientMultifileDecompressed(self, mfname):
        returnValue = libpandaexpress._inP2KOdwEYN(self.this, mfname)
        return returnValue

    
    def setClientMultifileExtracted(self, mfname):
        returnValue = libpandaexpress._inP2KOdBgOD(self.this, mfname)
        return returnValue

    
    def getServerNumFiles(self, mfname):
        returnValue = libpandaexpress._inP2KOduRAy(self.this, mfname)
        return returnValue

    
    def getServerFileName(self, mfname, index):
        returnValue = libpandaexpress._inP2KOdkMf6(self.this, mfname, index)
        return returnValue

    
    def clientMultifileExists(self, mfname):
        returnValue = libpandaexpress._inP2KOdPqV1(self.this, mfname)
        return returnValue

    
    def clientMultifileComplete(self, mfname):
        returnValue = libpandaexpress._inP2KOdNg5P(self.this, mfname)
        return returnValue

    
    def clientMultifileDecompressed(self, mfname):
        returnValue = libpandaexpress._inP2KOdSEoI(self.this, mfname)
        return returnValue

    
    def clientMultifileExtracted(self, mfname):
        returnValue = libpandaexpress._inP2KOd9yC1(self.this, mfname)
        return returnValue

    
    def getClientMultifileHash(self, mfname):
        returnValue = libpandaexpress._inP2KOdzdCE(self.this, mfname)
        import HashVal
        returnObject = HashVal.HashVal(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setClientMultifileHash(self, mfname, val):
        returnValue = libpandaexpress._inP2KOdjMJh(self.this, mfname, val.this)
        return returnValue

    
    def getServerMultifileHash(self, mfname):
        returnValue = libpandaexpress._inP2KOd1YhV(self.this, mfname)
        import HashVal
        returnObject = HashVal.HashVal(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setServerMultifileHash(self, mfname, val):
        returnValue = libpandaexpress._inP2KOd6_my(self.this, mfname, val.this)
        return returnValue

    
    def deleteClientMultifile(self, mfname):
        returnValue = libpandaexpress._inP2KOdX638(self.this, mfname)
        return returnValue

    
    def addClientMultifile(self, serverMfname):
        returnValue = libpandaexpress._inP2KOdxOKg(self.this, serverMfname)
        return returnValue

    
    def expandClientMultifile(self, mfname):
        returnValue = libpandaexpress._inP2KOdrRXT(self.this, mfname)
        return returnValue

    
    def createNewServerDb(self):
        returnValue = libpandaexpress._inP2KOdvfrv(self.this)
        return returnValue

    
    def serverAddMultifile(self, mfname, phase, size, status):
        returnValue = libpandaexpress._inP2KOdjel4(self.this, mfname, phase, size, status)
        return returnValue

    
    def serverAddFile(self, mfname, fname):
        returnValue = libpandaexpress._inP2KOdQAQv(self.this, mfname, fname)
        return returnValue

    
    def _DownloadDb__overloaded_readDb_ptrDownloadDb_ptrFilename_bool(self, file, wantServerInfo):
        returnValue = libpandaexpress._inP2KOdfsdt(self.this, file.this, wantServerInfo)
        import Db
        returnObject = DownloadDb.Db(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _DownloadDb__overloaded_readDb_ptrDownloadDb_ptrRamfile_bool(self, file, wantServerInfo):
        returnValue = libpandaexpress._inP2KOdVwJj(self.this, file.this, wantServerInfo)
        import Db
        returnObject = DownloadDb.Db(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def writeDb(self, file, db, wantServerInfo):
        returnValue = libpandaexpress._inP2KOdN7K5(self.this, file.this, db.this, wantServerInfo)
        return returnValue

    
    def addVersion(self, name, hash, version):
        returnValue = libpandaexpress._inP2KOdm3aE(self.this, name.this, hash.this, version)
        return returnValue

    
    def insertNewVersion(self, name, hash):
        returnValue = libpandaexpress._inP2KOd15Zn(self.this, name.this, hash.this)
        return returnValue

    
    def hasVersion(self, name):
        returnValue = libpandaexpress._inP2KOdVFEb(self.this, name.this)
        return returnValue

    
    def getNumVersions(self, name):
        returnValue = libpandaexpress._inP2KOdbMUC(self.this, name.this)
        return returnValue

    
    def setNumVersions(self, name, numVersions):
        returnValue = libpandaexpress._inP2KOdLJWU(self.this, name.this, numVersions)
        return returnValue

    
    def getVersion(self, name, hash):
        returnValue = libpandaexpress._inP2KOdRTF2(self.this, name.this, hash.this)
        return returnValue

    
    def getHash(self, name, version):
        returnValue = libpandaexpress._inP2KOd6zuc(self.this, name.this, version)
        import HashVal
        returnObject = HashVal.HashVal(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DownloadDb__overloaded_constructor()
        elif numArgs == 2:
            import Ramfile
            import Filename
            if isinstance(_args[0], Ramfile.Ramfile):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    return self._DownloadDb__overloaded_constructor_ptrRamfile_ptrFilename(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            elif isinstance(_args[0], Filename.Filename):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    return self._DownloadDb__overloaded_constructor_ptrFilename_ptrFilename(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ramfile.Ramfile> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '

    
    def readDb(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import Ramfile
            import Filename
            if isinstance(_args[0], Ramfile.Ramfile):
                if isinstance(_args[1], types.IntType):
                    return self._DownloadDb__overloaded_readDb_ptrDownloadDb_ptrRamfile_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            elif isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._DownloadDb__overloaded_readDb_ptrDownloadDb_ptrFilename_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ramfile.Ramfile> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


