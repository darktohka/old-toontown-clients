# File: C (Python 2.2)

import types
import libotp
import libotpDowncasts
from direct.ffi import FFIExternalObject

class ClickablePopup(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libotpDowncasts]
    
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
        

    
    def destructor(self):
        if libotp and libotp._inPPj7biqoO:
            libotp._inPPj7biqoO(self.this)
        

    
    def getClassType():
        returnValue = libotp._inPPj7buteY()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getType(self):
        returnValue = libotp._inPPj7b1kMa(self.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject


