# File: D (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import DNAGroup

class DNAData(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DNAData__overloaded_constructor_ptrConstDNAData(self, copy):
        self.this = libtoontown._inPdt4yeOgM(copy.this)
        self.userManagesMemory = 1

    
    def _DNAData__overloaded_constructor_atomicstring(self, initialName):
        self.this = libtoontown._inPdt4ynx_q(initialName)
        self.userManagesMemory = 1

    
    def _DNAData__overloaded_constructor(self):
        self.this = libtoontown._inPdt4ydMjm()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPdt4yycrx:
            libtoontown._inPdt4yycrx(self.this)
        

    
    def _DNAData__overloaded_resolveDnaFilename_ptrFilename_ptrConstDSearchPath(dnaFilename, searchpath):
        returnValue = libtoontown._inPdt4yZPNG(dnaFilename.this, searchpath.this)
        return returnValue

    _DNAData__overloaded_resolveDnaFilename_ptrFilename_ptrConstDSearchPath = staticmethod(_DNAData__overloaded_resolveDnaFilename_ptrFilename_ptrConstDSearchPath)
    
    def _DNAData__overloaded_resolveDnaFilename_ptrFilename(dnaFilename):
        returnValue = libtoontown._inPdt4yHR01(dnaFilename.this)
        return returnValue

    _DNAData__overloaded_resolveDnaFilename_ptrFilename = staticmethod(_DNAData__overloaded_resolveDnaFilename_ptrFilename)
    
    def getClassType():
        returnValue = libtoontown._inPdt4yklrg()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libtoontown._inPdt4y9Iao(self.this, copy.this)
        returnObject = DNAData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _DNAData__overloaded_read_ptrDNAData_ptrFilename_ptrOstream(self, filename, error):
        returnValue = libtoontown._inPdt4yYqn0(self.this, filename.this, error.this)
        return returnValue

    
    def _DNAData__overloaded_read_ptrDNAData_ptrFilename(self, filename):
        returnValue = libtoontown._inPdt4yLS50(self.this, filename.this)
        return returnValue

    
    def _DNAData__overloaded_read_ptrDNAData_ptrIstream_ptrOstream(self, _in, error):
        returnValue = libtoontown._inPdt4yWygI(self.this, _in.this, error.this)
        return returnValue

    
    def _DNAData__overloaded_read_ptrDNAData_ptrIstream(self, _in):
        returnValue = libtoontown._inPdt4yWofQ(self.this, _in.this)
        return returnValue

    
    def _DNAData__overloaded_resolveExternals_ptrDNAData_atomicstring_ptrOstream(self, searchpath, error):
        returnValue = libtoontown._inPdt4yebLE(self.this, searchpath, error.this)
        return returnValue

    
    def _DNAData__overloaded_resolveExternals_ptrDNAData_atomicstring(self, searchpath):
        returnValue = libtoontown._inPdt4yXVKM(self.this, searchpath)
        return returnValue

    
    def _DNAData__overloaded_writeDna_ptrDNAData_ptrFilename_ptrOstream_ptrDNAStorage(self, filename, error, store):
        returnValue = libtoontown._inPdt4yrDGG(self.this, filename.this, error.this, store.this)
        return returnValue

    
    def _DNAData__overloaded_writeDna_ptrDNAData_ptrOstream_ptrOstream_ptrDNAStorage(self, out, error, store):
        returnValue = libtoontown._inPdt4yMyKP(self.this, out.this, error.this, store.this)
        return returnValue

    
    def setCoordinateSystem(self, coordsys):
        returnValue = libtoontown._inPdt4yrJA5(self.this, coordsys)
        return returnValue

    
    def getCoordinateSystem(self):
        returnValue = libtoontown._inPdt4y2_2I(self.this)
        return returnValue

    
    def setDnaFilename(self, directory):
        returnValue = libtoontown._inPdt4y1wSB(self.this, directory.this)
        return returnValue

    
    def getDnaFilename(self):
        returnValue = libtoontown._inPdt4yjqWP(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setDnaStorage(self, store):
        returnValue = libtoontown._inPdt4yfmc5(self.this, store.this)
        return returnValue

    
    def getDnaStorage(self):
        returnValue = libtoontown._inPdt4yrnzg(self.this)
        import DNAStorage
        returnObject = DNAStorage.DNAStorage(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def resolveDnaFilename(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return DNAData._DNAData__overloaded_resolveDnaFilename_ptrFilename(*_args)
        elif numArgs == 2:
            return DNAData._DNAData__overloaded_resolveDnaFilename_ptrFilename_ptrConstDSearchPath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    resolveDnaFilename = staticmethod(resolveDnaFilename)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DNAData__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DNAData__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], DNAData):
                return self._DNAData__overloaded_constructor_ptrConstDNAData(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAData> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def resolveExternals(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DNAData__overloaded_resolveExternals_ptrDNAData_atomicstring(*_args)
        elif numArgs == 2:
            return self._DNAData__overloaded_resolveExternals_ptrDNAData_atomicstring_ptrOstream(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def read(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Istream
            if isinstance(_args[0], Istream.Istream):
                return self._DNAData__overloaded_read_ptrDNAData_ptrIstream(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._DNAData__overloaded_read_ptrDNAData_ptrFilename(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
        elif numArgs == 2:
            import Istream
            if isinstance(_args[0], Istream.Istream):
                return self._DNAData__overloaded_read_ptrDNAData_ptrIstream_ptrOstream(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._DNAData__overloaded_read_ptrDNAData_ptrFilename_ptrOstream(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def writeDna(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._DNAData__overloaded_writeDna_ptrDNAData_ptrOstream_ptrOstream_ptrDNAStorage(*_args)
            
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._DNAData__overloaded_writeDna_ptrDNAData_ptrFilename_ptrOstream_ptrDNAStorage(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 '


