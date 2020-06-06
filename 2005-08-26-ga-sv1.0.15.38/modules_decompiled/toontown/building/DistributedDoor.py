# File: D (Python 2.2)

from toontown.toonbase.ToonBaseGlobal import *
from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.distributed import DistributedObject
from toontown.hood import ZoneUtil
from toontown.suit import Suit
from direct.distributed import DelayDelete
import FADoorCodes
import DoorTypes
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer

class DistributedDoor(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.openSfx = base.loadSfx('phase_3.5/audio/sfx/Door_Open_1.mp3')
        self.closeSfx = base.loadSfx('phase_3.5/audio/sfx/Door_Close_1.mp3')
        self.nametag = None
        self.fsm = ClassicFSM.ClassicFSM('DistributedDoor_right', [
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
        self.exitDoorFSM = ClassicFSM.ClassicFSM('DistributedDoor_left', [
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

    
    def wantsNametag(self):
        return not ZoneUtil.isInterior(self.zoneId)

    
    def setupNametag(self):
        if not self.wantsNametag():
            return None
        
        if self.nametag == None:
            self.nametag = NametagGroup()
            self.nametag.setFont(ToontownGlobals.getBuildingNametagFont())
            if TTLocalizer.BuildingNametagShadow:
                self.nametag.setShadow(*TTLocalizer.BuildingNametagShadow)
            
            self.nametag.setContents(Nametag.CName)
            self.nametag.setColorCode(NametagGroup.CCToonBuilding)
            self.nametag.setActive(0)
            self.nametag.setAvatar(self.getDoorNodePath())
            self.nametag.setObjectCode(self.block)
            name = self.cr.playGame.dnaStore.getTitleFromBlockNumber(self.block)
            self.nametag.setName(name)
            self.nametag.manage(base.marginManager)
        

    
    def clearNametag(self):
        if self.nametag != None:
            self.nametag.unmanage(base.marginManager)
            self.nametag.setAvatar(NodePath())
            self.nametag = None
        

    
    def getTriggerName(self):
        if self.doorType == DoorTypes.EXT_HQ and self.doorType == DoorTypes.INT_HQ and self.doorType == DoorTypes.INT_COGHQ or self.doorType == DoorTypes.EXT_COGHQ:
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
        if self.doorType == DoorTypes.EXT_HQ and self.doorType == DoorTypes.EXT_COGHQ or self.doorType == DoorTypes.INT_COGHQ:
            self.hideIfHasFlat(self.findDoorNode('rightDoor'))
            self.hideIfHasFlat(self.findDoorNode('leftDoor'))
            self.findDoorNode('doorFrameHoleRight').hide()
            self.findDoorNode('doorFrameHoleLeft').hide()
        else:
            return None

    
    def setTriggerName(self):
        if self.doorType == DoorTypes.EXT_HQ and self.doorType == DoorTypes.EXT_COGHQ or self.doorType == DoorTypes.INT_COGHQ:
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
        self.leftSwing = flags & 1 != 0
        self.rightSwing = flags & 2 != 0

    
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
        if self.doorType == DoorTypes.INT_STANDARD:
            self.bHasFlat = True
        else:
            self.bHasFlat = not self.findDoorNode('door*flat', True).isEmpty()
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
            elif self.doorType == DoorTypes.EXT_COGHQ or self.doorType == DoorTypes.INT_COGHQ:
                self.building = self.cr.playGame.hood.loader.geom
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
        track = LerpPosHprScaleInterval(nodePath = camera, other = avatar, duration = duration, pos = Point3(-10, -2, avatar.getHeight() + 2), hpr = VBase3(-79, -20, 0), scale = VBase3(1, 1, 1), blendType = 'easeIn')
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
        
        if avatar.doId == base.localAvatar.doId:
            track.append(LerpPosHprInterval(nodePath = camera, other = avatar, duration = duration, pos = Point3(0, -8, avatar.getHeight()), hpr = VBase3(0, 0, 0), blendType = 'easeInOut'))
        
        finalPos = avatar.getParent().getRelativePoint(otherNP, Point3(1.5, 2, ToontownGlobals.FloorOffset))
        moveHere = Sequence(self.getAnimStateInterval(avatar, 'walk'), LerpPosInterval(nodePath = avatar, duration = duration, pos = finalPos, blendType = 'easeIn'))
        track.append(moveHere)
        if avatar.doId == base.localAvatar.doId:
            track.append(Sequence(Wait(duration * 0.5), Func(base.transitions.irisOut, duration * 0.5), Wait(duration * 0.5), Func(avatar.b_setParent, ToontownGlobals.SPHidden)))
        
        track.delayDelete = DelayDelete.DelayDelete(avatar)
        return track

    
    def avatarEnqueueTrack(self, avatar, duration):
        if hasattr(avatar, 'stopSmooth'):
            avatar.stopSmooth()
        
        back = -5.0 - 2.0 * len(self.avatarIDList)
        if back < -9.0:
            back = -9.0
        
        offset = Point3(1.5, back, ToontownGlobals.FloorOffset)
        otherNP = self.getDoorNodePath()
        walkLike = ActorInterval(avatar, 'walk', startTime = 1, duration = duration, endTime = 0.0001)
        standHere = Sequence(LerpPosHprInterval(nodePath = avatar, other = otherNP, duration = duration, pos = offset, hpr = VBase3(0, 0, 0), blendType = 'easeInOut'), self.getAnimStateInterval(avatar, 'neutral'))
        trackName = 'avatarEnqueueDoor-%d-%d' % (self.doId, avatar.doId)
        track = Parallel(walkLike, standHere, name = trackName)
        track.delayDelete = DelayDelete.DelayDelete(avatar)
        return track

    
    def getAnimStateInterval(self, avatar, animName):
        isSuit = isinstance(avatar, Suit.Suit)
        if isSuit:
            return Func(avatar.loop, animName, 0)
        else:
            return Func(avatar.setAnimState, animName)

    
    def isDoorHit(self):
        vec = base.localAvatar.getRelativeVector(self.currentDoorNp, self.currentDoorVec)
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
            self.currentDoorVec = Vec3(args.getSurfaceNormal(self.currentDoorNp))
            if self.isDoorHit():
                self.enterDoor()
            else:
                self.accept(self.getExitTriggerEvent(), self.cancelCheckIsDoorHitTask)
                taskMgr.add(self.checkIsDoorHitTask, self.checkIsDoorHitTaskName())

    
    def avatarEnter(self, avatarID):
        avatar = self.cr.doId2do.get(avatarID, None)
        if avatar:
            avatar.setAnimState('neutral')
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
        self.rejectDialog = TTDialog.TTGlobalDialog(message = message, doneEvent = 'doorRejectAck', style = TTDialog.Acknowledge)
        self.rejectDialog.show()
        self.rejectDialog.delayDelete = DelayDelete.DelayDelete(self)
        base.localAvatar.b_setAnimState('neutral')
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
        elif self.doorType == DoorTypes.EXT_HQ and self.doorType == DoorTypes.EXT_COGHQ or self.doorType == DoorTypes.INT_COGHQ:
            building = self.getBuilding()
            otherNP = building.find('**/door_origin_' + str(self.doorIndex))
        elif self.doorType == DoorTypes.INT_HQ:
            otherNP = render.find('**/door_origin_' + str(self.doorIndex))
        else:
            self.notify.error('No such door type as ' + str(self.doorType))
        return otherNP

    
    def avatarExitTrack(self, avatar, duration):
        if hasattr(avatar, 'stopSmooth'):
            avatar.stopSmooth()
        
        otherNP = self.getDoorNodePath()
        trackName = 'avatarExitDoor-%d-%d' % (self.doId, avatar.doId)
        track = Sequence(name = trackName)
        track.append(self.getAnimStateInterval(avatar, 'walk'))
        track.append(PosHprInterval(avatar, Point3(-1.5, 0, ToontownGlobals.FloorOffset), VBase3(179, 0, 0), other = otherNP))
        track.append(Func(avatar.setParent, ToontownGlobals.SPRender))
        if avatar.doId == base.localAvatar.doId:
            track.append(PosHprInterval(camera, VBase3(-1.5, 5, avatar.getHeight()), VBase3(180, 0, 0), other = otherNP))
        
        if avatar.doId == base.localAvatar.doId:
            finalPos = render.getRelativePoint(otherNP, Point3(-1.5, -6, ToontownGlobals.FloorOffset))
        else:
            finalPos = render.getRelativePoint(otherNP, Point3(-1.5, -3, ToontownGlobals.FloorOffset))
        track.append(LerpPosInterval(nodePath = avatar, duration = duration, pos = finalPos, blendType = 'easeInOut'))
        if avatar.doId == base.localAvatar.doId:
            track.append(Func(self.exitCompleted))
            track.append(Func(base.transitions.irisIn))
        
        if hasattr(avatar, 'startSmooth'):
            track.append(Func(avatar.startSmooth))
        
        track.delayDelete = DelayDelete.DelayDelete(avatar)
        return track

    
    def exitCompleted(self):
        base.localAvatar.setAnimState('neutral')
        self.cr.playGame.getPlace().setState('walk')
        base.localAvatar.d_setParent(ToontownGlobals.SPRender)

    
    def avatarExit(self, avatarID):
        if avatarID in self.avatarIDList:
            self.avatarIDList.remove(avatarID)
            if avatarID == base.localAvatar.doId:
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

    
    def getRequestStatus(self):
        zoneId = self.otherZoneId
        request = {
            'loader': ZoneUtil.getBranchLoaderName(zoneId),
            'where': ZoneUtil.getToonWhereName(zoneId),
            'how': 'doorIn',
            'hoodId': ZoneUtil.getHoodId(zoneId),
            'zoneId': zoneId,
            'shardId': None,
            'avId': -1,
            'allowRedirect': 0,
            'doorDoId': self.otherDoId }
        return request

    
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
        if self.rightSwing:
            h = 100
        else:
            h = -100
        self.finishDoorTrack()
        self.doorTrack = Sequence(LerpHprInterval(nodePath = rightDoor, duration = 1.0, hpr = VBase3(0, 0, 0), startHpr = VBase3(h, 0, 0), other = otherNP, blendType = 'easeInOut'), Func(doorFrameHoleRight.hide), Func(self.hideIfHasFlat, rightDoor), SoundInterval(self.closeSfx, node = rightDoor), name = trackName)
        self.doorTrack.start(ts)
        if hasattr(self, 'done'):
            request = self.getRequestStatus()
            messenger.send('doorDoneEvent', [
                request])
        

    
    def exitClosing(self):
        pass

    
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
        if self.rightSwing:
            h = 100
        else:
            h = -100
        self.finishDoorTrack()
        self.doorTrack = Parallel(SoundInterval(self.openSfx, node = rightDoor), Sequence(HprInterval(rightDoor, VBase3(0, 0, 0), other = otherNP), Wait(0.40000000000000002), Func(rightDoor.show), Func(doorFrameHoleRight.show), LerpHprInterval(nodePath = rightDoor, duration = 0.59999999999999998, hpr = VBase3(h, 0, 0), startHpr = VBase3(0, 0, 0), other = otherNP, blendType = 'easeInOut')), name = trackName)
        self.doorTrack.start(ts)

    
    def exitOpening(self):
        pass

    
    def enterOpen(self, ts):
        for avatarID in self.avatarIDList:
            avatar = self.cr.doId2do.get(avatarID)
            if avatar:
                track = self.avatarEnterDoorTrack(avatar, 1.0)
                track.start(ts)
                self.avatarTracks.append(track)
            
            if avatarID == base.localAvatar.doId:
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
        
        if self.leftSwing:
            h = -100
        else:
            h = 100
        leftDoor = self.findDoorNode('leftDoor')
        if not leftDoor.isEmpty():
            otherNP = self.getDoorNodePath()
            trackName = 'doorExitTrack-%d' % self.doId
            self.finishDoorExitTrack()
            self.doorExitTrack = Sequence(LerpHprInterval(nodePath = leftDoor, duration = 1.0, hpr = VBase3(0, 0, 0), startHpr = VBase3(h, 0, 0), other = otherNP, blendType = 'easeInOut'), Func(doorFrameHoleLeft.hide), Func(self.hideIfHasFlat, leftDoor), SoundInterval(self.closeSfx, node = leftDoor), name = trackName)
            self.doorExitTrack.start(ts)
        

    
    def exitDoorExitClosing(self):
        pass

    
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
        if self.leftSwing:
            h = -100
        else:
            h = 100
        if not leftDoor.isEmpty():
            otherNP = self.getDoorNodePath()
            trackName = 'doorDoorExitTrack-%d' % self.doId
            self.finishDoorExitTrack()
            self.doorExitTrack = Parallel(SoundInterval(self.openSfx, node = leftDoor), Sequence(Func(leftDoor.show), Func(doorFrameHoleLeft.show), LerpHprInterval(nodePath = leftDoor, duration = 0.59999999999999998, hpr = VBase3(h, 0, 0), startHpr = VBase3(0, 0, 0), other = otherNP, blendType = 'easeInOut')), name = trackName)
            self.doorExitTrack.start(ts)
        else:
            self.notify.warning('exitDoorEnterOpening(): did not find leftDoor')

    
    def exitDoorExitOpening(self):
        pass

    
    def exitDoorEnterOpen(self, ts):
        for avatarID in self.avatarExitIDList:
            avatar = self.cr.doId2do.get(avatarID)
            if avatar:
                track = self.avatarExitTrack(avatar, 0.20000000000000001)
                track.start()
                self.avatarExitTracks.append(track)
            
        
        self.avatarExitIDList = []

    
    def exitDoorExitOpen(self):
        for track in self.avatarExitTracks:
            track.finish()
        
        self.avatarExitTracks = []

    
    def findDoorNode(self, string, allowEmpty = False):
        building = self.getBuilding()
        foundNode = building.find('**/door_' + str(self.doorIndex) + '/**/' + string + '*;+s+i')
        if foundNode.isEmpty():
            foundNode = building.find('**/' + string + '*;+s+i')
        
        if allowEmpty:
            return foundNode
        
        return foundNode

    
    def hideIfHasFlat(self, node):
        if self.bHasFlat:
            node.hide()
        


