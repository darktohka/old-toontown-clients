# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class MouseWatcherParameter(FFIExternalObject.FFIExternalObject):
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
        

    
    def destructor(self):
        if libpanda and libpanda._inPyiw5Wqnr:
            libpanda._inPyiw5Wqnr(self.this)
        

    
    def hasButton(self):
        returnValue = libpanda._inPyiw5HdBJ(self.this)
        return returnValue

    
    def getButton(self):
        returnValue = libpanda._inPyiw5Wbt7(self.this)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasKeycode(self):
        returnValue = libpanda._inPyiw5jsPh(self.this)
        return returnValue

    
    def getKeycode(self):
        returnValue = libpanda._inPyiw5Lr7T(self.this)
        return returnValue

    
    def hasCandidate(self):
        returnValue = libpanda._inPyiw5m3E2(self.this)
        return returnValue

    
    def _MouseWatcherParameter__overloaded_getCandidateStringEncoded_ptrConstMouseWatcherParameter(self):
        returnValue = libpanda._inPyiw5JON1(self.this)
        return returnValue

    
    def _MouseWatcherParameter__overloaded_getCandidateStringEncoded_ptrConstMouseWatcherParameter___enum__Encoding(self, encoding):
        returnValue = libpanda._inPyiw5ggbz(self.this, encoding)
        return returnValue

    
    def getHighlightStart(self):
        returnValue = libpanda._inPyiw52Qq_(self.this)
        return returnValue

    
    def getHighlightEnd(self):
        returnValue = libpanda._inPyiw5wcQ5(self.this)
        return returnValue

    
    def getCursorPos(self):
        returnValue = libpanda._inPyiw55fsc(self.this)
        return returnValue

    
    def getModifierButtons(self):
        returnValue = libpanda._inPyiw5D2au(self.this)
        import ModifierButtons
        returnObject = ModifierButtons.ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasMouse(self):
        returnValue = libpanda._inPyiw53Y9y(self.this)
        return returnValue

    
    def getMouse(self):
        returnValue = libpanda._inPyiw5nFpl(self.this)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isOutside(self):
        returnValue = libpanda._inPyiw5CuZd(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPyiw5P1BE(self.this, out.this)
        return returnValue

    
    def getCandidateStringEncoded(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._MouseWatcherParameter__overloaded_getCandidateStringEncoded_ptrConstMouseWatcherParameter(*_args)
        elif numArgs == 1:
            return self._MouseWatcherParameter__overloaded_getCandidateStringEncoded_ptrConstMouseWatcherParameter___enum__Encoding(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


