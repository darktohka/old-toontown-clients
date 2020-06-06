# File: P (Python 2.2)

from PurchaseBase import *
from toontown.toon import ToonHead
from toontown.toonbase import ToontownTimer
from direct.gui.DirectGuiGlobals import NORMAL, DISABLED
from direct.directnotify import DirectNotifyGlobal
COUNT_UP_RATE = 0.14999999999999999
DELAY_BEFORE_COUNT_UP = 1.25
DELAY_AFTER_COUNT_UP = 1.75
COUNT_DOWN_RATE = 0.074999999999999997
DELAY_AFTER_COUNT_DOWN = 0.0
DELAY_AFTER_CELEBRATE = 3.0

class Purchase(PurchaseBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('Purchase')
    
    def __init__(self, toon, pointsArray, playerMoney, ids, states, remain, doneEvent):
        PurchaseBase.__init__(self, toon, doneEvent)
        self.ids = ids
        self.pointsArray = pointsArray
        self.playerMoney = playerMoney
        self.states = states
        self.remain = remain
        self.tutorialMode = 0
        self.fsm.addState(State.State('reward', self.enterReward, self.exitReward, [
            'purchase']))
        doneState = self.fsm.getStateNamed('done')
        doneState.addTransition('reward')

    
    def load(self):
        purchaseModels = loader.loadModel('phase_4/models/gui/purchase_gui')
        PurchaseBase.load(self, purchaseModels)
        interiorPhase = 3.5
        self.bg = loader.loadModel('phase_%s/models/modules/toon_interior' % interiorPhase)
        self.bg.setPos(0.0, 5.0, -1.0)
        self.wt = self.bg.find('**/random_tc1_TI_wallpaper')
        wallTex = loader.loadTexture('phase_%s/maps/wall_paper_a5.jpg' % interiorPhase)
        self.wt.setTexture(wallTex, 100)
        self.wt.setColorScale(0.80000000000000004, 0.67000000000000004, 0.54900000000000004, 1.0)
        self.bt = self.bg.find('**/random_tc1_TI_wallpaper_border')
        wallTex = loader.loadTexture('phase_%s/maps/wall_paper_a5.jpg' % interiorPhase)
        self.bt.setTexture(wallTex, 100)
        self.bt.setColorScale(0.80000000000000004, 0.67000000000000004, 0.54900000000000004, 1.0)
        self.wb = self.bg.find('**/random_tc1_TI_wainscotting')
        wainTex = loader.loadTexture('phase_%s/maps/wall_paper_b4.jpg' % interiorPhase)
        self.wb.setTexture(wainTex, 100)
        self.wb.setColorScale(0.47299999999999998, 0.67500000000000004, 0.48799999999999999, 1.0)
        self.playAgain = DirectButton(parent = self.frame, relief = None, scale = 1.04, pos = (0.66000000000000003, 0, -0.23999999999999999), image = (purchaseModels.find('**/PurchScrn_BTN_UP'), purchaseModels.find('**/PurchScrn_BTN_DN'), purchaseModels.find('**/PurchScrn_BTN_RLVR'), purchaseModels.find('**/PurchScrn_BTN_UP')), text = TTLocalizer.GagShopPlayAgain, text_fg = (0, 0.10000000000000001, 0.69999999999999996, 1), text_scale = 0.050000000000000003, text_pos = (0, 0.014999999999999999, 0), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1), text3_fg = Vec4(0, 0, 0.40000000000000002, 1), command = self._Purchase__handlePlayAgain)
        self.backToPlayground = DirectButton(parent = self.frame, relief = None, scale = 1.04, pos = (0.66000000000000003, 0, -0.044999999999999998), image = (purchaseModels.find('**/PurchScrn_BTN_UP'), purchaseModels.find('**/PurchScrn_BTN_DN'), purchaseModels.find('**/PurchScrn_BTN_RLVR'), purchaseModels.find('**/PurchScrn_BTN_UP')), text = TTLocalizer.GagShopBackToPlayground, text_fg = (0, 0.10000000000000001, 0.69999999999999996, 1), text_scale = 0.050000000000000003, text_pos = (0, 0.014999999999999999, 0), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1), text3_fg = Vec4(0, 0, 0.40000000000000002, 1), command = self._Purchase__handleBackToPlayground)
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(self.frame)
        self.timer.posInTopRightCorner()
        numAvs = 0
        count = 0
        localToonIndex = 0
        for index in range(len(self.ids)):
            avId = self.ids[index]
            if avId == base.localAvatar.doId:
                localToonIndex = index
            
            if self.states[index] != PURCHASE_NO_CLIENT_STATE and self.states[index] != PURCHASE_DISCONNECTED_STATE:
                numAvs = numAvs + 1
            
        
        layoutList = (None, (0,), (0, 2), (0, 1, 3), (0, 1, 2, 3))
        layout = layoutList[numAvs]
        headFramePosList = (Vec3(0.050000000000000003, 0, -0.38400000000000001), Vec3(0.050000000000000003, 0, -0.77600000000000002), Vec3(0.80000000000000004, 0, -0.55500000000000005), Vec3(-0.70399999999999996, 0, -0.55500000000000005))
        AVID_INDEX = 0
        LAYOUT_INDEX = 1
        TOON_INDEX = 2
        self.avInfoArray = [
            (base.localAvatar.doId, headFramePosList[0], localToonIndex)]
        pos = 1
        for index in range(len(self.ids)):
            avId = self.ids[index]
            if self.states[index] != PURCHASE_NO_CLIENT_STATE and self.states[index] != PURCHASE_DISCONNECTED_STATE:
                if avId != base.localAvatar.doId:
                    if base.cr.doId2do.has_key(avId):
                        self.avInfoArray.append((avId, headFramePosList[layout[pos]], index))
                        pos = pos + 1
                    
                
            
        
        self.headFrames = []
        for avInfo in self.avInfoArray:
            av = base.cr.doId2do.get(avInfo[AVID_INDEX])
            if av:
                headFrame = PurchaseHeadFrame(av, purchaseModels)
                headFrame.setAvatarState(self.states[avInfo[TOON_INDEX]])
                headFrame.setPos(avInfo[LAYOUT_INDEX])
                self.headFrames.append((avInfo[AVID_INDEX], headFrame))
            
        
        purchaseModels.removeNode()
        self.foreground = loader.loadModelCopy('phase_3.5/models/modules/TT_A1')
        self.foreground.setPos(12.5, -20, -5.5)
        self.foreground.setHpr(180, 0, 0)
        self.backgroundL = loader.loadModelCopy('phase_3.5/models/modules/TT_A1')
        self.backgroundL.setPos(-12.5, -25, -5)
        self.backgroundL.setHpr(180, 0, 0)
        self.backgroundR = self.backgroundL.copyTo(hidden)
        self.backgroundR.setPos(20, -25, -5)
        streets = loader.loadModelOnce('phase_3.5/models/modules/street_modules')
        sidewalk = streets.find('**/street_sidewalk_40x40')
        self.sidewalk = sidewalk.copyTo(hidden)
        self.sidewalk.setPos(-20, -25, -5.5)
        self.sidewalk.setColor(0.90000000000000002, 0.59999999999999998, 0.40000000000000002)
        streets.removeNode()
        doors = loader.loadModelOnce('phase_4/models/modules/doors')
        door = doors.find('**/door_single_square_ur_door')
        self.door = door.copyTo(hidden)
        self.door.setH(180)
        self.door.setPos(0, -16.75, -5.5)
        self.door.setScale(1.5, 1.5, 2.0)
        self.door.setColor(1.0, 0.80000000000000004, 0, 1)
        doors.removeNode()
        self.countSound = base.loadSfx('phase_3.5/audio/sfx/tick_counter.mp3')
        self.overMaxSound = base.loadSfx('phase_3.5/audio/sfx/AV_collision.mp3')
        self.celebrateSound = base.loadSfx('phase_4/audio/sfx/MG_win.mp3')

    
    def unload(self):
        PurchaseBase.unload(self)
        self.bg.removeNode()
        del self.bg
        for headFrame in self.headFrames:
            headFrame[1].reparentTo(hidden)
            headFrame[1].destroy()
        
        del self.headFrames
        del self.playAgain
        del self.backToPlayground
        del self.timer
        for counter in self.counters:
            counter.destroy()
            del counter
        
        del self.counters
        for total in self.totalCounters:
            total.destroy()
            del total
        
        del self.totalCounters
        loader.unloadModel('phase_3.5/models/modules/TT_A1')
        loader.unloadModel('phase_3.5/models/modules/street_modules')
        loader.unloadModel('phase_4/models/modules/doors')
        self.foreground.removeNode()
        del self.foreground
        self.backgroundL.removeNode()
        del self.backgroundL
        self.backgroundR.removeNode()
        del self.backgroundR
        self.sidewalk.removeNode()
        del self.sidewalk
        self.door.removeNode()
        del self.door
        self.collisionFloor.removeNode()
        del self.collisionFloor
        del self.countSound
        del self.celebrateSound
        return None

    
    def showStatusText(self, text):
        self.statusLabel['text'] = text
        taskMgr.remove('resetStatusText')
        taskMgr.doMethodLater(2.0, self.resetStatusText, 'resetStatusText')
        return None

    
    def resetStatusText(self, task):
        self.statusLabel['text'] = ''
        return Task.done

    
    def _Purchase__handlePlayAgain(self):
        for headFrame in self.headFrames:
            headFrame[1].wrtReparentTo(aspect2d)
        
        self.toon.inventory.reparentTo(hidden)
        self.toon.inventory.hide()
        taskMgr.remove('resetStatusText')
        taskMgr.remove('showBrokeMsgTask')
        self.statusLabel['text'] = TTLocalizer.GagShopWaitingOtherPlayers
        messenger.send('purchasePlayAgain')
        return None

    
    def handleDone(self, playAgain):
        base.localAvatar.b_setParent(ToontownGlobals.SPHidden)
        if playAgain:
            self.doneStatus = {
                'loader': 'minigame',
                'where': 'minigame' }
        else:
            self.doneStatus = {
                'loader': 'safeZoneLoader',
                'where': 'playground' }
        messenger.send(self.doneEvent)

    
    def _Purchase__handleBackToPlayground(self):
        self.toon.inventory.reparentTo(hidden)
        self.toon.inventory.hide()
        messenger.send('purchaseBackToToontown')
        return None

    
    def _Purchase__timerExpired(self):
        messenger.send('purchaseTimeout')
        return None

    
    def findHeadFrame(self, id):
        for headFrame in self.headFrames:
            if headFrame[0] == id:
                return headFrame[1]
            
        
        return None

    
    def _Purchase__handleStateChange(self, playerStates):
        self.states = playerStates
        for avInfo in self.avInfoArray:
            index = avInfo[2]
            headFrame = self.findHeadFrame(avInfo[0])
            state = self.states[index]
            headFrame.setAvatarState(state)
        

    
    def enter(self):
        base.playMusic(self.music, looping = 1, volume = 0.80000000000000004)
        self.fsm.request('reward')

    
    def enterReward(self):
        numToons = 0
        toonLayouts = ((2,), (1, 3), (0, 2, 4), (0, 1, 3, 4))
        toonPositions = (5.0, 1.75, -0.25, -1.75, -5.0)
        self.toons = []
        self.toonsKeep = []
        self.counters = []
        self.totalCounters = []
        camera.reparentTo(render)
        base.camLens.setFov(ToontownGlobals.DefaultCameraFov)
        camera.setPos(0, 16.0, 2.0)
        camera.lookAt(0, 0, 0.75)
        base.transitions.irisIn(0.40000000000000002)
        self.title.reparentTo(aspect2d)
        self.foreground.reparentTo(render)
        self.backgroundL.reparentTo(render)
        self.backgroundR.reparentTo(render)
        self.sidewalk.reparentTo(render)
        self.door.reparentTo(render)
        size = 20
        z = -2.5
        floor = CollisionPolygon(Point3(-size, -size, z), Point3(size, -size, z), Point3(size, size, z), Point3(-size, size, z))
        floor.setTangible(1)
        floorNode = CollisionNode('collision_floor')
        floorNode.addSolid(floor)
        self.collisionFloor = render.attachNewNode(floorNode)
        NametagGlobals.setOnscreenChatForced(1)
        for index in range(len(self.ids)):
            avId = self.ids[index]
            if self.states[index] != PURCHASE_NO_CLIENT_STATE and self.states[index] != PURCHASE_DISCONNECTED_STATE and avId in base.cr.doId2do:
                numToons += 1
                toon = base.cr.doId2do[avId]
                toon.stopSmooth()
                self.toons.append(toon)
                self.toonsKeep.append(DelayDelete.DelayDelete(toon))
                counter = DirectLabel(parent = hidden, relief = None, pos = (0.0, 0.0, 0.0), text = str(0), text_scale = 0.20000000000000001, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_pos = (0, -0.10000000000000001, 0), text_font = ToontownGlobals.getSignFont())
                counter['image'] = getDefaultDialogGeom()
                counter['image_scale'] = (0.33000000000000002, 1, 0.33000000000000002)
                counter.setScale(0.5)
                counter.count = 0
                counter.max = self.pointsArray[index]
                self.counters.append(counter)
                money = self.playerMoney[index]
                totalCounter = DirectLabel(parent = hidden, relief = None, pos = (0.0, 0.0, 0.0), text = str(money), text_scale = 0.20000000000000001, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_pos = (0, -0.10000000000000001, 0), text_font = ToontownGlobals.getSignFont(), image = self.jarImage)
                totalCounter.setScale(0.5)
                totalCounter.count = money
                totalCounter.max = toon.getMaxMoney()
                self.totalCounters.append(totalCounter)
            
        
        pos = 0
        toonLayout = toonLayouts[numToons - 1]
        for toon in self.toons:
            thisPos = toonPositions[toonLayout[pos]]
            toon.setPos(Vec3(thisPos, 1.0, -2.5))
            toon.setHpr(Vec3(0, 0, 0))
            toon.setAnimState('neutral', 1)
            toon.setShadowHeight(0)
            if not toon.isDisabled():
                toon.reparentTo(render)
            
            self.counters[pos].setPos(thisPos * -0.17000000000000001, 0, toon.getHeight() / 10 + 0.25)
            self.counters[pos].reparentTo(aspect2d)
            self.totalCounters[pos].setPos(thisPos * -0.17000000000000001, 0, -0.82499999999999996)
            self.totalCounters[pos].reparentTo(aspect2d)
            pos += 1
        
        self.maxPoints = max(self.pointsArray)
        
        def reqCountUp(state):
            self.countUp()
            return Task.done

        countUpDelay = DELAY_BEFORE_COUNT_UP
        taskMgr.doMethodLater(countUpDelay, reqCountUp, 'countUpTask')
        
        def reqCountDown(state):
            self.countDown()
            return Task.done

        countDownDelay = countUpDelay + self.maxPoints * COUNT_UP_RATE + DELAY_AFTER_COUNT_UP
        taskMgr.doMethodLater(countDownDelay, reqCountDown, 'countDownTask')
        
        def celebrate(task):
            for counter in task.counters:
                counter.reparentTo(hidden)
            
            winningPoints = max(task.pointsArray)
            for i in range(len(task.ids)):
                if task.pointsArray[i] == winningPoints:
                    avId = task.ids[i]
                    if base.cr.doId2do.has_key(avId):
                        toon = base.cr.doId2do[avId]
                        toon.setAnimState('jump', 1.0)
                    
                
            
            base.playSfx(task.celebrateSound)
            return Task.done

        celebrateDelay = countDownDelay + self.maxPoints * COUNT_DOWN_RATE + DELAY_AFTER_COUNT_DOWN
        celebrateTask = taskMgr.doMethodLater(celebrateDelay, celebrate, 'celebrate')
        celebrateTask.counters = self.counters
        celebrateTask.pointsArray = self.pointsArray
        celebrateTask.ids = self.ids
        celebrateTask.celebrateSound = self.celebrateSound
        
        def reqPurchase(state):
            self.fsm.request('purchase')
            return Task.done

        purchaseDelay = celebrateDelay + DELAY_AFTER_CELEBRATE
        taskMgr.doMethodLater(purchaseDelay, reqPurchase, 'purchase-trans')
        if base.skipMinigameReward:
            self.fsm.request('purchase')
        

    
    def countUp(self):
        totalDelay = 0
        
        def delayAdd(state):
            state.counter.count += 1
            state.counter['text'] = str(state.counter.count)
            if state.id == base.localAvatar.doId:
                base.playSfx(state.countSound)
            
            return Task.done

        for count in range(0, self.maxPoints):
            for counter in self.counters:
                index = self.counters.index(counter)
                if count < counter.max:
                    addTask = taskMgr.doMethodLater(totalDelay, delayAdd, 'delayAdd')
                    addTask.counter = counter
                    addTask.id = self.ids[index]
                    addTask.countSound = self.countSound
                
            
            totalDelay += COUNT_UP_RATE
        

    
    def countDown(self):
        totalDelay = 0
        
        def delaySubtract(state):
            state.counter.count -= 1
            state.counter['text'] = str(state.counter.count)
            state.total.count += 1
            if state.total.count <= state.total.max:
                state.total['text'] = str(state.total.count)
            
            if state.total.count == state.total.max + 1:
                state.total['text_fg'] = (1, 0, 0, 1)
            
            if state.id == base.localAvatar.doId:
                if state.total.count <= state.total.max:
                    base.playSfx(state.countSound)
                else:
                    base.playSfx(state.overMaxSound)
            
            return Task.done

        for count in range(0, self.maxPoints):
            for counter in self.counters:
                if count < counter.max:
                    index = self.counters.index(counter)
                    subtractTask = taskMgr.doMethodLater(totalDelay, delaySubtract, 'delaySubtract')
                    subtractTask.counter = counter
                    subtractTask.total = self.totalCounters[index]
                    subtractTask.id = self.ids[index]
                    subtractTask.countSound = self.countSound
                    subtractTask.overMaxSound = self.overMaxSound
                
            
            totalDelay += COUNT_DOWN_RATE
        

    
    def exitReward(self):
        taskMgr.remove('countUpTask')
        taskMgr.remove('countDownTask')
        taskMgr.remove('celebrate')
        taskMgr.remove('purchase-trans')
        taskMgr.remove('delayAdd')
        taskMgr.remove('delaySubtract')
        for toon in self.toons:
            toon.detachNode()
        
        del self.toons
        del self.toonsKeep
        for counter in self.counters:
            counter.reparentTo(hidden)
        
        for total in self.totalCounters:
            total.reparentTo(hidden)
        
        self.foreground.reparentTo(hidden)
        self.backgroundL.reparentTo(hidden)
        self.backgroundR.reparentTo(hidden)
        self.sidewalk.reparentTo(hidden)
        self.door.reparentTo(hidden)
        self.title.reparentTo(self.frame)
        NametagGlobals.setOnscreenChatForced(0)

    
    def enterPurchase(self):
        PurchaseBase.enterPurchase(self)
        self.bg.reparentTo(render)
        base.setBackgroundColor(0.050000000000000003, 0.14000000000000001, 0.40000000000000002)
        self.accept('purchaseStateChange', self._Purchase__handleStateChange)
        self.playAgain.reparentTo(self.toon.inventory.purchaseFrame)
        self.backToPlayground.reparentTo(self.toon.inventory.purchaseFrame)
        self.pointDisplay.reparentTo(self.toon.inventory.purchaseFrame)
        self.statusLabel.reparentTo(self.toon.inventory.purchaseFrame)
        for headFrame in self.headFrames:
            headFrame[1].show()
            headFrame[1].reparentTo(self.toon.inventory.purchaseFrame)
        
        if base.cr.periodTimerExpired:
            base.cr.loginFSM.request('periodTimeout')
            return None
        
        if not (self.tutorialMode):
            if not config.GetBool('disable-purchase-timer', 0):
                self.timer.countdown(self.remain, self._Purchase__timerExpired)
            
        else:
            self.timer.hide()
            self.disablePlayAgain()
            self.accept('disableGagPanel', Functor(self.toon.inventory.setActivateMode, 'gagTutDisabled', gagTutMode = 1))
            self.accept('disableBackToPlayground', self.disableBackToPlayground)
            self.accept('enableGagPanel', self.handleEnableGagPanel)
            self.accept('enableBackToPlayground', self.enableBackToPlayground)
            for (avId, headFrame) in self.headFrames:
                if avId != self.newbieId:
                    headFrame.hide()
                
            
        messenger.send('gagScreenIsUp')
        if base.autoPlayAgain:
            self._Purchase__handlePlayAgain()
        

    
    def exitPurchase(self):
        PurchaseBase.exitPurchase(self)
        self.ignore('disableGagPanel')
        self.ignore('disableBackToPlayground')
        self.ignore('enableGagPanel')
        self.ignore('enableBackToPlayground')
        self.bg.reparentTo(hidden)
        self.playAgain.reparentTo(self.frame)
        self.backToPlayground.reparentTo(self.frame)
        self.pointDisplay.reparentTo(self.frame)
        self.statusLabel.reparentTo(self.frame)
        self.ignore('purchaseStateChange')
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)

    
    def disableBackToPlayground(self):
        self.backToPlayground['state'] = DISABLED

    
    def enableBackToPlayground(self):
        self.backToPlayground['state'] = NORMAL

    
    def disablePlayAgain(self):
        self.playAgain['state'] = DISABLED

    
    def enablePlayAgain(self):
        self.playAgain['state'] = NORMAL

    
    def enterTutorialMode(self, newbieId):
        self.tutorialMode = 1
        self.newbieId = newbieId

    
    def handleEnableGagPanel(self):
        self.toon.inventory.setActivateMode('purchase', gagTutMode = 1)
        self.checkForBroke()

    
    def handleGagTutorialDone(self):
        self.enableBackToPlayground()



class PurchaseHeadFrame(DirectFrame):
    
    def __init__(self, av, purchaseModels):
        DirectFrame.__init__(self, relief = None, image = purchaseModels.find('**/Char_Pnl'))
        self.initialiseoptions(PurchaseHeadFrame)
        self.statusLabel = DirectLabel(parent = self, relief = None, text = '', text_scale = 0.080000000000000002, text_wordwrap = 7.5, text_fg = (0.050000000000000003, 0.14000000000000001, 0.40000000000000002, 1), text_pos = (0.10000000000000001, 0, 0))
        self.av = av
        self.avKeep = DelayDelete.DelayDelete(av)
        self.head = self.stateNodePath[0].attachNewNode('head', 20)
        self.head.setPosHprScale(-0.22, 10.0, -0.10000000000000001, 180.0, 0.0, 0.0, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001)
        self.headModel = ToonHead.ToonHead()
        self.headModel.setupHead(self.av.style, forGui = 1)
        self.headModel.reparentTo(self.head)
        self.tag2Node = NametagFloat2d()
        self.tag2Node.setContents(Nametag.CName)
        self.av.nametag.addNametag(self.tag2Node)
        self.tag2 = self.attachNewNode(self.tag2Node.upcastToPandaNode())
        self.tag2.setPosHprScale(-0.22, 10.0, 0.12, 0, 0, 0, 0.045999999999999999, 0.045999999999999999, 0.045999999999999999)
        self.tag1Node = NametagFloat2d()
        self.tag1Node.setContents(Nametag.CSpeech | Nametag.CThought)
        self.av.nametag.addNametag(self.tag1Node)
        self.tag1 = self.attachNewNode(self.tag1Node.upcastToPandaNode())
        self.tag1.setPosHprScale(-0.14999999999999999, 0, -0.10000000000000001, 0, 0, 0, 0.045999999999999999, 0.045999999999999999, 0.045999999999999999)
        self.hide()

    
    def destroy(self):
        DirectFrame.destroy(self)
        del self.statusLabel
        self.headModel.delete()
        del self.headModel
        self.head.removeNode()
        del self.head
        self.av.nametag.removeNametag(self.tag1Node)
        self.av.nametag.removeNametag(self.tag2Node)
        self.tag1.removeNode()
        self.tag2.removeNode()
        del self.tag1
        del self.tag2
        del self.tag1Node
        del self.tag2Node
        del self.av
        del self.avKeep

    
    def setAvatarState(self, state):
        if state == PURCHASE_DISCONNECTED_STATE:
            self.statusLabel['text'] = TTLocalizer.GagShopPlayerDisconnected % self.av.getName()
            self.statusLabel['text_pos'] = (0.014999999999999999, 0.071999999999999995, 0)
            self.head.hide()
            self.tag1.hide()
            self.tag2.hide()
        elif state == PURCHASE_EXIT_STATE:
            self.statusLabel['text'] = TTLocalizer.GagShopPlayerExited % self.av.getName()
            self.statusLabel['text_pos'] = (0.014999999999999999, 0.071999999999999995, 0)
            self.head.hide()
            self.tag1.hide()
            self.tag2.hide()
        elif state == PURCHASE_PLAYAGAIN_STATE:
            self.statusLabel['text'] = TTLocalizer.GagShopPlayerPlayAgain
            self.statusLabel['text_pos'] = (0.10000000000000001, -0.12, 0)
        elif state == PURCHASE_WAITING_STATE:
            self.statusLabel['text'] = TTLocalizer.GagShopPlayerBuying
            self.statusLabel['text_pos'] = (0.10000000000000001, -0.12, 0)
        elif state == PURCHASE_NO_CLIENT_STATE:
            Purchase.notify.warning("setAvatarState('no client state'); OK for gag purchase tutorial")
        else:
            Purchase.notify.warning('unknown avatar state: %s' % state)


