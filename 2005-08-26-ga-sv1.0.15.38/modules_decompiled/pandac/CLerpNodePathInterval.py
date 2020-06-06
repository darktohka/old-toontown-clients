# File: C (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CLerpInterval

class CLerpNodePathInterval(CLerpInterval.CLerpInterval, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name, duration, blendType, bakeInStart, fluid, node, other):
        self.this = libdirect._inPSpsCdIA4(name, duration, blendType, bakeInStart, fluid, node.this, other.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inPSpsChQkQ:
            libdirect._inPSpsChQkQ(self.this)
        

    
    def getClassType():
        returnValue = libdirect._inPSpsCdTLY()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getNode(self):
        returnValue = libdirect._inPSpsC9PvW(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getOther(self):
        returnValue = libdirect._inPSpsCSM_v(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setStartPos(self, pos):
        returnValue = libdirect._inPSpsCaRxY(self.this, pos.this)
        return returnValue

    
    def setEndPos(self, pos):
        returnValue = libdirect._inPSpsCJiNY(self.this, pos.this)
        return returnValue

    
    def setStartHpr(self, hpr):
        returnValue = libdirect._inPSpsClyYW(self.this, hpr.this)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setEndHpr_ptrCLerpNodePathInterval_ptrConstLQuaternionf(self, quat):
        returnValue = libdirect._inPSpsCRVh4(self.this, quat.this)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setEndHpr_ptrCLerpNodePathInterval_ptrConstLVecBase3f(self, hpr):
        returnValue = libdirect._inPSpsCrohJ(self.this, hpr.this)
        return returnValue

    
    def setStartQuat(self, quat):
        returnValue = libdirect._inPSpsCc5Xe(self.this, quat.this)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setEndQuat_ptrCLerpNodePathInterval_ptrConstLQuaternionf(self, quat):
        returnValue = libdirect._inPSpsCt__n(self.this, quat.this)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setEndQuat_ptrCLerpNodePathInterval_ptrConstLVecBase3f(self, hpr):
        returnValue = libdirect._inPSpsCGCRI(self.this, hpr.this)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setStartScale_ptrCLerpNodePathInterval_ptrConstLVecBase3f(self, scale):
        returnValue = libdirect._inPSpsCPMwu(self.this, scale.this)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setStartScale_ptrCLerpNodePathInterval_float(self, scale):
        returnValue = libdirect._inPSpsCLfsN(self.this, scale)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setEndScale_ptrCLerpNodePathInterval_ptrConstLVecBase3f(self, scale):
        returnValue = libdirect._inPSpsCu_6i(self.this, scale.this)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setEndScale_ptrCLerpNodePathInterval_float(self, scale):
        returnValue = libdirect._inPSpsCBCOk(self.this, scale)
        return returnValue

    
    def setStartShear(self, shear):
        returnValue = libdirect._inPSpsCyKML(self.this, shear.this)
        return returnValue

    
    def setEndShear(self, shear):
        returnValue = libdirect._inPSpsC1jlK(self.this, shear.this)
        return returnValue

    
    def setStartColor(self, color):
        returnValue = libdirect._inPSpsCt8Tw(self.this, color.this)
        return returnValue

    
    def setEndColor(self, color):
        returnValue = libdirect._inPSpsCUGzY(self.this, color.this)
        return returnValue

    
    def setStartColorScale(self, colorScale):
        returnValue = libdirect._inPSpsCJuh7(self.this, colorScale.this)
        return returnValue

    
    def setEndColorScale(self, colorScale):
        returnValue = libdirect._inPSpsCUY_S(self.this, colorScale.this)
        return returnValue

    
    def setEndQuat(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._CLerpNodePathInterval__overloaded_setEndQuat_ptrCLerpNodePathInterval_ptrConstLVecBase3f(*_args)
            
            import Quat
            if isinstance(_args[0], Quat.Quat):
                return self._CLerpNodePathInterval__overloaded_setEndQuat_ptrCLerpNodePathInterval_ptrConstLQuaternionf(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> <Quat.Quat> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setEndScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._CLerpNodePathInterval__overloaded_setEndScale_ptrCLerpNodePathInterval_float(*_args)
            
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._CLerpNodePathInterval__overloaded_setEndScale_ptrCLerpNodePathInterval_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setEndHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._CLerpNodePathInterval__overloaded_setEndHpr_ptrCLerpNodePathInterval_ptrConstLVecBase3f(*_args)
            
            import Quat
            if isinstance(_args[0], Quat.Quat):
                return self._CLerpNodePathInterval__overloaded_setEndHpr_ptrCLerpNodePathInterval_ptrConstLQuaternionf(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> <Quat.Quat> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setStartScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._CLerpNodePathInterval__overloaded_setStartScale_ptrCLerpNodePathInterval_float(*_args)
            
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._CLerpNodePathInterval__overloaded_setStartScale_ptrCLerpNodePathInterval_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


