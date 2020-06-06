# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ConfigVariableBase

class ConfigVariableSearchPath(ConfigVariableBase.ConfigVariableBase, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ConfigVariableSearchPath__overloaded_constructor_atomicstring_atomicstring_int(self, name, description, flags):
        self.this = libpandaexpress._inPKoxtV4V4(name, description, flags)
        self.userManagesMemory = 1

    
    def _ConfigVariableSearchPath__overloaded_constructor_atomicstring_atomicstring(self, name, description):
        self.this = libpandaexpress._inPKoxti7el(name, description)
        self.userManagesMemory = 1

    
    def _ConfigVariableSearchPath__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaexpress._inPKoxtL6YY(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtUBi7:
            libpandaexpress._inPKoxtUBi7(self.this)
        

    
    def getValue(self):
        returnValue = libpandaexpress._inPKoxt8xvO(self.this)
        import DSearchPath
        returnObject = DSearchPath.DSearchPath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clearLocalValue(self):
        returnValue = libpandaexpress._inPKoxt9EIJ(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpandaexpress._inPKoxtTT5e(self.this)
        return returnValue

    
    def appendDirectory(self, directory):
        returnValue = libpandaexpress._inPKoxtCt4a(self.this, directory.this)
        return returnValue

    
    def prependDirectory(self, directory):
        returnValue = libpandaexpress._inPKoxtClTA(self.this, directory.this)
        return returnValue

    
    def _ConfigVariableSearchPath__overloaded_appendPath_ptrConfigVariableSearchPath_ptrConstDSearchPath(self, path):
        returnValue = libpandaexpress._inPKoxtsHLH(self.this, path.this)
        return returnValue

    
    def _ConfigVariableSearchPath__overloaded_appendPath_ptrConfigVariableSearchPath_atomicstring_atomicstring(self, path, separator):
        returnValue = libpandaexpress._inPKoxtA5UV(self.this, path, separator)
        return returnValue

    
    def _ConfigVariableSearchPath__overloaded_appendPath_ptrConfigVariableSearchPath_atomicstring(self, path):
        returnValue = libpandaexpress._inPKoxtqRVC(self.this, path)
        return returnValue

    
    def prependPath(self, path):
        returnValue = libpandaexpress._inPKoxtUO8I(self.this, path.this)
        return returnValue

    
    def isEmpty(self):
        returnValue = libpandaexpress._inPKoxtRA60(self.this)
        return returnValue

    
    def getNumDirectories(self):
        returnValue = libpandaexpress._inPKoxtSVN5(self.this)
        return returnValue

    
    def getDirectory(self, n):
        returnValue = libpandaexpress._inPKoxtcr0V(self.this, n)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def findFile(self, filename):
        returnValue = libpandaexpress._inPKoxtXwzn(self.this, filename.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findAllFiles(self, filename, results):
        returnValue = libpandaexpress._inPKoxtJhmL(self.this, filename.this, results.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPKoxtkYNJ(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpandaexpress._inPKoxtj3CN(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ConfigVariableSearchPath__overloaded_constructor_atomicstring(*_args)
        elif numArgs == 2:
            return self._ConfigVariableSearchPath__overloaded_constructor_atomicstring_atomicstring(*_args)
        elif numArgs == 3:
            return self._ConfigVariableSearchPath__overloaded_constructor_atomicstring_atomicstring_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def appendPath(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._ConfigVariableSearchPath__overloaded_appendPath_ptrConfigVariableSearchPath_atomicstring(*_args)
            
            import DSearchPath
            if isinstance(_args[0], DSearchPath.DSearchPath):
                return self._ConfigVariableSearchPath__overloaded_appendPath_ptrConfigVariableSearchPath_ptrConstDSearchPath(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DSearchPath.DSearchPath> '
        elif numArgs == 2:
            return self._ConfigVariableSearchPath__overloaded_appendPath_ptrConfigVariableSearchPath_atomicstring_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


