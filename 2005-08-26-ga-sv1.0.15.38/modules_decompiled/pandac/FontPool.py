# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class FontPool(FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPpUk_sGXl:
            libpanda._inPpUk_sGXl(self.this)
        

    
    def hasFont(filename):
        returnValue = libpanda._inPpUk_x__8(filename)
        return returnValue

    hasFont = staticmethod(hasFont)
    
    def verifyFont(filename):
        returnValue = libpanda._inPpUk_E_Sp(filename)
        return returnValue

    verifyFont = staticmethod(verifyFont)
    
    def loadFont(filename):
        returnValue = libpanda._inPpUk_8KSz(filename)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    loadFont = staticmethod(loadFont)
    
    def addFont(filename, font):
        returnValue = libpanda._inPpUk_Wzk8(filename, font.this)
        return returnValue

    addFont = staticmethod(addFont)
    
    def releaseFont(filename):
        returnValue = libpanda._inPpUk_Jw6N(filename)
        return returnValue

    releaseFont = staticmethod(releaseFont)
    
    def releaseAllFonts():
        returnValue = libpanda._inPpUk_xfGL()
        return returnValue

    releaseAllFonts = staticmethod(releaseAllFonts)
    
    def garbageCollect():
        returnValue = libpanda._inPpUk_c8Aj()
        return returnValue

    garbageCollect = staticmethod(garbageCollect)
    
    def listContents(out):
        returnValue = libpanda._inPpUk_UKZ4(out.this)
        return returnValue

    listContents = staticmethod(listContents)
    
    def write(out):
        returnValue = libpanda._inPpUk_V6yK(out.this)
        return returnValue

    write = staticmethod(write)

