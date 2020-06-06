# File: C (Python 2.2)

import DirectNotifyGlobal
import Datagram
from MsgTypes import *
moduleGlobals = globals()
moduleLocals = locals()

class ClientDistUpdate:
    notify = DirectNotifyGlobal.directNotify.newCategory('ClientDistUpdate')
    
    def __init__(self, cdc, dcField):
        self.cdc = cdc
        self.field = dcField
        self.number = dcField.getNumber()
        self.name = dcField.getName()
        self.types = []
        self.divisors = []
        self.deriveTypesFromParticle(dcField)
        exec ('import ' + cdc.name, moduleGlobals, moduleLocals)
        
        try:
            self.func = eval(cdc.name + '.' + cdc.name + '.' + self.name)
        except (NameError, AttributeError):
            e = None
            self.func = None

        return None

    
    def deriveTypesFromParticle(self, dcField):
        dcFieldAtomic = dcField.asAtomicField()
        dcFieldMolecular = dcField.asMolecularField()
        if dcFieldAtomic:
            for i in range(0, dcFieldAtomic.getNumElements()):
                self.types.append(dcFieldAtomic.getElementType(i))
                self.divisors.append(dcFieldAtomic.getElementDivisor(i))
            
        elif dcFieldMolecular:
            for i in range(0, dcFieldMolecular.getNumAtomics()):
                componentField = dcFieldMolecular.getAtomic(i)
                for j in range(0, componentField.getNumElements()):
                    self.types.append(componentField.getElementType(j))
                    self.divisors.append(componentField.getElementDivisor(j))
                
            
        else:
            ClientDistUpdate.notify.error('field is neither atom nor molecule')
        return None

    
    def updateField(self, cdc, do, di):
        args = self.extractArgs(di)
        if self.func != None:
            apply(self.func, [
                do] + args)
        
        return None

    
    def extractArgs(self, di):
        args = []
        numTypes = len(self.types)
        for i in range(numTypes):
            args.append(di.getArg(self.types[i], self.divisors[i]))
        
        return args

    
    def addArgs(self, datagram, args):
        numElems = len(args)
        for i in range(0, numElems):
            datagram.putArg(args[i], self.types[i], self.divisors[i])
        

    
    def sendUpdate(self, cr, do, args, sendToId = None):
        if sendToId == None:
            sendToId = do.doId
        
        datagram = Datagram.Datagram()
        datagram.addUint16(CLIENT_OBJECT_UPDATE_FIELD)
        datagram.addUint32(sendToId)
        datagram.addUint16(self.number)
        self.addArgs(datagram, args)
        cr.send(datagram)


