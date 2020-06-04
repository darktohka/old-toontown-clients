# File: S (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Iostream

class SocketStream(Iostream.Iostream, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdAW2i:
            libpandaexpress._inP2KOdAW2i(self.this)
        

    
    def receiveDatagram(self, dg):
        returnValue = libpandaexpress._inP2KOdD7eO(self.this, dg.this)
        return returnValue

    
    def sendDatagram(self, dg):
        returnValue = libpandaexpress._inP2KOdKdSV(self.this, dg.this)
        return returnValue

    
    def isClosed(self):
        returnValue = libpandaexpress._inP2KOdB8Lh(self.this)
        return returnValue


