# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DataNode

class TrackerNode(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, client, deviceName):
        self.this = libpanda._inPOfOPHyCC(client.this, deviceName)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPOfOPbA7p()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isValid(self):
        returnValue = libpanda._inPOfOPDEoZ(self.this)
        return returnValue

    
    def getPos(self):
        returnValue = libpanda._inPOfOPfpbJ(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getOrient(self):
        returnValue = libpanda._inPOfOPc1d9(self.this)
        import LOrientationf
        returnObject = LOrientationf.LOrientationf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getTransform(self):
        returnValue = libpanda._inPOfOPzbsf(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getTime(self):
        returnValue = libpanda._inPOfOPKr_I(self.this)
        return returnValue

    
    def hasTime(self):
        returnValue = libpanda._inPOfOPgtUM(self.this)
        return returnValue

    
    def setTrackerCoordinateSystem(self, cs):
        returnValue = libpanda._inPOfOPSq_7(self.this, cs)
        return returnValue

    
    def getTrackerCoordinateSystem(self):
        returnValue = libpanda._inPOfOPOtgh(self.this)
        return returnValue

    
    def setGraphCoordinateSystem(self, cs):
        returnValue = libpanda._inPOfOPgH95(self.this, cs)
        return returnValue

    
    def getGraphCoordinateSystem(self):
        returnValue = libpanda._inPOfOP_MOP(self.this)
        return returnValue


