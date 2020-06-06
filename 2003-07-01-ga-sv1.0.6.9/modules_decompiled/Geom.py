# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DDrawable

class Geom(DDrawable.DDrawable, FFIExternalObject.FFIExternalObject):
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
        

    
    def destructor(self):
        if libpanda and libpanda._inPMAKPFEZJ:
            libpanda._inPMAKPFEZJ(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPMAKPyQKN()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Geom__overloaded_write_ptrConstGeom_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPMAKPC21S(self.this, out.this, indentLevel)
        return returnValue

    
    def _Geom__overloaded_write_ptrConstGeom_ptrOstream(self, out):
        returnValue = libpanda._inPMAKP0uiX(self.this, out.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPMAKPoXR3(self.this, out.this)
        return returnValue

    
    def writeVerbose(self, out, indentLevel):
        returnValue = libpanda._inPMAKPfq3D(self.this, out.this, indentLevel)
        return returnValue

    
    def getBinding(self, attr):
        returnValue = libpanda._inPMAKP2hes(self.this, attr)
        return returnValue

    
    def getCoordsArray(self):
        returnValue = libpanda._inPMAKPrFPn(self.this)
        import PTAVertexf
        returnObject = PTAVertexf.PTAVertexf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNormalsArray(self):
        returnValue = libpanda._inPMAKPsmqp(self.this)
        import PTANormalf
        returnObject = PTANormalf.PTANormalf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getColorsArray(self):
        returnValue = libpanda._inPMAKP7QeS(self.this)
        import PTAColorf
        returnObject = PTAColorf.PTAColorf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getTexcoordsArray(self):
        returnValue = libpanda._inPMAKPoSNd(self.this)
        import PTATexCoordf
        returnObject = PTATexCoordf.PTATexCoordf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getCoordsIndex(self):
        returnValue = libpanda._inPMAKPJyUk(self.this)
        import PTAUshort
        returnObject = PTAUshort.PTAUshort(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNormalsIndex(self):
        returnValue = libpanda._inPMAKPuN_L(self.this)
        import PTAUshort
        returnObject = PTAUshort.PTAUshort(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getColorsIndex(self):
        returnValue = libpanda._inPMAKPtOjP(self.this)
        import PTAUshort
        returnObject = PTAUshort.PTAUshort(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getTexcoordsIndex(self):
        returnValue = libpanda._inPMAKPs9ba(self.this)
        import PTAUshort
        returnObject = PTAUshort.PTAUshort(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Geom__overloaded_write_ptrConstGeom_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._Geom__overloaded_write_ptrConstGeom_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


