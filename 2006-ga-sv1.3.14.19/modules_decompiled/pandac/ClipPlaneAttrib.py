# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RenderAttrib

class ClipPlaneAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    OAdd = 1
    ORemove = 2
    OSet = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyos0_S:
            libpanda._inPnJyos0_S(self.this)
        

    
    def makeAllOff():
        returnValue = libpanda._inPnJyoIhtw()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeAllOff = staticmethod(makeAllOff)
    
    def _ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode(op, planeBase):
        returnValue = libpanda._inPnJyoSf11(op, planeBase.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode = staticmethod(_ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode)
    
    def _ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode(op, plane1, plane2):
        returnValue = libpanda._inPnJyoAiXQ(op, plane1.this, plane2.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode = staticmethod(_ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode)
    
    def _ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode(op, plane1, plane2, plane3):
        returnValue = libpanda._inPnJyoCohu(op, plane1.this, plane2.this, plane3.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode = staticmethod(_ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode)
    
    def _ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode(op, plane1, plane2, plane3, plane4):
        returnValue = libpanda._inPnJyouzti(op, plane1.this, plane2.this, plane3.this, plane4.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode = staticmethod(_ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode)
    
    def getClassType():
        returnValue = libpanda._inPnJyoiYmd()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getOperation(self):
        returnValue = libpanda._inPnJyojfgg(self.this)
        return returnValue

    
    def getNumPlanes(self):
        returnValue = libpanda._inPnJyohARe(self.this)
        return returnValue

    
    def getPlane(self, n):
        returnValue = libpanda._inPnJyoS5RG(self.this, n)
        import PlaneNode
        returnObject = PlaneNode.PlaneNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def hasPlane(self, planeBase):
        returnValue = libpanda._inPnJyoxcJo(self.this, planeBase.this)
        return returnValue

    
    def addPlane(self, planeBase):
        returnValue = libpanda._inPnJyohmfX(self.this, planeBase.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removePlane(self, planeBase):
        returnValue = libpanda._inPnJyor4Ff(self.this, planeBase.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def isIdentity(self):
        returnValue = libpanda._inPnJyo1m0T(self.this)
        return returnValue

    
    def isAllOff(self):
        returnValue = libpanda._inPnJyoXopr(self.this)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return ClipPlaneAttrib._ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode(*_args)
        elif numArgs == 3:
            return ClipPlaneAttrib._ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode(*_args)
        elif numArgs == 4:
            return ClipPlaneAttrib._ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode(*_args)
        elif numArgs == 5:
            return ClipPlaneAttrib._ClipPlaneAttrib__overloaded_make___enum__Operation_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode_ptrPlaneNode(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 5 '

    make = staticmethod(make)

