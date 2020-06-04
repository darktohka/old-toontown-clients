# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class GraphicsPipeSelection(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
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
        returnValue = libpanda._inPO9cYa86m()
        returnObject = GraphicsPipeSelection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalPtr = staticmethod(getGlobalPtr)
    
    def getNumPipeTypes(self):
        returnValue = libpanda._inPO9cYkGJV(self.this)
        return returnValue

    
    def getPipeType(self, n):
        returnValue = libpanda._inPO9cYdWon(self.this, n)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def printPipeTypes(self):
        returnValue = libpanda._inPO9cYKhch(self.this)
        return returnValue

    
    def makePipe(self, type):
        returnValue = libpanda._inPO9cYgtWV(self.this, type.this)
        import GraphicsPipe
        returnObject = GraphicsPipe.GraphicsPipe(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def makeDefaultPipe(self):
        returnValue = libpanda._inPO9cYJlGM(self.this)
        import GraphicsPipe
        returnObject = GraphicsPipe.GraphicsPipe(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumAuxModules(self):
        returnValue = libpanda._inPO9cYtQ2r(self.this)
        return returnValue

    
    def loadAuxModules(self):
        returnValue = libpanda._inPO9cY4_4n(self.this)
        return returnValue


