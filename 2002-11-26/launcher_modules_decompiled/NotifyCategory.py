# File: N (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class NotifyCategory(FFIExternalObject.FFIExternalObject):
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
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtO6fS:
            libpandaexpress._inPJoxtO6fS(self.this)
        

    
    def getFullname(self):
        returnValue = libpandaexpress._inPJoxtFwaK(self.this)
        return returnValue

    
    def getBasename(self):
        returnValue = libpandaexpress._inPJoxt76Av(self.this)
        return returnValue

    
    def getSeverity(self):
        returnValue = libpandaexpress._inPJoxtgotj(self.this)
        return returnValue

    
    def setSeverity(self, severity):
        returnValue = libpandaexpress._inPJoxtXmtm(self.this, severity)
        return returnValue

    
    def isOn(self, severity):
        returnValue = libpandaexpress._inPJoxtNeuG(self.this, severity)
        return returnValue

    
    def isSpam(self):
        returnValue = libpandaexpress._inPJoxteQtp(self.this)
        return returnValue

    
    def isDebug(self):
        returnValue = libpandaexpress._inPJoxtzDGx(self.this)
        return returnValue

    
    def isInfo(self):
        returnValue = libpandaexpress._inPJoxtlDsK(self.this)
        return returnValue

    
    def isWarning(self):
        returnValue = libpandaexpress._inPJoxtOEpj(self.this)
        return returnValue

    
    def isError(self):
        returnValue = libpandaexpress._inPJoxt7Fq4(self.this)
        return returnValue

    
    def isFatal(self):
        returnValue = libpandaexpress._inPJoxtud58(self.this)
        return returnValue

    
    def _NotifyCategory__overloaded_out_ptrConstNotifyCategory___enum__NotifySeverity_bool(self, severity, prefix):
        returnValue = libpandaexpress._inPJoxtTXie(self.this, severity, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_out_ptrConstNotifyCategory___enum__NotifySeverity(self, severity):
        returnValue = libpandaexpress._inPJoxtTVa3(self.this, severity)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_spam_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPJoxtYZYH(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_spam_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPJoxt1AGf(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_debug_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPJoxtcLBq(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_debug_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPJoxtoz6f(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_info_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPJoxtdLKB(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_info_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPJoxt9Q3Y(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_warning_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPJoxtic9G(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_warning_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPJoxt6bPB(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_error_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPJoxte0DR(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_error_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPJoxtos7G(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_fatal_ptrConstNotifyCategory_bool(self, prefix):
        returnValue = libpandaexpress._inPJoxt_JPC(self.this, prefix)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _NotifyCategory__overloaded_fatal_ptrConstNotifyCategory(self):
        returnValue = libpandaexpress._inPJoxtseI4(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumChildren(self):
        returnValue = libpandaexpress._inPJoxt8NNN(self.this)
        return returnValue

    
    def getChild(self, i):
        returnValue = libpandaexpress._inPJoxt0YK4(self.this, i)
        returnObject = NotifyCategory(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def info(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_info_ptrConstNotifyCategory()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NotifyCategory__overloaded_info_ptrConstNotifyCategory_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def spam(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_spam_ptrConstNotifyCategory()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NotifyCategory__overloaded_spam_ptrConstNotifyCategory_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def warning(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_warning_ptrConstNotifyCategory()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NotifyCategory__overloaded_warning_ptrConstNotifyCategory_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def error(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_error_ptrConstNotifyCategory()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NotifyCategory__overloaded_error_ptrConstNotifyCategory_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def debug(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_debug_ptrConstNotifyCategory()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NotifyCategory__overloaded_debug_ptrConstNotifyCategory_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def fatal(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NotifyCategory__overloaded_fatal_ptrConstNotifyCategory()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NotifyCategory__overloaded_fatal_ptrConstNotifyCategory_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def out(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NotifyCategory__overloaded_out_ptrConstNotifyCategory___enum__NotifySeverity(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._NotifyCategory__overloaded_out_ptrConstNotifyCategory___enum__NotifySeverity_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


