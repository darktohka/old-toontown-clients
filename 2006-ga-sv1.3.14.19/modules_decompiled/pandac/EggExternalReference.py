# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggFilenameNode

class EggExternalReference(EggFilenameNode.EggFilenameNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggExternalReference__overloaded_constructor_ptrConstEggExternalReference(self, copy):
        self.this = libpandaegg._inPkAOM_0_W(copy.this)
        self.userManagesMemory = 1

    
    def _EggExternalReference__overloaded_constructor_atomicstring_atomicstring(self, nodeName, filename):
        self.this = libpandaegg._inPkAOM8ySO(nodeName, filename)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMqNhj:
            libpandaegg._inPkAOMqNhj(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMp9UM()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMmtLn(self.this, copy.this)
        returnObject = EggExternalReference(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggExternalReference__overloaded_constructor_ptrConstEggExternalReference(*_args)
        elif numArgs == 2:
            return self._EggExternalReference__overloaded_constructor_atomicstring_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


