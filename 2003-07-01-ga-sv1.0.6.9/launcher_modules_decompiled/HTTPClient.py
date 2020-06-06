# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class HTTPClient(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    VSNoDateCheck = 1
    VSNormal = 2
    VSNoVerify = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _HTTPClient__overloaded_constructor(self):
        self.this = libpandaexpress._inP2KOdhdYN()
        self.userManagesMemory = 1

    
    def _HTTPClient__overloaded_constructor_ptrConstHTTPClient(self, copy):
        self.this = libpandaexpress._inP2KOde2lz(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdNiJk:
            libpandaexpress._inP2KOdNiJk(self.this)
        

    
    def parseHttpVersionString(version):
        returnValue = libpandaexpress._inP2KOdG_NH(version)
        return returnValue

    parseHttpVersionString = staticmethod(parseHttpVersionString)
    
    def assign(self, copy):
        returnValue = libpandaexpress._inP2KOdLPp_(self.this, copy.this)
        returnObject = HTTPClient(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setProxy(self, proxy):
        returnValue = libpandaexpress._inP2KOdWEcd(self.this, proxy.this)
        return returnValue

    
    def getProxy(self):
        returnValue = libpandaexpress._inP2KOdJuD2(self.this)
        import URLSpec
        returnObject = URLSpec.URLSpec(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setProxySpec(self, proxySpec):
        returnValue = libpandaexpress._inP2KOd0gjL(self.this, proxySpec)
        return returnValue

    
    def getProxySpec(self):
        returnValue = libpandaexpress._inP2KOdddMt(self.this)
        return returnValue

    
    def setDirectHostSpec(self, directHostSpec):
        returnValue = libpandaexpress._inP2KOdDtsw(self.this, directHostSpec)
        return returnValue

    
    def getDirectHostSpec(self):
        returnValue = libpandaexpress._inP2KOd_OJB(self.this)
        return returnValue

    
    def clearProxy(self):
        returnValue = libpandaexpress._inP2KOd6XUO(self.this)
        return returnValue

    
    def addProxy(self, scheme, proxy):
        returnValue = libpandaexpress._inP2KOdgkTU(self.this, scheme, proxy.this)
        return returnValue

    
    def clearDirectHost(self):
        returnValue = libpandaexpress._inP2KOdMVZA(self.this)
        return returnValue

    
    def addDirectHost(self, hostname):
        returnValue = libpandaexpress._inP2KOdlCAB(self.this, hostname)
        return returnValue

    
    def _HTTPClient__overloaded_getProxiesForUrl_ptrConstHTTPClient_ptrConstURLSpec(self, url):
        returnValue = libpandaexpress._inP2KOdIHk7(self.this, url.this)
        return returnValue

    
    def _HTTPClient__overloaded_getProxiesForUrl_ptrConstHTTPClient_ptrConstURLSpec_ptrVectorURLSpec(self, url, proxies):
        returnValue = libpandaexpress._inP2KOdWtH7(self.this, url.this, proxies.this)
        return returnValue

    
    def setUsername(self, server, realm, username):
        returnValue = libpandaexpress._inP2KOdgpQq(self.this, server, realm, username)
        return returnValue

    
    def getUsername(self, server, realm):
        returnValue = libpandaexpress._inP2KOdlElE(self.this, server, realm)
        return returnValue

    
    def setHttpVersion(self, version):
        returnValue = libpandaexpress._inP2KOdsU3G(self.this, version)
        return returnValue

    
    def getHttpVersion(self):
        returnValue = libpandaexpress._inP2KOdMyb3(self.this)
        return returnValue

    
    def getHttpVersionString(self):
        returnValue = libpandaexpress._inP2KOd8nwv(self.this)
        return returnValue

    
    def loadCertificates(self, filename):
        returnValue = libpandaexpress._inP2KOdcD3X(self.this, filename.this)
        return returnValue

    
    def setVerifySsl(self, verifySsl):
        returnValue = libpandaexpress._inP2KOd7Lvd(self.this, verifySsl)
        return returnValue

    
    def getVerifySsl(self):
        returnValue = libpandaexpress._inP2KOdZMkP(self.this)
        return returnValue

    
    def setCipherList(self, cipherList):
        returnValue = libpandaexpress._inP2KOdQ6r0(self.this, cipherList)
        return returnValue

    
    def getCipherList(self):
        returnValue = libpandaexpress._inP2KOdqJQo(self.this)
        return returnValue

    
    def addExpectedServer(self, serverAttributes):
        returnValue = libpandaexpress._inP2KOdcDTY(self.this, serverAttributes)
        return returnValue

    
    def clearExpectedServers(self):
        returnValue = libpandaexpress._inP2KOd4GYo(self.this)
        return returnValue

    
    def makeChannel(self, persistentConnection):
        returnValue = libpandaexpress._inP2KOdEV90(self.this, persistentConnection)
        import HTTPChannel
        returnObject = HTTPChannel.HTTPChannel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def postForm(self, url, body):
        returnValue = libpandaexpress._inP2KOdd7dJ(self.this, url.this, body)
        import HTTPChannel
        returnObject = HTTPChannel.HTTPChannel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getDocument(self, url):
        returnValue = libpandaexpress._inP2KOdUmtQ(self.this, url.this)
        import HTTPChannel
        returnObject = HTTPChannel.HTTPChannel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getHeader(self, url):
        returnValue = libpandaexpress._inP2KOdC6NS(self.this, url.this)
        import HTTPChannel
        returnObject = HTTPChannel.HTTPChannel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._HTTPClient__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], HTTPClient):
                return self._HTTPClient__overloaded_constructor_ptrConstHTTPClient(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <HTTPClient> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getProxiesForUrl(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import URLSpec
            if isinstance(_args[0], URLSpec.URLSpec):
                return self._HTTPClient__overloaded_getProxiesForUrl_ptrConstHTTPClient_ptrConstURLSpec(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <URLSpec.URLSpec> '
        elif numArgs == 2:
            import URLSpec
            if isinstance(_args[0], URLSpec.URLSpec):
                import VectorURLSpec
                if isinstance(_args[1], VectorURLSpec.VectorURLSpec):
                    return self._HTTPClient__overloaded_getProxiesForUrl_ptrConstHTTPClient_ptrConstURLSpec_ptrVectorURLSpec(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VectorURLSpec.VectorURLSpec> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <URLSpec.URLSpec> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


