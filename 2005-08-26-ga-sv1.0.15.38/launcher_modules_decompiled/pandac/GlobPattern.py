# File: G (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class GlobPattern(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _GlobPattern__overloaded_constructor_ptrConstGlobPattern(self, copy):
        self.this = libpandaexpress._inPKoxtXLB8(copy.this)
        self.userManagesMemory = 1

    
    def _GlobPattern__overloaded_constructor_atomicstring(self, pattern):
        self.this = libpandaexpress._inPKoxtA2Rm(pattern)
        self.userManagesMemory = 1

    
    def _GlobPattern__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtIp0c()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxt_V_e:
            libpandaexpress._inPKoxt_V_e(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inPKoxtgOgc(self.this, copy.this)
        returnObject = GlobPattern(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def eq(self, other):
        returnValue = libpandaexpress._inPKoxtD9Td(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inPKoxtK_Dx(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inPKoxtyvIe(self.this, other.this)
        return returnValue

    
    def setPattern(self, pattern):
        returnValue = libpandaexpress._inPKoxtkjXp(self.this, pattern)
        return returnValue

    
    def getPattern(self):
        returnValue = libpandaexpress._inPKoxttRZ0(self.this)
        return returnValue

    
    def setCaseSensitive(self, caseSensitive):
        returnValue = libpandaexpress._inPKoxtiND_(self.this, caseSensitive)
        return returnValue

    
    def getCaseSensitive(self):
        returnValue = libpandaexpress._inPKoxtCAJw(self.this)
        return returnValue

    
    def matches(self, candidate):
        returnValue = libpandaexpress._inPKoxt6aT3(self.this, candidate)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtEKr3(self.this, out.this)
        return returnValue

    
    def hasGlobCharacters(self):
        returnValue = libpandaexpress._inPKoxtP369(self.this)
        return returnValue

    
    def _GlobPattern__overloaded_matchFiles_ptrGlobPattern_ptrVectorbasicStringchar_ptrConstFilename(self, results, cwd):
        returnValue = libpandaexpress._inPKoxtuzy2(self.this, results.this, cwd.this)
        return returnValue

    
    def _GlobPattern__overloaded_matchFiles_ptrGlobPattern_ptrVectorbasicStringchar(self, results):
        returnValue = libpandaexpress._inPKoxtdu9b(self.this, results.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._GlobPattern__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._GlobPattern__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], GlobPattern):
                return self._GlobPattern__overloaded_constructor_ptrConstGlobPattern(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <GlobPattern> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def matchFiles(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._GlobPattern__overloaded_matchFiles_ptrGlobPattern_ptrVectorbasicStringchar(*_args)
        elif numArgs == 2:
            return self._GlobPattern__overloaded_matchFiles_ptrGlobPattern_ptrVectorbasicStringchar_ptrConstFilename(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


