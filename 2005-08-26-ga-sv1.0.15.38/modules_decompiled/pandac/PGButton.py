# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PGItem

class PGButton(PGItem.PGItem, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    SRollover = 2
    SDepressed = 1
    SReady = 0
    SInactive = 3
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPVvimXygN(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClickPrefix():
        returnValue = libpanda._inPVvimh0Du()
        return returnValue

    getClickPrefix = staticmethod(getClickPrefix)
    
    def getClassType():
        returnValue = libpanda._inPVvimj_dU()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath(self, ready):
        returnValue = libpanda._inPVvimpw8O(self.this, ready.this)
        return returnValue

    
    def _PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath(self, ready, depressed):
        returnValue = libpanda._inPVvimBoE3(self.this, ready.this, depressed.this)
        return returnValue

    
    def _PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath(self, ready, depressed, rollover):
        returnValue = libpanda._inPVvim8enX(self.this, ready.this, depressed.this, rollover.this)
        return returnValue

    
    def _PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath(self, ready, depressed, rollover, inactive):
        returnValue = libpanda._inPVvimNB5Z(self.this, ready.this, depressed.this, rollover.this, inactive.this)
        return returnValue

    
    def _PGButton__overloaded_setup_ptrPGButton_atomicstring(self, label):
        returnValue = libpanda._inPVvimYvE_(self.this, label)
        return returnValue

    
    def addClickButton(self, button):
        returnValue = libpanda._inPVvimGBUK(self.this, button.this)
        return returnValue

    
    def removeClickButton(self, button):
        returnValue = libpanda._inPVvim7S68(self.this, button.this)
        return returnValue

    
    def hasClickButton(self, button):
        returnValue = libpanda._inPVvimYiLX(self.this, button.this)
        return returnValue

    
    def isButtonDown(self):
        returnValue = libpanda._inPVvimxDul(self.this)
        return returnValue

    
    def getClickEvent(self, button):
        returnValue = libpanda._inPVvimZ0l2(self.this, button.this)
        return returnValue

    
    def setup(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._PGButton__overloaded_setup_ptrPGButton_atomicstring(*_args)
            
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                return self._PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <NodePath.NodePath> '
        elif numArgs == 2:
            return self._PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath(*_args)
        elif numArgs == 3:
            return self._PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath(*_args)
        elif numArgs == 4:
            return self._PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '


