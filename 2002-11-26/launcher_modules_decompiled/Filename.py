# File: F (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

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
        
        apply(self.constructor, _args)

    
    def _Filename__overloaded_constructor_ptrConstFilename(self, copy):
        self.this = libpandaexpress._inPJoxt0xIC(copy.this)
        self.userManagesMemory = 1

    
    def _Filename__overloaded_constructor_ptrConstFilename_ptrConstFilename(self, dirname, basename):
        self.this = libpandaexpress._inPJoxtw3ik(dirname.this, basename.this)
        self.userManagesMemory = 1

    
    def _Filename__overloaded_constructor_atomicstring(self, filename):
        self.this = libpandaexpress._inPJoxtMYs9(filename)
        self.userManagesMemory = 1

    
    def _Filename__overloaded_constructor(self):
        self.this = libpandaexpress._inPJoxtzHmO()
        self.userManagesMemory = 1

    
    def _Filename__overloaded_constructor_atomicstring(self, filename):
        self.this = libpandaexpress._inPJoxtYS9H(filename)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxt7vP8:
            libpandaexpress._inPJoxt7vP8(self.this)
        

    
    def textFilename(filename):
        returnValue = libpandaexpress._inPJoxteamt(filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    textFilename = staticmethod(textFilename)
    
    def binaryFilename(filename):
        returnValue = libpandaexpress._inPJoxtvv92(filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    binaryFilename = staticmethod(binaryFilename)
    
    def dsoFilename(filename):
        returnValue = libpandaexpress._inPJoxtPXPP(filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    dsoFilename = staticmethod(dsoFilename)
    
    def executableFilename(filename):
        returnValue = libpandaexpress._inPJoxt_2MI(filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    executableFilename = staticmethod(executableFilename)
    
    def _Filename__overloaded_fromOsSpecific_atomicstring___enum__Type(osSpecific, type):
        returnValue = libpandaexpress._inPJoxtJF4r(osSpecific, type)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_fromOsSpecific_atomicstring___enum__Type = staticmethod(_Filename__overloaded_fromOsSpecific_atomicstring___enum__Type)
    
    def _Filename__overloaded_fromOsSpecific_atomicstring(osSpecific):
        returnValue = libpandaexpress._inPJoxt9IuR(osSpecific)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_fromOsSpecific_atomicstring = staticmethod(_Filename__overloaded_fromOsSpecific_atomicstring)
    
    def _Filename__overloaded_expandFrom_atomicstring___enum__Type(userString, type):
        returnValue = libpandaexpress._inPJoxtY4vm(userString, type)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_expandFrom_atomicstring___enum__Type = staticmethod(_Filename__overloaded_expandFrom_atomicstring___enum__Type)
    
    def _Filename__overloaded_expandFrom_atomicstring(userString):
        returnValue = libpandaexpress._inPJoxt9Iq5(userString)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_expandFrom_atomicstring = staticmethod(_Filename__overloaded_expandFrom_atomicstring)
    
    def _Filename__overloaded_temporary_atomicstring_atomicstring___enum__Type(dirname, prefix, type):
        returnValue = libpandaexpress._inPJoxtbIxB(dirname, prefix, type)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_temporary_atomicstring_atomicstring___enum__Type = staticmethod(_Filename__overloaded_temporary_atomicstring_atomicstring___enum__Type)
    
    def _Filename__overloaded_temporary_atomicstring_atomicstring(dirname, prefix):
        returnValue = libpandaexpress._inPJoxt_IGw(dirname, prefix)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Filename__overloaded_temporary_atomicstring_atomicstring = staticmethod(_Filename__overloaded_temporary_atomicstring_atomicstring)
    
    def _Filename__overloaded_assign_ptrFilename_ptrConstFilename(self, copy):
        returnValue = libpandaexpress._inPJoxte4GP(self.this, copy.this)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Filename__overloaded_assign_ptrFilename_atomicstring(self, filename):
        returnValue = libpandaexpress._inPJoxt5V61(self.this, filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Filename__overloaded_assign_ptrFilename_atomicstring(self, filename):
        returnValue = libpandaexpress._inPJoxtHn_g(self.this, filename)
        returnObject = Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def cStr(self):
        returnValue = libpandaexpress._inPJoxtmyvU(self.this)
        return returnValue

    
    def empty(self):
        returnValue = libpandaexpress._inPJoxtOFzc(self.this)
        return returnValue

    
    def length(self):
        returnValue = libpandaexpress._inPJoxthE4s(self.this)
        return returnValue

    
    def __getitem__(self, n):
        returnValue = libpandaexpress._inPJoxt9cHo(self.this, n)
        return returnValue

    
    def getFullpath(self):
        returnValue = libpandaexpress._inPJoxtFzJX(self.this)
        return returnValue

    
    def getDirname(self):
        returnValue = libpandaexpress._inPJoxtgZLo(self.this)
        return returnValue

    
    def getBasename(self):
        returnValue = libpandaexpress._inPJoxtdGTD(self.this)
        return returnValue

    
    def getFullpathWoExtension(self):
        returnValue = libpandaexpress._inPJoxtpN0c(self.this)
        return returnValue

    
    def getBasenameWoExtension(self):
        returnValue = libpandaexpress._inPJoxtNi_I(self.this)
        return returnValue

    
    def getExtension(self):
        returnValue = libpandaexpress._inPJoxt8MQ8(self.this)
        return returnValue

    
    def setFullpath(self, s):
        returnValue = libpandaexpress._inPJoxt3Uip(self.this, s)
        return returnValue

    
    def setDirname(self, s):
        returnValue = libpandaexpress._inPJoxtTdlj(self.this, s)
        return returnValue

    
    def setBasename(self, s):
        returnValue = libpandaexpress._inPJoxtSasV(self.this, s)
        return returnValue

    
    def setFullpathWoExtension(self, s):
        returnValue = libpandaexpress._inPJoxtu0Xc(self.this, s)
        return returnValue

    
    def setBasenameWoExtension(self, s):
        returnValue = libpandaexpress._inPJoxtQChI(self.this, s)
        return returnValue

    
    def setExtension(self, s):
        returnValue = libpandaexpress._inPJoxtw6fv(self.this, s)
        return returnValue

    
    def setBinary(self):
        returnValue = libpandaexpress._inPJoxtK9mc(self.this)
        return returnValue

    
    def setText(self):
        returnValue = libpandaexpress._inPJoxtOixh(self.this)
        return returnValue

    
    def isBinary(self):
        returnValue = libpandaexpress._inPJoxtnswQ(self.this)
        return returnValue

    
    def isText(self):
        returnValue = libpandaexpress._inPJoxte3Vw(self.this)
        return returnValue

    
    def setType(self, type):
        returnValue = libpandaexpress._inPJoxtc7yW(self.this, type)
        return returnValue

    
    def getType(self):
        returnValue = libpandaexpress._inPJoxtFLir(self.this)
        return returnValue

    
    def standardize(self):
        returnValue = libpandaexpress._inPJoxtNUbk(self.this)
        return returnValue

    
    def isLocal(self):
        returnValue = libpandaexpress._inPJoxtGI_b(self.this)
        return returnValue

    
    def isFullyQualified(self):
        returnValue = libpandaexpress._inPJoxtsIAk(self.this)
        return returnValue

    
    def _Filename__overloaded_makeAbsolute_ptrFilename(self):
        returnValue = libpandaexpress._inPJoxt_eKM(self.this)
        return returnValue

    
    def _Filename__overloaded_makeAbsolute_ptrFilename_ptrConstFilename(self, startDirectory):
        returnValue = libpandaexpress._inPJoxtvdOz(self.this, startDirectory.this)
        return returnValue

    
    def makeCanonical(self):
        returnValue = libpandaexpress._inPJoxttwJA(self.this)
        return returnValue

    
    def toOsSpecific(self):
        returnValue = libpandaexpress._inPJoxt4Qhn(self.this)
        return returnValue

    
    def exists(self):
        returnValue = libpandaexpress._inPJoxtUz2_(self.this)
        return returnValue

    
    def isRegularFile(self):
        returnValue = libpandaexpress._inPJoxt5vqn(self.this)
        return returnValue

    
    def isDirectory(self):
        returnValue = libpandaexpress._inPJoxtADlT(self.this)
        return returnValue

    
    def isExecutable(self):
        returnValue = libpandaexpress._inPJoxtdwcX(self.this)
        return returnValue

    
    def _Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename_bool_bool(self, other, thisMissingIsOld, otherMissingIsOld):
        returnValue = libpandaexpress._inPJoxtQRcf(self.this, other.this, thisMissingIsOld, otherMissingIsOld)
        return returnValue

    
    def _Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename_bool(self, other, thisMissingIsOld):
        returnValue = libpandaexpress._inPJoxtjhlq(self.this, other.this, thisMissingIsOld)
        return returnValue

    
    def _Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename(self, other):
        returnValue = libpandaexpress._inPJoxtwwx_(self.this, other.this)
        return returnValue

    
    def _Filename__overloaded_resolveFilename_ptrFilename_ptrConstDSearchPath_atomicstring(self, searchpath, defaultExtension):
        returnValue = libpandaexpress._inPJoxtKd7B(self.this, searchpath.this, defaultExtension)
        return returnValue

    
    def _Filename__overloaded_resolveFilename_ptrFilename_ptrConstDSearchPath(self, searchpath):
        returnValue = libpandaexpress._inPJoxtk2zY(self.this, searchpath.this)
        return returnValue

    
    def _Filename__overloaded_makeRelativeTo_ptrFilename_ptrFilename_bool(self, directory, allowBackups):
        returnValue = libpandaexpress._inPJoxteEHg(self.this, directory.this, allowBackups)
        return returnValue

    
    def _Filename__overloaded_makeRelativeTo_ptrFilename_ptrFilename(self, directory):
        returnValue = libpandaexpress._inPJoxt85oI(self.this, directory.this)
        return returnValue

    
    def findOnSearchpath(self, searchpath):
        returnValue = libpandaexpress._inPJoxt75N1(self.this, searchpath.this)
        return returnValue

    
    def scanDirectory(self, contents):
        returnValue = libpandaexpress._inPJoxtwKbx(self.this, contents.this)
        return returnValue

    
    def openRead(self, stream):
        returnValue = libpandaexpress._inPJoxtZ4Va(self.this, stream.this)
        return returnValue

    
    def _Filename__overloaded_openWrite_ptrConstFilename_ptrOfstream_bool(self, stream, truncate):
        returnValue = libpandaexpress._inPJoxtqfrI(self.this, stream.this, truncate)
        return returnValue

    
    def _Filename__overloaded_openWrite_ptrConstFilename_ptrOfstream(self, stream):
        returnValue = libpandaexpress._inPJoxt7E__(self.this, stream.this)
        return returnValue

    
    def openAppend(self, stream):
        returnValue = libpandaexpress._inPJoxts6KK(self.this, stream.this)
        return returnValue

    
    def openReadWrite(self, stream):
        returnValue = libpandaexpress._inPJoxtIMts(self.this, stream.this)
        return returnValue

    
    def touch(self):
        returnValue = libpandaexpress._inPJoxtFry9(self.this)
        return returnValue

    
    def unlink(self):
        returnValue = libpandaexpress._inPJoxtaMuO(self.this)
        return returnValue

    
    def renameTo(self, other):
        returnValue = libpandaexpress._inPJoxtbavz(self.this, other.this)
        return returnValue

    
    def makeDir(self):
        returnValue = libpandaexpress._inPJoxtOOnR(self.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpandaexpress._inPJoxtTm2T(self.this, other)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPJoxtNclT(self.this, other)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPJoxtyKFd(self.this, other)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPJoxtp_Iv(self.this, out.this)
        return returnValue

    
    def fromOsSpecific(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return Filename._Filename__overloaded_fromOsSpecific_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return Filename._Filename__overloaded_fromOsSpecific_atomicstring___enum__Type(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    fromOsSpecific = staticmethod(fromOsSpecific)
    
    def expandFrom(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return Filename._Filename__overloaded_expandFrom_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return Filename._Filename__overloaded_expandFrom_atomicstring___enum__Type(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    expandFrom = staticmethod(expandFrom)
    
    def temporary(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.StringType):
                    return Filename._Filename__overloaded_temporary_atomicstring_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.IntType):
                        return Filename._Filename__overloaded_temporary_atomicstring_atomicstring___enum__Type(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    temporary = staticmethod(temporary)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Filename__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Filename__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], Filename):
                return self._Filename__overloaded_constructor_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Filename> '
        elif numArgs == 2:
            if isinstance(_args[0], Filename):
                if isinstance(_args[1], Filename):
                    return self._Filename__overloaded_constructor_ptrConstFilename_ptrConstFilename(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def openWrite(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ofstream
            if isinstance(_args[0], Ofstream.Ofstream):
                return self._Filename__overloaded_openWrite_ptrConstFilename_ptrOfstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ofstream.Ofstream> '
        elif numArgs == 2:
            import Ofstream
            if isinstance(_args[0], Ofstream.Ofstream):
                if isinstance(_args[1], types.IntType):
                    return self._Filename__overloaded_openWrite_ptrConstFilename_ptrOfstream_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ofstream.Ofstream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def compareTimestamps(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Filename):
                return self._Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename> '
        elif numArgs == 2:
            if isinstance(_args[0], Filename):
                if isinstance(_args[1], types.IntType):
                    return self._Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename> '
        elif numArgs == 3:
            if isinstance(_args[0], Filename):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._Filename__overloaded_compareTimestamps_ptrConstFilename_ptrConstFilename_bool_bool(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def resolveFilename(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import DSearchPath
            if isinstance(_args[0], DSearchPath.DSearchPath):
                return self._Filename__overloaded_resolveFilename_ptrFilename_ptrConstDSearchPath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <DSearchPath.DSearchPath> '
        elif numArgs == 2:
            import DSearchPath
            if isinstance(_args[0], DSearchPath.DSearchPath):
                if isinstance(_args[1], types.StringType):
                    return self._Filename__overloaded_resolveFilename_ptrFilename_ptrConstDSearchPath_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <DSearchPath.DSearchPath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def makeRelativeTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Filename):
                return self._Filename__overloaded_makeRelativeTo_ptrFilename_ptrFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename> '
        elif numArgs == 2:
            if isinstance(_args[0], Filename):
                if isinstance(_args[1], types.IntType):
                    return self._Filename__overloaded_makeRelativeTo_ptrFilename_ptrFilename_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def makeAbsolute(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Filename__overloaded_makeAbsolute_ptrFilename()
        elif numArgs == 1:
            if isinstance(_args[0], Filename):
                return self._Filename__overloaded_makeAbsolute_ptrFilename_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Filename__overloaded_assign_ptrFilename_atomicstring(_args[0])
            elif isinstance(_args[0], Filename):
                return self._Filename__overloaded_assign_ptrFilename_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


