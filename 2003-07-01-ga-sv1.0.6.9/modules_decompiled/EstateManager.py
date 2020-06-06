# File: E (Python 2.2)

from ShowBaseGlobal import *
import ToontownGlobals
import DistributedObject
import DirectNotifyGlobal
import whrandom
from DirectGui import *
import Localizer
import HouseGlobals

class EstateManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('EstateManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.availableZones = 0
        self.popupInfo = None
        return None

    
    def disable(self):
        self.notify.debug("i'm disabling EstateManager rightnow.")
        self.ignore('getLocalEstateZone')
        self.ignoreAll()
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        return None

    
    def get_drop_point(self, drop_point_list):
        if self.dbg_drop_mode == 0:
            return whrandom.choice(drop_point_list)
        else:
            droppnt = self.current_drop_point % len(drop_point_list)
            self.current_drop_point = (self.current_drop_point + 1) % len(drop_point_list)
            return drop_point_list[droppnt]

    
    def allocateMyEstateZone(self):
        self.getLocalEstateZone(toonbase.localToon.getDoId())

    
    def getLocalEstateZone(self, avId):
        name = ''
        if toonbase.localToon.doId == avId:
            name = toonbase.tcr.userName
        
        self.sendUpdate('getEstateZone', [
            avId,
            name])

    
    def setEstateZone(self, ownerId, zoneId):
        messenger.send('setLocalEstateZone', [
            ownerId,
            zoneId])
        return None

    
    def generate(self):
        self.notify.debug('BASE: generate')
        DistributedObject.DistributedObject.generate(self)
        toonbase.tcr.estateMgr = self
        self.accept('getLocalEstateZone', self.getLocalEstateZone)
        self.announceGenerateName = self.uniqueName('generate')
        return None

    
    def setAvHouseId(self, avId, houseIds):
        self.notify.debug('setAvHouseId %d' % toonbase.localToon.doId)
        for av in toonbase.tcr.avList:
            if av.id == avId:
                houseId = houseIds[av.position]
                ownerAv = toonbase.tcr.doId2do.get(avId)
                if ownerAv:
                    ownerAv.b_setHouseId(houseId)
                
                return None
            
        

    
    def sendAvToPlayground(self, avId, retCode):
        self.notify.debug('sendAvToPlayground: %d' % avId)
        messenger.send('kickToPlayground', [
            retCode])

    
    def leaveEstate(self):
        self.sendUpdate('exitEstate')

    
    def removeFriend(self, ownerId, avId):
        self.notify.debug('removeFriend ownerId = %s, avId = %s' % (ownerId, avId))
        self.sendUpdate('removeFriend', [
            ownerId,
            avId])


