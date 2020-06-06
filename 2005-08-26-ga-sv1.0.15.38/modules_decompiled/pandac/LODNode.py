# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class LODNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyonKZh(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoqgkj:
            libpanda._inPnJyoqgkj(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyolHCR()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def addSwitch(self, _in, out):
        returnValue = libpanda._inPnJyoRFoz(self.this, _in, out)
        return returnValue

    
    def setSwitch(self, index, _in, out):
        returnValue = libpanda._inPnJyohpdI(self.this, index, _in, out)
        return returnValue

    
    def clearSwitches(self):
        returnValue = libpanda._inPnJyo25DC(self.this)
        return returnValue

    
    def getNumSwitches(self):
        returnValue = libpanda._inPnJyob65Z(self.this)
        return returnValue

    
    def getIn(self, index):
        returnValue = libpanda._inPnJyoSHPo(self.this, index)
        return returnValue

    
    def getOut(self, index):
        returnValue = libpanda._inPnJyoWO_6(self.this, index)
        return returnValue

    
    def getLowestSwitch(self):
        returnValue = libpanda._inPnJyoXVB9(self.this)
        return returnValue

    
    def getHighestSwitch(self):
        returnValue = libpanda._inPnJyo0Jag(self.this)
        return returnValue

    
    def forceSwitch(self, index):
        returnValue = libpanda._inPnJyos5Rf(self.this, index)
        return returnValue

    
    def clearForceSwitch(self):
        returnValue = libpanda._inPnJyokueh(self.this)
        return returnValue

    
    def setCenter(self, center):
        returnValue = libpanda._inPnJyoPHp_(self.this, center.this)
        return returnValue

    
    def getCenter(self):
        returnValue = libpanda._inPnJyo8mat(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject


