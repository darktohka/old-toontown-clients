# File: P (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class Patchfile(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Patchfile__overloaded_constructor(self):
        self.this = libpandaexpress._inPJoxtZIfo()
        self.userManagesMemory = 1

    
    def _Patchfile__overloaded_constructor_ptrBuffer(self, buffer):
        self.this = libpandaexpress._inPJoxtmsa6(buffer.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxt7yso:
            libpandaexpress._inPJoxt7yso(self.this)
        

    
    def build(self, fileOrig, fileNew, patchName):
        returnValue = libpandaexpress._inPJoxtH5YG(self.this, fileOrig.this, fileNew.this, patchName.this)
        return returnValue

    
    def readHeader(self, patchFile):
        returnValue = libpandaexpress._inPJoxtEEDi(self.this, patchFile.this)
        return returnValue

    
    def initiate(self, patchFile, file):
        returnValue = libpandaexpress._inPJoxtbtBi(self.this, patchFile.this, file.this)
        return returnValue

    
    def run(self):
        returnValue = libpandaexpress._inPJoxtDkYw(self.this)
        return returnValue

    
    def apply(self, patchFile, file):
        returnValue = libpandaexpress._inPJoxtrMgQ(self.this, patchFile.this, file.this)
        return returnValue

    
    def getProgress(self):
        returnValue = libpandaexpress._inPJoxtKJeX(self.this)
        return returnValue

    
    def setFootprintLength(self, length):
        returnValue = libpandaexpress._inPJoxtYc1x(self.this, length)
        return returnValue

    
    def getFootprintLength(self):
        returnValue = libpandaexpress._inPJoxtPsYn(self.this)
        return returnValue

    
    def resetFootprintLength(self):
        returnValue = libpandaexpress._inPJoxtqU88(self.this)
        return returnValue

    
    def hasSourceHash(self):
        returnValue = libpandaexpress._inPJoxtNoom(self.this)
        return returnValue

    
    def getSourceHash(self):
        returnValue = libpandaexpress._inPJoxt5eHg(self.this)
        import HashVal
        returnObject = HashVal.HashVal(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getResultHash(self):
        returnValue = libpandaexpress._inPJoxthkYw(self.this)
        import HashVal
        returnObject = HashVal.HashVal(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Patchfile__overloaded_constructor()
        elif numArgs == 1:
            import Buffer
            if isinstance(_args[0], Buffer.Buffer):
                return self._Patchfile__overloaded_constructor_ptrBuffer(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Buffer.Buffer> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


