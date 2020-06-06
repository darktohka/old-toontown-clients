# File: C (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CLerpInterval

class CLerpNodePathInterval(CLerpInterval.CLerpInterval, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name, duration, blendType, bakeInStart, node, other):
        self.this = libdirect._inPSpsCneUg(name, duration, blendType, bakeInStart, node.this, other.this)
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
        returnValue = libdirect._inPSpsCTM_v(self.this)
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

    
    def setEndHpr(self, hpr):
        returnValue = libdirect._inPSpsCrohJ(self.this, hpr.this)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setStartScale_ptrCLerpNodePathInterval_ptrConstLVecBase3f(self, scale):
        returnValue = libdirect._inPSpsCMMwu(self.this, scale.this)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setStartScale_ptrCLerpNodePathInterval_float(self, scale):
        returnValue = libdirect._inPSpsCLfsN(self.this, scale)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setEndScale_ptrCLerpNodePathInterval_ptrConstLVecBase3f(self, scale):
        returnValue = libdirect._inPSpsCv_6i(self.this, scale.this)
        return returnValue

    
    def _CLerpNodePathInterval__overloaded_setEndScale_ptrCLerpNodePathInterval_float(self, scale):
        returnValue = libdirect._inPSpsCACOk(self.this, scale)
        return returnValue

    
    def setStartColor(self, color):
        returnValue = libdirect._inPSpsCu8Tw(self.this, color.this)
        return returnValue

    
    def setEndColor(self, color):
        returnValue = libdirect._inPSpsCUGzY(self.this, color.this)
        return returnValue

    
    def setStartColorScale(self, colorScale):
        returnValue = libdirect._inPSpsCIuh7(self.this, colorScale.this)
        return returnValue

    
    def setEndColorScale(self, colorScale):
        returnValue = libdirect._inPSpsCUY_S(self.this, colorScale.this)
        return returnValue

    
    def setEndScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._CLerpNodePathInterval__overloaded_setEndScale_ptrCLerpNodePathInterval_float(_args[0])
            elif isinstance(_args[0], VBase3.VBase3):
                return self._CLerpNodePathInterval__overloaded_setEndScale_ptrCLerpNodePathInterval_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setStartScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._CLerpNodePathInterval__overloaded_setStartScale_ptrCLerpNodePathInterval_float(_args[0])
            elif isinstance(_args[0], VBase3.VBase3):
                return self._CLerpNodePathInterval__overloaded_setStartScale_ptrCLerpNodePathInterval_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


