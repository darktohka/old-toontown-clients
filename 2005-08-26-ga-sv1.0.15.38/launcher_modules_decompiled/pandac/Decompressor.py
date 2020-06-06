# File: D (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class Decompressor(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaexpress._inP2KOdB4PE()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdJ0Mb:
            libpandaexpress._inP2KOdJ0Mb(self.this)
        

    
    def _Decompressor__overloaded_initiate_ptrDecompressor_ptrConstFilename(self, sourceFile):
        returnValue = libpandaexpress._inP2KOdw6VS(self.this, sourceFile.this)
        return returnValue

    
    def _Decompressor__overloaded_initiate_ptrDecompressor_ptrConstFilename_ptrConstFilename(self, sourceFile, destFile):
        returnValue = libpandaexpress._inP2KOdP1ck(self.this, sourceFile.this, destFile.this)
        return returnValue

    
    def run(self):
        returnValue = libpandaexpress._inP2KOd4YBi(self.this)
        return returnValue

    
    def _Decompressor__overloaded_decompress_ptrDecompressor_ptrConstFilename(self, sourceFile):
        returnValue = libpandaexpress._inP2KOdHZkY(self.this, sourceFile.this)
        return returnValue

    
    def _Decompressor__overloaded_decompress_ptrDecompressor_ptrRamfile(self, sourceAndDestFile):
        returnValue = libpandaexpress._inP2KOdDUun(self.this, sourceAndDestFile.this)
        return returnValue

    
    def getProgress(self):
        returnValue = libpandaexpress._inP2KOdujks(self.this)
        return returnValue

    
    def initiate(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Decompressor__overloaded_initiate_ptrDecompressor_ptrConstFilename(*_args)
        elif numArgs == 2:
            return self._Decompressor__overloaded_initiate_ptrDecompressor_ptrConstFilename_ptrConstFilename(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def decompress(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ramfile
            if isinstance(_args[0], Ramfile.Ramfile):
                return self._Decompressor__overloaded_decompress_ptrDecompressor_ptrRamfile(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._Decompressor__overloaded_decompress_ptrDecompressor_ptrConstFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Ramfile.Ramfile> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


