# File: Q (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ConnectionManager
import QueuedReturnPointerToConnection

class QueuedConnectionManager(ConnectionManager.ConnectionManager, QueuedReturnPointerToConnection.QueuedReturnPointerToConnection, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inP9ImM4UnC()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inP9ImMqHMK:
            libpanda._inP9ImMqHMK(self.this)
        

    
    def resetConnectionAvailable(self):
        returnValue = libpanda._inP9ImM_mZr(self.this)
        return returnValue

    
    def getResetConnection(self, connection):
        returnValue = libpanda._inP9ImMiC0F(self.this, connection.this)
        return returnValue

    
    def upcastToQueuedReturnPointerToConnection(self):
        returnValue = libpanda._inP9ImMv2GO(self.this)
        import QueuedReturnPointerToConnection
        returnObject = QueuedReturnPointerToConnection.QueuedReturnPointerToConnection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _QueuedConnectionManager__overloaded_openUDPConnection_ptrConnectionManager_int(self, port):
        upcastSelf = self
        returnValue = libpanda._inP9ImMtiqs(upcastSelf.this, port)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QueuedConnectionManager__overloaded_openUDPConnection_ptrConnectionManager(self):
        upcastSelf = self
        returnValue = libpanda._inP9ImMMLgh(upcastSelf.this)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def openTCPServerRendezvous(self, port, backlog):
        upcastSelf = self
        returnValue = libpanda._inP9ImMhDIi(upcastSelf.this, port, backlog)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QueuedConnectionManager__overloaded_openTCPClientConnection_ptrConnectionManager_ptrConstNetAddress_int(self, address, timeoutMs):
        upcastSelf = self
        returnValue = libpanda._inP9ImMDKvU(upcastSelf.this, address.this, timeoutMs)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QueuedConnectionManager__overloaded_openTCPClientConnection_ptrConnectionManager_atomicstring_int_int(self, hostname, port, timeoutMs):
        upcastSelf = self
        returnValue = libpanda._inP9ImMnsPM(upcastSelf.this, hostname, port, timeoutMs)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def closeConnection(self, connection):
        upcastSelf = self
        returnValue = libpanda._inP9ImMigqc(upcastSelf.this, connection.this)
        return returnValue

    
    def openUDPConnection(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._QueuedConnectionManager__overloaded_openUDPConnection_ptrConnectionManager()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._QueuedConnectionManager__overloaded_openUDPConnection_ptrConnectionManager_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def openTCPClientConnection(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import NetAddress
            if isinstance(_args[0], NetAddress.NetAddress):
                if isinstance(_args[1], types.IntType):
                    return self._QueuedConnectionManager__overloaded_openTCPClientConnection_ptrConnectionManager_ptrConstNetAddress_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NetAddress.NetAddress> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._QueuedConnectionManager__overloaded_openTCPClientConnection_ptrConnectionManager_atomicstring_int_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setMaxQueueSize(self, maxSize):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToQueuedReturnPointerToConnection()
        returnValue = libpanda._inP9ImMBHvr(upcastSelf.this, maxSize)
        return returnValue

    
    def getMaxQueueSize(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToQueuedReturnPointerToConnection()
        returnValue = libpanda._inP9ImMCaPK(upcastSelf.this)
        return returnValue

    
    def getCurrentQueueSize(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToQueuedReturnPointerToConnection()
        returnValue = libpanda._inP9ImMswOz(upcastSelf.this)
        return returnValue


