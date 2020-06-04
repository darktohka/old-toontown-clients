# File: D (Python 2.2)

from ClockDelta import *
from PandaModules import *
from PythonUtil import Functor, sameElements, list2dict, uniqueElements
from IntervalGlobal import *
from ToontownMsgTypes import *
import ToontownGlobals
import DistributedObject
import Level
import LevelConstants
import DirectNotifyGlobal
import EntityCreator
import OnscreenText
import Task
import LevelUtil
import FactoryCameraViews
import random

class DistributedLevel(DistributedObject.DistributedObject, Level.Level):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLevel')
    WantVisibility = config.GetBool('level-visibility', 1)
    ColorZonesAllDOs = 0
    FloorCollPrefix = 'zoneFloor'
    OuchTaskName = 'ouchTask'
    VisChangeTaskName = 'visChange'
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        Level.Level.__init__(self)
        self.lastToonZone = None
        self.lastCamZone = 0
        self.titleColor = (1, 1, 1, 1)
        self.titleText = OnscreenText.OnscreenText('', fg = self.titleColor, shadow = (0, 0, 0, 1), font = ToontownGlobals.getSuitFont(), pos = (0, -0.5), scale = 0.16, drawOrder = 0, mayChange = 1)
        self.smallTitleText = OnscreenText.OnscreenText('', fg = self.titleColor, font = ToontownGlobals.getSuitFont(), pos = (0.65000000000000002, 0.90000000000000002), scale = 0.080000000000000002, drawOrder = 0, mayChange = 1, bg = (0.5, 0.5, 0.5, 0.5), align = TextNode.ARight)
        self.zonesEnteredList = []
        self.fColorZones = 0

    
    def generate(self):
        DistributedLevel.notify.debug('generate')
        DistributedObject.DistributedObject.generate(self)
        self.parent2pendingChildren = { }
        self.curSpec = None
        toonbase.tcr.timeManager.synchronize('DistributedLevel.generate')
        toonbase.localToon.chatMgr.chatInputSpeedChat.addFactoryMenu()
        self.factoryViews = FactoryCameraViews.FactoryCameraViews(self)

    
    def setLevelZoneId(self, zoneId):
        self.levelZone = zoneId

    
    def setPlayerIds(self, avIdList):
        self.avIdList = avIdList

    
    def setEntranceId(self, entranceId):
        self.entranceId = entranceId

    
    def getEntranceId(self):
        return self.entranceId

    
    def setZoneIds(self, zoneIds):
        DistributedLevel.notify.debug('setZoneIds: %s' % zoneIds)
        self.zoneIds = zoneIds

    
    def setStartTimestamp(self, timestamp):
        DistributedLevel.notify.debug('setStartTimestamp: %s' % timestamp)
        self.startTime = globalClockDelta.networkToLocalTime(timestamp, bits = 32)

    
    def setScenarioIndex(self, scenarioIndex):
        self.scenarioIndex = scenarioIndex
        self.privGotAllRequired()

    
    def privGotAllRequired(self):
        self.levelAnnounceGenerate()

    
    def levelAnnounceGenerate(self):
        pass

    
    def initializeLevel(self, levelSpec):
        if __dev__:
            self.candidateSpec = levelSpec
            self.sendUpdate('requestCurrentLevelSpec', [
                hash(levelSpec),
                levelSpec.entTypeReg.getHashStr()])
        else:
            self.privGotSpec(levelSpec)

    if __dev__:
        
        def reportModelSpecSyncError(self, msg):
            DistributedLevel.notify.error('%s\n\nyour spec does not match the level model\nuse SpecUtil.updateSpec, then restart your AI and client' % msg)

        
        def setSpecDeny(self, reason):
            DistributedLevel.notify.error(reason)

        
        def setSpecSenderDoId(self, doId):
            DistributedLevel.notify.debug('setSpecSenderDoId: %s' % doId)
            blobSender = toonbase.tcr.doId2do[doId]
            
            def setSpecBlob(specBlob, blobSender = blobSender, self = self):
                blobSender.sendAck()
                LevelSpec = LevelSpec
                import LevelSpec
                spec = eval(specBlob)
                if spec is None:
                    spec = self.candidateSpec
                
                del self.candidateSpec
                self.privGotSpec(spec)

            if blobSender.isComplete():
                setSpecBlob(blobSender.getBlob())
            else:
                evtName = self.uniqueName('specDone')
                blobSender.setDoneEvent(evtName)
                self.acceptOnce(evtName, setSpecBlob)

    
    
    def privGotSpec(self, levelSpec):
        Level.Level.initializeLevel(self, self.doId, levelSpec, self.scenarioIndex)
        modelZoneNums = self.zoneNums
        specZoneNums = self.zoneNum2zoneId.keys()
        if not sameElements(modelZoneNums, specZoneNums):
            self.reportModelSpecSyncError('model zone nums (%s) do not match spec zone nums (%s)' % (modelZoneNums, specZoneNums))
        
        self.initVisibility()
        self.placeLocalToon()

    
    def announceLeaving(self):
        DistributedLevel.notify.info('announceLeaving')
        self.doneBarrier()

    
    def placeLocalToon(self):
        if self.entranceId not in self.entranceId2entity:
            self.notify.warning('unknown entranceId %s' % self.entranceId)
            toonbase.localToon.setPos(0, 0, 0)
            self.notify.warning('showing all zones')
            self.setColorZones(1)
            zoneEntIds = self.entType2ids['zone']
            while 1:
                zoneEntId = random.choice(zoneEntIds)
                if zoneEntId is not LevelConstants.UberZoneEntId:
                    initialZoneEnt = self.getEntity(zoneEntId)
                    toonbase.localToon.setPos(render, initialZoneEnt.getZoneNode().getPos(render))
                    break
                
        else:
            epEnt = self.entranceId2entity[self.entranceId]
            epEnt.placeToon(toonbase.localToon, self.avIdList.index(toonbase.localToon.doId), len(self.avIdList))
            initialZoneEnt = self.getEntity(epEnt.getZoneEntId())
        self.enterZone(initialZoneEnt.entId)

    
    def createEntityCreator(self):
        return EntityCreator.EntityCreator(level = self)

    
    def onEntityTypePostCreate(self, entType):
        Level.Level.onEntityTypePostCreate(self, entType)
        if entType == 'levelMgr':
            self._DistributedLevel__handleLevelMgrCreated()
        

    
    def _DistributedLevel__handleLevelMgrCreated(self):
        levelMgr = self.getEntity(LevelConstants.LevelMgrEntId)
        self.geom = levelMgr.geom
        self.zoneNum2node = LevelUtil.getZoneNum2Node(self.geom)
        self.zoneNums = self.zoneNum2node.keys()
        self.zoneNums.sort()
        self.zoneNumDict = list2dict(self.zoneNums)
        DistributedLevel.notify.debug('zones from model: %s' % self.zoneNums)
        for (zoneNum, zoneNode) in self.zoneNum2node.items():
            if zoneNum == LevelConstants.UberZoneEntId:
                continue
            
            allColls = zoneNode.findAllMatches('**/+CollisionNode').asList()
            floorColls = []
            for coll in allColls:
                bitmask = coll.node().getIntoCollideMask()
                if not (bitmask & ToontownGlobals.FloorBitmask).isZero():
                    floorColls.append(coll)
                
            
            if len(floorColls) > 0:
                floorCollName = '%s%s' % (DistributedLevel.FloorCollPrefix, zoneNum)
                others = zoneNode.findAllMatches('**/%s' % floorCollName).asList()
                for other in others:
                    other.setName('%s_renamed' % floorCollName)
                
                for floorColl in floorColls:
                    floorColl.setName(floorCollName)
                
                
                def handleZoneEnter(collisionEntry, self = self, zoneNum = zoneNum):
                    self.toonEnterZone(zoneNum)
                    floorNode = collisionEntry.getIntoNode()
                    if floorNode.hasTag('ouch'):
                        ouchLevel = int(floorNode.getTag('ouch'))
                        self.startOuch(ouchLevel)
                    

                self.accept('enter%s' % floorCollName, handleZoneEnter)
                
                def handleZoneExit(collisionEntry, self = self, zoneNum = zoneNum):
                    floorNode = collisionEntry.getIntoNode()
                    if floorNode.hasTag('ouch'):
                        self.stopOuch()
                    

                self.accept('exit%s' % floorCollName, handleZoneExit)
            
        

    
    def announceGenerate(self):
        DistributedLevel.notify.debug('announceGenerate')
        DistributedObject.DistributedObject.announceGenerate(self)

    
    def disable(self):
        DistributedLevel.notify.debug('disable')
        if hasattr(self, 'geom'):
            del self.geom
        
        self.shutdownVisibility()
        self.destroyLevel()
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('titleText'))
        if self.smallTitleText:
            self.smallTitleText.cleanup()
            self.smallTitleText = None
        
        if self.titleText:
            self.titleText.cleanup()
            self.titleText = None
        
        self.zonesEnteredList = []
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        DistributedLevel.notify.debug('delete')
        DistributedObject.DistributedObject.delete(self)
        toonbase.localToon.chatMgr.chatInputSpeedChat.removeFactoryMenu()
        del self.factoryViews
        self.stopOuch()

    
    def requestReparent(self, entity, parentId):
        parent = self.getEntity(parentId)
        if parent is not None:
            entity.reparentTo(parent.getNodePath())
        else:
            DistributedLevel.notify.debug('entity %s requesting reparent to %s, not yet created' % (entity, parentId))
            entity.reparentTo(hidden)
            if not self.parent2pendingChildren.has_key(parentId):
                self.parent2pendingChildren[parentId] = []
                
                def doReparent(parentId = parentId, self = self):
                    parent = self.getEntity(parentId)
                    for child in self.parent2pendingChildren[parentId]:
                        DistributedLevel.notify.debug('performing pending reparent of %s to %s' % (child, parent))
                        child.reparentTo(parent.getNodePath())
                    
                    del self.parent2pendingChildren[parentId]
                    self.ignore(self.getEntityCreateEvent(parentId))

                self.accept(self.getEntityCreateEvent(parentId), doReparent)
            
            self.parent2pendingChildren[parentId].append(entity)

    
    def getZoneNode(self, zoneEntId):
        return self.zoneNum2node.get(zoneEntId)

    
    def warpToZone(self, zoneNum):
        zoneNode = self.getZoneNode(zoneNum)
        if zoneNode is None:
            return None
        
        toonbase.localToon.setPos(zoneNode, 0, 0, 0)
        toonbase.localToon.setHpr(zoneNode, 0, 0, 0)
        self.enterZone(zoneNum)

    
    def showZone(self, zoneNum):
        zone = self.getZoneNode(zoneNum)
        zone.unstash()
        zone.clearColor()

    
    def setColorZones(self, fColorZones):
        self.fColorZones = fColorZones
        self.resetVisibility()

    
    def getColorZones(self):
        return self.fColorZones

    
    def hideZone(self, zoneNum):
        zone = self.getZoneNode(zoneNum)
        if self.fColorZones:
            zone.unstash()
            zone.setColor(1, 0, 0)
        else:
            zone.stash()

    
    def setTransparency(self, alpha, zone = None):
        self.geom.setTransparency(1)
        if zone is None:
            node = self.geom
        else:
            node = self.getZoneNode(zoneNum)
        node.setAlphaScale(alpha)

    
    def initVisibility(self):
        self.curVisibleZoneNums = list2dict(self.zoneNums)
        del self.curVisibleZoneNums[LevelConstants.UberZoneEntId]
        self.curZoneNum = None
        self.visChangedThisFrame = 0
        self.fForceSetZoneThisFrame = 0
        
        def handleCameraRayFloorCollision(collEntry, self = self):
            name = collEntry.getIntoNode().getName()
            print 'camera floor ray collided with: %s' % name
            prefixLen = len(DistributedLevel.FloorCollPrefix)
            if name[:prefixLen] == DistributedLevel.FloorCollPrefix:
                
                try:
                    zoneNum = int(name[prefixLen:])
                except:
                    DistributedLevel.notify.warning('Invalid zone floor collision node: %s' % name)

                self.camEnterZone(zoneNum)
            

        self.accept('on-floor', handleCameraRayFloorCollision)
        if not (DistributedLevel.WantVisibility):
            zoneNums = list(self.zoneNums)
            zoneNums.remove(LevelConstants.UberZoneEntId)
            self.forceSetZoneThisFrame()
            self.setVisibility(zoneNums)
        
        taskMgr.add(self.visChangeTask, self.uniqueName(DistributedLevel.VisChangeTaskName), priority = 49)

    
    def shutdownVisibility(self):
        taskMgr.remove(self.uniqueName(DistributedLevel.VisChangeTaskName))

    
    def toonEnterZone(self, zoneNum, ouchLevel = None):
        DistributedLevel.notify.info('toonEnterZone%s' % zoneNum)
        if zoneNum != self.lastToonZone:
            self.lastToonZone = zoneNum
            print 'toon is standing in zone %s' % zoneNum
            messenger.send('factoryZoneChanged', [
                zoneNum])
        

    
    def camEnterZone(self, zoneNum):
        DistributedLevel.notify.info('camEnterZone%s' % zoneNum)
        self.enterZone(zoneNum)
        if zoneNum != self.lastCamZone:
            self.lastCamZone = zoneNum
            self.smallTitleText.hide()
            self.spawnTitleText()
        

    
    def lockVisibility(self, zoneNum = None, zoneId = None):
        if zoneId is not None:
            zoneNum = self.getZoneNumFromId(zoneId)
        
        self.notify.info('lockVisibility to zoneNum %s' % zoneNum)
        self.lockVizZone = zoneNum
        self.enterZone(self.lockVizZone)

    
    def unlockVisibility(self):
        self.notify.info('unlockVisibility')
        if not hasattr(self, 'lockVizZone'):
            self.notify.warning('visibility already unlocked')
        else:
            del self.lockVizZone
            self.updateVisibility()

    
    def enterZone(self, zoneNum):
        DistributedLevel.notify.info('entering zone %s' % zoneNum)
        if not (DistributedLevel.WantVisibility):
            return None
        
        if zoneNum == self.curZoneNum:
            return None
        
        if zoneNum not in self.zoneNumDict:
            DistributedLevel.notify.error('no ZoneEntity for this zone (%s)!!' % zoneNum)
        
        self.updateVisibility(zoneNum)

    
    def updateVisibility(self, zoneNum = None):
        if zoneNum is None:
            zoneNum = self.curZoneNum
            if zoneNum is None:
                return None
            
        
        if hasattr(self, 'lockVizZone'):
            zoneNum = self.lockVizZone
        
        zoneEnt = self.getEntity(zoneNum)
        visibleZoneNums = list2dict([
            zoneNum])
        visibleZoneNums.update(list2dict(zoneEnt.getVisibleZoneNums()))
        if not __debug__:
            if self.lastToonZone not in visibleZoneNums:
                if self.lastToonZone is not None:
                    self.notify.warning('adding zoneNum %s to visibility list because toon is standing in that zone!' % self.lastToonZone)
                    visibleZoneNums.update(list2dict([
                        self.lastToonZone]))
                
            
        
        vizZonesChanged = 1
        addedZoneNums = []
        removedZoneNums = []
        allVZ = dict(visibleZoneNums)
        allVZ.update(self.curVisibleZoneNums)
        for (vz, dummy) in allVZ.items():
            new = vz in visibleZoneNums
            old = vz in self.curVisibleZoneNums
            if new and old:
                continue
            
            if new:
                addedZoneNums.append(vz)
            else:
                removedZoneNums.append(vz)
        
        if not addedZoneNums and not removedZoneNums:
            DistributedLevel.notify.info('visible zone list has not changed')
            vizZonesChanged = 0
        else:
            DistributedLevel.notify.info('showing zones %s' % addedZoneNums)
            for az in addedZoneNums:
                self.showZone(az)
            
            DistributedLevel.notify.info('hiding zones %s' % removedZoneNums)
            for rz in removedZoneNums:
                self.hideZone(rz)
            
        if vizZonesChanged or self.fForceSetZoneThisFrame:
            self.setVisibility(visibleZoneNums.keys())
            self.fForceSetZoneThisFrame = 0
        
        self.curZoneNum = zoneNum
        self.curVisibleZoneNums = visibleZoneNums

    
    def setVisibility(self, vizList):
        if self.fColorZones and DistributedLevel.ColorZonesAllDOs:
            vizList = list(self.zoneNums)
            vizList.remove(LevelConstants.UberZoneEntId)
        
        uberZone = self.getZoneId(LevelConstants.UberZoneEntId)
        visibleZoneIds = [
            ToontownGlobals.UberZone,
            self.levelZone,
            uberZone]
        for vz in vizList:
            visibleZoneIds.append(self.getZoneId(vz))
        
        DistributedLevel.notify.info('new viz list: %s' % visibleZoneIds)
        toonbase.tcr.sendSetZoneMsg(self.levelZone, visibleZoneIds)

    
    def resetVisibility(self):
        self.curVisibleZoneNums = list2dict(self.zoneNums)
        del self.curVisibleZoneNums[LevelConstants.UberZoneEntId]
        for (vz, dummy) in self.curVisibleZoneNums.items():
            self.showZone(vz)
        
        self.updateVisibility()

    
    def handleVisChange(self):
        Level.Level.handleVisChange(self)
        self.visChangedThisFrame = 1

    
    def forceSetZoneThisFrame(self):
        self.fForceSetZoneThisFrame = 1

    
    def visChangeTask(self, task):
        if self.visChangedThisFrame or self.fForceSetZoneThisFrame:
            self.updateVisibility()
            self.visChangedThisFrame = 0
        
        return Task.cont

    if __dev__:
        
        def setAttribChange(self, entId, attribName, valueStr, username):
            value = eval(valueStr)
            self.levelSpec.setAttribChange(entId, attribName, value, username)

    
    
    def spawnTitleText(self):
        
        def getDescription(zoneNum, self = self):
            ent = self.entities.get(zoneNum)
            if ent and hasattr(ent, 'description'):
                return ent.description
            
            return None

        description = getDescription(self.lastCamZone)
        if description and description != '':
            taskMgr.remove(self.uniqueName('titleText'))
            self.smallTitleText.setText(description)
            self.titleText.setText(description)
            self.titleText.setColor(Vec4(*self.titleColor))
            self.titleText.setFg(self.titleColor)
            titleSeq = None
            if not (self.lastCamZone in self.zonesEnteredList):
                self.zonesEnteredList.append(self.lastCamZone)
                titleSeq = Task.sequence(Task.Task(self.hideSmallTitleTextTask), Task.Task(self.showTitleTextTask), Task.pause(0.10000000000000001), Task.pause(6.0), self.titleText.lerpColor(Vec4(self.titleColor[0], self.titleColor[1], self.titleColor[2], self.titleColor[3]), Vec4(self.titleColor[0], self.titleColor[1], self.titleColor[2], 0.0), 0.5))
            
            smallTitleSeq = Task.sequence(Task.Task(self.hideTitleTextTask), Task.Task(self.showSmallTitleTask))
            if titleSeq:
                seq = Task.sequence(titleSeq, smallTitleSeq)
            else:
                seq = smallTitleSeq
            taskMgr.add(seq, self.uniqueName('titleText'))
        

    
    def showTitleTextTask(self, task):
        self.titleText.show()
        return Task.done

    
    def hideTitleTextTask(self, task):
        if self.titleText:
            self.titleText.hide()
        
        return Task.done

    
    def showSmallTitleTask(self, task):
        if self.titleText:
            self.titleText.hide()
        
        self.smallTitleText.show()
        return Task.done

    
    def hideSmallTitleTextTask(self, task):
        if self.smallTitleText:
            self.smallTitleText.hide()
        
        return Task.done

    
    def startOuch(self, ouchLevel, period = 2):
        print 'startOuch %s' % ouchLevel
        if not hasattr(self, 'doingOuch'):
            
            def doOuch(task, self = self, ouchLevel = ouchLevel, period = period):
                self.b_setOuch(ouchLevel)
                self.lastOuchTime = globalClock.getFrameTime()
                taskMgr.doMethodLater(period, doOuch, DistributedLevel.OuchTaskName)

            delay = 0
            if hasattr(self, 'lastOuchTime'):
                curFrameTime = globalClock.getFrameTime()
                timeSinceLastOuch = curFrameTime - self.lastOuchTime
                if timeSinceLastOuch < period:
                    delay = period - timeSinceLastOuch
                
            
            if delay > 0:
                taskMgr.doMethodLater(period, doOuch, DistributedLevel.OuchTaskName)
            else:
                doOuch(None)
            self.doingOuch = 1
        

    
    def stopOuch(self):
        if hasattr(self, 'doingOuch'):
            taskMgr.remove(DistributedLevel.OuchTaskName)
            del self.doingOuch
        

    
    def b_setOuch(self, penalty, anim = None):
        self.notify.debug('b_setOuch %s' % penalty)
        av = toonbase.localToon
        if not (av.isStunned):
            self.d_setOuch(penalty)
            self.setOuch(penalty, anim)
        

    
    def d_setOuch(self, penalty):
        self.sendUpdate('setOuch', [
            penalty])

    
    def setOuch(self, penalty, anim = None):
        if anim == 'Squish':
            toonbase.tcr.playGame.getPlace().fsm.request('squished')
        elif anim == 'Fall':
            toonbase.tcr.playGame.getPlace().fsm.request('fallDown')
        
        av = toonbase.localToon
        av.stunToon()
        av.playDialogueForString('!')


