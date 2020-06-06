# File: T (Python 2.2)

from otp.otpbase import OTPBase
from direct.showbase.DirectObject import *
from direct.showbase.PythonUtil import *
import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from toontown.launcher import DownloadWatcher
import ToontownLoader
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *

class ToonBase(OTPBase.OTPBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonBase')
    
    def __init__(self):
        OTPBase.OTPBase.__init__(self)
        if not self.isMainWindowOpen():
            
            try:
                launcher.setPandaErrorCode(7)
            except:
                pass

            sys.exit(1)
        
        self.disableShowbaseMouse()
        camera.setPosHpr(0, 0, 0, 0, 0, 0)
        self.camLens.setFov(ToontownGlobals.DefaultCameraFov)
        self.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        self.musicManager.setVolume(0.65000000000000002)
        self.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
        tpm = TextPropertiesManager.getGlobalPtr()
        candidateActive = TextProperties()
        candidateActive.setTextColor(0, 0, 1, 1)
        tpm.setProperties('candidate_active', candidateActive)
        candidateInactive = TextProperties()
        candidateInactive.setTextColor(0.29999999999999999, 0.29999999999999999, 0.69999999999999996, 1)
        tpm.setProperties('candidate_inactive', candidateInactive)
        self.transitions.IrisModelName = 'phase_3/models/misc/iris'
        self.transitions.FadeModelName = 'phase_3/models/misc/fade'
        self.exitFunc = self.userExit
        if __builtins__.has_key('launcher') and launcher:
            launcher.setPandaErrorCode(11)
        
        globalClock.setMaxDt(0.20000000000000001)
        if self.config.GetBool('want-particles', 1) == 1:
            self.notify.debug('Enabling particles')
            self.enableParticles()
        
        self.accept(ToontownGlobals.ScreenshotHotkey, self.takeScreenShot)
        self.accept('panda3d-render-error', self.panda3dRenderError)
        self.loader = ToontownLoader.ToontownLoader(self)
        __builtins__['loader'] = self.loader
        self.accept('PandaPaused', self.disableAllAudio)
        self.accept('PandaRestarted', self.enableAllAudio)
        self.wantPets = self.config.GetBool('want-pets', 1)
        self.wantBingo = self.config.GetBool('want-fish-bingo', 1)
        self.wantNewSpecies = self.config.GetBool('want-new-species', 0)
        self.randomMinigameAbort = self.config.GetBool('random-minigame-abort', 0)
        self.randomMinigameDisconnect = self.config.GetBool('random-minigame-disconnect', 0)
        self.randomMinigameNetworkPlugPull = self.config.GetBool('random-minigame-netplugpull', 0)
        self.autoPlayAgain = self.config.GetBool('auto-play-again', 0)
        self.skipMinigameReward = self.config.GetBool('skip-minigame-reward', 0)
        self.wantMinigameDifficulty = self.config.GetBool('want-minigame-difficulty', 0)
        self.minigameDifficulty = self.config.GetFloat('minigame-difficulty', -1.0)
        if self.minigameDifficulty == -1.0:
            del self.minigameDifficulty
        
        self.minigameSafezoneId = self.config.GetInt('minigame-safezone-id', -1)
        if self.minigameSafezoneId == -1:
            del self.minigameSafezoneId
        
        self.creditCardUpFront = self.config.GetInt('credit-card-up-front', -1)
        if self.creditCardUpFront == -1:
            del self.creditCardUpFront
        else:
            self.creditCardUpFront = self.creditCardUpFront != 0
        self.housingEnabled = self.config.GetBool('want-housing', 1)
        self.cannonsEnabled = self.config.GetBool('estate-cannons', 0)
        self.fireworksEnabled = self.config.GetBool('estate-fireworks', 0)
        self.dayNightEnabled = self.config.GetBool('estate-day-night', 0)
        self.cloudPlatformsEnabled = self.config.GetBool('estate-clouds', 0)
        self.goonsEnabled = self.config.GetBool('estate-goon', 0)
        self.restrictTrialers = self.config.GetBool('restrict-trialers', 1)

    
    def disableShowbaseMouse(self):
        self.useDrive()
        self.disableMouse()
        if self.mouseInterface:
            self.mouseInterface.reparentTo(self.dataUnused)
        
        if base.mouse2cam:
            self.mouse2cam.reparentTo(self.dataUnused)
        

    
    def takeScreenShot(self):
        if not hasattr(self, 'localAvatar') or not self.config.GetBool('screenshot-coords', 1):
            base.screenshot()
            return None
        
        self.localAvatar.stopThisFrame = 1
        ctext = self.localAvatar.getAvPosStr()
        coordTextLabel = DirectLabel(pos = (-0.81000000000000005, 0.001, -0.87), text = ctext, text_scale = 0.050000000000000003, text_fg = VBase4(1.0, 1.0, 1.0, 1.0), text_bg = (0, 0, 0, 0), text_shadow = (0, 0, 0, 1), relief = None)
        coordTextLabel.setBin('gui-popup', 0)
        self.screenshotStr = ''
        messenger.send('takingScreenshot')
        strTextLabel = None
        if len(self.screenshotStr):
            strTextLabel = DirectLabel(pos = (0.0, 0.001, 0.90000000000000002), text = self.screenshotStr, text_scale = 0.050000000000000003, text_fg = VBase4(1.0, 1.0, 1.0, 1.0), text_bg = (0, 0, 0, 0), text_shadow = (0, 0, 0, 1), relief = None)
            strTextLabel.setBin('gui-popup', 0)
        
        self.graphicsEngine.renderFrame()
        self.screenshot()
        if strTextLabel is not None:
            strTextLabel.destroy()
        
        coordTextLabel.destroy()

    
    def addScreenshotString(self, str):
        if len(self.screenshotStr):
            self.screenshotStr += '\n'
        
        self.screenshotStr += str

    
    def initNametagGlobals(self):
        arrow = loader.loadModel('phase_3/models/props/arrow')
        card = loader.loadModel('phase_3/models/props/panel')
        speech3d = ChatBalloon(loader.loadModelNode('phase_3/models/props/chatbox'))
        thought3d = ChatBalloon(loader.loadModelNode('phase_3/models/props/chatbox_thought_cutout'))
        speech2d = ChatBalloon(loader.loadModelNode('phase_3/models/props/chatbox_noarrow'))
        chatButtonGui = loader.loadModelOnce('phase_3/models/gui/chat_button_gui')
        NametagGlobals.setCamera(self.cam)
        NametagGlobals.setArrowModel(arrow)
        NametagGlobals.setNametagCard(card, VBase4(-0.5, 0.5, -0.5, 0.5))
        if self.mouseWatcherNode:
            NametagGlobals.setMouseWatcher(self.mouseWatcherNode)
        
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
        rolloverSound = DirectGuiGlobals.getDefaultRolloverSound()
        if rolloverSound:
            NametagGlobals.setRolloverSound(rolloverSound)
        
        clickSound = DirectGuiGlobals.getDefaultClickSound()
        if clickSound:
            NametagGlobals.setClickSound(clickSound)
        
        NametagGlobals.setToon(self.cam)
        self.marginManager = MarginManager()
        self.margins = self.aspect2d.attachNewNode(self.marginManager, DirectGuiGlobals.MIDGROUND_SORT_INDEX + 1)
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

    
    def startShow(self, cr, launcherServer = None):
        self.cr = cr
        base.graphicsEngine.renderFrame()
        if launcher:
            self.downloadWatcher = DownloadWatcher.DownloadWatcher()
            self.acceptOnce('launcherAllPhasesComplete', self.cleanupDownloadWatcher)
        
        gameServer = base.config.GetString('game-server', '')
        if gameServer:
            self.notify.info('Using game-server from Configrc: %s ' % gameServer)
        elif launcherServer:
            gameServer = launcherServer
            self.notify.info('Using gameServer from launcher: %s ' % gameServer)
        else:
            gameServer = 'localhost'
        serverPort = base.config.GetInt('server-port', 6667)
        serverList = []
        for name in string.split(gameServer, ';'):
            url = URLSpec(name, 1)
            url.setScheme('s')
            if not url.hasPort():
                url.setPort(serverPort)
            
            serverList.append(url)
        
        if len(serverList) == 1:
            failover = base.config.GetString('server-failover', '')
            serverURL = serverList[0]
            for arg in failover.split():
                
                try:
                    port = int(arg)
                    url = URLSpec(serverURL)
                    url.setPort(port)
                except:
                    url = URLSpec(arg, 1)

                if url != serverURL:
                    serverList.append(url)
                
            
        
        cr.loginFSM.request('connect', [
            serverList])

    
    def exitShow(self):
        self.notify.info('Exiting Toontown')
        if launcher:
            launcher.setPandaErrorCode(0)
        
        sys.exit()

    
    def userExit(self):
        
        try:
            self.localAvatar.d_setAnimState('TeleportOut', 1)
        except:
            pass

        if self.cr.timeManager:
            self.cr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectCloseWindow)
        
        self.cr.loginFSM.request('shutdown')
        self.notify.warning('Could not request shutdown; exiting anyway.')
        self.exitShow()

    
    def panda3dRenderError(self):
        if launcher:
            launcher.setPandaErrorCode(14)
        
        if self.cr.timeManager:
            self.cr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectGraphicsError)
        
        self.cr.sendDisconnect()
        sys.exit()


