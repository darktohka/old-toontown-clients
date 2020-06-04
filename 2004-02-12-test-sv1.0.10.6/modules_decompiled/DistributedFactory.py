# File: D (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from ClockDelta import *
from IntervalGlobal import *
import random
import DistributedLevel
import DirectNotifyGlobal
import FactoryBase
import FactoryEntityCreator
import FactorySpecs
import LevelSpec
import LevelConstants
import Localizer

class DistributedFactory(DistributedLevel.DistributedLevel, FactoryBase.FactoryBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFactory')
    
    def __init__(self, cr):
        DistributedLevel.DistributedLevel.__init__(self, cr)
        FactoryBase.FactoryBase.__init__(self)
        self.suitIds = []
        self.suits = []
        self.reserveSuits = []
        self.joiningReserves = []
        self.suitsInitialized = 0

    
    def createEntityCreator(self):
        return FactoryEntityCreator.FactoryEntityCreator(level = self)

    
    def generate(self):
        self.notify.debug('generate')
        DistributedLevel.DistributedLevel.generate(self)

    
    def delete(self):
        DistributedLevel.DistributedLevel.delete(self)

    
    def setFactoryId(self, id):
        FactoryBase.FactoryBase.setFactoryId(self, id)

    
    def setForemanConfronted(self, avId):
        if avId == toonbase.localToon.doId:
            return None
        
        av = toonbase.tcr.identifyFriend(avId)
        if av is None:
            return None
        
        toonbase.localToon.setSystemMessage(avId, Localizer.ForemanConfrontedMsg % av.getName())

    
    def setDefeated(self):
        self.notify.info('setDefeated')
        messenger.send('FactoryWinEvent')

    
    def levelAnnounceGenerate(self):
        self.notify.debug('levelAnnounceGenerate')
        DistributedLevel.DistributedLevel.levelAnnounceGenerate(self)
        specModule = FactorySpecs.getFactorySpecModule(self.factoryId)
        factorySpec = LevelSpec.LevelSpec(specModule)
        if __dev__:
            typeReg = self.getFactoryEntityTypeReg()
            factorySpec.setEntityTypeReg(typeReg)
        
        DistributedLevel.DistributedLevel.initializeLevel(self, factorySpec)

    
    def privGotSpec(self, levelSpec):
        if __dev__:
            if not levelSpec.hasEntityTypeReg():
                typeReg = self.getFactoryEntityTypeReg()
                levelSpec.setEntityTypeReg(typeReg)
            
        
        firstSetZoneDoneEvent = self.cr.getNextSetZoneDoneEvent()
        
        def handleFirstSetZoneDone():
            print 'handleFirstSetZoneDone'
            toonbase.factoryReady = 1
            messenger.send('FactoryReady')

        self.acceptOnce(firstSetZoneDoneEvent, handleFirstSetZoneDone)
        modelCount = len(levelSpec.getAllEntIds())
        loader.beginBulkLoad('factory', Localizer.HeadingToFactoryTitle % Localizer.FactoryNames[self.factoryId], modelCount, 1, Localizer.TIP_COGHQ)
        DistributedLevel.DistributedLevel.privGotSpec(self, levelSpec)
        loader.endBulkLoad('factory')
        
        def printPos(self = self):
            pos = toonbase.localToon.getPos(self.getZoneNode(self.lastToonZone))
            h = toonbase.localToon.getH(self.getZoneNode(self.lastToonZone))
            print 'factory pos: %s, h: %s, zone %s' % (repr(pos), h, self.lastToonZone)
            posStr = 'X: %.3f' % pos[0] + '\nY: %.3f' % pos[1] + '\nZ: %.3f' % pos[2] + '\nH: %.3f' % h + '\nZone: %s' % str(self.lastToonZone)
            toonbase.localToon.setChat(posStr, CFThought)

        self.accept('f2', printPos)
        toonbase.localToon.setCameraCollisionsCanMove(1)
        self.acceptOnce('leavingFactory', self.announceLeaving)

    
    def disable(self):
        self.notify.debug('disable')
        toonbase.localToon.setCameraCollisionsCanMove(0)
        if hasattr(self, 'suits'):
            del self.suits
        
        if hasattr(self, 'relatedObjectMgrRequest') and self.relatedObjectMgrRequest:
            self.cr.relatedObjectMgr.abortRequest(self.relatedObjectMgrRequest)
            del self.relatedObjectMgrRequest
        
        DistributedLevel.DistributedLevel.disable(self)

    
    def setSuits(self, suitIds, reserveSuitIds):
        oldSuitIds = list(self.suitIds)
        self.suitIds = suitIds
        self.reserveSuitIds = reserveSuitIds
        newSuitIds = []
        for suitId in self.suitIds:
            if suitId not in oldSuitIds:
                newSuitIds.append(suitId)
            
        
        if len(newSuitIds):
            
            def bringOutOfReserve(suits):
                for suit in suits:
                    suit.comeOutOfReserve()
                

            self.relatedObjectMgrRequest = self.cr.relatedObjectMgr.requestObjects(newSuitIds, bringOutOfReserve)
        

    
    def reservesJoining(self):
        pass

    
    def getCogSpec(self, cogId):
        cogSpecModule = FactorySpecs.getCogSpecModule(self.factoryId)
        return cogSpecModule.CogData[cogId]

    
    def getReserveCogSpec(self, cogId):
        cogSpecModule = FactorySpecs.getCogSpecModule(self.factoryId)
        return cogSpecModule.ReserveCogData[cogId]

    
    def getBattleCellSpec(self, battleCellId):
        cogSpecModule = FactorySpecs.getCogSpecModule(self.factoryId)
        return cogSpecModule.BattleCells[battleCellId]


