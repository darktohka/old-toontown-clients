# File: S (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RecorderBase

class SocketStreamRecorder(RecorderBase.RecorderBase, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _SocketStreamRecorder__overloaded_constructor(self):
        self.this = libpanda._inPc5FL4hpl()
        self.userManagesMemory = 1

    
    def _SocketStreamRecorder__overloaded_constructor_ptrSocketStream_bool(self, stream, ownsStream):
        self.this = libpanda._inPc5FLsab4(stream.this, ownsStream)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPc5FL24Kh:
            libpanda._inPc5FL24Kh(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPc5FLtYL0()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def receiveDatagram(self, dg):
        returnValue = libpanda._inPc5FL4uRL(self.this, dg.this)
        return returnValue

    
    def sendDatagram(self, dg):
        returnValue = libpanda._inPc5FL9r0L(self.this, dg.this)
        return returnValue

    
    def isClosed(self):
        returnValue = libpanda._inPc5FL5XJQ(self.this)
        return returnValue

    
    def close(self):
        returnValue = libpanda._inPc5FL2w02(self.this)
        return returnValue

    
    def setCollectTcp(self, collectTcp):
        returnValue = libpanda._inPc5FLhdjA(self.this, collectTcp)
        return returnValue

    
    def getCollectTcp(self):
        returnValue = libpanda._inPc5FLg_ig(self.this)
        return returnValue

    
    def setCollectTcpInterval(self, interval):
        returnValue = libpanda._inPc5FLvs9Y(self.this, interval)
        return returnValue

    
    def getCollectTcpInterval(self):
        returnValue = libpanda._inPc5FLs4oX(self.this)
        return returnValue

    
    def considerFlush(self):
        returnValue = libpanda._inPc5FLHOJb(self.this)
        return returnValue

    
    def flush(self):
        returnValue = libpanda._inPc5FL8T3a(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._SocketStreamRecorder__overloaded_constructor(*_args)
        elif numArgs == 2:
            return self._SocketStreamRecorder__overloaded_constructor_ptrSocketStream_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '


