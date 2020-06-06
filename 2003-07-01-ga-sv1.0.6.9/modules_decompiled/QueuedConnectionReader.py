# File: Q (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ConnectionReader
import QueuedReturnNetDatagram

class QueuedConnectionReader(ConnectionReader.ConnectionReader, QueuedReturnNetDatagram.QueuedReturnNetDatagram, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, manager, numThreads):
        self.this = libpanda._inP9ImMg6wa(manager.this, numThreads)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inP9ImMzbDn:
            libpanda._inP9ImMzbDn(self.this)
        

    
    def dataAvailable(self):
        returnValue = libpanda._inP9ImM36NV(self.this)
        return returnValue

    
    def _QueuedConnectionReader__overloaded_getData_ptrQueuedConnectionReader_ptrDatagram(self, result):
        returnValue = libpanda._inP9ImM5yzz(self.this, result.this)
        return returnValue

    
    def _QueuedConnectionReader__overloaded_getData_ptrQueuedConnectionReader_ptrNetDatagram(self, result):
        returnValue = libpanda._inP9ImMW1An(self.this, result.this)
        return returnValue

    
    def upcastToQueuedReturnNetDatagram(self):
        returnValue = libpanda._inP9ImMov2h(self.this)
        import QueuedReturnNetDatagram
        returnObject = QueuedReturnNetDatagram.QueuedReturnNetDatagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def addConnection(self, connection):
        upcastSelf = self
        returnValue = libpanda._inP9ImMqLA4(upcastSelf.this, connection.this)
        return returnValue

    
    def removeConnection(self, connection):
        upcastSelf = self
        returnValue = libpanda._inP9ImMBUJ8(upcastSelf.this, connection.this)
        return returnValue

    
    def isConnectionOk(self, connection):
        upcastSelf = self
        returnValue = libpanda._inP9ImMNKeX(upcastSelf.this, connection.this)
        return returnValue

    
    def poll(self):
        upcastSelf = self
        returnValue = libpanda._inP9ImMXxFz(upcastSelf.this)
        return returnValue

    
    def getManager(self):
        upcastSelf = self
        returnValue = libpanda._inP9ImMivcH(upcastSelf.this)
        import ConnectionManager
        returnObject = ConnectionManager.ConnectionManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isPolling(self):
        upcastSelf = self
        returnValue = libpanda._inP9ImMLEEA(upcastSelf.this)
        return returnValue

    
    def getNumThreads(self):
        upcastSelf = self
        returnValue = libpanda._inP9ImM2jeO(upcastSelf.this)
        return returnValue

    
    def setRawMode(self, mode):
        upcastSelf = self
        returnValue = libpanda._inP9ImM7duY(upcastSelf.this, mode)
        return returnValue

    
    def getRawMode(self):
        upcastSelf = self
        returnValue = libpanda._inP9ImMCWld(upcastSelf.this)
        return returnValue

    
    def setMaxQueueSize(self, maxSize):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToQueuedReturnNetDatagram()
        returnValue = libpanda._inP9ImMSCal(upcastSelf.this, maxSize)
        return returnValue

    
    def getMaxQueueSize(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToQueuedReturnNetDatagram()
        returnValue = libpanda._inP9ImM2D9N(upcastSelf.this)
        return returnValue

    
    def getCurrentQueueSize(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToQueuedReturnNetDatagram()
        returnValue = libpanda._inP9ImM4Ce3(upcastSelf.this)
        return returnValue

    
    def getData(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Datagram
            import NetDatagram
            if isinstance(_args[0], Datagram.Datagram):
                return self._QueuedConnectionReader__overloaded_getData_ptrQueuedConnectionReader_ptrDatagram(_args[0])
            elif isinstance(_args[0], NetDatagram.NetDatagram):
                return self._QueuedConnectionReader__overloaded_getData_ptrQueuedConnectionReader_ptrNetDatagram(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> <NetDatagram.NetDatagram> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


