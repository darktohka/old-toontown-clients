# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggNode

class EggComment(EggNode.EggNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggComment__overloaded_constructor_ptrConstEggComment(self, copy):
        self.this = libpandaegg._inPkAOMljwn(copy.this)
        self.userManagesMemory = 1

    
    def _EggComment__overloaded_constructor_atomicstring_atomicstring(self, nodeName, comment):
        self.this = libpandaegg._inPkAOMPzAM(nodeName, comment)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMnH8l:
            libpandaegg._inPkAOMnH8l(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMikvz()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _EggComment__overloaded_assign_ptrEggComment_ptrConstEggComment(self, copy):
        returnValue = libpandaegg._inPkAOMAmi9(self.this, copy.this)
        returnObject = EggComment(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggComment__overloaded_assign_ptrEggComment_atomicstring(self, comment):
        returnValue = libpandaegg._inPkAOMokdP(self.this, comment)
        returnObject = EggComment(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setComment(self, comment):
        returnValue = libpandaegg._inPkAOM_5Ek(self.this, comment)
        return returnValue

    
    def getComment(self):
        returnValue = libpandaegg._inPkAOMgAcI(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggComment__overloaded_constructor_ptrConstEggComment(*_args)
        elif numArgs == 2:
            return self._EggComment__overloaded_constructor_atomicstring_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggComment__overloaded_assign_ptrEggComment_atomicstring(*_args)
            
            if isinstance(_args[0], EggComment):
                return self._EggComment__overloaded_assign_ptrEggComment_ptrConstEggComment(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggComment> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


