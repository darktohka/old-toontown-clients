# File: S (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CInterval

class ShowInterval(CInterval.CInterval, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _ShowInterval__overloaded_constructor_ptrConstNodePath_atomicstring(self, node, name):
        self.this = libdirect._inPSpsCKLk_(node.this, name)
        self.userManagesMemory = 1

    
    def _ShowInterval__overloaded_constructor_ptrConstNodePath(self, node):
        self.this = libdirect._inPSpsCxxld(node.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inPSpsCDA_5:
            libdirect._inPSpsCDA_5(self.this)
        

    
    def getClassType():
        returnValue = libdirect._inPSpsC1PEe()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                return self._ShowInterval__overloaded_constructor_ptrConstNodePath(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        elif numArgs == 2:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                if isinstance(_args[1], types.StringType):
                    return self._ShowInterval__overloaded_constructor_ptrConstNodePath_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


