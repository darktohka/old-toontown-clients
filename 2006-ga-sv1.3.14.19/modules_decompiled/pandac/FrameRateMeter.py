# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TextNode

class FrameRateMeter(TextNode.TextNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPXs2xYERg(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPXs2xKim9()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _FrameRateMeter__overloaded_setupLayer_ptrFrameRateMeter_ptrGraphicsChannel(self, channel):
        returnValue = libpanda._inPXs2xjBms(self.this, channel.this)
        return returnValue

    
    def _FrameRateMeter__overloaded_setupLayer_ptrFrameRateMeter_ptrGraphicsOutput(self, window):
        returnValue = libpanda._inPXs2xGku4(self.this, window.this)
        return returnValue

    
    def clearLayer(self):
        returnValue = libpanda._inPXs2xtb6o(self.this)
        return returnValue

    
    def getLayer(self):
        returnValue = libpanda._inPXs2xeJSC(self.this)
        import GraphicsLayer
        returnObject = GraphicsLayer.GraphicsLayer(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setUpdateInterval(self, updateInterval):
        returnValue = libpanda._inPXs2xUvgr(self.this, updateInterval)
        return returnValue

    
    def getUpdateInterval(self):
        returnValue = libpanda._inPXs2x0Ouf(self.this)
        return returnValue

    
    def setTextPattern(self, textPattern):
        returnValue = libpanda._inPXs2xNbmG(self.this, textPattern)
        return returnValue

    
    def getTextPattern(self):
        returnValue = libpanda._inPXs2xJ3wF(self.this)
        return returnValue

    
    def setClockObject(self, clockObject):
        returnValue = libpanda._inPXs2xqr7U(self.this, clockObject.this)
        return returnValue

    
    def getClockObject(self):
        returnValue = libpanda._inPXs2xZmdy(self.this)
        import ClockObject
        returnObject = ClockObject.ClockObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setupLayer(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import GraphicsOutput
            if isinstance(_args[0], GraphicsOutput.GraphicsOutput):
                return self._FrameRateMeter__overloaded_setupLayer_ptrFrameRateMeter_ptrGraphicsOutput(*_args)
            
            import GraphicsChannel
            if isinstance(_args[0], GraphicsChannel.GraphicsChannel):
                return self._FrameRateMeter__overloaded_setupLayer_ptrFrameRateMeter_ptrGraphicsChannel(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <GraphicsOutput.GraphicsOutput> <GraphicsChannel.GraphicsChannel> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


