# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VirtualFile

class HTTPDocument(VirtualFile.VirtualFile, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
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
        returnValue = libpandaexpress._inP2KOdsDMU()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isValid(self):
        returnValue = libpandaexpress._inP2KOdw_SK(self.this)
        return returnValue

    
    def getUrl(self):
        returnValue = libpandaexpress._inP2KOd08OE(self.this)
        import URLSpec
        returnObject = URLSpec.URLSpec(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getHttpVersion(self):
        returnValue = libpandaexpress._inP2KOdbDGN(self.this)
        return returnValue

    
    def getHttpVersionString(self):
        returnValue = libpandaexpress._inP2KOda7tc(self.this)
        return returnValue

    
    def getStatusCode(self):
        returnValue = libpandaexpress._inP2KOdVfzf(self.this)
        return returnValue

    
    def getStatusString(self):
        returnValue = libpandaexpress._inP2KOdloW0(self.this)
        return returnValue

    
    def getRealm(self):
        returnValue = libpandaexpress._inP2KOdWcvv(self.this)
        return returnValue

    
    def getRedirect(self):
        returnValue = libpandaexpress._inP2KOd4YWd(self.this)
        import URLSpec
        returnObject = URLSpec.URLSpec(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getHeaderValue(self, key):
        returnValue = libpandaexpress._inP2KOdtJ3F(self.this, key)
        return returnValue

    
    def setPersistentConnection(self, persistentConnection):
        returnValue = libpandaexpress._inP2KOdgY6Y(self.this, persistentConnection)
        return returnValue

    
    def getPersistentConnection(self):
        returnValue = libpandaexpress._inP2KOdsd8j(self.this)
        return returnValue

    
    def getFileSize(self):
        returnValue = libpandaexpress._inP2KOdyvfs(self.this)
        return returnValue

    
    def writeHeaders(self, out):
        returnValue = libpandaexpress._inP2KOdpXVq(self.this, out.this)
        return returnValue

    
    def _HTTPDocument__overloaded_getDocument_ptrHTTPDocument_ptrConstURLSpec_atomicstring(self, url, body):
        returnValue = libpandaexpress._inP2KOd6ohl(self.this, url.this, body)
        return returnValue

    
    def _HTTPDocument__overloaded_getDocument_ptrHTTPDocument_ptrConstURLSpec(self, url):
        returnValue = libpandaexpress._inP2KOd4mhS(self.this, url.this)
        return returnValue

    
    def getHeader(self, url):
        returnValue = libpandaexpress._inP2KOdGmoF(self.this, url.this)
        return returnValue

    
    def getDocument(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import URLSpec
            if isinstance(_args[0], URLSpec.URLSpec):
                return self._HTTPDocument__overloaded_getDocument_ptrHTTPDocument_ptrConstURLSpec(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <URLSpec.URLSpec> '
        elif numArgs == 2:
            import URLSpec
            if isinstance(_args[0], URLSpec.URLSpec):
                if isinstance(_args[1], types.StringType):
                    return self._HTTPDocument__overloaded_getDocument_ptrHTTPDocument_ptrConstURLSpec_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <URLSpec.URLSpec> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


