# File: D (Python 2.2)

from ToonBaseGlobal import *
from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
import ToontownGlobals
import DirectNotifyGlobal
import FSM
import DistributedObject
import ZoneUtil
import Suit
import DelayDelete
import FADoorCodes
import DoorTypes
import ToontownDialog

class DistributedDoor(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.openSfx = base.loadSfx('phase_3.5/audio/sfx/Door_Open_1.mp3')
        self.closeSfx = base.loadSfx('phase_3.5/audio/sfx/Door_Close_1.mp3')
        self.nametag = None
        self.fsm = FSM.FSM('DistributedDoor_right', [
            State.State('off', self.enterOff, self.exitOff, [
                'closing',
                'closed',
                'opening',
                'open']),
            State.State('closing', self.enterClosing, self.exitClosing, [
                'closed',
                'opening']),
            State.State('closed', self.enterClosed, self.exitClosed, [
                'opening']),
            State.State('opening', self.enterOpening, self.exitOpening, [
                'open']),
            State.State('open', self.enterOpen, self.exitOpen, [
                'closing',
                'open'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.exitDoorFSM = FSM.FSM('DistributedDoor_left', [
            State.State('off', self.exitDoorEnterOff, self.exitDoorExitOff, [
                'closing',
                'closed',
                'opening',
                'open']),
            State.State('closing', self.exitDoorEnterClosing, self.exitDoorExitClosing, [
                'closed',
                'opening']),
            State.State('closed', self.exitDoorEnterClosed, self.exitDoorExitClosed, [
                'opening']),
            State.State('opening', self.exitDoorEnterOpening, self.exitDoorExitOpening, [
                'open']),
            State.State('open', self.exitDoorEnterOpen, self.exitDoorExitOpen, [
                'closing',
                'open'])], 'off', 'off')
        self.exitDoorFSM.enterInitialState()

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.avatarTracks = []
        self.avatarExitTracks = []
        self.avatarIDList = []
        self.avatarExitIDList = []
        self.doorTrack = None
        self.doorExitTrack = None

    
    def disable(self):
        self.clearNametag()
        taskMgr.remove(self.checkIsDoorHitTaskName())
        self.ignore(self.getEnterTriggerEvent())
        self.ignore(self.getExitTriggerEvent())
        self.ignore('clearOutToonInterior')
        self.fsm.request('off')
        self.exitDoorFSM.request('off')
        if self.__dict__.has_key('building'):
            del self.building
        
        self.finishAllTracks()
        self.avatarIDList = []
        self.avatarExitIDList = []
        if hasattr(self, 'tempDoorNodePath'):
            self.tempDoorNodePath.removeNode()
            del self.tempDoorNodePath
        
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        del self.fsm
        del self.exitDoorFSM
        del self.openSfx
        del self.closeSfx
        DistributedObject.DistributedObject.delete(self)

    
    def setupNametag(self):
        if ZoneUtil.isInterior(self.zoneId):
            return None
        
        if self.nametag == None:
            self.nametag = NametagGroup()
            self.nametag.setFont(ToontownGlobals.getSignFont())
            self.nametag.setContents(Nametag.CName)
            self.nametag.setColorCode(NametagGroup.CCToonBuilding)
            self.nametag.setActive(0)
            self.nametag.setAvatar(self.getDoorNodePath())
            self.nametag.setObjectCode(self.block)
            name = self.cr.playGame.dnaStore.getTitleFromBlockNumber(self.block)
            self.nametag.setName(name)
            self.nametag.manage(toonbase.marginManager)
        

    
    def clearNametag(self):
        if self.nametag != None:
            self.nametag.unmanage(toonbase.marginManager)
            self.nametag.setAvatar(NodePath())
            self.nametag = None
        

    
    def getTriggerName(self):
        if self.doorType == DoorTypes.EXT_HQ or self.doorType == DoorTypes.INT_HQ:
            return 'door_trigger_' + str(self.block) + '_' + str(self.doorIndex)
        else:
            return 'door_trigger_' + str(self.block)

    
    def getTriggerName_wip(self):
        name = 'door_trigger_%d' % (self.doId,)
        return name

    
    def getEnterTriggerEvent(self):
        return 'enter' + self.getTriggerName()

    
    def getExitTriggerEvent(self):
        return 'exit' + self.getTriggerName()

    
    def hideDoorParts(self):
        if self.doorType == DoorTypes.EXT_HQ:
            self.findDoorNode('leftDoor').hide()
            self.findDoorNode('rightDoor').hide()
            self.findDoorNode('doorFrameHoleRight').hide()
            self.findDoorNode('doorFrameHoleLeft').hide()
        else:
            return None

    
    def setTriggerName(self):
        if self.doorType == DoorTypes.EXT_HQ:
            building = self.getBuilding()
            doorTrigger = building.find('**/door_' + str(self.doorIndex) + '/**/door_trigger*')
            doorTrigger.node().setName(self.getTriggerName())
        else:
            return None

    
    def setTriggerName_wip(self):
        building = self.getBuilding()
        doorTrigger = building.find('**/door_%d/**/door_trigger_%d' % (self.doorIndex, self.block))
        if doorTrigger.isEmpty():
            doorTrigger = building.find('**/door_trigger_%d' % (self.block,))
        
        if doorTrigger.isEmpty():
            doorTrigger = building.find('**/door_%d/**/door_trigger_*' % (self.doorIndex,))
        
        if doorTrigger.isEmpty():
            doorTrigger = building.find('**/door_trigger_*')
        
        doorTrigger.node().setName(self.getTriggerName())

    
    def setZoneIdAndBlock(self, zoneId, block):
        self.zoneId = zoneId
        self.block = block

    
    def setDoorType(self, doorType):
        self.doorType = doorType

    
    def setDoorIndex(self, doorIndex):
        self.doorIndex = doorIndex

    
    def setSwing(self, flags):
        self.swing = flags & 1 != 0
        self.exitDoorSwing = flags & 2 != 0

    
    def setOtherZoneIdAndDoId(self, zoneId, distributedObjectID):
        self.otherZoneId = zoneId
        self.otherDoId = distributedObjectID

    
    def setState(self, state, timestamp):
        self.fsm.request(state, [
            globalClockDelta.localElapsedTime(timestamp)])

    
    def setExitDoorState(self, state, timestamp):
        self.exitDoorFSM.request(state, [
            globalClockDelta.localElapsedTime(timestamp)])

    
    def announceGenerate(self):
        self.hideDoorParts()
        self.setTriggerName()
        self.accept(self.getEnterTriggerEvent(), self.doorTrigger)
        self.acceptOnce('clearOutToonInterior', self.doorTrigger)
        self.setupNametag()

    
    def getBuilding(self):
        if not self.__dict__.has_key('building'):
            if self.doorType == DoorTypes.INT_STANDARD:
                door = render.find('**/leftDoor;+s')
                self.building = door.getParent()
            elif self.doorType == DoorTypes.INT_HQ:
                door = render.find('**/door_0')
                self.building = door.getParent()
            elif self.doorType == DoorTypes.EXT_STANDARD or self.doorType == DoorTypes.EXT_HQ:
                self.building = self.cr.playGame.hood.loader.geom.find('**/??' + str(self.block) + ':*_landmark_*_DNARoot;+s')
            else:
                self.notify.error('No such door type as ' + str(self.doorType))
        
        return self.building

    
    def getBuilding_wip(self):
        if not self.__dict__.has_key('building'):
            if self.__dict__.has_key('block'):
                self.building = self.cr.playGame.hood.loader.geom.find('**/??' + str(self.block) + ':*_landmark_*_DNARoot;+s')
            else:
                self.building = self.cr.playGame.hood.loader.geom
                print '---------------- door is interior -------'
        
        return self.building

    
    def avatarInstantFeedbackTrack(self, avatar, duration):
        avatar.stopSmooth()
        track = LerpPosHprScaleInterval(node = camera, other = avatar, duration = duration, pos = Point3(-10, -2, avatar.getHeight() + 2), hpr = VBase3(-79, -20, 0), scale = VBase3(1, 1, 1), blendType = 'easeIn')
        track.delayDelete = DelayDelete.DelayDelete(avatar)
        return track

    
    def readyToExit(self):
        base.transitions.fadeScreen(1.0)
        self.sendUpdate('requestExit')

    
    def avatarEnterDoorTrack(self, avatar, duration):
        trackName = 'avatarEnterDoor-%d-%d' % (self.doId, avatar.doId)
        track = Parallel(name = trackName)
        otherNP = self.getDoorNodePath()
        if hasattr(avatar, 'stopSmooth'):
            avatar.stopSmooth()
        
        if avatar.doId == toonbase.localToon.doId:
            track.append(LerpPosHprInterval(node = camera, other = avatar, duration = duration, pos = Point3(0, -8, avatar.getHeight()), hpr = VBase3(0, 0, 0), blendType = 'easeInOut'))
        
        finalPos = avatar.getParent().getRelativePoint(otherNP, Point3(1.5, 2, ToontownGlobals.FloorOffset))
        moveHere = Sequence(self.getAnimStateInterval(avatar, 'walk'), LerpPosInterval(node = avatar, duration = duration, pos = finalPos, blendType = 'easeIn'))
        track.append(moveHere)
        if avatar.doId == toonbase.localToon.doId:
            track.append(Sequence(Wait(duration * 0.5), Func(base.transitions.irisOut, duration * 0.5), Wait(duration * 0.5), Func(avatar.b_setParent, ToontownGlobals.SPHidden)))
        
        track.delayDelete = DelayDelete.DelayDelete(avatar)
        return track

    
    def avatarEnqueueTrack(self, avatar, duration):
        if hasattr(avatar, 'stopSmooth'):
            avatar.stopSmooth()
        
        offset = Point3(1.5, -5 + -2 * len(self.avatarIDList), ToontownGlobals.FloorOffset)
        otherNP = self.getDoorNodePath()
        walkLike = ActorInterval(avatar, 'walk', startTime = 1, duration = duration, endTime = 0.0001)
        standHere = Sequence(LerpPosHprInterval(node = avatar, other = otherNP, duration = duration, pos = offset, hpr = VBase3(0, 0, 0), blendType = 'easeInOut'), self.getAnimStateInterval(avatar, 'neutral'))
        trackName = 'avatarEnqueueDoor-%d-%d' % (self.doId, avatar.doId)
        track = Parallel(walkLike, standHere, name = trackName)
        track.delayDelete = DelayDelete.DelayDelete(avatar)
        return track

    
    def getAnimStateInterval(self, avatar, animName):
        isSuit = isinstance(avatar, Suit.Suit)
        if isSuit:
            return Func(avatar.loop, animName, 0)
        else:
            return Func(avatar.setAnimState, animName, 1.0)

    
    def isDoorHit(self):
        vec = toonbase.localToon.getRelativeVector(self.currentDoorNp, self.currentDoorVec)
        return vec.getY() < -0.5

    
    def enterDoor(self):
        messenger.send('DistributedDoor_doorTrigger')
        self.sendUpdate('requestEnter')

    
    def checkIsDoorHitTaskName(self):
        return 'checkIsDoorHit' + self.getTriggerName()

    
    def checkIsDoorHitTask(self, task):
        if self.isDoorHit():
            self.ignore(self.checkIsDoorHitTaskName())
            self.ignore(self.getExitTriggerEvent())
            self.enterDoor()
            return Task.done
        
        return Task.cont

    
    def cancelCheckIsDoorHitTask(self, args):
        taskMgr.remove(self.checkIsDoorHitTaskName())
        del self.currentDoorNp
        del self.currentDoorVec
        self.ignore(self.getExitTriggerEvent())
        self.accept(self.getEnterTriggerEvent(), self.doorTrigger)

    
    def doorTrigger(self, args = None):
        self.ignore(self.getEnterTriggerEvent())
        if args == None:
            self.enterDoor()
        else:
            self.currentDoorNp = NodePath(args.getIntoNodePath())
            self.currentDoorVec = Vec3(args.getIntoSurfaceNormal())
            if self.isDoorHit():
                self.enterDoor()
            else:
                self.accept(self.getExitTriggerEvent(), self.cancelCheckIsDoorHitTask)
                taskMgr.add(self.checkIsDoorHitTask, self.checkIsDoorHitTaskName())

    
    def toonEnter(self, avatarID):
        avatar = self.cr.doId2do.get(avatarID, None)
        if avatar:
            track = self.avatarEnqueueTrack(avatar, 0.5)
            track.start()
            self.avatarTracks.append(track)
            self.avatarIDList.append(avatarID)
        

    
    def suitEnter(self, avatarID):
        avatar = self.cr.doId2do.get(avatarID, None)
        if avatar:
            avatar.setState('Door')
            track = self.avatarEnqueueTrack(avatar, 0.5)
            track.start()
            self.avatarTracks.append(track)
            self.avatarIDList.append(avatarID)
        

    
    def rejectEnter(self, reason):
        message = FADoorCodes.reasonDict[reason]
        if message:
            self._DistributedDoor__faRejectEnter(message)
        else:
            self._DistributedDoor__basicRejectEnter()

    
    def _DistributedDoor__basicRejectEnter(self):
        self.accept(self.getEnterTriggerEvent(), self.doorTrigger)
        self.cr.playGame.getPlace().setState('walk')

    
    def _DistributedDoor__faRejectEnter(self, message):
        self.rejectDialog = ToontownDialog.GlobalDialog(message = message, doneEvent = 'doorRejectAck', style = ToontownDialog.Acknowledge)
        self.rejectDialog.show()
        self.rejectDialog.delayDelete = DelayDelete.DelayDelete(self)
        toonbase.localToon.b_setAnimState('neutral', 1.0)
        self.acceptOnce('doorRejectAck', self._DistributedDoor__handleRejectAck)

    
    def _DistributedDoor__handleRejectAck(self):
        doneStatus = self.rejectDialog.doneStatus
        if doneStatus != 'ok':
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))
        
        self._DistributedDoor__basicRejectEnter()
        self.rejectDialog.cleanup()
        del self.rejectDialog

    
    def getDoorNodePath(self):
        if self.doorType == DoorTypes.INT_STANDARD:
            otherNP = render.find('**/door_origin')
        elif self.doorType == DoorTypes.EXT_STANDARD:
            if hasattr(self, 'tempDoorNodePath'):
                return self.tempDoorNodePath
            else:
                posHpr = self.cr.playGame.dnaStore.getDoorPosHprFromBlockNumber(self.block)
                otherNP = NodePath('doorOrigin')
                otherNP.setPos(posHpr.getPos())
                otherNP.setHpr(posHpr.getHpr())
                self.tempDoorNodePath = otherNP
        elif self.doorType == DoorTypes.EXT_HQ:
            building = self.getBuilding()
            otherNP = building.find('**/door_origin_' + str(self.doorIndex))
        elif self.doorType == DoorTypes.INT_HQ:
            otherNP = render.find('**/door_origin_' + str(self.doorIndex))
        else:
            self.notify.error('No such door type as ' + str(self.doorType))
        return otherNP

    
    def avatarExitTrack(self, avatar, duration):
        avatar.stopSmooth()
        otherNP = self.getDoorNodePath()
        trackName = 'avatarExitDoor-%d-%d' % (self.doId, avatar.doId)
        track = Sequence(name = trackName)
        track.append(Func(avatar.setAnimState, 'walk', 1.0))
        track.append(PosHprInterval(avatar, Point3(-1.5, 2, ToontownGlobals.FloorOffset), VBase3(179, 0, 0), other = otherNP))
        track.append(Func(avatar.setParent, ToontownGlobals.SPRender))
        if avatar.doId == toonbase.localToon.doId:
            track.append(PosHprInterval(camera, VBase3(-1.5, 5, avatar.getHeight()), VBase3(180, 0, 0), other = otherNP))
        
        track.append(LerpPosHprInterval(node = avatar, other = otherNP, duration = duration, pos = Point3(-1.5, -5, ToontownGlobals.FloorOffset), hpr = VBase3(179, 0, 0), blendType = 'easeInOut'))
        if avatar.doId == toonbase.localToon.doId:
            track.append(Func(self.exitCompleted))
            track.append(Func(base.transitions.irisIn))
        
        track.append(Func(avatar.startSmooth))
        track.delayDelete = DelayDelete.DelayDelete(avatar)
        return track

    
    def exitCompleted(self):
        toonbase.localToon.setAnimState('neutral', 1.0)
        self.cr.playGame.getPlace().setState('walk')
        toonbase.localToon.d_setParent(ToontownGlobals.SPRender)

    
    def toonExit(self, avatarID):
        if avatarID in self.avatarIDList:
            self.avatarIDList.remove(avatarID)
            if avatarID == toonbase.localToon.doId:
                self.exitCompleted()
            
        else:
            self.avatarExitIDList.append(avatarID)

    
    def finishDoorTrack(self):
        if self.doorTrack:
            self.doorTrack.finish()
        
        self.doorTrack = None

    
    def finishDoorExitTrack(self):
        if self.doorExitTrack:
            self.doorExitTrack.finish()
        
        self.doorExitTrack = None

    
    def finishAllTracks(self):
        self.finishDoorTrack()
        self.finishDoorExitTrack()
        for t in self.avatarTracks:
            t.finish()
        
        self.avatarTracks = []
        for t in self.avatarExitTracks:
            t.finish()
        
        self.avatarExitTracks = []

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterClosing(self, ts):
        doorFrameHoleRight = self.findDoorNode('doorFrameHoleRight')
        if doorFrameHoleRight.isEmpty():
            self.notify.warning('enterClosing(): did not find doorFrameHoleRight')
            return None
        
        rightDoor = self.findDoorNode('rightDoor')
        if rightDoor.isEmpty():
            self.notify.warning('enterClosing(): did not find rightDoor')
            return None
        
        otherNP = self.getDoorNodePath()
        trackName = 'doorClose-%d' % self.doId
        self.doorTrack = Sequence(LerpHprInterval(node = rightDoor, duration = 1.0, hpr = VBase3(0, 0, 0), startHpr = VBase3(100, 0, 0), other = otherNP, blendType = 'easeInOut'), Func(doorFrameHoleRight.hide), Func(rightDoor.hide), SoundInterval(self.closeSfx, node = rightDoor), name = trackName)
        self.doorTrack.start(ts)
        if hasattr(self, 'done'):
            zoneId = self.otherZoneId
            request = {
                'loader': ZoneUtil.getBranchLoaderName(zoneId),
                'where': ZoneUtil.getToonWhereName(zoneId),
                'how': 'doorIn',
                'hoodId': ZoneUtil.getHoodId(zoneId),
                'zoneId': zoneId,
                'shardId': None,
                'avId': -1,
                'doorDoId': self.otherDoId }
            messenger.send('doorDoneEvent', [
                request])
        

    
    def exitClosing(self):
        self.finishDoorTrack()

    
    def enterClosed(self, ts):
        pass

    
    def exitClosed(self):
        pass

    
    def enterOpening(self, ts):
        doorFrameHoleRight = self.findDoorNode('doorFrameHoleRight')
        if doorFrameHoleRight.isEmpty():
            self.notify.warning('enterOpening(): did not find doorFrameHoleRight')
            return None
        
        rightDoor = self.findDoorNode('rightDoor')
        if rightDoor.isEmpty():
            self.notify.warning('enterOpening(): did not find rightDoor')
            return None
        
        otherNP = self.getDoorNodePath()
        trackName = 'doorOpen-%d' % self.doId
        self.doorTrack = Parallel(SoundInterval(self.openSfx, node = rightDoor), Sequence(HprInterval(rightDoor, VBase3(0, 0, 0), other = otherNP), Wait(0.40000000000000002), Func(rightDoor.show), Func(doorFrameHoleRight.show), LerpHprInterval(node = rightDoor, duration = 0.59999999999999998, hpr = VBase3(100, 0, 0), startHpr = VBase3(0, 0, 0), other = otherNP, blendType = 'easeInOut')), name = trackName)
        self.doorTrack.start(ts)

    
    def exitOpening(self):
        self.finishDoorTrack()

    
    def enterOpen(self, ts):
        for avatarID in self.avatarIDList:
            avatar = self.cr.doId2do.get(avatarID)
            if avatar:
                track = self.avatarEnterDoorTrack(avatar, 1.0)
                track.start(ts)
                self.avatarTracks.append(track)
            
            if avatarID == toonbase.localToon.doId:
                self.done = 1
            
        
        self.avatarIDList = []

    
    def exitOpen(self):
        for track in self.avatarTracks:
            track.finish()
        
        self.avatarTracks = []

    
    def exitDoorEnterOff(self):
        pass

    
    def exitDoorExitOff(self):
        pass

    
    def exitDoorEnterClosing(self, ts):
        doorFrameHoleLeft = self.findDoorNode('doorFrameHoleLeft')
        if doorFrameHoleLeft.isEmpty():
            self.notify.warning('enterOpening(): did not find flatDoors')
            return None
        
        leftDoor = self.findDoorNode('leftDoor')
        if not leftDoor.isEmpty():
            otherNP = self.getDoorNodePath()
            trackName = 'doorExitTrack-%d' % self.doId
            self.doorExitTrack = Sequence(LerpHprInterval(node = leftDoor, duration = 1.0, hpr = VBase3(0, 0, 0), startHpr = VBase3(-100, 0, 0), other = otherNP, blendType = 'easeInOut'), Func(doorFrameHoleLeft.hide), Func(leftDoor.hide), SoundInterval(self.closeSfx, node = leftDoor), name = trackName)
            self.doorExitTrack.start(ts)
        

    
    def exitDoorExitClosing(self):
        self.finishDoorExitTrack()

    
    def exitDoorEnterClosed(self, ts):
        pass

    
    def exitDoorExitClosed(self):
        pass

    
    def exitDoorEnterOpening(self, ts):
        doorFrameHoleLeft = self.findDoorNode('doorFrameHoleLeft')
        if doorFrameHoleLeft.isEmpty():
            self.notify.warning('enterOpening(): did not find flatDoors')
            return None
        
        leftDoor = self.findDoorNode('leftDoor')
        if not leftDoor.isEmpty():
            otherNP = self.getDoorNodePath()
            trackName = 'doorDoorExitTrack-%d' % self.doId
            self.doorExitTrack = Parallel(SoundInterval(self.openSfx, node = leftDoor), Sequence(Func(leftDoor.show), Func(doorFrameHoleLeft.show), LerpHprInterval(node = leftDoor, duration = 0.59999999999999998, hpr = VBase3(-100, 0, 0), startHpr = VBase3(0, 0, 0), other = otherNP, blendType = 'easeInOut')), name = trackName)
            self.doorExitTrack.start(ts)
        else:
            self.notify.warning('exitDoorEnterOpening(): did not find leftDoor')

    
    def exitDoorExitOpening(self):
        self.finishDoorExitTrack()

    
    def exitDoorEnterOpen(self, ts):
        for avatarID in self.avatarExitIDList:
            avatar = self.cr.doId2do.get(avatarID)
            if avatar:
                track = self.avatarExitTrack(avatar, 0.20000000000000001)
                track.start(ts)
                self.avatarExitTracks.append(track)
            
        
        self.avatarExitIDList = []

    
    def exitDoorExitOpen(self):
        for track in self.avatarExitTracks:
            track.finish()
        
        self.avatarExitTracks = []

    
    def findDoorNode(self, string):
        building = self.getBuilding()
        foundNode = building.find('**/door_' + str(self.doorIndex) + '/**/' + string + '*;+s')
        if foundNode.isEmpty():
            foundNode = building.find('**/' + string + '*;+s')
        
        return foundNode


