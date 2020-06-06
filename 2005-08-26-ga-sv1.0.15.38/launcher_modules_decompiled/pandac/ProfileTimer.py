# File: P (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class ProfileTimer(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ProfileTimer__overloaded_constructor_ptrConstProfileTimer(self, other):
        self.this = libpandaexpress._inPKoxtvclK(other.this)
        self.userManagesMemory = 1

    
    def _ProfileTimer__overloaded_constructor_atomicstring_int(self, name, maxEntries):
        self.this = libpandaexpress._inPKoxtCJKJ(name, maxEntries)
        self.userManagesMemory = 1

    
    def _ProfileTimer__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaexpress._inPKoxt1b5J(name)
        self.userManagesMemory = 1

    
    def _ProfileTimer__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtyvu0()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtP1oe:
            libpandaexpress._inPKoxtP1oe(self.this)
        

    
    def _ProfileTimer__overloaded_consolidateAllTo_ptrOstream(out):
        returnValue = libpandaexpress._inPKoxtr9_x(out.this)
        return returnValue

    _ProfileTimer__overloaded_consolidateAllTo_ptrOstream = staticmethod(_ProfileTimer__overloaded_consolidateAllTo_ptrOstream)
    
    def _ProfileTimer__overloaded_consolidateAllTo():
        returnValue = libpandaexpress._inPKoxtQiNX()
        return returnValue

    _ProfileTimer__overloaded_consolidateAllTo = staticmethod(_ProfileTimer__overloaded_consolidateAllTo)
    
    def _ProfileTimer__overloaded_printAllTo_ptrOstream(out):
        returnValue = libpandaexpress._inPKoxt0a5y(out.this)
        return returnValue

    _ProfileTimer__overloaded_printAllTo_ptrOstream = staticmethod(_ProfileTimer__overloaded_printAllTo_ptrOstream)
    
    def _ProfileTimer__overloaded_printAllTo():
        returnValue = libpandaexpress._inPKoxtupg_()
        return returnValue

    _ProfileTimer__overloaded_printAllTo = staticmethod(_ProfileTimer__overloaded_printAllTo)
    
    def _ProfileTimer__overloaded_init_ptrProfileTimer_atomicstring_int(self, name, maxEntries):
        returnValue = libpandaexpress._inPKoxt98tX(self.this, name, maxEntries)
        return returnValue

    
    def _ProfileTimer__overloaded_init_ptrProfileTimer_atomicstring(self, name):
        returnValue = libpandaexpress._inPKoxti6RM(self.this, name)
        return returnValue

    
    def on(self):
        returnValue = libpandaexpress._inPKoxt8f04(self.this)
        return returnValue

    
    def mark(self, tag):
        returnValue = libpandaexpress._inPKoxtZpR4(self.this, tag)
        return returnValue

    
    def _ProfileTimer__overloaded_off_ptrProfileTimer(self):
        returnValue = libpandaexpress._inPKoxt5qDp(self.this)
        return returnValue

    
    def _ProfileTimer__overloaded_off_ptrProfileTimer_atomicstring(self, tag):
        returnValue = libpandaexpress._inPKoxtez0S(self.this, tag)
        return returnValue

    
    def getTotalTime(self):
        returnValue = libpandaexpress._inPKoxtQ1Vu(self.this)
        return returnValue

    
    def _ProfileTimer__overloaded_consolidateTo_ptrConstProfileTimer_ptrOstream(self, out):
        returnValue = libpandaexpress._inPKoxtLAMQ(self.this, out.this)
        return returnValue

    
    def _ProfileTimer__overloaded_consolidateTo_ptrConstProfileTimer(self):
        returnValue = libpandaexpress._inPKoxtENRS(self.this)
        return returnValue

    
    def _ProfileTimer__overloaded_printTo_ptrConstProfileTimer_ptrOstream(self, out):
        returnValue = libpandaexpress._inPKoxtUUXZ(self.this, out.this)
        return returnValue

    
    def _ProfileTimer__overloaded_printTo_ptrConstProfileTimer(self):
        returnValue = libpandaexpress._inPKoxtBgcv(self.this)
        return returnValue

    
    def consolidateAllTo(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return ProfileTimer._ProfileTimer__overloaded_consolidateAllTo(*_args)
        elif numArgs == 1:
            return ProfileTimer._ProfileTimer__overloaded_consolidateAllTo_ptrOstream(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    consolidateAllTo = staticmethod(consolidateAllTo)
    
    def printAllTo(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return ProfileTimer._ProfileTimer__overloaded_printAllTo(*_args)
        elif numArgs == 1:
            return ProfileTimer._ProfileTimer__overloaded_printAllTo_ptrOstream(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    printAllTo = staticmethod(printAllTo)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ProfileTimer__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._ProfileTimer__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], ProfileTimer):
                return self._ProfileTimer__overloaded_constructor_ptrConstProfileTimer(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <ProfileTimer> '
        elif numArgs == 2:
            return self._ProfileTimer__overloaded_constructor_atomicstring_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def printTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ProfileTimer__overloaded_printTo_ptrConstProfileTimer(*_args)
        elif numArgs == 1:
            return self._ProfileTimer__overloaded_printTo_ptrConstProfileTimer_ptrOstream(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def init(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ProfileTimer__overloaded_init_ptrProfileTimer_atomicstring(*_args)
        elif numArgs == 2:
            return self._ProfileTimer__overloaded_init_ptrProfileTimer_atomicstring_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def off(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ProfileTimer__overloaded_off_ptrProfileTimer(*_args)
        elif numArgs == 1:
            return self._ProfileTimer__overloaded_off_ptrProfileTimer_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def consolidateTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ProfileTimer__overloaded_consolidateTo_ptrConstProfileTimer(*_args)
        elif numArgs == 1:
            return self._ProfileTimer__overloaded_consolidateTo_ptrConstProfileTimer_ptrOstream(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


