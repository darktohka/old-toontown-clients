# File: D (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class Downloader(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpandaexpress._inP2KOdyCaY()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdUglw:
            libpandaexpress._inP2KOdUglw(self.this)
        

    
    def connectToServerByProxy(self, proxy, serverName):
        returnValue = libpandaexpress._inP2KOd5LC5(self.this, proxy.this, serverName)
        return returnValue

    
    def _Downloader__overloaded_connectToServer_ptrDownloader_atomicstring_unsignedint(self, name, port):
        returnValue = libpandaexpress._inP2KOdi9s1(self.this, name, port)
        return returnValue

    
    def _Downloader__overloaded_connectToServer_ptrDownloader_atomicstring(self, name):
        returnValue = libpandaexpress._inP2KOdsLDw(self.this, name)
        return returnValue

    
    def disconnectFromServer(self):
        returnValue = libpandaexpress._inP2KOdQ45A(self.this)
        return returnValue

    
    def _Downloader__overloaded_initiate_ptrDownloader_atomicstring(self, fileName):
        returnValue = libpandaexpress._inP2KOdF_c4(self.this, fileName)
        return returnValue

    
    def _Downloader__overloaded_initiate_ptrDownloader_atomicstring_ptrFilename(self, fileName, fileDest):
        returnValue = libpandaexpress._inP2KOdHfBB(self.this, fileName, fileDest.this)
        return returnValue

    
    def _Downloader__overloaded_initiate_ptrDownloader_atomicstring_ptrFilename_int_int_int_bool(self, fileName, fileDest, firstByte, lastByte, totalBytes, partialContent):
        returnValue = libpandaexpress._inP2KOdNlfS(self.this, fileName, fileDest.this, firstByte, lastByte, totalBytes, partialContent)
        return returnValue

    
    def _Downloader__overloaded_initiate_ptrDownloader_atomicstring_ptrFilename_int_int_int(self, fileName, fileDest, firstByte, lastByte, totalBytes):
        returnValue = libpandaexpress._inP2KOd0CGC(self.this, fileName, fileDest.this, firstByte, lastByte, totalBytes)
        return returnValue

    
    def getFileSize(self):
        returnValue = libpandaexpress._inP2KOdeKmN(self.this)
        return returnValue

    
    def run(self):
        returnValue = libpandaexpress._inP2KOdFn_I(self.this)
        return returnValue

    
    def getRamfile(self, rfile):
        returnValue = libpandaexpress._inP2KOdmC2A(self.this, rfile.this)
        return returnValue

    
    def setFrequency(self, frequency):
        returnValue = libpandaexpress._inP2KOdeu_F(self.this, frequency)
        return returnValue

    
    def getFrequency(self):
        returnValue = libpandaexpress._inP2KOd8_Rx(self.this)
        return returnValue

    
    def setByteRate(self, bytes):
        returnValue = libpandaexpress._inP2KOd0MBp(self.this, bytes)
        return returnValue

    
    def getByteRate(self):
        returnValue = libpandaexpress._inP2KOdZ_TU(self.this)
        return returnValue

    
    def setDiskWriteFrequency(self, frequency):
        returnValue = libpandaexpress._inP2KOd0__M(self.this, frequency)
        return returnValue

    
    def getDiskWriteFrequency(self):
        returnValue = libpandaexpress._inP2KOdJfp8(self.this)
        return returnValue

    
    def getBytesWritten(self):
        returnValue = libpandaexpress._inP2KOdknv1(self.this)
        return returnValue

    
    def getBytesRequested(self):
        returnValue = libpandaexpress._inP2KOddSje(self.this)
        return returnValue

    
    def getBytesPerSecond(self):
        returnValue = libpandaexpress._inP2KOdtSav(self.this)
        return returnValue

    
    def cleanup(self):
        returnValue = libpandaexpress._inP2KOdDv3B(self.this)
        return returnValue

    
    def initiate(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Downloader__overloaded_initiate_ptrDownloader_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    return self._Downloader__overloaded_initiate_ptrDownloader_atomicstring_ptrFilename(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 5:
            if isinstance(_args[0], types.StringType):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    if isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.IntType):
                                return self._Downloader__overloaded_initiate_ptrDownloader_atomicstring_ptrFilename_int_int_int(_args[0], _args[1], _args[2], _args[3], _args[4])
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 6:
            if isinstance(_args[0], types.StringType):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    if isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.IntType):
                                    return self._Downloader__overloaded_initiate_ptrDownloader_atomicstring_ptrFilename_int_int_int_bool(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <types.IntType> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 5 6 '

    
    def connectToServer(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Downloader__overloaded_connectToServer_ptrDownloader_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._Downloader__overloaded_connectToServer_ptrDownloader_atomicstring_unsignedint(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


