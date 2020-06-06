# File: E (Python 2.2)

from ShowBaseGlobal import *
from ToontownMsgTypes import *
from ToontownGlobals import *
from DirectGui import *
from IntervalGlobal import *
import DirectNotifyGlobal
import Place
import PandaObject
import StateData
import FSM
import State
import Task
import Toon
import StateData
import House
import QuietZoneState
import ZoneUtil
import SkyUtil
import Estate
import HouseGlobals

class EstateLoader(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('EstateLoader')
    
    def __init__(self, parentFSMState, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.parentFSMState = parentFSMState
        self.place = None
        self.fsm = FSM.FSM('EstateLoader', [
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
        self.id = MyEstate
        self.estateOwnerId = None
        self.branchZone = None
        self.houseDoneEvent = 'houseDone'
        self.estateDoneEvent = 'estateDone'
        self.estateDNAFile = 'phase_5.5/dna/estate_1.dna'
        self.estateStorageDNAFile = 'phase_5.5/dna/storage_estate.dna'
        self.popupInfo = None
        self.enteredHouse = None
        self.fsm.enterInitialState()

    
    def load(self, requestStatus):
        self.sky = loader.loadModel('phase_3.5/models/props/TT_sky')
        self.sky.setFogOff()
        self.underwaterSound = base.loadSfx('phase_4/audio/sfx/AV_ambient_water.mp3')
        self.swimSound = base.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.mp3')
        self.submergeSound = base.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.mp3')
        self.createEstate(self.estateDNAFile)
        self.parentFSMState.addChild(self.fsm)

    
    def unload(self):
        self.ignoreAll()
        toonbase.tcr.estateMgr.leaveEstate()
        self.estateOwnerId = None
        self.estateZoneId = None
        self.parentFSMState.removeChild(self.fsm)
        self.stopSky()
        self.sky.removeNode()
        del self.sky
        del self.parentFSMState
        del self.fsm
        del self.place
        del self.underwaterSound
        del self.swimSound
        del self.submergeSound
        self.dnaStore.resetNodes()
        self.dnaStore.resetTextures()
        del self.dnaStore
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def enter(self, requestStatus):
        self.estateOwnerId = requestStatus.get('ownerId', toonbase.localToon.doId)
        self.setState(requestStatus['where'], requestStatus)
        self.accept('kickToPlayground', self.kickToPlayground)

    
    def exit(self):
        self.ignoreAll()
        toonbase.localToon.stopChat()

    
    def setState(self, stateName, requestStatus):
        self.fsm.request(stateName, [
            requestStatus])

    
    def createEstate(self, dnaFile):
        self.dnaStore = DNAStorage()
        self.dnaStore.storeFont('humanist', getInterfaceFont())
        self.dnaStore.storeFont('mickey', getSignFont())
        loader.loadDNAFile(self.dnaStore, self.estateStorageDNAFile)
        self.notify.debug('Loading dnaFile = %s ' % dnaFile)
        node = loader.loadDNAFile(self.dnaStore, dnaFile)
        if node.getNumParents() == 1:
            self.geom = NodePath(node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries(self.dnaStore)
        self.createAnimatedProps(self.nodeList)
        self.geom.flattenMedium()
        self.geom.prepareScene(base.win.getGsg())

    
    def makeDictionaries(self, dnaStore):
        self.nodeList = []
        self.notify.debug('numVis Groups = %s' % dnaStore.getNumDNAVisGroups())
        self.notify.debug('num panda nodes = %s' % dnaStore.getNumPandaNodes())
        self.notify.debug('panda nodes = %s' % dnaStore.printPandaNodes())
        for i in range(dnaStore.getNumDNAVisGroups()):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            self.notify.debug('%s: group Full name = %s' % (i, groupFullName))
            groupName = toonbase.tcr.hoodMgr.extractGroupName(groupFullName)
            groupNode = self.geom.find('**/' + groupFullName)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            
            self.nodeList.append(groupNode)
        
        self.dnaStore.resetPlaceNodes()
        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()

    
    def createAnimatedProps(self, nodeList):
        self.animPropDict = { }
        for i in nodeList:
            animPropNodes = i.findAllMatches('**/animated_prop_*')
            numAnimPropNodes = animPropNodes.getNumPaths()
            for j in range(numAnimPropNodes):
                self.notify.debug('animProp %s' % j)
                animPropNode = animPropNodes.getPath(j)
                className = animPropNode.getName()[14:-8]
                exec 'import %s' % className
                animPropObj = eval('%s.%s(animPropNode)' % (className, className))
                animPropList = self.animPropDict.setdefault(i, [])
                animPropList.append(animPropObj)
            
        

    
    def deleteAnimatedProps(self):
        for (zoneNode, animPropList) in self.animPropDict.items():
            for animProp in animPropList:
                animProp.delete()
            
        
        del self.animPropDict

    
    def enterAnimatedProps(self, zoneNode):
        for animProp in self.animPropDict.get(zoneNode, ()):
            animProp.enter()
        

    
    def exitAnimatedProps(self, zoneNode):
        for animProp in self.animPropDict.get(zoneNode, ()):
            animProp.exit()
        

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterEstate(self, requestStatus):
        self.notify.debug('enterEstate: requestStatus = %s' % requestStatus)
        ownerId = requestStatus.get('ownerId')
        if ownerId:
            self.estateOwnerId = ownerId
        
        zoneId = requestStatus['zoneId']
        self.notify.debug('enterEstate, ownerId = %s, zoneId = %s' % (self.estateOwnerId, zoneId))
        self.place = Estate.Estate(self, self.estateOwnerId, zoneId, self.fsm.getStateNamed('estate'), self.estateDoneEvent)
        toonbase.tcr.playGame.setPlace(self.place)
        self.accept(self.estateDoneEvent, self.handleEstateDone)
        self.place.load()
        self.place.enter(requestStatus)
        self.estateZoneId = zoneId

    
    def exitEstate(self):
        self.notify.debug('exitEstate')
        self.ignore(self.estateDoneEvent)
        self.place.exit()
        self.place.unload()
        toonbase.tcr.cache.flush()

    
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
        toonbase.tcr.playGame.setPlace(self.place)
        self.place.load()
        self.place.enter(requestStatus)

    
    def exitHouse(self):
        self.ignore(self.houseDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        toonbase.tcr.playGame.setPlace(self.place)

    
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

    
    def enterQuietZone(self, requestStatus):
        self.quietZoneDoneEvent = 'quietZoneDone'
        self.acceptOnce(self.quietZoneDoneEvent, self.handleQuietZoneDone)
        self.quietZoneStateData = QuietZoneState.QuietZoneState(self.quietZoneDoneEvent)
        self.quietZoneStateData.load()
        self.quietZoneStateData.enter(requestStatus)

    
    def exitQuietZone(self):
        self.ignore(self.quietZoneDoneEvent)
        del self.quietZoneDoneEvent
        self.quietZoneStateData.exit()
        self.quietZoneStateData.unload()
        self.quietZoneStateData = None

    
    def handleQuietZoneDone(self):
        status = toonbase.tcr.handlerArgs
        self.fsm.request(status['where'], [
            status])

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def startSky(self):
        SkyUtil.startCloudSky(self)

    
    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)

    
    def stopSky(self):
        self.notify.debug('stopSky')
        taskMgr.remove('skyTrack')
        self.sky.reparentTo(hidden)

    
    def kickToPlayground(self, retCode):
        if retCode == 0:
            msg = Localizer.EstateOwnerLeftMessage % HouseGlobals.BOOT_GRACE_PERIOD
            self._EstateLoader__popupKickoutMessage(msg)
        elif retCode == 1:
            zoneId = toonbase.localToon.lastHood
            self.doneStatus = {
                'loader': ZoneUtil.getBranchLoaderName(zoneId),
                'where': ZoneUtil.getToonWhereName(zoneId),
                'how': 'teleportIn',
                'hoodId': zoneId,
                'zoneId': zoneId,
                'shardId': None,
                'avId': -1 }
            messenger.send(self.doneEvent, [
                self.doneStatus])
        elif retCode == 2:
            zoneId = toonbase.localToon.lastHood
            self.doneStatus = {
                'loader': ZoneUtil.getBranchLoaderName(zoneId),
                'where': ZoneUtil.getToonWhereName(zoneId),
                'how': 'teleportIn',
                'hoodId': zoneId,
                'zoneId': zoneId,
                'shardId': None,
                'avId': -1 }
            messenger.send(self.doneEvent, [
                self.doneStatus])
        else:
            self.notify.error('unknown reason for exiting estate')

    
    def _EstateLoader__popupKickoutMessage(self, msg):
        if self.popupInfo != None:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        self.popupInfo = DirectFrame(parent = hidden, relief = None, state = 'normal', text = msg, frameSize = (-1, 1, -1, 1), text_wordwrap = 10, geom = getDefaultDialogGeom(), geom_color = GlobalDialogColor, geom_scale = (0.88, 1, 0.75), geom_pos = (0, 0, -0.080000000000000002), text_scale = 0.080000000000000002, text_pos = (0, 0.10000000000000001))
        DirectButton(self.popupInfo, image = okButtonImage, relief = None, text = Localizer.EstatePopupOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.29999999999999999), command = self._EstateLoader__handleKickoutOk)
        buttons.removeNode()
        self.popupInfo.reparentTo(aspect2d)

    
    def _EstateLoader__handleKickoutOk(self):
        self.popupInfo.reparentTo(hidden)

    
    def atMyEstate(self):
        if self.estateOwnerId != None:
            if self.estateOwnerId == toonbase.localToon.getDoId():
                return 1
            else:
                return 0
        else:
            self.notify.warning("We aren't in an estate")

    
    def setHouse(self, houseId):
        
        try:
            houseDo = toonbase.tcr.doId2do[houseId]
            self.enteredHouse = houseDo.house
        except KeyError:
            self.notify.debug("can't find house: %d" % houseId)



