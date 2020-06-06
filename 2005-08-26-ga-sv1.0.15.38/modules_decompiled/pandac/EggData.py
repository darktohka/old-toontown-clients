# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggGroupNode

class EggData(EggGroupNode.EggGroupNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggData__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOM_Tjy()
        self.userManagesMemory = 1

    
    def _EggData__overloaded_constructor_ptrConstEggData(self, copy):
        self.this = libpandaegg._inPkAOMYDEk(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMK4Q8:
            libpandaegg._inPkAOMK4Q8(self.this)
        

    
    def _EggData__overloaded_resolveEggFilename_ptrFilename_ptrConstDSearchPath(eggFilename, searchpath):
        returnValue = libpandaegg._inPkAOMqWzm(eggFilename.this, searchpath.this)
        return returnValue

    _EggData__overloaded_resolveEggFilename_ptrFilename_ptrConstDSearchPath = staticmethod(_EggData__overloaded_resolveEggFilename_ptrFilename_ptrConstDSearchPath)
    
    def _EggData__overloaded_resolveEggFilename_ptrFilename(eggFilename):
        returnValue = libpandaegg._inPkAOM_5ZW(eggFilename.this)
        return returnValue

    _EggData__overloaded_resolveEggFilename_ptrFilename = staticmethod(_EggData__overloaded_resolveEggFilename_ptrFilename)
    
    def getClassType():
        returnValue = libpandaegg._inPkAOMDr_V()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMdsvy(self.this, copy.this)
        returnObject = EggData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _EggData__overloaded_read_ptrEggData_ptrFilename_atomicstring(self, filename, displayName):
        returnValue = libpandaegg._inPkAOMR9jy(self.this, filename.this, displayName)
        return returnValue

    
    def _EggData__overloaded_read_ptrEggData_ptrFilename(self, filename):
        returnValue = libpandaegg._inPkAOM8ZNq(self.this, filename.this)
        return returnValue

    
    def _EggData__overloaded_read_ptrEggData_ptrIstream(self, _in):
        returnValue = libpandaegg._inPkAOMluzF(self.this, _in.this)
        return returnValue

    
    def merge(self, other):
        returnValue = libpandaegg._inPkAOMvw2D(self.this, other.this)
        return returnValue

    
    def _EggData__overloaded_loadExternals_ptrEggData_ptrConstDSearchPath(self, searchpath):
        returnValue = libpandaegg._inPkAOMEkdE(self.this, searchpath.this)
        return returnValue

    
    def _EggData__overloaded_loadExternals_ptrEggData(self):
        returnValue = libpandaegg._inPkAOMlY7S(self.this)
        return returnValue

    
    def collapseEquivalentTextures(self):
        returnValue = libpandaegg._inPkAOMfumv(self.this)
        return returnValue

    
    def collapseEquivalentMaterials(self):
        returnValue = libpandaegg._inPkAOMGkhb(self.this)
        return returnValue

    
    def _EggData__overloaded_writeEgg_ptrEggData_ptrFilename(self, filename):
        returnValue = libpandaegg._inPkAOMUZKh(self.this, filename.this)
        return returnValue

    
    def _EggData__overloaded_writeEgg_ptrEggData_ptrOstream(self, out):
        returnValue = libpandaegg._inPkAOMOkbY(self.this, out.this)
        return returnValue

    
    def setAutoResolveExternals(self, resolve):
        returnValue = libpandaegg._inPkAOMkJsK(self.this, resolve)
        return returnValue

    
    def getAutoResolveExternals(self):
        returnValue = libpandaegg._inPkAOMVTWc(self.this)
        return returnValue

    
    def originalHadAbsolutePathnames(self):
        returnValue = libpandaegg._inPkAOMLqtE(self.this)
        return returnValue

    
    def setCoordinateSystem(self, coordsys):
        returnValue = libpandaegg._inPkAOMwPUu(self.this, coordsys)
        return returnValue

    
    def getCoordinateSystem(self):
        returnValue = libpandaegg._inPkAOMW4K_(self.this)
        return returnValue

    
    def setEggFilename(self, eggFilenamea):
        returnValue = libpandaegg._inPkAOMgZ_q(self.this, eggFilenamea.this)
        return returnValue

    
    def getEggFilename(self):
        returnValue = libpandaegg._inPkAOMOvC5(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def recomputeVertexNormals(self, threshold):
        returnValue = libpandaegg._inPkAOMHKMn(self.this, threshold)
        return returnValue

    
    def recomputePolygonNormals(self):
        returnValue = libpandaegg._inPkAOMI60Q(self.this)
        return returnValue

    
    def stripNormals(self):
        returnValue = libpandaegg._inPkAOMMttE(self.this)
        return returnValue

    
    def resolveEggFilename(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return EggData._EggData__overloaded_resolveEggFilename_ptrFilename(*_args)
        elif numArgs == 2:
            return EggData._EggData__overloaded_resolveEggFilename_ptrFilename_ptrConstDSearchPath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    resolveEggFilename = staticmethod(resolveEggFilename)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggData__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._EggData__overloaded_constructor_ptrConstEggData(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def read(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Istream
            if isinstance(_args[0], Istream.Istream):
                return self._EggData__overloaded_read_ptrEggData_ptrIstream(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._EggData__overloaded_read_ptrEggData_ptrFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
        elif numArgs == 2:
            return self._EggData__overloaded_read_ptrEggData_ptrFilename_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writeEgg(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._EggData__overloaded_writeEgg_ptrEggData_ptrOstream(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._EggData__overloaded_writeEgg_ptrEggData_ptrFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def loadExternals(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggData__overloaded_loadExternals_ptrEggData(*_args)
        elif numArgs == 1:
            return self._EggData__overloaded_loadExternals_ptrEggData_ptrConstDSearchPath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


