# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PandaNode

class ParametricCurve(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPHc9WxWO8()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isValid(self):
        returnValue = libpanda._inPHc9WhDM7(self.this)
        return returnValue

    
    def getMaxT(self):
        returnValue = libpanda._inPHc9Wan3O(self.this)
        return returnValue

    
    def setCurveType(self, type):
        returnValue = libpanda._inPHc9Wumed(self.this, type)
        return returnValue

    
    def getCurveType(self):
        returnValue = libpanda._inPHc9WuPVX(self.this)
        return returnValue

    
    def setNumDimensions(self, num):
        returnValue = libpanda._inPHc9WKuzT(self.this, num)
        return returnValue

    
    def getNumDimensions(self):
        returnValue = libpanda._inPHc9WiD71(self.this)
        return returnValue

    
    def _ParametricCurve__overloaded_calcLength_ptrConstParametricCurve(self):
        returnValue = libpanda._inPHc9WbQeF(self.this)
        return returnValue

    
    def _ParametricCurve__overloaded_calcLength_ptrConstParametricCurve_float_float(self, _from, to):
        returnValue = libpanda._inPHc9WBINZ(self.this, _from, to)
        return returnValue

    
    def findLength(self, startT, lengthOffset):
        returnValue = libpanda._inPHc9WFyLm(self.this, startT, lengthOffset)
        return returnValue

    
    def getPoint(self, t, point):
        returnValue = libpanda._inPHc9Wo5OE(self.this, t, point.this)
        return returnValue

    
    def getTangent(self, t, tangent):
        returnValue = libpanda._inPHc9WHDs0(self.this, t, tangent.this)
        return returnValue

    
    def getPt(self, t, point, tangent):
        returnValue = libpanda._inPHc9WIOPy(self.this, t, point.this, tangent.this)
        return returnValue

    
    def get2ndtangent(self, t, tangent2):
        returnValue = libpanda._inPHc9WP1ia(self.this, t, tangent2.this)
        return returnValue

    
    def adjustPoint(self, t, px, py, pz):
        returnValue = libpanda._inPHc9W7vVs(self.this, t, px, py, pz)
        return returnValue

    
    def adjustTangent(self, t, tx, ty, tz):
        returnValue = libpanda._inPHc9WjLxE(self.this, t, tx, ty, tz)
        return returnValue

    
    def adjustPt(self, t, px, py, pz, tx, ty, tz):
        returnValue = libpanda._inPHc9WxacM(self.this, t, px, py, pz, tx, ty, tz)
        return returnValue

    
    def recompute(self):
        returnValue = libpanda._inPHc9WkG_o(self.this)
        return returnValue

    
    def stitch(self, a, b):
        returnValue = libpanda._inPHc9WKq7P(self.this, a.this, b.this)
        return returnValue

    
    def _ParametricCurve__overloaded_writeEgg_ptrParametricCurve_ptrFilename___enum__CoordinateSystem(self, filename, cs):
        returnValue = libpanda._inPHc9W_qGa(self.this, filename.this, cs)
        return returnValue

    
    def _ParametricCurve__overloaded_writeEgg_ptrParametricCurve_ptrFilename(self, filename):
        returnValue = libpanda._inPHc9Wx_vA(self.this, filename.this)
        return returnValue

    
    def _ParametricCurve__overloaded_writeEgg_ptrParametricCurve_ptrOstream_ptrConstFilename___enum__CoordinateSystem(self, out, filename, cs):
        returnValue = libpanda._inPHc9WuHju(self.this, out.this, filename.this, cs)
        return returnValue

    
    def writeEgg(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._ParametricCurve__overloaded_writeEgg_ptrParametricCurve_ptrFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._ParametricCurve__overloaded_writeEgg_ptrParametricCurve_ptrFilename___enum__CoordinateSystem(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 3:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                import Filename
                if isinstance(_args[1], Filename.Filename):
                    if isinstance(_args[2], types.IntType):
                        return self._ParametricCurve__overloaded_writeEgg_ptrParametricCurve_ptrOstream_ptrConstFilename___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def calcLength(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ParametricCurve__overloaded_calcLength_ptrConstParametricCurve()
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._ParametricCurve__overloaded_calcLength_ptrConstParametricCurve_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '


