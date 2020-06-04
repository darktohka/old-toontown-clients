# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggNode

class EggFilenameNode(EggNode.EggNode, FFIExternalObject.FFIExternalObject):
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
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMSE_b:
            libpandaegg._inPkAOMSE_b(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMMHF_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOM_1Ie(self.this, copy.this)
        returnObject = EggFilenameNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getDefaultExtension(self):
        returnValue = libpandaegg._inPkAOMXj7g(self.this)
        return returnValue

    
    def getFilename(self):
        returnValue = libpandaegg._inPkAOMXJxZ(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setFilename(self, filename):
        returnValue = libpandaegg._inPkAOMA0g1(self.this, filename.this)
        return returnValue

    
    def getFullpath(self):
        returnValue = libpandaegg._inPkAOM8Thq(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setFullpath(self, fullpath):
        returnValue = libpandaegg._inPkAOMI1PG(self.this, fullpath.this)
        return returnValue


