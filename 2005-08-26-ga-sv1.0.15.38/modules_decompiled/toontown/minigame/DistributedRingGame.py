# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.interval.IntervalGlobal import *
from DistributedMinigame import *
from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task import Task
import ArrowKeys
import Ring
import RingTrack
import RingGameGlobals
import RingGroup
import RingTrackGroups
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class DistributedRingGame(DistributedMinigame):
    UPDATE_ENVIRON_TASK = 'RingGameUpdateEnvironTask'
    UPDATE_LOCALTOON_TASK = 'RingGameUpdateLocalToonTask'
    UPDATE_RINGS_TASK = 'RingGameUpdateRingsTask'
    UPDATE_SHADOWS_TASK = 'RingGameUpdateShadowsTask'
    COLLISION_DETECTION_TASK = 'RingGameCollisionDetectionTask'
    END_GAME_WAIT_TASK = 'RingGameCollisionDetectionTask'
    COLLISION_DETECTION_PRIORITY = 5
    UPDATE_SHADOWS_PRIORITY = 47
    RT_UNKNOWN = 0
    RT_SUCCESS = 1
    RT_GROUPSUCCESS = 2
    RT_FAILURE = 3
    
    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)
        self.gameFSM = ClassicFSM.ClassicFSM('DistributedRingGame', [
            State.State('off', self.enterOff, self.exitOff, [
                'swim']),
            State.State('swim', self.enterSwim, self.exitSwim, [
                'cleanup']),
            State.State('cleanup', self.enterCleanup, self.exitCleanup, [])], 'off', 'cleanup')
        self.addChildGameFSM(self.gameFSM)

    
    def getTitle(self):
        return TTLocalizer.RingGameTitle

    
    def getInstructions(self):
        p = self.avIdList.index(self.localAvId)
        if self.isSinglePlayer():
            text = TTLocalizer.RingGameInstructionsSinglePlayer
        else:
            text = TTLocalizer.RingGameInstructionsMultiPlayer
        return text % RingGameGlobals.ringColors[self.colorIndices[p]][0]

    
    def getMaxDuration(self):
        return RingGameGlobals.NUM_RING_GROUPS * self.ringGroupArrivalPeriod + self.T_FIRST_RING_GROUP_ARRIVES + self.GAME_END_DELAY

    
    def defineConstants(self):
        self.CAMERA_Y = -15
        self.TOON_Y = 0
        self.FAR_PLANE_DIST = 150
        tScreenCenterToEdge = 1.0
        self.TOONXZ_SPEED = RingGameGlobals.MAX_TOONXZ / tScreenCenterToEdge
        self.WATER_DEPTH = 35.0
        self.ENVIRON_LENGTH = 150.0
        self.ENVIRON_START_OFFSET = 20.0
        self.TOON_INITIAL_SPACING = 4.0
        waterZOffset = 3.0
        self.SEA_FLOOR_Z = -(self.WATER_DEPTH) / 2.0 + waterZOffset
        farPlaneDist = self.CAMERA_Y + self.FAR_PLANE_DIST - self.TOON_Y
        self.ringGroupArrivalPeriod = 3.0
        self.RING_GROUP_SPACING = farPlaneDist / 2.0
        self.TOON_SWIM_VEL = self.RING_GROUP_SPACING / self.ringGroupArrivalPeriod
        self.T_FIRST_RING_GROUP_ARRIVES = farPlaneDist / self.TOON_SWIM_VEL
        self.WATER_COLOR = Vec4(0, 0, 0.59999999999999998, 1)
        self.SHADOW_Z_OFFSET = 0.10000000000000001
        self.Y_VIS_MAX = self.FAR_PLANE_DIST
        self.Y_VIS_MIN = self.CAMERA_Y
        ringRadius = RingGameGlobals.RING_RADIUS * 1.0249999999999999
        self.RING_RADIUS_SQRD = ringRadius * ringRadius
        self.GAME_END_DELAY = 1.0
        self.RING_RESPONSE_DELAY = 0.10000000000000001
        self.TOON_LOD = 1000
        self.NumRingGroups = 16

    
    def load(self):
        self.notify.debug('load')
        DistributedMinigame.load(self)
        self.defineConstants()
        self.music = base.loadMusic('phase_4/audio/bgm/MG_toontag.mid')
        self.sndAmbience = base.loadSfx('phase_4/audio/sfx/AV_ambient_water.mp3')
        self.sndPerfect = base.loadSfx('phase_4/audio/sfx/ring_perfect.mp3')
        loadBase = 'phase_4/models/minigames/'
        self.environModel = loader.loadModel(loadBase + 'swimming_game.bam')
        self.environModel.setPos(0, self.ENVIRON_LENGTH / 2.0, self.SEA_FLOOR_Z)
        self.environModel.flattenMedium()
        self.ringModel = loader.loadModel(loadBase + 'swimming_game_ring.bam')
        self.ringModel.setTransparency(1)
        modelRadius = 4.0
        self.ringModel.setScale(RingGameGlobals.RING_RADIUS / modelRadius)
        self.ringModel.flattenMedium()
        self.dropShadowModel = loader.loadModel('phase_3/models/props/drop_shadow')
        self.dropShadowModel.setColor(0, 0, 0, 0.5)
        self.dropShadowModel.flattenMedium()
        self.toonDropShadows = []
        self.ringDropShadows = []
        self._DistributedRingGame__textGen = TextNode('ringGame')
        self._DistributedRingGame__textGen.setFont(ToontownGlobals.getSignFont())
        self._DistributedRingGame__textGen.setAlign(TextNode.ACenter)

    
    def unload(self):
        self.notify.debug('unload')
        DistributedMinigame.unload(self)
        del self._DistributedRingGame__textGen
        del self.toonDropShadows
        del self.ringDropShadows
        self.dropShadowModel.removeNode()
        del self.dropShadowModel
        self.environModel.removeNode()
        del self.environModel
        self.ringModel.removeNode()
        del self.ringModel
        del self.music
        del self.sndAmbience
        del self.sndPerfect
        self.removeChildGameFSM(self.gameFSM)
        del self.gameFSM

    
    def onstage(self):
        self.notify.debug('onstage')
        DistributedMinigame.onstage(self)
        self.arrowKeys = ArrowKeys.ArrowKeys()
        toon = base.localAvatar
        toon.reparentTo(render)
        toon.setAnimState('swim', 1.0)
        toon.stopBobSwimTask()
        toon.useLOD(self.TOON_LOD)
        self._DistributedRingGame__placeToon(self.localAvId)
        toon.dropShadow.hide()
        camera.reparentTo(render)
        camera.reparentTo(base.localAvatar)
        camera.setPosHpr(0, self.CAMERA_Y + self.TOON_Y, 0, 0, 0, 0)
        base.camLens.setFov(80)
        base.camLens.setFar(self.FAR_PLANE_DIST)
        base.setBackgroundColor(self.WATER_COLOR)
        self._DistributedRingGame__fog = Fog('ringGameFog')
        if base.wantFog:
            self._DistributedRingGame__fog.setColor(self.WATER_COLOR)
            self._DistributedRingGame__fog.setLinearRange(0.10000000000000001, self.FAR_PLANE_DIST - 1.0)
            render.setFog(self._DistributedRingGame__fog)
        
        self.environNode = render.attachNewNode('environNode')
        self.environBlocks = []
        for i in range(0, 2):
            instance = self.environModel.instanceUnderNode(self.environNode, 'model')
            y = self.ENVIRON_LENGTH * i
            instance.setY(y)
            self.environBlocks.append(instance)
            for j in range(0, 2):
                instance = self.environModel.instanceUnderNode(self.environNode, 'blocks')
                x = self.ENVIRON_LENGTH * (j + 1)
                instance.setY(y)
                instance.setX(-x)
                self.environBlocks.append(instance)
            
            for j in range(0, 2):
                instance = self.environModel.instanceUnderNode(self.environNode, 'blocks')
                x = self.ENVIRON_LENGTH * (j + 1)
                instance.setY(y)
                instance.setX(x)
                self.environBlocks.append(instance)
            
        
        self.ringNode = render.attachNewNode('ringNode')
        self.sndTable = {
            'gotRing': [
                None] * self.numPlayers,
            'missedRing': [
                None] * self.numPlayers }
        for i in range(0, self.numPlayers):
            self.sndTable['gotRing'][i] = base.loadSfx('phase_4/audio/sfx/ring_get.mp3')
            self.sndTable['missedRing'][i] = base.loadSfx('phase_4/audio/sfx/ring_miss.mp3')
        
        self._DistributedRingGame__addToonDropShadow(self.getAvatar(self.localAvId))
        self._DistributedRingGame__spawnUpdateEnvironTask()
        self._DistributedRingGame__spawnUpdateShadowsTask()
        self._DistributedRingGame__spawnUpdateLocalToonTask()
        base.playMusic(self.music, looping = 0, volume = 0.80000000000000004)
        if None != self.sndAmbience:
            base.playSfx(self.sndAmbience, looping = 1, volume = 0.80000000000000004)
        

    
    def offstage(self):
        self.notify.debug('offstage')
        DistributedMinigame.offstage(self)
        self.music.stop()
        if None != self.sndAmbience:
            self.sndAmbience.stop()
        
        self._DistributedRingGame__killUpdateLocalToonTask()
        self._DistributedRingGame__killUpdateShadowsTask()
        self._DistributedRingGame__killUpdateEnvironTask()
        del self.sndTable
        self._DistributedRingGame__removeAllToonDropShadows()
        render.clearFog()
        base.camLens.setFar(ToontownGlobals.DefaultCameraFar)
        base.camLens.setFov(ToontownGlobals.DefaultCameraFov)
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
        self.arrowKeys.destroy()
        del self.arrowKeys
        for block in self.environBlocks:
            del block
        
        self.environNode.removeNode()
        del self.environNode
        self.ringNode.removeNode()
        del self.ringNode
        for avId in self.avIdList:
            av = self.getAvatar(avId)
            if av:
                av.dropShadow.show()
                av.resetLOD()
                av.setAnimState('neutral', 1.0)
            
        

    
    def handleDisabledAvatar(self, avId):
        self.notify.debug('handleDisabledAvatar')
        self.notify.debug('avatar ' + str(avId) + ' disabled')
        self._DistributedRingGame__removeToonDropShadow(self.remoteToons[avId])
        DistributedMinigame.handleDisabledAvatar(self, avId)

    
    def _DistributedRingGame__genText(self, text):
        self._DistributedRingGame__textGen.setText(text)
        return self._DistributedRingGame__textGen.generate()

    
    def _DistributedRingGame__placeToon(self, avId):
        toon = self.getAvatar(avId)
        i = self.avIdList.index(avId)
        numToons = float(self.numPlayers)
        x = i * self.TOON_INITIAL_SPACING
        x -= self.TOON_INITIAL_SPACING * (numToons - 1) / 2.0
        toon.setPosHpr(x, self.TOON_Y, 0, 0, 0, 0)

    
    def setGameReady(self):
        if not (self.hasLocalToon):
            return None
        
        self.notify.debug('setGameReady')
        if DistributedMinigame.setGameReady(self):
            return None
        
        if not self.isSinglePlayer():
            base.localAvatar.collisionsOff()
            cSphere = CollisionSphere(0.0, 0.0, 0.0, RingGameGlobals.CollisionRadius)
            cSphereNode = CollisionNode('RingGameSphere-%s' % self.localAvId)
            cSphereNode.addSolid(cSphere)
            cSphereNode.setFromCollideMask(RingGameGlobals.CollideMask)
            cSphereNode.setIntoCollideMask(BitMask32.allOff())
            self.cSphereNodePath = base.localAvatar.attachNewNode(cSphereNode)
            self.pusher = CollisionHandlerPusher()
            self.pusher.addCollider(self.cSphereNodePath, base.localAvatar)
            self.pusher.setHorizontal(0)
            self.cTrav = CollisionTraverser('DistributedRingGame')
            self.cTrav.addCollider(self.cSphereNodePath, self.pusher)
            self.remoteToonCollNPs = { }
            for avId in self.remoteAvIdList:
                toon = self.getAvatar(avId)
                if toon:
                    cSphere = CollisionSphere(0.0, 0.0, 0.0, RingGameGlobals.CollisionRadius)
                    cSphereNode = CollisionNode('RingGameSphere-%s' % avId)
                    cSphereNode.addSolid(cSphere)
                    cSphereNode.setCollideMask(RingGameGlobals.CollideMask)
                    cSphereNP = toon.attachNewNode(cSphereNode)
                    self.remoteToonCollNPs[avId] = cSphereNP
                
            
        
        for avId in self.remoteAvIdList:
            toon = self.getAvatar(avId)
            if toon:
                toon.reparentTo(render)
                self._DistributedRingGame__placeToon(avId)
                toon.setAnimState('swim', 1.0)
                toon.stopBobSwimTask()
                toon.useLOD(self.TOON_LOD)
                toon.dropShadow.hide()
                self._DistributedRingGame__addToonDropShadow(toon)
                toon.startSmooth()
            
        
        self.remoteToons = { }
        for avId in self.remoteAvIdList:
            toon = self.getAvatar(avId)
            self.remoteToons[avId] = toon
        
        self._DistributedRingGame__nextRingGroupResultIndex = 0

    
    def setGameStart(self, timestamp):
        if not (self.hasLocalToon):
            return None
        
        self.notify.debug('setGameStart')
        DistributedMinigame.setGameStart(self, timestamp)
        self.gameFSM.request('swim')

    
    def enterOff(self):
        self.notify.debug('enterOff')

    
    def exitOff(self):
        pass

    
    def enterSwim(self):
        self.notify.debug('enterSwim')
        self._DistributedRingGame__ringTimeBase = self.gameStartTime
        self._DistributedRingGame__numRingGroups = RingGameGlobals.NUM_RING_GROUPS
        self._DistributedRingGame__ringGroupsPassed = 0
        self._DistributedRingGame__generateRings()
        self._DistributedRingGame__spawnUpdateRingsTask()
        self._DistributedRingGame__spawnCollisionDetectionTask()
        self._DistributedRingGame__ringTracks = []
        self.colorRing = self.ringModel.copyTo(hidden)
        self.colorRing.reparentTo(aspect2d)
        self.colorRing.setTwoSided(0)
        self.colorRing.setPos(1.1899999999999999, 10, -0.85999999999999999)
        self.colorRing.setScale(0.040000000000000001)
        p = self.avIdList.index(self.localAvId)
        self.colorRing.setColor(RingGameGlobals.ringColors[self.colorIndices[p]][1])
        self.resultTable = [
            self.RT_UNKNOWN] * self._DistributedRingGame__numRingGroups
        self._DistributedRingGame__initTallyDisplay()

    
    def _DistributedRingGame__initTallyDisplay(self):
        self._DistributedRingGame__tallyTextNode = TextNode('tally')
        self._DistributedRingGame__tallyTextNode.setFont(ToontownGlobals.getSignFont())
        self._DistributedRingGame__tallyTextNode.setAlign(TextNode.ACenter)
        self.tallyMarkers = [
            None] * self._DistributedRingGame__numRingGroups
        for i in range(0, self._DistributedRingGame__numRingGroups):
            self._DistributedRingGame__createTallyMarker(i, self.RT_UNKNOWN)
        

    
    def _DistributedRingGame__destroyTallyDisplay(self):
        for i in range(0, self._DistributedRingGame__numRingGroups):
            self._DistributedRingGame__deleteTallyMarker(i)
        
        del self.tallyMarkers
        del self._DistributedRingGame__tallyTextNode

    
    def _DistributedRingGame__createTallyMarker(self, index, result):
        chars = '-OOX'
        colors = (Point4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1), Point4(0, 1, 0, 1), Point4(1, 1, 0, 1), Point4(1, 0, 0, 1))
        self._DistributedRingGame__deleteTallyMarker(index)
        self._DistributedRingGame__tallyTextNode.setText(chars[result])
        node = self._DistributedRingGame__tallyTextNode.generate()
        tallyText = aspect2d.attachNewNode(node)
        tallyText.setColor(colors[result])
        tallyText.setScale(0.10000000000000001)
        zOffset = 0
        if result == self.RT_UNKNOWN:
            zOffset = 0.014999999999999999
        
        xSpacing = 0.085000000000000006
        tallyText.setPos(-1.0 + xSpacing * index, 0, -0.93000000000000005 + zOffset)
        self.tallyMarkers[index] = tallyText

    
    def _DistributedRingGame__deleteTallyMarker(self, index):
        marker = self.tallyMarkers[index]
        if None != marker:
            marker.removeNode()
            self.tallyMarkers[index] = None
        

    
    def _DistributedRingGame__updateTallyDisplay(self, index):
        self._DistributedRingGame__createTallyMarker(index, self.resultTable[index])

    
    def _DistributedRingGame__generateRings(self):
        self.ringGroups = []
        difficultyDistributions = {
            ToontownGlobals.ToontownCentral: [
                14,
                2,
                0],
            ToontownGlobals.DonaldsDock: [
                10,
                6,
                0],
            ToontownGlobals.DaisyGardens: [
                4,
                12,
                0],
            ToontownGlobals.MinniesMelodyland: [
                4,
                8,
                4],
            ToontownGlobals.TheBrrrgh: [
                4,
                6,
                6],
            ToontownGlobals.DonaldsDreamland: [
                2,
                6,
                8] }
        for distr in difficultyDistributions.values():
            sum = reduce(lambda x, y: x + y, distr)
        
        difficultyPatterns = {
            ToontownGlobals.ToontownCentral: [
                [
                    0] * 14 + [
                    1] * 2 + [
                    2] * 0,
                [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1] * 2,
                [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    1]],
            ToontownGlobals.DonaldsDock: [
                [
                    0] * 10 + [
                    1] * 6 + [
                    2] * 0,
                [
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    1,
                    1] * 2,
                [
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    1,
                    1] * 2],
            ToontownGlobals.DaisyGardens: [
                [
                    0] * 4 + [
                    1] * 12 + [
                    2] * 0,
                [
                    0,
                    0,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1] * 2,
                [
                    0,
                    1,
                    1,
                    1,
                    0,
                    1,
                    1,
                    1] * 2],
            ToontownGlobals.MinniesMelodyland: [
                [
                    0] * 4 + [
                    1] * 8 + [
                    2] * 4,
                [
                    0,
                    0,
                    1,
                    1,
                    1,
                    1,
                    2,
                    2] * 2,
                [
                    0,
                    1,
                    1,
                    1,
                    1,
                    0,
                    2,
                    2] * 2,
                [
                    0,
                    1,
                    1,
                    2,
                    0,
                    1,
                    1,
                    2] * 2,
                [
                    0,
                    1,
                    2,
                    1,
                    0,
                    1,
                    2,
                    1] * 2],
            ToontownGlobals.TheBrrrgh: [
                [
                    0] * 4 + [
                    1] * 6 + [
                    2] * 6,
                [
                    0,
                    0,
                    1,
                    1,
                    1,
                    2,
                    2,
                    2] * 2,
                [
                    0,
                    1,
                    1,
                    1,
                    0,
                    2,
                    2,
                    2] * 2,
                [
                    0,
                    1,
                    1,
                    2,
                    0,
                    1,
                    2,
                    2] * 2,
                [
                    0,
                    1,
                    2,
                    1,
                    0,
                    1,
                    2,
                    2] * 2],
            ToontownGlobals.DonaldsDreamland: [
                [
                    0] * 2 + [
                    1] * 6 + [
                    2] * 8,
                [
                    0,
                    1,
                    1,
                    1,
                    2,
                    2,
                    2,
                    2] * 2,
                [
                    0,
                    1,
                    1,
                    2,
                    2,
                    1,
                    2,
                    2] * 2,
                [
                    0,
                    1,
                    2,
                    1,
                    2,
                    1,
                    2,
                    2] * 2] }
        safezone = self.getSafezoneId()
        numGroupsPerDifficulty = difficultyDistributions[safezone]
        
        def patternsAreValid(difficultyPatterns = difficultyPatterns, difficultyDistributions = difficultyDistributions):
            for sz in difficultyPatterns.keys():
                for pattern in difficultyPatterns[sz]:
                    for difficulty in [
                        0,
                        1,
                        2]:
                        numGroupsPerDifficulty = difficultyDistributions[sz]
                        if numGroupsPerDifficulty[difficulty] != pattern.count(difficulty):
                            print 'safezone:', sz
                            print 'pattern:', pattern
                            print 'difficulty:', difficulty
                            print 'expected %s %ss, found %s' % (numGroupsPerDifficulty[difficulty], difficulty, pattern.count(difficulty))
                            return 0
                        
                    
                
            
            return 1

        pattern = self.randomNumGen.choice(difficultyPatterns[self.getSafezoneId()])
        for i in range(0, self._DistributedRingGame__numRingGroups):
            numRings = self.numPlayers
            trackGroup = RingTrackGroups.getRandomRingTrackGroup(pattern[i], numRings, self.randomNumGen)
            ringGroup = RingGroup.RingGroup(trackGroup, self.ringModel, RingGameGlobals.MAX_TOONXZ, self.colorIndices)
            for r in range(numRings):
                self._DistributedRingGame__addRingDropShadow(ringGroup.getRing(r))
            
            self.ringGroups.append(ringGroup)
            ringGroup.reparentTo(self.ringNode)
            firstGroupOffset = self.TOON_Y + self.T_FIRST_RING_GROUP_ARRIVES * self.TOON_SWIM_VEL
            ringGroup.setY(i * self.RING_GROUP_SPACING + firstGroupOffset)
        

    
    def _DistributedRingGame__destroyRings(self):
        for group in self.ringGroups:
            group.delete()
            group.removeNode()
        
        self._DistributedRingGame__removeAllRingDropShadows()
        del self.ringGroups

    
    def _DistributedRingGame__spawnUpdateLocalToonTask(self):
        self._DistributedRingGame__initPosBroadcast()
        taskMgr.remove(self.UPDATE_LOCALTOON_TASK)
        taskMgr.add(self._DistributedRingGame__updateLocalToonTask, self.UPDATE_LOCALTOON_TASK)

    
    def _DistributedRingGame__killUpdateLocalToonTask(self):
        taskMgr.remove(self.UPDATE_LOCALTOON_TASK)

    
    def _DistributedRingGame__initPosBroadcast(self):
        self._DistributedRingGame__posBroadcastPeriod = 0.10000000000000001
        self._DistributedRingGame__timeSinceLastPosBroadcast = 0.0
        self._DistributedRingGame__lastPosBroadcast = self.getAvatar(self.localAvId).getPos()
        self._DistributedRingGame__storeStop = 0
        lt = self.getAvatar(self.localAvId)
        lt.d_clearSmoothing()
        lt.sendCurrentPosition()

    
    def _DistributedRingGame__posBroadcast(self, dt):
        self._DistributedRingGame__timeSinceLastPosBroadcast += dt
        if self._DistributedRingGame__timeSinceLastPosBroadcast > self._DistributedRingGame__posBroadcastPeriod:
            self._DistributedRingGame__timeSinceLastPosBroadcast -= self._DistributedRingGame__posBroadcastPeriod
            self.getAvatar(self.localAvId).cnode.broadcastPosHprFull()
        

    
    def _DistributedRingGame__updateLocalToonTask(self, task):
        dt = globalClock.getDt()
        toonPos = self.getAvatar(self.localAvId).getPos()
        pos = [
            toonPos[0],
            0,
            toonPos[2]]
        xVel = 0.0
        if self.arrowKeys.leftPressed():
            xVel -= self.TOONXZ_SPEED
        
        if self.arrowKeys.rightPressed():
            xVel += self.TOONXZ_SPEED
        
        pos[0] += xVel * dt
        if pos[0] < -(RingGameGlobals.MAX_TOONXZ):
            pos[0] = -(RingGameGlobals.MAX_TOONXZ)
        
        if pos[0] > RingGameGlobals.MAX_TOONXZ:
            pos[0] = RingGameGlobals.MAX_TOONXZ
        
        zVel = 0.0
        if self.arrowKeys.upPressed():
            zVel += self.TOONXZ_SPEED
        
        if self.arrowKeys.downPressed():
            zVel -= self.TOONXZ_SPEED
        
        pos[2] += zVel * dt
        if pos[2] < -(RingGameGlobals.MAX_TOONXZ):
            pos[2] = -(RingGameGlobals.MAX_TOONXZ)
        
        if pos[2] > RingGameGlobals.MAX_TOONXZ:
            pos[2] = RingGameGlobals.MAX_TOONXZ
        
        self.getAvatar(self.localAvId).setPos(pos[0], self.TOON_Y, pos[2])
        if hasattr(self, 'cTrav'):
            self.cTrav.traverse(render)
        
        self._DistributedRingGame__posBroadcast(dt)
        return Task.cont

    
    def exitSwim(self):
        for track in self._DistributedRingGame__ringTracks:
            track.finish()
        
        del self._DistributedRingGame__ringTracks
        self.colorRing.removeNode()
        del self.colorRing
        self._DistributedRingGame__destroyTallyDisplay()
        del self.resultTable
        taskMgr.remove(self.END_GAME_WAIT_TASK)
        self._DistributedRingGame__killUpdateRingsTask()
        self._DistributedRingGame__killCollisionDetectionTask()
        self._DistributedRingGame__destroyRings()

    
    def enterCleanup(self):
        self.notify.debug('enterCleanup')
        if not self.isSinglePlayer():
            for np in self.remoteToonCollNPs.values():
                np.removeNode()
            
            del self.remoteToonCollNPs
            self.cSphereNodePath.removeNode()
            del self.cSphereNodePath
            del self.pusher
            del self.cTrav
            base.localAvatar.collisionsOn()
        

    
    def exitCleanup(self):
        pass

    
    def _DistributedRingGame__addDropShadow_INTERNAL(self, object, scale_x, scale_y, scale_z, list):
        shadow = self.dropShadowModel.copyTo(render)
        shadow.setPos(0, self.CAMERA_Y, -100)
        shadow.setScale(scale_x, scale_y, scale_z)
        list.append([
            shadow,
            object])

    
    def _DistributedRingGame__removeDropShadow_INTERNAL(self, object, list):
        for i in range(len(list)):
            entry = list[i]
            if entry[1] == object:
                entry[0].removeNode()
                list.pop(i)
                return None
            
        
        self.notify.warning('parent object ' + str(object) + ' not found in drop shadow list!')

    
    def _DistributedRingGame__addToonDropShadow(self, object):
        self._DistributedRingGame__addDropShadow_INTERNAL(object, 0.5, 0.5, 0.5, self.toonDropShadows)

    
    def _DistributedRingGame__removeToonDropShadow(self, object):
        self._DistributedRingGame__removeDropShadow_INTERNAL(object, self.toonDropShadows)

    
    def _DistributedRingGame__addRingDropShadow(self, object):
        self._DistributedRingGame__addDropShadow_INTERNAL(object, 1.2, 0.31, 1.0, self.ringDropShadows)

    
    def _DistributedRingGame__removeRingDropShadow(self, object):
        self._DistributedRingGame__removeDropShadow_INTERNAL(object, self.ringDropShadows)

    
    def _DistributedRingGame__removeAllToonDropShadows(self):
        for entry in self.toonDropShadows:
            entry[0].removeNode()
        
        self.toonDropShadows = []

    
    def _DistributedRingGame__removeAllRingDropShadows(self):
        for entry in self.ringDropShadows:
            entry[0].removeNode()
        
        self.ringDropShadows = []

    
    def _DistributedRingGame__spawnUpdateShadowsTask(self):
        taskMgr.remove(self.UPDATE_SHADOWS_TASK)
        taskMgr.add(self._DistributedRingGame__updateShadowsTask, self.UPDATE_SHADOWS_TASK, priority = self.UPDATE_SHADOWS_PRIORITY)

    
    def _DistributedRingGame__killUpdateShadowsTask(self):
        taskMgr.remove(self.UPDATE_SHADOWS_TASK)

    
    def _DistributedRingGame__updateShadowsTask(self, task):
        list = self.toonDropShadows + self.ringDropShadows
        for entry in list:
            object = entry[1]
            y = object.getY(render)
            if y > self.Y_VIS_MAX:
                continue
            
            x = object.getX(render)
            z = self.SEA_FLOOR_Z + self.SHADOW_Z_OFFSET
            shadow = entry[0]
            shadow.setPos(x, y, z)
        
        return Task.cont

    
    def _DistributedRingGame__spawnUpdateEnvironTask(self):
        taskMgr.remove(self.UPDATE_ENVIRON_TASK)
        taskMgr.add(self._DistributedRingGame__updateEnvironTask, self.UPDATE_ENVIRON_TASK)

    
    def _DistributedRingGame__killUpdateEnvironTask(self):
        taskMgr.remove(self.UPDATE_ENVIRON_TASK)

    
    def _DistributedRingGame__updateEnvironTask(self, task):
        t = globalClock.getFrameTime() - self._DistributedRingGame__timeBase
        distance = t * self.TOON_SWIM_VEL
        distance %= self.ENVIRON_LENGTH
        distance += self.ENVIRON_START_OFFSET
        self.environNode.setY(-distance)
        return Task.cont

    
    def _DistributedRingGame__spawnUpdateRingsTask(self):
        taskMgr.remove(self.UPDATE_RINGS_TASK)
        taskMgr.add(self._DistributedRingGame__updateRingsTask, self.UPDATE_RINGS_TASK)

    
    def _DistributedRingGame__killUpdateRingsTask(self):
        taskMgr.remove(self.UPDATE_RINGS_TASK)

    
    def _DistributedRingGame__updateRingsTask(self, task):
        t = globalClock.getFrameTime() - self._DistributedRingGame__ringTimeBase
        distance = t * self.TOON_SWIM_VEL
        self.ringNode.setY(-distance)
        for ringGroup in self.ringGroups:
            groupY = ringGroup.getY(render)
            if groupY <= self.Y_VIS_MAX and groupY >= self.Y_VIS_MIN:
                ringGroup.setT(t)
            
        
        return Task.cont

    
    def _DistributedRingGame__spawnCollisionDetectionTask(self):
        self._DistributedRingGame__ringGroupsPassed = 0
        taskMgr.remove(self.COLLISION_DETECTION_TASK)
        taskMgr.add(self._DistributedRingGame__collisionDetectionTask, self.COLLISION_DETECTION_TASK, priority = self.COLLISION_DETECTION_PRIORITY)

    
    def _DistributedRingGame__killCollisionDetectionTask(self):
        taskMgr.remove(self.COLLISION_DETECTION_TASK)

    
    def _DistributedRingGame__makeRingSuccessFadeTrack(self, ring, duration, endScale, ringIndex):
        targetScale = Point3(endScale, endScale, endScale)
        dFade = 0.5 * duration
        dColorChange = duration - dFade
        origColor = ring.getColor()
        targetColor = Point4(1.0 - origColor[0], 1.0 - origColor[1], 1.0 - origColor[2], 1)
        
        def colorChangeFunc(t, ring = ring, targetColor = targetColor, origColor = origColor):
            newColor = targetColor * t + origColor * (1.0 - t)
            ring.setColor(newColor)

        
        def fadeFunc(t, ring = ring):
            ring.setColorScale(1, 1, 1, 1.0 - t)

        fadeAwayTrack = Parallel(Sequence(LerpFunctionInterval(colorChangeFunc, fromData = 0.0, toData = 1.0, duration = dColorChange), LerpFunctionInterval(fadeFunc, fromData = 0.0, toData = 1.0, duration = dFade)), LerpScaleInterval(ring, duration, targetScale))
        successTrack = Sequence(Wait(self.RING_RESPONSE_DELAY), Parallel(SoundInterval(self.sndTable['gotRing'][ringIndex]), Sequence(Func(ring.wrtReparentTo, render), fadeAwayTrack, Func(self._DistributedRingGame__removeRingDropShadow, ring), Func(ring.reparentTo, hidden))))
        return successTrack

    
    def _DistributedRingGame__makeRingFailureFadeTrack(self, ring, duration, ringIndex):
        ts = 0.01
        targetScale = Point3(ts, ts, ts)
        missedTextNode = self._DistributedRingGame__genText(TTLocalizer.RingGameMissed)
        missedText = hidden.attachNewNode(missedTextNode)
        ringColor = RingGameGlobals.ringColors[self.colorIndices[ringIndex]][1]
        
        def addMissedText(ring = ring, ringColor = ringColor, missedText = missedText):
            missedText.reparentTo(render)
            missedText.setPos(ring.getPos(render) + Point3(0, -1, 0))
            missedText.setColor(ringColor)

        
        def removeMissedText(missedText = missedText):
            missedText.removeNode()
            missedText = None

        failureTrack = Sequence(Wait(self.RING_RESPONSE_DELAY), Parallel(SoundInterval(self.sndTable['missedRing'][ringIndex]), Sequence(Func(ring.wrtReparentTo, render), Func(addMissedText), LerpScaleInterval(ring, duration, targetScale, blendType = 'easeIn'), Func(removeMissedText), Func(self._DistributedRingGame__removeRingDropShadow, ring), Func(ring.reparentTo, hidden))))
        return failureTrack

    
    def _DistributedRingGame__makeRingFadeAway(self, ring, success, ringIndex):
        if success:
            track = self._DistributedRingGame__makeRingSuccessFadeTrack(ring, 0.5, 2.0, ringIndex)
        else:
            track = self._DistributedRingGame__makeRingFailureFadeTrack(ring, 0.5, ringIndex)
        self._DistributedRingGame__ringTracks.append(track)
        track.start()

    
    def _DistributedRingGame__collisionDetectionTask(self, task):
        nextRingGroupIndex = self._DistributedRingGame__ringGroupsPassed
        nextRingGroup = self.ringGroups[nextRingGroupIndex]
        if nextRingGroup.getY(render) < 0:
            groupIndex = nextRingGroupIndex
            gotRing = 0
            ourRing = nextRingGroup.getRing(self.avIdList.index(self.localAvId))
            ringPos = ourRing.getPos(render)
            localToonPos = base.localAvatar.getPos(render)
            distX = localToonPos[0] - ringPos[0]
            distZ = localToonPos[2] - ringPos[2]
            distSqrd = distX * distX + distZ * distZ
            if distSqrd <= self.RING_RADIUS_SQRD:
                gotRing = 1
            
            self._DistributedRingGame__makeRingFadeAway(ourRing, gotRing, self.avIdList.index(self.localAvId))
            if gotRing:
                self.resultTable[groupIndex] = self.RT_SUCCESS
            else:
                self.resultTable[groupIndex] = self.RT_FAILURE
            self._DistributedRingGame__updateTallyDisplay(groupIndex)
            self.sendUpdate('setToonGotRing', [
                gotRing])
            if self.isSinglePlayer():
                self._DistributedRingGame__processRingGroupResults([
                    gotRing])
            
            self._DistributedRingGame__ringGroupsPassed += 1
            if self._DistributedRingGame__ringGroupsPassed >= self._DistributedRingGame__numRingGroups:
                self._DistributedRingGame__killCollisionDetectionTask()
            
        
        return Task.cont

    
    def _DistributedRingGame__endGameDolater(self, task):
        self.gameOver()
        return Task.done

    
    def setTimeBase(self, timestamp):
        if not (self.hasLocalToon):
            return None
        
        self._DistributedRingGame__timeBase = globalClockDelta.networkToLocalTime(timestamp)

    
    def setColorIndices(self, a, b, c, d):
        if not (self.hasLocalToon):
            return None
        
        self.colorIndices = [
            a,
            b,
            c,
            d]

    
    def _DistributedRingGame__getSuccessTrack(self, groupIndex):
        
        def makeSuccessTrack(text, holdDuration, fadeDuration = 0.5, perfect = 0, self = self):
            successText = hidden.attachNewNode(self._DistributedRingGame__genText(text))
            successText.setScale(0.25)
            successText.setColor(1, 1, 0.5, 1)
            
            def fadeFunc(t, text):
                text.setColorScale(1, 1, 1, 1.0 - t)

            
            def destroyText(text):
                text.removeNode()
                text = None

            track = Sequence(Func(successText.reparentTo, aspect2d), Wait(holdDuration), LerpFunctionInterval(fadeFunc, extraArgs = [
                successText], fromData = 0.0, toData = 1.0, duration = fadeDuration, blendType = 'easeIn'), Func(destroyText, successText))
            if perfect:
                track = Parallel(track, SoundInterval(self.sndPerfect))
            
            return track

        
        def isPerfect(list, goodValues):
            for value in list:
                if value not in goodValues:
                    return 0
                
            
            return 1

        if groupIndex >= self._DistributedRingGame__numRingGroups - 1:
            if not self.isSinglePlayer():
                if isPerfect(self.resultTable, [
                    self.RT_GROUPSUCCESS]):
                    return makeSuccessTrack(TTLocalizer.RingGameGroupPerfect, 1.5, perfect = 1)
                
            
            if isPerfect(self.resultTable, [
                self.RT_SUCCESS,
                self.RT_GROUPSUCCESS]):
                return makeSuccessTrack(TTLocalizer.RingGamePerfect, 1.5, perfect = 1)
            
            return Wait(1.0)
        
        if not self.isSinglePlayer():
            if self.resultTable[groupIndex] == self.RT_GROUPSUCCESS:
                return makeSuccessTrack(TTLocalizer.RingGameGroupBonus, 0.0, fadeDuration = 0.40000000000000002)
            
        
        return None

    
    def _DistributedRingGame__processRingGroupResults(self, results):
        groupIndex = self._DistributedRingGame__nextRingGroupResultIndex
        ringGroup = self.ringGroups[self._DistributedRingGame__nextRingGroupResultIndex]
        self._DistributedRingGame__nextRingGroupResultIndex += 1
        for i in range(0, self.numPlayers):
            if self.avIdList[i] != self.localAvId:
                ring = ringGroup.getRing(i)
                self._DistributedRingGame__makeRingFadeAway(ring, results[i], i)
            
        
        if not self.isSinglePlayer():
            if not (0 in results):
                self.notify.debug('Everyone got their rings!!')
                self.resultTable[groupIndex] = self.RT_GROUPSUCCESS
                self._DistributedRingGame__updateTallyDisplay(groupIndex)
            
        
        successTrack = self._DistributedRingGame__getSuccessTrack(groupIndex)
        endGameTrack = None
        if groupIndex >= self._DistributedRingGame__numRingGroups - 1:
            
            def endTheGame(self = self):
                if not (RingGameGlobals.ENDLESS_GAME):
                    taskMgr.doMethodLater(self.GAME_END_DELAY, self._DistributedRingGame__endGameDolater, self.END_GAME_WAIT_TASK)
                

            endGameTrack = Func(endTheGame)
        
        if None != successTrack or None != endGameTrack:
            track = Sequence()
            if None != successTrack:
                track.append(Wait(self.RING_RESPONSE_DELAY))
                track.append(successTrack)
            
            if None != endGameTrack:
                track.append(endGameTrack)
            
            self._DistributedRingGame__ringTracks.append(track)
            track.start()
        

    
    def setRingGroupResults(self, bitfield):
        if not (self.hasLocalToon):
            return None
        
        if self.gameFSM.getCurrentState().getName() != 'swim':
            return None
        
        results = []
        mask = 1
        for avId in self.avIdList:
            results.append(not (bitfield & mask))
            mask <<= 1
        
        self._DistributedRingGame__processRingGroupResults(results)


