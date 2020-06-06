# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class TexturePool(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
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
        if libpanda and libpanda._inPMAKP8DhA:
            libpanda._inPMAKP8DhA(self.this)
        

    
    def hasTexture(filename):
        returnValue = libpanda._inPMAKP_aBv(filename)
        return returnValue

    hasTexture = staticmethod(hasTexture)
    
    def verifyTexture(filename):
        returnValue = libpanda._inPMAKPBZev(filename)
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
        returnValue = libpanda._inPMAKPBTdl(filename, primaryFileNumChannels)
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
        returnValue = libpanda._inPMAKPmyxl(texture.this)
        return returnValue

    addTexture = staticmethod(addTexture)
    
    def releaseTexture(texture):
        returnValue = libpanda._inPMAKPo_Lr(texture.this)
        return returnValue

    releaseTexture = staticmethod(releaseTexture)
    
    def releaseAllTextures():
        returnValue = libpanda._inPMAKPB290()
        return returnValue

    releaseAllTextures = staticmethod(releaseAllTextures)
    
    def garbageCollect():
        returnValue = libpanda._inPMAKPfx9C()
        return returnValue

    garbageCollect = staticmethod(garbageCollect)
    
    def listContents(out):
        returnValue = libpanda._inPMAKPaY3s(out.this)
        return returnValue

    listContents = staticmethod(listContents)
    
    def loadTexture(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return TexturePool._TexturePool__overloaded_loadTexture_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return TexturePool._TexturePool__overloaded_loadTexture_atomicstring_int(_args[0], _args[1])
                elif isinstance(_args[1], types.StringType):
                    return TexturePool._TexturePool__overloaded_loadTexture_atomicstring_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.IntType):
                        return TexturePool._TexturePool__overloaded_loadTexture_atomicstring_atomicstring_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.IntType):
                            return TexturePool._TexturePool__overloaded_loadTexture_atomicstring_atomicstring_int_int(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    loadTexture = staticmethod(loadTexture)

