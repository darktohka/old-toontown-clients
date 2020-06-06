# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount

class DNASuitPoint(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    FRONTDOORPOINT = 1
    SIDEDOORPOINT = 2
    STREETPOINT = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DNASuitPoint__overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f_int(self, index, type, pos, lbIndex):
        self.this = libtoontown._inPet4yraal(index, type, pos.this, lbIndex)
        self.userManagesMemory = 1

    
    def _DNASuitPoint__overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f(self, index, type, pos):
        self.this = libtoontown._inPet4yaogd(index, type, pos.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPet4yqwXD:
            libtoontown._inPet4yqwXD(self.this)
        

    
    def getClassType():
        returnValue = libtoontown._inPet4y88If()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setIndex(self, index):
        returnValue = libtoontown._inPet4y1KrK(self.this, index)
        return returnValue

    
    def getIndex(self):
        returnValue = libtoontown._inPet4yTHKF(self.this)
        return returnValue

    
    def setPointType(self, type):
        returnValue = libtoontown._inPet4yPzDT(self.this, type)
        return returnValue

    
    def getPointType(self):
        returnValue = libtoontown._inPet4yCXF8(self.this)
        return returnValue

    
    def setPos(self, pos):
        returnValue = libtoontown._inPet4yxt9s(self.this, pos.this)
        return returnValue

    
    def getPos(self):
        returnValue = libtoontown._inPet4yoSRO(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setLandmarkBuildingIndex(self, lbIndex):
        returnValue = libtoontown._inPet4yjoF_(self.this, lbIndex)
        return returnValue

    
    def getLandmarkBuildingIndex(self):
        returnValue = libtoontown._inPet4ySC6v(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libtoontown._inPet4yRrxR(self.this, out.this)
        return returnValue

    
    def _DNASuitPoint__overloaded_write_ptrConstDNASuitPoint_ptrOstream_int(self, out, indentLevel):
        returnValue = libtoontown._inPet4yv_3h(self.this, out.this, indentLevel)
        return returnValue

    
    def _DNASuitPoint__overloaded_write_ptrConstDNASuitPoint_ptrOstream(self, out):
        returnValue = libtoontown._inPet4ymXK6(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    import Point3
                    if isinstance(_args[2], Point3.Point3):
                        return self._DNASuitPoint__overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    import Point3
                    if isinstance(_args[2], Point3.Point3):
                        if isinstance(_args[3], types.IntType):
                            return self._DNASuitPoint__overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f_int(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._DNASuitPoint__overloaded_write_ptrConstDNASuitPoint_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._DNASuitPoint__overloaded_write_ptrConstDNASuitPoint_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


