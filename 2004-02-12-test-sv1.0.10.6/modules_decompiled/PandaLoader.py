# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
            
            apply(self.constructor, _args)

        
        def _Results__overloaded_constructor(self):
            self.this = libpanda._inPkJyorhem()
            self.userManagesMemory = 1

        
        def _Results__overloaded_constructor_ptrConstResults(self, copy):
            self.this = libpanda._inPkJyoRMrN(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPkJyoh0M_:
                libpanda._inPkJyoh0M_(self.this)
            

        
        def assign(self, copy):
            returnValue = libpanda._inPkJyopwhN(self.this, copy.this)
            returnObject = PandaLoader.Results(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def clear(self):
            returnValue = libpanda._inPkJyozgfE(self.this)
            return returnValue

        
        def getNumFiles(self):
            returnValue = libpanda._inPkJyokk1z(self.this)
            return returnValue

        
        def getFile(self, n):
            returnValue = libpanda._inPkJyo5XxT(self.this, n)
            import Filename
            returnObject = Filename.Filename(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getFileType(self, n):
            returnValue = libpanda._inPkJyoyNYp(self.this, n)
            import LoaderFileType
            returnObject = LoaderFileType.LoaderFileType(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self._Results__overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], PandaLoader.Results):
                    return self._Results__overloaded_constructor_ptrConstResults(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PandaLoader.Results> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPkJyop8fi()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def findAllFiles(self, filename, searchPath, results):
        returnValue = libpanda._inPkJyoNTOF(self.this, filename.this, searchPath.this, results.this)
        return returnValue

    
    def _PandaLoader__overloaded_loadSync_ptrConstLoader_ptrConstFilename_bool(self, filename, search):
        returnValue = libpanda._inPkJyoxPn6(self.this, filename.this, search)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _PandaLoader__overloaded_loadSync_ptrConstLoader_ptrConstFilename(self, filename):
        returnValue = libpanda._inPkJyoz7yV(self.this, filename.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _PandaLoader__overloaded_requestLoad_ptrLoader_atomicstring_ptrConstFilename_bool(self, eventName, filename, search):
        returnValue = libpanda._inPkJyouYoe(self.this, eventName, filename.this, search)
        return returnValue

    
    def _PandaLoader__overloaded_requestLoad_ptrLoader_atomicstring_ptrConstFilename(self, eventName, filename):
        returnValue = libpanda._inPkJyonUlc(self.this, eventName, filename.this)
        return returnValue

    
    def checkLoad(self, id):
        returnValue = libpanda._inPkJyoH4Qu(self.this, id)
        return returnValue

    
    def fetchLoad(self, id):
        returnValue = libpanda._inPkJyo0kTC(self.this, id)
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
            if isinstance(_args[0], types.StringType):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    return self._PandaLoader__overloaded_requestLoad_ptrLoader_atomicstring_ptrConstFilename(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    if isinstance(_args[2], types.IntType):
                        return self._PandaLoader__overloaded_requestLoad_ptrLoader_atomicstring_ptrConstFilename_bool(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def loadSync(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._PandaLoader__overloaded_loadSync_ptrConstLoader_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._PandaLoader__overloaded_loadSync_ptrConstLoader_ptrConstFilename_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


