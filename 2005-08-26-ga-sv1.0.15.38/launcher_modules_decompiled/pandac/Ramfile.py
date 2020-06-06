# File: R (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class Ramfile(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaexpress._inPKoxtzbIp()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxttwrg:
            libpandaexpress._inPKoxttwrg(self.this)
        

    
    def seek(self, pos):
        returnValue = libpandaexpress._inPKoxtKGYV(self.this, pos)
        return returnValue

    
    def tell(self):
        returnValue = libpandaexpress._inPKoxtQvNL(self.this)
        return returnValue

    
    def read(self, length):
        returnValue = libpandaexpress._inPKoxtAU2w(self.this, length)
        return returnValue

    
    def readline(self):
        returnValue = libpandaexpress._inPKoxtCYbY(self.this)
        return returnValue

    
    def getData(self):
        returnValue = libpandaexpress._inPKoxtBwPQ(self.this)
        return returnValue

    
    def readlines(self):
        lines = []
        line = self.readline()
        while line:
            lines.append(line)
            line = self.readline()
        return lines


