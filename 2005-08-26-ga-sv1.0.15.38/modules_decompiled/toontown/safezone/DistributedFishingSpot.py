# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.directtools.DirectGeometry import LineNodePath
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.fishing import FishGlobals
from toontown.shtiker import FishPage
from toontown.toonbase import TTLocalizer
from toontown.quest import Quests
from direct.actor import Actor
from direct.showutil import Rope
import math
import whrandom
import random
from toontown.fishing import FishingTargetGlobals
from toontown.fishing import FishBase
from toontown.fishing import FishPanel
from toontown.effects import Ripples
from toontown.toontowngui import TTDialog
from toontown.toonbase import ToontownTimer
from direct.fsm import ClassicFSM
from direct.fsm import State

class DistributedFishingSpot(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingSpot')
    vZeroMax = 25.0
    angleMax = 30.0
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.lastAvId = 0
        self.lastFrame = 0
        self.avId = 0
        self.av = None
        self.placedAvatar = 0
        self.localToonFishing = 0
        self.nodePath = None
        self.collSphere = None
        self.collNode = None
        self.collNodePath = None
        self.castTrack = None
        self.pond = None
        self.guiTrack = None
        self.madeGui = 0
        self.castGui = None
        self.itemGui = None
        self.pole = None
        self.line = None
        self.poleNode = []
        self.ptop = None
        self.bob = None
        self.bobBobTask = None
        self.splashSounds = None
        self.ripples = None
        self.line = None
        self.lineSphere = None
        self.power = 0.0
        self.startAngleNP = 0
        self.firstCast = 1
        self.fishPanel = None
        self.fsm = ClassicFSM.ClassicFSM('DistributedFishingSpot', [
            State.State('off', self.enterOff, self.exitOff, [
                'waiting',
                'distCasting',
                'fishing',
                'reward',
                'leaving']),
            State.State('waiting', self.enterWaiting, self.exitWaiting, [
                'localAdjusting',
                'distCasting',
                'leaving',
                'sellFish']),
            State.State('localAdjusting', self.enterLocalAdjusting, self.exitLocalAdjusting, [
                'localCasting',
                'leaving']),
            State.State('localCasting', self.enterLocalCasting, self.exitLocalCasting, [
                'localAdjusting',
                'fishing',
                'leaving']),
            State.State('distCasting', self.enterDistCasting, self.exitDistCasting, [
                'fishing',
                'leaving',
                'reward']),
            State.State('fishing', self.enterFishing, self.exitFishing, [
                'localAdjusting',
                'distCasting',
                'waitForAI',
                'reward',
                'leaving']),
            State.State('sellFish', self.enterSellFish, self.exitSellFish, [
                'waiting',
                'leaving']),
            State.State('waitForAI', self.enterWaitForAI, self.exitWaitForAI, [
                'reward',
                'leaving']),
            State.State('reward', self.enterReward, self.exitReward, [
                'localAdjusting',
                'distCasting',
                'leaving',
                'sellFish']),
            State.State('leaving', self.enterLeaving, self.exitLeaving, [])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def disable(self):
        self.ignore(self.uniqueName('enterFishingSpotSphere'))
        self.setOccupied(0)
        self.avId = 0
        if self.castTrack != None:
            if self.castTrack.isPlaying():
                self.castTrack.finish()
            
            self.castTrack = None
        
        if self.guiTrack != None:
            if self.guiTrack.isPlaying():
                self.guiTrack.finish()
            
            self.guiTrack = None
        
        self._DistributedFishingSpot__hideBob()
        self.nodePath.detachNode()
        self._DistributedFishingSpot__unmakeGui()
        self.pond.stopCheckingTargets()
        self.pond = None
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        del self.pond
        del self.fsm
        if self.nodePath:
            self.nodePath.removeNode()
            del self.nodePath
        
        DistributedObject.DistributedObject.delete(self)

    
    def generateInit(self):
        self.nodePath = NodePath(self.uniqueName('FishingSpot'))
        self.angleNP = self.nodePath.attachNewNode(self.uniqueName('FishingSpotAngleNP'))
        self.collSphere = CollisionSphere(0, 0, 0, self.getSphereRadius())
        self.collSphere.setTangible(0)
        self.collNode = CollisionNode(self.uniqueName('FishingSpotSphere'))
        self.collNode.setCollideMask(ToontownGlobals.WallBitmask)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.nodePath.attachNewNode(self.collNode)
        self.bobStartPos = Point3(0.0, 3.0, 8.5)

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.nodePath.reparentTo(self.getParentNodePath())
        self.accept(self.uniqueName('enterFishingSpotSphere'), self._DistributedFishingSpot__handleEnterSphere)

    
    def setPondDoId(self, pondDoId):
        self.pond = base.cr.doId2do[pondDoId]
        self.area = self.pond.getArea()
        self.waterLevel = FishingTargetGlobals.getWaterLevel(self.area)

    
    def _DistributedFishingSpot__handleEnterSphere(self, collEntry):
        if base.localAvatar.doId == self.lastAvId and globalClock.getFrameCount() <= self.lastFrame + 1:
            self.notify.info('Ignoring duplicate entry for avatar.')
            return None
        
        if base.localAvatar.hp > 0:
            self.cr.playGame.getPlace().detectedFishingCollision()
            self.d_requestEnter()
        

    
    def d_requestEnter(self):
        self.sendUpdate('requestEnter', [])

    
    def rejectEnter(self):
        self.cr.playGame.getPlace().setState('walk')

    
    def d_requestExit(self):
        self.sendUpdate('requestExit', [])

    
    def d_doCast(self, power, heading):
        self.sendUpdate('doCast', [
            power,
            heading])

    
    def getSphereRadius(self):
        return 1.5

    
    def getParentNodePath(self):
        return render

    
    def setPosHpr(self, x, y, z, h, p, r):
        self.nodePath.setPosHpr(x, y, z, h, p, r)
        self.angleNP.setH(render, self.nodePath.getH(render))

    
    def setOccupied(self, avId):
        if self.av != None:
            if not self.av.isEmpty():
                self._DistributedFishingSpot__dropPole()
                self.av.loop('neutral')
                self.av.setParent(ToontownGlobals.SPRender)
                self.av.startSmooth()
            
            self.ignore(self.av.uniqueName('disable'))
            self._DistributedFishingSpot__hideBob()
            self.fsm.requestFinalState()
            self._DistributedFishingSpot__removePole()
            self.av = None
            self.placedAvatar = 0
            self.angleNP.setH(render, self.nodePath.getH(render))
        
        self._DistributedFishingSpot__hideLine()
        wasLocalToon = self.localToonFishing
        self.lastAvId = self.avId
        self.lastFrame = globalClock.getFrameCount()
        self.avId = avId
        self.localToonFishing = 0
        if self.avId == 0:
            self.collSphere.setTangible(0)
        else:
            self.collSphere.setTangible(1)
            if self.avId == base.localAvatar.doId:
                base.setCellsAvailable(base.bottomCells, 0)
                self.localToonFishing = 1
                if base.wantBingo:
                    self.pond.setLocalToonSpot(self)
                
            
            av = self.cr.doId2do.get(self.avId)
            if av:
                self.av = av
                self._DistributedFishingSpot__loadStuff()
                self.placedAvatar = 0
                self.firstCast = 1
                self.acceptOnce(self.av.uniqueName('disable'), self._DistributedFishingSpot__avatarGone)
                self.av.stopSmooth()
                self.av.wrtReparentTo(self.angleNP)
                self.av.setAnimState('neutral', 1.0)
                self.createCastTrack()
            else:
                self.notify.warning('Unknown avatar %d in fishing spot %d' % (self.avId, self.doId))
        if wasLocalToon and not (self.localToonFishing):
            self._DistributedFishingSpot__hideCastGui()
            if base.wantBingo:
                self.pond.setLocalToonSpot()
            
            base.setCellsAvailable([
                base.bottomCells[1],
                base.bottomCells[2]], 1)
            base.setCellsAvailable(base.rightCells, 1)
            place = base.cr.playGame.getPlace()
            if place:
                place.setState('walk')
            
        

    
    def _DistributedFishingSpot__avatarGone(self):
        self.setOccupied(0)

    
    def setMovie(self, mode, code, itemDesc1, itemDesc2, itemDesc3, power, h):
        if self.av == None:
            return None
        
        if mode == FishGlobals.NoMovie:
            pass
        1
        if mode == FishGlobals.EnterMovie:
            self.fsm.request('waiting')
        elif mode == FishGlobals.ExitMovie:
            self.fsm.request('leaving')
        elif mode == FishGlobals.CastMovie:
            if not (self.localToonFishing):
                self.fsm.request('distCasting', [
                    power,
                    h])
            
        elif mode == FishGlobals.PullInMovie:
            self.fsm.request('reward', [
                code,
                itemDesc1,
                itemDesc2,
                itemDesc3])
        

    
    def getStareAtNodeAndOffset(self):
        return (self.nodePath, Point3())

    
    def _DistributedFishingSpot__loadStuff(self):
        rodId = self.av.getFishingRod()
        rodPath = FishGlobals.RodFileDict.get(rodId)
        if not rodPath:
            self.notify.warning('Rod id: %s model not found' % rodId)
            rodPath = RodFileDict[0]
        
        self.pole = Actor.Actor()
        self.pole.loadModel(rodPath)
        self.pole.loadAnims({
            'cast': 'phase_4/models/props/fishing-pole-chan' })
        self.pole.pose('cast', 0)
        self.ptop = self.pole.find('**/joint_attachBill')
        if self.line == None:
            self.line = Rope.Rope(self.uniqueName('Line'))
            self.line.setColor(1, 1, 1, 0.40000000000000002)
            self.line.setTransparency(1)
            self.lineSphere = BoundingSphere(Point3(-0.59999999999999998, -2, -5), 5.5)
        
        if self.bob == None:
            self.bob = loader.loadModelCopy('phase_4/models/props/fishing_bob')
            self.bob.setScale(1.5)
            self.ripples = Ripples.Ripples(self.nodePath)
            self.ripples.setScale(0.40000000000000002)
            self.ripples.hide()
        
        if self.splashSounds == None:
            self.splashSounds = (base.loadSfx('phase_4/audio/sfx/TT_splash1.mp3'), base.loadSfx('phase_4/audio/sfx/TT_splash2.mp3'))
        

    
    def _DistributedFishingSpot__placeAvatar(self):
        if not (self.placedAvatar):
            self.placedAvatar = 1
            self._DistributedFishingSpot__holdPole()
            self.av.setPosHpr(0, 0, 0, 0, 0, 0)
        

    
    def _DistributedFishingSpot__holdPole(self):
        if self.poleNode != []:
            self._DistributedFishingSpot__dropPole()
        
        np = NodePath('pole-holder')
        hands = self.av.getRightHands()
        for h in hands:
            self.poleNode.append(np.instanceTo(h))
        
        self.pole.reparentTo(self.poleNode[0])

    
    def _DistributedFishingSpot__dropPole(self):
        self._DistributedFishingSpot__hideBob()
        self._DistributedFishingSpot__hideLine()
        if self.pole != None:
            self.pole.clearMat()
            self.pole.detachNode()
        
        for pn in self.poleNode:
            pn.removeNode()
        
        self.poleNode = []

    
    def _DistributedFishingSpot__removePole(self):
        self.pole.removeNode()
        self.poleNode = []
        self.ptop.removeNode()
        self.pole = None
        self.ptop = None

    
    def _DistributedFishingSpot__showLineWaiting(self):
        self.line.setup(4, ((None, (0, 0, 0)), (None, (0, -2, -4)), (self.bob, (0, -1, 0)), (self.bob, (0, 0, 0))))
        self.line.ropeNode.setBound(self.lineSphere)
        self.line.reparentTo(self.ptop)

    
    def _DistributedFishingSpot__showLineCasting(self):
        self.line.setup(2, ((None, (0, 0, 0)), (self.bob, (0, 0, 0))))
        self.line.ropeNode.setBound(self.lineSphere)
        self.line.reparentTo(self.ptop)

    
    def _DistributedFishingSpot__showLineReeling(self):
        self.line.setup(2, ((None, (0, 0, 0)), (self.bob, (0, 0, 0))))
        self.line.ropeNode.setBound(self.lineSphere)
        self.line.reparentTo(self.ptop)

    
    def _DistributedFishingSpot__hideLine(self):
        if self.line:
            self.line.detachNode()
        

    
    def _DistributedFishingSpot__showBobFloat(self):
        self._DistributedFishingSpot__hideBob()
        self.bob.reparentTo(self.angleNP)
        self.ripples.reparentTo(self.angleNP)
        self.ripples.setPos(self.bob.getPos())
        self.ripples.setZ(self.waterLevel + 0.025000000000000001)
        self.ripples.play()
        splashSound = random.choice(self.splashSounds)
        base.playSfx(splashSound, volume = 0.80000000000000004, node = self.bob)
        self.bobBobTask = taskMgr.add(self._DistributedFishingSpot__doBobBob, self.taskName('bob'))

    
    def _DistributedFishingSpot__hideBob(self):
        if self.bob:
            self.bob.detachNode()
        
        if self.bobBobTask:
            taskMgr.remove(self.bobBobTask)
            self.bobBobTask = None
        
        if self.ripples:
            self.ripples.stop()
            self.ripples.detachNode()
        

    
    def _DistributedFishingSpot__doBobBob(self, task):
        z = math.sin(task.time * 1.8) * 0.080000000000000002
        self.bob.setZ(self.waterLevel + z)
        return Task.cont

    
    def _DistributedFishingSpot__userExit(self, event = None):
        if self.localToonFishing:
            self.fsm.request('leaving')
            self.d_requestExit()
        

    
    def _DistributedFishingSpot__sellFish(self, result = None):
        if self.localToonFishing:
            if result == TTDialog.DIALOG_OK:
                self.sendUpdate('sellFish', [])
                for button in self.sellFishDialog.buttonList:
                    button['state'] = DISABLED
                
            else:
                self.fsm.request('leaving')
                self.d_requestExit()
        

    
    def _DistributedFishingSpot__sellFishConfirm(self, result = None):
        if self.localToonFishing:
            self.fsm.request('waiting', [
                False])
        

    
    def _DistributedFishingSpot__showCastGui(self):
        self._DistributedFishingSpot__hideCastGui()
        self._DistributedFishingSpot__makeGui()
        self.castButton.show()
        self.arrow.hide()
        self.exitButton.show()
        self.timer.show()
        self._DistributedFishingSpot__updateFishTankGui()
        self.castGui.reparentTo(aspect2d)
        self.castButton['state'] = NORMAL
        self.jar['text'] = str(self.av.getMoney())
        self.accept(localAvatar.uniqueName('moneyChange'), self._DistributedFishingSpot__moneyChange)
        if base.wantBingo:
            self._DistributedFishingSpot__setBingoCastGui()
        
        
        def requestLocalAdjusting(mouseEvent):
            if self.av.isFishTankFull() and self._DistributedFishingSpot__allowSellFish():
                self.fsm.request('sellFish')
            else:
                self.fsm.request('localAdjusting')

        
        def requestLocalCasting(mouseEvent):
            if self.av.isFishTankFull():
                pass
            if not self._DistributedFishingSpot__allowSellFish():
                self.fsm.request('localCasting')
            

        self.castButton.bind(B1PRESS, requestLocalAdjusting)
        self.castButton.bind(B3PRESS, requestLocalAdjusting)
        self.castButton.bind(B1RELEASE, requestLocalCasting)
        self.castButton.bind(B3RELEASE, requestLocalCasting)
        if self.firstCast and len(self.av.fishCollection) == 0 and len(self.av.fishTank) == 0:
            self._DistributedFishingSpot__showHowTo(TTLocalizer.FishingHowToFirstTime)
        elif base.wantBingo and self.pond.hasPondBingoManager() and not (self.av.bFishBingoTutorialDone):
            self._DistributedFishingSpot__showHowTo(TTLocalizer.FishBingoHelpMain)
            self.av.b_setFishBingoTutorialDone(True)
        

    
    def _DistributedFishingSpot__moneyChange(self, money):
        self.jar['text'] = str(money)

    
    def _DistributedFishingSpot__initCastGui(self):
        self.timer.countdown(FishGlobals.CastTimeout)

    
    def _DistributedFishingSpot__showQuestItem(self, itemId):
        self._DistributedFishingSpot__makeGui()
        itemName = Quests.getItemName(itemId)
        self.itemLabel['text'] = itemName
        self.itemGui.reparentTo(aspect2d)
        self.itemPackage.show()
        self.itemJellybean.hide()
        self.itemBoot.hide()

    
    def _DistributedFishingSpot__showBootItem(self):
        self._DistributedFishingSpot__makeGui()
        itemName = TTLocalizer.FishingBootItem
        self.itemLabel['text'] = itemName
        self.itemGui.reparentTo(aspect2d)
        self.itemBoot.show()
        self.itemJellybean.hide()
        self.itemPackage.hide()

    
    def _DistributedFishingSpot__setItemLabel(self):
        if self.pond.hasPondBingoManager():
            self.itemLabel['text'] = str(itemName + '\n\n' + 'BINGO WILDCARD')
        else:
            self.itemLabel['text'] = itemName

    
    def _DistributedFishingSpot__showJellybeanItem(self, amount):
        self._DistributedFishingSpot__makeGui()
        itemName = TTLocalizer.FishingJellybeanItem % amount
        self.itemLabel['text'] = itemName
        self.itemGui.reparentTo(aspect2d)
        self.jar['text'] = str(self.av.getMoney())
        self.itemJellybean.show()
        self.itemBoot.hide()
        self.itemPackage.hide()

    
    def _DistributedFishingSpot__showFishItem(self, code, fish):
        self.fishPanel = FishPanel.FishPanel(fish)
        self._DistributedFishingSpot__setFishItemPos()
        self.fishPanel.setSwimBounds(-0.29999999999999999, 0.29999999999999999, -0.23499999999999999, 0.25)
        self.fishPanel.setSwimColor(1.0, 1.0, 0.74900999999999995, 1.0)
        self.fishPanel.load()
        self.fishPanel.show(code)
        self._DistributedFishingSpot__updateFishTankGui()

    
    def _DistributedFishingSpot__setFishItemPos(self):
        if base.wantBingo:
            if self.pond.hasPondBingoManager():
                self.fishPanel.setPos(0.65000000000000002, 0, 0.40000000000000002)
            else:
                self.fishPanel.setPos(0, 0, 0.5)
        else:
            self.fishPanel.setPos(0, 0, 0.5)

    
    def _DistributedFishingSpot__updateFishTankGui(self):
        fishTank = self.av.getFishTank()
        lenFishTank = len(fishTank)
        maxFishTank = self.av.getMaxFishTank()
        self.bucket['text'] = '%s/%s' % (lenFishTank, maxFishTank)

    
    def _DistributedFishingSpot__showFailureReason(self, code):
        self._DistributedFishingSpot__makeGui()
        reason = ''
        if code == FishGlobals.OverTankLimit:
            reason = TTLocalizer.FishingOverTankLimit
        
        self.failureDialog['text'] = reason
        self.failureDialog.show()

    
    def _DistributedFishingSpot__showSellFishDialog(self):
        self._DistributedFishingSpot__makeGui()
        self.sellFishDialog.show()

    
    def _DistributedFishingSpot__hideSellFishDialog(self):
        self._DistributedFishingSpot__makeGui()
        self.sellFishDialog.hide()

    
    def _DistributedFishingSpot__showSellFishConfirmDialog(self, numFishCaught):
        self._DistributedFishingSpot__makeGui()
        msg = TTLocalizer.STOREOWNER_TROPHY % (numFishCaught, FishGlobals.getTotalNumFish())
        self.sellFishConfirmDialog.setMessage(msg)
        self.sellFishConfirmDialog.show()

    
    def _DistributedFishingSpot__hideSellFishConfirmDialog(self):
        self._DistributedFishingSpot__makeGui()
        self.sellFishConfirmDialog.hide()

    
    def _DistributedFishingSpot__showBroke(self):
        self._DistributedFishingSpot__makeGui()
        self.brokeDialog.show()
        self.castButton['state'] = DISABLED

    
    def _DistributedFishingSpot__showHowTo(self, message):
        self._DistributedFishingSpot__makeGui()
        self.howToDialog['text'] = message
        self.howToDialog.show()

    
    def _DistributedFishingSpot__hideHowTo(self, event = None):
        self._DistributedFishingSpot__makeGui()
        self.howToDialog.hide()

    
    def _DistributedFishingSpot__showFishTankFull(self):
        self._DistributedFishingSpot__makeGui()
        self._DistributedFishingSpot__showFailureReason(FishGlobals.OverTankLimit)
        self.castButton['state'] = DISABLED

    
    def _DistributedFishingSpot__hideCastGui(self):
        if self.madeGui:
            self.timer.hide()
            self.castGui.detachNode()
            self.itemGui.detachNode()
            self.failureDialog.hide()
            self.sellFishDialog.hide()
            self.sellFishConfirmDialog.hide()
            self.brokeDialog.hide()
            self.howToDialog.hide()
            self.castButton.unbind(B1PRESS)
            self.castButton.unbind(B3PRESS)
            self.castButton.unbind(B1RELEASE)
            self.castButton.unbind(B3RELEASE)
            self.ignore(localAvatar.uniqueName('moneyChange'))
        

    
    def _DistributedFishingSpot__itemGuiClose(self):
        self.itemGui.detachNode()

    
    def _DistributedFishingSpot__makeGui(self):
        if self.madeGui:
            return None
        
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.posInTopRightCorner()
        self.timer.hide()
        self.castGui = loader.loadModel('phase_4/models/gui/fishingGui')
        self.castGui.setScale(0.67000000000000004)
        self.castGui.setPos(0, 1, 0)
        for nodeName in ('bucket', 'jar', 'display_bucket', 'display_jar'):
            self.castGui.find('**/' + nodeName).reparentTo(self.castGui)
        
        self.exitButton = DirectButton(parent = self.castGui, relief = None, text = ('', TTLocalizer.FishingExit, TTLocalizer.FishingExit), text_align = TextNode.ACenter, text_scale = 0.10000000000000001, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0.0, -0.12), pos = (1.75, 0, -1.3300000000000001), textMayChange = 0, image = (self.castGui.find('**/exit_buttonUp'), self.castGui.find('**/exit_buttonDown'), self.castGui.find('**/exit_buttonRollover')), command = self._DistributedFishingSpot__userExit)
        self.castGui.find('**/exitButton').removeNode()
        self.castButton = DirectButton(parent = self.castGui, relief = None, text = TTLocalizer.FishingCast, text_align = TextNode.ACenter, text_scale = (3, 3 * 0.75, 3 * 0.75), text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -4), image = self.castGui.find('**/castButton'), image0_color = (1, 0, 0, 1), image1_color = (0, 1, 0, 1), image2_color = (1, 1, 0, 1), image3_color = (0.80000000000000004, 0.5, 0.5, 1), pos = (0, -0.050000000000000003, -0.66600000000000004), scale = (0.035999999999999997, 1, 0.048000000000000001))
        self.castGui.find('**/castButton').removeNode()
        self.arrow = self.castGui.find('**/arrow')
        self.arrowTip = self.arrow.find('**/arrowTip')
        self.arrowTail = self.arrow.find('**/arrowTail')
        self.arrow.reparentTo(self.castGui)
        self.arrow.setColorScale(0.90000000000000002, 0.90000000000000002, 0.10000000000000001, 0.69999999999999996)
        self.arrow.hide()
        self.jar = DirectLabel(parent = self.castGui, relief = None, text = str(self.av.getMoney()), text_scale = 0.16, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_font = ToontownGlobals.getSignFont(), pos = (-1.1200000000000001, 0, -1.3))
        self.bucket = DirectLabel(parent = self.castGui, relief = None, text = '', text_scale = 0.089999999999999997, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), pos = (1.1399999999999999, 0, -1.3300000000000001))
        self._DistributedFishingSpot__updateFishTankGui()
        self.itemGui = NodePath('itemGui')
        self.itemFrame = DirectFrame(parent = self.itemGui, relief = None, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (1, 1, 0.59999999999999998), text = TTLocalizer.FishingItemFound, text_pos = (0, 0.20000000000000001), text_scale = 0.080000000000000002, pos = (0, 0, 0.58699999999999997))
        self.itemLabel = DirectLabel(parent = self.itemFrame, text = '', text_scale = 0.059999999999999998, pos = (0, 0, -0.25))
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        self.itemGuiCloseButton = DirectButton(parent = self.itemFrame, pos = (0.44, 0, -0.23999999999999999), relief = None, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), image_scale = (0.69999999999999996, 1, 0.69999999999999996), command = self._DistributedFishingSpot__itemGuiClose)
        buttons.removeNode()
        jarGui = loader.loadModelOnce('phase_3.5/models/gui/jar_gui')
        bootGui = loader.loadModelOnce('phase_4/models/gui/fishing_boot')
        packageGui = loader.loadModelOnce('phase_3.5/models/gui/stickerbook_gui').find('**/package')
        self.itemJellybean = DirectFrame(parent = self.itemFrame, relief = None, image = jarGui, scale = 0.5)
        self.itemBoot = DirectFrame(parent = self.itemFrame, relief = None, image = bootGui, scale = 0.20000000000000001)
        self.itemPackage = DirectFrame(parent = self.itemFrame, relief = None, image = packageGui, scale = 0.25)
        self.itemJellybean.hide()
        self.itemBoot.hide()
        self.itemPackage.hide()
        self.failureDialog = TTDialog.TTGlobalDialog(dialogName = self.uniqueName('failureDialog'), doneEvent = self.uniqueName('failureDialog'), command = self._DistributedFishingSpot__userExit, message = TTLocalizer.FishingFailure, style = TTDialog.CancelOnly, cancelButtonText = TTLocalizer.FishingExit)
        self.failureDialog.hide()
        self.sellFishDialog = TTDialog.TTGlobalDialog(dialogName = self.uniqueName('sellFishDialog'), doneEvent = self.uniqueName('sellFishDialog'), command = self._DistributedFishingSpot__sellFish, message = TTLocalizer.FishBingoOfferToSellFish, style = TTDialog.YesNo)
        self.sellFishDialog.hide()
        self.sellFishConfirmDialog = TTDialog.TTGlobalDialog(dialogName = self.uniqueName('sellFishConfirmDialog'), doneEvent = self.uniqueName('sellFishConfirmDialog'), command = self._DistributedFishingSpot__sellFishConfirm, message = TTLocalizer.STOREOWNER_TROPHY, style = TTDialog.Acknowledge)
        self.sellFishConfirmDialog.hide()
        self.brokeDialog = TTDialog.TTGlobalDialog(dialogName = self.uniqueName('brokeDialog'), doneEvent = self.uniqueName('brokeDialog'), command = self._DistributedFishingSpot__userExit, message = TTLocalizer.FishingBroke, style = TTDialog.CancelOnly, cancelButtonText = TTLocalizer.FishingExit)
        self.brokeDialog.hide()
        self.howToDialog = TTDialog.TTGlobalDialog(dialogName = self.uniqueName('howToDialog'), doneEvent = self.uniqueName('howToDialog'), fadeScreen = 0, message = TTLocalizer.FishingHowToFailed, style = TTDialog.Acknowledge)
        self.howToDialog['command'] = self._DistributedFishingSpot__hideHowTo
        self.howToDialog.setPos(-0.29999999999999999, 0, 0.5)
        self.howToDialog.hide()
        self.madeGui = 1

    
    def _DistributedFishingSpot__setBingoCastGui(self):
        if self.pond.hasPondBingoManager():
            self.notify.info('__setBingoCastGui: Has PondBing Manager %s' % self.pond.getPondBingoManager().getDoId())
            bucket = self.castGui.find('**/bucket')
            self.castGui.find('**/display_bucket').reparentTo(bucket)
            self.bucket.reparentTo(bucket)
            jar = self.castGui.find('**/jar')
            self.castGui.find('**/display_jar').reparentTo(jar)
            self.jar.reparentTo(jar)
            base.setCellsAvailable(base.rightCells, 0)
            bucket.setScale(0.90000000000000002)
            bucket.setX(-1.8999999999999999)
            bucket.setZ(-0.11)
            jar.setScale(0.90000000000000002)
            jar.setX(-0.375)
            jar.setZ(-0.13500000000000001)
        else:
            self.notify.info('__setItemFramePos: Has No Pond Bingo Manager')
            bucket = self.castGui.find('**/bucket')
            bucket.setScale(1)
            bucket.setPos(0, 0, 0)
            jar = self.castGui.find('**/jar')
            jar.setScale(1)
            jar.setPos(0, 0, 0)

    
    def resetCastGui(self):
        self.notify.info('resetCastGui: Bingo Night Ends - resetting Gui')
        bucket = self.castGui.find('**/bucket')
        jar = self.castGui.find('**/jar')
        bucketPosInt = bucket.posInterval(5.0, Point3(0, 0, 0), startPos = bucket.getPos(), blendType = 'easeInOut')
        bucketScaleInt = bucket.scaleInterval(5.0, VBase3(1.0, 1.0, 1.0), startScale = bucket.getScale(), blendType = 'easeInOut')
        bucketTrack = Parallel(bucketPosInt, bucketScaleInt)
        jarPosInt = jar.posInterval(5.0, Point3(0, 0, 0), startPos = jar.getPos(), blendType = 'easeInOut')
        jarScaleInt = jar.scaleInterval(5.0, VBase3(1.0, 1.0, 1.0), startScale = jar.getScale(), blendType = 'easeInOut')
        jarTrack = Parallel(jarPosInt, jarScaleInt)
        self.guiTrack = Parallel(bucketTrack, jarTrack)
        self.guiTrack.start()

    
    def setCastGui(self):
        self.notify.info('setCastGui: Bingo Night Starts - setting Gui')
        bucket = self.castGui.find('**/bucket')
        self.castGui.find('**/display_bucket').reparentTo(bucket)
        self.bucket.reparentTo(bucket)
        jar = self.castGui.find('**/jar')
        self.castGui.find('**/display_jar').reparentTo(jar)
        self.jar.reparentTo(jar)
        bucketPosInt = bucket.posInterval(3.0, Point3(-1.8999999999999999, 0, -0.11), startPos = bucket.getPos(), blendType = 'easeInOut')
        bucketScaleInt = bucket.scaleInterval(3.0, VBase3(0.90000000000000002, 0.90000000000000002, 0.90000000000000002), startScale = bucket.getScale(), blendType = 'easeInOut')
        bucketTrack = Parallel(bucketPosInt, bucketScaleInt)
        jarPosInt = jar.posInterval(3.0, Point3(-0.375, 0, -0.13500000000000001), startPos = jar.getPos(), blendType = 'easeInOut')
        jarScaleInt = jar.scaleInterval(3.0, VBase3(0.90000000000000002, 0.90000000000000002, 0.90000000000000002), startScale = jar.getScale(), blendType = 'easeInOut')
        jarTrack = Parallel(jarPosInt, jarScaleInt)
        self.guiTrack = Parallel(bucketTrack, jarTrack)
        self.guiTrack.start()

    
    def setJarAmount(self, amount):
        if self.madeGui:
            money = int(self.jar['text']) + amount
            pocketMoney = min(money, self.av.getMaxMoney())
            self.jar.setProp('text', str(pocketMoney))
        

    
    def _DistributedFishingSpot__unmakeGui(self):
        if not (self.madeGui):
            return None
        
        self.timer.destroy()
        del self.timer
        self.exitButton.destroy()
        self.castButton.destroy()
        self.jar.destroy()
        self.bucket.destroy()
        self.itemFrame.destroy()
        self.itemGui.removeNode()
        self.failureDialog.cleanup()
        self.sellFishDialog.cleanup()
        self.sellFishConfirmDialog.cleanup()
        self.brokeDialog.cleanup()
        self.howToDialog.cleanup()
        self.castGui.removeNode()
        self.madeGui = 0

    
    def localAdjustingCastTask(self, state):
        self.getMouse()
        deltaX = self.mouseX - self.initMouseX
        deltaY = self.mouseY - self.initMouseY
        if deltaY >= 0:
            if self.power == 0:
                self.arrowTail.setScale(0.074999999999999997, 0.074999999999999997, 0)
                self.arrow.setR(0)
            
            self.castTrack.pause()
            return Task.cont
        
        dist = math.sqrt(deltaX * deltaX + deltaY * deltaY)
        delta = dist / 0.5
        self.power = max(min(abs(delta), 1.0), 0.0)
        self.castTrack.setT(0.20000000000000001 + self.power * 0.69999999999999996)
        angle = rad2Deg(math.atan(deltaX / deltaY))
        if self.power < 0.25:
            angle = angle * math.pow(self.power * 4, 3)
        
        if delta < 0:
            angle += 180
        
        minAngle = -(FishGlobals.FishingAngleMax)
        maxAngle = FishGlobals.FishingAngleMax
        if angle < minAngle:
            self.arrow.setColorScale(1, 0, 0, 1)
            angle = minAngle
        elif angle > maxAngle:
            self.arrow.setColorScale(1, 0, 0, 1)
            angle = maxAngle
        else:
            self.arrow.setColorScale(1, 1 - math.pow(self.power, 3), 0.10000000000000001, 0.69999999999999996)
        self.arrowTail.setScale(0.074999999999999997, 0.074999999999999997, self.power * 0.20000000000000001)
        self.arrow.setR(angle)
        self.angleNP.setH(-angle)
        return Task.cont

    
    def localAdjustingCastTaskIndAxes(self, state):
        self.getMouse()
        deltaX = self.mouseX - self.initMouseX
        deltaY = self.mouseY - self.initMouseY
        self.power = max(min(abs(deltaY) * 1.5, 1.0), 0.0)
        self.castTrack.setT(0.40000000000000002 + self.power * 0.5)
        angle = deltaX * -180.0
        self.angleNP.setH(self.startAngleNP - angle)
        return Task.cont

    
    def getMouse(self):
        if base.mouseWatcherNode.hasMouse():
            self.mouseX = base.mouseWatcherNode.getMouseX()
            self.mouseY = base.mouseWatcherNode.getMouseY()
        else:
            self.mouseX = 0
            self.mouseY = 0

    
    def createCastTrack(self):
        self.castTrack = Sequence(ActorInterval(self.av, 'castlong', playRate = 4), ActorInterval(self.av, 'cast', startFrame = 20), Func(self.av.loop, 'fish-neutral'))

    
    def startMoveBobTask(self):
        self._DistributedFishingSpot__showBob()
        taskMgr.add(self.moveBobTask, self.taskName('moveBobTask'))

    
    def moveBobTask(self, task):
        g = 32.200000000000003
        t = task.time
        vZero = self.power * self.vZeroMax
        angle = deg2Rad(self.power * self.angleMax)
        deltaY = vZero * math.cos(angle) * t
        deltaZ = vZero * math.sin(angle) * t - g * t * t / 2.0
        deltaPos = Point3(0, deltaY, deltaZ)
        self.bobStartPos = Point3(0.0, 3.0, 8.5)
        pos = self.bobStartPos + deltaPos
        self.bob.setPos(pos)
        if pos[2] < self.waterLevel:
            self.fsm.request('fishing')
            return Task.done
        else:
            return Task.cont

    
    def _DistributedFishingSpot__showBob(self):
        self._DistributedFishingSpot__hideBob()
        self.bob.reparentTo(self.angleNP)
        self.bob.setPos(self.ptop, 0, 0, 0)
        self.av.update(0)

    
    def hitTarget(self):
        self.fsm.request('waitForAI')

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterWaiting(self, doAnimation = True):
        self.av.stopLookAround()
        self._DistributedFishingSpot__hideLine()
        self.track = Parallel()
        if doAnimation:
            toonTrack = Sequence(Func(self.av.setPlayRate, 1.0, 'run'), Func(self.av.loop, 'run'), LerpPosHprInterval(self.av, 1.0, Point3(0, 0, 0), Point3(0, 0, 0)), Func(self._DistributedFishingSpot__placeAvatar), Parallel(ActorInterval(self.av, 'pole'), Func(self.pole.pose, 'cast', 0), LerpScaleInterval(self.pole, duration = 0.5, scale = 1.0, startScale = 0.01)), Func(self.av.loop, 'pole-neutral'))
            if self.localToonFishing:
                camera.wrtReparentTo(render)
                self.track.append(LerpPosHprInterval(nodePath = camera, other = self.av, duration = 1.5, pos = Point3(0, -12, 15), hpr = VBase3(0, -38, 0), blendType = 'easeInOut'))
                toonTrack.append(Func(self._DistributedFishingSpot__showCastGui))
                toonTrack.append(Func(self._DistributedFishingSpot__initCastGui))
                if base.wantBingo:
                    self._DistributedFishingSpot__appendBingoMethod(toonTrack, self.pond.showBingoGui)
                
            
            self.track.append(toonTrack)
        else:
            self._DistributedFishingSpot__showCastGui()
        self.track.start()

    
    def _DistributedFishingSpot__appendBingoMethod(self, interval, callback):
        interval.append(Func(callback))

    
    def exitWaiting(self):
        self.track.finish()
        self.track = None

    
    def enterLocalAdjusting(self, guiEvent = None):
        if self.track:
            self.track.pause()
        
        if self.castTrack:
            self.castTrack.pause()
        
        self.power = 0.0
        self.firstCast = 0
        self.castButton['image0_color'] = Vec4(0, 1, 0, 1)
        self.castButton['text'] = ''
        self.av.stopLookAround()
        self._DistributedFishingSpot__hideLine()
        self._DistributedFishingSpot__hideBob()
        self.howToDialog.hide()
        castCost = FishGlobals.getCastCost(self.av.getFishingRod())
        if self.av.getMoney() < castCost:
            self._DistributedFishingSpot__hideCastGui()
            self._DistributedFishingSpot__showBroke()
            self.av.loop('pole-neutral')
            return None
        
        if self.av.isFishTankFull():
            self._DistributedFishingSpot__hideCastGui()
            self._DistributedFishingSpot__showFishTankFull()
            self.av.loop('pole-neutral')
            return None
        
        self.arrow.show()
        self.arrow.setColorScale(1, 1, 0, 0.69999999999999996)
        self.startAngleNP = self.angleNP.getH()
        self.getMouse()
        self.initMouseX = self.mouseX
        self.initMouseY = self.mouseY
        self._DistributedFishingSpot__hideBob()
        if config.GetBool('fishing-independent-axes', 0):
            taskMgr.add(self.localAdjustingCastTaskIndAxes, self.taskName('adjustCastTask'))
        else:
            taskMgr.add(self.localAdjustingCastTask, self.taskName('adjustCastTask'))
        if base.wantBingo:
            bingoMgr = self.pond.getPondBingoManager()
            if bingoMgr:
                bingoMgr.castingStarted()
            
        

    
    def exitLocalAdjusting(self):
        taskMgr.remove(self.taskName('adjustCastTask'))
        self.castButton['image0_color'] = Vec4(1, 0, 0, 1)
        self.castButton['text'] = TTLocalizer.FishingCast
        self.arrow.hide()

    
    def enterLocalCasting(self):
        if self.power == 0.0 and len(self.av.fishCollection) == 0:
            self._DistributedFishingSpot__showHowTo(TTLocalizer.FishingHowToFailed)
            if self.castTrack:
                self.castTrack.pause()
            
            self.av.loop('pole-neutral')
            self.track = None
            return None
        
        castCost = FishGlobals.getCastCost(self.av.getFishingRod())
        self.jar['text'] = str(max(self.av.getMoney() - castCost, 0))
        if not (self.castTrack):
            self.createCastTrack()
        
        self.castTrack.pause()
        startT = 0.69999999999999996 + (1 - self.power) * 0.29999999999999999
        self.castTrack.start(startT)
        self.track = Sequence(Wait(1.2 - startT), Func(self.startMoveBobTask), Func(self._DistributedFishingSpot__showLineCasting))
        self.track.start()
        heading = self.angleNP.getH()
        self.d_doCast(self.power, heading)
        self.timer.countdown(FishGlobals.CastTimeout)

    
    def exitLocalCasting(self):
        taskMgr.remove(self.taskName('moveBobTask'))
        if self.track:
            self.track.pause()
            self.track = None
        
        if self.castTrack:
            self.castTrack.pause()
        
        self._DistributedFishingSpot__hideLine()
        self._DistributedFishingSpot__hideBob()

    
    def enterDistCasting(self, power, h):
        self.av.stopLookAround()
        self._DistributedFishingSpot__placeAvatar()
        self._DistributedFishingSpot__hideLine()
        self._DistributedFishingSpot__hideBob()
        self.angleNP.setH(h)
        self.power = power
        self.track = Parallel(Sequence(ActorInterval(self.av, 'cast'), Func(self.pole.pose, 'cast', 0), Func(self.av.loop, 'fish-neutral')), Sequence(Wait(1.0), Func(self.startMoveBobTask), Func(self._DistributedFishingSpot__showLineCasting)))
        self.track.start()

    
    def exitDistCasting(self):
        self.track.finish()
        self.track = None
        taskMgr.remove(self.taskName('moveBobTask'))
        self._DistributedFishingSpot__hideLine()
        self._DistributedFishingSpot__hideBob()

    
    def enterFishing(self):
        if self.localToonFishing:
            self.track = Sequence(ActorInterval(self.av, 'cast'), Func(self.pole.pose, 'cast', 0), Func(self.av.loop, 'fish-neutral'))
            self.track.start(self.castTrack.getT())
        else:
            self.track = None
            self.av.loop('fish-neutral')
        self._DistributedFishingSpot__showBobFloat()
        self._DistributedFishingSpot__showLineWaiting()
        if self.localToonFishing:
            self.pond.startCheckingTargets(self, self.bob.getPos(render))
        

    
    def exitFishing(self):
        if self.localToonFishing:
            self.pond.stopCheckingTargets()
        
        if self.track:
            self.track.finish()
            self.track = None
        

    
    def enterWaitForAI(self):
        self.castButton['state'] = DISABLED

    
    def exitWaitForAI(self):
        self.castButton['state'] = NORMAL

    
    def enterReward(self, code, itemDesc1, itemDesc2, itemDesc3):
        self._DistributedFishingSpot__placeAvatar()
        self.bob.reparentTo(self.angleNP)
        self.bob.setZ(self.waterLevel)
        self._DistributedFishingSpot__showLineReeling()
        self.castTrack.pause()
        if self.localToonFishing:
            self._DistributedFishingSpot__showCastGui()
            if code == FishGlobals.QuestItem:
                self._DistributedFishingSpot__showQuestItem(itemDesc1)
            elif code in (FishGlobals.FishItem, FishGlobals.FishItemNewEntry, FishGlobals.FishItemNewRecord):
                (genus, species, weight) = (itemDesc1, itemDesc2, itemDesc3)
                fish = FishBase.FishBase(genus, species, weight)
                self._DistributedFishingSpot__showFishItem(code, fish)
                if base.wantBingo:
                    self.pond.handleBingoCatch((genus, species))
                
            elif code == FishGlobals.BootItem:
                self._DistributedFishingSpot__showBootItem()
                if base.wantBingo:
                    self.pond.handleBingoCatch(FishGlobals.BingoBoot)
                
            elif code == FishGlobals.JellybeanItem:
                amount = itemDesc1
                self._DistributedFishingSpot__showJellybeanItem(amount)
            elif code == FishGlobals.OverTankLimit:
                self._DistributedFishingSpot__hideCastGui()
            else:
                self._DistributedFishingSpot__showFailureReason(code)
        
        self.track = Sequence(Parallel(ActorInterval(self.av, 'reel'), ActorInterval(self.pole, 'cast', startFrame = 63, endFrame = 127)), ActorInterval(self.av, 'reel-neutral'), Func(self._DistributedFishingSpot__hideLine), Func(self._DistributedFishingSpot__hideBob), ActorInterval(self.av, 'fish-again'), Func(self.av.loop, 'pole-neutral'))
        self.track.start()

    
    def cleanupFishPanel(self):
        if self.fishPanel:
            self.fishPanel.hide()
            self.fishPanel.destroy()
            self.fishPanel = None
        

    
    def hideBootPanel(self):
        if self.madeGui and self.itemBoot:
            self._DistributedFishingSpot__itemGuiClose()
        

    
    def exitReward(self):
        if self.localToonFishing:
            self.itemGui.detachNode()
            self.cleanupFishPanel()
        
        self.track.finish()
        self.track = None

    
    def enterLeaving(self):
        if self.localToonFishing:
            self._DistributedFishingSpot__hideCastGui()
            if base.wantBingo:
                self.pond.cleanupBingoMgr()
            
        
        self.av.stopLookAround()
        self.av.startLookAround()
        self._DistributedFishingSpot__placeAvatar()
        self._DistributedFishingSpot__hideLine()
        self._DistributedFishingSpot__hideBob()
        self.track = Sequence(Parallel(ActorInterval(self.av, 'fish-end'), Func(self.pole.pose, 'cast', 0), LerpScaleInterval(self.pole, duration = 0.5, scale = 0.01, startScale = 1.0)), Func(self._DistributedFishingSpot__dropPole), Func(self.av.loop, 'neutral'))
        if self.localToonFishing:
            self.track.append(Func(self.fsm.requestFinalState))
        
        self.track.start()

    
    def exitLeaving(self):
        self.track.pause()
        self.track = None

    
    def enterSellFish(self):
        self.castButton['state'] = DISABLED
        self._DistributedFishingSpot__showSellFishDialog()
        self._DistributedFishingSpot__hideHowTo()

    
    def exitSellFish(self):
        self.castButton['state'] = NORMAL
        self._DistributedFishingSpot__hideSellFishDialog()
        self._DistributedFishingSpot__hideSellFishConfirmDialog()

    
    def sellFishComplete(self, trophyResult, numFishCaught):
        for button in self.sellFishDialog.buttonList:
            button['state'] = NORMAL
        
        if self.localToonFishing:
            if trophyResult:
                self._DistributedFishingSpot__hideSellFishDialog()
                self._DistributedFishingSpot__showSellFishConfirmDialog(numFishCaught)
            else:
                self.fsm.request('waiting', [
                    False])
        

    
    def _DistributedFishingSpot__allowSellFish(self):
        if base.wantBingo:
            if self.pond.hasPondBingoManager():
                hoodId = base.cr.playGame.getPlaceId()
                if hoodId == ToontownGlobals.MyEstate:
                    return True
                
            
        
        return False


