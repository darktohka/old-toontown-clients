# File: W (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class WindowProperties(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    ZBottom = 0
    ZNormal = 1
    ZTop = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
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
        if libpanda and libpanda._inPO9cYJOp5:
            libpanda._inPO9cYJOp5(self.this)
        

    
    def getDefault():
        returnValue = libpanda._inPO9cY1hD1()
        returnObject = WindowProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getDefault = staticmethod(getDefault)
    
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
        returnValue = libpanda._inPO9cY_Vsq(self.this, other.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPO9cYIj6c(self.this)
        return returnValue

    
    def isAnySpecified(self):
        returnValue = libpanda._inPO9cY5Hm3(self.this)
        return returnValue

    
    def setOrigin(self, xOrigin, yOrigin):
        returnValue = libpanda._inPO9cY_6s1(self.this, xOrigin, yOrigin)
        return returnValue

    
    def getXOrigin(self):
        returnValue = libpanda._inPO9cYmWEm(self.this)
        return returnValue

    
    def getYOrigin(self):
        returnValue = libpanda._inPO9cYjWge(self.this)
        return returnValue

    
    def hasOrigin(self):
        returnValue = libpanda._inPO9cYeNcv(self.this)
        return returnValue

    
    def clearOrigin(self):
        returnValue = libpanda._inPO9cYJusE(self.this)
        return returnValue

    
    def setSize(self, xSize, ySize):
        returnValue = libpanda._inPO9cY7Ba1(self.this, xSize, ySize)
        return returnValue

    
    def getXSize(self):
        returnValue = libpanda._inPO9cYVfNw(self.this)
        return returnValue

    
    def getYSize(self):
        returnValue = libpanda._inPO9cYQfpo(self.this)
        return returnValue

    
    def hasSize(self):
        returnValue = libpanda._inPO9cY04_T(self.this)
        return returnValue

    
    def clearSize(self):
        returnValue = libpanda._inPO9cYChuY(self.this)
        return returnValue

    
    def setTitle(self, title):
        returnValue = libpanda._inPO9cYEtQx(self.this, title)
        return returnValue

    
    def getTitle(self):
        returnValue = libpanda._inPO9cYLpK6(self.this)
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

    
    def setFixedSize(self, fixedSize):
        returnValue = libpanda._inPO9cYhxLw(self.this, fixedSize)
        return returnValue

    
    def getFixedSize(self):
        returnValue = libpanda._inPO9cYi_y_(self.this)
        return returnValue

    
    def hasFixedSize(self):
        returnValue = libpanda._inPO9cY7wcF(self.this)
        return returnValue

    
    def clearFixedSize(self):
        returnValue = libpanda._inPO9cYPwhp(self.this)
        return returnValue

    
    def setFullscreen(self, fullscreen):
        returnValue = libpanda._inPO9cYq0Uu(self.this, fullscreen)
        return returnValue

    
    def getFullscreen(self):
        returnValue = libpanda._inPO9cYtz98(self.this)
        return returnValue

    
    def hasFullscreen(self):
        returnValue = libpanda._inPO9cYi3nD(self.this)
        return returnValue

    
    def clearFullscreen(self):
        returnValue = libpanda._inPO9cYwgpW(self.this)
        return returnValue

    
    def setForeground(self, foreground):
        returnValue = libpanda._inPO9cYpPA6(self.this, foreground)
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
        returnValue = libpanda._inPO9cYJuBm(self.this, minimized)
        return returnValue

    
    def getMinimized(self):
        returnValue = libpanda._inPO9cYUuGt(self.this)
        return returnValue

    
    def hasMinimized(self):
        returnValue = libpanda._inPO9cYgrwz(self.this)
        return returnValue

    
    def clearMinimized(self):
        returnValue = libpanda._inPO9cYNh8v(self.this)
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
        returnValue = libpanda._inPO9cYXQu6(self.this)
        return returnValue

    
    def setCursorHidden(self, cursorHidden):
        returnValue = libpanda._inPO9cYuag3(self.this, cursorHidden)
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

    
    def setIconFilename(self, iconFilename):
        returnValue = libpanda._inPO9cYvab1(self.this, iconFilename.this)
        return returnValue

    
    def getIconFilename(self):
        returnValue = libpanda._inPO9cYaEsZ(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasIconFilename(self):
        returnValue = libpanda._inPO9cYqEWg(self.this)
        return returnValue

    
    def clearIconFilename(self):
        returnValue = libpanda._inPO9cYOBF2(self.this)
        return returnValue

    
    def setCursorFilename(self, cursorFilename):
        returnValue = libpanda._inPO9cYFBsD(self.this, cursorFilename.this)
        return returnValue

    
    def getCursorFilename(self):
        returnValue = libpanda._inPO9cYzq6A(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasCursorFilename(self):
        returnValue = libpanda._inPO9cYjlkH(self.this)
        return returnValue

    
    def clearCursorFilename(self):
        returnValue = libpanda._inPO9cYImNb(self.this)
        return returnValue

    
    def setZOrder(self, zOrder):
        returnValue = libpanda._inPO9cYonGh(self.this, zOrder)
        return returnValue

    
    def getZOrder(self):
        returnValue = libpanda._inPO9cY_iJo(self.this)
        return returnValue

    
    def hasZOrder(self):
        returnValue = libpanda._inPO9cYuhzu(self.this)
        return returnValue

    
    def clearZOrder(self):
        returnValue = libpanda._inPO9cYLFwW(self.this)
        return returnValue

    
    def addProperties(self, other):
        returnValue = libpanda._inPO9cYcUzF(self.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPO9cYXFj2(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._WindowProperties__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._WindowProperties__overloaded_constructor_ptrConstWindowProperties(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


