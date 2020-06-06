# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPWvimXygN(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClickPrefix():
        returnValue = libpanda._inPWvimm0Du()
        return returnValue

    getClickPrefix = staticmethod(getClickPrefix)
    
    def getClassType():
        returnValue = libpanda._inPWvimj_dU()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath(self, ready):
        returnValue = libpanda._inPWvimpw8O(self.this, ready.this)
        return returnValue

    
    def _PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath(self, ready, depressed):
        returnValue = libpanda._inPWvimAoE3(self.this, ready.this, depressed.this)
        return returnValue

    
    def _PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath(self, ready, depressed, rollover):
        returnValue = libpanda._inPWvim8enX(self.this, ready.this, depressed.this, rollover.this)
        return returnValue

    
    def _PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath(self, ready, depressed, rollover, inactive):
        returnValue = libpanda._inPWvimNB5Z(self.this, ready.this, depressed.this, rollover.this, inactive.this)
        return returnValue

    
    def _PGButton__overloaded_setup_ptrPGButton_atomicstring(self, label):
        returnValue = libpanda._inPWvimXvE_(self.this, label)
        return returnValue

    
    def addClickButton(self, button):
        returnValue = libpanda._inPWvimGBUK(self.this, button.this)
        return returnValue

    
    def removeClickButton(self, button):
        returnValue = libpanda._inPWvim6S68(self.this, button.this)
        return returnValue

    
    def hasClickButton(self, button):
        returnValue = libpanda._inPWvimYiLX(self.this, button.this)
        return returnValue

    
    def getClickEvent(self, button):
        returnValue = libpanda._inPWvima0l2(self.this, button.this)
        return returnValue

    
    def setup(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import NodePath
            if isinstance(_args[0], types.StringType):
                return self._PGButton__overloaded_setup_ptrPGButton_atomicstring(_args[0])
            elif isinstance(_args[0], NodePath.NodePath):
                return self._PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <NodePath.NodePath> '
        elif numArgs == 2:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import NodePath
                if isinstance(_args[1], NodePath.NodePath):
                    return self._PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <NodePath.NodePath> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        elif numArgs == 3:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import NodePath
                if isinstance(_args[1], NodePath.NodePath):
                    import NodePath
                    if isinstance(_args[2], NodePath.NodePath):
                        return self._PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <NodePath.NodePath> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <NodePath.NodePath> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        elif numArgs == 4:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import NodePath
                if isinstance(_args[1], NodePath.NodePath):
                    import NodePath
                    if isinstance(_args[2], NodePath.NodePath):
                        import NodePath
                        if isinstance(_args[3], NodePath.NodePath):
                            return self._PGButton__overloaded_setup_ptrPGButton_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath_ptrConstNodePath(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <NodePath.NodePath> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <NodePath.NodePath> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <NodePath.NodePath> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '


