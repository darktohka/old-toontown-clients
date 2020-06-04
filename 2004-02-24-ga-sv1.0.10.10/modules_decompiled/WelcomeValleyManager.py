# File: W (Python 2.2)

from PandaModules import *
import DistributedObject
import DirectNotifyGlobal
import ToontownGlobals
import PythonUtil

class WelcomeValleyManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('WelcomeValleyManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def generate(self):
        if toonbase.tcr.welcomeValleyManager != None:
            toonbase.tcr.welcomeValleyManager.delete()
        
        toonbase.tcr.welcomeValleyManager = self
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        self.ignore(ToontownGlobals.SynchronizeHotkey)
        toonbase.tcr.welcomeValleyManager = None
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        self.ignore(ToontownGlobals.SynchronizeHotkey)
        toonbase.tcr.welcomeValleyManager = None
        DistributedObject.DistributedObject.delete(self)

    
    def d_clientSetZone(self, zoneId):
        self.sendUpdate('clientSetZone', [
            zoneId])

    
    def requestZoneId(self, origZoneId, callback):
        context = self.getCallbackContext(callback)
        self.sendUpdate('requestZoneIdMessage', [
            origZoneId,
            context])

    
    def requestZoneIdResponse(self, zoneId, context):
        self.doCallbackContext(context, [
            zoneId])


