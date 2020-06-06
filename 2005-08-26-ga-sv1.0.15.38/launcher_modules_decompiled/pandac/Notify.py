# File: N (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class Notify(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaexpress._inPKoxtdB8d()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxt2gi0:
            libpandaexpress._inPKoxt2gi0(self.this)
        

    
    def out():
        returnValue = libpandaexpress._inPKoxtppce()
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    out = staticmethod(out)
    
    def null():
        returnValue = libpandaexpress._inPKoxtYCcj()
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    null = staticmethod(null)
    
    def writeString(str):
        returnValue = libpandaexpress._inPKoxtzqoR(str)
        return returnValue

    writeString = staticmethod(writeString)
    
    def ptr():
        returnValue = libpandaexpress._inPKoxt8DCI()
        returnObject = Notify(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    ptr = staticmethod(ptr)
    
    def setOstreamPtr(self, ostreamPtr, deleteLater):
        returnValue = libpandaexpress._inPKoxtvrEn(self.this, ostreamPtr.this, deleteLater)
        return returnValue

    
    def getOstreamPtr(self):
        returnValue = libpandaexpress._inPKoxtVkUe(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clearAssertHandler(self):
        returnValue = libpandaexpress._inPKoxt5Y26(self.this)
        return returnValue

    
    def hasAssertHandler(self):
        returnValue = libpandaexpress._inPKoxt_0e5(self.this)
        return returnValue

    
    def getAssertHandler(self):
        returnValue = libpandaexpress._inPKoxt6z03(self.this)
        return returnValue

    
    def hasAssertFailed(self):
        returnValue = libpandaexpress._inPKoxtWXtw(self.this)
        return returnValue

    
    def getAssertErrorMessage(self):
        returnValue = libpandaexpress._inPKoxtSHZe(self.this)
        return returnValue

    
    def clearAssertFailed(self):
        returnValue = libpandaexpress._inPKoxtu1XD(self.this)
        return returnValue

    
    def getTopCategory(self):
        returnValue = libpandaexpress._inPKoxt6gyi(self.this)
        import NotifyCategory
        returnObject = NotifyCategory.NotifyCategory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Notify__overloaded_getCategory_ptrNotify_atomicstring(self, fullname):
        returnValue = libpandaexpress._inPKoxtx5dT(self.this, fullname)
        import NotifyCategory
        returnObject = NotifyCategory.NotifyCategory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Notify__overloaded_getCategory_ptrNotify_atomicstring_ptrNotifyCategory(self, basename, parentCategory):
        returnValue = libpandaexpress._inPKoxt73Bf(self.this, basename, parentCategory.this)
        import NotifyCategory
        returnObject = NotifyCategory.NotifyCategory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Notify__overloaded_getCategory_ptrNotify_atomicstring_atomicstring(self, basename, parentFullname):
        returnValue = libpandaexpress._inPKoxt1kmX(self.this, basename, parentFullname)
        import NotifyCategory
        returnObject = NotifyCategory.NotifyCategory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getCategory(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Notify__overloaded_getCategory_ptrNotify_atomicstring(*_args)
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.StringType):
                    return self._Notify__overloaded_getCategory_ptrNotify_atomicstring_atomicstring(*_args)
                
                import NotifyCategory
                if isinstance(_args[1], NotifyCategory.NotifyCategory):
                    return self._Notify__overloaded_getCategory_ptrNotify_atomicstring_ptrNotifyCategory(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> <NotifyCategory.NotifyCategory> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


