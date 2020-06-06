# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class PGTop(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPVvim0dnl(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPVvimZr4x()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setMouseWatcher(self, watcher):
        returnValue = libpanda._inPVvim7YJ9(self.this, watcher.this)
        return returnValue

    
    def getMouseWatcher(self):
        returnValue = libpanda._inPVvimlICk(self.this)
        import MouseWatcher
        returnObject = MouseWatcher.MouseWatcher(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setStartSort(self, startSort):
        returnValue = libpanda._inPVvimiqSM(self.this, startSort)
        return returnValue

    
    def getStartSort(self):
        returnValue = libpanda._inPVvimyCvK(self.this)
        return returnValue


