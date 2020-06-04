# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RenderAttrib

class TextureAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
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
        if libpanda and libpanda._inPnJyo93vi:
            libpanda._inPnJyo93vi(self.this)
        

    
    def _TextureAttrib__overloaded_make():
        returnValue = libpanda._inPnJyo92CO()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TextureAttrib__overloaded_make = staticmethod(_TextureAttrib__overloaded_make)
    
    def _TextureAttrib__overloaded_make_ptrTexture(tex):
        returnValue = libpanda._inPnJyo0rhz(tex.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TextureAttrib__overloaded_make_ptrTexture = staticmethod(_TextureAttrib__overloaded_make_ptrTexture)
    
    def makeOff():
        returnValue = libpanda._inPnJyoHcOV()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeOff = staticmethod(makeOff)
    
    def makeAllOff():
        returnValue = libpanda._inPnJyoiAmG()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeAllOff = staticmethod(makeAllOff)
    
    def getClassType():
        returnValue = libpanda._inPnJyopGJm()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isOff(self):
        returnValue = libpanda._inPnJyoSDxK(self.this)
        return returnValue

    
    def getTexture(self):
        returnValue = libpanda._inPnJyoa2tR(self.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumOnStages(self):
        returnValue = libpanda._inPnJyoPts5(self.this)
        return returnValue

    
    def getOnStage(self, n):
        returnValue = libpanda._inPnJyoxAIF(self.this, n)
        import TextureStage
        returnObject = TextureStage.TextureStage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasOnStage(self, stage):
        returnValue = libpanda._inPnJyoJ52n(self.this, stage.this)
        return returnValue

    
    def getOnTexture(self, stage):
        returnValue = libpanda._inPnJyoNSWS(self.this, stage.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumOffStages(self):
        returnValue = libpanda._inPnJyoRCki(self.this)
        return returnValue

    
    def getOffStage(self, n):
        returnValue = libpanda._inPnJyofsjm(self.this, n)
        import TextureStage
        returnObject = TextureStage.TextureStage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasOffStage(self, stage):
        returnValue = libpanda._inPnJyoIoIC(self.this, stage.this)
        return returnValue

    
    def hasAllOff(self):
        returnValue = libpanda._inPnJyoQEFa(self.this)
        return returnValue

    
    def isIdentity(self):
        returnValue = libpanda._inPnJyoJvNO(self.this)
        return returnValue

    
    def addOnStage(self, stage, tex):
        returnValue = libpanda._inPnJyoCbpG(self.this, stage.this, tex.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeOnStage(self, stage):
        returnValue = libpanda._inPnJyopW4_(self.this, stage.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def addOffStage(self, stage):
        returnValue = libpanda._inPnJyo7rdo(self.this, stage.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeOffStage(self, stage):
        returnValue = libpanda._inPnJyopBrg(self.this, stage.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def unifyTextureStages(self, stage):
        returnValue = libpanda._inPnJyo3f6O(self.this, stage.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return TextureAttrib._TextureAttrib__overloaded_make(*_args)
        elif numArgs == 1:
            return TextureAttrib._TextureAttrib__overloaded_make_ptrTexture(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    make = staticmethod(make)

