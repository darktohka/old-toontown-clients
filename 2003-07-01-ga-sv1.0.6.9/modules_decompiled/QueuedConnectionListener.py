# File: Q (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ConnectionListener
import QueuedReturnConnectionListenerData

class QueuedConnectionListener(ConnectionListener.ConnectionListener, QueuedReturnConnectionListenerData.QueuedReturnConnectionListenerData, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, manager, numThreads):
        self.this = libpanda._inP9ImMIgYr(manager.this, numThreads)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inP9ImMN_NM:
            libpanda._inP9ImMN_NM(self.this)
        

    
    def newConnectionAvailable(self):
        returnValue = libpanda._inP9ImMjF0a(self.this)
        return returnValue

    
    def _QueuedConnectionListener__overloaded_getNewConnection_ptrQueuedConnectionListener_ptrPointerToConnection(self, newConnection):
        returnValue = libpanda._inP9ImMwbmC(self.this, newConnection.this)
        return returnValue

    
    def _QueuedConnectionListener__overloaded_getNewConnection_ptrQueuedConnectionListener_ptrPointerToConnection_ptrNetAddress_ptrPointerToConnection(self, rendezvous, address, newConnection):
        returnValue = libpanda._inP9ImMieyI(self.this, rendezvous.this, address.this, newConnection.this)
        return returnValue

    
    def upcastToQueuedReturnConnectionListenerData(self):
        returnValue = libpanda._inP9ImM_bnE(self.this)
        import QueuedReturnConnectionListenerData
        returnObject = QueuedReturnConnectionListenerData.QueuedReturnConnectionListenerData(None)
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
        upcastSelf = upcastSelf.upcastToQueuedReturnConnectionListenerData()
        returnValue = libpanda._inP9ImMRXgW(upcastSelf.this, maxSize)
        return returnValue

    
    def getMaxQueueSize(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToQueuedReturnConnectionListenerData()
        returnValue = libpanda._inP9ImM_qdb(upcastSelf.this)
        return returnValue

    
    def getCurrentQueueSize(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToQueuedReturnConnectionListenerData()
        returnValue = libpanda._inP9ImMzNtc(upcastSelf.this)
        return returnValue

    
    def getNewConnection(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PointerToConnection
            if isinstance(_args[0], PointerToConnection.PointerToConnection):
                return self._QueuedConnectionListener__overloaded_getNewConnection_ptrQueuedConnectionListener_ptrPointerToConnection(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PointerToConnection.PointerToConnection> '
        elif numArgs == 3:
            import PointerToConnection
            if isinstance(_args[0], PointerToConnection.PointerToConnection):
                import NetAddress
                if isinstance(_args[1], NetAddress.NetAddress):
                    import PointerToConnection
                    if isinstance(_args[2], PointerToConnection.PointerToConnection):
                        return self._QueuedConnectionListener__overloaded_getNewConnection_ptrQueuedConnectionListener_ptrPointerToConnection_ptrNetAddress_ptrPointerToConnection(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <PointerToConnection.PointerToConnection> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <NetAddress.NetAddress> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PointerToConnection.PointerToConnection> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


