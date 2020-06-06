# File: P (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class Patchfile(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Patchfile__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtYIfo()
        self.userManagesMemory = 1

    
    def _Patchfile__overloaded_constructor_ptrBuffer(self, buffer):
        self.this = libpandaexpress._inPKoxthsa6(buffer.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtE1so:
            libpandaexpress._inPKoxtE1so(self.this)
        

    
    def build(self, fileOrig, fileNew, patchName):
        returnValue = libpandaexpress._inPKoxtH5YG(self.this, fileOrig.this, fileNew.this, patchName.this)
        return returnValue

    
    def readHeader(self, patchFile):
        returnValue = libpandaexpress._inPKoxtDEDi(self.this, patchFile.this)
        return returnValue

    
    def initiate(self, patchFile, file):
        returnValue = libpandaexpress._inPKoxtatBi(self.this, patchFile.this, file.this)
        return returnValue

    
    def run(self):
        returnValue = libpandaexpress._inPKoxtAkYw(self.this)
        return returnValue

    
    def apply(self, patchFile, file):
        returnValue = libpandaexpress._inPKoxtrMgQ(self.this, patchFile.this, file.this)
        return returnValue

    
    def getProgress(self):
        returnValue = libpandaexpress._inPKoxtKJeX(self.this)
        return returnValue

    
    def setFootprintLength(self, length):
        returnValue = libpandaexpress._inPKoxtbc1x(self.this, length)
        return returnValue

    
    def getFootprintLength(self):
        returnValue = libpandaexpress._inPKoxtAsYn(self.this)
        return returnValue

    
    def resetFootprintLength(self):
        returnValue = libpandaexpress._inPKoxtlU88(self.this)
        return returnValue

    
    def hasSourceHash(self):
        returnValue = libpandaexpress._inPKoxtMoom(self.this)
        return returnValue

    
    def getSourceHash(self):
        returnValue = libpandaexpress._inPKoxt4eHg(self.this)
        import HashVal
        returnObject = HashVal.HashVal(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getResultHash(self):
        returnValue = libpandaexpress._inPKoxtmkYw(self.this)
        import HashVal
        returnObject = HashVal.HashVal(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Patchfile__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._Patchfile__overloaded_constructor_ptrBuffer(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


