# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggBinMaker

class EggPolysetMaker(EggBinMaker.EggBinMaker, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    BNNone = 0
    BNPolyset = 1
    PPolyColor = 32
    PBface = 512
    PHasVertexNormal = 128
    PTexture = 2
    PHasPolyNormal = 64
    PHasTexture = 1
    PHasMaterial = 4
    PHasVertexColor = 256
    PMaterial = 8
    PHasPolyColor = 16
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaegg._inPkAOMS2yw()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMHPpU:
            libpandaegg._inPkAOMHPpU(self.this)
        

    
    def setProperties(self, properties):
        returnValue = libpandaegg._inPkAOMlQny(self.this, properties)
        return returnValue


