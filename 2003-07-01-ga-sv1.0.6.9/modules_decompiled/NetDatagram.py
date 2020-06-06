# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Datagram

class NetDatagram(Datagram.Datagram, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _NetDatagram__overloaded_constructor(self):
        self.this = libpanda._inP9ImMElXx()
        self.userManagesMemory = 1

    
    def _NetDatagram__overloaded_constructor_ptrConstDatagram(self, copy):
        self.this = libpanda._inP9ImMrT0b(copy.this)
        self.userManagesMemory = 1

    
    def _NetDatagram__overloaded_constructor_ptrConstNetDatagram(self, copy):
        self.this = libpanda._inP9ImMVk0H(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inP9ImMJirl:
            libpanda._inP9ImMJirl(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inP9ImMss1L()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _NetDatagram__overloaded_assign_ptrNetDatagram_ptrConstDatagram(self, copy):
        returnValue = libpanda._inP9ImMVtlI(self.this, copy.this)
        returnObject = NetDatagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def _NetDatagram__overloaded_assign_ptrNetDatagram_ptrConstNetDatagram(self, copy):
        returnValue = libpanda._inP9ImMkg9z(self.this, copy.this)
        returnObject = NetDatagram(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def setConnection(self, connection):
        returnValue = libpanda._inP9ImM_JK9(self.this, connection.this)
        return returnValue

    
    def getConnection(self):
        returnValue = libpanda._inP9ImMXxCi(self.this)
        import Connection
        returnObject = Connection.Connection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setAddress(self, address):
        returnValue = libpanda._inP9ImMeaZL(self.this, address.this)
        return returnValue

    
    def getAddress(self):
        returnValue = libpanda._inP9ImMDIhL(self.this)
        import NetAddress
        returnObject = NetAddress.NetAddress(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NetDatagram__overloaded_constructor()
        elif numArgs == 1:
            import Datagram
            if isinstance(_args[0], Datagram.Datagram):
                return self._NetDatagram__overloaded_constructor_ptrConstDatagram(_args[0])
            elif isinstance(_args[0], NetDatagram):
                return self._NetDatagram__overloaded_constructor_ptrConstNetDatagram(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> <NetDatagram> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Datagram
            if isinstance(_args[0], Datagram.Datagram):
                return self._NetDatagram__overloaded_assign_ptrNetDatagram_ptrConstDatagram(_args[0])
            elif isinstance(_args[0], NetDatagram):
                return self._NetDatagram__overloaded_assign_ptrNetDatagram_ptrConstNetDatagram(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> <NetDatagram> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


