# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class GraphicsLayer(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
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
        

    
    def getClassType():
        returnValue = libpanda._inPO9cYBdnF()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _GraphicsLayer__overloaded_makeDisplayRegion_ptrGraphicsLayer(self):
        returnValue = libpanda._inPO9cYiC1O(self.this)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _GraphicsLayer__overloaded_makeDisplayRegion_ptrGraphicsLayer_float_float_float_float(self, l, r, b, t):
        returnValue = libpanda._inPO9cY_q23(self.this, l, r, b, t)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumDrs(self):
        returnValue = libpanda._inPO9cYi79D(self.this)
        return returnValue

    
    def getDr(self, index):
        returnValue = libpanda._inPO9cYoRO1(self.this, index)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _GraphicsLayer__overloaded_removeDr_ptrGraphicsLayer_ptrDisplayRegion(self, displayRegion):
        returnValue = libpanda._inPO9cY4u5p(self.this, displayRegion.this)
        return returnValue

    
    def _GraphicsLayer__overloaded_removeDr_ptrGraphicsLayer_int(self, index):
        returnValue = libpanda._inPO9cYOWCB(self.this, index)
        return returnValue

    
    def getChannel(self):
        returnValue = libpanda._inPO9cYbKvA(self.this)
        import GraphicsChannel
        returnObject = GraphicsChannel.GraphicsChannel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getWindow(self):
        returnValue = libpanda._inPO9cYw_Xk(self.this)
        import GraphicsOutput
        returnObject = GraphicsOutput.GraphicsOutput(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getPipe(self):
        returnValue = libpanda._inPO9cYE9wO(self.this)
        import GraphicsPipe
        returnObject = GraphicsPipe.GraphicsPipe(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def setActive(self, active):
        returnValue = libpanda._inPO9cY_hJu(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libpanda._inPO9cYUCvw(self.this)
        return returnValue

    
    def setSort(self, sort):
        returnValue = libpanda._inPO9cYBV_Z(self.this, sort)
        return returnValue

    
    def getSort(self):
        returnValue = libpanda._inPO9cYmytS(self.this)
        return returnValue

    
    def makeDisplayRegion(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._GraphicsLayer__overloaded_makeDisplayRegion_ptrGraphicsLayer(*_args)
        elif numArgs == 4:
            return self._GraphicsLayer__overloaded_makeDisplayRegion_ptrGraphicsLayer_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 4 '

    
    def removeDr(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._GraphicsLayer__overloaded_removeDr_ptrGraphicsLayer_int(*_args)
            
            import DisplayRegion
            if isinstance(_args[0], DisplayRegion.DisplayRegion):
                return self._GraphicsLayer__overloaded_removeDr_ptrGraphicsLayer_ptrDisplayRegion(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <DisplayRegion.DisplayRegion> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


