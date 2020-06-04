# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggObject

class EggBinMaker(EggObject.EggObject, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
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
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOM_kc_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def makeBins(self, rootGroup):
        returnValue = libpandaegg._inPkAOM8q6p(self.this, rootGroup.this)
        return returnValue

    
    def getBinNumber(self, node):
        returnValue = libpandaegg._inPkAOM_qCk(self.this, node.this)
        return returnValue

    
    def sortsLess(self, binNumber, a, b):
        returnValue = libpandaegg._inPkAOMZCvy(self.this, binNumber, a.this, b.this)
        return returnValue

    
    def collapseGroup(self, group, binNumber):
        returnValue = libpandaegg._inPkAOMGhQi(self.this, group.this, binNumber)
        return returnValue

    
    def getBinName(self, binNumber):
        returnValue = libpandaegg._inPkAOMsEA6(self.this, binNumber)
        return returnValue


