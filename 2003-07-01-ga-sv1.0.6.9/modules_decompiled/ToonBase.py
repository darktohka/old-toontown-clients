# File: T (Python 2.2)

from ShowBaseGlobal import *
from DirectObject import *
from PythonUtil import *
import ToontownGlobals
import DirectNotifyGlobal
import DownloadWatcher
import ToontownLoader
import DirectGuiGlobals
from DirectGui import *

class ToonBase(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonBase')
    
    def __init__(self):
        base.useDrive()
        base.disableMouse()
        camera.setPosHpr(0, 0, 0, 0, 0, 0)
        base.camLens.setFov(ToontownGlobals.DefaultCameraFov)
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        base.musicManager.setVolume(0.65000000000000002)
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
        base.transitions.IrisModelName = 'phase_3/models/misc/iris'
        base.transitions.FadeModelName = 'phase_3/models/misc/fade'
        base.exitFunc = self.userExit
        if launcher:
            launcher.setPandaErrorCode(11)
        
        globalClock.setMaxDt(1.0)
        if base.config.GetBool('want-particles', 1) == 1:
            self.notify.debug('Enabling particles')
            base.enableParticles()
        
        self.base = base
        self.accept(ToontownGlobals.ScreenshotHotkey, self.takeScreenShot)
        self.loader = ToontownLoader.ToontownLoader(base)
        self.accept('PandaPaused', base.disableAllAudio)
        self.accept('PandaRestarted', base.enableAllAudio)
        self.randomMinigameAbort = base.config.GetBool('random-minigame-abort', 0)
        self.randomMinigameDisconnect = base.config.GetBool('random-minigame-disconnect', 0)
        self.randomMinigameNetworkPlugPull = base.config.GetBool('random-minigame-netplugpull', 0)
        self.autoPlayAgain = base.config.GetBool('auto-play-again', 0)
        self.skipMinigameReward = base.config.GetBool('skip-minigame-reward', 0)
        self.wantMinigameDifficulty = base.config.GetBool('want-minigame-difficulty', 0)
        self.minigameDifficulty = base.config.GetFloat('minigame-difficulty', -1.0)
        if self.minigameDifficulty == -1.0:
            del self.minigameDifficulty
        
        self.minigameSafezoneId = base.config.GetInt('minigame-safezone-id', -1)
        if self.minigameSafezoneId == -1:
            del self.minigameSafezoneId
        
        self.creditCardUpFront = base.config.GetInt('credit-card-up-front', -1)
        if self.creditCardUpFront == -1:
            del self.creditCardUpFront
        else:
            self.creditCardUpFront = self.creditCardUpFront != 0
        self.emotionsEnabled = base.config.GetBool('want-emotions', 0)
        self.emotionsMenuEnabled = base.config.GetBool('want-emotions-menu', 0)
        self.customMenuEnabled = base.config.GetBool('want-custom-menu', 0)
        self.housingEnabled = base.config.GetBool('want-housing', 1)

    
    def takeScreenShot(self):
        if not hasattr(toonbase, 'localToon') or not base.config.GetBool('screenshot-coords', 1):
            base.screenshot()
            return None
        
        base.drive.node().setStopThisFrame(1)
        ctext = toonbase.localToon.getAvPosStr()
        coordTextLabel = DirectLabel(pos = (-0.81000000000000005, 0.001, -0.87), text = ctext, text_scale = 0.050000000000000003, text_fg = VBase4(1.0, 1.0, 1.0, 1.0), text_bg = (0, 0, 0, 0), text_shadow = (0, 0, 0, 1), relief = None)
        coordTextLabel.setBin('gui-popup', 0)
        base.graphicsEngine.renderFrame()
        base.screenshot()
        coordTextLabel.destroy()
        del coordTextLabel

    
    def initNametagGlobals(self):
        arrow = loader.loadModel('phase_3/models/props/arrow')
        card = loader.loadModel('phase_3/models/props/panel')
        speech3d = ChatBalloon(loader.loadModelNode('phase_3/models/props/chatbox'))
        thought3d = ChatBalloon(loader.loadModelNode('phase_3/models/props/chatbox_thought_cutout'))
        speech2d = ChatBalloon(loader.loadModelNode('phase_3/models/props/chatbox_noarrow'))
        chatButtonGui = loader.loadModelOnce('phase_3/models/gui/chat_button_gui')
        NametagGlobals.setCamera(base.cam)
        NametagGlobals.setArrowModel(arrow)
        NametagGlobals.setNametagCard(card, VBase4(-0.5, 0.5, -0.5, 0.5))
        NametagGlobals.setMouseWatcher(base.mouseWatcherNode)
        NametagGlobals.setSpeechBalloon3d(speech3d)
        NametagGlobals.setThoughtBalloon3d(thought3d)
        NametagGlobals.setSpeechBalloon2d(speech2d)
        NametagGlobals.setThoughtBalloon2d(thought3d)
        NametagGlobals.setPageButton(PGButton.SReady, chatButtonGui.find('**/Horiz_Arrow_UP'))
        NametagGlobals.setPageButton(PGButton.SDepressed, chatButtonGui.find('**/Horiz_Arrow_DN'))
        NametagGlobals.setPageButton(PGButton.SRollover, chatButtonGui.find('**/Horiz_Arrow_Rllvr'))
        NametagGlobals.setQuitButton(PGButton.SReady, chatButtonGui.find('**/CloseBtn_UP'))
        NametagGlobals.setQuitButton(PGButton.SDepressed, chatButtonGui.find('**/CloseBtn_DN'))
        NametagGlobals.setQuitButton(PGButton.SRollover, chatButtonGui.find('**/CloseBtn_Rllvr'))
        arrow.removeNode()
        card.removeNode()
        chatButtonGui.removeNode()
        rolloverSound = DirectGuiGlobals.getDefaultRolloverSound()
        if rolloverSound:
            NametagGlobals.setRolloverSound(rolloverSound)
        
        clickSound = DirectGuiGlobals.getDefaultClickSound()
        if clickSound:
            NametagGlobals.setClickSound(clickSound)
        
        NametagGlobals.setToon(base.cam)
        self.marginManager = MarginManager()
        self.margins = base.aspect2d.attachNewNode(self.marginManager, DirectGuiGlobals.MIDGROUND_SORT_INDEX + 1)
        mm = self.marginManager
        self.leftCells = [
            mm.addGridCell(0, 1, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop),
            mm.addGridCell(0, 2, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop),
            mm.addGridCell(0, 3, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)]
        self.bottomCells = [
            mm.addGridCell(0.5, 0, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop),
            mm.addGridCell(1.5, 0, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop),
            mm.addGridCell(2.5, 0, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop),
            mm.addGridCell(3.5, 0, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop),
            mm.addGridCell(4.5, 0, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)]
        self.rightCells = [
            mm.addGridCell(5, 2, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop),
            mm.addGridCell(5, 1, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)]

    
    def setCellsAvailable(self, cell_list, available):
        for cell in cell_list:
            self.marginManager.setCellAvailable(cell, available)
        

    
    def cleanupDownloadWatcher(self):
        self.downloadWatcher.cleanup()
        self.downloadWatcher = None

    
    def startShow(self, tcr, launcherServerURL = None):
        self.tcr = tcr
        base.graphicsEngine.renderFrame()
        if launcher:
            self.downloadWatcher = DownloadWatcher.DownloadWatcher()
            self.acceptOnce('launcherAllPhasesComplete', self.cleanupDownloadWatcher)
        
        serverURL = URLSpec(base.config.GetString('server-ip', ''), 1)
        if not serverURL.empty():
            self.notify.info('Using server-ip to set serverURL to: %s ' % serverURL.cStr())
        elif launcherServerURL:
            serverURL = launcherServerURL
            self.notify.info('Using launcher to set serverURL to: %s ' % serverURL.cStr())
        else:
            serverType = base.config.GetString('server-type', '')
            if serverType:
                if serverType == 'prod':
                    serverURL = URLSpec(ToontownGlobals.prodServerIP, 1)
                elif serverType == 'dev':
                    serverURL = URLSpec(ToontownGlobals.devServerIP, 1)
                elif serverType == 'debug':
                    serverURL = URLSpec(ToontownGlobals.debugServerIP, 1)
                else:
                    self.notify.error('Unknown server type: ' + serverType)
                self.notify.info('Using server-type to set serverURL to: %s' % serverURL.cStr())
            else:
                serverURL = URLSpec(ToontownGlobals.prodServerIP, 1)
                self.notify.info('Defaulting serverURL to: %s ' % serverURL.cStr())
        if not serverURL.hasPort():
            serverURL.setPort(base.config.GetInt('server-port', 6667))
        
        serverList = [
            serverURL]
        failover = base.config.GetString('server-failover', '')
        for arg in failover.split():
            
            try:
                port = int(arg)
                url = URLSpec(serverURL)
                url.setPort(port)
            except:
                url = URLSpec(arg, 1)

            if url != serverURL:
                serverList.append(url)
            
        
        tcr.loginFSM.request('connect', [
            serverList])

    
    def exitShow(self):
        self.notify.info('Exiting Toontown')
        if launcher:
            launcher.setPandaErrorCode(0)
        
        sys.exit()

    
    def userExit(self):
        
        try:
            self.localToon.d_setAnimState('TeleportOut', 1)
        except:
            pass

        if self.tcr.timeManager:
            self.tcr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectCloseWindow)
        
        self.tcr.loginFSM.request('shutdown')
        self.notify.warning('Could not request shutdown; exiting anyway.')
        self.exitShow()


