# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class AuxSceneData(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
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
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoHXOS:
            libpanda._inPnJyoHXOS(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyosxVE()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setDuration(self, duration):
        returnValue = libpanda._inPnJyoMBDR(self.this, duration)
        return returnValue

    
    def getDuration(self):
        returnValue = libpanda._inPnJyowhQH(self.this)
        return returnValue

    
    def setLastRenderTime(self, renderTime):
        returnValue = libpanda._inPnJyordrX(self.this, renderTime)
        return returnValue

    
    def getLastRenderTime(self):
        returnValue = libpanda._inPnJyozXEn(self.this)
        return returnValue

    
    def getExpirationTime(self):
        returnValue = libpanda._inPnJyoLlWf(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPnJyood_2(self.this, out.this)
        return returnValue

    
    def _AuxSceneData__overloaded_write_ptrConstAuxSceneData_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPnJyocHFH(self.this, out.this, indentLevel)
        return returnValue

    
    def _AuxSceneData__overloaded_write_ptrConstAuxSceneData_ptrOstream(self, out):
        returnValue = libpanda._inPnJyoovWf(self.this, out.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._AuxSceneData__overloaded_write_ptrConstAuxSceneData_ptrOstream(*_args)
        elif numArgs == 2:
            return self._AuxSceneData__overloaded_write_ptrConstAuxSceneData_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


