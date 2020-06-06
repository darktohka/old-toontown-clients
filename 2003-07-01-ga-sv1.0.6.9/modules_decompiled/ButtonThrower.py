# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DataNode

class ButtonThrower(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPziw574xy(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPziw5mOhU()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setPrefix(self, prefix):
        returnValue = libpanda._inPziw5_tb8(self.this, prefix)
        return returnValue

    
    def hasPrefix(self):
        returnValue = libpanda._inPziw59nYr(self.this)
        return returnValue

    
    def getPrefix(self):
        returnValue = libpanda._inPziw53m_a(self.this)
        return returnValue

    
    def addParameter(self, obj):
        returnValue = libpanda._inPziw5EaR_(self.this, obj.this)
        return returnValue

    
    def getNumParameters(self):
        returnValue = libpanda._inPziw5aj99(self.this)
        return returnValue

    
    def getParameter(self, n):
        returnValue = libpanda._inPziw5ZmFl(self.this, n)
        import EventParameter
        returnObject = EventParameter.EventParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getModifierButtons(self):
        returnValue = libpanda._inPziw5GlsX(self.this)
        import ModifierButtons
        returnObject = ModifierButtons.ModifierButtons(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setModifierButtons(self, mods):
        returnValue = libpanda._inPziw57l_D(self.this, mods.this)
        return returnValue

    
    def setThrowButtonsActive(self, flag):
        returnValue = libpanda._inPziw5uTqR(self.this, flag)
        return returnValue

    
    def getThrowButtonsActive(self):
        returnValue = libpanda._inPziw55I8a(self.this)
        return returnValue

    
    def addThrowButton(self, mods, button):
        returnValue = libpanda._inPziw5Ji9T(self.this, mods.this, button.this)
        return returnValue

    
    def removeThrowButton(self, mods, button):
        returnValue = libpanda._inPziw5psxI(self.this, mods.this, button.this)
        return returnValue

    
    def _ButtonThrower__overloaded_hasThrowButton_ptrConstButtonThrower_ptrConstButtonHandle(self, button):
        returnValue = libpanda._inPziw5UvSd(self.this, button.this)
        return returnValue

    
    def _ButtonThrower__overloaded_hasThrowButton_ptrConstButtonThrower_ptrConstModifierButtons_ptrConstButtonHandle(self, mods, button):
        returnValue = libpanda._inPziw5dX_g(self.this, mods.this, button.this)
        return returnValue

    
    def clearThrowButtons(self):
        returnValue = libpanda._inPziw5NSSv(self.this)
        return returnValue

    
    def hasThrowButton(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import ButtonHandle
            if isinstance(_args[0], ButtonHandle.ButtonHandle):
                return self._ButtonThrower__overloaded_hasThrowButton_ptrConstButtonThrower_ptrConstButtonHandle(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <ButtonHandle.ButtonHandle> '
        elif numArgs == 2:
            import ModifierButtons
            if isinstance(_args[0], ModifierButtons.ModifierButtons):
                import ButtonHandle
                if isinstance(_args[1], ButtonHandle.ButtonHandle):
                    return self._ButtonThrower__overloaded_hasThrowButton_ptrConstButtonThrower_ptrConstModifierButtons_ptrConstButtonHandle(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <ButtonHandle.ButtonHandle> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <ModifierButtons.ModifierButtons> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


