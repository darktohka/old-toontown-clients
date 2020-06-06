# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class ModelPool(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyorvKs:
            libpanda._inPkJyorvKs(self.this)
        

    
    def hasModel(filename):
        returnValue = libpanda._inPkJyo5EJQ(filename)
        return returnValue

    hasModel = staticmethod(hasModel)
    
    def verifyModel(filename):
        returnValue = libpanda._inPkJyogyNk(filename)
        return returnValue

    verifyModel = staticmethod(verifyModel)
    
    def loadModel(filename):
        returnValue = libpanda._inPkJyo0OhZ(filename)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    loadModel = staticmethod(loadModel)
    
    def addModel(filename, model):
        returnValue = libpanda._inPkJyoimu1(filename, model.this)
        return returnValue

    addModel = staticmethod(addModel)
    
    def releaseModel(filename):
        returnValue = libpanda._inPkJyoAecZ(filename)
        return returnValue

    releaseModel = staticmethod(releaseModel)
    
    def releaseAllModels():
        returnValue = libpanda._inPkJyo4zQY()
        return returnValue

    releaseAllModels = staticmethod(releaseAllModels)
    
    def garbageCollect():
        returnValue = libpanda._inPkJyoqWBO()
        return returnValue

    garbageCollect = staticmethod(garbageCollect)
    
    def listContents(out):
        returnValue = libpanda._inPkJyoGOv6(out.this)
        return returnValue

    listContents = staticmethod(listContents)

