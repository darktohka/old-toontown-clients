# File: F (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class Filename(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    TDso = 1
    TGeneral = 0
    TExecutable = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Filename__overloaded_constructor_ptrConstFilename(self, copy):
        self.this = libpandaexpress._inPKoxt0xIC(copy.this)
        self.userManagesMemory = 1

    
    def _Filename__overloaded_constructor_ptrConstFilename_ptrConstFilename(self, dirname, basename):
        self.this = libpandaexpress._inPKoxtz3ik(dirname.this, basename.this)
        self.userManagesMemory = 1

    
    def _Filename__overloaded_constructor_atomicstring(self, filename):
        self.this = libpandaexpress._inPKoxtLYs9(filename)
        self.userManagesMemory = 1

    
    def _Filename__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtzHmO()
        self.userManagesMemory = 1

    
    def _Filename__overloaded_constructor_atomicstring(self, filename):
        self.this = libpandaexpress._inPKoxtYS9H(filename)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxt4vP8:
            libpandaexpress._inPKoxt4vP8(self.this)
        

    
    def textFilename(filename):
        returnValue = libpandaexpress._inPKoxtfamt(filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    textFilename = staticmethod(textFilename)
    
    def binaryFilename(filename):
        returnValue = libpandaexpress._inPKoxtuv92(filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    binaryFilename = staticmethod(binaryFilename)
    
    def dsoFilename(filename):
        returnValue = libpandaexpress._inPKoxtPXPP(filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    dsoFilename = staticmethod(dsoFilename)
    
    def executableFilename(filename):
        returnValue = libpandaexpress._inPKoxt_2MI(filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    executableFilename = staticmethod(executableFilename)
    
    def _Filename__overloaded_fromOsSpecific_atomicstring___enum__Type(osSpecific, type):
        returnValue = libpandaexpress._inPKoxtIF4r(osSpecific, type)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_fromOsSpecific_atomicstring___enum__Type = staticmethod(_Filename__overloaded_fromOsSpecific_atomicstring___enum__Type)
    
    def _Filename__overloaded_fromOsSpecific_atomicstring(osSpecific):
        returnValue = libpandaexpress._inPKoxt9IuR(osSpecific)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_fromOsSpecific_atomicstring = staticmethod(_Filename__overloaded_fromOsSpecific_atomicstring)
    
    def _Filename__overloaded_expandFrom_atomicstring___enum__Type(userString, type):
        returnValue = libpandaexpress._inPKoxtZ4vm(userString, type)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_expandFrom_atomicstring___enum__Type = staticmethod(_Filename__overloaded_expandFrom_atomicstring___enum__Type)
    
    def _Filename__overloaded_expandFrom_atomicstring(userString):
        returnValue = libpandaexpress._inPKoxt_Iq5(userString)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_expandFrom_atomicstring = staticmethod(_Filename__overloaded_expandFrom_atomicstring)
    
    def _Filename__overloaded_temporary_atomicstring_atomicstring___enum__Type(dirname, prefix, type):
        returnValue = libpandaexpress._inPKoxtbIxB(dirname, prefix, type)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_temporary_atomicstring_atomicstring___enum__Type = staticmethod(_Filename__overloaded_temporary_atomicstring_atomicstring___enum__Type)
    
    def _Filename__overloaded_temporary_atomicstring_atomicstring(dirname, prefix):
        returnValue = libpandaexpress._inPKoxtwIGw(dirname, prefix)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_temporary_atomicstring_atomicstring = staticmethod(_Filename__overloaded_temporary_atomicstring_atomicstring)
    
    def _Filename__overloaded_assign_ptrFilename_ptrConstFilename(self, copy):
        returnValue = libpandaexpress._inPKoxte4GP(self.this, copy.this)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Filename__overloaded_assign_ptrFilename_atomicstring(self, filename):
        returnValue = libpandaexpress._inPKoxt6V61(self.this, filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Filename__overloaded_assign_ptrFilename_atomicstring(self, filename):
        returnValue = libpandaexpress._inPKoxtAn_g(self.this, filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def cStr(self):
        returnValue = libpandaexpress._inPKoxtmyvU(self.this)
        return returnValue

    
    def empty(self):
        returnValue = libpandaexpress._inPKoxtOFzc(self.this)
        return returnValue

    
    def length(self):
        returnValue = libpandaexpress._inPKoxtgE4s(self.this)
        return returnValue

    
    def __getitem__(self, n):
        returnValue = libpandaexpress._inPKoxt6cHo(self.this, n)
        return returnValue

    
    def getFullpath(self):
        returnValue = libpandaexpress._inPKoxtFzJX(self.this)
        return returnValue

    
    def getDirname(self):
        returnValue = libpandaexpress._inPKoxtnZLo(self.this)
        return returnValue

    
    def getBasename(self):
        returnValue = libpandaexpress._inPKoxtdGTD(self.this)
        return returnValue

    
    def getFullpathWoExtension(self):
        returnValue = libpandaexpress._inPKoxtpN0c(self.this)
        return returnValue

    
    def getBasenameWoExtension(self):
        returnValue = libpandaexpress._inPKoxtNi_I(self.this)
        return returnValue

    
    def getExtension(self):
        returnValue = libpandaexpress._inPKoxt_MQ8(self.this)
        return returnValue

    
    def setFullpath(self, s):
        returnValue = libpandaexpress._inPKoxtoUip(self.this, s)
        return returnValue

    
    def setDirname(self, s):
        returnValue = libpandaexpress._inPKoxtSdlj(self.this, s)
        return returnValue

    
    def setBasename(self, s):
        returnValue = libpandaexpress._inPKoxtSasV(self.this, s)
        return returnValue

    
    def setFullpathWoExtension(self, s):
        returnValue = libpandaexpress._inPKoxtu0Xc(self.this, s)
        return returnValue

    
    def setBasenameWoExtension(self, s):
        returnValue = libpandaexpress._inPKoxtQChI(self.this, s)
        return returnValue

    
    def setExtension(self, s):
        returnValue = libpandaexpress._inPKoxtx6fv(self.this, s)
        return returnValue

    
    def setBinary(self):
        returnValue = libpandaexpress._inPKoxtK9mc(self.this)
        return returnValue

    
    def setText(self):
        returnValue = libpandaexpress._inPKoxtBixh(self.this)
        return returnValue

    
    def isBinary(self):
        returnValue = libpandaexpress._inPKoxtnswQ(self.this)
        return returnValue

    
    def isText(self):
        returnValue = libpandaexpress._inPKoxtf3Vw(self.this)
        return returnValue

    
    def setType(self, type):
        returnValue = libpandaexpress._inPKoxtc7yW(self.this, type)
        return returnValue

    
    def getType(self):
        returnValue = libpandaexpress._inPKoxtELir(self.this)
        return returnValue

    
    def extractComponents(self, components):
        returnValue = libpandaexpress._inPKoxtTzFq(self.this, components.this)
        return returnValue

    
    def standardize(self):
        returnValue = libpandaexpress._inPKoxtMUbk(self.this)
        return returnValue

    
    def isLocal(self):
        returnValue = libpandaexpress._inPKoxtGI_b(self.this)
        return returnValue

    
    def isFullyQualified(self):
        returnValue = libpandaexpress._inPKoxttIAk(self.this)
        return returnValue

    
    def _Filename__overloaded_makeAbsolute_ptrFilename(self):
        returnValue = libpandaexpress._inPKoxt_eKM(self.this)
        return returnValue

    
    def _Filename__overloaded_makeAbsolute_ptrFilename_ptrConstFilename(self, startDirectory):
        returnValue = libpandaexpress._inPKoxtudOz(self.this, startDirectory.this)
        return returnValue

    
    def makeCanonical(self):
        returnValue = libpandaexpress._inPKoxttwJA(self.this)
        return returnValue

    
    def toOsSpecific(self):
        returnValue = libpandaexpress._inPKoxtHThn(self.this)
        return returnValue

    
    def toOsGeneric(self):
        returnValue = libpandaexpress._inPKoxtT7Xd(self.this)
        return returnValue

    
    def exists(self):
        returnValue = libpandaexpress._inPKoxtXz2_(self.this)
        return returnValue

    
    def isRegularFile(self):
        returnValue = libpandaexpress._inPKoxt4vqn(self.this)
        return returnValue

    
    def isDirectory(self):
        returnValue = libpandaexpress._inPKoxtADlT(self.this)
        return returnValue

    
    def isExecutable(self):
        returnValue = libpandaexpress._inPKoxtdwcX(self.this)
        return returnValue

    
    def _Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename_bool_bool(self, other, thisMissingIsOld, otherMissingIsOld):
        returnValue = libpandaexpress._inPKoxtQRcf(self.this, other.this, thisMissingIsOld, otherMissingIsOld)
        return returnValue

    
    def _Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename_bool(self, other, thisMissingIsOld):
        returnValue = libpandaexpress._inPKoxtihlq(self.this, other.this, thisMissingIsOld)
        return returnValue

    
    def _Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename(self, other):
        returnValue = libpandaexpress._inPKoxt3wx_(self.this, other.this)
        return returnValue

    
    def _Filename__overloaded_resolveFilename_ptrFilename_ptrConstDSearchPath_atomicstring(self, searchpath, defaultExtension):
        returnValue = libpandaexpress._inPKoxtKd7B(self.this, searchpath.this, defaultExtension)
        return returnValue

    
    def _Filename__overloaded_resolveFilename_ptrFilename_ptrConstDSearchPath(self, searchpath):
        returnValue = libpandaexpress._inPKoxtk2zY(self.this, searchpath.this)
        return returnValue

    
    def _Filename__overloaded_makeRelativeTo_ptrFilename_ptrFilename_bool(self, directory, allowBackups):
        returnValue = libpandaexpress._inPKoxtfEHg(self.this, directory.this, allowBackups)
        return returnValue

    
    def _Filename__overloaded_makeRelativeTo_ptrFilename_ptrFilename(self, directory):
        returnValue = libpandaexpress._inPKoxt85oI(self.this, directory.this)
        return returnValue

    
    def findOnSearchpath(self, searchpath):
        returnValue = libpandaexpress._inPKoxt45N1(self.this, searchpath.this)
        return returnValue

    
    def scanDirectory(self, contents):
        returnValue = libpandaexpress._inPKoxtPKbx(self.this, contents.this)
        return returnValue

    
    def openRead(self, stream):
        returnValue = libpandaexpress._inPKoxtZ4Va(self.this, stream.this)
        return returnValue

    
    def _Filename__overloaded_openWrite_ptrConstFilename_ptrOfstream_bool(self, stream, truncate):
        returnValue = libpandaexpress._inPKoxtqfrI(self.this, stream.this, truncate)
        return returnValue

    
    def _Filename__overloaded_openWrite_ptrConstFilename_ptrOfstream(self, stream):
        returnValue = libpandaexpress._inPKoxt6E__(self.this, stream.this)
        return returnValue

    
    def openAppend(self, stream):
        returnValue = libpandaexpress._inPKoxts6KK(self.this, stream.this)
        return returnValue

    
    def openReadWrite(self, stream):
        returnValue = libpandaexpress._inPKoxtLMts(self.this, stream.this)
        return returnValue

    
    def touch(self):
        returnValue = libpandaexpress._inPKoxtCry9(self.this)
        return returnValue

    
    def unlink(self):
        returnValue = libpandaexpress._inPKoxtaMuO(self.this)
        return returnValue

    
    def renameTo(self, other):
        returnValue = libpandaexpress._inPKoxtaavz(self.this, other.this)
        return returnValue

    
    def makeDir(self):
        returnValue = libpandaexpress._inPKoxtOOnR(self.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpandaexpress._inPKoxtTm2T(self.this, other)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPKoxtNclT(self.this, other)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPKoxtyKFd(self.this, other)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxto_Iv(self.this, out.this)
        return returnValue

    
    def fromOsSpecific(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Filename._Filename__overloaded_fromOsSpecific_atomicstring(*_args)
        elif numArgs == 2:
            return Filename._Filename__overloaded_fromOsSpecific_atomicstring___enum__Type(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    fromOsSpecific = staticmethod(fromOsSpecific)
    
    def expandFrom(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Filename._Filename__overloaded_expandFrom_atomicstring(*_args)
        elif numArgs == 2:
            return Filename._Filename__overloaded_expandFrom_atomicstring___enum__Type(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    expandFrom = staticmethod(expandFrom)
    
    def temporary(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Filename._Filename__overloaded_temporary_atomicstring_atomicstring(*_args)
        elif numArgs == 3:
            return Filename._Filename__overloaded_temporary_atomicstring_atomicstring___enum__Type(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    temporary = staticmethod(temporary)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Filename__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Filename__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], Filename):
                return self._Filename__overloaded_constructor_ptrConstFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Filename> '
        elif numArgs == 2:
            return self._Filename__overloaded_constructor_ptrConstFilename_ptrConstFilename(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def openWrite(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Filename__overloaded_openWrite_ptrConstFilename_ptrOfstream(*_args)
        elif numArgs == 2:
            return self._Filename__overloaded_openWrite_ptrConstFilename_ptrOfstream_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def compareTimestamps(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename(*_args)
        elif numArgs == 2:
            return self._Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename_bool(*_args)
        elif numArgs == 3:
            return self._Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename_bool_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def resolveFilename(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Filename__overloaded_resolveFilename_ptrFilename_ptrConstDSearchPath(*_args)
        elif numArgs == 2:
            return self._Filename__overloaded_resolveFilename_ptrFilename_ptrConstDSearchPath_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def makeRelativeTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Filename__overloaded_makeRelativeTo_ptrFilename_ptrFilename(*_args)
        elif numArgs == 2:
            return self._Filename__overloaded_makeRelativeTo_ptrFilename_ptrFilename_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def makeAbsolute(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Filename__overloaded_makeAbsolute_ptrFilename(*_args)
        elif numArgs == 1:
            return self._Filename__overloaded_makeAbsolute_ptrFilename_ptrConstFilename(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Filename__overloaded_assign_ptrFilename_atomicstring(*_args)
            
            if isinstance(_args[0], Filename):
                return self._Filename__overloaded_assign_ptrFilename_ptrConstFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


