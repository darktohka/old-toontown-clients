# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class NodePathCollection(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _NodePathCollection__overloaded_constructor(self):
        self.this = libpanda._inPnJyo3iXv()
        self.userManagesMemory = 1

    
    def _NodePathCollection__overloaded_constructor_ptrConstNodePathCollection(self, copy):
        self.this = libpanda._inPnJyo2o9H(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoiPHD:
            libpanda._inPnJyoiPHD(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPnJyohGif(self.this, copy.this)
        returnObject = NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def addPath(self, nodePath):
        returnValue = libpanda._inPnJyooj7i(self.this, nodePath.this)
        return returnValue

    
    def removePath(self, nodePath):
        returnValue = libpanda._inPnJyo_4Zw(self.this, nodePath.this)
        return returnValue

    
    def addPathsFrom(self, other):
        returnValue = libpanda._inPnJyoD16c(self.this, other.this)
        return returnValue

    
    def removePathsFrom(self, other):
        returnValue = libpanda._inPnJyoPgsC(self.this, other.this)
        return returnValue

    
    def removeDuplicatePaths(self):
        returnValue = libpanda._inPnJyofBHO(self.this)
        return returnValue

    
    def hasPath(self, path):
        returnValue = libpanda._inPnJyoW5qJ(self.this, path.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPnJyoOyfl(self.this)
        return returnValue

    
    def isEmpty(self):
        returnValue = libpanda._inPnJyoYTzI(self.this)
        return returnValue

    
    def getNumPaths(self):
        returnValue = libpanda._inPnJyo6KKi(self.this)
        return returnValue

    
    def getPath(self, index):
        returnValue = libpanda._inPnJyo02PJ(self.this, index)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __getitem__(self, index):
        returnValue = libpanda._inPnJyoyiIl(self.this, index)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePathCollection__overloaded_ls_ptrConstNodePathCollection(self):
        returnValue = libpanda._inPnJyo3QA8(self.this)
        return returnValue

    
    def _NodePathCollection__overloaded_ls_ptrConstNodePathCollection_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPnJyoRtqi(self.this, out.this, indentLevel)
        return returnValue

    
    def _NodePathCollection__overloaded_ls_ptrConstNodePathCollection_ptrOstream(self, out):
        returnValue = libpanda._inPnJyo1d_6(self.this, out.this)
        return returnValue

    
    def findAllMatches(self, path):
        returnValue = libpanda._inPnJyoXeNM(self.this, path)
        returnObject = NodePathCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def reparentTo(self, other):
        returnValue = libpanda._inPnJyob1jO(self.this, other.this)
        return returnValue

    
    def wrtReparentTo(self, other):
        returnValue = libpanda._inPnJyoqRqE(self.this, other.this)
        return returnValue

    
    def show(self):
        returnValue = libpanda._inPnJyo7UQK(self.this)
        return returnValue

    
    def hide(self):
        returnValue = libpanda._inPnJyo583n(self.this)
        return returnValue

    
    def stash(self):
        returnValue = libpanda._inPnJyoiPiS(self.this)
        return returnValue

    
    def unstash(self):
        returnValue = libpanda._inPnJyoLTV5(self.this)
        return returnValue

    
    def detach(self):
        returnValue = libpanda._inPnJyoMNIX(self.this)
        return returnValue

    
    def getCollideMask(self):
        returnValue = libpanda._inPnJyoNmTQ(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _NodePathCollection__overloaded_setCollideMask_ptrNodePathCollection_ptrBitMask32_ptrBitMask32_ptrTypeHandle(self, newMask, bitsToChange, nodeType):
        returnValue = libpanda._inPnJyoZCJf(self.this, newMask.this, bitsToChange.this, nodeType.this)
        return returnValue

    
    def _NodePathCollection__overloaded_setCollideMask_ptrNodePathCollection_ptrBitMask32_ptrBitMask32(self, newMask, bitsToChange):
        returnValue = libpanda._inPnJyoFNs1(self.this, newMask.this, bitsToChange.this)
        return returnValue

    
    def _NodePathCollection__overloaded_setCollideMask_ptrNodePathCollection_ptrBitMask32(self, newMask):
        returnValue = libpanda._inPnJyoM6Up(self.this, newMask.this)
        return returnValue

    
    def _NodePathCollection__overloaded_setColor_ptrNodePathCollection_ptrConstLVecBase4f_int(self, color, priority):
        returnValue = libpanda._inPnJyoKnbq(self.this, color.this, priority)
        return returnValue

    
    def _NodePathCollection__overloaded_setColor_ptrNodePathCollection_ptrConstLVecBase4f(self, color):
        returnValue = libpanda._inPnJyopnAB(self.this, color.this)
        return returnValue

    
    def _NodePathCollection__overloaded_setColor_ptrNodePathCollection_float_float_float_float_int(self, r, g, b, a, priority):
        returnValue = libpanda._inPnJyoOAR_(self.this, r, g, b, a, priority)
        return returnValue

    
    def _NodePathCollection__overloaded_setColor_ptrNodePathCollection_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPnJyoM8OR(self.this, r, g, b, a)
        return returnValue

    
    def _NodePathCollection__overloaded_setColor_ptrNodePathCollection_float_float_float(self, r, g, b):
        returnValue = libpanda._inPnJyofNdA(self.this, r, g, b)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPnJyouSFB(self.this, out.this)
        return returnValue

    
    def _NodePathCollection__overloaded_write_ptrConstNodePathCollection_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPnJyocn9H(self.this, out.this, indentLevel)
        return returnValue

    
    def _NodePathCollection__overloaded_write_ptrConstNodePathCollection_ptrOstream(self, out):
        returnValue = libpanda._inPnJyo_nJZ(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePathCollection__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._NodePathCollection__overloaded_constructor_ptrConstNodePathCollection(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePathCollection__overloaded_write_ptrConstNodePathCollection_ptrOstream(*_args)
        elif numArgs == 2:
            return self._NodePathCollection__overloaded_write_ptrConstNodePathCollection_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCollideMask(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePathCollection__overloaded_setCollideMask_ptrNodePathCollection_ptrBitMask32(*_args)
        elif numArgs == 2:
            return self._NodePathCollection__overloaded_setCollideMask_ptrNodePathCollection_ptrBitMask32_ptrBitMask32(*_args)
        elif numArgs == 3:
            return self._NodePathCollection__overloaded_setCollideMask_ptrNodePathCollection_ptrBitMask32_ptrBitMask32_ptrTypeHandle(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def setColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NodePathCollection__overloaded_setColor_ptrNodePathCollection_ptrConstLVecBase4f(*_args)
        elif numArgs == 2:
            return self._NodePathCollection__overloaded_setColor_ptrNodePathCollection_ptrConstLVecBase4f_int(*_args)
        elif numArgs == 3:
            return self._NodePathCollection__overloaded_setColor_ptrNodePathCollection_float_float_float(*_args)
        elif numArgs == 4:
            return self._NodePathCollection__overloaded_setColor_ptrNodePathCollection_float_float_float_float(*_args)
        elif numArgs == 5:
            return self._NodePathCollection__overloaded_setColor_ptrNodePathCollection_float_float_float_float_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 5 '

    
    def ls(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NodePathCollection__overloaded_ls_ptrConstNodePathCollection(*_args)
        elif numArgs == 1:
            return self._NodePathCollection__overloaded_ls_ptrConstNodePathCollection_ptrOstream(*_args)
        elif numArgs == 2:
            return self._NodePathCollection__overloaded_ls_ptrConstNodePathCollection_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def asList(self):
        if self.isEmpty():
            return []
        else:
            npList = []
            for nodePathIndex in range(self.getNumPaths()):
                npList.append(self.getPath(nodePathIndex))
            
            return npList

    
    def getTightBounds(self):
        Point3 = Point3
        import pandac
        if self.getNumPaths() == 0:
            return (Point3.Point3(0), Point3.Point3(0))
        
        (v1, v2) = self.getPath(0).getTightBounds()
        for i in range(1, self.getNumPaths()):
            (v1x, v2x) = self.getPath(i).getTightBounds()
            v1 = Point3.Point3(min(v1[0], v1x[0]), min(v1[1], v1x[1]), min(v1[2], v1x[2]))
            v2 = Point3.Point3(max(v2[0], v2x[0]), max(v2[1], v2x[1]), max(v2[2], v2x[2]))
        
        return (v1, v2)


