# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PGItem

class PGSliderBar(PGItem.PGItem, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PGSliderBar__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPVvimOw_Q(name)
        self.userManagesMemory = 1

    
    def _PGSliderBar__overloaded_constructor(self):
        self.this = libpanda._inPVvimKJhH()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPVvim7cbW()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setup(self, width, height, range):
        returnValue = libpanda._inPVvimjXEx(self.this, width, height, range)
        return returnValue

    
    def setRange(self, range):
        returnValue = libpanda._inPVvimVo99(self.this, range)
        return returnValue

    
    def getRange(self):
        returnValue = libpanda._inPVvim1xy9(self.this)
        return returnValue

    
    def setValue(self, value):
        returnValue = libpanda._inPVvimmiFz(self.this, value)
        return returnValue

    
    def getValue(self):
        returnValue = libpanda._inPVvimEO6y(self.this)
        return returnValue

    
    def getMappedValue(self):
        returnValue = libpanda._inPVvim3H1h(self.this)
        return returnValue

    
    def getUpdatePosition(self):
        returnValue = libpanda._inPVvimyc4z(self.this)
        return returnValue

    
    def setSpeed(self, speed):
        returnValue = libpanda._inPVvimFrsY(self.this, speed)
        return returnValue

    
    def getSpeed(self):
        returnValue = libpanda._inPVvimhOiY(self.this)
        return returnValue

    
    def setScale(self, speed):
        returnValue = libpanda._inPVvim_DjJ(self.this, speed)
        return returnValue

    
    def getScale(self):
        returnValue = libpanda._inPVvimomZJ(self.this)
        return returnValue

    
    def setSliderOnly(self, value):
        returnValue = libpanda._inPVvimT8jS(self.this, value)
        return returnValue

    
    def getSliderOnly(self):
        returnValue = libpanda._inPVvimUBnS(self.this)
        return returnValue

    
    def setNegativeMapping(self, value):
        returnValue = libpanda._inPVvimTKfR(self.this, value)
        return returnValue

    
    def getNegativeMapping(self):
        returnValue = libpanda._inPVvimP2p7(self.this)
        return returnValue

    
    def setBarStyle(self, style):
        returnValue = libpanda._inPVvim0t5j(self.this, style.this)
        return returnValue

    
    def getBarStyle(self):
        returnValue = libpanda._inPVvimPe_R(self.this)
        import PGFrameStyle
        returnObject = PGFrameStyle.PGFrameStyle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getClickEvent(self):
        returnValue = libpanda._inPVvimG7ba(self.this)
        return returnValue

    
    def setSliderButton(self, np, button):
        returnValue = libpanda._inPVvimjMjx(self.this, np.this, button.this)
        return returnValue

    
    def getSliderButton(self):
        returnValue = libpanda._inPVvimccJB(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getLeftButton(self):
        returnValue = libpanda._inPVvim3LGY(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRightButton(self):
        returnValue = libpanda._inPVvimM5Pl(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PGSliderBar__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PGSliderBar__overloaded_constructor_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


