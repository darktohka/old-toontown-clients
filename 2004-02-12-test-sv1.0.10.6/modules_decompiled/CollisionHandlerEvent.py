# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionHandler

class CollisionHandlerEvent(CollisionHandler.CollisionHandler, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPHwcaFTvw()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaT4lv:
            libpanda._inPHwcaT4lv(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaXcqn()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def clearInPatterns(self):
        returnValue = libpanda._inPHwcaS2HY(self.this)
        return returnValue

    
    def addInPattern(self, inPattern):
        returnValue = libpanda._inPHwca_2Bj(self.this, inPattern)
        return returnValue

    
    def setInPattern(self, inPattern):
        returnValue = libpanda._inPHwca7Szo(self.this, inPattern)
        return returnValue

    
    def getNumInPatterns(self):
        returnValue = libpanda._inPHwcac0hf(self.this)
        return returnValue

    
    def getInPattern(self, n):
        returnValue = libpanda._inPHwcalCzc(self.this, n)
        return returnValue

    
    def clearAgainPatterns(self):
        returnValue = libpanda._inPHwcac7gg(self.this)
        return returnValue

    
    def addAgainPattern(self, againPattern):
        returnValue = libpanda._inPHwcarwhr(self.this, againPattern)
        return returnValue

    
    def setAgainPattern(self, againPattern):
        returnValue = libpanda._inPHwcaHYTx(self.this, againPattern)
        return returnValue

    
    def getNumAgainPatterns(self):
        returnValue = libpanda._inPHwcasi_4(self.this)
        return returnValue

    
    def getAgainPattern(self, n):
        returnValue = libpanda._inPHwcaBNwh(self.this, n)
        return returnValue

    
    def clearOutPatterns(self):
        returnValue = libpanda._inPHwcaiRM0(self.this)
        return returnValue

    
    def addOutPattern(self, outPattern):
        returnValue = libpanda._inPHwcaKN0g(self.this, outPattern)
        return returnValue

    
    def setOutPattern(self, outPattern):
        returnValue = libpanda._inPHwcakKnm(self.this, outPattern)
        return returnValue

    
    def getNumOutPatterns(self):
        returnValue = libpanda._inPHwcaClvc(self.this)
        return returnValue

    
    def getOutPattern(self, n):
        returnValue = libpanda._inPHwcaJFH_(self.this, n)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPHwcavtnS(self.this)
        return returnValue


