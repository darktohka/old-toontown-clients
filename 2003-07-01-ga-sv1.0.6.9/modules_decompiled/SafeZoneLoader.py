# File: S (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from ToontownMsgTypes import *
import ZoneUtil
import DirectNotifyGlobal
import Place
import PandaObject
import StateData
import FSM
import State
import Task
import DownloadForceAcknowledge
import HealthForceAcknowledge
import TutorialForceAcknowledge
from ToontownGlobals import *
import ToonInterior
import QuietZoneState

class SafeZoneLoader(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('SafeZoneLoader')
    
    def __init__(self, hood, parentFSMState, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.hood = hood
        self.parentFSMState = parentFSMState
        self.fsm = FSM.FSM('SafeZoneLoader', [
            State.State('start', self.enterStart, self.exitStart, [
                'quietZone',
                'playground',
                'toonInterior']),
            State.State('playground', self.enterPlayground, self.exitPlayground, [
                'quietZone']),
            State.State('toonInterior', self.enterToonInterior, self.exitToonInterior, [
                'quietZone']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'playground',
                'toonInterior']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.placeDoneEvent = 'placeDone'
        self.place = None

    
    def load(self):
        self.music = base.loadMusic(self.musicFile)
        self.activityMusic = base.loadMusic(self.activityMusicFile)
        self.createSafeZone(self.dnaFile)
        self.parentFSMState.addChild(self.fsm)

    
    def unload(self):
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        self.geom.removeNode()
        del self.geom
        del self.fsm
        del self.hood
        del self.nodeList
        del self.playgroundClass
        del self.music
        del self.activityMusic
        self.deleteAnimatedProps()
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        messenger.send('enterSafeZone')
        self.setState(requestStatus['where'], requestStatus)

    
    def exit(self):
        messenger.send('exitSafeZone')

    
    def setState(self, stateName, requestStatus):
        self.fsm.request(stateName, [
            requestStatus])

    
    def createSafeZone(self, dnaFile):
        loader.loadDNAFile(self.hood.dnaStore, self.safeZoneStorageDNAFile)
        node = loader.loadDNAFile(self.hood.dnaStore, dnaFile)
        if node.getNumParents() == 1:
            self.geom = NodePath(node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries(self.hood.dnaStore)
        self.createAnimatedProps(self.nodeList)
        self.geom.flattenMedium()
        self.geom.prepareScene(base.win.getGsg())

    
    def makeDictionaries(self, dnaStore):
        self.nodeList = []
        for i in range(dnaStore.getNumDNAVisGroups()):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            groupName = toonbase.tcr.hoodMgr.extractGroupName(groupFullName)
            groupNode = self.geom.find('**/' + groupFullName)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            
            self.nodeList.append(groupNode)
        
        self.removeLandmarkBlockNodes()
        self.hood.dnaStore.resetPlaceNodes()
        self.hood.dnaStore.resetDNAGroups()
        self.hood.dnaStore.resetDNAVisGroups()
        self.hood.dnaStore.resetDNAVisGroupsAI()

    
    def removeLandmarkBlockNodes(self):
        npc = self.geom.findAllMatches('**/suit_building_origin')
        for i in range(npc.getNumPaths()):
            npc.getPath(i).removeNode()
        

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterPlayground(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.handlePlaygroundDone)
        self.place = self.playgroundClass(self, self.fsm, self.placeDoneEvent)
        self.place.load()
        self.place.enter(requestStatus)
        toonbase.tcr.playGame.setPlace(self.place)

    
    def exitPlayground(self):
        self.ignore(self.placeDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        toonbase.tcr.playGame.setPlace(self.place)

    
    def handlePlaygroundDone(self):
        status = self.place.doneStatus
        if ZoneUtil.getBranchZone(status['zoneId']) == self.hood.id and status['shardId'] == None:
            self.fsm.request('quietZone', [
                status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)

    
    def enterToonInterior(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.handleToonInteriorDone)
        self.place = ToonInterior.ToonInterior(self, self.fsm.getStateNamed('toonInterior'), self.placeDoneEvent)
        toonbase.tcr.playGame.setPlace(self.place)
        self.place.load()
        self.place.enter(requestStatus)

    
    def exitToonInterior(self):
        self.ignore(self.placeDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        toonbase.tcr.playGame.setPlace(self.place)

    
    def handleToonInteriorDone(self):
        status = self.place.doneStatus
        if ZoneUtil.getBranchZone(status['zoneId']) == self.hood.id and status['shardId'] == None:
            self.fsm.request('quietZone', [
                status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)

    
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
        if status['where'] == 'estate':
            self.doneStatus = status
            messenger.send(self.doneEvent)
        else:
            self.fsm.request(status['where'], [
                status])

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def createAnimatedProps(self, nodeList):
        self.animPropDict = { }
        for i in nodeList:
            animPropNodes = i.findAllMatches('**/animated_prop_*')
            numAnimPropNodes = animPropNodes.getNumPaths()
            for j in range(numAnimPropNodes):
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
        


