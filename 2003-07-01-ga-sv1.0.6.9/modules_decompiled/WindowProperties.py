# File: W (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class WindowProperties(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _WindowProperties__overloaded_constructor(self):
        self.this = libpanda._inPO9cYGNZU()
        self.userManagesMemory = 1

    
    def _WindowProperties__overloaded_constructor_ptrConstWindowProperties(self, copy):
        self.this = libpanda._inPO9cYlceF(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPO9cYIOp5:
            libpanda._inPO9cYIOp5(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPO9cYZC_R(self.this, copy.this)
        returnObject = WindowProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def eq(self, other):
        returnValue = libpanda._inPO9cYgRMD(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPO9cYxVsq(self.this, other.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPO9cYIj6c(self.this)
        return returnValue

    
    def isAnySpecified(self):
        returnValue = libpanda._inPO9cY4Hm3(self.this)
        return returnValue

    
    def setOrigin(self, xOrigin, yOrigin):
        returnValue = libpanda._inPO9cY96s1(self.this, xOrigin, yOrigin)
        return returnValue

    
    def getXOrigin(self):
        returnValue = libpanda._inPO9cYnWEm(self.this)
        return returnValue

    
    def getYOrigin(self):
        returnValue = libpanda._inPO9cYjWge(self.this)
        return returnValue

    
    def hasOrigin(self):
        returnValue = libpanda._inPO9cYfNcv(self.this)
        return returnValue

    
    def clearOrigin(self):
        returnValue = libpanda._inPO9cYJusE(self.this)
        return returnValue

    
    def setSize(self, xSize, ySize):
        returnValue = libpanda._inPO9cY6Ba1(self.this, xSize, ySize)
        return returnValue

    
    def getXSize(self):
        returnValue = libpanda._inPO9cYUfNw(self.this)
        return returnValue

    
    def getYSize(self):
        returnValue = libpanda._inPO9cYTfpo(self.this)
        return returnValue

    
    def hasSize(self):
        returnValue = libpanda._inPO9cY04_T(self.this)
        return returnValue

    
    def clearSize(self):
        returnValue = libpanda._inPO9cYChuY(self.this)
        return returnValue

    
    def setTitle(self, title):
        returnValue = libpanda._inPO9cYDtQx(self.this, title)
        return returnValue

    
    def getTitle(self):
        returnValue = libpanda._inPO9cYMpK6(self.this)
        return returnValue

    
    def hasTitle(self):
        returnValue = libpanda._inPO9cY4p0A(self.this)
        return returnValue

    
    def clearTitle(self):
        returnValue = libpanda._inPO9cY2KzX(self.this)
        return returnValue

    
    def setUndecorated(self, undecorated):
        returnValue = libpanda._inPO9cY1wGY(self.this, undecorated)
        return returnValue

    
    def getUndecorated(self):
        returnValue = libpanda._inPO9cYJtRY(self.this)
        return returnValue

    
    def hasUndecorated(self):
        returnValue = libpanda._inPO9cYds7e(self.this)
        return returnValue

    
    def clearUndecorated(self):
        returnValue = libpanda._inPO9cY6EZL(self.this)
        return returnValue

    
    def setFullscreen(self, fullscreen):
        returnValue = libpanda._inPO9cYp0Uu(self.this, fullscreen)
        return returnValue

    
    def getFullscreen(self):
        returnValue = libpanda._inPO9cYqz98(self.this)
        return returnValue

    
    def hasFullscreen(self):
        returnValue = libpanda._inPO9cYi3nD(self.this)
        return returnValue

    
    def clearFullscreen(self):
        returnValue = libpanda._inPO9cYwgpW(self.this)
        return returnValue

    
    def setForeground(self, foreground):
        returnValue = libpanda._inPO9cYuPA6(self.this, foreground)
        return returnValue

    
    def getForeground(self):
        returnValue = libpanda._inPO9cYrFnI(self.this)
        return returnValue

    
    def hasForeground(self):
        returnValue = libpanda._inPO9cY7CRP(self.this)
        return returnValue

    
    def clearForeground(self):
        returnValue = libpanda._inPO9cYNghP(self.this)
        return returnValue

    
    def setMinimized(self, minimized):
        returnValue = libpanda._inPO9cYKuBm(self.this, minimized)
        return returnValue

    
    def getMinimized(self):
        returnValue = libpanda._inPO9cYVuGt(self.this)
        return returnValue

    
    def hasMinimized(self):
        returnValue = libpanda._inPO9cYhrwz(self.this)
        return returnValue

    
    def clearMinimized(self):
        returnValue = libpanda._inPO9cYMh8v(self.this)
        return returnValue

    
    def setOpen(self, open):
        returnValue = libpanda._inPO9cY0PHZ(self.this, open)
        return returnValue

    
    def getOpen(self):
        returnValue = libpanda._inPO9cYnBqS(self.this)
        return returnValue

    
    def hasOpen(self):
        returnValue = libpanda._inPO9cY3AUZ(self.this)
        return returnValue

    
    def clearOpen(self):
        returnValue = libpanda._inPO9cYUQu6(self.this)
        return returnValue

    
    def setCursorHidden(self, cursorHidden):
        returnValue = libpanda._inPO9cYvag3(self.this, cursorHidden)
        return returnValue

    
    def getCursorHidden(self):
        returnValue = libpanda._inPO9cYILMV(self.this)
        return returnValue

    
    def hasCursorHidden(self):
        returnValue = libpanda._inPO9cY0O2b(self.this)
        return returnValue

    
    def clearCursorHidden(self):
        returnValue = libpanda._inPO9cYnQoK(self.this)
        return returnValue

    
    def addProperties(self, other):
        returnValue = libpanda._inPO9cYcUzF(self.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPO9cYYFj2(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._WindowProperties__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], WindowProperties):
                return self._WindowProperties__overloaded_constructor_ptrConstWindowProperties(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <WindowProperties> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


