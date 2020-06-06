# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount

class MouseWatcherGroup(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
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
        if libpanda and libpanda._inPziw5SttB:
            libpanda._inPziw5SttB(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPziw52_jo()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def addRegion(self, region):
        returnValue = libpanda._inPziw5xUMA(self.this, region.this)
        return returnValue

    
    def hasRegion(self, region):
        returnValue = libpanda._inPziw575tC(self.this, region.this)
        return returnValue

    
    def removeRegion(self, region):
        returnValue = libpanda._inPziw5nY6C(self.this, region.this)
        return returnValue

    
    def findRegion(self, name):
        returnValue = libpanda._inPziw52SzS(self.this, name)
        import MouseWatcherRegion
        returnObject = MouseWatcherRegion.MouseWatcherRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearRegions(self):
        returnValue = libpanda._inPziw58D_y(self.this)
        return returnValue

    
    def upcastToReferenceCount(self):
        returnValue = libpanda._inPziw5XWnS(self.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject


