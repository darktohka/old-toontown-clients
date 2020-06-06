# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggNode

class EggAnimData(EggNode.EggNode, FFIExternalObject.FFIExternalObject):
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
        if libpandaegg and libpandaegg._inPkAOMnNOS:
            libpandaegg._inPkAOMnNOS(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOM25FJ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMZZeu(self.this, copy.this)
        returnObject = EggAnimData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setFps(self, type):
        returnValue = libpandaegg._inPkAOMgqhB(self.this, type)
        return returnValue

    
    def clearFps(self):
        returnValue = libpandaegg._inPkAOMKf9p(self.this)
        return returnValue

    
    def hasFps(self):
        returnValue = libpandaegg._inPkAOMJAtY(self.this)
        return returnValue

    
    def getFps(self):
        returnValue = libpandaegg._inPkAOMRAYV(self.this)
        return returnValue

    
    def clearData(self):
        returnValue = libpandaegg._inPkAOMML2y(self.this)
        return returnValue

    
    def addData(self, value):
        returnValue = libpandaegg._inPkAOMAf6I(self.this, value)
        return returnValue

    
    def getSize(self):
        returnValue = libpandaegg._inPkAOMDiDs(self.this)
        return returnValue

    
    def getData(self):
        returnValue = libpandaegg._inPkAOMd_fL(self.this)
        import PTADouble
        returnObject = PTADouble.PTADouble(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setData(self, data):
        returnValue = libpandaegg._inPkAOM3VXr(self.this, data.this)
        return returnValue

    
    def quantize(self, quantum):
        returnValue = libpandaegg._inPkAOMbri2(self.this, quantum)
        return returnValue


