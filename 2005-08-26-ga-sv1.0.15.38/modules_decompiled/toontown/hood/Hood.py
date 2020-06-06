# File: H (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from toontown.distributed.ToontownMsgTypes import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from direct.task import Task
from toontown.minigame import Purchase
from direct.gui import OnscreenText
from otp.avatar import DistributedAvatar
from toontown.building import SuitInterior
import QuietZoneState
import ZoneUtil
from toontown.toonbase import TTLocalizer

class Hood(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('Hood')
    
    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        StateData.StateData.__init__(self, doneEvent)
        self.parentFSM = parentFSM
        self.dnaStore = dnaStore
        self.loaderDoneEvent = 'loaderDone'
        self.id = None
        self.hoodId = hoodId
        self.titleText = None
        self.titleColor = (1, 1, 1, 1)
        self.holidayStorageDNADict = { }

    
    def enter(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        hoodText = self.getHoodText(zoneId)
        self.titleText = OnscreenText.OnscreenText(hoodText, fg = self.titleColor, font = getSignFont(), pos = (0, -0.5), scale = 0.16, drawOrder = 0, mayChange = 1)
        self.fsm.request(requestStatus['loader'], [
            requestStatus])

    
    def getHoodText(self, zoneId):
        hoodText = base.cr.hoodMgr.getFullnameFromId(self.id)
        if self.id != Tutorial:
            streetName = StreetNames.get(ZoneUtil.getCanonicalBranchZone(zoneId))
            if streetName:
                hoodText = hoodText + '\n' + streetName[-1]
            
        
        return hoodText

    
    def spawnTitleText(self, zoneId):
        hoodText = self.getHoodText(zoneId)
        self.doSpawnTitleText(hoodText)

    
    def doSpawnTitleText(self, text):
        self.titleText.setText(text)
        self.titleText.show()
        self.titleText.setColor(Vec4(*self.titleColor))
        self.titleText.clearColorScale()
        self.titleText.setFg(self.titleColor)
        seq = Task.sequence(Task.pause(0.10000000000000001), Task.pause(6.0), self.titleText.lerpColorScale(Vec4(1.0, 1.0, 1.0, 1.0), Vec4(1.0, 1.0, 1.0, 0.0), 0.5), Task.Task(self.hideTitleTextTask))
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
        
        base.localAvatar.stopChat()

    
    def load(self):
        if self.storageDNAFile:
            loader.loadDNAFile(self.dnaStore, self.storageDNAFile)
        
        newsManager = base.cr.newsManager
        if newsManager:
            for storageFile in self.holidayStorageDNADict.get(newsManager.getDecorationHolidayId(), []):
                loader.loadDNAFile(self.dnaStore, storageFile)
            
        
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setScale(1.0)
        self.sky.setFogOff()

    
    def unload(self):
        if not wantOtpServer:
            base.cr.disableAll()
        
        if hasattr(self, 'loader'):
            self.notify.info('Aggressively cleaning up loader: %s' % self.loader)
            self.loader.exit()
            self.loader.unload()
            del self.loader
        
        del self.fsm
        del self.parentFSM
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
        print 'isSameHood, hoodId = %s, self.id = %s' % (status['hoodId'], self.id)
        if status['hoodId'] == self.hoodId:
            pass
        return status['shardId'] == None

    
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
        self.ignore('enterWaitForSetZoneResponse')
        del self.quietZoneDoneEvent
        self.quietZoneStateData.exit()
        self.quietZoneStateData.unload()
        self.quietZoneStateData = None

    
    def loadLoader(self, requestStatus):
        pass

    
    def handleWaitForSetZoneResponse(self, requestStatus):
        loaderName = requestStatus['loader']
        if loaderName == 'safeZoneLoader':
            if not (loader.inBulkBlock):
                loader.beginBulkLoad('hood', TTLocalizer.HeadingToPlayground, safeZoneCountMap[self.id], 1, TTLocalizer.TIP_GENERAL)
            
            self.loadLoader(requestStatus)
            loader.endBulkLoad('hood')
        elif loaderName == 'townLoader':
            if not (loader.inBulkBlock):
                zoneId = requestStatus['zoneId']
                toPhrase = StreetNames[ZoneUtil.getCanonicalBranchZone(zoneId)][0]
                streetName = StreetNames[ZoneUtil.getCanonicalBranchZone(zoneId)][-1]
                loader.beginBulkLoad('hood', TTLocalizer.HeadingToStreet % (toPhrase, streetName), townCountMap[self.id], 1, TTLocalizer.TIP_STREET)
            
            self.loadLoader(requestStatus)
            loader.endBulkLoad('hood')
        elif loaderName == 'minigame':
            pass
        elif loaderName == 'cogHQLoader':
            print 'should be loading HQ'
        

    
    def handleQuietZoneDone(self):
        status = base.cr.handlerArgs
        self.fsm.request(status['loader'], [
            status])

    
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
            print 'leaving the hood'
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)

    
    def startSky(self):
        self.sky.reparentTo(camera)
        self.sky.setZ(0.0)
        self.sky.setHpr(0.0, 0.0, 0.0)
        ce = CompassEffect.make(NodePath(), CompassEffect.PRot | CompassEffect.PZ)
        self.sky.node().setEffect(ce)

    
    def stopSky(self):
        taskMgr.remove('skyTrack')
        self.sky.reparentTo(hidden)


