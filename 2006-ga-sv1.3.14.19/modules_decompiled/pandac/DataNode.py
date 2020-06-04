# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class DataNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPSLSebRQs(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPSLSeksRt:
            libpanda._inPSLSeksRt(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPSLSePSzN()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def writeInputs(self, out):
        returnValue = libpanda._inPSLSe4fqQ(self.this, out.this)
        return returnValue

    
    def writeOutputs(self, out):
        returnValue = libpanda._inPSLSeUk5z(self.this, out.this)
        return returnValue

    
    def writeConnections(self, out):
        returnValue = libpanda._inPSLSeUqT4(self.this, out.this)
        return returnValue


