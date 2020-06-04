# File: P (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class Patcher(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Patcher__overloaded_constructor(self):
        self.this = libpandaexpress._inP2KOdWe93()
        self.userManagesMemory = 1

    
    def _Patcher__overloaded_constructor_ptrBuffer(self, buffer):
        self.this = libpandaexpress._inP2KOd8YxX(buffer.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOddP0w:
            libpandaexpress._inP2KOddP0w(self.this)
        

    
    def initiate(self, patch, infile):
        returnValue = libpandaexpress._inP2KOdYc1E(self.this, patch.this, infile.this)
        return returnValue

    
    def run(self):
        returnValue = libpandaexpress._inP2KOd8N2z(self.this)
        return returnValue

    
    def getProgress(self):
        returnValue = libpandaexpress._inP2KOdw_F5(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Patcher__overloaded_constructor()
        elif numArgs == 1:
            import Buffer
            if isinstance(_args[0], Buffer.Buffer):
                return self._Patcher__overloaded_constructor_ptrBuffer(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Buffer.Buffer> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


