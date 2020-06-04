# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggObject

class EggNameUniquifier(EggObject.EggObject, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMDsSt()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def clear(self):
        returnValue = libpandaegg._inPkAOM8kwb(self.this)
        return returnValue

    
    def uniquify(self, node):
        returnValue = libpandaegg._inPkAOMeFPl(self.this, node.this)
        return returnValue

    
    def getNode(self, category, name):
        returnValue = libpandaegg._inPkAOMOi3s(self.this, category, name)
        import EggNode
        returnObject = EggNode.EggNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasName(self, category, name):
        returnValue = libpandaegg._inPkAOMXkGH(self.this, category, name)
        return returnValue

    
    def _EggNameUniquifier__overloaded_addName_ptrEggNameUniquifier_atomicstring_atomicstring_ptrEggNode(self, category, name, node):
        returnValue = libpandaegg._inPkAOMEft2(self.this, category, name, node.this)
        return returnValue

    
    def _EggNameUniquifier__overloaded_addName_ptrEggNameUniquifier_atomicstring_atomicstring(self, category, name):
        returnValue = libpandaegg._inPkAOMYHHH(self.this, category, name)
        return returnValue

    
    def getCategory(self, node):
        returnValue = libpandaegg._inPkAOM3vi3(self.this, node.this)
        return returnValue

    
    def filterName(self, node):
        returnValue = libpandaegg._inPkAOMEi4Q(self.this, node.this)
        return returnValue

    
    def generateName(self, node, category, index):
        returnValue = libpandaegg._inPkAOM1Kmh(self.this, node.this, category, index)
        return returnValue

    
    def addName(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._EggNameUniquifier__overloaded_addName_ptrEggNameUniquifier_atomicstring_atomicstring(*_args)
        elif numArgs == 3:
            return self._EggNameUniquifier__overloaded_addName_ptrEggNameUniquifier_atomicstring_atomicstring_ptrEggNode(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


