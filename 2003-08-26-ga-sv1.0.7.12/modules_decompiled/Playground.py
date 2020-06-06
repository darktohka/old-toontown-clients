# File: P (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
import DirectNotifyGlobal
import Place
import PandaObject
import StateData
import FSM
import State
import Task
import DeathForceAcknowledge
import HealthForceAcknowledge
import TutorialForceAcknowledge
import NPCForceAcknowledge
import Trolley
import ToontownDialog
import ToontownGlobals
import Localizer
import DirectLabel

class Playground(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('Playground')
    
    def __init__(self, loader, parentFSM, doneEvent):
        Place.Place.__init__(self, loader, doneEvent)
        self.tfaDoneEvent = 'tfaDoneEvent'
        self.fsm = FSM.FSM('Playground', [
            State.State('start', self.enterStart, self.exitStart, [
                'walk',
                'deathAck',
                'doorIn',
                'tunnelIn']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'sit',
                'stickerBook',
                'TFA',
                'DFA',
                'trolley',
                'final',
                'doorOut',
                'options',
                'quest',
                'purchase',
                'phone',
                'fishing']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk',
                'DFA',
                'TFA']),
            State.State('sit', self.enterSit, self.exitSit, [
                'walk',
                'DFA']),
            State.State('trolley', self.enterTrolley, self.exitTrolley, [
                'walk']),
            State.State('doorIn', self.enterDoorIn, self.exitDoorIn, [
                'walk']),
            State.State('doorOut', self.enterDoorOut, self.exitDoorOut, [
                'walk']),
            State.State('TFA', self.enterTFA, self.exitTFA, [
                'TFAReject',
                'DFA']),
            State.State('TFAReject', self.enterTFAReject, self.exitTFAReject, [
                'walk']),
            State.State('DFA', self.enterDFA, self.exitDFA, [
                'DFAReject',
                'NPCFA',
                'HFA']),
            State.State('DFAReject', self.enterDFAReject, self.exitDFAReject, [
                'walk']),
            State.State('NPCFA', self.enterNPCFA, self.exitNPCFA, [
                'NPCFAReject',
                'HFA']),
            State.State('NPCFAReject', self.enterNPCFAReject, self.exitNPCFAReject, [
                'walk']),
            State.State('HFA', self.enterHFA, self.exitHFA, [
                'HFAReject',
                'teleportOut',
                'tunnelOut']),
            State.State('HFAReject', self.enterHFAReject, self.exitHFAReject, [
                'walk']),
            State.State('deathAck', self.enterDeathAck, self.exitDeathAck, [
                'teleportIn']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk',
                'popup']),
            State.State('popup', self.enterPopup, self.exitPopup, [
                'walk']),
            State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, [
                'deathAck']),
            State.State('tunnelIn', self.enterTunnelIn, self.exitTunnelIn, [
                'walk']),
            State.State('tunnelOut', self.enterTunnelOut, self.exitTunnelOut, [
                'final']),
            State.State('quest', self.enterQuest, self.exitQuest, [
                'walk']),
            State.State('purchase', self.enterPurchase, self.exitPurchase, [
                'walk']),
            State.State('phone', self.enterPhone, self.exitPhone, [
                'walk']),
            State.State('fishing', self.enterFishing, self.exitFishing, [
                'walk']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.parentFSM = parentFSM
        self.tunnelOriginList = []
        self.trolleyDoneEvent = 'trolleyDone'
        self.hfaDoneEvent = 'hfaDoneEvent'
        self.npcfaDoneEvent = 'npcfaDoneEvent'
        self.dialog = None
        self.deathAckBox = None

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        messenger.send('enterPlayground')
        self.accept('doorDoneEvent', self.handleDoorDoneEvent)
        self.accept('DistributedDoor_doorTrigger', self.handleDoorTrigger)
        base.playMusic(self.loader.music, looping = 1, volume = 0.80000000000000004)
        self.loader.geom.reparentTo(render)
        for i in self.loader.nodeList:
            self.loader.enterAnimatedProps(i)
        
        self.loader.hood.startSky()
        NametagGlobals.setMasterArrowsOn(1)
        self.zoneId = requestStatus['zoneId']
        self.tunnelOriginList = toonbase.tcr.hoodMgr.addLinkTunnelHooks(self, self.loader.nodeList, self.zoneId)
        how = requestStatus['how']
        if how == 'teleportIn':
            how = 'deathAck'
        
        self.fsm.request(how, [
            requestStatus])

    
    def exit(self):
        self.ignoreAll()
        messenger.send('exitPlayground')
        for node in self.tunnelOriginList:
            node.removeNode()
        
        del self.tunnelOriginList
        self.loader.geom.reparentTo(hidden)
        NametagGlobals.setMasterArrowsOn(0)
        for i in self.loader.nodeList:
            self.loader.exitAnimatedProps(i)
        
        self.loader.hood.stopSky()
        self.loader.music.stop()

    
    def load(self):
        Place.Place.load(self)
        self.parentFSM.getStateNamed('playground').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('playground').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        
        if self.deathAckBox:
            self.deathAckBox.cleanup()
            self.deathAckBox = None
        
        ToontownDialog.cleanupDialog('globalDialog')
        self.ignoreAll()
        Place.Place.unload(self)

    
    def showTreasurePoints(self, points):
        self.hideDebugPointText()
        for i in range(len(points)):
            p = points[i]
            self.showDebugPointText(str(i), p)
        

    
    def showDropPoints(self, points):
        self.hideDebugPointText()
        for i in range(len(points)):
            p = points[i]
            self.showDebugPointText(str(i), p)
        

    
    def showPathPoints(self, paths, waypoints):
        self.hideDebugPointText()
        lines = LineSegs()
        lines.setColor(1, 0, 0, 1)
        import CCharPaths
        for (name, pointDef) in paths.items():
            self.showDebugPointText(name, pointDef[0])
            for connectTo in pointDef[1]:
                toDef = paths[connectTo]
                fromP = pointDef[0]
                toP = toDef[0]
                lines.moveTo(fromP[0], fromP[1], fromP[2] + 2.0)
                wpList = CCharPaths.getWayPoints(name, connectTo, paths, waypoints)
                for wp in wpList:
                    lines.drawTo(wp[0], wp[1], wp[2] + 2.0)
                    self.showDebugPointText('*', wp)
                
                lines.drawTo(toP[0], toP[1], toP[2] + 2.0)
            
        
        self.debugText.attachNewNode(lines.create())

    
    def hideDebugPointText(self):
        if hasattr(self, 'debugText'):
            children = self.debugText.getChildren()
            for i in range(children.getNumPaths()):
                children[i].removeNode()
            
        

    
    def showDebugPointText(self, text, point):
        if not hasattr(self, 'debugText'):
            self.debugText = self.loader.geom.attachNewNode('debugText')
            self.debugTextNode = TextNode('debugTextNode')
            self.debugTextNode.freeze()
            self.debugTextNode.setTextColor(1, 0, 0, 1)
            self.debugTextNode.setAlign(TextNode.ACenter)
            self.debugTextNode.setFont(ToontownGlobals.getSignFont())
        
        self.debugTextNode.setText(text)
        np = self.debugText.attachNewNode(self.debugTextNode.generate())
        np.setPos(point[0], point[1], point[2])
        np.setScale(4.0)
        np.setBillboardPointEye()

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterTrolley(self):
        toonbase.localToon.laffMeter.start()
        toonbase.localToon.b_setAnimState('off', 1)
        self.accept(self.trolleyDoneEvent, self.handleTrolleyDone)
        self.trolley = Trolley.Trolley(self, self.fsm, self.trolleyDoneEvent)
        self.trolley.load()
        self.trolley.enter()
        return None

    
    def exitTrolley(self):
        toonbase.localToon.laffMeter.stop()
        self.ignore(self.trolleyDoneEvent)
        self.trolley.unload()
        self.trolley.exit()
        del self.trolley
        return None

    
    def detectedTrolleyCollision(self):
        self.fsm.request('trolley')
        return None

    
    def handleTrolleyDone(self, doneStatus):
        self.notify.debug('handling trolley done event')
        mode = doneStatus['mode']
        if mode == 'reject':
            self.fsm.request('walk')
        elif mode == 'exit':
            self.fsm.request('walk')
        elif mode == 'minigame':
            self.doneStatus = {
                'loader': 'minigame',
                'where': 'minigame',
                'hoodId': self.loader.hood.id,
                'zoneId': doneStatus['zoneId'],
                'shardId': None,
                'minigameId': doneStatus['minigameId'] }
            messenger.send(self.doneEvent)
        else:
            self.notify.error('Unknown mode: ' + mode + ' in handleTrolleyDone')

    
    def debugStartMinigame(self, zoneId, minigameId):
        self.doneStatus = {
            'loader': 'minigame',
            'where': 'minigame',
            'hoodId': self.loader.hood.id,
            'zoneId': zoneId,
            'shardId': None,
            'minigameId': minigameId }
        messenger.send(self.doneEvent)

    
    def enterTFACallback(self, requestStatus, doneStatus):
        self.tfa.exit()
        del self.tfa
        doneStatusMode = doneStatus['mode']
        if doneStatusMode == 'complete':
            self.fsm.request('DFA', [
                requestStatus])
        elif doneStatusMode == 'incomplete':
            self.fsm.request('TFAReject')
        else:
            self.notify.error('Unknown mode: %s' % doneStatusMode)
        return None

    
    def enterDFACallback(self, requestStatus, doneStatus):
        self.dfa.exit()
        del self.dfa
        ds = doneStatus['mode']
        if ds == 'complete':
            self.fsm.request('NPCFA', [
                requestStatus])
        elif ds == 'incomplete':
            self.fsm.request('DFAReject')
        else:
            self.notify.error('Unknown done status for DownloadForceAcknowledge: ' + `doneStatus`)
        return None

    
    def enterHFA(self, requestStatus):
        self.acceptOnce(self.hfaDoneEvent, self.enterHFACallback, [
            requestStatus])
        self.hfa = HealthForceAcknowledge.HealthForceAcknowledge(self.hfaDoneEvent)
        self.hfa.enter(1)

    
    def exitHFA(self):
        self.ignore(self.hfaDoneEvent)

    
    def enterHFACallback(self, requestStatus, doneStatus):
        self.hfa.exit()
        del self.hfa
        if doneStatus['mode'] == 'complete':
            outHow = {
                'teleportIn': 'teleportOut',
                'tunnelIn': 'tunnelOut',
                'doorIn': 'doorOut' }
            self.fsm.request(outHow[requestStatus['how']], [
                requestStatus])
        elif doneStatus['mode'] == 'incomplete':
            self.fsm.request('HFAReject')
        else:
            self.notify.error('Unknown done status for HealthForceAcknowledge: ' + `doneStatus`)
        return None

    
    def enterHFAReject(self):
        self.fsm.request('walk')

    
    def exitHFAReject(self):
        pass

    
    def enterNPCFA(self, requestStatus):
        if toonbase.localToon.teleportCheat:
            self.fsm.request('HFA', [
                requestStatus])
        else:
            self.acceptOnce(self.npcfaDoneEvent, self.enterNPCFACallback, [
                requestStatus])
            self.npcfa = NPCForceAcknowledge.NPCForceAcknowledge(self.npcfaDoneEvent)
            self.npcfa.enter()

    
    def exitNPCFA(self):
        self.ignore(self.npcfaDoneEvent)

    
    def enterNPCFACallback(self, requestStatus, doneStatus):
        self.npcfa.exit()
        del self.npcfa
        if doneStatus['mode'] == 'complete':
            self.fsm.request('HFA', [
                requestStatus])
        elif doneStatus['mode'] == 'incomplete':
            self.fsm.request('NPCFAReject')
        else:
            self.notify.error('Unknown done status for NPCForceAcknowledge: ' + `doneStatus`)
        return None

    
    def enterNPCFAReject(self):
        self.fsm.request('walk')

    
    def exitNPCFAReject(self):
        pass

    
    def enterDeathAck(self, requestStatus):
        self.deathAckBox = None
        self.fsm.request('teleportIn', [
            requestStatus])

    
    def exitDeathAck(self):
        if self.deathAckBox:
            self.ignore('deathAck')
            self.deathAckBox.cleanup()
            self.deathAckBox = None
        

    
    def enterTeleportIn(self, requestStatus):
        if len(toonbase.localToon.quests) == 1 and toonbase.localToon.quests[0][0] == NPCForceAcknowledge.TROLLEY_QUEST:
            requestStatus['nextState'] = 'popup'
            imageModel = loader.loadModel('phase_4/models/gui/tfa_images')
            if toonbase.localToon.quests[0][4] < 1:
                (x, y, z, h, p, r) = toonbase.tcr.hoodMgr.get_drop_point(toonbase.tcr.hoodMgr.ToontownCentral_initial_drop_points)
                msg = Localizer.NPCForceAcknowledgeMessage3
                imgNodePath = imageModel.find('**/trolley-dialog-image')
                imgPos = (0, 0, 0.040000000000000001)
                pos = (0, 0, -0.10000000000000001)
                heading = 55.0
                scale = 0.017999999999999999
            else:
                (x, y, z, h, p, r) = toonbase.tcr.hoodMgr.get_drop_point(toonbase.tcr.hoodMgr.ToontownCentral_hq_drop_points)
                msg = Localizer.NPCForceAcknowledgeMessage4
                imgNodePath = imageModel.find('**/hq-dialog-image')
                imgPos = (0, 0, -0.02)
                pos = (0, 0, -0.20000000000000001)
                heading = 45.0
                scale = 0.0070000000000000001
            self.dialog = ToontownDialog.ToontownDialog(text = msg, command = self._Playground__cleanupDialog, style = ToontownDialog.Acknowledge)
            imgLabel = DirectLabel.DirectLabel(parent = self.dialog, relief = None, pos = imgPos, scale = 1.0, image = imgNodePath, image_scale = 0.25)
        else:
            requestStatus['nextState'] = 'walk'
            (x, y, z, h, p, r) = toonbase.tcr.hoodMgr.getPlaygroundCenterFromId(self.loader.hood.id)
            if toonbase.localToon.hp < 1:
                requestStatus['nextState'] = 'popup'
                self.accept('deathAck', self._Playground__handleDeathAck, extraArgs = [
                    requestStatus])
                self.deathAckBox = DeathForceAcknowledge.DeathForceAcknowledge(doneEvent = 'deathAck')
            
        toonbase.localToon.reparentTo(hidden)
        toonbase.localToon.setPosHpr(render, x, y, z, h, p, r)
        Place.Place.enterTeleportIn(self, requestStatus)

    
    def _Playground__cleanupDialog(self, value):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        
        self.fsm.request('walk', [
            1])

    
    def _Playground__handleDeathAck(self, requestStatus):
        if self.deathAckBox:
            self.ignore('deathAck')
            self.deathAckBox.cleanup()
            self.deathAckBox = None
        
        self.fsm.request('walk', [
            1])

    
    def enterPopup(self, teleportIn = 0):
        if toonbase.localToon.hp < 1:
            toonbase.localToon.b_setAnimState('Sad', 1)
        else:
            toonbase.localToon.b_setAnimState('neutral', 1.0)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.startSleepWatch(self._Playground__handleFallingAsleepPopup)

    
    def exitPopup(self):
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')

    
    def _Playground__handleFallingAsleepPopup(self, task):
        if hasattr(self, 'fsm'):
            self.fsm.request('walk')
            toonbase.localToon.forceGotoSleep()
        
        return Task.done

    
    def enterTeleportOut(self, requestStatus):
        Place.Place.enterTeleportOut(self, requestStatus, self._Playground__teleportOutDone)

    
    def _Playground__teleportOutDone(self, requestStatus):
        if hasattr(self, 'activityFsm'):
            self.activityFsm.requestFinalState()
        
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        avId = requestStatus['avId']
        shardId = requestStatus['shardId']
        if hoodId == self.loader.hood.hoodId and zoneId == self.loader.hood.hoodId and shardId == None:
            self.fsm.request('deathAck', [
                requestStatus])
        elif hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    
    def exitTeleportOut(self):
        Place.Place.exitTeleportOut(self)

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def createPlayground(self, dnaFile):
        loader.loadDNAFile(self.loader.dnaStore, self.safeZoneStorageDNAFile)
        node = loader.loadDNAFile(self.loader.dnaStore, dnaFile)
        if node.getNumParents() == 1:
            self.geom = NodePath(node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries(self.loader.dnaStore)
        self.tunnelOriginList = toonbase.tcr.hoodMgr.addLinkTunnelHooks(self, self.nodeList, self.zoneId)
        self.geom.flattenMedium()
        gsg = base.win.getGsg()
        if gsg:
            self.geom.prepareScene(gsg)
        

    
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
        self.loader.dnaStore.resetPlaceNodes()
        self.loader.dnaStore.resetDNAGroups()
        self.loader.dnaStore.resetDNAVisGroups()
        self.loader.dnaStore.resetDNAVisGroupsAI()

    
    def removeLandmarkBlockNodes(self):
        npc = self.geom.findAllMatches('**/suit_building_origin')
        for i in range(npc.getNumPaths()):
            npc.getPath(i).removeNode()
        

    
    def enterTFA(self, requestStatus):
        self.acceptOnce(self.tfaDoneEvent, self.enterTFACallback, [
            requestStatus])
        self.tfa = TutorialForceAcknowledge.TutorialForceAcknowledge(self.tfaDoneEvent)
        self.tfa.enter()

    
    def exitTFA(self):
        self.ignore(self.tfaDoneEvent)

    
    def enterTFAReject(self):
        self.fsm.request('walk')

    
    def exitTFAReject(self):
        pass


