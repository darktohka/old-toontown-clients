# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class CullBinManager(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    BTUnsorted = 1
    BTFrontToBack = 4
    BTFixed = 5
    BTStateSorted = 2
    BTBackToFront = 3
    BTInvalid = 0
    
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
        

    
    def getGlobalPtr():
        returnValue = libpanda._inPnJyo_lYP()
        returnObject = CullBinManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalPtr = staticmethod(getGlobalPtr)
    
    def addBin(self, name, type, sort):
        returnValue = libpanda._inPnJyo3XHI(self.this, name, type, sort)
        return returnValue

    
    def removeBin(self, binIndex):
        returnValue = libpanda._inPnJyobswe(self.this, binIndex)
        return returnValue

    
    def getNumBins(self):
        returnValue = libpanda._inPnJyoj_LX(self.this)
        return returnValue

    
    def getBin(self, n):
        returnValue = libpanda._inPnJyooytP(self.this, n)
        return returnValue

    
    def findBin(self, name):
        returnValue = libpanda._inPnJyo5zCj(self.this, name)
        return returnValue

    
    def getBinName(self, binIndex):
        returnValue = libpanda._inPnJyoo76W(self.this, binIndex)
        return returnValue

    
    def getBinType(self, binIndex):
        returnValue = libpanda._inPnJyoxiQg(self.this, binIndex)
        return returnValue

    
    def getBinSort(self, binIndex):
        returnValue = libpanda._inPnJyoJVUe(self.this, binIndex)
        return returnValue

    
    def setBinSort(self, binIndex, sort):
        returnValue = libpanda._inPnJyoU8RN(self.this, binIndex, sort)
        return returnValue


