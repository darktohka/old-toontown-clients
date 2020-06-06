# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class ConnectionManager(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inP9ImMf_YP()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inP9ImMMJmi:
            libpanda._inP9ImMMJmi(self.this)
        

    
    def getHostName():
        returnValue = libpanda._inP9ImMNjTl()
        return returnValue

    getHostName = staticmethod(getHostName)
    
    def _ConnectionManager__overloaded_openUDPConnection_ptrConnectionManager_int(self, port):
        returnValue = libpanda._inP9ImMtiqs(self.this, port)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _ConnectionManager__overloaded_openUDPConnection_ptrConnectionManager(self):
        returnValue = libpanda._inP9ImMMLgh(self.this)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def openTCPServerRendezvous(self, port, backlog):
        returnValue = libpanda._inP9ImMhDIi(self.this, port, backlog)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _ConnectionManager__overloaded_openTCPClientConnection_ptrConnectionManager_ptrConstNetAddress_int(self, address, timeoutMs):
        returnValue = libpanda._inP9ImMDKvU(self.this, address.this, timeoutMs)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _ConnectionManager__overloaded_openTCPClientConnection_ptrConnectionManager_atomicstring_int_int(self, hostname, port, timeoutMs):
        returnValue = libpanda._inP9ImMnsPM(self.this, hostname, port, timeoutMs)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def closeConnection(self, connection):
        returnValue = libpanda._inP9ImMigqc(self.this, connection.this)
        return returnValue

    
    def openUDPConnection(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ConnectionManager__overloaded_openUDPConnection_ptrConnectionManager()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._ConnectionManager__overloaded_openUDPConnection_ptrConnectionManager_int(_args[0])
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
                    return self._ConnectionManager__overloaded_openTCPClientConnection_ptrConnectionManager_ptrConstNetAddress_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NetAddress.NetAddress> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._ConnectionManager__overloaded_openTCPClientConnection_ptrConnectionManager_atomicstring_int_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


