# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class TexturePool(FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPMAKP8DhA:
            libpanda._inPMAKP8DhA(self.this)
        

    
    def hasTexture(filename):
        returnValue = libpanda._inPMAKP_aBv(filename)
        return returnValue

    hasTexture = staticmethod(hasTexture)
    
    def verifyTexture(filename):
        returnValue = libpanda._inPMAKPAZev(filename)
        return returnValue

    verifyTexture = staticmethod(verifyTexture)
    
    def _TexturePool__overloaded_loadTexture_atomicstring_atomicstring_int_int(filename, alphaFilename, primaryFileNumChannels, alphaFileChannel):
        returnValue = libpanda._inPMAKPhuDO(filename, alphaFilename, primaryFileNumChannels, alphaFileChannel)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TexturePool__overloaded_loadTexture_atomicstring_atomicstring_int_int = staticmethod(_TexturePool__overloaded_loadTexture_atomicstring_atomicstring_int_int)
    
    def _TexturePool__overloaded_loadTexture_atomicstring_atomicstring_int(filename, alphaFilename, primaryFileNumChannels):
        returnValue = libpanda._inPMAKPoc5Q(filename, alphaFilename, primaryFileNumChannels)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TexturePool__overloaded_loadTexture_atomicstring_atomicstring_int = staticmethod(_TexturePool__overloaded_loadTexture_atomicstring_atomicstring_int)
    
    def _TexturePool__overloaded_loadTexture_atomicstring_atomicstring(filename, alphaFilename):
        returnValue = libpanda._inPMAKPRDVS(filename, alphaFilename)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TexturePool__overloaded_loadTexture_atomicstring_atomicstring = staticmethod(_TexturePool__overloaded_loadTexture_atomicstring_atomicstring)
    
    def _TexturePool__overloaded_loadTexture_atomicstring_int(filename, primaryFileNumChannels):
        returnValue = libpanda._inPMAKPATdl(filename, primaryFileNumChannels)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TexturePool__overloaded_loadTexture_atomicstring_int = staticmethod(_TexturePool__overloaded_loadTexture_atomicstring_int)
    
    def _TexturePool__overloaded_loadTexture_atomicstring(filename):
        returnValue = libpanda._inPMAKPfj8J(filename)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _TexturePool__overloaded_loadTexture_atomicstring = staticmethod(_TexturePool__overloaded_loadTexture_atomicstring)
    
    def addTexture(texture):
        returnValue = libpanda._inPMAKPnyxl(texture.this)
        return returnValue

    addTexture = staticmethod(addTexture)
    
    def releaseTexture(texture):
        returnValue = libpanda._inPMAKPp_Lr(texture.this)
        return returnValue

    releaseTexture = staticmethod(releaseTexture)
    
    def releaseAllTextures():
        returnValue = libpanda._inPMAKPA290()
        return returnValue

    releaseAllTextures = staticmethod(releaseAllTextures)
    
    def garbageCollect():
        returnValue = libpanda._inPMAKPfx9C()
        return returnValue

    garbageCollect = staticmethod(garbageCollect)
    
    def listContents(out):
        returnValue = libpanda._inPMAKPbY3s(out.this)
        return returnValue

    listContents = staticmethod(listContents)
    
    def setFakeTextureImage(filename):
        returnValue = libpanda._inPMAKP9QHr(filename)
        return returnValue

    setFakeTextureImage = staticmethod(setFakeTextureImage)
    
    def clearFakeTextureImage():
        returnValue = libpanda._inPMAKPF81s()
        return returnValue

    clearFakeTextureImage = staticmethod(clearFakeTextureImage)
    
    def hasFakeTextureImage():
        returnValue = libpanda._inPMAKPXpQC()
        return returnValue

    hasFakeTextureImage = staticmethod(hasFakeTextureImage)
    
    def getFakeTextureImage():
        returnValue = libpanda._inPMAKPOn7_()
        return returnValue

    getFakeTextureImage = staticmethod(getFakeTextureImage)
    
    def write(out):
        returnValue = libpanda._inPMAKPA_aL(out.this)
        return returnValue

    write = staticmethod(write)
    
    def loadTexture(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return TexturePool._TexturePool__overloaded_loadTexture_atomicstring(*_args)
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return TexturePool._TexturePool__overloaded_loadTexture_atomicstring_int(*_args)
                
                if isinstance(_args[1], types.StringType):
                    return TexturePool._TexturePool__overloaded_loadTexture_atomicstring_atomicstring(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <types.StringType> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            return TexturePool._TexturePool__overloaded_loadTexture_atomicstring_atomicstring_int(*_args)
        elif numArgs == 4:
            return TexturePool._TexturePool__overloaded_loadTexture_atomicstring_atomicstring_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    loadTexture = staticmethod(loadTexture)

