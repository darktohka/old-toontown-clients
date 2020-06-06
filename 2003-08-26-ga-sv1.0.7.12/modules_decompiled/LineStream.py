# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Ostream

class LineStream(Ostream.Ostream, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPelboWztw()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPelbojn21:
            libpanda._inPelbojn21(self.this)
        

    
    def isTextAvailable(self):
        returnValue = libpanda._inPelboqsxw(self.this)
        return returnValue

    
    def getLine(self):
        returnValue = libpanda._inPelboqylt(self.this)
        return returnValue

    
    def hasNewline(self):
        returnValue = libpanda._inPelboTJFM(self.this)
        return returnValue


