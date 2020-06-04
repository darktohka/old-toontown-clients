# File: U (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class URLSpec(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _URLSpec__overloaded_constructor(self):
        self.this = libpandaexpress._inP2KOdd3sO()
        self.userManagesMemory = 1

    
    def _URLSpec__overloaded_constructor_ptrConstURLSpec(self, copy):
        self.this = libpandaexpress._inP2KOdLJ80(copy.this)
        self.userManagesMemory = 1

    
    def _URLSpec__overloaded_constructor_atomicstring_bool(self, url, serverNameExpected):
        self.this = libpandaexpress._inP2KOdbRSb(url, serverNameExpected)
        self.userManagesMemory = 1

    
    def _URLSpec__overloaded_constructor_atomicstring(self, url):
        self.this = libpandaexpress._inP2KOdqRHT(url)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOd6ZkA:
            libpandaexpress._inP2KOd6ZkA(self.this)
        

    
    def _URLSpec__overloaded_quote_atomicstring_atomicstring(source, safe):
        returnValue = libpandaexpress._inP2KOdko8E(source, safe)
        return returnValue

    _URLSpec__overloaded_quote_atomicstring_atomicstring = staticmethod(_URLSpec__overloaded_quote_atomicstring_atomicstring)
    
    def _URLSpec__overloaded_quote_atomicstring(source):
        returnValue = libpandaexpress._inP2KOddj8i(source)
        return returnValue

    _URLSpec__overloaded_quote_atomicstring = staticmethod(_URLSpec__overloaded_quote_atomicstring)
    
    def _URLSpec__overloaded_quotePlus_atomicstring_atomicstring(source, safe):
        returnValue = libpandaexpress._inP2KOdCXNb(source, safe)
        return returnValue

    _URLSpec__overloaded_quotePlus_atomicstring_atomicstring = staticmethod(_URLSpec__overloaded_quotePlus_atomicstring_atomicstring)
    
    def _URLSpec__overloaded_quotePlus_atomicstring(source):
        returnValue = libpandaexpress._inP2KOdo8IX(source)
        return returnValue

    _URLSpec__overloaded_quotePlus_atomicstring = staticmethod(_URLSpec__overloaded_quotePlus_atomicstring)
    
    def unquote(source):
        returnValue = libpandaexpress._inP2KOdsqPc(source)
        return returnValue

    unquote = staticmethod(unquote)
    
    def unquotePlus(source):
        returnValue = libpandaexpress._inP2KOdF1dJ(source)
        return returnValue

    unquotePlus = staticmethod(unquotePlus)
    
    def _URLSpec__overloaded_assign_ptrURLSpec_ptrConstURLSpec(self, copy):
        returnValue = libpandaexpress._inP2KOdeMOO(self.this, copy.this)
        returnObject = URLSpec(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _URLSpec__overloaded_assign_ptrURLSpec_atomicstring(self, url):
        returnValue = libpandaexpress._inP2KOdhCwY(self.this, url)
        returnObject = URLSpec(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def eq(self, other):
        returnValue = libpandaexpress._inP2KOdUZVF(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inP2KOdj_VB(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inP2KOdq_Dk(self.this, other.this)
        return returnValue

    
    def hasScheme(self):
        returnValue = libpandaexpress._inP2KOdaXfj(self.this)
        return returnValue

    
    def hasAuthority(self):
        returnValue = libpandaexpress._inP2KOd7GBb(self.this)
        return returnValue

    
    def hasUsername(self):
        returnValue = libpandaexpress._inP2KOdMvY8(self.this)
        return returnValue

    
    def hasServer(self):
        returnValue = libpandaexpress._inP2KOd7ZQR(self.this)
        return returnValue

    
    def hasPort(self):
        returnValue = libpandaexpress._inP2KOdMCN_(self.this)
        return returnValue

    
    def hasPath(self):
        returnValue = libpandaexpress._inP2KOdsN5k(self.this)
        return returnValue

    
    def hasQuery(self):
        returnValue = libpandaexpress._inP2KOdSAZN(self.this)
        return returnValue

    
    def getScheme(self):
        returnValue = libpandaexpress._inP2KOdEoNu(self.this)
        return returnValue

    
    def getAuthority(self):
        returnValue = libpandaexpress._inP2KOd8ewl(self.this)
        return returnValue

    
    def getUsername(self):
        returnValue = libpandaexpress._inP2KOdiXGH(self.this)
        return returnValue

    
    def getServer(self):
        returnValue = libpandaexpress._inP2KOdz1_b(self.this)
        return returnValue

    
    def getPortStr(self):
        returnValue = libpandaexpress._inP2KOdYGG8(self.this)
        return returnValue

    
    def getPort(self):
        returnValue = libpandaexpress._inP2KOdqS8J(self.this)
        return returnValue

    
    def getServerAndPort(self):
        returnValue = libpandaexpress._inP2KOdDsHV(self.this)
        return returnValue

    
    def getPath(self):
        returnValue = libpandaexpress._inP2KOdGWmv(self.this)
        return returnValue

    
    def getQuery(self):
        returnValue = libpandaexpress._inP2KOdU1HY(self.this)
        return returnValue

    
    def getUrl(self):
        returnValue = libpandaexpress._inP2KOdDCPV(self.this)
        return returnValue

    
    def setScheme(self, scheme):
        returnValue = libpandaexpress._inP2KOdjPvz(self.this, scheme)
        return returnValue

    
    def setAuthority(self, authority):
        returnValue = libpandaexpress._inP2KOdOWTX(self.this, authority)
        return returnValue

    
    def setUsername(self, username):
        returnValue = libpandaexpress._inP2KOdw7oh(self.this, username)
        return returnValue

    
    def setServer(self, server):
        returnValue = libpandaexpress._inP2KOdyigh(self.this, server)
        return returnValue

    
    def _URLSpec__overloaded_setPort_ptrURLSpec_atomicstring(self, port):
        returnValue = libpandaexpress._inP2KOd11tS(self.this, port)
        return returnValue

    
    def _URLSpec__overloaded_setPort_ptrURLSpec_int(self, port):
        returnValue = libpandaexpress._inP2KOdX1E4(self.this, port)
        return returnValue

    
    def setServerAndPort(self, serverAndPort):
        returnValue = libpandaexpress._inP2KOdJbzZ(self.this, serverAndPort)
        return returnValue

    
    def setPath(self, path):
        returnValue = libpandaexpress._inP2KOdahX4(self.this, path)
        return returnValue

    
    def setQuery(self, query):
        returnValue = libpandaexpress._inP2KOd11SR(self.this, query)
        return returnValue

    
    def _URLSpec__overloaded_setUrl_ptrURLSpec_atomicstring_bool(self, url, serverNameExpected):
        returnValue = libpandaexpress._inP2KOdEfs6(self.this, url, serverNameExpected)
        return returnValue

    
    def _URLSpec__overloaded_setUrl_ptrURLSpec_atomicstring(self, url):
        returnValue = libpandaexpress._inP2KOdDXhy(self.this, url)
        return returnValue

    
    def cStr(self):
        returnValue = libpandaexpress._inP2KOd1Ix1(self.this)
        return returnValue

    
    def empty(self):
        returnValue = libpandaexpress._inP2KOdAkB4(self.this)
        return returnValue

    
    def length(self):
        returnValue = libpandaexpress._inP2KOdNVhO(self.this)
        return returnValue

    
    def __getitem__(self, n):
        returnValue = libpandaexpress._inP2KOd7pUs(self.this, n)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inP2KOdhWk2(self.this, out.this)
        return returnValue

    
    def quote(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return URLSpec._URLSpec__overloaded_quote_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.StringType):
                    return URLSpec._URLSpec__overloaded_quote_atomicstring_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    quote = staticmethod(quote)
    
    def quotePlus(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return URLSpec._URLSpec__overloaded_quotePlus_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.StringType):
                    return URLSpec._URLSpec__overloaded_quotePlus_atomicstring_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    quotePlus = staticmethod(quotePlus)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._URLSpec__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._URLSpec__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], URLSpec):
                return self._URLSpec__overloaded_constructor_ptrConstURLSpec(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <URLSpec> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._URLSpec__overloaded_constructor_atomicstring_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def setUrl(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._URLSpec__overloaded_setUrl_ptrURLSpec_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._URLSpec__overloaded_setUrl_ptrURLSpec_atomicstring_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setPort(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._URLSpec__overloaded_setPort_ptrURLSpec_int(_args[0])
            elif isinstance(_args[0], types.StringType):
                return self._URLSpec__overloaded_setPort_ptrURLSpec_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._URLSpec__overloaded_assign_ptrURLSpec_atomicstring(_args[0])
            elif isinstance(_args[0], URLSpec):
                return self._URLSpec__overloaded_assign_ptrURLSpec_ptrConstURLSpec(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <URLSpec> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


