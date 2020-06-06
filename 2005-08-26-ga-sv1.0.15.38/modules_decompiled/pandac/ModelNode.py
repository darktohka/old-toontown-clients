# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class ModelNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    PTNet = 2
    PTLocal = 1
    PTNone = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyoUtdT(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoT7l3:
            libpanda._inPnJyoT7l3(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyoYGvp()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setPreserveTransform(self, preserveTransform):
        returnValue = libpanda._inPnJyodAt4(self.this, preserveTransform)
        return returnValue

    
    def getPreserveTransform(self):
        returnValue = libpanda._inPnJyoEjAF(self.this)
        return returnValue


