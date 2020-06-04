# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class MouseButton(FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPelbotMWo:
            libpanda._inPelbotMWo(self.this)
        

    
    def button(buttonNumber):
        returnValue = libpanda._inPelboa24C(buttonNumber)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    button = staticmethod(button)
    
    def one():
        returnValue = libpanda._inPelboRfhO()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    one = staticmethod(one)
    
    def two():
        returnValue = libpanda._inPelbo6jlR()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    two = staticmethod(two)
    
    def three():
        returnValue = libpanda._inPelbohxQB()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    three = staticmethod(three)
    
    def isMouseButton(button):
        returnValue = libpanda._inPelboLqpQ(button.this)
        return returnValue

    isMouseButton = staticmethod(isMouseButton)

