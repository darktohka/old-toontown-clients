# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.battle.BattleProps import *
from toontown.battle.BattleSounds import *
from toontown.distributed.ToontownMsgTypes import *
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import cleanupDialog
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import Place
from direct.showbase import PandaObject
from direct.fsm import StateData
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task import Task
import TownBattle
from toontown.toon import Toon
from toontown.battle import BattleParticles
from direct.fsm import StateData
from toontown.building import ToonInterior
from toontown.hood import QuietZoneState
from toontown.hood import ZoneUtil
from direct.interval.IntervalGlobal import *

class TownLoader(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownLoader')
    
    def __init__(self, hood, parentFSMState, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.hood = hood
        self.parentFSMState = parentFSMState
        self.fsm = ClassicFSM.ClassicFSM('TownLoader', [
            State.State('start', self.enterStart, self.exitStart, [
                'quietZone',
                'street',
                'toonInterior']),
            State.State('street', self.enterStreet, self.exitStreet, [
                'quietZone']),
            State.State('toonInterior', self.enterToonInterior, self.exitToonInterior, [
                'quietZone']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'street',
                'toonInterior']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.branchZone = None
        self.canonicalBranchZone = None
        self.placeDoneEvent = 'placeDone'
        self.townBattleDoneEvent = 'town-battle-done'

    
    def loadBattleAnims(self):
        Toon.loadBattleAnims()

    
    def unloadBattleAnims(self):
        Toon.unloadBattleAnims()

    
    def load(self, zoneId):
        self.zoneId = zoneId
        self.parentFSMState.addChild(self.fsm)
        self.loadBattleAnims()
        self.branchZone = ZoneUtil.getBranchZone(zoneId)
        self.canonicalBranchZone = ZoneUtil.getCanonicalBranchZone(zoneId)
        self.music = base.loadMusic(self.musicFile)
        self.activityMusic = base.loadMusic(self.activityMusicFile)
        self.battleMusic = base.loadMusic('phase_3.5/audio/bgm/encntr_general_bg.mid')
        self.townBattle = TownBattle.TownBattle(self.townBattleDoneEvent)
        self.townBattle.load()

    
    def unload(self):
        self.unloadBattleAnims()
        globalPropPool.unloadProps()
        globalBattleSoundCache.clear()
        BattleParticles.unloadParticles()
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        del self.fsm
        del self.streetClass
        self.landmarkBlocks.removeNode()
        del self.landmarkBlocks
        self.hood.dnaStore.resetSuitPoints()
        self.hood.dnaStore.resetBattleCells()
        del self.hood
        del self.nodeDict
        del self.zoneDict
        del self.fadeInDict
        del self.fadeOutDict
        del self.nodeList
        self.geom.removeNode()
        del self.geom
        self.townBattle.unload()
        self.townBattle.cleanup()
        del self.townBattle
        del self.battleMusic
        del self.music
        del self.activityMusic
        del self.holidayPropTransforms
        self.deleteAnimatedProps()
        cleanupDialog('globalDialog')
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        self.setState(requestStatus['where'], requestStatus)

    
    def exit(self):
        self.ignoreAll()

    
    def setState(self, stateName, requestStatus):
        self.fsm.request(stateName, [
            requestStatus])

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterStreet(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.streetDone)
        self.place = self.streetClass(self, self.fsm, self.placeDoneEvent)
        self.place.load()
        base.cr.playGame.setPlace(self.place)
        self.place.enter(requestStatus)

    
    def exitStreet(self):
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)

    
    def streetDone(self):
        self.requestStatus = self.place.doneStatus
        status = self.place.doneStatus
        if status['loader'] == 'townLoader' and ZoneUtil.getBranchZone(status['zoneId']) == self.branchZone and status['shardId'] == None:
            self.fsm.request('quietZone', [
                status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)

    
    def enterToonInterior(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.handleToonInteriorDone)
        self.place = ToonInterior.ToonInterior(self, self.fsm.getStateNamed('toonInterior'), self.placeDoneEvent)
        base.cr.playGame.setPlace(self.place)
        self.place.load()
        self.place.enter(requestStatus)

    
    def exitToonInterior(self):
        self.ignore(self.placeDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)

    
    def handleToonInteriorDone(self):
        status = self.place.doneStatus
        if ZoneUtil.getBranchZone(status['zoneId']) == self.branchZone and status['shardId'] == None:
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
        status = base.cr.handlerArgs
        self.fsm.request(status['where'], [
            status])

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def createHood(self, dnaFile, loadStorage = 1):
        if loadStorage:
            loader.loadDNAFile(self.hood.dnaStore, 'phase_5/dna/storage_town.dna')
            loader.loadDNAFile(self.hood.dnaStore, self.townStorageDNAFile)
        
        node = loader.loadDNAFile(self.hood.dnaStore, dnaFile)
        if node.getNumParents() == 1:
            self.geom = NodePath(node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries(self.hood.dnaStore)
        self.reparentLandmarkBlockNodes()
        self.renameFloorPolys(self.nodeList)
        self.createAnimatedProps(self.nodeList)
        self.holidayPropTransforms = { }
        npl = self.geom.findAllMatches('**/=DNARoot=holiday_prop')
        for i in range(npl.getNumPaths()):
            np = npl.getPath(i)
            np.setTag('transformIndex', `i`)
            self.holidayPropTransforms[i] = np.getNetTransform()
        
        self.geom.flattenMedium()
        gsg = base.win.getGsg()
        if gsg:
            self.geom.prepareScene(gsg)
        
        self.geom.setName('town_top_level')

    
    def reparentLandmarkBlockNodes(self):
        bucket = hidden.attachNewNode('landmarkBlocks')
        self.landmarkBlocks = hidden.attachNewNode('landmarkBlocks')
        npc = self.geom.findAllMatches('**/sb*:*_landmark_*_DNARoot')
        for i in range(npc.getNumPaths()):
            nodePath = npc.getPath(i)
            nodePath.wrtReparentTo(bucket)
        

    
    def makeDictionaries(self, dnaStore):
        self.nodeDict = { }
        self.zoneDict = { }
        self.nodeList = []
        self.fadeInDict = { }
        self.fadeOutDict = { }
        a1 = Vec4(1, 1, 1, 1)
        a0 = Vec4(1, 1, 1, 0)
        numVisGroups = dnaStore.getNumDNAVisGroups()
        for i in range(numVisGroups):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            groupName = base.cr.hoodMgr.extractGroupName(groupFullName)
            zoneId = int(groupName)
            zoneId = ZoneUtil.getTrueZoneId(zoneId, self.zoneId)
            groupNode = self.geom.find('**/' + groupFullName)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            elif ':' in groupName:
                groupName = '%s%s' % (zoneId, groupName[groupName.index(':'):])
            else:
                groupName = '%s' % zoneId
            groupNode.setName(groupName)
            self.nodeDict[zoneId] = []
            self.nodeList.append(groupNode)
            self.zoneDict[zoneId] = groupNode
            fadeDuration = 0.5
            self.fadeOutDict[groupNode] = Sequence(Func(groupNode.setTransparency, 1), LerpColorScaleInterval(groupNode, fadeDuration, a0, startColorScale = a1), Func(groupNode.clearColorScale), Func(groupNode.clearTransparency), Func(groupNode.stash), name = 'fadeZone-' + str(zoneId), autoPause = 1)
            self.fadeInDict[groupNode] = Sequence(Func(groupNode.unstash), Func(groupNode.setTransparency, 1), LerpColorScaleInterval(groupNode, fadeDuration, a1, startColorScale = a0), Func(groupNode.clearColorScale), Func(groupNode.clearTransparency), name = 'fadeZone-' + str(zoneId), autoPause = 1)
        
        for i in range(numVisGroups):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            zoneId = int(base.cr.hoodMgr.extractGroupName(groupFullName))
            zoneId = ZoneUtil.getTrueZoneId(zoneId, self.zoneId)
            for j in range(dnaStore.getNumVisiblesInDNAVisGroup(i)):
                visName = dnaStore.getVisibleName(i, j)
                groupName = base.cr.hoodMgr.extractGroupName(visName)
                nextZoneId = int(groupName)
                nextZoneId = ZoneUtil.getTrueZoneId(nextZoneId, self.zoneId)
                visNode = self.zoneDict[nextZoneId]
                self.nodeDict[zoneId].append(visNode)
            
        
        self.hood.dnaStore.resetPlaceNodes()
        self.hood.dnaStore.resetDNAGroups()
        self.hood.dnaStore.resetDNAVisGroups()
        self.hood.dnaStore.resetDNAVisGroupsAI()

    
    def renameFloorPolys(self, nodeList):
        for i in nodeList:
            collNodePaths = i.findAllMatches('**/+CollisionNode')
            numCollNodePaths = collNodePaths.getNumPaths()
            visGroupName = i.node().getName()
            for j in range(numCollNodePaths):
                collNodePath = collNodePaths.getPath(j)
                bitMask = collNodePath.node().getIntoCollideMask()
                if bitMask.getBit(1):
                    collNodePath.node().setName(visGroupName)
                
            
        

    
    def createAnimatedProps(self, nodeList):
        self.animPropDict = { }
        for i in nodeList:
            animPropNodes = i.findAllMatches('**/animated_prop_*')
            numAnimPropNodes = animPropNodes.getNumPaths()
            for j in range(numAnimPropNodes):
                animPropNode = animPropNodes.getPath(j)
                className = animPropNode.getName()[14:-8]
                symbols = { }
                base.cr.importModule(symbols, 'toontown.hood', [
                    className])
                classObj = getattr(symbols[className], className)
                animPropObj = classObj(animPropNode)
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
        


