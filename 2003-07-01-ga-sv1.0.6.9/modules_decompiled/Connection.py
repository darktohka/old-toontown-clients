# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount

class Connection(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, manager, socket):
        self.this = libpanda._inP9ImMQ8ix(manager.this, socket.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inP9ImMQPhL:
            libpanda._inP9ImMQPhL(self.this)
        

    
    def getAddress(self):
        returnValue = libpanda._inP9ImMF__C(self.this)
        import NetAddress
        returnObject = NetAddress.NetAddress(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getManager(self):
        returnValue = libpanda._inP9ImM2GOO(self.this)
        import ConnectionManager
        returnObject = ConnectionManager.ConnectionManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getSocket(self):
        returnValue = libpanda._inP9ImM8tyZ(self.this)
        import PRFileDesc
        returnObject = PRFileDesc.PRFileDesc(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setCollectTcp(self, collectTcp):
        returnValue = libpanda._inP9ImMLoGo(self.this, collectTcp)
        return returnValue

    
    def getCollectTcp(self):
        returnValue = libpanda._inP9ImMQIEw(self.this)
        return returnValue

    
    def setCollectTcpInterval(self, interval):
        returnValue = libpanda._inP9ImMn8H_(self.this, interval)
        return returnValue

    
    def getCollectTcpInterval(self):
        returnValue = libpanda._inP9ImMou1t(self.this)
        return returnValue

    
    def considerFlush(self):
        returnValue = libpanda._inP9ImMyeve(self.this)
        return returnValue

    
    def flush(self):
        returnValue = libpanda._inP9ImMvSru(self.this)
        return returnValue

    
    def setNonblock(self, flag):
        returnValue = libpanda._inP9ImM7OUw(self.this, flag)
        return returnValue

    
    def setLinger(self, flag, time):
        returnValue = libpanda._inP9ImMyOTH(self.this, flag, time)
        return returnValue

    
    def setReuseAddr(self, flag):
        returnValue = libpanda._inP9ImM87ZK(self.this, flag)
        return returnValue

    
    def setKeepAlive(self, flag):
        returnValue = libpanda._inP9ImMbmIV(self.this, flag)
        return returnValue

    
    def setRecvBufferSize(self, size):
        returnValue = libpanda._inP9ImM4Glj(self.this, size)
        return returnValue

    
    def setSendBufferSize(self, size):
        returnValue = libpanda._inP9ImMSxS1(self.this, size)
        return returnValue

    
    def setIpTimeToLive(self, ttl):
        returnValue = libpanda._inP9ImMQkWX(self.this, ttl)
        return returnValue

    
    def setIpTypeOfService(self, tos):
        returnValue = libpanda._inP9ImMCpUD(self.this, tos)
        return returnValue

    
    def setNoDelay(self, flag):
        returnValue = libpanda._inP9ImMf5D7(self.this, flag)
        return returnValue

    
    def setMaxSegment(self, size):
        returnValue = libpanda._inP9ImMcSC_(self.this, size)
        return returnValue


