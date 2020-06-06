# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import AsyncUtility

class PandaLoader(AsyncUtility.AsyncUtility, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    class Results(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            self.constructor(*_args)

        
        def _Results__overloaded_constructor(self):
            self.this = libpanda._inPnJyoohem()
            self.userManagesMemory = 1

        
        def _Results__overloaded_constructor_ptrConstResults(self, copy):
            self.this = libpanda._inPnJyoRMrN(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPnJyom0M_:
                libpanda._inPnJyom0M_(self.this)
            

        
        def assign(self, copy):
            returnValue = libpanda._inPnJyopwhN(self.this, copy.this)
            returnObject = PandaLoader.Results(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def clear(self):
            returnValue = libpanda._inPnJyozgfE(self.this)
            return returnValue

        
        def getNumFiles(self):
            returnValue = libpanda._inPnJyolk1z(self.this)
            return returnValue

        
        def getFile(self, n):
            returnValue = libpanda._inPnJyo5XxT(self.this, n)
            import Filename
            returnObject = Filename.Filename(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getFileType(self, n):
            returnValue = libpanda._inPnJyozNYp(self.this, n)
            import LoaderFileType
            returnObject = LoaderFileType.LoaderFileType(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self._Results__overloaded_constructor(*_args)
            elif numArgs == 1:
                return self._Results__overloaded_constructor_ptrConstResults(*_args)
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPnJyoq8fi()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def findAllFiles(self, filename, searchPath, results):
        returnValue = libpanda._inPnJyoNTOF(self.this, filename.this, searchPath.this, results.this)
        return returnValue

    
    def _PandaLoader__overloaded_loadSync_ptrConstLoader_ptrConstFilename_bool(self, filename, search):
        returnValue = libpanda._inPnJyo2Pn6(self.this, filename.this, search)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _PandaLoader__overloaded_loadSync_ptrConstLoader_ptrConstFilename(self, filename):
        returnValue = libpanda._inPnJyoz7yV(self.this, filename.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _PandaLoader__overloaded_requestLoad_ptrLoader_atomicstring_ptrConstFilename_bool(self, eventName, filename, search):
        returnValue = libpanda._inPnJyouYoe(self.this, eventName, filename.this, search)
        return returnValue

    
    def _PandaLoader__overloaded_requestLoad_ptrLoader_atomicstring_ptrConstFilename(self, eventName, filename):
        returnValue = libpanda._inPnJyonUlc(self.this, eventName, filename.this)
        return returnValue

    
    def checkLoad(self, id):
        returnValue = libpanda._inPnJyoE4Qu(self.this, id)
        return returnValue

    
    def fetchLoad(self, id):
        returnValue = libpanda._inPnJyo0kTC(self.this, id)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def requestLoad(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._PandaLoader__overloaded_requestLoad_ptrLoader_atomicstring_ptrConstFilename(*_args)
        elif numArgs == 3:
            return self._PandaLoader__overloaded_requestLoad_ptrLoader_atomicstring_ptrConstFilename_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def loadSync(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PandaLoader__overloaded_loadSync_ptrConstLoader_ptrConstFilename(*_args)
        elif numArgs == 2:
            return self._PandaLoader__overloaded_loadSync_ptrConstLoader_ptrConstFilename_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


