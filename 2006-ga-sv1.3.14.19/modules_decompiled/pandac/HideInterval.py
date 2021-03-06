# File: H (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CInterval

class HideInterval(CInterval.CInterval, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _HideInterval__overloaded_constructor_ptrConstNodePath_atomicstring(self, node, name):
        self.this = libdirect._inPSpsCVO63(node.this, name)
        self.userManagesMemory = 1

    
    def _HideInterval__overloaded_constructor_ptrConstNodePath(self, node):
        self.this = libdirect._inPSpsC866V(node.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inPSpsCUMoC:
            libdirect._inPSpsCUMoC(self.this)
        

    
    def getClassType():
        returnValue = libdirect._inPSpsCVV6X()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._HideInterval__overloaded_constructor_ptrConstNodePath(*_args)
        elif numArgs == 2:
            return self._HideInterval__overloaded_constructor_ptrConstNodePath_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


