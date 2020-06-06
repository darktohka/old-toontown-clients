# File: S (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import LightLensNode

class Spotlight(LightLensNode.LightLensNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPkJyoJNYH(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyo_e_q:
            libpanda._inPkJyo_e_q(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPkJyoinHs()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getExponent(self):
        returnValue = libpanda._inPkJyoylCB(self.this)
        return returnValue

    
    def setExponent(self, exponent):
        returnValue = libpanda._inPkJyonRlj(self.this, exponent)
        return returnValue

    
    def getSpecularColor(self):
        returnValue = libpanda._inPkJyoEy11(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setSpecularColor(self, color):
        returnValue = libpanda._inPkJyohJVa(self.this, color.this)
        return returnValue

    
    def getAttenuation(self):
        returnValue = libpanda._inPkJyo8nFC(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setAttenuation(self, attenuation):
        returnValue = libpanda._inPkJyoFLbM(self.this, attenuation.this)
        return returnValue


