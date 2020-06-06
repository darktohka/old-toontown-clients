# File: E (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class Event(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Event__overloaded_constructor_ptrConstEvent(self, copy):
        self.this = libpanda._inPfkxobaOf(copy.this)
        self.userManagesMemory = 1

    
    def _Event__overloaded_constructor_atomicstring_ptrEventReceiver(self, eventName, receiver):
        self.this = libpanda._inPfkxo_Cqe(eventName, receiver.this)
        self.userManagesMemory = 1

    
    def _Event__overloaded_constructor_atomicstring(self, eventName):
        self.this = libpanda._inPfkxoiMjT(eventName)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPfkxoUXdZ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpanda._inPfkxoyjne(self.this, copy.this)
        returnObject = Event(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setName(self, name):
        returnValue = libpanda._inPfkxo3_7n(self.this, name)
        return returnValue

    
    def clearName(self):
        returnValue = libpanda._inPfkxorUk3(self.this)
        return returnValue

    
    def hasName(self):
        returnValue = libpanda._inPfkxo9bdj(self.this)
        return returnValue

    
    def getName(self):
        returnValue = libpanda._inPfkxoDka7(self.this)
        return returnValue

    
    def addParameter(self, obj):
        returnValue = libpanda._inPfkxo6aTn(self.this, obj.this)
        return returnValue

    
    def getNumParameters(self):
        returnValue = libpanda._inPfkxouadO(self.this)
        return returnValue

    
    def getParameter(self, n):
        returnValue = libpanda._inPfkxoCpxs(self.this, n)
        import EventParameter
        returnObject = EventParameter.EventParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasReceiver(self):
        returnValue = libpanda._inPfkxouqic(self.this)
        return returnValue

    
    def getReceiver(self):
        returnValue = libpanda._inPfkxog9f0(self.this)
        import EventReceiver
        returnObject = EventReceiver.EventReceiver(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setReceiver(self, receiver):
        returnValue = libpanda._inPfkxof1ch(self.this, receiver.this)
        return returnValue

    
    def clearReceiver(self):
        returnValue = libpanda._inPfkxoVAhd(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPfkxoYPzc(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Event__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], Event):
                return self._Event__overloaded_constructor_ptrConstEvent(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Event> '
        elif numArgs == 2:
            return self._Event__overloaded_constructor_atomicstring_ptrEventReceiver(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


