# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class TextureCollection(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _TextureCollection__overloaded_constructor(self):
        self.this = libpanda._inPkJyotz_w()
        self.userManagesMemory = 1

    
    def _TextureCollection__overloaded_constructor_ptrConstTextureCollection(self, copy):
        self.this = libpanda._inPkJyoH2Wq(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyoavHf:
            libpanda._inPkJyoavHf(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPkJyovUB_(self.this, copy.this)
        returnObject = TextureCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def addTexture(self, nodeTexture):
        returnValue = libpanda._inPkJyorcTz(self.this, nodeTexture.this)
        return returnValue

    
    def removeTexture(self, nodeTexture):
        returnValue = libpanda._inPkJyo1SuY(self.this, nodeTexture.this)
        return returnValue

    
    def addTexturesFrom(self, other):
        returnValue = libpanda._inPkJyoAW2_(self.this, other.this)
        return returnValue

    
    def removeTexturesFrom(self, other):
        returnValue = libpanda._inPkJyoubPS(self.this, other.this)
        return returnValue

    
    def removeDuplicateTextures(self):
        returnValue = libpanda._inPkJyoKXB3(self.this)
        return returnValue

    
    def hasTexture(self, texture):
        returnValue = libpanda._inPkJyoeRIZ(self.this, texture.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPkJyof_8F(self.this)
        return returnValue

    
    def findTexture(self, name):
        returnValue = libpanda._inPkJyousRb(self.this, name)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumTextures(self):
        returnValue = libpanda._inPkJyorq1E(self.this)
        return returnValue

    
    def getTexture(self, index):
        returnValue = libpanda._inPkJyoWzkn(self.this, index)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def __getitem__(self, index):
        returnValue = libpanda._inPkJyoeP4T(self.this, index)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def output(self, out):
        returnValue = libpanda._inPkJyo3Sw8(self.this, out.this)
        return returnValue

    
    def _TextureCollection__overloaded_write_ptrConstTextureCollection_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPkJyofS_c(self.this, out.this, indentLevel)
        return returnValue

    
    def _TextureCollection__overloaded_write_ptrConstTextureCollection_ptrOstream(self, out):
        returnValue = libpanda._inPkJyokwgN(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TextureCollection__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], TextureCollection):
                return self._TextureCollection__overloaded_constructor_ptrConstTextureCollection(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <TextureCollection> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._TextureCollection__overloaded_write_ptrConstTextureCollection_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._TextureCollection__overloaded_write_ptrConstTextureCollection_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


