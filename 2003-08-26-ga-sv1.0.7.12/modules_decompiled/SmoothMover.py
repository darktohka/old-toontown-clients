# File: S (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import FFIExternalObject

class SmoothMover(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    SMOn = 1
    SMOff = 0
    PMOff = 0
    PMOn = 1
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libdirect._inPx5Y6PfNd()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inPx5Y6qnlW:
            libdirect._inPx5Y6qnlW(self.this)
        

    
    def setSmoothMode(mode):
        returnValue = libdirect._inPx5Y6_UPz(mode)
        return returnValue

    setSmoothMode = staticmethod(setSmoothMode)
    
    def getSmoothMode():
        returnValue = libdirect._inPx5Y6jHbf()
        return returnValue

    getSmoothMode = staticmethod(getSmoothMode)
    
    def setPredictionMode(mode):
        returnValue = libdirect._inPx5Y65I6v(mode)
        return returnValue

    setPredictionMode = staticmethod(setPredictionMode)
    
    def getPredictionMode():
        returnValue = libdirect._inPx5Y6sYHY()
        return returnValue

    getPredictionMode = staticmethod(getPredictionMode)
    
    def setDelay(delay):
        returnValue = libdirect._inPx5Y6B_i_(delay)
        return returnValue

    setDelay = staticmethod(setDelay)
    
    def getDelay():
        returnValue = libdirect._inPx5Y64AIs()
        return returnValue

    getDelay = staticmethod(getDelay)
    
    def setAcceptClockSkew(flag):
        returnValue = libdirect._inPx5Y6zWkf(flag)
        return returnValue

    setAcceptClockSkew = staticmethod(setAcceptClockSkew)
    
    def getAcceptClockSkew():
        returnValue = libdirect._inPx5Y6gmDB()
        return returnValue

    getAcceptClockSkew = staticmethod(getAcceptClockSkew)
    
    def setMaxPositionAge(age):
        returnValue = libdirect._inPx5Y631KR(age)
        return returnValue

    setMaxPositionAge = staticmethod(setMaxPositionAge)
    
    def getMaxPositionAge():
        returnValue = libdirect._inPx5Y6H52x()
        return returnValue

    getMaxPositionAge = staticmethod(getMaxPositionAge)
    
    def setResetVelocityAge(age):
        returnValue = libdirect._inPx5Y6Dgwu(age)
        return returnValue

    setResetVelocityAge = staticmethod(setResetVelocityAge)
    
    def getResetVelocityAge():
        returnValue = libdirect._inPx5Y6fH9v()
        return returnValue

    getResetVelocityAge = staticmethod(getResetVelocityAge)
    
    def _SmoothMover__overloaded_setScale_ptrSmoothMover_ptrConstLVecBase3f(self, scale):
        returnValue = libdirect._inPx5Y6VYzt(self.this, scale.this)
        return returnValue

    
    def _SmoothMover__overloaded_setScale_ptrSmoothMover_float_float_float(self, sx, sy, sz):
        returnValue = libdirect._inPx5Y6wGHJ(self.this, sx, sy, sz)
        return returnValue

    
    def setSx(self, sx):
        returnValue = libdirect._inPx5Y6oQsW(self.this, sx)
        return returnValue

    
    def setSy(self, sy):
        returnValue = libdirect._inPx5Y6evtd(self.this, sy)
        return returnValue

    
    def setSz(self, sz):
        returnValue = libdirect._inPx5Y6Putk(self.this, sz)
        return returnValue

    
    def _SmoothMover__overloaded_setPos_ptrSmoothMover_ptrConstLVecBase3f(self, pos):
        returnValue = libdirect._inPx5Y6O99C(self.this, pos.this)
        return returnValue

    
    def _SmoothMover__overloaded_setPos_ptrSmoothMover_float_float_float(self, x, y, z):
        returnValue = libdirect._inPx5Y651r_(self.this, x, y, z)
        return returnValue

    
    def setX(self, x):
        returnValue = libdirect._inPx5Y6vc6s(self.this, x)
        return returnValue

    
    def setY(self, y):
        returnValue = libdirect._inPx5Y6tcIJ(self.this, y)
        return returnValue

    
    def setZ(self, z):
        returnValue = libdirect._inPx5Y6gcWl(self.this, z)
        return returnValue

    
    def _SmoothMover__overloaded_setHpr_ptrSmoothMover_ptrConstLVecBase3f(self, hpr):
        returnValue = libdirect._inPx5Y6HbNI(self.this, hpr.this)
        return returnValue

    
    def _SmoothMover__overloaded_setHpr_ptrSmoothMover_float_float_float(self, h, p, r):
        returnValue = libdirect._inPx5Y63N7D(self.this, h, p, r)
        return returnValue

    
    def setH(self, h):
        returnValue = libdirect._inPx5Y6Udap(self.this, h)
        return returnValue

    
    def setP(self, p):
        returnValue = libdirect._inPx5Y67cKL(self.this, p)
        return returnValue

    
    def setR(self, r):
        returnValue = libdirect._inPx5Y68cmD(self.this, r)
        return returnValue

    
    def setMat(self, mat):
        returnValue = libdirect._inPx5Y6eUzA(self.this, mat.this)
        return returnValue

    
    def setPhonyTimestamp(self):
        returnValue = libdirect._inPx5Y6h7VW(self.this)
        return returnValue

    
    def setTimestamp(self, timestamp):
        returnValue = libdirect._inPx5Y6lAg7(self.this, timestamp)
        return returnValue

    
    def markPosition(self):
        returnValue = libdirect._inPx5Y6GTFs(self.this)
        return returnValue

    
    def clearPositions(self, resetVelocity):
        returnValue = libdirect._inPx5Y6_lt8(self.this, resetVelocity)
        return returnValue

    
    def _SmoothMover__overloaded_computeSmoothPosition_ptrSmoothMover(self):
        returnValue = libdirect._inPx5Y6NhMU(self.this)
        return returnValue

    
    def _SmoothMover__overloaded_computeSmoothPosition_ptrSmoothMover_double(self, timestamp):
        returnValue = libdirect._inPx5Y6CIgu(self.this, timestamp)
        return returnValue

    
    def getLatestPosition(self):
        returnValue = libdirect._inPx5Y6p1_G(self.this)
        return returnValue

    
    def getSmoothPos(self):
        returnValue = libdirect._inPx5Y67_MU(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getSmoothHpr(self):
        returnValue = libdirect._inPx5Y6TcHB(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getSmoothMat(self):
        returnValue = libdirect._inPx5Y6HMYE(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getSmoothForwardVelocity(self):
        returnValue = libdirect._inPx5Y6DxNc(self.this)
        return returnValue

    
    def getSmoothRotationalVelocity(self):
        returnValue = libdirect._inPx5Y6lTjX(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libdirect._inPx5Y6WhUX(self.this, out.this)
        return returnValue

    
    def write(self, out):
        returnValue = libdirect._inPx5Y6ednE(self.this, out.this)
        return returnValue

    
    def setPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._SmoothMover__overloaded_setPos_ptrSmoothMover_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._SmoothMover__overloaded_setPos_ptrSmoothMover_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._SmoothMover__overloaded_setHpr_ptrSmoothMover_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._SmoothMover__overloaded_setHpr_ptrSmoothMover_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def computeSmoothPosition(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._SmoothMover__overloaded_computeSmoothPosition_ptrSmoothMover()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._SmoothMover__overloaded_computeSmoothPosition_ptrSmoothMover_double(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setScale(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._SmoothMover__overloaded_setScale_ptrSmoothMover_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._SmoothMover__overloaded_setScale_ptrSmoothMover_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


