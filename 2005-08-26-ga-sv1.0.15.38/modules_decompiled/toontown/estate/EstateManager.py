# File: E (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase import ToontownGlobals
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
import whrandom
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
import HouseGlobals

class EstateManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('EstateManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.availableZones = 0
        self.popupInfo = None

    
    def disable(self):
        self.notify.debug("i'm disabling EstateManager rightnow.")
        self.ignore('getLocalEstateZone')
        self.ignoreAll()
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        DistributedObject.DistributedObject.disable(self)

    
    def allocateMyEstateZone(self):
        self.getLocalEstateZone(base.localAvatar.getDoId())

    
    def getLocalEstateZone(self, avId):
        name = ''
        if base.localAvatar.doId == avId:
            name = base.cr.userName
        
        self.sendUpdate('getEstateZone', [
            avId,
            name])

    
    def setEstateZone(self, ownerId, zoneId):
        self.notify.debug('setEstateZone(%s, %s)' % (ownerId, zoneId))
        messenger.send('setLocalEstateZone', [
            ownerId,
            zoneId])

    
    def generate(self):
        self.notify.debug('BASE: generate')
        DistributedObject.DistributedObject.generate(self)
        base.cr.estateMgr = self
        self.accept('getLocalEstateZone', self.getLocalEstateZone)
        self.announceGenerateName = self.uniqueName('generate')

    
    def setAvHouseId(self, avId, houseIds):
        self.notify.debug('setAvHouseId %d' % base.localAvatar.doId)
        for av in base.cr.avList:
            if av.id == avId:
                houseId = houseIds[av.position]
                ownerAv = base.cr.doId2do.get(avId)
                if ownerAv:
                    ownerAv.b_setHouseId(houseId)
                
                return None
            
        

    
    def sendAvToPlayground(self, avId, retCode):
        self.notify.debug('sendAvToPlayground: %d' % avId)
        messenger.send('kickToPlayground', [
            retCode])

    
    def leaveEstate(self):
        if self.isDisabled():
            self.notify.warning('EstateManager disabled; unable to leave estate.')
            return None
        
        self.sendUpdate('exitEstate')

    
    def removeFriend(self, ownerId, avId):
        self.notify.debug('removeFriend ownerId = %s, avId = %s' % (ownerId, avId))
        self.sendUpdate('removeFriend', [
            ownerId,
            avId])


