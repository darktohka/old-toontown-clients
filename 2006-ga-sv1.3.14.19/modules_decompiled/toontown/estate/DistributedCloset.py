# File: D (Python 2.2)

from direct.gui.DirectGui import *
from toontown.toonbase.ToontownGlobals import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import ToontownGlobals
from direct.showbase import PandaObject
from toontown.toon import ToonDNA
from direct.fsm import StateData
import ClosetGUI
import ClosetGlobals
import DistributedFurnitureItem
from toontown.toonbase import TTLocalizer

class DistributedCloset(DistributedFurnitureItem.DistributedFurnitureItem):
    notify = directNotify.newCategory('DistributedCloset')
    
    def __init__(self, cr):
        DistributedFurnitureItem.DistributedFurnitureItem.__init__(self, cr)
        self.notify.debug('__init__')
        self.lastAvId = 0
        self.hasLocalAvatar = 0
        self.lastTime = 0
        self.av = None
        self.closetGUI = None
        self.closetModel = None
        self.closetSphere = None
        self.closetSphereNode = None
        self.closetSphereNodePath = None
        self.topList = []
        self.botList = []
        self.oldTopList = []
        self.oldBotList = []
        self.oldStyle = None
        self.button = None
        self.topTrashButton = None
        self.bottomTrashButton = None
        self.isLocalToon = None
        self.popupInfo = None
        self.isOwner = 0
        self.ownerId = 0
        self.customerId = 0
        self.purchaseDoneEvent = ''
        self.swapEvent = ''
        self.locked = 0
        self.gender = None
        self.topDeleted = 0
        self.bottomDeleted = 0
        self.closetTrack = None
        self.avMoveTrack = None
        self.fsm = ClassicFSM.ClassicFSM('Closet', [
            State.State('off', self.enterOff, self.exitOff, [
                'ready',
                'open',
                'closed']),
            State.State('ready', self.enterReady, self.exitReady, [
                'open',
                'closed']),
            State.State('closed', self.enterClosed, self.exitClosed, [
                'open',
                'off']),
            State.State('open', self.enterOpen, self.exitOpen, [
                'closed',
                'off'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def generate(self):
        DistributedFurnitureItem.DistributedFurnitureItem.generate(self)

    
    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        self.setupCollisionSphere()
        self.load()
        self.fsm.request('ready')

    
    def load(self):
        self.setTwoSided(1)
        lNode = self.find('**/door_rotate_L')
        lDoor = self.find('**/closetdoor_L')
        if lNode.isEmpty() or lDoor.isEmpty():
            self.leftDoor = None
        else:
            lDoor.wrtReparentTo(lNode)
            self.leftDoor = lNode
        rNode = self.find('**/door_rotate_R')
        rDoor = self.find('**/closetdoor_R')
        if rNode.isEmpty() or rDoor.isEmpty():
            self.rightDoor = None
        else:
            rDoor.wrtReparentTo(rNode)
            self.rightDoor = rNode

    
    def setupCollisionSphere(self):
        if self.ownerId:
            self.closetSphereEvent = self.uniqueName('closetSphere')
            self.closetSphereEnterEvent = 'enter' + self.closetSphereEvent
            self.closetSphere = CollisionSphere(0, 0, 0, 1.8)
            self.closetSphere.setTangible(0)
            self.closetSphereNode = CollisionNode(self.closetSphereEvent)
            self.closetSphereNode.setIntoCollideMask(WallBitmask)
            self.closetSphereNode.addSolid(self.closetSphere)
            self.closetSphereNodePath = self.attachNewNode(self.closetSphereNode)
        

    
    def disable(self):
        self.notify.debug('disable')
        self.ignore(self.closetSphereEnterEvent)
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupChangeClothesGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        taskMgr.remove(self.uniqueName('lerpToon'))
        if self.closetTrack:
            self.closetTrack.finish()
            self.closetTrack = None
        
        if self.closetGUI:
            self.closetGUI.resetClothes(self.oldStyle)
            self.resetCloset()
        
        if self.hasLocalAvatar:
            self.freeAvatar()
        
        self.ignoreAll()
        DistributedFurnitureItem.DistributedFurnitureItem.disable(self)

    
    def delete(self):
        self.notify.debug('delete')
        DistributedFurnitureItem.DistributedFurnitureItem.delete(self)
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        if self.av:
            del self.av
        
        del self.gender
        del self.closetSphere
        del self.closetSphereNode
        del self.closetSphereNodePath
        del self.closetGUI
        del self.fsm

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterReady(self):
        if self.ownerId:
            self.accept(self.closetSphereEnterEvent, self.handleEnterSphere)
        

    
    def exitReady(self):
        pass

    
    def enterOpen(self):
        if self.ownerId:
            self.ignore(self.closetSphereEnterEvent)
            self._DistributedCloset__openDoors()
            if self.customerId == base.localAvatar.doId:
                camera.wrtReparentTo(self)
                camera.lerpPosHpr(-7.5800000000000001, -6.0199999999999996, 6.9000000000000004, 286.30000000000001, 336.80000000000001, 0, 1, other = self, blendType = 'easeOut', task = self.uniqueName('lerpCamera'))
                camera.setPosHpr(self, -7.5800000000000001, -6.0199999999999996, 6.9000000000000004, 286.30000000000001, 336.80000000000001, 0)
            
            if self.av:
                if self.avMoveTrack:
                    self.avMoveTrack.finish()
                
                self.av.stopSmooth()
                self.avMoveTrack = Sequence(Parallel(Func(self.av.play, 'walk'), LerpPosHprInterval(nodePath = self.av, other = self, duration = 1.0, pos = Vec3(1.6699999999999999, -3.29, 0.025000000000000001), hpr = Vec3(112, 0, 0), blendType = 'easeOut')), Func(self.av.loop, 'neutral'), Func(self.av.startSmooth))
                self.avMoveTrack.start()
            
        

    
    def exitOpen(self):
        if self.ownerId:
            self._DistributedCloset__closeDoors()
        

    
    def enterClosed(self):
        if self.ownerId:
            self.accept(self.closetSphereEnterEvent, self.handleEnterSphere)
        

    
    def exitClosed(self):
        pass

    
    def handleEnterSphere(self, collEntry):
        if self.smoothStarted:
            return None
        
        if base.localAvatar.doId == self.lastAvId and globalClock.getFrameTime() <= self.lastTime + 0.5:
            self.notify.info('Ignoring duplicate entry for avatar.')
            return None
        
        if self.hasLocalAvatar:
            self.freeAvatar()
        
        self.notify.debug('Entering Closet Sphere....%s' % self.closetSphereEnterEvent)
        if self.cr.playGame.getPlace() == None:
            self.notify.info('Not opening closet before place is defined.')
            return None
        
        self.ignore(self.closetSphereEnterEvent)
        if not (self.locked):
            self.cr.playGame.getPlace().fsm.request('closet')
            self.sendUpdate('enterAvatar', [])
            self.hasLocalAvatar = 1
        

    
    def setState(self, mode, avId, ownerId, gender, topList, botList):
        self.notify.debug('setState, mode=%s, avId=%s, ownerId=%d' % (mode, avId, ownerId))
        self.isOwner = avId == ownerId
        self.ownerGender = gender
        if mode == ClosetGlobals.CLOSED:
            self.fsm.request('closed')
            return None
        elif mode == ClosetGlobals.OPEN:
            self.customerId = avId
            self.av = self.cr.doId2do.get(self.customerId, None)
            if self.av:
                if base.localAvatar.getDoId() == self.customerId:
                    self.gender = self.av.style.gender
                    self.topList = topList
                    self.botList = botList
                    self.oldTopList = self.topList[0:]
                    self.oldBotList = self.botList[0:]
                    print '-----------Starting closet interaction-----------'
                    print 'customerId: %s, gender: %s, ownerId: %s' % (self.av.doId, self.av.style.gender, ownerId)
                    print 'current top = %s,%s,%s,%s and  bot = %s,%s,' % (self.av.style.topTex, self.av.style.topTexColor, self.av.style.sleeveTex, self.av.style.sleeveTexColor, self.av.style.botTex, self.av.style.botTexColor)
                    print 'topsList = %s' % self.av.getClothesTopsList()
                    print 'bottomsList = %s' % self.av.getClothesBottomsList()
                    print '-------------------------------------------------'
                    if not (self.isOwner):
                        self._DistributedCloset__popupNotOwnerPanel()
                    else:
                        taskMgr.doMethodLater(0.5, self.popupChangeClothesGUI, self.uniqueName('popupChangeClothesGUI'))
                
                self.fsm.request('open')
            
        

    
    def _DistributedCloset__revertGender(self):
        if self.gender:
            self.av.style.gender = self.gender
            self.av.loop('neutral')
        

    
    def popupChangeClothesGUI(self, task):
        self.notify.debug('popupChangeClothesGUI')
        self.purchaseDoneEvent = self.uniqueName('purchaseDone')
        self.swapEvent = self.uniqueName('swap')
        self.cancelEvent = self.uniqueName('cancel')
        self.accept(self.purchaseDoneEvent, self._DistributedCloset__proceedToCheckout)
        self.accept(self.swapEvent, self._DistributedCloset__handleSwap)
        self.accept(self.cancelEvent, self._DistributedCloset__handleCancel)
        self.deleteEvent = self.uniqueName('delete')
        if self.isOwner:
            self.accept(self.deleteEvent, self._DistributedCloset__handleDelete)
        
        self.closetGUI = ClosetGUI.ClosetGUI(self.isOwner, self.purchaseDoneEvent, self.cancelEvent, self.swapEvent, self.deleteEvent, self.topList, self.botList)
        self.closetGUI.load()
        if self.gender != self.ownerGender:
            self.closetGUI.setGender(self.ownerGender)
        
        self.closetGUI.enter(base.localAvatar)
        self.closetGUI.showButtons()
        if base.localAvatar.getHeight() > 3.5:
            self.closetGUI.topLButton.setZ(0.10000000000000001)
            self.closetGUI.topRButton.setZ(0.10000000000000001)
            self.closetGUI.bottomLButton.setZ(-0.29999999999999999)
            self.closetGUI.bottomRButton.setZ(-0.29999999999999999)
        else:
            self.closetGUI.topLButton.setZ(0)
            self.closetGUI.topRButton.setZ(0)
            self.closetGUI.bottomLButton.setZ(-0.40000000000000002)
            self.closetGUI.bottomRButton.setZ(-0.40000000000000002)
        style = self.av.getStyle()
        self.oldStyle = ToonDNA.ToonDNA()
        self.oldStyle.makeFromNetString(style.makeNetString())
        return Task.done

    
    def resetCloset(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupChangeClothesGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        taskMgr.remove(self.uniqueName('lerpToon'))
        if self.closetGUI:
            self.closetGUI.hideButtons()
            self.closetGUI.exit()
            self.closetGUI.unload()
            self.closetGUI = None
            del self.av
        
        self.av = base.localAvatar
        style = self.av.getStyle()
        self.oldStyle = ToonDNA.ToonDNA()
        self.oldStyle.makeFromNetString(style.makeNetString())
        self.topDeleted = 0
        self.bottomDeleted = 0
        return Task.done

    
    def _DistributedCloset__handleButton(self):
        messenger.send('next')

    
    def _DistributedCloset__handleCancel(self):
        self.d_setDNA(self.oldStyle.makeNetString(), 1)
        self.closetGUI.resetClothes(self.oldStyle)

    
    def _DistributedCloset__handleSwap(self):
        self.d_setDNA(self.av.getStyle().makeNetString(), 0)

    
    def _DistributedCloset__handleDelete(self, t_or_b):
        if t_or_b == ClosetGlobals.SHIRT:
            itemList = self.closetGUI.tops
            trashIndex = self.closetGUI.topChoice
            swapFunc = self.closetGUI.swapTop
            removeFunc = self.closetGUI.removeTop
            self.topDeleted = self.topDeleted | 1
            
            def setItemChoice(i):
                self.closetGUI.topChoice = i

        else:
            itemList = self.closetGUI.bottoms
            trashIndex = self.closetGUI.bottomChoice
            swapFunc = self.closetGUI.swapBottom
            removeFunc = self.closetGUI.removeBottom
            self.bottomDeleted = self.bottomDeleted | 1
            
            def setItemChoice(i):
                self.closetGUI.bottomChoice = i

        if len(itemList) > 1:
            trashDNA = ToonDNA.ToonDNA()
            trashItem = self.av.getStyle().makeNetString()
            trashDNA.makeFromNetString(trashItem)
            if trashIndex == 0:
                swapFunc(1)
            else:
                swapFunc(-1)
            removeFunc(trashIndex)
            self.sendUpdate('removeItem', [
                trashItem,
                t_or_b])
            swapFunc(0)
            self.closetGUI.updateTrashButtons()
        else:
            self.notify.warning("cant delete this item(type = %s), since we don't have a replacement" % t_or_b)

    
    def resetItemLists(self):
        self.topList = self.oldTopList[0:]
        self.botList = self.oldBotList[0:]
        self.closetGUI.tops = self.topList
        self.closetGUI.bottoms = self.botList
        self.topDeleted = 0
        self.bottomDeleted = 0

    
    def _DistributedCloset__proceedToCheckout(self):
        if self.topDeleted or self.bottomDeleted:
            self._DistributedCloset__popupAreYouSurePanel()
        else:
            self._DistributedCloset__handlePurchaseDone()

    
    def _DistributedCloset__handlePurchaseDone(self, timeout = 0):
        if timeout == 1:
            self.d_setDNA(self.oldStyle.makeNetString(), 1)
        else:
            which = 0
            if self.closetGUI.topChoice != 0 or self.topDeleted:
                which = which | 1
            
            if self.closetGUI.bottomChoice != 0 or self.bottomDeleted:
                which = which | 2
            
            self.d_setDNA(self.av.getStyle().makeNetString(), 2, which)

    
    def d_setDNA(self, dnaString, finished, whichItems = 3):
        self.sendUpdate('setDNA', [
            dnaString,
            finished,
            whichItems])

    
    def setCustomerDNA(self, avId, dnaString):
        if avId and avId != base.localAvatar.doId:
            av = base.cr.doId2do.get(avId, None)
            if av:
                if self.av == base.cr.doId2do[avId]:
                    self.av.style.makeFromNetString(dnaString)
                    self.av.generateToonClothes()
                
            
        

    
    def setMovie(self, mode, avId, timestamp):
        self.isLocalToon = avId == base.localAvatar.doId
        if avId != 0:
            self.lastAvId = avId
        
        self.lastTime = globalClock.getFrameTime()
        if mode == ClosetGlobals.CLOSET_MOVIE_CLEAR:
            return None
        elif mode == ClosetGlobals.CLOSET_MOVIE_COMPLETE:
            if self.isLocalToon:
                self._DistributedCloset__revertGender()
                print '-----------ending closet interaction-----------'
                print 'avid: %s, gender: %s' % (self.av.doId, self.av.style.gender)
                print 'current top = %s,%s,%s,%s and  bot = %s,%s,' % (self.av.style.topTex, self.av.style.topTexColor, self.av.style.sleeveTex, self.av.style.sleeveTexColor, self.av.style.botTex, self.av.style.botTexColor)
                print 'topsList = %s' % self.av.getClothesTopsList()
                print 'bottomsList = %s' % self.av.getClothesBottomsList()
                print '-------------------------------------------------'
                self.resetCloset()
                self.freeAvatar()
                return None
            
        elif mode == ClosetGlobals.CLOSET_MOVIE_TIMEOUT:
            taskMgr.remove(self.uniqueName('lerpCamera'))
            taskMgr.remove(self.uniqueName('lerpToon'))
            if self.isLocalToon:
                self.ignore(self.purchaseDoneEvent)
                self.ignore(self.swapEvent)
                if self.closetGUI:
                    self.closetGUI.resetClothes(self.oldStyle)
                    self._DistributedCloset__handlePurchaseDone(timeout = 1)
                    self.resetCloset()
                
                self._DistributedCloset__popupTimeoutPanel()
                self.freeAvatar()
            
        

    
    def freeAvatar(self):
        self.notify.debug('freeAvatar()')
        if self.hasLocalAvatar:
            base.localAvatar.posCamera(0, 0)
            base.cr.playGame.getPlace().setState('walk')
            base.localAvatar.startLookAround()
            self.hasLocalAvatar = 0
        
        self.lastTime = globalClock.getFrameTime()

    
    def setOwnerId(self, avId):
        self.ownerId = avId

    
    def _DistributedCloset__popupTimeoutPanel(self):
        if self.popupInfo != None:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        self.popupInfo = DirectFrame(parent = hidden, relief = None, state = 'normal', text = TTLocalizer.ClosetTimeoutMessage, frameSize = (-1, 1, -1, 1), geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (0.88, 1, 0.45000000000000001), geom_pos = (0, 0, -0.080000000000000002), text_scale = 0.080000000000000002)
        DirectButton(self.popupInfo, image = okButtonImage, relief = None, text = TTLocalizer.ClosetPopupOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.16), command = self._DistributedCloset__handleTimeoutMessageOK)
        buttons.removeNode()
        self.popupInfo.reparentTo(aspect2d)

    
    def _DistributedCloset__handleTimeoutMessageOK(self):
        self.popupInfo.reparentTo(hidden)

    
    def _DistributedCloset__popupNotOwnerPanel(self):
        if self.popupInfo != None:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        self.popupInfo = DirectFrame(parent = hidden, relief = None, state = 'normal', text = TTLocalizer.ClosetNotOwnerMessage, frameSize = (-1, 1, -1, 1), text_wordwrap = 10, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (0.88, 1, 0.55000000000000004), geom_pos = (0, 0, -0.080000000000000002), text_scale = 0.080000000000000002, text_pos = (0, 0.059999999999999998))
        DirectButton(self.popupInfo, image = okButtonImage, relief = None, text = TTLocalizer.ClosetPopupOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.20999999999999999), command = self._DistributedCloset__handleNotOwnerMessageOK)
        buttons.removeNode()
        self.popupInfo.reparentTo(aspect2d)

    
    def _DistributedCloset__handleNotOwnerMessageOK(self):
        self.popupInfo.reparentTo(hidden)
        taskMgr.doMethodLater(0.10000000000000001, self.popupChangeClothesGUI, self.uniqueName('popupChangeClothesGUI'))

    
    def _DistributedCloset__popupAreYouSurePanel(self):
        if self.popupInfo != None:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
        self.popupInfo = DirectFrame(parent = hidden, relief = None, state = 'normal', text = TTLocalizer.ClosetAreYouSureMessage, frameSize = (-1, 1, -1, 1), text_wordwrap = 10, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (0.88, 1, 0.55000000000000004), geom_pos = (0, 0, -0.080000000000000002), text_scale = 0.080000000000000002, text_pos = (0, 0.080000000000000002))
        DirectButton(self.popupInfo, image = okButtonImage, relief = None, text = TTLocalizer.ClosetPopupOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (-0.10000000000000001, 0.0, -0.20999999999999999), command = self._DistributedCloset__handleYesImSure)
        DirectButton(self.popupInfo, image = cancelButtonImage, relief = None, text = TTLocalizer.ClosetPopupCancel, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.10000000000000001, 0.0, -0.20999999999999999), command = self._DistributedCloset__handleNotSure)
        buttons.removeNode()
        self.popupInfo.reparentTo(aspect2d)

    
    def _DistributedCloset__handleYesImSure(self):
        self.popupInfo.reparentTo(hidden)
        self._DistributedCloset__handlePurchaseDone()

    
    def _DistributedCloset__handleNotSure(self):
        self.popupInfo.reparentTo(hidden)

    
    def _DistributedCloset__openDoors(self):
        if self.closetTrack:
            self.closetTrack.finish()
        
        leftHpr = Vec3(-110, 0, 0)
        rightHpr = Vec3(110, 0, 0)
        self.closetTrack = Parallel()
        if self.rightDoor:
            self.closetTrack.append(self.rightDoor.hprInterval(0.5, rightHpr))
        
        if self.leftDoor:
            self.closetTrack.append(self.leftDoor.hprInterval(0.5, leftHpr))
        
        self.closetTrack.start()

    
    def _DistributedCloset__closeDoors(self):
        if self.closetTrack:
            self.closetTrack.finish()
        
        leftHpr = Vec3(0, 0, 0)
        rightHpr = Vec3(0, 0, 0)
        self.closetTrack = Parallel()
        if self.rightDoor:
            self.closetTrack.append(self.rightDoor.hprInterval(0.5, rightHpr))
        
        if self.leftDoor:
            self.closetTrack.append(self.leftDoor.hprInterval(0.5, leftHpr))
        
        self.closetTrack.start()


