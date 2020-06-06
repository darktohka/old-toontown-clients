# File: C (Python 2.2)

from PandaModules import *
import DirectNotifyGlobal
import ClientDistUpdate

class ClientDistClass:
    
    def __init__(self, dcClass):
        self.number = dcClass.getNumber()
        self.name = dcClass.getName()
        self.allFields = self.parseFields(dcClass)
        self.allCDU = self.createAllCDU(self.allFields)
        self.number2CDU = self.createNumber2CDUDict(self.allCDU)
        self.name2CDU = self.createName2CDUDict(self.allCDU)
        self.broadcastRequiredCDU = self.listBroadcastRequiredCDU(self.allCDU)
        self.allRequiredCDU = self.listRequiredCDU(self.allCDU)
        exec 'import ' + self.name
        self.constructor = eval(self.name + '.' + self.name)
        return None

    
    def parseFields(self, dcClass):
        fields = []
        for i in range(0, dcClass.getNumInheritedFields()):
            fields.append(dcClass.getInheritedField(i))
        
        return fields

    
    def createAllCDU(self, allFields):
        allCDU = []
        for i in allFields:
            allCDU.append(ClientDistUpdate.ClientDistUpdate(self, i))
        
        return allCDU

    
    def createNumber2CDUDict(self, allCDU):
        dict = { }
        for i in allCDU:
            dict[i.number] = i
        
        return dict

    
    def createName2CDUDict(self, allCDU):
        dict = { }
        for i in allCDU:
            dict[i.name] = i
        
        return dict

    
    def listBroadcastRequiredCDU(self, allCDU):
        requiredCDU = []
        for i in allCDU:
            atom = i.field.asAtomicField()
            if atom:
                if atom.isRequired() and atom.isBroadcast():
                    requiredCDU.append(i)
                
            
        
        return requiredCDU

    
    def listRequiredCDU(self, allCDU):
        requiredCDU = []
        for i in allCDU:
            atom = i.field.asAtomicField()
            if atom:
                if atom.isRequired():
                    requiredCDU.append(i)
                
            
        
        return requiredCDU

    
    def updateField(self, do, di):
        fieldId = di.getArg(STUint16)
        cdu = self.number2CDU[fieldId]
        cdu.updateField(self, do, di)
        return None

    
    def sendUpdate(self, cr, do, fieldName, args, sendToId = None):
        cdu = self.name2CDU[fieldName]
        cdu.sendUpdate(cr, do, args, sendToId)


