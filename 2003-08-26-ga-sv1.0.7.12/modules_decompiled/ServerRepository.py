# File: S (Python 2.2)

from PandaModules import *
from TaskManagerGlobal import *
from MsgTypes import *
import Task
import DirectNotifyGlobal

class ServerRepository:
    
    def __init__(self, tcpPort, udpPort):
        self.qcm = QueuedConnectionManager()
        self.qcl = QueuedConnectionListener(self.qcm, 0)
        self.qcr = QueuedConnectionReader(self.qcm, 0)
        self.cw = ConnectionWriter(self.qcm, 0)
        self.tcpRendezvous = self.qcm.openTCPServerRendezvous(tcpPort, 10)
        print self.tcpRendezvous
        self.qcl.addConnection(self.tcpRendezvous)
        self.startListenerPollTask()
        self.startReaderPollTask()
        self.startResetPollTask()
        return None

    
    def startListenerPollTask(self):
        taskMgr.add(self.listenerPoll, 'serverListenerPollTask')
        return None

    
    def listenerPoll(self, task):
        if self.qcl.newConnectionAvailable():
            print 'New connection is available'
            rendezvous = PointerToConnection()
            netAddress = NetAddress()
            newConnection = PointerToConnection()
            retVal = self.qcl.getNewConnection(rendezvous, netAddress, newConnection)
            if retVal:
                newConnection = newConnection.p()
                self.qcr.addConnection(newConnection)
                print 'Got a connection!'
                self.lastConnection = newConnection
            else:
                ServerRepository.notify.warning('getNewConnection returned false')
        
        return Task.cont

    
    def startReaderPollTask(self):
        taskMgr.add(self.readerPollUntilEmpty, 'serverReaderPollTask')
        return None

    
    def readerPollUntilEmpty(self, task):
        while self.readerPollOnce():
            pass
        return Task.cont

    
    def readerPollOnce(self):
        availGetVal = self.qcr.dataAvailable()
        if availGetVal:
            datagram = NetDatagram()
            readRetVal = self.qcr.getData(datagram)
            if readRetVal:
                self.handleDatagram(datagram)
            else:
                ClientRepository.notify.warning('getData returned false')
        
        return availGetVal

    
    def handleDatagram(self, datagram):
        print 'Server got a datagram!'
        dgi = DatagramIterator(datagram)
        print dgi.getUint16()
        print dgi.getString()
        print dgi.getUint32()
        print dgi.getUint16()
        newDatagram = Datagram()
        newDatagram.addUint16(LOGIN_RESPONSE)
        newDatagram.addUint8(ord('s'))
        self.cw.send(newDatagram, self.lastConnection)
        return None

    
    def sendAvatarGenerate(self):
        datagram = Datagram()
        datagram.addUint16(ALL_OBJECT_GENERATE_WITH_REQUIRED)
        datagram.addUint8(2)
        datagram.addUint32(10)
        datagram.addUint32(999)
        self.cw.send(datagram, self.lastConnection)

    
    def startResetPollTask(self):
        return None

    
    def resetPollUntilEmpty(self):
        return None

    
    def resetPollOnce(self):
        return None


