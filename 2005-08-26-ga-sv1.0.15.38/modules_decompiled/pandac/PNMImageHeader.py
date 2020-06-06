# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class PNMImageHeader(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    CTGrayscale = 1
    CTInvalid = 0
    CTFourChannel = 4
    CTColor = 3
    CTTwoChannel = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PNMImageHeader__overloaded_constructor(self):
        self.this = libpanda._inP5U4kBReb()
        self.userManagesMemory = 1

    
    def _PNMImageHeader__overloaded_constructor_ptrConstPNMImageHeader(self, copy):
        self.this = libpanda._inP5U4k2f0p(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inP5U4kCS6X:
            libpanda._inP5U4kCS6X(self.this)
        

    
    def isGrayscale(colorType):
        returnValue = libpanda._inP5U4kc8Xa(colorType)
        return returnValue

    isGrayscale = staticmethod(isGrayscale)
    
    def hasAlpha(colorType):
        returnValue = libpanda._inP5U4kLbsW(colorType)
        return returnValue

    hasAlpha = staticmethod(hasAlpha)
    
    def readMagicNumber(file, magicNumber, numBytes):
        returnValue = libpanda._inP5U4k3Qff(file.this, magicNumber.this, numBytes)
        return returnValue

    readMagicNumber = staticmethod(readMagicNumber)
    
    def assign(self, copy):
        returnValue = libpanda._inP5U4kglLY(self.this, copy.this)
        returnObject = PNMImageHeader(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getColorType(self):
        returnValue = libpanda._inP5U4k7arZ(self.this)
        return returnValue

    
    def getNumChannels(self):
        returnValue = libpanda._inP5U4kieYf(self.this)
        return returnValue

    
    def isGrayscale(self):
        returnValue = libpanda._inP5U4kAZAi(self.this)
        return returnValue

    
    def hasAlpha(self):
        returnValue = libpanda._inP5U4kAlRN(self.this)
        return returnValue

    
    def getMaxval(self):
        returnValue = libpanda._inP5U4k_pzV(self.this)
        return returnValue

    
    def getXSize(self):
        returnValue = libpanda._inP5U4koepx(self.this)
        return returnValue

    
    def getYSize(self):
        returnValue = libpanda._inP5U4k488x(self.this)
        return returnValue

    
    def hasType(self):
        returnValue = libpanda._inP5U4kVIh0(self.this)
        return returnValue

    
    def getType(self):
        returnValue = libpanda._inP5U4kN1gn(self.this)
        import PNMFileType
        returnObject = PNMFileType.PNMFileType(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setType(self, type):
        returnValue = libpanda._inP5U4kKhXL(self.this, type.this)
        return returnValue

    
    def _PNMImageHeader__overloaded_readHeader_ptrPNMImageHeader_ptrConstFilename_ptrPNMFileType(self, filename, type):
        returnValue = libpanda._inP5U4k6NNp(self.this, filename.this, type.this)
        return returnValue

    
    def _PNMImageHeader__overloaded_readHeader_ptrPNMImageHeader_ptrConstFilename(self, filename):
        returnValue = libpanda._inP5U4kMN61(self.this, filename.this)
        return returnValue

    
    def _PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrConstFilename_ptrPNMFileType(self, filename, type):
        returnValue = libpanda._inP5U4kXjYE(self.this, filename.this, type.this)
        import PNMReader
        returnObject = PNMReader.PNMReader(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrConstFilename(self, filename):
        returnValue = libpanda._inP5U4kHm13(self.this, filename.this)
        import PNMReader
        returnObject = PNMReader.PNMReader(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrIstream_bool_ptrConstFilename_atomicstring_ptrPNMFileType(self, file, ownsFile, filename, magicNumber, type):
        returnValue = libpanda._inP5U4kB_GS(self.this, file.this, ownsFile, filename.this, magicNumber, type.this)
        import PNMReader
        returnObject = PNMReader.PNMReader(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrIstream_bool_ptrConstFilename_atomicstring(self, file, ownsFile, filename, magicNumber):
        returnValue = libpanda._inP5U4k9Nkt(self.this, file.this, ownsFile, filename.this, magicNumber)
        import PNMReader
        returnObject = PNMReader.PNMReader(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrIstream_bool_ptrConstFilename(self, file, ownsFile, filename):
        returnValue = libpanda._inP5U4kXIKf(self.this, file.this, ownsFile, filename.this)
        import PNMReader
        returnObject = PNMReader.PNMReader(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrIstream_bool(self, file, ownsFile):
        returnValue = libpanda._inP5U4khpvx(self.this, file.this, ownsFile)
        import PNMReader
        returnObject = PNMReader.PNMReader(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrIstream(self, file):
        returnValue = libpanda._inP5U4kG56G(self.this, file.this)
        import PNMReader
        returnObject = PNMReader.PNMReader(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrConstFilename_ptrPNMFileType(self, filename, type):
        returnValue = libpanda._inP5U4k5aMD(self.this, filename.this, type.this)
        import PNMWriter
        returnObject = PNMWriter.PNMWriter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrConstFilename(self, filename):
        returnValue = libpanda._inP5U4kZHo2(self.this, filename.this)
        import PNMWriter
        returnObject = PNMWriter.PNMWriter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrOstream_bool_ptrConstFilename_ptrPNMFileType(self, file, ownsFile, filename, type):
        returnValue = libpanda._inP5U4knxIJ(self.this, file.this, ownsFile, filename.this, type.this)
        import PNMWriter
        returnObject = PNMWriter.PNMWriter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrOstream_bool_ptrConstFilename(self, file, ownsFile, filename):
        returnValue = libpanda._inP5U4kMA9F(self.this, file.this, ownsFile, filename.this)
        import PNMWriter
        returnObject = PNMWriter.PNMWriter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrOstream_bool(self, file, ownsFile):
        returnValue = libpanda._inP5U4kvviY(self.this, file.this, ownsFile)
        import PNMWriter
        returnObject = PNMWriter.PNMWriter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrOstream(self, file):
        returnValue = libpanda._inP5U4kKDut(self.this, file.this)
        import PNMWriter
        returnObject = PNMWriter.PNMWriter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def output(self, out):
        returnValue = libpanda._inP5U4kN1NO(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PNMImageHeader__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PNMImageHeader__overloaded_constructor_ptrConstPNMImageHeader(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def readHeader(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PNMImageHeader__overloaded_readHeader_ptrPNMImageHeader_ptrConstFilename(*_args)
        elif numArgs == 2:
            return self._PNMImageHeader__overloaded_readHeader_ptrPNMImageHeader_ptrConstFilename_ptrPNMFileType(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def makeReader(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Istream
            if isinstance(_args[0], Istream.Istream):
                return self._PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrIstream(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrConstFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
        elif numArgs == 2:
            import Istream
            if isinstance(_args[0], Istream.Istream):
                return self._PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrIstream_bool(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrConstFilename_ptrPNMFileType(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
        elif numArgs == 3:
            return self._PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrIstream_bool_ptrConstFilename(*_args)
        elif numArgs == 4:
            return self._PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrIstream_bool_ptrConstFilename_atomicstring(*_args)
        elif numArgs == 5:
            return self._PNMImageHeader__overloaded_makeReader_ptrConstPNMImageHeader_ptrIstream_bool_ptrConstFilename_atomicstring_ptrPNMFileType(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 5 '

    
    def makeWriter(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrOstream(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrConstFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrOstream_bool(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrConstFilename_ptrPNMFileType(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
        elif numArgs == 3:
            return self._PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrOstream_bool_ptrConstFilename(*_args)
        elif numArgs == 4:
            return self._PNMImageHeader__overloaded_makeWriter_ptrConstPNMImageHeader_ptrOstream_bool_ptrConstFilename_ptrPNMFileType(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '


