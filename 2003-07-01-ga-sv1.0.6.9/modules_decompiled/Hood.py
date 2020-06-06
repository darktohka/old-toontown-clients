# File: H (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from ToontownGlobals import *
from ToontownMsgTypes import *
import DirectNotifyGlobal
import StateData
import FSM
import State
import Task
import Purchase
import OnscreenText
import DistributedAvatar
import SuitInterior
import QuietZoneState
import ZoneUtil
import Localizer

class Hood(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('Hood')
    
    def __init__(self, parentFSM, doneEvent, dnaStore):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = FSM.FSM('Hood', [
            State.State('start', self.enterStart, self.exitStart, [
                'townLoader',
                'safeZoneLoader']),
            State.State('townLoader', self.enterTownLoader, self.exitTownLoader, [
                'quietZone',
                'safeZoneLoader',
                'suitInterior']),
            State.State('shop', self.enterShop, self.exitShop, [
                'safeZoneLoader']),
            State.State('safeZoneLoader', self.enterSafeZoneLoader, self.exitSafeZoneLoader, [
                'quietZone',
                'suitInterior',
                'townLoader',
                'shop',
                'minigame']),
            State.State('purchase', self.enterPurchase, self.exitPurchase, [
                'quietZone',
                'minigame',
                'safeZoneLoader']),
            State.State('suitInterior', self.enterSuitInterior, self.exitSuitInterior, [
                'quietZone',
                'townLoader',
                'safeZoneLoader']),
            State.State('minigame', self.enterMinigame, self.exitMinigame, [
                'purchase']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'safeZoneLoader',
                'townLoader',
                'suitInterior',
                'minigame']),
            State.State('final', self.enterFinal, self.exitFinal, [])], 'start', 'final')
        self.fsm.enterInitialState()
        self.parentFSM = parentFSM
        self.dnaStore = dnaStore
        self.loaderDoneEvent = 'loaderDone'
        self.suitInteriorDoneEvent = 'suitInteriorDone'
        self.minigameDoneEvent = 'minigameDone'
        self.id = None
        self.titleText = None
        self.titleColor = (1, 1, 1, 1)

    
    def enter(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        if self.id != Tutorial:
            streetName = StreetNames[ZoneUtil.getBranchZone(zoneId)][1]
            hoodText = toonbase.tcr.hoodMgr.getFullnameFromId(self.id) + '\n' + streetName
        else:
            hoodText = toonbase.tcr.hoodMgr.getFullnameFromId(self.id)
        self.titleText = OnscreenText.OnscreenText(hoodText, fg = self.titleColor, font = getSignFont(), pos = (0, -0.5), scale = 0.16, drawOrder = 0, mayChange = 1)
        self.fsm.request(requestStatus['loader'], [
            requestStatus])

    
    def spawnTitleText(self, zoneId):
        if self.id != Tutorial:
            streetName = StreetNames[ZoneUtil.getBranchZone(zoneId)][1]
            hoodText = toonbase.tcr.hoodMgr.getFullnameFromId(self.id) + '\n' + streetName
        else:
            hoodText = toonbase.tcr.hoodMgr.getFullnameFromId(self.id)
        self.titleText.setText(hoodText)
        self.titleText.show()
        self.titleText.setColor(Vec4(*self.titleColor))
        self.titleText.setFg(self.titleColor)
        seq = Task.sequence(Task.pause(0.10000000000000001), Task.pause(6.0), self.titleText.lerpColor(Vec4(self.titleColor[0], self.titleColor[1], self.titleColor[2], self.titleColor[3]), Vec4(self.titleColor[0], self.titleColor[1], self.titleColor[2], 0.0), 0.5), Task.Task(self.hideTitleTextTask))
        taskMgr.add(seq, 'titleText')

    
    def hideTitleTextTask(self, task):
        self.titleText.hide()
        return Task.done

    
    def hideTitleText(self):
        if self.titleText:
            self.titleText.hide()
        

    
    def exit(self):
        taskMgr.remove('titleText')
        if self.titleText:
            self.titleText.cleanup()
            self.titleText = None
        
        toonbase.localToon.stopChat()

    
    def load(self):
        if self.storageDNAFile:
            loader.loadDNAFile(self.dnaStore, self.storageDNAFile)
        
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setScale(1.0)
        self.sky.setFogOff()

    
    def unload(self):
        toonbase.tcr.disableAll()
        del self.fsm
        del self.parentFSM
        del self.safeZoneLoaderClass
        del self.townLoaderClass
        self.dnaStore.resetHood()
        del self.dnaStore
        self.sky.removeNode()
        del self.sky
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def isSameHood(self, status):
        if status['hoodId'] == self.id:
            pass
        return status['shardId'] == None

    
    def enterSafeZoneLoader(self, requestStatus):
        self.accept(self.loaderDoneEvent, self.handleSafeZoneLoaderDone)
        self.loader.enter(requestStatus)
        self.spawnTitleText(requestStatus['zoneId'])

    
    def exitSafeZoneLoader(self):
        taskMgr.remove('titleText')
        self.hideTitleText()
        self.ignore(self.loaderDoneEvent)
        self.loader.exit()
        self.loader.unload()
        del self.loader

    
    def handleSafeZoneLoaderDone(self):
        doneStatus = self.loader.getDoneStatus()
        print 'safeZoneLoaderDone, status = %s' % doneStatus
        if self.isSameHood(doneStatus) or doneStatus['loader'] == 'minigame':
            self.fsm.request('quietZone', [
                doneStatus])
        else:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)

    
    def enterTownLoader(self, requestStatus):
        self.accept(self.loaderDoneEvent, self.handleTownLoaderDone)
        self.loader.enter(requestStatus)
        self.spawnTitleText(requestStatus['zoneId'])

    
    def exitTownLoader(self):
        taskMgr.remove('titleText')
        self.hideTitleText()
        self.ignore(self.loaderDoneEvent)
        self.loader.exit()
        self.loader.unload()
        del self.loader

    
    def handleTownLoaderDone(self):
        doneStatus = self.loader.getDoneStatus()
        if self.isSameHood(doneStatus):
            self.fsm.request('quietZone', [
                doneStatus])
        else:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)

    
    def enterShop(self):
        pass

    
    def exitShop(self):
        pass

    
    def handleShopEntry(self):
        self.fsm.request('shop')

    
    def enterPurchase(self, pointsAwarded, playerMoney, playerIds, playerStates, remain):
        messenger.send('enterSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 0
        toonbase.localToon.laffMeter.start()
        self.purchaseDoneEvent = 'purchaseDone'
        self.accept(self.purchaseDoneEvent, self.handlePurchaseDone)
        self.purchase = Purchase.Purchase(toonbase.localToon, pointsAwarded, playerMoney, playerIds, playerStates, remain, self.purchaseDoneEvent)
        self.purchase.load()
        self.purchase.enter()

    
    def exitPurchase(self):
        messenger.send('exitSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 1
        toonbase.localToon.laffMeter.stop()
        self.ignore(self.purchaseDoneEvent)
        self.purchase.exit()
        self.purchase.unload()
        del self.purchase

    
    def handlePurchaseDone(self):
        doneStatus = self.purchase.getDoneStatus()
        if doneStatus['where'] == 'playground':
            if self.id == Tutorial:
                newDoneStatus = {
                    'loader': 'safeZoneLoader',
                    'where': 'playground',
                    'how': 'teleportIn',
                    'hoodId': ToontownCentral,
                    'zoneId': ToontownCentral,
                    'shardId': None,
                    'avId': -1 }
                self.doneStatus = newDoneStatus
                messenger.send(self.doneEvent)
            else:
                self.fsm.request('quietZone', [
                    {
                        'loader': 'safeZoneLoader',
                        'where': 'playground',
                        'how': 'teleportIn',
                        'hoodId': self.id,
                        'zoneId': self.id,
                        'shardId': None,
                        'avId': -1 }])
        elif doneStatus['loader'] == 'minigame':
            self.fsm.request('minigame')
        else:
            self.notify.error('handlePurchaseDone: unknown mode')

    
    def enterSuitInterior(self, requestStatus = None):
        self.placeDoneEvent = 'suit-interior-done'
        self.acceptOnce(self.placeDoneEvent, self.handleSuitInteriorDone)
        self.place = SuitInterior.SuitInterior(self, self.fsm, self.placeDoneEvent)
        self.place.load()
        self.place.enter(requestStatus)
        toonbase.tcr.playGame.setPlace(self.place)

    
    def exitSuitInterior(self):
        self.ignore(self.placeDoneEvent)
        del self.placeDoneEvent
        self.place.exit()
        self.place.unload()
        self.place = None
        toonbase.tcr.playGame.setPlace(self.place)

    
    def handleSuitInteriorDone(self):
        doneStatus = self.place.getDoneStatus()
        if self.isSameHood(doneStatus):
            self.fsm.request('quietZone', [
                doneStatus])
        else:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)

    
    def enterMinigame(self, ignoredParameter = None):
        messenger.send('enterSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 0
        toonbase.localToon.laffMeter.start()
        toonbase.tcr.forbidCheesyEffects(1)
        self.acceptOnce(self.minigameDoneEvent, self.handleMinigameDone)
        return None

    
    def exitMinigame(self):
        messenger.send('exitSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 1
        toonbase.localToon.laffMeter.stop()
        toonbase.tcr.forbidCheesyEffects(0)
        self.ignore(self.minigameDoneEvent)
        minigameState = self.fsm.getStateNamed('minigame')
        for childFSM in minigameState.getChildren():
            minigameState.removeChild(childFSM)
        

    
    def handleMinigameDone(self):
        return None

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def enterQuietZone(self, requestStatus):
        self.quietZoneDoneEvent = 'quietZoneDone'
        self.acceptOnce(self.quietZoneDoneEvent, self.handleQuietZoneDone)
        self.acceptOnce('enterWaitForSetZoneResponse', self.handleWaitForSetZoneResponse)
        self.quietZoneStateData = QuietZoneState.QuietZoneState(self.quietZoneDoneEvent)
        self.quietZoneStateData.load()
        self.quietZoneStateData.enter(requestStatus)

    
    def exitQuietZone(self):
        self.ignore(self.quietZoneDoneEvent)
        del self.quietZoneDoneEvent
        self.quietZoneStateData.exit()
        self.quietZoneStateData.unload()
        self.quietZoneStateData = None

    
    def loadLoader(self, requestStatus):
        loaderName = requestStatus['loader']
        if loaderName == 'safeZoneLoader':
            self.loader = self.safeZoneLoaderClass(self, self.fsm.getStateNamed('safeZoneLoader'), self.loaderDoneEvent)
            self.loader.load()
        elif loaderName == 'townLoader':
            self.loader = self.townLoaderClass(self, self.fsm.getStateNamed('townLoader'), self.loaderDoneEvent)
            self.loader.load(requestStatus['zoneId'])
        

    
    def handleWaitForSetZoneResponse(self, requestStatus):
        loaderName = requestStatus['loader']
        if loaderName == 'safeZoneLoader':
            if not (loader.inBulkBlock):
                loader.beginBulkLoad('hood', Localizer.HeadingToPlayground, safeZoneCountMap[self.id])
            
            self.loadLoader(requestStatus)
            loader.endBulkLoad('hood')
        elif loaderName == 'townLoader':
            if not (loader.inBulkBlock):
                zoneId = requestStatus['zoneId']
                toPhrase = StreetNames[ZoneUtil.getBranchZone(zoneId)][0]
                streetName = StreetNames[ZoneUtil.getBranchZone(zoneId)][1]
                loader.beginBulkLoad('hood', Localizer.HeadingToStreet % (toPhrase, streetName), townCountMap[self.id])
            
            self.loadLoader(requestStatus)
            loader.endBulkLoad('hood')
        elif loaderName == 'minigame':
            pass
        

    
    def handleQuietZoneDone(self):
        status = toonbase.tcr.handlerArgs
        self.fsm.request(status['loader'], [
            status])

    
    def startSky(self):
        self.sky.reparentTo(camera)
        self.sky.setZ(0.0)
        self.sky.setHpr(0.0, 0.0, 0.0)
        ce = CompassEffect.make(NodePath(), CompassEffect.PRot | CompassEffect.PZ)
        self.sky.node().setEffect(ce)

    
    def stopSky(self):
        taskMgr.remove('skyTrack')
        self.sky.reparentTo(hidden)


