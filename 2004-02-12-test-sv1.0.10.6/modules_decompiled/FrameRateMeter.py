# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TextNode

class FrameRateMeter(TextNode.TextNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPWs2xbERg(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPWs2xLim9()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _FrameRateMeter__overloaded_setupLayer_ptrFrameRateMeter_ptrGraphicsChannel(self, channel):
        returnValue = libpanda._inPWs2xsBms(self.this, channel.this)
        return returnValue

    
    def _FrameRateMeter__overloaded_setupLayer_ptrFrameRateMeter_ptrGraphicsWindow(self, window):
        returnValue = libpanda._inPWs2xQ7GV(self.this, window.this)
        return returnValue

    
    def clearLayer(self):
        returnValue = libpanda._inPWs2xqb6o(self.this)
        return returnValue

    
    def getLayer(self):
        returnValue = libpanda._inPWs2xeJSC(self.this)
        import GraphicsLayer
        returnObject = GraphicsLayer.GraphicsLayer(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setUpdateInterval(self, updateInterval):
        returnValue = libpanda._inPWs2xTvgr(self.this, updateInterval)
        return returnValue

    
    def getUpdateInterval(self):
        returnValue = libpanda._inPWs2x0Ouf(self.this)
        return returnValue

    
    def setTextPattern(self, textPattern):
        returnValue = libpanda._inPWs2xNbmG(self.this, textPattern)
        return returnValue

    
    def getTextPattern(self):
        returnValue = libpanda._inPWs2xJ3wF(self.this)
        return returnValue

    
    def setClockObject(self, clockObject):
        returnValue = libpanda._inPWs2xqr7U(self.this, clockObject.this)
        return returnValue

    
    def getClockObject(self):
        returnValue = libpanda._inPWs2xmpdy(self.this)
        import ClockObject
        returnObject = ClockObject.ClockObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setupLayer(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import GraphicsWindow
            import GraphicsChannel
            if isinstance(_args[0], GraphicsWindow.GraphicsWindow):
                return self._FrameRateMeter__overloaded_setupLayer_ptrFrameRateMeter_ptrGraphicsWindow(_args[0])
            elif isinstance(_args[0], GraphicsChannel.GraphicsChannel):
                return self._FrameRateMeter__overloaded_setupLayer_ptrFrameRateMeter_ptrGraphicsChannel(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <GraphicsWindow.GraphicsWindow> <GraphicsChannel.GraphicsChannel> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


