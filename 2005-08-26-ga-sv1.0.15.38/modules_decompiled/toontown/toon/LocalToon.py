# File: L (Python 2.2)

from direct.showbase.PandaObject import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from direct.showbase.InputStateGlobal import inputState
from direct.gui.DirectGui import *
import DistributedToon
from otp.avatar import LocalAvatar
import Toon
from toontown.shtiker import ShtikerBook
from toontown.shtiker import InventoryPage
from toontown.shtiker import MapPage
from toontown.shtiker import OptionsPage
from toontown.shtiker import ShardPage
from toontown.shtiker import QuestPage
from toontown.shtiker import TrackPage
from toontown.shtiker import SuitPage
from toontown.shtiker import DisguisePage
from toontown.shtiker import PhotoAlbumPage
from toontown.shtiker import BuildingPage
from toontown.shtiker import FishPage
from toontown.shtiker import NPCFriendPage
import LaffMeter
import whrandom
from toontown.quest import Quests
from toontown.quest import QuestParser
from toontown.toonbase import ToontownGlobals
from direct.showbase import PythonUtil
from toontown.toonbase import TTLocalizer
import math
from direct.directnotify import DirectNotifyGlobal
from otp.avatar import PositionExaminer
from direct.gui import DirectGuiGlobals
from toontown.catalog import CatalogNotifyDialog
from toontown.chat import ToontownChatManager
from otp.otpbase import OTPGlobals

class LocalToon(DistributedToon.DistributedToon, LocalAvatar.LocalAvatar):
    neverDisable = 1
    piePowerSpeed = base.config.GetDouble('pie-power-speed', 0.20000000000000001)
    piePowerExponent = base.config.GetDouble('pie-power-exponent', 0.75)
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.LocalToon_initialized = 1
            DistributedToon.DistributedToon.__init__(self, cr)
            chatMgr = ToontownChatManager.ToontownChatManager(cr, self)
            LocalAvatar.LocalAvatar.__init__(self, cr, chatMgr)
            self.soundRun = base.loadSfx('phase_3.5/audio/sfx/AV_footstep_runloop.wav')
            self.soundWalk = base.loadSfx('phase_3.5/audio/sfx/AV_footstep_walkloop.wav')
            self.soundWhisper = base.loadSfx('phase_3.5/audio/sfx/GUI_whisper_3.mp3')
            self.soundPhoneRing = base.loadSfx('phase_3.5/audio/sfx/telephone_ring.mp3')
            self.positionExaminer = PositionExaminer.PositionExaminer()
            friendsGui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
            friendsButtonNormal = friendsGui.find('**/FriendsBox_Closed')
            friendsButtonPressed = friendsGui.find('**/FriendsBox_Rollover')
            friendsButtonRollover = friendsGui.find('**/FriendsBox_Rollover')
            self.bFriendsList = DirectButton(image = (friendsButtonNormal, friendsButtonPressed, friendsButtonRollover), relief = None, pos = (1.1919999999999999, 0, 0.875), scale = 0.80000000000000004, text = ('', TTLocalizer.FriendsListLabel, TTLocalizer.FriendsListLabel), text_scale = 0.089999999999999997, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.17999999999999999), text_font = ToontownGlobals.getInterfaceFont(), command = self.sendFriendsListEvent)
            self.bFriendsList.hide()
            self.friendsListButtonActive = 0
            self.friendsListButtonObscured = 0
            self.moveFurnitureButtonObscured = 0
            self.clarabelleButtonObscured = 0
            friendsGui.removeNode()
            self._LocalToon__furnitureGui = None
            self._LocalToon__clarabelleButton = None
            self._LocalToon__clarabelleFlash = None
            self.furnitureManager = None
            self.furnitureDirector = None
            self.gotCatalogNotify = 0
            self._LocalToon__catalogNotifyDialog = None
            self.accept('phaseComplete-5.5', self.refreshOnscreenButtons)
            Toon.loadDialog()
            self.isIt = 0
            self.inTutorial = 0
            self.tunnelX = 0.0
            self.estate = None
            self._LocalToon__pieBubble = None
            self.allowPies = 0
            self._LocalToon__pieButton = None
            self._LocalToon__piePowerMeter = None
            self._LocalToon__piePowerMeterSequence = None
            self._LocalToon__pieButtonType = None
            self._LocalToon__pieButtonCount = None
            self.tossPieStart = None
            self._LocalToon__presentingPie = 0
            self._LocalToon__pieSequence = 0
            self.wantBattles = base.config.GetBool('want-battles', 1)
            self.teleportCheat = base.config.GetBool('teleport-all', 0)
            self.seeGhosts = base.config.GetBool('see-ghosts', 0)


    
    def announceGenerate(self):
        self.startLookAround()
        self.nametag.manage(base.marginManager)
        DistributedToon.DistributedToon.announceGenerate(self)

    
    def disable(self):
        self.laffMeter.destroy()
        del self.laffMeter
        self.book.unload()
        del self.optionsPage
        del self.shardPage
        del self.mapPage
        del self.invPage
        del self.questPage
        del self.suitPage
        del self.sosPage
        del self.disguisePage
        del self.fishPage
        del self.trackPage
        del self.book
        self.nametag.unmanage(base.marginManager)
        self.ignoreAll()
        DistributedToon.DistributedToon.disable(self)
        return None

    
    def disableBodyCollisions(self):
        pass

    
    def delete(self):
        
        try:
            pass
        except:
            self.LocalToon_deleted = 1
            Toon.unloadDialog()
            QuestParser.clear()
            DistributedToon.DistributedToon.delete(self)
            LocalAvatar.LocalAvatar.delete(self)
            if self._LocalToon__pieButton:
                self._LocalToon__pieButton.destroy()
                self._LocalToon__pieButton = None
            
            if self._LocalToon__piePowerMeter:
                self._LocalToon__piePowerMeter.destroy()
                self._LocalToon__piePowerMeter = None
            
            taskMgr.remove('lerpFurnitureButton')
            if self._LocalToon__furnitureGui:
                self._LocalToon__furnitureGui.destroy()
            
            del self._LocalToon__furnitureGui
            if self._LocalToon__clarabelleButton:
                self._LocalToon__clarabelleButton.destroy()
            
            del self._LocalToon__clarabelleButton
            if self._LocalToon__clarabelleFlash:
                self._LocalToon__clarabelleFlash.finish()
            
            del self._LocalToon__clarabelleFlash
            if self._LocalToon__catalogNotifyDialog:
                self._LocalToon__catalogNotifyDialog.cleanup()
            
            del self._LocalToon__catalogNotifyDialog


    
    def initInterface(self):
        self.book = ShtikerBook.ShtikerBook('bookDone')
        self.book.load()
        self.book.hideButton()
        self.optionsPage = OptionsPage.OptionsPage()
        self.optionsPage.load()
        self.book.addPage(self.optionsPage, pageName = TTLocalizer.OptionsPageTitle)
        self.shardPage = ShardPage.ShardPage()
        self.shardPage.load()
        self.book.addPage(self.shardPage, pageName = TTLocalizer.ShardPageTitle)
        self.mapPage = MapPage.MapPage()
        self.mapPage.load()
        self.book.addPage(self.mapPage, pageName = TTLocalizer.MapPageTitle)
        self.invPage = InventoryPage.InventoryPage()
        self.invPage.load()
        self.book.addPage(self.invPage, pageName = TTLocalizer.InventoryPageTitle)
        self.questPage = QuestPage.QuestPage()
        self.questPage.load()
        self.book.addPage(self.questPage, pageName = TTLocalizer.QuestPageToonTasks)
        self.trackPage = TrackPage.TrackPage()
        self.trackPage.load()
        self.book.addPage(self.trackPage, pageName = TTLocalizer.TrackPageShortTitle)
        self.suitPage = SuitPage.SuitPage()
        self.suitPage.load()
        self.book.addPage(self.suitPage, pageName = TTLocalizer.SuitPageTitle)
        if base.config.GetBool('want-photo-album', 0):
            self.photoAlbumPage = PhotoAlbumPage.PhotoAlbumPage()
            self.photoAlbumPage.load()
            self.book.addPage(self.photoAlbumPage, pageName = TTLocalizer.PhotoPageTitle)
        
        self.fishPage = FishPage.FishPage()
        self.fishPage.setAvatar(self)
        self.fishPage.load()
        self.book.addPage(self.fishPage, pageName = TTLocalizer.FishPageTitle)
        if self.disguisePageFlag:
            self.loadDisguisePages()
        
        self.book.setPage(self.mapPage)
        self.laffMeter = LaffMeter.LaffMeter(self.style, self.hp, self.maxHp)
        self.laffMeter.setAvatar(self)
        self.laffMeter.setScale(0.074999999999999997)
        if self.style.getAnimal() == 'monkey':
            self.laffMeter.setPos(-1.1799999999999999, 0.0, -0.87)
        else:
            self.laffMeter.setPos(-1.2, 0.0, -0.87)
        self.laffMeter.stop()
        self.accept('time-insert', self._LocalToon__beginTossPie)
        self.accept('time-insert-up', self._LocalToon__endTossPie)
        self.accept('pieHit', self._LocalToon__pieHit)
        self.accept('interrupt-pie', self.interruptPie)
        self.accept('InputState-jump', self._LocalToon__toonMoved)
        self.accept('InputState-forward', self._LocalToon__toonMoved)
        self.accept('InputState-reverse', self._LocalToon__toonMoved)
        self.accept('InputState-turnLeft', self._LocalToon__toonMoved)
        self.accept('InputState-turnRight', self._LocalToon__toonMoved)
        self.accept('InputState-slide', self._LocalToon__toonMoved)
        QuestParser.init()

    
    def setWantBattles(self, wantBattles):
        self.wantBattles = wantBattles

    
    def loadDisguisePages(self):
        if self.disguisePage != None or self.sosPage != None:
            return None
        
        if launcher and not launcher.getPhaseComplete(9):
            self.acceptOnce('phaseComplete-9', self.loadDisguisePages)
            return None
        
        self.disguisePage = DisguisePage.DisguisePage()
        self.disguisePage.load()
        self.book.addPage(self.disguisePage, pageName = TTLocalizer.DisguisePageTitle)
        self.sosPage = NPCFriendPage.NPCFriendPage()
        self.sosPage.load()
        self.book.addPage(self.sosPage, pageName = TTLocalizer.NPCFriendPageTitle)

    
    def displayWhisper(self, fromId, chatString, whisperType):
        LocalAvatar.LocalAvatar.displayWhisper(self, fromId, chatString, whisperType)

    
    def isLocal(self):
        return 1

    
    def canChat(self):
        if not self.cr.allowSecretChat():
            return 0
        
        if self.commonChatFlags & (ToontownGlobals.CommonChat | ToontownGlobals.SuperChat):
            return 1
        
        for (friendId, flags) in self.friendsList:
            if flags & ToontownGlobals.FriendChat:
                return 1
            
        
        return 0

    
    def startChat(self):
        LocalAvatar.LocalAvatar.startChat(self)
        self.accept('chatUpdateSCToontask', self.b_setSCToontask)
        self.accept('chatUpdateSCResistance', self.d_reqSCResistance)
        self.accept('whisperUpdateSCToontask', self.whisperSCToontaskTo)

    
    def stopChat(self):
        LocalAvatar.LocalAvatar.stopChat(self)
        self.ignore('chatUpdateSCToontask')
        self.ignore('chatUpdateSCResistance')
        self.ignore('whisperUpdateSCToontask')

    
    def tunnelIn(self, tunnelOrigin):
        self.b_setTunnelIn(self.tunnelX * 0.80000000000000004, tunnelOrigin)

    
    def tunnelOut(self, tunnelOrigin):
        self.tunnelX = self.getX(tunnelOrigin)
        tunnelY = self.getY(tunnelOrigin)
        self.b_setTunnelOut(self.tunnelX * 0.94999999999999996, tunnelY, tunnelOrigin)

    
    def handleTunnelIn(self, startTime, endX, x, y, z, h):
        self.notify.debug('LocalToon.handleTunnelIn')
        tunnelOrigin = render.attachNewNode('tunnelOrigin')
        tunnelOrigin.setPosHpr(x, y, z, h, 0, 0)
        self.b_setAnimState('run', self.animMultiplier)
        self.stopLookAround()
        self.reparentTo(render)
        self.runSound()
        camera.reparentTo(render)
        camera.setPosHpr(tunnelOrigin, 0, 20, 12, 180, -20, 0)
        base.transitions.irisIn(0.40000000000000002)
        toonTrack = self.getTunnelInToonTrack(endX, tunnelOrigin)
        
        def cleanup(self = self, tunnelOrigin = tunnelOrigin):
            self.stopSound()
            tunnelOrigin.removeNode()
            messenger.send('tunnelInMovieDone')

        self.tunnelTrack = Sequence(toonTrack, Func(cleanup))
        self.tunnelTrack.start(globalClock.getFrameTime() - startTime)

    
    def handleTunnelOut(self, startTime, startX, startY, x, y, z, h):
        self.notify.debug('LocalToon.handleTunnelOut')
        tunnelOrigin = render.attachNewNode('tunnelOrigin')
        tunnelOrigin.setPosHpr(x, y, z, h, 0, 0)
        self.b_setAnimState('run', self.animMultiplier)
        self.runSound()
        self.stopLookAround()
        tracks = Parallel()
        camera.wrtReparentTo(render)
        startPos = camera.getPos(tunnelOrigin)
        startHpr = camera.getHpr(tunnelOrigin)
        camLerpDur = 1.0
        reducedCamH = fitDestAngle2Src(startHpr[0], 180)
        tracks.append(LerpPosHprInterval(camera, camLerpDur, pos = Point3(0, 20, 12), hpr = Point3(reducedCamH, -20, 0), startPos = startPos, startHpr = startHpr, other = tunnelOrigin, blendType = 'easeInOut', name = 'tunnelOutLerpCamPos'))
        toonTrack = self.getTunnelOutToonTrack(startX, startY, tunnelOrigin)
        tracks.append(toonTrack)
        irisDur = 0.40000000000000002
        tracks.append(Sequence(Wait(toonTrack.getDuration() - irisDur + 0.10000000000000001), Func(base.transitions.irisOut, irisDur)))
        
        def cleanup(self = self, tunnelOrigin = tunnelOrigin):
            self.stopSound()
            self.detachNode()
            tunnelOrigin.removeNode()
            messenger.send('tunnelOutMovieDone')

        self.tunnelTrack = Sequence(tracks, Func(cleanup))
        self.tunnelTrack.start(globalClock.getFrameTime() - startTime)

    
    def getPieBubble(self):
        if self._LocalToon__pieBubble == None:
            bubble = CollisionSphere(0, 0, 0, 1)
            node = CollisionNode('pieBubble')
            node.addSolid(bubble)
            node.setFromCollideMask(ToontownGlobals.PieBitmask | ToontownGlobals.CameraBitmask | ToontownGlobals.FloorBitmask)
            node.setIntoCollideMask(BitMask32.allOff())
            self._LocalToon__pieBubble = NodePath(node)
            self.pieHandler = CollisionHandlerEvent()
            self.pieHandler.addInPattern('pieHit')
            self.pieHandler.addInPattern('pieHit-%in')
        
        return self._LocalToon__pieBubble

    
    def _LocalToon__beginTossPieMouse(self, mouseParam):
        self._LocalToon__beginTossPie(globalClock.getFrameTime())

    
    def _LocalToon__endTossPieMouse(self, mouseParam):
        self._LocalToon__endTossPie(globalClock.getFrameTime())

    
    def _LocalToon__beginTossPie(self, time):
        if self.tossPieStart != None:
            return None
        
        if not (self.allowPies):
            return None
        
        if self.numPies == 0:
            messenger.send('outOfPies')
            return None
        
        if self._LocalToon__pieInHand():
            return None
        
        if getattr(self.controlManager.currentControls, 'isAirborne', 0):
            return None
        
        messenger.send('wakeup')
        self.localPresentPie(time)
        taskName = self.uniqueName('updatePiePower')
        taskMgr.add(self._LocalToon__updatePiePower, taskName)

    
    def _LocalToon__endTossPie(self, time):
        if self.tossPieStart == None:
            return None
        
        taskName = self.uniqueName('updatePiePower')
        taskMgr.remove(taskName)
        messenger.send('wakeup')
        power = self._LocalToon__getPiePower(time)
        self.tossPieStart = None
        self.localTossPie(power)

    
    def localPresentPie(self, time):
        import TTEmote
        Emote = Emote
        import otp.avatar
        self._LocalToon__stopPresentPie()
        if self.tossTrack:
            tossTrack = self.tossTrack
            self.tossTrack = None
            tossTrack.finish()
        
        self.interruptPie()
        self.tossPieStart = time
        self._LocalToon__pieSequence = self._LocalToon__pieSequence + 1 & 255
        sequence = self._LocalToon__pieSequence
        self._LocalToon__presentingPie = 1
        pos = self.getPos()
        hpr = self.getHpr()
        timestamp32 = globalClockDelta.getFrameNetworkTime(bits = 32)
        self.sendUpdate('presentPie', [
            pos[0],
            pos[1],
            pos[2],
            hpr[0],
            hpr[1],
            hpr[2],
            timestamp32])
        Emote.globalEmote.disableBody(self)
        messenger.send('begin-pie')
        ival = self.getPresentPieInterval(pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2])
        ival = Sequence(ival, name = self.uniqueName('localPresentPie'))
        self.tossTrack = ival
        ival.start()
        self.makePiePowerMeter()
        self._LocalToon__piePowerMeter.show()
        self._LocalToon__piePowerMeterSequence = sequence
        self._LocalToon__piePowerMeter['value'] = 0

    
    def _LocalToon__stopPresentPie(self):
        if self._LocalToon__presentingPie:
            import TTEmote
            Emote = Emote
            import otp.avatar
            Emote.globalEmote.releaseBody(self)
            messenger.send('end-pie')
            self._LocalToon__presentingPie = 0
        
        taskName = self.uniqueName('updatePiePower')
        taskMgr.remove(taskName)

    
    def _LocalToon__getPiePower(self, time):
        elapsed = max(time - self.tossPieStart, 0.0)
        t = elapsed / self.piePowerSpeed
        t = math.pow(t, self.piePowerExponent)
        power = int(t * 100) % 200
        if power > 100:
            power = 200 - power
        
        return power

    
    def _LocalToon__updatePiePower(self, task):
        if not (self._LocalToon__piePowerMeter):
            return Task.done
        
        self._LocalToon__piePowerMeter['value'] = self._LocalToon__getPiePower(globalClock.getFrameTime())
        return Task.cont

    
    def interruptPie(self):
        self.cleanupPieInHand()
        self._LocalToon__stopPresentPie()
        if self._LocalToon__piePowerMeter:
            self._LocalToon__piePowerMeter.hide()
        
        pie = self.pieTracks.get(self._LocalToon__pieSequence)
        if pie and pie.getT() < 14.0 / 24.0:
            del self.pieTracks[self._LocalToon__pieSequence]
            pie.pause()
        

    
    def _LocalToon__pieInHand(self):
        pie = self.pieTracks.get(self._LocalToon__pieSequence)
        if pie:
            pass
        return pie.getT() < 15.0 / 24.0

    
    def _LocalToon__toonMoved(self, isSet):
        if isSet:
            self.interruptPie()
        

    
    def localTossPie(self, power):
        if not (self._LocalToon__presentingPie):
            return None
        
        pos = self.getPos()
        hpr = self.getHpr()
        timestamp32 = globalClockDelta.getFrameNetworkTime(bits = 32)
        sequence = self._LocalToon__pieSequence
        if self.tossTrack:
            tossTrack = self.tossTrack
            self.tossTrack = None
            tossTrack.finish()
        
        if self.pieTracks.has_key(sequence):
            pieTrack = self.pieTracks[sequence]
            del self.pieTracks[sequence]
            pieTrack.finish()
        
        if self.splatTracks.has_key(sequence):
            splatTrack = self.splatTracks[sequence]
            del self.splatTracks[sequence]
            splatTrack.finish()
        
        self.makePiePowerMeter()
        self._LocalToon__piePowerMeter['value'] = power
        self._LocalToon__piePowerMeter.show()
        self._LocalToon__piePowerMeterSequence = sequence
        pieBubble = self.getPieBubble().instanceTo(NodePath())
        
        def pieFlies(self = self, pos = pos, hpr = hpr, sequence = sequence, power = power, timestamp32 = timestamp32, pieBubble = pieBubble):
            self.sendUpdate('tossPie', [
                pos[0],
                pos[1],
                pos[2],
                hpr[0],
                hpr[1],
                hpr[2],
                sequence,
                power,
                timestamp32])
            if self.numPies != ToontownGlobals.FullPies:
                self.setNumPies(self.numPies - 1)
            
            base.cTrav.addCollider(pieBubble, self.pieHandler)

        (toss, pie, flyPie) = self.getTossPieInterval(pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2], power, beginFlyIval = Func(pieFlies))
        pieBubble.reparentTo(flyPie)
        flyPie.setTag('pieSequence', str(sequence))
        toss = Sequence(toss)
        self.tossTrack = toss
        toss.start()
        pie = Sequence(pie, Func(base.cTrav.removeCollider, pieBubble), Func(self.pieFinishedFlying, sequence))
        self.pieTracks[sequence] = pie
        pie.start()

    
    def pieFinishedFlying(self, sequence):
        DistributedToon.DistributedToon.pieFinishedFlying(self, sequence)
        if self._LocalToon__piePowerMeterSequence == sequence:
            self._LocalToon__piePowerMeter.hide()
        

    
    def _LocalToon__finishPieTrack(self, sequence):
        if self.pieTracks.has_key(sequence):
            pieTrack = self.pieTracks[sequence]
            del self.pieTracks[sequence]
            pieTrack.finish()
        

    
    def _LocalToon__pieHit(self, entry):
        if not entry.hasSurfacePoint() or not entry.hasInto():
            return None
        
        if not entry.getInto().isTangible():
            return None
        
        sequence = int(entry.getFromNodePath().getNetTag('pieSequence'))
        self._LocalToon__finishPieTrack(sequence)
        if self.splatTracks.has_key(sequence):
            splatTrack = self.splatTracks[sequence]
            del self.splatTracks[sequence]
            splatTrack.finish()
        
        pieCode = 0
        pieCodeStr = entry.getIntoNodePath().getNetTag('pieCode')
        if pieCodeStr:
            pieCode = int(pieCodeStr)
        
        pos = entry.getSurfacePoint(render)
        timestamp32 = globalClockDelta.getFrameNetworkTime(bits = 32)
        self.sendUpdate('pieSplat', [
            pos[0],
            pos[1],
            pos[2],
            sequence,
            pieCode,
            timestamp32])
        splat = self.getPieSplatInterval(pos[0], pos[1], pos[2], pieCode)
        splat = Sequence(splat, Func(self.pieFinishedSplatting, sequence))
        self.splatTracks[sequence] = splat
        splat.start()
        messenger.send('pieSplat', [
            self,
            pieCode])
        messenger.send('localPieSplat', [
            pieCode,
            entry])

    
    def beginAllowPies(self):
        self.allowPies = 1
        self.updatePieButton()

    
    def endAllowPies(self):
        self.allowPies = 0
        self.updatePieButton()

    
    def makePiePowerMeter(self):
        DirectWaitBar = DirectWaitBar
        SUNKEN = SUNKEN
        import direct.gui.DirectGui
        if self._LocalToon__piePowerMeter == None:
            self._LocalToon__piePowerMeter = DirectWaitBar(frameSize = (-0.20000000000000001, 0.20000000000000001, -0.029999999999999999, 0.029999999999999999), relief = SUNKEN, borderWidth = (0.0050000000000000001, 0.0050000000000000001), barColor = (0.40000000000000002, 0.59999999999999998, 1.0, 1), pos = (0, 0.10000000000000001, 0.80000000000000004))
            self._LocalToon__piePowerMeter.hide()
        

    
    def updatePieButton(self):
        ToontownBattleGlobals = ToontownBattleGlobals
        import toontown.toonbase
        DirectButton = DirectButton
        NORMAL = NORMAL
        DISABLED = DISABLED
        B1PRESS = B1PRESS
        B1RELEASE = B1RELEASE
        import direct.gui.DirectGui
        wantButton = 0
        if self.allowPies and self.numPies > 0:
            wantButton = 1
        
        if launcher and not launcher.getPhaseComplete(5):
            wantButton = 0
        
        haveButton = self._LocalToon__pieButton != None
        if not haveButton and not wantButton:
            return None
        
        if haveButton and not wantButton:
            self._LocalToon__pieButton.destroy()
            self._LocalToon__pieButton = None
            self._LocalToon__pieButtonType = None
            self._LocalToon__pieButtonCount = None
            return None
        
        if self._LocalToon__pieButtonType != self.pieType:
            if self._LocalToon__pieButton:
                self._LocalToon__pieButton.destroy()
                self._LocalToon__pieButton = None
            
        
        if self._LocalToon__pieButton == None:
            inv = self.inventory
            self._LocalToon__pieButton = DirectButton(image = (inv.upButton, inv.downButton, inv.rolloverButton), geom = inv.invModels[ToontownBattleGlobals.THROW_TRACK][self.pieType], text = '50', text_scale = 0.040000000000000001, text_align = TextNode.ARight, geom_scale = 0.84999999999999998, geom_pos = (-0.01, 0, 0), text_fg = Vec4(1, 1, 1, 1), text_pos = (0.070000000000000007, -0.040000000000000001), relief = None, image_color = (0, 0.59999999999999998, 1, 1), pos = (0, 0.10000000000000001, 0.90000000000000002))
            self._LocalToon__pieButton.bind(B1PRESS, self._LocalToon__beginTossPieMouse)
            self._LocalToon__pieButton.bind(B1RELEASE, self._LocalToon__endTossPieMouse)
            self._LocalToon__pieButtonType = self.pieType
            self._LocalToon__pieButtonCount = None
        
        if self._LocalToon__pieButtonCount != self.numPies:
            if self.numPies == ToontownGlobals.FullPies:
                self._LocalToon__pieButton['text'] = ''
            else:
                self._LocalToon__pieButton['text'] = str(self.numPies)
            self._LocalToon__pieButtonCount = self.numPies
        

    
    def displayWhisper(self, fromId, chatString, whisperType):
        sender = None
        sfx = self.soundWhisper
        if fromId == TTLocalizer.Clarabelle:
            chatString = TTLocalizer.Clarabelle + ': ' + chatString
            sfx = self.soundPhoneRing
        elif fromId != 0:
            sender = base.cr.identifyAvatar(fromId)
        
        if whisperType == WhisperPopup.WTNormal or whisperType == WhisperPopup.WTQuickTalker:
            if sender == None:
                return None
            
            chatString = sender.getName() + ': ' + chatString
        
        whisper = WhisperPopup(chatString, OTPGlobals.getInterfaceFont(), whisperType)
        if sender != None:
            whisper.setClickable(sender.getName(), fromId)
        
        whisper.manage(base.marginManager)
        base.playSfx(sfx)

    
    def loadFurnitureGui(self):
        if self._LocalToon__furnitureGui:
            return None
        
        guiModels = loader.loadModel('phase_5.5/models/gui/house_design_gui')
        self._LocalToon__furnitureGui = DirectFrame(relief = None, pos = (-1.1899999999999999, 0.0, 0.33000000000000002), scale = 0.040000000000000001, image = guiModels.find('**/attic'))
        DirectLabel(parent = self._LocalToon__furnitureGui, relief = None, image = guiModels.find('**/rooftile'))
        bMoveStartUp = guiModels.find('**/bu_attic/bu_attic_up')
        bMoveStartDown = guiModels.find('**/bu_attic/bu_attic_down')
        bMoveStartRollover = guiModels.find('**/bu_attic/bu_attic_rollover')
        DirectButton(parent = self._LocalToon__furnitureGui, relief = None, image = [
            bMoveStartUp,
            bMoveStartDown,
            bMoveStartRollover,
            bMoveStartUp], text = [
            '',
            TTLocalizer.HDMoveFurnitureButton,
            TTLocalizer.HDMoveFurnitureButton], text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_font = ToontownGlobals.getInterfaceFont(), pos = (-0.29999999999999999, 0, 9.4000000000000004), command = self._LocalToon__startMoveFurniture)
        self._LocalToon__furnitureGui.hide()
        guiModels.removeNode()

    
    def showFurnitureGui(self):
        self.loadFurnitureGui()
        self._LocalToon__furnitureGui.show()

    
    def hideFurnitureGui(self):
        if self._LocalToon__furnitureGui:
            self._LocalToon__furnitureGui.hide()
        

    
    def loadClarabelleGui(self):
        if self._LocalToon__clarabelleButton:
            return None
        
        guiItems = loader.loadModelCopy('phase_5.5/models/gui/catalog_gui')
        circle = guiItems.find('**/cover/blue_circle')
        icon = guiItems.find('**/cover/clarabelle')
        icon.reparentTo(circle)
        rgba = VBase4(0.71589000000000003, 0.78454699999999999, 0.97399999999999998, 1.0)
        white = VBase4(1.0, 1.0, 1.0, 1.0)
        icon.setColor(white)
        self._LocalToon__clarabelleButton = DirectButton(relief = None, image = circle, text = '', text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_scale = 0.10000000000000001, text_pos = (-1.0600000000000001, 1.0600000000000001), text_font = ToontownGlobals.getInterfaceFont(), pos = (1.45, 1.0, 0.37), scale = 0.5, command = self._LocalToon__handleClarabelleButton)
        self._LocalToon__clarabelleButton.reparentTo(aspect2d, 1)
        button = self._LocalToon__clarabelleButton.stateNodePath[0]
        self._LocalToon__clarabelleFlash = Sequence(LerpColorInterval(button, 2, white, blendType = 'easeInOut'), LerpColorInterval(button, 2, rgba, blendType = 'easeInOut'))
        self._LocalToon__clarabelleFlash.loop()
        self._LocalToon__clarabelleFlash.pause()

    
    def showClarabelleGui(self, mailboxItems):
        self.loadClarabelleGui()
        if mailboxItems:
            self._LocalToon__clarabelleButton['text'] = [
                '',
                TTLocalizer.CatalogNewDeliveryButton,
                TTLocalizer.CatalogNewDeliveryButton]
        else:
            self._LocalToon__clarabelleButton['text'] = [
                '',
                TTLocalizer.CatalogNewCatalogButton,
                TTLocalizer.CatalogNewCatalogButton]
        self._LocalToon__clarabelleButton.show()
        self._LocalToon__clarabelleFlash.resume()

    
    def hideClarabelleGui(self):
        if self._LocalToon__clarabelleButton:
            self._LocalToon__clarabelleButton.hide()
            self._LocalToon__clarabelleFlash.pause()
        

    
    def _LocalToon__handleClarabelleButton(self):
        place = base.cr.playGame.getPlace()
        if place == None:
            self.notify.warning('Tried to go home, but place is None.')
            return None
        
        if self._LocalToon__catalogNotifyDialog:
            self._LocalToon__catalogNotifyDialog.cleanup()
            self._LocalToon__catalogNotifyDialog = None
        
        place.goHomeNow(self.lastHood)

    
    def _LocalToon__startMoveFurniture(self):
        if self.cr.furnitureManager != None:
            self.cr.furnitureManager.d_suggestDirector(self.doId)
        elif self.furnitureManager != None:
            self.furnitureManager.d_suggestDirector(self.doId)
        

    
    def stopMoveFurniture(self):
        if self.furnitureManager != None:
            self.furnitureManager.d_suggestDirector(0)
        

    
    def setFurnitureDirector(self, avId, furnitureManager):
        if avId == 0:
            if self.furnitureManager == furnitureManager:
                messenger.send('exitFurnitureMode', [
                    furnitureManager])
                self.furnitureManager = None
                self.furnitureDirector = None
            
        elif avId != self.doId:
            if self.furnitureManager == None or self.furnitureDirector != avId:
                self.furnitureManager = furnitureManager
                self.furnitureDirector = avId
                messenger.send('enterFurnitureMode', [
                    furnitureManager,
                    0])
            
        elif self.furnitureManager != None:
            messenger.send('exitFurnitureMode', [
                self.furnitureManager])
            self.furnitureManager = None
        
        self.furnitureManager = furnitureManager
        self.furnitureDirector = avId
        messenger.send('enterFurnitureMode', [
            furnitureManager,
            1])
        self.refreshOnscreenButtons()

    
    def getAvPosStr(self):
        pos = self.getPos()
        hpr = self.getHpr()
        serverVersion = base.cr.getServerVersion()
        districtName = base.cr.getShardName(base.localAvatar.defaultShard)
        if hasattr(base.cr.playGame.hood, 'loader') and hasattr(base.cr.playGame.hood.loader, 'place') and base.cr.playGame.getPlace() != None:
            zoneId = base.cr.playGame.getPlace().getZoneId()
        else:
            zoneId = '?'
        strPosCoordText = 'X: %.3f' % pos[0] + ', Y: %.3f' % pos[1] + '\nZ: %.3f' % pos[2] + ', H: %.3f' % hpr[0] + '\nZone: %s' % str(zoneId) + ', Ver: %s, ' % serverVersion + 'District: %s' % districtName
        return strPosCoordText
        self.refreshOnscreenButtons()

    
    def thinkPos(self):
        pos = self.getPos()
        hpr = self.getHpr()
        serverVersion = base.cr.getServerVersion()
        districtName = base.cr.getShardName(base.localAvatar.defaultShard)
        if hasattr(base.cr.playGame.hood, 'loader') and hasattr(base.cr.playGame.hood.loader, 'place') and base.cr.playGame.getPlace() != None:
            zoneId = base.cr.playGame.getPlace().getZoneId()
        else:
            zoneId = '?'
        strPos = 'X: %.3f' % pos[0] + '\nY: %.3f' % pos[1] + '\nZ: %.3f' % pos[2] + '\nH: %.3f' % hpr[0] + '\nZone: %s' % str(zoneId) + ',\nVer: %s, ' % serverVersion + '\nDistrict: %s' % districtName
        print 'Current position=', strPos.replace('\n', ', ')
        self.setChatAbsolute(strPos, CFThought | CFTimeout)

    
    def _LocalToon__placeMarker(self):
        pos = self.getPos()
        hpr = self.getHpr()
        chest = loader.loadModelOnce('phase_4/models/props/coffin')
        chest.reparentTo(render)
        chest.setColor(1, 0, 0, 1)
        chest.setPosHpr(pos, hpr)
        chest.setScale(0.5)

    
    def setFriendsListButtonActive(self, active):
        self.friendsListButtonActive = active
        self.refreshOnscreenButtons()

    
    def obscureFriendsListButton(self, increment):
        self.friendsListButtonObscured += increment
        self.refreshOnscreenButtons()

    
    def obscureMoveFurnitureButton(self, increment):
        self.moveFurnitureButtonObscured += increment
        self.refreshOnscreenButtons()

    
    def obscureClarabelleButton(self, increment):
        self.clarabelleButtonObscured += increment
        self.refreshOnscreenButtons()

    
    def refreshOnscreenButtons(self):
        self.bFriendsList.hide()
        self.hideFurnitureGui()
        self.hideClarabelleGui()
        clarabelleHidden = 1
        self.ignore(ToontownGlobals.FriendsListHotkey)
        if self.friendsListButtonActive and self.friendsListButtonObscured <= 0:
            self.bFriendsList.show()
            self.accept(ToontownGlobals.FriendsListHotkey, self.sendFriendsListEvent)
            if self.clarabelleButtonObscured <= 0 and self.isTeleportAllowed():
                if self.catalogNotify == ToontownGlobals.NewItems or self.mailboxNotify == ToontownGlobals.NewItems:
                    if not not launcher:
                        pass
                    showClarabelle = launcher.getPhaseComplete(5.5)
                    for quest in self.quests:
                        if quest[0] in Quests.PreClarabelleQuestIds:
                            showClarabelle = 0
                        
                    
                    if showClarabelle:
                        self.showClarabelleGui(self.mailboxNotify == ToontownGlobals.NewItems)
                        clarabelleHidden = 0
                    
                
            
        
        if clarabelleHidden:
            if self._LocalToon__catalogNotifyDialog:
                self._LocalToon__catalogNotifyDialog.cleanup()
                self._LocalToon__catalogNotifyDialog = None
            
        else:
            self.newCatalogNotify()
        if self.moveFurnitureButtonObscured <= 0:
            if self.furnitureManager != None and self.furnitureDirector == self.doId:
                self.loadFurnitureGui()
                self._LocalToon__furnitureGui.setPos(-1.1599999999999999, 0, -0.029999999999999999)
                self._LocalToon__furnitureGui.setScale(0.059999999999999998)
            elif self.cr.furnitureManager != None:
                self.showFurnitureGui()
                taskMgr.remove('lerpFurnitureButton')
                self._LocalToon__furnitureGui.lerpPosHprScale(pos = Point3(-1.1899999999999999, 0.0, 0.33000000000000002), hpr = Vec3(0.0, 0.0, 0.0), scale = Vec3(0.040000000000000001, 0.040000000000000001, 0.040000000000000001), time = 1.0, blendType = 'easeInOut', task = 'lerpFurnitureButton')
            
        

    
    def setGhostMode(self, flag):
        if flag == 2:
            self.seeGhosts = 1
        
        DistributedToon.DistributedToon.setGhostMode(self, flag)

    
    def newCatalogNotify(self):
        if not (self.gotCatalogNotify):
            return None
        
        if not not launcher:
            pass
        hasPhase = launcher.getPhaseComplete(5.5)
        if not hasPhase:
            return None
        
        if not (self.friendsListButtonActive) or self.friendsListButtonObscured > 0:
            return None
        
        self.gotCatalogNotify = 0
        currentWeek = self.catalogScheduleCurrentWeek - 1
        if currentWeek < 57:
            seriesNumber = currentWeek / ToontownGlobals.CatalogNumWeeksPerSeries + 1
            weekNumber = currentWeek % ToontownGlobals.CatalogNumWeeksPerSeries + 1
        elif currentWeek < 65:
            seriesNumber = 6
            weekNumber = currentWeek - 56
        else:
            seriesNumber = currentWeek / ToontownGlobals.CatalogNumWeeksPerSeries + 2
            weekNumber = currentWeek % ToontownGlobals.CatalogNumWeeksPerSeries + 1
        message = None
        if self.mailboxNotify == ToontownGlobals.NoItems:
            if self.catalogNotify == ToontownGlobals.NewItems:
                if self.catalogScheduleCurrentWeek == 1:
                    message = (TTLocalizer.CatalogNotifyFirstCatalog, TTLocalizer.CatalogNotifyInstructions)
                else:
                    message = (TTLocalizer.CatalogNotifyNewCatalog % weekNumber,)
            
        elif self.mailboxNotify == ToontownGlobals.NewItems:
            if self.catalogNotify == ToontownGlobals.NewItems:
                message = (TTLocalizer.CatalogNotifyNewCatalogNewDelivery % weekNumber,)
            else:
                message = (TTLocalizer.CatalogNotifyNewDelivery,)
        elif self.mailboxNotify == ToontownGlobals.OldItems:
            if self.catalogNotify == ToontownGlobals.NewItems:
                message = (TTLocalizer.CatalogNotifyNewCatalogOldDelivery % weekNumber,)
            else:
                message = (TTLocalizer.CatalogNotifyOldDelivery,)
        
        if message == None:
            return None
        
        if self._LocalToon__catalogNotifyDialog:
            self._LocalToon__catalogNotifyDialog.cleanup()
        
        self._LocalToon__catalogNotifyDialog = CatalogNotifyDialog.CatalogNotifyDialog(message)
        base.playSfx(self.soundPhoneRing)

    
    def allowHardLand(self):
        retval = LocalAvatar.LocalAvatar.allowHardLand(self)
        if retval:
            pass
        return not (self.isDisguised)


