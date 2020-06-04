# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class MouseButton(FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPflbosMWo:
            libpanda._inPflbosMWo(self.this)
        

    
    def button(buttonNumber):
        returnValue = libpanda._inPflboa24C(buttonNumber)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    button = staticmethod(button)
    
    def one():
        returnValue = libpanda._inPflboRfhO()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    one = staticmethod(one)
    
    def two():
        returnValue = libpanda._inPflbo6jlR()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    two = staticmethod(two)
    
    def three():
        returnValue = libpanda._inPflbohxQB()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    three = staticmethod(three)
    
    def wheelUp():
        returnValue = libpanda._inPflboCrvD()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    wheelUp = staticmethod(wheelUp)
    
    def wheelDown():
        returnValue = libpanda._inPflboFLlN()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    wheelDown = staticmethod(wheelDown)
    
    def isMouseButton(button):
        returnValue = libpanda._inPflboLqpQ(button.this)
        return returnValue

    isMouseButton = staticmethod(isMouseButton)

