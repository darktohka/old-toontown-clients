# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DDrawable

class Geom(DDrawable.DDrawable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
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
    
    def transformVertices(self, mat):
        returnValue = libpanda._inPMAKPYlMV(self.this, mat.this)
        return returnValue

    
    def _Geom__overloaded_setCoords_ptrGeom_ptrConstPTAVertexf___enum__GeomBindType_ptrConstPTAUshort(self, coords, bind, vindex):
        returnValue = libpanda._inPMAKPRSBw(self.this, coords.this, bind, vindex.this)
        return returnValue

    
    def _Geom__overloaded_setCoords_ptrGeom_ptrConstPTAVertexf___enum__GeomBindType(self, coords, bind):
        returnValue = libpanda._inPMAKPdJzT(self.this, coords.this, bind)
        return returnValue

    
    def _Geom__overloaded_setCoords_ptrGeom_ptrConstPTAVertexf_ptrConstPTAUshort(self, coords, vindex):
        returnValue = libpanda._inPMAKPjn48(self.this, coords.this, vindex.this)
        return returnValue

    
    def _Geom__overloaded_setCoords_ptrGeom_ptrConstPTAVertexf(self, coords):
        returnValue = libpanda._inPMAKPV_mL(self.this, coords.this)
        return returnValue

    
    def _Geom__overloaded_setNormals_ptrGeom_ptrConstPTANormalf___enum__GeomBindType_ptrConstPTAUshort(self, norms, bind, nindex):
        returnValue = libpanda._inPMAKPj7xY(self.this, norms.this, bind, nindex.this)
        return returnValue

    
    def _Geom__overloaded_setNormals_ptrGeom_ptrConstPTANormalf___enum__GeomBindType(self, norms, bind):
        returnValue = libpanda._inPMAKP_x75(self.this, norms.this, bind)
        return returnValue

    
    def _Geom__overloaded_setColors_ptrGeom_ptrConstPTAColorf___enum__GeomBindType_ptrConstPTAUshort(self, colors, bind, cindex):
        returnValue = libpanda._inPMAKPJ_X7(self.this, colors.this, bind, cindex.this)
        return returnValue

    
    def _Geom__overloaded_setColors_ptrGeom_ptrConstPTAColorf___enum__GeomBindType(self, colors, bind):
        returnValue = libpanda._inPMAKPA4hc(self.this, colors.this, bind)
        return returnValue

    
    def _Geom__overloaded_setTexcoords_ptrGeom_ptrConstPTATexCoordf___enum__GeomBindType_ptrConstPTAUshort(self, texcoords, bind, tindex):
        returnValue = libpanda._inPMAKPPjh2(self.this, texcoords.this, bind, tindex.this)
        return returnValue

    
    def _Geom__overloaded_setTexcoords_ptrGeom_ptrConstPTATexCoordf___enum__GeomBindType(self, texcoords, bind):
        returnValue = libpanda._inPMAKPSo9X(self.this, texcoords.this, bind)
        return returnValue

    
    def _Geom__overloaded_setTexcoords_ptrGeom_ptrConstTexCoordName_ptrConstPTATexCoordf_ptrConstPTAUshort(self, name, texcoords, tindex):
        returnValue = libpanda._inPMAKP__Rx(self.this, name.this, texcoords.this, tindex.this)
        return returnValue

    
    def _Geom__overloaded_setTexcoords_ptrGeom_ptrConstTexCoordName_ptrConstPTATexCoordf(self, name, texcoords):
        returnValue = libpanda._inPMAKPFifF(self.this, name.this, texcoords.this)
        return returnValue

    
    def removeTexcoords(self, name):
        returnValue = libpanda._inPMAKPHjWs(self.this, name.this)
        return returnValue

    
    def getBinding(self, attr):
        returnValue = libpanda._inPMAKP3hes(self.this, attr)
        return returnValue

    
    def hasAnyTexcoords(self):
        returnValue = libpanda._inPMAKPXXMA(self.this)
        return returnValue

    
    def hasTexcoords(self, name):
        returnValue = libpanda._inPMAKPdu6M(self.this, name.this)
        return returnValue

    
    def getCoordsArray(self):
        returnValue = libpanda._inPMAKPqFPn(self.this)
        import PTAVertexf
        returnObject = PTAVertexf.PTAVertexf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNormalsArray(self):
        returnValue = libpanda._inPMAKPtmqp(self.this)
        import PTANormalf
        returnObject = PTANormalf.PTANormalf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getColorsArray(self):
        returnValue = libpanda._inPMAKP7QeS(self.this)
        import PTAColorf
        returnObject = PTAColorf.PTAColorf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Geom__overloaded_getTexcoordsArray_ptrConstGeom(self):
        returnValue = libpanda._inPMAKPoSNd(self.this)
        import PTATexCoordf
        returnObject = PTATexCoordf.PTATexCoordf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Geom__overloaded_getTexcoordsArray_ptrConstGeom_ptrConstTexCoordName(self, name):
        returnValue = libpanda._inPMAKPW99i(self.this, name.this)
        import PTATexCoordf
        returnObject = PTATexCoordf.PTATexCoordf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCoordsIndex(self):
        returnValue = libpanda._inPMAKPKyUk(self.this)
        import PTAUshort
        returnObject = PTAUshort.PTAUshort(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNormalsIndex(self):
        returnValue = libpanda._inPMAKPuN_L(self.this)
        import PTAUshort
        returnObject = PTAUshort.PTAUshort(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getColorsIndex(self):
        returnValue = libpanda._inPMAKPtOjP(self.this)
        import PTAUshort
        returnObject = PTAUshort.PTAUshort(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Geom__overloaded_getTexcoordsIndex_ptrConstGeom(self):
        returnValue = libpanda._inPMAKPs9ba(self.this)
        import PTAUshort
        returnObject = PTAUshort.PTAUshort(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Geom__overloaded_getTexcoordsIndex_ptrConstGeom_ptrConstTexCoordName(self, name):
        returnValue = libpanda._inPMAKPpUNg(self.this, name.this)
        import PTAUshort
        returnObject = PTAUshort.PTAUshort(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def areTexcoordsIndexed(self):
        returnValue = libpanda._inPMAKPDLyi(self.this)
        return returnValue

    
    def prepare(self, preparedObjects):
        returnValue = libpanda._inPMAKPkUN5(self.this, preparedObjects.this)
        return returnValue

    
    def setNumPrims(self, num):
        returnValue = libpanda._inPMAKPkJO7(self.this, num)
        return returnValue

    
    def getNumPrims(self):
        returnValue = libpanda._inPMAKPlZiV(self.this)
        return returnValue

    
    def setLengths(self, lengths):
        returnValue = libpanda._inPMAKPeIM9(self.this, lengths.this)
        return returnValue

    
    def getLengths(self):
        returnValue = libpanda._inPMAKP4HKB(self.this)
        import PTAInt
        returnObject = PTAInt.PTAInt(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumVerticesPerPrim(self):
        returnValue = libpanda._inPMAKPeEbs(self.this)
        return returnValue

    
    def getNumMoreVerticesThanComponents(self):
        returnValue = libpanda._inPMAKPsp6Q(self.this)
        return returnValue

    
    def usesComponents(self):
        returnValue = libpanda._inPMAKP6oeZ(self.this)
        return returnValue

    
    def getNumVertices(self):
        returnValue = libpanda._inPMAKP6GWS(self.this)
        return returnValue

    
    def getLength(self, prim):
        returnValue = libpanda._inPMAKPqIdG(self.this, prim)
        return returnValue

    
    def explode(self):
        returnValue = libpanda._inPMAKPO8AD(self.this)
        returnObject = Geom(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getTris(self):
        returnValue = libpanda._inPMAKPjDw6(self.this)
        import PTAUshort
        returnObject = PTAUshort.PTAUshort(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Geom__overloaded_write_ptrConstGeom_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPMAKPC21S(self.this, out.this, indentLevel)
        return returnValue

    
    def _Geom__overloaded_write_ptrConstGeom_ptrOstream(self, out):
        returnValue = libpanda._inPMAKP0uiX(self.this, out.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPMAKPrXR3(self.this, out.this)
        return returnValue

    
    def writeVerbose(self, out, indentLevel):
        returnValue = libpanda._inPMAKPfq3D(self.this, out.this, indentLevel)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Geom__overloaded_write_ptrConstGeom_ptrOstream(*_args)
        elif numArgs == 2:
            return self._Geom__overloaded_write_ptrConstGeom_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getTexcoordsArray(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Geom__overloaded_getTexcoordsArray_ptrConstGeom(*_args)
        elif numArgs == 1:
            return self._Geom__overloaded_getTexcoordsArray_ptrConstGeom_ptrConstTexCoordName(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getTexcoordsIndex(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Geom__overloaded_getTexcoordsIndex_ptrConstGeom(*_args)
        elif numArgs == 1:
            return self._Geom__overloaded_getTexcoordsIndex_ptrConstGeom_ptrConstTexCoordName(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setNormals(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._Geom__overloaded_setNormals_ptrGeom_ptrConstPTANormalf___enum__GeomBindType(*_args)
        elif numArgs == 3:
            return self._Geom__overloaded_setNormals_ptrGeom_ptrConstPTANormalf___enum__GeomBindType_ptrConstPTAUshort(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setCoords(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Geom__overloaded_setCoords_ptrGeom_ptrConstPTAVertexf(*_args)
        elif numArgs == 2:
            import PTAVertexf
            if isinstance(_args[0], PTAVertexf.PTAVertexf):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return self._Geom__overloaded_setCoords_ptrGeom_ptrConstPTAVertexf___enum__GeomBindType(*_args)
                
                import PTAUshort
                if isinstance(_args[1], PTAUshort.PTAUshort):
                    return self._Geom__overloaded_setCoords_ptrGeom_ptrConstPTAVertexf_ptrConstPTAUshort(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <PTAUshort.PTAUshort> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <PTAVertexf.PTAVertexf> '
        elif numArgs == 3:
            return self._Geom__overloaded_setCoords_ptrGeom_ptrConstPTAVertexf___enum__GeomBindType_ptrConstPTAUshort(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    
    def setTexcoords(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import TexCoordName
            if isinstance(_args[0], TexCoordName.TexCoordName):
                return self._Geom__overloaded_setTexcoords_ptrGeom_ptrConstTexCoordName_ptrConstPTATexCoordf(*_args)
            
            import PTATexCoordf
            if isinstance(_args[0], PTATexCoordf.PTATexCoordf):
                return self._Geom__overloaded_setTexcoords_ptrGeom_ptrConstPTATexCoordf___enum__GeomBindType(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <TexCoordName.TexCoordName> <PTATexCoordf.PTATexCoordf> '
        elif numArgs == 3:
            import TexCoordName
            if isinstance(_args[0], TexCoordName.TexCoordName):
                return self._Geom__overloaded_setTexcoords_ptrGeom_ptrConstTexCoordName_ptrConstPTATexCoordf_ptrConstPTAUshort(*_args)
            
            import PTATexCoordf
            if isinstance(_args[0], PTATexCoordf.PTATexCoordf):
                return self._Geom__overloaded_setTexcoords_ptrGeom_ptrConstPTATexCoordf___enum__GeomBindType_ptrConstPTAUshort(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <TexCoordName.TexCoordName> <PTATexCoordf.PTATexCoordf> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setColors(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._Geom__overloaded_setColors_ptrGeom_ptrConstPTAColorf___enum__GeomBindType(*_args)
        elif numArgs == 3:
            return self._Geom__overloaded_setColors_ptrGeom_ptrConstPTAColorf___enum__GeomBindType_ptrConstPTAUshort(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


