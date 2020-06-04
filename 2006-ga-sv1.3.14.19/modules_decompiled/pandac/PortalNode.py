# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class PortalNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyoI_Vv(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyo0yAx:
            libpanda._inPnJyo0yAx(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyo0Yop()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setPortalMask(self, mask):
        returnValue = libpanda._inPnJyotMRk(self.this, mask.this)
        return returnValue

    
    def setFromPortalMask(self, mask):
        returnValue = libpanda._inPnJyoSi2m(self.this, mask.this)
        return returnValue

    
    def setIntoPortalMask(self, mask):
        returnValue = libpanda._inPnJyoYCon(self.this, mask.this)
        return returnValue

    
    def getFromPortalMask(self):
        returnValue = libpanda._inPnJyoK6im(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getIntoPortalMask(self):
        returnValue = libpanda._inPnJyoMSVn(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setPortalGeom(self, flag):
        returnValue = libpanda._inPnJyohvNY(self.this, flag)
        return returnValue

    
    def getPortalGeom(self):
        returnValue = libpanda._inPnJyoWqMg(self.this)
        return returnValue

    
    def clearVertices(self):
        returnValue = libpanda._inPnJyojFbb(self.this)
        return returnValue

    
    def addVertex(self, vertex):
        returnValue = libpanda._inPnJyopPIP(self.this, vertex.this)
        return returnValue

    
    def getNumVertices(self):
        returnValue = libpanda._inPnJyo7Gy1(self.this)
        return returnValue

    
    def getVertex(self, n):
        returnValue = libpanda._inPnJyoXSGA(self.this, n)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setZoneIn(self, zone):
        returnValue = libpanda._inPnJyoaDBy(self.this, zone.this)
        return returnValue

    
    def getZoneIn(self):
        returnValue = libpanda._inPnJyoiOTw(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setZoneOut(self, zone):
        returnValue = libpanda._inPnJyoi_8_(self.this, zone.this)
        return returnValue

    
    def getZoneOut(self):
        returnValue = libpanda._inPnJyomziJ(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setVisible(self, value):
        returnValue = libpanda._inPnJyovbBN(self.this, value)
        return returnValue

    
    def isVisible(self):
        returnValue = libpanda._inPnJyoKXV7(self.this)
        return returnValue


