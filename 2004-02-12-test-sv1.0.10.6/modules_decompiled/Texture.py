# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ImageBuffer

class Texture(ImageBuffer.ImageBuffer, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    FTLinearMipmapNearest = 3
    FTNearestMipmapNearest = 2
    FTNearest = 0
    FTLinearMipmapLinear = 5
    FTLinear = 1
    FTNearestMipmapLinear = 4
    FTInvalid = 6
    WMMirror = 2
    WMRepeat = 1
    WMMirrorOnce = 3
    WMInvalid = 5
    WMClamp = 0
    WMBorderColor = 4
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPMAKPN0nZ()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPMAKPDbsL:
            libpanda._inPMAKPDbsL(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPMAKPrC2_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename_int_int(self, fullpath, alphaFullpath, primaryFileNumChannels, alphaFileChannel):
        returnValue = libpanda._inPMAKPpATv(self.this, fullpath.this, alphaFullpath.this, primaryFileNumChannels, alphaFileChannel)
        return returnValue

    
    def _Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename_int(self, fullpath, alphaFullpath, primaryFileNumChannels):
        returnValue = libpanda._inPMAKPMdQT(self.this, fullpath.this, alphaFullpath.this, primaryFileNumChannels)
        return returnValue

    
    def _Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename(self, fullpath, alphaFullpath):
        returnValue = libpanda._inPMAKPDjPl(self.this, fullpath.this, alphaFullpath.this)
        return returnValue

    
    def _Texture__overloaded_read_ptrTexture_ptrConstFilename_int(self, fullpath, primaryFileNumChannels):
        returnValue = libpanda._inPMAKPtKjv(self.this, fullpath.this, primaryFileNumChannels)
        return returnValue

    
    def _Texture__overloaded_read_ptrTexture_ptrConstFilename(self, fullpath):
        returnValue = libpanda._inPMAKP3IDU(self.this, fullpath.this)
        return returnValue

    
    def _Texture__overloaded_write_ptrConstTexture_ptrConstFilename(self, fullpath):
        returnValue = libpanda._inPMAKPfjd6(self.this, fullpath.this)
        return returnValue

    
    def _Texture__overloaded_write_ptrConstTexture(self):
        returnValue = libpanda._inPMAKPeL8T(self.this)
        return returnValue

    
    def setWrapu(self, wrap):
        returnValue = libpanda._inPMAKPaI99(self.this, wrap)
        return returnValue

    
    def setWrapv(self, wrap):
        returnValue = libpanda._inPMAKPYILa(self.this, wrap)
        return returnValue

    
    def setMinfilter(self, filter):
        returnValue = libpanda._inPMAKPnEu7(self.this, filter)
        return returnValue

    
    def setMagfilter(self, filter):
        returnValue = libpanda._inPMAKP9Kn6(self.this, filter)
        return returnValue

    
    def setAnisotropicDegree(self, anisotropicDegree):
        returnValue = libpanda._inPMAKPHRw3(self.this, anisotropicDegree)
        return returnValue

    
    def setBorderColor(self, color):
        returnValue = libpanda._inPMAKP2r4a(self.this, color.this)
        return returnValue

    
    def getWrapu(self):
        returnValue = libpanda._inPMAKPPedk(self.this)
        return returnValue

    
    def getWrapv(self):
        returnValue = libpanda._inPMAKPNerA(self.this)
        return returnValue

    
    def getMinfilter(self):
        returnValue = libpanda._inPMAKPmseL(self.this)
        return returnValue

    
    def getMagfilter(self):
        returnValue = libpanda._inPMAKP8eYK(self.this)
        return returnValue

    
    def getAnisotropicDegree(self):
        returnValue = libpanda._inPMAKPSCMk(self.this)
        return returnValue

    
    def usesMipmaps(self):
        returnValue = libpanda._inPMAKPZXSi(self.this)
        return returnValue

    
    def read(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._Texture__overloaded_read_ptrTexture_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                import Filename
                if isinstance(_args[1], types.IntType):
                    return self._Texture__overloaded_read_ptrTexture_ptrConstFilename_int(_args[0], _args[1])
                elif isinstance(_args[1], Filename.Filename):
                    return self._Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 3:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    if isinstance(_args[2], types.IntType):
                        return self._Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 4:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    if isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.IntType):
                            return self._Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename_int_int(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Texture__overloaded_write_ptrConstTexture()
        elif numArgs == 1:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._Texture__overloaded_write_ptrConstTexture_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


