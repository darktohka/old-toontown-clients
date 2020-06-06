# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class MouseWatcherParameter(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPziw5Vqnr:
            libpanda._inPziw5Vqnr(self.this)
        

    
    def hasButton(self):
        returnValue = libpanda._inPziw5HdBJ(self.this)
        return returnValue

    
    def getButton(self):
        returnValue = libpanda._inPziw5Xbt7(self.this)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasKeycode(self):
        returnValue = libpanda._inPziw5ssPh(self.this)
        return returnValue

    
    def getKeycode(self):
        returnValue = libpanda._inPziw5Lr7T(self.this)
        return returnValue

    
    def getModifierButtons(self):
        returnValue = libpanda._inPziw5A2au(self.this)
        import ModifierButtons
        returnObject = ModifierButtons.ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasMouse(self):
        returnValue = libpanda._inPziw50Y9y(self.this)
        return returnValue

    
    def getMouse(self):
        returnValue = libpanda._inPziw5kFpl(self.this)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isOutside(self):
        returnValue = libpanda._inPziw5CuZd(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPziw5P1BE(self.this, out.this)
        return returnValue


