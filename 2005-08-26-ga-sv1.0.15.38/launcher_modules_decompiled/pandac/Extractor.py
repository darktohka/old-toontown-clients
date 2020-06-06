# File: E (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class Extractor(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaexpress._inP2KOdUQPe()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdo_o6:
            libpandaexpress._inP2KOdo_o6(self.this)
        

    
    def setMultifile(self, multifileName):
        returnValue = libpandaexpress._inP2KOdszJD(self.this, multifileName.this)
        return returnValue

    
    def setExtractDir(self, extractDir):
        returnValue = libpandaexpress._inP2KOdbwYp(self.this, extractDir.this)
        return returnValue

    
    def reset(self):
        returnValue = libpandaexpress._inP2KOdZFSE(self.this)
        return returnValue

    
    def requestSubfile(self, subfileName):
        returnValue = libpandaexpress._inP2KOd22R_(self.this, subfileName.this)
        return returnValue

    
    def requestAllSubfiles(self):
        returnValue = libpandaexpress._inP2KOdRYjW(self.this)
        return returnValue

    
    def step(self):
        returnValue = libpandaexpress._inP2KOdCcut(self.this)
        return returnValue

    
    def getProgress(self):
        returnValue = libpandaexpress._inP2KOdhtp3(self.this)
        return returnValue

    
    def run(self):
        returnValue = libpandaexpress._inP2KOdaBlQ(self.this)
        return returnValue


