# File: E (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.interval.IntervalGlobal import *
from toontown.safezone import SafeZoneLoader
import whrandom
from toontown.launcher import DownloadForceAcknowledge
import House
import Estate
import HouseGlobals
import random
from toontown.coghq import MovingPlatform
from direct.directnotify import DirectNotifyGlobal

class EstateLoader(SafeZoneLoader.SafeZoneLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('EstateLoader')
    
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        del self.fsm
        self.fsm = ClassicFSM.ClassicFSM('EstateLoader', [
            State.State('start', self.enterStart, self.exitStart, [
                'quietZone',
                'estate',
                'house']),
            State.State('estate', self.enterEstate, self.exitEstate, [
                'quietZone']),
            State.State('house', self.enterHouse, self.exitHouse, [
                'quietZone']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'house',
                'estate']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.mid'
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.mid'
        self.dnaFile = 'phase_5.5/dna/estate_1.dna'
        self.safeZoneStorageDNAFile = None
        self.id = MyEstate
        self.estateOwnerId = None
        self.branchZone = None
        self.houseDoneEvent = 'houseDone'
        self.estateDoneEvent = 'estateDone'
        self.enteredHouse = None
        self.houseNode = [
            None] * 6
        self.houseModels = [
            None] * HouseGlobals.NUM_HOUSE_TYPES
        self.houseId2house = { }
        self.barrel = None
        self.clouds = []
        self.cloudTrack = None
        self.sunMoonNode = None
        self.fsm.enterInitialState()

    
    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.music = base.loadMusic('phase_4/audio/bgm/TC_nbrhood.mid')
        self.underwaterSound = base.loadSfx('phase_4/audio/sfx/AV_ambient_water.mp3')
        self.swimSound = base.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.mp3')
        self.submergeSound = base.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.mp3')
        self.birdSound = map(base.loadSfx, [
            'phase_4/audio/sfx/SZ_TC_bird1.mp3',
            'phase_4/audio/sfx/SZ_TC_bird2.mp3',
            'phase_4/audio/sfx/SZ_TC_bird3.mp3'])
        self.cricketSound = map(base.loadSfx, [
            'phase_4/audio/sfx/SZ_TC_bird1.mp3',
            'phase_4/audio/sfx/SZ_TC_bird2.mp3',
            'phase_4/audio/sfx/SZ_TC_bird3.mp3'])
        if base.goonsEnabled:
            invModel = loader.loadModel('phase_3.5/models/gui/inventory_icons')
            self.invModels = []
            ToontownBattleGlobals = ToontownBattleGlobals
            import toontown.toonbase
            for track in range(len(ToontownBattleGlobals.AvPropsNew)):
                itemList = []
                for item in range(len(ToontownBattleGlobals.AvPropsNew[track])):
                    itemList.append(invModel.find('**/' + ToontownBattleGlobals.AvPropsNew[track][item]))
                
                self.invModels.append(itemList)
            
            invModel.removeNode()
            del invModel
        

    
    def unload(self):
        self.ignoreAll()
        base.cr.estateMgr.leaveEstate()
        self.estateOwnerId = None
        self.estateZoneId = None
        if self.place:
            self.place.exit()
            self.place.unload()
            del self.place
        
        del self.underwaterSound
        del self.swimSound
        del self.submergeSound
        del self.birdSound
        del self.cricketSound
        for node in self.houseNode:
            node.removeNode()
        
        del self.houseNode
        for model in self.houseModels:
            model.removeNode()
        
        del self.houseModels
        del self.houseId2house
        if self.sunMoonNode:
            self.sunMoonNode.removeNode()
            del self.sunMoonNode
            self.sunMoonNode = None
        
        if self.clouds:
            for cloud in self.clouds:
                cloud[0].removeNode()
                cloud[0].destroy()
                del cloud[1]
            
            del self.clouds
        
        if self.barrel:
            self.barrel.removeNode()
        
        SafeZoneLoader.SafeZoneLoader.unload(self)

    
    def enter(self, requestStatus):
        self.estateOwnerId = requestStatus.get('ownerId', base.localAvatar.doId)
        base.localAvatar.inEstate = 1
        if base.cloudPlatformsEnabled:
            self.loadCloudPlatforms()
        
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    
    def exit(self):
        self.ignoreAll()
        if not wantOtpServer:
            base.cr.disableAll()
        
        base.cr.cache.flush()
        base.localAvatar.stopChat()
        base.localAvatar.inEstate = 0
        SafeZoneLoader.SafeZoneLoader.exit(self)

    
    def createSafeZone(self, dnaFile):
        SafeZoneLoader.SafeZoneLoader.createSafeZone(self, dnaFile)
        self.loadHouses()
        self.loadSunMoon()

    
    def loadHouses(self):
        for i in range(HouseGlobals.NUM_HOUSE_TYPES):
            self.houseModels[i] = loader.loadModel(HouseGlobals.houseModels[i])
        
        for i in range(6):
            posHpr = HouseGlobals.houseDrops[i]
            self.houseNode[i] = self.geom.attachNewNode('esHouse_' + str(i))
            self.houseNode[i].setPosHpr(*posHpr)
        

    
    def loadSunMoon(self):
        self.sun = loader.loadModel('phase_4/models/props/sun.bam')
        self.moon = loader.loadModel('phase_5.5/models/props/moon.bam')
        self.sunMoonNode = self.geom.attachNewNode('sunMoon')
        self.sunMoonNode.setPosHpr(0, 0, 0, 0, 0, 0)
        if self.sun:
            self.sun.reparentTo(self.sunMoonNode)
            self.sun.setY(270)
            self.sun.setScale(2)
            self.sun.setBillboardPointEye()
        
        if self.moon:
            self.moon.setP(180)
            self.moon.reparentTo(self.sunMoonNode)
            self.moon.setY(-270)
            self.moon.setScale(15)
            self.moon.setBillboardPointEye()
        
        self.sunMoonNode.setP(30)

    
    def enterEstate(self, requestStatus):
        self.notify.debug('enterEstate: requestStatus = %s' % requestStatus)
        ownerId = requestStatus.get('ownerId')
        if ownerId:
            self.estateOwnerId = ownerId
        
        zoneId = requestStatus['zoneId']
        self.notify.debug('enterEstate, ownerId = %s, zoneId = %s' % (self.estateOwnerId, zoneId))
        self.accept(self.estateDoneEvent, self.handleEstateDone)
        self.place = Estate.Estate(self, self.estateOwnerId, zoneId, self.fsm.getStateNamed('estate'), self.estateDoneEvent)
        base.cr.playGame.setPlace(self.place)
        self.place.load()
        self.place.enter(requestStatus)
        self.estateZoneId = zoneId

    
    def exitEstate(self):
        self.notify.debug('exitEstate')
        self.ignore(self.estateDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)
        base.cr.cache.flush()

    
    def handleEstateDone(self, doneStatus = None):
        if not doneStatus:
            doneStatus = self.place.getDoneStatus()
        
        how = doneStatus['how']
        shardId = doneStatus['shardId']
        hoodId = doneStatus['hoodId']
        zoneId = doneStatus['zoneId']
        avId = doneStatus.get('avId', -1)
        ownerId = doneStatus.get('ownerId', -1)
        if shardId != None or hoodId != MyEstate:
            self.notify.debug('estate done, and we are backing out to a different hood/shard')
            self.notify.debug('hoodId = %s, avId = %s' % (hoodId, avId))
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
            return None
        
        if how in [
            'tunnelIn',
            'teleportIn',
            'doorIn',
            'elevatorIn']:
            self.notify.debug('staying in estateloader')
            self.fsm.request('quietZone', [
                doneStatus])
        else:
            self.notify.error('Exited hood with unexpected mode %s' % how)

    
    def enterHouse(self, requestStatus):
        ownerId = requestStatus.get('ownerId')
        if ownerId:
            self.estateOwnerId = ownerId
        
        self.acceptOnce(self.houseDoneEvent, self.handleHouseDone)
        self.place = House.House(self, self.estateOwnerId, self.fsm.getStateNamed('house'), self.houseDoneEvent)
        base.cr.playGame.setPlace(self.place)
        self.place.load()
        self.place.enter(requestStatus)

    
    def exitHouse(self):
        self.ignore(self.houseDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)

    
    def handleHouseDone(self, doneStatus = None):
        if not doneStatus:
            doneStatus = self.place.getDoneStatus()
        
        shardId = doneStatus['shardId']
        hoodId = doneStatus['hoodId']
        if shardId != None or hoodId != MyEstate:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
            return None
        
        how = doneStatus['how']
        if how in [
            'tunnelIn',
            'teleportIn',
            'doorIn',
            'elevatorIn']:
            self.fsm.request('quietZone', [
                doneStatus])
        else:
            self.notify.error('Exited hood with unexpected mode %s' % how)

    
    def handleQuietZoneDone(self):
        status = base.cr.handlerArgs
        self.fsm.request(status['where'], [
            status])

    
    def atMyEstate(self):
        if self.estateOwnerId != None:
            if self.estateOwnerId == base.localAvatar.getDoId():
                return 1
            else:
                return 0
        else:
            self.notify.warning("We aren't in an estate")

    
    def setHouse(self, houseId):
        
        try:
            houseDo = base.cr.doId2do[houseId]
            self.enteredHouse = houseDo.house
        except KeyError:
            self.notify.debug("can't find house: %d" % houseId)


    
    def startCloudPlatforms(self):
        if len(self.clouds):
            self.cloudTrack = self._EstateLoader__cloudTrack()
            self.cloudTrack.loop()
        

    
    def stopCloudPlatforms(self):
        if self.cloudTrack:
            self.cloudTrack.pause()
            del self.cloudTrack
            self.cloudTrack = None
        

    
    def _EstateLoader__cloudTrack(self):
        track = Parallel()
        for cloud in self.clouds:
            axis = cloud[1]
            pos = cloud[0].getPos(render)
            newPos = pos + axis * 30
            reversePos = pos - axis * 30
            track.append(Sequence(LerpPosInterval(cloud[0], 10, newPos), LerpPosInterval(cloud[0], 20, reversePos), LerpPosInterval(cloud[0], 10, pos)))
        
        return track

    
    def loadCloudPlatforms(self):
        self.cloudOrigin = self.geom.attachNewNode('cloudOrigin')
        self.cloudOrigin.setZ(30)
        self.numClouds = 10
        dTheta = 2.0 * math.pi / self.numClouds
        cloudModel = loader.loadModel('phase_4/models/minigames/block')
        fog = loader.loadModel('phase_8/models/props/test_clouds')
        axes = [
            Vec3(1, 0, 0),
            Vec3(0, 1, 0),
            Vec3(0, 0, 1)]
        for i in range(self.numClouds):
            cloud = MovingPlatform.MovingPlatform()
            cloud.setupCopyModel(i, cloudModel)
            cloud.reparentTo(self.cloudOrigin)
            cloud.setPos(40 * math.cos(i * dTheta), 40 * math.sin(i * dTheta), 4 * random.random())
            colSphere = CollisionSphere(0, 0, 0, 3.5)
            colSphere.setTangible(0)
            colNode = CollisionNode('cloudSphere-' + str(i))
            colNode.addSolid(colSphere)
            colSphereNode = cloud.attachNewNode(colNode)
            colSphereNode.setZ(-3)
            self.clouds.append([
                cloud,
                random.choice(axes)])
        
        del fog


