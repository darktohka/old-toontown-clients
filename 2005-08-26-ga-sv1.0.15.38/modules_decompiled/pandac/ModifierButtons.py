# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class ModifierButtons(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ModifierButtons__overloaded_constructor(self):
        self.this = libpanda._inPflboUVR4()
        self.userManagesMemory = 1

    
    def _ModifierButtons__overloaded_constructor_ptrConstModifierButtons(self, copy):
        self.this = libpanda._inPflboPxfU(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPflboLQES:
            libpanda._inPflboLQES(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPflbofwyS(self.this, copy.this)
        returnObject = ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def eq(self, other):
        returnValue = libpanda._inPflboahow(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPflboig3N(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPflbozaOV(self.this, other.this)
        return returnValue

    
    def __and__(self, other):
        returnValue = libpanda._inPflbo46nn(self.this, other.this)
        returnObject = ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __or__(self, other):
        returnValue = libpanda._inPflboea_2(self.this, other.this)
        returnObject = ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iand__(self, other):
        returnValue = libpanda._inPflbo1hOw(self.this, other.this)
        return self

    
    def __ior__(self, other):
        returnValue = libpanda._inPflboLBn_(self.this, other.this)
        return self

    
    def setButtonList(self, other):
        returnValue = libpanda._inPflbo_tdp(self.this, other.this)
        return returnValue

    
    def matches(self, other):
        returnValue = libpanda._inPflbozNfr(self.this, other.this)
        return returnValue

    
    def addButton(self, button):
        returnValue = libpanda._inPflboTLZg(self.this, button.this)
        return returnValue

    
    def hasButton(self, button):
        returnValue = libpanda._inPflboMHRl(self.this, button.this)
        return returnValue

    
    def removeButton(self, button):
        returnValue = libpanda._inPflboiuBm(self.this, button.this)
        return returnValue

    
    def getNumButtons(self):
        returnValue = libpanda._inPflbow9C5(self.this)
        return returnValue

    
    def getButton(self, index):
        returnValue = libpanda._inPflboKJca(self.this, index)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def buttonDown(self, button):
        returnValue = libpanda._inPflboigE5(self.this, button.this)
        return returnValue

    
    def buttonUp(self, button):
        returnValue = libpanda._inPflbo3WnW(self.this, button.this)
        return returnValue

    
    def allButtonsUp(self):
        returnValue = libpanda._inPflboeJ_1(self.this)
        return returnValue

    
    def _ModifierButtons__overloaded_isDown_ptrConstModifierButtons_ptrButtonHandle(self, button):
        returnValue = libpanda._inPflbo6vCj(self.this, button.this)
        return returnValue

    
    def _ModifierButtons__overloaded_isDown_ptrConstModifierButtons_int(self, index):
        returnValue = libpanda._inPflboucQV(self.this, index)
        return returnValue

    
    def isAnyDown(self):
        returnValue = libpanda._inPflboS0db(self.this)
        return returnValue

    
    def getPrefix(self):
        returnValue = libpanda._inPflbo9FCN(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPflbobeaY(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpanda._inPflboDRR3(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ModifierButtons__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._ModifierButtons__overloaded_constructor_ptrConstModifierButtons(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def isDown(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._ModifierButtons__overloaded_isDown_ptrConstModifierButtons_int(*_args)
            
            import ButtonHandle
            if isinstance(_args[0], ButtonHandle.ButtonHandle):
                return self._ModifierButtons__overloaded_isDown_ptrConstModifierButtons_ptrButtonHandle(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <ButtonHandle.ButtonHandle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


