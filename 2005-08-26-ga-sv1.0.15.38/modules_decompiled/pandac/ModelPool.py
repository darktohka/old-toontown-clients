# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class ModelPool(FFIExternalObject.FFIExternalObject):
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
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoovKs:
            libpanda._inPnJyoovKs(self.this)
        

    
    def hasModel(filename):
        returnValue = libpanda._inPnJyo5EJQ(filename)
        return returnValue

    hasModel = staticmethod(hasModel)
    
    def verifyModel(filename):
        returnValue = libpanda._inPnJyohyNk(filename)
        return returnValue

    verifyModel = staticmethod(verifyModel)
    
    def loadModel(filename):
        returnValue = libpanda._inPnJyo0OhZ(filename)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    loadModel = staticmethod(loadModel)
    
    def addModel(filename, model):
        returnValue = libpanda._inPnJyojmu1(filename, model.this)
        return returnValue

    addModel = staticmethod(addModel)
    
    def releaseModel(filename):
        returnValue = libpanda._inPnJyoAecZ(filename)
        return returnValue

    releaseModel = staticmethod(releaseModel)
    
    def releaseAllModels():
        returnValue = libpanda._inPnJyo4zQY()
        return returnValue

    releaseAllModels = staticmethod(releaseAllModels)
    
    def garbageCollect():
        returnValue = libpanda._inPnJyoqWBO()
        return returnValue

    garbageCollect = staticmethod(garbageCollect)
    
    def listContents(out):
        returnValue = libpanda._inPnJyoBOv6(out.this)
        return returnValue

    listContents = staticmethod(listContents)
    
    def write(out):
        returnValue = libpanda._inPnJyopGeH(out.this)
        return returnValue

    write = staticmethod(write)

