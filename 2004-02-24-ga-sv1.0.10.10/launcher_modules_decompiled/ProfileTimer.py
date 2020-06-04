# File: P (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class ProfileTimer(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _ProfileTimer__overloaded_constructor_ptrConstProfileTimer(self, other):
        self.this = libpandaexpress._inPJoxtvclK(other.this)
        self.userManagesMemory = 1

    
    def _ProfileTimer__overloaded_constructor_atomicstring_int(self, name, maxEntries):
        self.this = libpandaexpress._inPJoxtCJKJ(name, maxEntries)
        self.userManagesMemory = 1

    
    def _ProfileTimer__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaexpress._inPJoxt1b5J(name)
        self.userManagesMemory = 1

    
    def _ProfileTimer__overloaded_constructor(self):
        self.this = libpandaexpress._inPJoxtzvu0()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxtP1oe:
            libpandaexpress._inPJoxtP1oe(self.this)
        

    
    def _ProfileTimer__overloaded_consolidateAllTo_ptrOstream(out):
        returnValue = libpandaexpress._inPJoxtq9_x(out.this)
        return returnValue

    _ProfileTimer__overloaded_consolidateAllTo_ptrOstream = staticmethod(_ProfileTimer__overloaded_consolidateAllTo_ptrOstream)
    
    def _ProfileTimer__overloaded_consolidateAllTo():
        returnValue = libpandaexpress._inPJoxtQiNX()
        return returnValue

    _ProfileTimer__overloaded_consolidateAllTo = staticmethod(_ProfileTimer__overloaded_consolidateAllTo)
    
    def _ProfileTimer__overloaded_printAllTo_ptrOstream(out):
        returnValue = libpandaexpress._inPJoxt1a5y(out.this)
        return returnValue

    _ProfileTimer__overloaded_printAllTo_ptrOstream = staticmethod(_ProfileTimer__overloaded_printAllTo_ptrOstream)
    
    def _ProfileTimer__overloaded_printAllTo():
        returnValue = libpandaexpress._inPJoxtR2g_()
        return returnValue

    _ProfileTimer__overloaded_printAllTo = staticmethod(_ProfileTimer__overloaded_printAllTo)
    
    def _ProfileTimer__overloaded_init_ptrProfileTimer_atomicstring_int(self, name, maxEntries):
        returnValue = libpandaexpress._inPJoxt98tX(self.this, name, maxEntries)
        return returnValue

    
    def _ProfileTimer__overloaded_init_ptrProfileTimer_atomicstring(self, name):
        returnValue = libpandaexpress._inPJoxti6RM(self.this, name)
        return returnValue

    
    def on(self):
        returnValue = libpandaexpress._inPJoxt9f04(self.this)
        return returnValue

    
    def mark(self, tag):
        returnValue = libpandaexpress._inPJoxtepR4(self.this, tag)
        return returnValue

    
    def _ProfileTimer__overloaded_off_ptrProfileTimer(self):
        returnValue = libpandaexpress._inPJoxtmqDp(self.this)
        return returnValue

    
    def _ProfileTimer__overloaded_off_ptrProfileTimer_atomicstring(self, tag):
        returnValue = libpandaexpress._inPJoxtez0S(self.this, tag)
        return returnValue

    
    def getTotalTime(self):
        returnValue = libpandaexpress._inPJoxtf1Vu(self.this)
        return returnValue

    
    def _ProfileTimer__overloaded_consolidateTo_ptrConstProfileTimer_ptrOstream(self, out):
        returnValue = libpandaexpress._inPJoxtLAMQ(self.this, out.this)
        return returnValue

    
    def _ProfileTimer__overloaded_consolidateTo_ptrConstProfileTimer(self):
        returnValue = libpandaexpress._inPJoxtENRS(self.this)
        return returnValue

    
    def _ProfileTimer__overloaded_printTo_ptrConstProfileTimer_ptrOstream(self, out):
        returnValue = libpandaexpress._inPJoxtUUXZ(self.this, out.this)
        return returnValue

    
    def _ProfileTimer__overloaded_printTo_ptrConstProfileTimer(self):
        returnValue = libpandaexpress._inPJoxtAgcv(self.this)
        return returnValue

    
    def consolidateAllTo(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return ProfileTimer._ProfileTimer__overloaded_consolidateAllTo()
        elif numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return ProfileTimer._ProfileTimer__overloaded_consolidateAllTo_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    consolidateAllTo = staticmethod(consolidateAllTo)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ProfileTimer__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._ProfileTimer__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], ProfileTimer):
                return self._ProfileTimer__overloaded_constructor_ptrConstProfileTimer(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <ProfileTimer> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._ProfileTimer__overloaded_constructor_atomicstring_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def printAllTo(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return ProfileTimer._ProfileTimer__overloaded_printAllTo()
        elif numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return ProfileTimer._ProfileTimer__overloaded_printAllTo_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    printAllTo = staticmethod(printAllTo)
    
    def printTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ProfileTimer__overloaded_printTo_ptrConstProfileTimer()
        elif numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._ProfileTimer__overloaded_printTo_ptrConstProfileTimer_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def init(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._ProfileTimer__overloaded_init_ptrProfileTimer_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._ProfileTimer__overloaded_init_ptrProfileTimer_atomicstring_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def off(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ProfileTimer__overloaded_off_ptrProfileTimer()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._ProfileTimer__overloaded_off_ptrProfileTimer_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def consolidateTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ProfileTimer__overloaded_consolidateTo_ptrConstProfileTimer()
        elif numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._ProfileTimer__overloaded_consolidateTo_ptrConstProfileTimer_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


