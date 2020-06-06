# File: N (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class NotifyCategory(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
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
        if libpandaexpress and libpandaexpress._inPKoxtO6fS:
            libpandaexpress._inPKoxtO6fS(self.this)
        

    
    def setServerDelta(delta):
        returnValue = libpandaexpress._inPKoxtHFLo(delta)
        return returnValue

    setServerDelta = staticmethod(setServerDelta)
    
    def getFullname(self):
        returnValue = libpandaexpress._inPKoxtFwaK(self.this)
        return returnValue

    
    def getBasename(self):
        returnValue = libpandaexpress._inPKoxt66Av(self.this)
        return returnValue

    
    def getSeverity(self):
        returnValue = libpandaexpress._inPKoxtjotj(self.this)
        return returnValue

    
    def setSeverity(self, severity):
        returnValue = libpandaexpress._inPKoxtQmtm(self.this, severity)
        return returnValue

    
    def isOn(self, severity):
        returnValue = libpandaexpress._inPKoxtNeuG(self.this, severity)
        return returnValue

    
    def isSpam(self):
        returnValue = libpandaexpress._inPKoxtdQtp(self.this)
        return returnValue

    
    def isDebug(self):
        returnValue = libpandaexpress._inPKoxtyDGx(self.this)
        return returnValue

    
    def isInfo(self):
        returnValue = libpandaexpress._inPKoxtlDsK(self.this)
        return returnValue

    
    def isWarning(self):
        returnValue = libpandaexpress._inPKoxtPEpj(self.this)
        return returnValue

    
    def isError(self):
        returnValue = libpandaexpress._inPKoxt6Fq4(self.this)
        return returnValue

    
    def isFatal(self):
        returnValue = libpandaexpress._inPKoxtvd58(self.this)
        return returnValue

    
    def _NotifyCategory__overloaded_out_ptrConstNotifyCategory___enum__NotifySeverity_bool(self, severity, prefix):
        returnValue = libpandaexpress._inPKoxtTXie(self.this, severity, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_out_ptrConstNotifyCategory___enum__NotifySeverity(self, severity):
        returnValue = libpandaexpress._inPKoxtUVa3(self.this, severity)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_spam_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPKoxtYZYH(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_spam_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPKoxt1AGf(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_debug_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPKoxtdLBq(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_debug_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPKoxtoz6f(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_info_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPKoxtdLKB(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_info_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPKoxt9Q3Y(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_warning_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPKoxtic9G(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_warning_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPKoxt6bPB(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_error_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPKoxte0DR(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_error_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPKoxtos7G(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_fatal_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPKoxt_JPC(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_fatal_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPKoxtreI4(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumChildren(self):
        returnValue = libpandaexpress._inPKoxt8NNN(self.this)
        return returnValue

    
    def getChild(self, i):
        returnValue = libpandaexpress._inPKoxt1YK4(self.this, i)
        returnObject = NotifyCategory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def info(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_info_ptrConstNotifyCategory(*_args)
        elif numArgs == 1:
            return self._NotifyCategory__overloaded_info_ptrConstNotifyCategory_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def spam(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_spam_ptrConstNotifyCategory(*_args)
        elif numArgs == 1:
            return self._NotifyCategory__overloaded_spam_ptrConstNotifyCategory_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def warning(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_warning_ptrConstNotifyCategory(*_args)
        elif numArgs == 1:
            return self._NotifyCategory__overloaded_warning_ptrConstNotifyCategory_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def error(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_error_ptrConstNotifyCategory(*_args)
        elif numArgs == 1:
            return self._NotifyCategory__overloaded_error_ptrConstNotifyCategory_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def debug(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_debug_ptrConstNotifyCategory(*_args)
        elif numArgs == 1:
            return self._NotifyCategory__overloaded_debug_ptrConstNotifyCategory_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def fatal(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_fatal_ptrConstNotifyCategory(*_args)
        elif numArgs == 1:
            return self._NotifyCategory__overloaded_fatal_ptrConstNotifyCategory_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def out(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._NotifyCategory__overloaded_out_ptrConstNotifyCategory___enum__NotifySeverity(*_args)
        elif numArgs == 2:
            return self._NotifyCategory__overloaded_out_ptrConstNotifyCategory___enum__NotifySeverity_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


