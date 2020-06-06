# File: K (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class KeyboardButton(FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPflbotf0c:
            libpanda._inPflbotf0c(self.this)
        

    
    def _KeyboardButton__overloaded_asciiKey_atomicstring(asciiEquivalent):
        returnValue = libpanda._inPflboubDB(asciiEquivalent)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _KeyboardButton__overloaded_asciiKey_atomicstring = staticmethod(_KeyboardButton__overloaded_asciiKey_atomicstring)
    
    def _KeyboardButton__overloaded_asciiKey_char(asciiEquivalent):
        returnValue = libpanda._inPflbof5oq(asciiEquivalent)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _KeyboardButton__overloaded_asciiKey_char = staticmethod(_KeyboardButton__overloaded_asciiKey_char)
    
    def space():
        returnValue = libpanda._inPflbowvOd()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    space = staticmethod(space)
    
    def backspace():
        returnValue = libpanda._inPflbowFyx()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    backspace = staticmethod(backspace)
    
    def tab():
        returnValue = libpanda._inPflboJuf_()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    tab = staticmethod(tab)
    
    def enter():
        returnValue = libpanda._inPflbojDap()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    enter = staticmethod(enter)
    
    def escape():
        returnValue = libpanda._inPflborLDY()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    escape = staticmethod(escape)
    
    def f1():
        returnValue = libpanda._inPflbo1OGt()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f1 = staticmethod(f1)
    
    def f2():
        returnValue = libpanda._inPflbo2OUJ()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f2 = staticmethod(f2)
    
    def f3():
        returnValue = libpanda._inPflbowOil()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f3 = staticmethod(f3)
    
    def f4():
        returnValue = libpanda._inPflbo9OwB()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f4 = staticmethod(f4)
    
    def f5():
        returnValue = libpanda._inPflbo_O_d()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f5 = staticmethod(f5)
    
    def f6():
        returnValue = libpanda._inPflbo5OM6()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f6 = staticmethod(f6)
    
    def f7():
        returnValue = libpanda._inPflbo6OaW()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f7 = staticmethod(f7)
    
    def f8():
        returnValue = libpanda._inPflbokOoy()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f8 = staticmethod(f8)
    
    def f9():
        returnValue = libpanda._inPflbohO2O()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f9 = staticmethod(f9)
    
    def f10():
        returnValue = libpanda._inPflboLFnR()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f10 = staticmethod(f10)
    
    def f11():
        returnValue = libpanda._inPflboZanY()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f11 = staticmethod(f11)
    
    def f12():
        returnValue = libpanda._inPflbovbnf()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    f12 = staticmethod(f12)
    
    def left():
        returnValue = libpanda._inPflbogrB1()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    left = staticmethod(left)
    
    def right():
        returnValue = libpanda._inPflbobHch()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    right = staticmethod(right)
    
    def up():
        returnValue = libpanda._inPflbouoHo()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    up = staticmethod(up)
    
    def down():
        returnValue = libpanda._inPflbof_Gf()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    down = staticmethod(down)
    
    def pageUp():
        returnValue = libpanda._inPflbo7XIX()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    pageUp = staticmethod(pageUp)
    
    def pageDown():
        returnValue = libpanda._inPflboQsHF()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    pageDown = staticmethod(pageDown)
    
    def home():
        returnValue = libpanda._inPflbor4iM()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    home = staticmethod(home)
    
    def end():
        returnValue = libpanda._inPflbo1_Fy()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    end = staticmethod(end)
    
    def insert():
        returnValue = libpanda._inPflboImkh()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    insert = staticmethod(insert)
    
    def _del():
        returnValue = libpanda._inPflboYsPn()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _del = staticmethod(_del)
    
    def shift():
        returnValue = libpanda._inPflbo0QFY()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    shift = staticmethod(shift)
    
    def control():
        returnValue = libpanda._inPflbon_Xd()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    control = staticmethod(control)
    
    def alt():
        returnValue = libpanda._inPflboaaIW()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    alt = staticmethod(alt)
    
    def meta():
        returnValue = libpanda._inPflbovAt7()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    meta = staticmethod(meta)
    
    def capsLock():
        returnValue = libpanda._inPflbonQ06()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    capsLock = staticmethod(capsLock)
    
    def shiftLock():
        returnValue = libpanda._inPflboKGms()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    shiftLock = staticmethod(shiftLock)
    
    def numLock():
        returnValue = libpanda._inPflboUJca()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    numLock = staticmethod(numLock)
    
    def scrollLock():
        returnValue = libpanda._inPflbok1PW()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    scrollLock = staticmethod(scrollLock)
    
    def printScreen():
        returnValue = libpanda._inPflboetDN()
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    printScreen = staticmethod(printScreen)
    
    def asciiKey(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return KeyboardButton._KeyboardButton__overloaded_asciiKey_char(*_args)
            
            if isinstance(_args[0], types.StringType):
                return KeyboardButton._KeyboardButton__overloaded_asciiKey_atomicstring(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    asciiKey = staticmethod(asciiKey)

