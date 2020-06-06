# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class TextPropertiesManager(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
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
        

    
    def getGlobalPtr():
        returnValue = libpanda._inPpUk_BXYT()
        returnObject = TextPropertiesManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalPtr = staticmethod(getGlobalPtr)
    
    def setProperties(self, name, properties):
        returnValue = libpanda._inPpUk_YE4B(self.this, name, properties.this)
        return returnValue

    
    def getProperties(self, name):
        returnValue = libpanda._inPpUk_4Bnj(self.this, name)
        import TextProperties
        returnObject = TextProperties.TextProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasProperties(self, name):
        returnValue = libpanda._inPpUk_GLtg(self.this, name)
        return returnValue

    
    def clearProperties(self, name):
        returnValue = libpanda._inPpUk_TUsF(self.this, name)
        return returnValue

    
    def _TextPropertiesManager__overloaded_write_ptrConstTextPropertiesManager_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPpUk_UMME(self.this, out.this, indentLevel)
        return returnValue

    
    def _TextPropertiesManager__overloaded_write_ptrConstTextPropertiesManager_ptrOstream(self, out):
        returnValue = libpanda._inPpUk_7FOX(self.this, out.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextPropertiesManager__overloaded_write_ptrConstTextPropertiesManager_ptrOstream(*_args)
        elif numArgs == 2:
            return self._TextPropertiesManager__overloaded_write_ptrConstTextPropertiesManager_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


