# File: M (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PandaNode

class MarginManager(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libtoontown._inPPj7bShwo()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libtoontown._inPPj7b7u8L()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def addGridCell(self, x, y, screenLeft, screenRight, screenBottom, screenTop):
        returnValue = libtoontown._inPPj7bP7jl(self.this, x, y, screenLeft, screenRight, screenBottom, screenTop)
        return returnValue

    
    def addCell(self, left, right, bottom, top):
        returnValue = libtoontown._inPPj7bXEvz(self.this, left, right, bottom, top)
        return returnValue

    
    def setCellAvailable(self, cellIndex, available):
        returnValue = libtoontown._inPPj7bu2yR(self.this, cellIndex, available)
        return returnValue

    
    def getCellAvailable(self, cellIndex):
        returnValue = libtoontown._inPPj7b0WH7(self.this, cellIndex)
        return returnValue


