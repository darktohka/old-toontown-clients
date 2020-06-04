# File: E (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount

class Event(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Event__overloaded_constructor_ptrConstEvent(self, copy):
        self.this = libpandaexpress._inPekxobaOf(copy.this)
        self.userManagesMemory = 1

    
    def _Event__overloaded_constructor_atomicstring_ptrEventReceiver(self, eventName, receiver):
        self.this = libpandaexpress._inPekxo_Cqe(eventName, receiver.this)
        self.userManagesMemory = 1

    
    def _Event__overloaded_constructor_atomicstring(self, eventName):
        self.this = libpandaexpress._inPekxoiMjT(eventName)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaexpress._inPekxoUXdZ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaexpress._inPekxoyjne(self.this, copy.this)
        returnObject = Event(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setName(self, name):
        returnValue = libpandaexpress._inPekxo0_7n(self.this, name)
        return returnValue

    
    def clearName(self):
        returnValue = libpandaexpress._inPekxosUk3(self.this)
        return returnValue

    
    def hasName(self):
        returnValue = libpandaexpress._inPekxo8bdj(self.this)
        return returnValue

    
    def getName(self):
        returnValue = libpandaexpress._inPekxoCka7(self.this)
        return returnValue

    
    def addParameter(self, obj):
        returnValue = libpandaexpress._inPekxo7aTn(self.this, obj.this)
        return returnValue

    
    def getNumParameters(self):
        returnValue = libpandaexpress._inPekxouadO(self.this)
        return returnValue

    
    def getParameter(self, n):
        returnValue = libpandaexpress._inPekxoDpxs(self.this, n)
        import EventParameter
        returnObject = EventParameter.EventParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasReceiver(self):
        returnValue = libpandaexpress._inPekxouqic(self.this)
        return returnValue

    
    def getReceiver(self):
        returnValue = libpandaexpress._inPekxov9f0(self.this)
        import EventReceiver
        returnObject = EventReceiver.EventReceiver(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setReceiver(self, receiver):
        returnValue = libpandaexpress._inPekxoe1ch(self.this, receiver.this)
        return returnValue

    
    def clearReceiver(self):
        returnValue = libpandaexpress._inPekxoVAhd(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPekxoYPzc(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._Event__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], Event):
                return self._Event__overloaded_constructor_ptrConstEvent(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Event> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                import EventReceiver
                if isinstance(_args[1], EventReceiver.EventReceiver):
                    return self._Event__overloaded_constructor_atomicstring_ptrEventReceiver(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <EventReceiver.EventReceiver> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


