# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
from direct.ffi import FFIExternalObject

class DNALoader(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libtoontown._inPdt4ynacW()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yZRXO:
            libtoontown._inPdt4yZRXO(self.this)
        

    
    def _DNALoader__overloaded_buildGraph_ptrDNALoader_ptrDNAStorage_int(self, dnaStore, editing):
        returnValue = libtoontown._inPdt4yWgdC(self.this, dnaStore.this, editing)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _DNALoader__overloaded_buildGraph_ptrDNALoader_ptrDNAStorage(self, dnaStore):
        returnValue = libtoontown._inPdt4ySjxN(self.this, dnaStore.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getData(self):
        returnValue = libtoontown._inPdt4yt8FI(self.this)
        import DNAData
        returnObject = DNAData.DNAData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def buildGraph(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DNALoader__overloaded_buildGraph_ptrDNALoader_ptrDNAStorage(*_args)
        elif numArgs == 2:
            return self._DNALoader__overloaded_buildGraph_ptrDNALoader_ptrDNAStorage_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


