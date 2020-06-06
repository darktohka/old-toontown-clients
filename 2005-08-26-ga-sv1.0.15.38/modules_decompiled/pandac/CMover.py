# File: C (Python 2.2)

import types
import libotp
import libotpDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class CMover(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libotpDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CMover__overloaded_constructor_ptrNodePath_float_float(self, objNodePath, fwdSpeed, rotSpeed):
        self.this = libotp._inPYe45g4dY(objNodePath.this, fwdSpeed, rotSpeed)
        self.userManagesMemory = 1

    
    def _CMover__overloaded_constructor_ptrNodePath_float(self, objNodePath, fwdSpeed):
        self.this = libotp._inPYe457_Sr(objNodePath.this, fwdSpeed)
        self.userManagesMemory = 1

    
    def _CMover__overloaded_constructor_ptrNodePath(self, objNodePath):
        self.this = libotp._inPYe45Cqga(objNodePath.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libotp._inPYe45xEsw()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setFwdSpeed(self, fwdSpeed):
        returnValue = libotp._inPYe4528SC(self.this, fwdSpeed)
        return returnValue

    
    def setRotSpeed(self, rotSpeed):
        returnValue = libotp._inPYe45wyrP(self.this, rotSpeed)
        return returnValue

    
    def getFwdSpeed(self):
        returnValue = libotp._inPYe45SWm2(self.this)
        return returnValue

    
    def getRotSpeed(self):
        returnValue = libotp._inPYe45Vb_D(self.this)
        return returnValue

    
    def addCImpulse(self, name, impulse):
        returnValue = libotp._inPYe456CKx(self.this, name, impulse.this)
        return returnValue

    
    def removeCImpulse(self, name):
        returnValue = libotp._inPYe45IhB9(self.this, name)
        return returnValue

    
    def _CMover__overloaded_processCImpulses_ptrCMover_float(self, dt):
        returnValue = libotp._inPYe45oXrR(self.this, dt)
        return returnValue

    
    def _CMover__overloaded_processCImpulses_ptrCMover(self):
        returnValue = libotp._inPYe45JjcH(self.this)
        return returnValue

    
    def integrate(self):
        returnValue = libotp._inPYe45J0F6(self.this)
        return returnValue

    
    def addForce(self, force):
        returnValue = libotp._inPYe45atG_(self.this, force.this)
        return returnValue

    
    def addRotForce(self, rotForce):
        returnValue = libotp._inPYe453mQd(self.this, rotForce.this)
        return returnValue

    
    def addShove(self, shove):
        returnValue = libotp._inPYe45aq4P(self.this, shove.this)
        return returnValue

    
    def addRotShove(self, rotShove):
        returnValue = libotp._inPYe45vGYi(self.this, rotShove.this)
        return returnValue

    
    def getNodePath(self):
        returnValue = libotp._inPYe45lqIw(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getDt(self):
        returnValue = libotp._inPYe45cvr7(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CMover__overloaded_constructor_ptrNodePath(*_args)
        elif numArgs == 2:
            return self._CMover__overloaded_constructor_ptrNodePath_float(*_args)
        elif numArgs == 3:
            return self._CMover__overloaded_constructor_ptrNodePath_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def processCImpulses(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CMover__overloaded_processCImpulses_ptrCMover(*_args)
        elif numArgs == 1:
            return self._CMover__overloaded_processCImpulses_ptrCMover_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


