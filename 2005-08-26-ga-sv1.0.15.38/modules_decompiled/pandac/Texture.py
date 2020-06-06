# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
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
        
        self.constructor(*_args)

    
    def _Texture__overloaded_constructor_bool(self, matchFramebufferFormat):
        self.this = libpanda._inPMAKPnZa9(matchFramebufferFormat)
        self.userManagesMemory = 1

    
    def _Texture__overloaded_constructor(self):
        self.this = libpanda._inPMAKPN0nZ()
        self.userManagesMemory = 1

    
    def _Texture__overloaded_constructor_int_int_int_int___enum__Type___enum__Format_bool(self, xsize, ysize, components, componentWidth, type, format, allocateRam):
        self.this = libpanda._inPMAKPwxuL(xsize, ysize, components, componentWidth, type, format, allocateRam)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPMAKPDbsL:
            libpanda._inPMAKPDbsL(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPMAKPoC2_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename_int_int(self, fullpath, alphaFullpath, primaryFileNumChannels, alphaFileChannel):
        returnValue = libpanda._inPMAKPoATv(self.this, fullpath.this, alphaFullpath.this, primaryFileNumChannels, alphaFileChannel)
        return returnValue

    
    def _Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename_int(self, fullpath, alphaFullpath, primaryFileNumChannels):
        returnValue = libpanda._inPMAKPMdQT(self.this, fullpath.this, alphaFullpath.this, primaryFileNumChannels)
        return returnValue

    
    def _Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename(self, fullpath, alphaFullpath):
        returnValue = libpanda._inPMAKPCjPl(self.this, fullpath.this, alphaFullpath.this)
        return returnValue

    
    def _Texture__overloaded_read_ptrTexture_ptrConstFilename_int(self, fullpath, primaryFileNumChannels):
        returnValue = libpanda._inPMAKPuKjv(self.this, fullpath.this, primaryFileNumChannels)
        return returnValue

    
    def _Texture__overloaded_read_ptrTexture_ptrConstFilename(self, fullpath):
        returnValue = libpanda._inPMAKP3IDU(self.this, fullpath.this)
        return returnValue

    
    def _Texture__overloaded_write_ptrConstTexture_ptrConstFilename(self, fullpath):
        returnValue = libpanda._inPMAKPcjd6(self.this, fullpath.this)
        return returnValue

    
    def _Texture__overloaded_write_ptrConstTexture(self):
        returnValue = libpanda._inPMAKPeL8T(self.this)
        return returnValue

    
    def load(self, pnmimage):
        returnValue = libpanda._inPMAKPBHdq(self.this, pnmimage.this)
        return returnValue

    
    def store(self, pnmimage):
        returnValue = libpanda._inPMAKPfuOO(self.this, pnmimage.this)
        return returnValue

    
    def setWrapu(self, wrap):
        returnValue = libpanda._inPMAKPdI99(self.this, wrap)
        return returnValue

    
    def setWrapv(self, wrap):
        returnValue = libpanda._inPMAKPYILa(self.this, wrap)
        return returnValue

    
    def setMinfilter(self, filter):
        returnValue = libpanda._inPMAKPmEu7(self.this, filter)
        return returnValue

    
    def setMagfilter(self, filter):
        returnValue = libpanda._inPMAKP8Kn6(self.this, filter)
        return returnValue

    
    def setAnisotropicDegree(self, anisotropicDegree):
        returnValue = libpanda._inPMAKPGRw3(self.this, anisotropicDegree)
        return returnValue

    
    def setBorderColor(self, color):
        returnValue = libpanda._inPMAKP2r4a(self.this, color.this)
        return returnValue

    
    def setBorderWidth(self, borderWidth):
        returnValue = libpanda._inPMAKPTzD4(self.this, borderWidth)
        return returnValue

    
    def getWrapu(self):
        returnValue = libpanda._inPMAKPIedk(self.this)
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
        returnValue = libpanda._inPMAKPRCMk(self.this)
        return returnValue

    
    def getBorderColor(self):
        returnValue = libpanda._inPMAKPrLZH(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getBorderWidth(self):
        returnValue = libpanda._inPMAKPsdMV(self.this)
        return returnValue

    
    def usesMipmaps(self):
        returnValue = libpanda._inPMAKPYXSi(self.this)
        return returnValue

    
    def getMatchFramebufferFormat(self):
        returnValue = libpanda._inPMAKP608G(self.this)
        return returnValue

    
    def prepare(self, preparedObjects):
        returnValue = libpanda._inPMAKPLFHv(self.this, preparedObjects.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Texture__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._Texture__overloaded_constructor_bool(*_args)
        elif numArgs == 7:
            return self._Texture__overloaded_constructor_int_int_int_int___enum__Type___enum__Format_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 7 '

    
    def read(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Texture__overloaded_read_ptrTexture_ptrConstFilename(*_args)
        elif numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return self._Texture__overloaded_read_ptrTexture_ptrConstFilename_int(*_args)
                
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    return self._Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <Filename.Filename> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 3:
            return self._Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename_int(*_args)
        elif numArgs == 4:
            return self._Texture__overloaded_read_ptrTexture_ptrConstFilename_ptrConstFilename_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Texture__overloaded_write_ptrConstTexture(*_args)
        elif numArgs == 1:
            return self._Texture__overloaded_write_ptrConstTexture_ptrConstFilename(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


