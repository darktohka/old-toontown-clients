# File: D (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class DocumentSpec(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    RMEqualOrNewer = 3
    RMEqual = 1
    RMAny = 0
    RMNewer = 2
    CCAllowCache = 0
    CCRevalidate = 1
    CCNoCache = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DocumentSpec__overloaded_constructor(self):
        self.this = libpandaexpress._inP2KOdaGVJ()
        self.userManagesMemory = 1

    
    def _DocumentSpec__overloaded_constructor_ptrConstDocumentSpec(self, copy):
        self.this = libpandaexpress._inP2KOdrhhh(copy.this)
        self.userManagesMemory = 1

    
    def _DocumentSpec__overloaded_constructor_ptrConstURLSpec(self, url):
        self.this = libpandaexpress._inP2KOdBmXi(url.this)
        self.userManagesMemory = 1

    
    def _DocumentSpec__overloaded_constructor_atomicstring(self, url):
        self.this = libpandaexpress._inP2KOdctNb(url)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdQTkZ:
            libpandaexpress._inP2KOdQTkZ(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inP2KOdpTpy(self.this, copy.this)
        returnObject = DocumentSpec(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def eq(self, other):
        returnValue = libpandaexpress._inP2KOdiL7f(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inP2KOdzx6X(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inP2KOd2Z_X(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpandaexpress._inP2KOd4ZmY(self.this, other.this)
        return returnValue

    
    def setUrl(self, url):
        returnValue = libpandaexpress._inP2KOdUTc6(self.this, url.this)
        return returnValue

    
    def getUrl(self):
        returnValue = libpandaexpress._inP2KOdUTT8(self.this)
        import URLSpec
        returnObject = URLSpec.URLSpec(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setTag(self, tag):
        returnValue = libpandaexpress._inP2KOdKAZX(self.this, tag.this)
        return returnValue

    
    def hasTag(self):
        returnValue = libpandaexpress._inP2KOdbgI_(self.this)
        return returnValue

    
    def getTag(self):
        returnValue = libpandaexpress._inP2KOdTNmT(self.this)
        import HTTPEntityTag
        returnObject = HTTPEntityTag.HTTPEntityTag(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clearTag(self):
        returnValue = libpandaexpress._inP2KOdHg2z(self.this)
        return returnValue

    
    def setDate(self, date):
        returnValue = libpandaexpress._inP2KOdBu_L(self.this, date.this)
        return returnValue

    
    def hasDate(self):
        returnValue = libpandaexpress._inP2KOdwwOq(self.this)
        return returnValue

    
    def getDate(self):
        returnValue = libpandaexpress._inP2KOd16s_(self.this)
        import HTTPDate
        returnObject = HTTPDate.HTTPDate(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clearDate(self):
        returnValue = libpandaexpress._inP2KOd1ns7(self.this)
        return returnValue

    
    def setRequestMode(self, requestMode):
        returnValue = libpandaexpress._inP2KOdOwGy(self.this, requestMode)
        return returnValue

    
    def getRequestMode(self):
        returnValue = libpandaexpress._inP2KOdis_z(self.this)
        return returnValue

    
    def setCacheControl(self, cacheControl):
        returnValue = libpandaexpress._inP2KOdaqta(self.this, cacheControl)
        return returnValue

    
    def getCacheControl(self):
        returnValue = libpandaexpress._inP2KOdiIC1(self.this)
        return returnValue

    
    def input(self, _in):
        returnValue = libpandaexpress._inP2KOdXwSU(self.this, _in.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inP2KOdg56_(self.this, out.this)
        return returnValue

    
    def _DocumentSpec__overloaded_write_ptrConstDocumentSpec_ptrOstream_int(self, out, indentLevel):
        returnValue = libpandaexpress._inP2KOdEH_O(self.this, out.this, indentLevel)
        return returnValue

    
    def _DocumentSpec__overloaded_write_ptrConstDocumentSpec_ptrOstream(self, out):
        returnValue = libpandaexpress._inP2KOdf_Sn(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DocumentSpec__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DocumentSpec__overloaded_constructor_atomicstring(*_args)
            
            import URLSpec
            if isinstance(_args[0], URLSpec.URLSpec):
                return self._DocumentSpec__overloaded_constructor_ptrConstURLSpec(*_args)
            
            if isinstance(_args[0], DocumentSpec):
                return self._DocumentSpec__overloaded_constructor_ptrConstDocumentSpec(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <URLSpec.URLSpec> <DocumentSpec> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DocumentSpec__overloaded_write_ptrConstDocumentSpec_ptrOstream(*_args)
        elif numArgs == 2:
            return self._DocumentSpec__overloaded_write_ptrConstDocumentSpec_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


