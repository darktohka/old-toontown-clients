# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class TextureCollection(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _TextureCollection__overloaded_constructor(self):
        self.this = libpanda._inPnJyosz_w()
        self.userManagesMemory = 1

    
    def _TextureCollection__overloaded_constructor_ptrConstTextureCollection(self, copy):
        self.this = libpanda._inPnJyoG2Wq(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoavHf:
            libpanda._inPnJyoavHf(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPnJyouUB_(self.this, copy.this)
        returnObject = TextureCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def addTexture(self, nodeTexture):
        returnValue = libpanda._inPnJyoqcTz(self.this, nodeTexture.this)
        return returnValue

    
    def removeTexture(self, nodeTexture):
        returnValue = libpanda._inPnJyo1SuY(self.this, nodeTexture.this)
        return returnValue

    
    def addTexturesFrom(self, other):
        returnValue = libpanda._inPnJyoBW2_(self.this, other.this)
        return returnValue

    
    def removeTexturesFrom(self, other):
        returnValue = libpanda._inPnJyoubPS(self.this, other.this)
        return returnValue

    
    def removeDuplicateTextures(self):
        returnValue = libpanda._inPnJyoJXB3(self.this)
        return returnValue

    
    def hasTexture(self, texture):
        returnValue = libpanda._inPnJyoeRIZ(self.this, texture.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPnJyof_8F(self.this)
        return returnValue

    
    def findTexture(self, name):
        returnValue = libpanda._inPnJyousRb(self.this, name)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumTextures(self):
        returnValue = libpanda._inPnJyorq1E(self.this)
        return returnValue

    
    def getTexture(self, index):
        returnValue = libpanda._inPnJyoXzkn(self.this, index)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def __getitem__(self, index):
        returnValue = libpanda._inPnJyoeP4T(self.this, index)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def output(self, out):
        returnValue = libpanda._inPnJyo2Sw8(self.this, out.this)
        return returnValue

    
    def _TextureCollection__overloaded_write_ptrConstTextureCollection_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPnJyofS_c(self.this, out.this, indentLevel)
        return returnValue

    
    def _TextureCollection__overloaded_write_ptrConstTextureCollection_ptrOstream(self, out):
        returnValue = libpanda._inPnJyokwgN(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TextureCollection__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._TextureCollection__overloaded_constructor_ptrConstTextureCollection(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextureCollection__overloaded_write_ptrConstTextureCollection_ptrOstream(*_args)
        elif numArgs == 2:
            return self._TextureCollection__overloaded_write_ptrConstTextureCollection_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


