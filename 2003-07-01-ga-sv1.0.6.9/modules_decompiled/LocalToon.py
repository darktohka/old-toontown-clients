# File: L (Python 2.2)

from PandaObject import *
from IntervalGlobal import *
import DistributedToon
import LocalAvatar
import Toon
import ShtikerBook
import InventoryPage
import MapPage
import OptionsPage
import ShardPage
import QuestPage
import TrackPage
import SuitPage
import PhotoAlbumPage
import BuildingPage
import FishPage
import LaffMeter
import whrandom
import QuestParser
import ToontownGlobals
import PythonUtil

class LocalToon(DistributedToon.DistributedToon, LocalAvatar.LocalAvatar):
    neverDisable = 1
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.LocalToon_initialized = 1
            DistributedToon.DistributedToon.__init__(self, cr)
            LocalAvatar.LocalAvatar.__init__(self, cr)
            self.nametag2dContents = Nametag.CSpeech
            self.nametag.getNametag2d().setContents(self.nametag2dContents & self.nametag2dDist)
            self.setPickable(0)
            Toon.loadDialog()
            self.isIt = 0
            self.inTutorial = 0
            self.tunnelX = 0.0
            self.estate = None

        return None

    
    def generate(self):
        self.book = ShtikerBook.ShtikerBook('bookDone')
        self.book.load()
        self.book.hideButton()
        self.optionsPage = OptionsPage.OptionsPage()
        self.optionsPage.load()
        self.book.addPage(self.optionsPage)
        self.shardPage = ShardPage.ShardPage()
        self.shardPage.load()
        self.book.addPage(self.shardPage)
        self.mapPage = MapPage.MapPage()
        self.mapPage.load()
        self.book.addPage(self.mapPage)
        self.invPage = InventoryPage.InventoryPage()
        self.invPage.load()
        self.book.addPage(self.invPage)
        self.questPage = QuestPage.QuestPage()
        self.questPage.load()
        self.book.addPage(self.questPage)
        self.trackPage = TrackPage.TrackPage()
        self.trackPage.load()
        self.book.addPage(self.trackPage)
        self.suitPage = SuitPage.SuitPage()
        self.suitPage.load()
        self.book.addPage(self.suitPage)
        self.book.setPage(self.mapPage)
        self.laffMeter = LaffMeter.LaffMeter(self.style, self.hp, self.maxHp)
        self.laffMeter.setAvatar(self)
        self.laffMeter.setScale(0.074999999999999997)
        self.laffMeter.setPos(-1.2, 0.0, -0.87)
        self.laffMeter.stop()
        self.startLookAround()
        self.nametag.manage(toonbase.marginManager)
        QuestParser.init()
        DistributedToon.DistributedToon.generate(self)
        return None

    
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
        del self.book
        self.nametag.unmanage(toonbase.marginManager)
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

        return None

    
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
        tracks = []
        toonTrack = self.getTunnelInToonTrack(endX, tunnelOrigin)
        tracks.append(toonTrack)
        
        def cleanup(self = self, tunnelOrigin = tunnelOrigin):
            self.stopSound()
            tunnelOrigin.removeNode()
            messenger.send('tunnelInMovieDone')

        self.tunnelTrack = Sequence(Parallel(tracks), Func(cleanup))
        self.tunnelTrack.start(globalClock.getFrameTime() - startTime)

    
    def handleTunnelOut(self, startTime, startX, startY, x, y, z, h):
        self.notify.debug('LocalToon.handleTunnelOut')
        tunnelOrigin = render.attachNewNode('tunnelOrigin')
        tunnelOrigin.setPosHpr(x, y, z, h, 0, 0)
        self.b_setAnimState('run', self.animMultiplier)
        self.runSound()
        self.stopLookAround()
        tracks = []
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
            self.reparentTo(hidden)
            tunnelOrigin.removeNode()
            messenger.send('tunnelOutMovieDone')

        self.tunnelTrack = Sequence(Parallel(tracks), Func(cleanup))
        self.tunnelTrack.start(globalClock.getFrameTime() - startTime)


