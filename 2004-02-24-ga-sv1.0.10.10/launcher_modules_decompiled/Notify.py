# File: N (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class Notify(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpandaexpress._inPJoxtdB8d()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxt1gi0:
            libpandaexpress._inPJoxt1gi0(self.this)
        

    
    def out():
        returnValue = libpandaexpress._inPJoxtppce()
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    out = staticmethod(out)
    
    def null():
        returnValue = libpandaexpress._inPJoxtZCcj()
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    null = staticmethod(null)
    
    def writeString(str):
        returnValue = libpandaexpress._inPJoxtzqoR(str)
        return returnValue

    writeString = staticmethod(writeString)
    
    def ptr():
        returnValue = libpandaexpress._inPJoxt8DCI()
        returnObject = Notify(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    ptr = staticmethod(ptr)
    
    def setOstreamPtr(self, ostreamPtr, deleteLater):
        returnValue = libpandaexpress._inPJoxturEn(self.this, ostreamPtr.this, deleteLater)
        return returnValue

    
    def getOstreamPtr(self):
        returnValue = libpandaexpress._inPJoxtVkUe(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def clearAssertHandler(self):
        returnValue = libpandaexpress._inPJoxt4Y26(self.this)
        return returnValue

    
    def hasAssertHandler(self):
        returnValue = libpandaexpress._inPJoxt_0e5(self.this)
        return returnValue

    
    def getAssertHandler(self):
        returnValue = libpandaexpress._inPJoxt5z03(self.this)
        return returnValue

    
    def hasAssertFailed(self):
        returnValue = libpandaexpress._inPJoxtVXtw(self.this)
        return returnValue

    
    def getAssertErrorMessage(self):
        returnValue = libpandaexpress._inPJoxtSHZe(self.this)
        return returnValue

    
    def clearAssertFailed(self):
        returnValue = libpandaexpress._inPJoxtu1XD(self.this)
        return returnValue

    
    def getTopCategory(self):
        returnValue = libpandaexpress._inPJoxt7gyi(self.this)
        import NotifyCategory
        returnObject = NotifyCategory.NotifyCategory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Notify__overloaded_getCategory_ptrNotify_atomicstring(self, fullname):
        returnValue = libpandaexpress._inPJoxtx5dT(self.this, fullname)
        import NotifyCategory
        returnObject = NotifyCategory.NotifyCategory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Notify__overloaded_getCategory_ptrNotify_atomicstring_ptrNotifyCategory(self, basename, parentCategory):
        returnValue = libpandaexpress._inPJoxt73Bf(self.this, basename, parentCategory.this)
        import NotifyCategory
        returnObject = NotifyCategory.NotifyCategory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Notify__overloaded_getCategory_ptrNotify_atomicstring_atomicstring(self, basename, parentFullname):
        returnValue = libpandaexpress._inPJoxt1kmX(self.this, basename, parentFullname)
        import NotifyCategory
        returnObject = NotifyCategory.NotifyCategory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getCategory(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Notify__overloaded_getCategory_ptrNotify_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                import NotifyCategory
                if isinstance(_args[1], types.StringType):
                    return self._Notify__overloaded_getCategory_ptrNotify_atomicstring_atomicstring(_args[0], _args[1])
                elif isinstance(_args[1], NotifyCategory.NotifyCategory):
                    return self._Notify__overloaded_getCategory_ptrNotify_atomicstring_ptrNotifyCategory(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> <NotifyCategory.NotifyCategory> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


