# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class ConnectionWriter(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, manager, numThreads):
        self.this = libpanda._inP9ImMPv9q(manager.this, numThreads)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inP9ImMseTQ:
            libpanda._inP9ImMseTQ(self.this)
        

    
    def _ConnectionWriter__overloaded_send_ptrConnectionWriter_ptrConstDatagram_ptrConnection(self, datagram, connection):
        returnValue = libpanda._inP9ImM5_fV(self.this, datagram.this, connection.this)
        return returnValue

    
    def _ConnectionWriter__overloaded_send_ptrConnectionWriter_ptrConstDatagram_ptrConnection_ptrConstNetAddress(self, datagram, connection, address):
        returnValue = libpanda._inP9ImM6Lcw(self.this, datagram.this, connection.this, address.this)
        return returnValue

    
    def isValidForUdp(self, datagram):
        returnValue = libpanda._inP9ImMysIn(self.this, datagram.this)
        return returnValue

    
    def getManager(self):
        returnValue = libpanda._inP9ImMTVbQ(self.this)
        import ConnectionManager
        returnObject = ConnectionManager.ConnectionManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isImmediate(self):
        returnValue = libpanda._inP9ImML_Gm(self.this)
        return returnValue

    
    def getNumThreads(self):
        returnValue = libpanda._inP9ImMm3eX(self.this)
        return returnValue

    
    def setRawMode(self, mode):
        returnValue = libpanda._inP9ImM7nth(self.this, mode)
        return returnValue

    
    def getRawMode(self):
        returnValue = libpanda._inP9ImM7jjm(self.this)
        return returnValue

    
    def send(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import Datagram
            if isinstance(_args[0], Datagram.Datagram):
                import Connection
                if isinstance(_args[1], Connection.Connection):
                    return self._ConnectionWriter__overloaded_send_ptrConnectionWriter_ptrConstDatagram_ptrConnection(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Connection.Connection> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> '
        elif numArgs == 3:
            import Datagram
            if isinstance(_args[0], Datagram.Datagram):
                import Connection
                if isinstance(_args[1], Connection.Connection):
                    import NetAddress
                    if isinstance(_args[2], NetAddress.NetAddress):
                        return self._ConnectionWriter__overloaded_send_ptrConnectionWriter_ptrConstDatagram_ptrConnection_ptrConstNetAddress(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <NetAddress.NetAddress> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Connection.Connection> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


