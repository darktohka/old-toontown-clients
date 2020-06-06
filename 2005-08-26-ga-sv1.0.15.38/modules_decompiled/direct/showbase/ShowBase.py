# File: S (Python 2.2)

from pandac.PandaModules import *
__builtins__['config'] = ConfigConfigureGetConfigConfigShowbase
from direct.directnotify.DirectNotifyGlobal import *
from MessengerGlobal import *
from BulletinBoardGlobal import *
from direct.task.TaskManagerGlobal import *
from EventManagerGlobal import *
from PythonUtil import *
from direct.particles.ParticleManagerGlobal import *
from PhysicsManagerGlobal import *
from direct.interval.IntervalManager import ivalMgr
from InputStateGlobal import inputState
from direct.task import Task
import EventManager
import math
import sys
import Loader
import time
from direct.fsm import ClassicFSM
from direct.fsm import State
import DirectObject
import SfxPlayer
import OnScreenDebug
__builtins__['FADE_SORT_INDEX'] = 1000
__builtins__['NO_FADE_SORT_INDEX'] = 2000

class ShowBase(DirectObject.DirectObject):
    notify = directNotify.newCategory('ShowBase')
    
    def __init__(self):
        self.config = config
        Verify.wantVerifyPdb = self.config.GetBool('want-verify-pdb', 0)
        self.printEnvDebugInfo()
        if self.config.GetBool('use-vfs', 1):
            vfs = VirtualFileSystem.getGlobalPtr()
        else:
            vfs = None
        self.nextWindowIndex = 1
        self.sfxActive = self.config.GetBool('audio-sfx-active', 1)
        self.musicActive = self.config.GetBool('audio-music-active', 1)
        self.wantFog = self.config.GetBool('want-fog', 1)
        self.screenshotExtension = self.config.GetString('screenshot-extension', 'jpg')
        self.musicManager = None
        self.musicManagerIsValid = None
        self.sfxManagerList = []
        self.sfxManagerIsValidList = []
        self.wantStats = self.config.GetBool('want-pstats', 0)
        self.clientSleep = self.config.GetFloat('client-sleep', 0.0)
        self.mwClientSleep = 0.0
        self.sleepCycle = 0.0
        self.exitFunc = None
        Task.TaskManager.taskTimerVerbose = self.config.GetBool('task-timer-verbose', 0)
        Task.TaskManager.extendedExceptions = self.config.GetBool('extended-exceptions', 0)
        Task.TaskManager.pStatsTasks = self.config.GetBool('pstats-tasks', 0)
        taskMgr.resumeFunc = PStatClient.resumeAfterPause
        fsmRedefine = self.config.GetBool('fsm-redefine', 0)
        State.FsmRedefine = fsmRedefine
        self.aspectRatio = ConfigVariableDouble('aspect-ratio', 0)
        self.windowType = self.config.GetString('window-type', 'onscreen')
        self.requireWindow = self.config.GetBool('require-window', 1)
        self.win = None
        self.frameRateMeter = None
        self.winList = []
        self.mainWinMinimized = 0
        self.pipe = None
        self.pipeList = []
        self.mouse2cam = None
        self.buttonThrowers = None
        self.mouseWatcher = None
        self.mouseWatcherNode = None
        self.pointerWatcherNodes = None
        self.mouseInterface = None
        self.drive = None
        self.trackball = None
        self.cam = None
        self.camList = []
        self.camNode = None
        self.camLens = None
        self.camera = None
        self.camera2d = None
        self.camera2dp = None
        self.camFrustumVis = None
        
        try:
            self.clusterSyncFlag = clusterSyncFlag
        except NameError:
            self.clusterSyncFlag = self.config.GetBool('cluster-sync', 0)

        self.hidden = NodePath('hidden')
        self.graphicsEngine = GraphicsEngine()
        self.setupRender()
        self.setupRender2d()
        self.setupRender2dp()
        self.setupDataGraph()
        self.shadowTrav = 0
        self.cTrav = 0
        self.appTrav = 0
        self.dgTrav = DataGraphTraverser()
        self.recorder = None
        playbackSession = self.config.GetString('playback-session', '')
        recordSession = self.config.GetString('record-session', '')
        if playbackSession:
            self.recorder = RecorderController()
            self.recorder.beginPlayback(Filename.fromOsSpecific(playbackSession))
        elif recordSession:
            self.recorder = RecorderController()
            self.recorder.beginRecord(Filename.fromOsSpecific(recordSession))
        
        if self.recorder:
            import random
            import whrandom
            seed = self.recorder.getRandomSeed()
            random.seed(seed)
            whrandom.seed(seed & 255, seed >> 8 & 255, seed >> 16 & 255)
        
        self.oldexitfunc = getattr(sys, 'exitfunc', None)
        sys.exitfunc = self.exitfunc
        if self.windowType != 'none':
            self.openDefaultWindow()
        
        self.loader = Loader.Loader(self)
        self.eventMgr = eventMgr
        self.messenger = messenger
        self.bboard = bulletinBoard
        self.taskMgr = taskMgr
        self.particleMgr = particleMgr
        self.particleMgr.setFrameStepping(1)
        self.particleMgrEnabled = 0
        self.physicsMgr = physicsMgr
        integrator = LinearEulerIntegrator()
        self.physicsMgr.attachLinearIntegrator(integrator)
        self.physicsMgrEnabled = 0
        self.physicsMgrAngular = 0
        self.createBaseAudioManagers()
        self.createStats()
        self.AppHasAudioFocus = 1
        __builtins__['base'] = self
        __builtins__['render2d'] = self.render2d
        __builtins__['render2dp'] = self.render2dp
        __builtins__['aspect2d'] = self.aspect2d
        __builtins__['aspect2dp'] = self.aspect2dp
        __builtins__['render'] = self.render
        __builtins__['hidden'] = self.hidden
        __builtins__['camera'] = self.camera
        __builtins__['loader'] = self.loader
        __builtins__['taskMgr'] = self.taskMgr
        __builtins__['eventMgr'] = self.eventMgr
        __builtins__['messenger'] = self.messenger
        __builtins__['bboard'] = self.bboard
        __builtins__['run'] = self.run
        __builtins__['ostream'] = Notify.out()
        __builtins__['directNotify'] = directNotify
        __builtins__['globalClock'] = ClockObject.getGlobalClock()
        __builtins__['vfs'] = vfs
        __builtins__['cpMgr'] = ConfigPageManager.getGlobalPtr()
        __builtins__['cvMgr'] = ConfigVariableManager.getGlobalPtr()
        __builtins__['__dev__'] = base.config.GetBool('want-dev', 0)
        __builtins__['wantOtpServer'] = base.config.GetBool('want-otp-server', 0)
        __builtins__['onScreenDebug'] = OnScreenDebug.OnScreenDebug()
        ShowBase.notify.info('__dev__ == %s' % __dev__)
        self.accept('window-event', self._ShowBase__windowEvent)
        import Transitions
        self.transitions = Transitions.Transitions(self.loader)
        fTk = self.config.GetBool('want-tk', 0)
        if not self.config.GetBool('want-directtools', 0):
            pass
        fDirect = base.config.GetString('cluster-mode', '') != ''
        self.startDirect(fWantDirect = fDirect, fWantTk = fTk)
        self.restart()

    
    def printEnvDebugInfo(self):
        if self.config.GetBool('want-env-debug-info', 0):
            print '\n\nEnvironment Debug Info {'
            print '* model path:', getModelPath()
            print '* texture path:', getTexturePath()
            print '* sound path:', getSoundPath()
            print '}'
        

    
    def exitfunc(self):
        self.graphicsEngine.removeAllWindows()
        del self.win
        del self.winList
        del self.pipe
        del self.musicManager
        del self.sfxManagerList
        
        try:
            direct.panel.destroy()
        except StandardError:
            pass

        if self.oldexitfunc:
            self.oldexitfunc()
        

    
    def makeDefaultPipe(self):
        selection = GraphicsPipeSelection.getGlobalPtr()
        selection.printPipeTypes()
        self.pipe = selection.makeDefaultPipe()
        if not (self.pipe):
            self.notify.error('No graphics pipe is available!\nYour Config.prc file must name at least one valid panda display\nlibrary via load-display or aux-display.')
        
        self.notify.info('Default graphics pipe is %s (%s).' % (self.pipe.getInterfaceName(), self.pipe.getType().getName()))
        self.pipeList.append(self.pipe)

    
    def makeAllPipes(self):
        shouldPrintPipes = 0
        selection = GraphicsPipeSelection.getGlobalPtr()
        selection.loadAuxModules()
        if self.pipe == None:
            self.makeDefaultPipe()
        
        numPipeTypes = selection.getNumPipeTypes()
        for i in range(numPipeTypes):
            pipeType = selection.getPipeType(i)
            already = 0
            for pipe in self.pipeList:
                if pipe.getType() == pipeType:
                    already = 1
                
            
            if not already:
                pipe = selection.makePipe(pipeType)
                if pipe:
                    self.notify.info('Got aux graphics pipe %s (%s).' % (pipe.getInterfaceName(), pipe.getType().getName()))
                    self.pipeList.append(pipe)
                else:
                    self.notify.info('Could not make graphics pipe %s.' % pipeType.getName())
            
        

    
    def openWindow(self, props = None, pipe = None, gsg = None, type = None, name = None, scene = None, aspectRatio = None):
        if pipe == None:
            pipe = self.pipe
            if pipe == None:
                self.makeDefaultPipe()
                pipe = self.pipe
            
            if pipe == None:
                return None
            
        
        if gsg == None:
            gsg = self.graphicsEngine.makeGsg(pipe)
            if gsg == None:
                return None
            
        
        if type == None:
            type = self.windowType
        
        if props == None:
            props = WindowProperties.getDefault()
        
        if name == None:
            name = 'window%s' % self.nextWindowIndex
            self.nextWindowIndex += 1
        
        win = None
        if type == 'onscreen':
            win = self.graphicsEngine.makeWindow(gsg, name, 0)
        elif type == 'offscreen':
            win = self.graphicsEngine.makeBuffer(gsg, name, 0, props.getXSize(), props.getYSize(), 0)
        
        if win == None:
            return None
        
        if hasattr(win, 'requestProperties'):
            win.requestProperties(props)
        
        if self.win == None:
            self.win = win
        
        self.winList.append(win)
        self.makeCamera(win, scene = scene, aspectRatio = aspectRatio)
        return win

    
    def closeWindow(self, win):
        numRegions = win.getNumDisplayRegions()
        for i in range(numRegions):
            dr = win.getDisplayRegion(i)
            cam = NodePath(dr.getCamera())
            dr.setCamera(NodePath())
            if not cam.isEmpty() and cam.node().getNumDisplayRegions() == 0:
                if self.camList.count(cam) != 0:
                    self.camList.remove(cam)
                
                if cam == self.cam:
                    self.cam = None
                
                cam.removeNode()
            
        
        self.graphicsEngine.removeWindow(win)
        self.winList.remove(win)
        if win == self.win:
            self.win = None
            self.frameRateMeter = None
        

    
    def openDefaultWindow(self):
        self.openMainWindow()
        self.graphicsEngine.openWindows()
        if self.win != None and not self.isMainWindowOpen():
            self.notify.info('Window did not open, removing.')
            self.closeWindow(self.win)
        
        if self.win == None:
            self.makeAllPipes()
            while self.win == None and len(self.pipeList) > 1:
                self.pipeList.remove(self.pipe)
                self.pipe = self.pipeList[0]
                self.openMainWindow()
                self.graphicsEngine.openWindows()
                if self.win != None and not self.isMainWindowOpen():
                    self.notify.info('Window did not open, removing.')
                    self.closeWindow(self.win)
                
        
        if self.win == None:
            self.notify.warning("Unable to open '%s' window." % self.windowType)
            if self.requireWindow:
                raise StandardError, 'Could not open window.'
            
        
        return self.win != None

    
    def isMainWindowOpen(self):
        if self.win != None:
            return self.win.isValid()
        
        return 0

    
    def openMainWindow(self):
        success = 1
        oldWin = self.win
        oldLens = self.camLens
        oldClearColorActive = None
        if self.win != None:
            oldClearColorActive = self.win.getClearColorActive()
            oldClearColor = VBase4(self.win.getClearColor())
            oldClearDepthActive = self.win.getClearDepthActive()
            oldClearDepth = self.win.getClearDepth()
            self.closeWindow(self.win)
        
        self.openWindow()
        if self.win == None:
            self.win = oldWin
            self.winList.append(oldWin)
            success = 0
        
        if self.win != None:
            if isinstance(self.win, GraphicsWindow):
                self.setupMouse(self.win)
            
            self.makeCamera2d(self.win)
            self.makeCamera2dp(self.win)
            if oldLens != None:
                self.camNode.setLens(oldLens)
                self.camLens = oldLens
            
            if oldClearColorActive != None:
                self.win.setClearColorActive(oldClearColorActive)
                self.win.setClearColor(oldClearColor)
                self.win.setClearDepthActive(oldClearDepthActive)
                self.win.setClearDepth(oldClearDepth)
            
            self.setFrameRateMeter(self.config.GetBool('show-frame-rate-meter', 0))
        
        return success

    
    def setSleep(self, amount):
        if self.sleepCycle == amount:
            return ()
        
        if time == 0.0:
            self.taskMgr.remove('sleep-cycle')
        else:
            self.sleepCycle = amount
            self.taskMgr.add(self.sleepCycleTask, 'sleep-cycle')

    
    def sleepCycleTask(self, state):
        time.sleep(self.sleepCycle)
        return Task.cont

    
    def setFrameRateMeter(self, flag):
        if flag:
            if not (self.frameRateMeter):
                self.frameRateMeter = FrameRateMeter('frameRateMeter')
                self.frameRateMeter.setupWindow(self.win)
            
        elif self.frameRateMeter:
            self.frameRateMeter.clearWindow()
            self.frameRateMeter = None
        

    
    def setupRender(self):
        self.render = NodePath('render')
        
        try:
            self.render.node().setAttrib(RescaleNormalAttrib.makeDefault())
        except:
            pass

        self.render.setTwoSided(0)
        self.backfaceCullingEnabled = 1
        self.textureEnabled = 1
        self.wireframeEnabled = 0

    
    def setupRender2d(self):
        self.render2d = NodePath('render2d')
        dt = DepthTestAttrib.make(DepthTestAttrib.MNone)
        dw = DepthWriteAttrib.make(DepthWriteAttrib.MOff)
        self.render2d.node().setAttrib(dt)
        self.render2d.node().setAttrib(dw)
        self.render2d.setMaterialOff(1)
        self.render2d.setTwoSided(1)
        aspectRatio = self.getAspectRatio()
        self.aspect2d = self.render2d.attachNewNode(PGTop('aspect2d'))
        self.aspect2d.setScale(1.0 / aspectRatio, 1.0, 1.0)
        self.a2dTop = 1.0
        self.a2dBottom = -1.0
        self.a2dLeft = -aspectRatio
        self.a2dRight = aspectRatio

    
    def setupRender2dp(self):
        self.render2dp = NodePath('render2dp')
        dt = DepthTestAttrib.make(DepthTestAttrib.MNone)
        dw = DepthWriteAttrib.make(DepthWriteAttrib.MOff)
        self.render2dp.node().setAttrib(dt)
        self.render2dp.node().setAttrib(dw)
        self.render2dp.setMaterialOff(1)
        self.render2dp.setTwoSided(1)
        aspectRatio = self.getAspectRatio()
        self.aspect2dp = self.render2dp.attachNewNode(PGTop('aspect2dp'))
        if hasattr(PGTop, 'setStartSort'):
            self.aspect2dp.node().setStartSort(16384)
        
        self.aspect2dp.setScale(1.0 / aspectRatio, 1.0, 1.0)
        self.a2dpTop = 1.0
        self.a2dpBottom = -1.0
        self.a2dpLeft = -aspectRatio
        self.a2dpRight = aspectRatio

    
    def getAspectRatio(self, win = None):
        if self.aspectRatio:
            return self.aspectRatio
        
        aspectRatio = 1
        if win == None:
            win = self.win
        
        if win != None and win.hasSize():
            aspectRatio = float(win.getXSize()) / float(win.getYSize())
        else:
            props = WindowProperties.getDefault()
            if not props.hasSize():
                props = win.getRequestedProperties()
            
            if props.hasSize():
                aspectRatio = float(props.getXSize()) / float(props.getYSize())
            
        return aspectRatio

    
    def makeCamera(self, win, sort = 0, scene = None, displayRegion = (0, 1, 0, 1), aspectRatio = None, camName = 'cam'):
        dr = win.makeDisplayRegion(*displayRegion)
        dr.setSort(sort)
        if scene == None:
            scene = self.render
        
        if aspectRatio == None:
            aspectRatio = self.getAspectRatio()
        
        camNode = Camera(camName)
        lens = PerspectiveLens()
        lens.setAspectRatio(aspectRatio)
        camNode.setLens(lens)
        if self.camera == None:
            self.camera = self.render.attachNewNode('camera')
            __builtins__['camera'] = self.camera
        
        cam = self.camera.attachNewNode(camNode)
        dr.setCamera(cam)
        if self.cam == None:
            self.cam = cam
            self.camNode = camNode
            self.camLens = lens
        
        self.camList.append(cam)
        return cam

    
    def makeCamera2d(self, win, sort = 10, displayRegion = (0, 1, 0, 1), coords = (-1, 1, -1, 1)):
        dr = win.makeDisplayRegion(*displayRegion)
        dr.setSort(sort)
        dr.setClearDepthActive(1)
        (left, right, bottom, top) = coords
        cam2dNode = Camera('cam2d')
        lens = OrthographicLens()
        lens.setFilmSize(right - left, top - bottom)
        lens.setFilmOffset((right + left) * 0.5, (top + bottom) * 0.5)
        lens.setNearFar(-1000, 1000)
        cam2dNode.setLens(lens)
        if self.camera2d == None:
            self.camera2d = self.render2d.attachNewNode('camera2d')
        
        camera2d = self.camera2d.attachNewNode(cam2dNode)
        dr.setCamera(camera2d)
        return camera2d

    
    def makeCamera2dp(self, win, sort = 20, displayRegion = (0, 1, 0, 1), coords = (-1, 1, -1, 1)):
        dr = win.makeDisplayRegion(*displayRegion)
        dr.setSort(sort)
        dr.setClearDepthActive(1)
        (left, right, bottom, top) = coords
        cam2dNode = Camera('cam2d')
        lens = OrthographicLens()
        lens.setFilmSize(right - left, top - bottom)
        lens.setFilmOffset((right + left) * 0.5, (top + bottom) * 0.5)
        lens.setNearFar(-1000, 1000)
        cam2dNode.setLens(lens)
        if self.camera2dp == None:
            self.camera2dp = self.render2dp.attachNewNode('camera2dp')
        
        camera2dp = self.camera2dp.attachNewNode(cam2dNode)
        dr.setCamera(camera2dp)
        return camera2dp

    
    def setupDataGraph(self):
        self.dataRoot = NodePath('dataRoot')
        self.dataRootNode = self.dataRoot.node()
        self.dataUnused = NodePath('dataUnused')

    
    def setupMouse(self, win):
        if self.buttonThrowers != None:
            for bt in self.buttonThrowers:
                mw = bt.getParent()
                mk = mw.getParent()
                bt.removeNode()
                mw.removeNode()
                mk.removeNode()
            
        
        self.buttonThrowers = []
        self.pointerWatcherNodes = []
        for i in range(win.getNumInputDevices()):
            name = win.getInputDeviceName(i)
            mk = self.dataRoot.attachNewNode(MouseAndKeyboard(win, i, name))
            mw = mk.attachNewNode(MouseWatcher(name))
            mb = mw.node().getModifierButtons()
            mb.addButton(KeyboardButton.shift())
            mb.addButton(KeyboardButton.control())
            mb.addButton(KeyboardButton.alt())
            mw.node().setModifierButtons(mb)
            bt = mw.attachNewNode(ButtonThrower(name))
            if i != 0:
                bt.node().setPrefix('mousedev' + str(i) + '-')
            
            mods = ModifierButtons()
            mods.addButton(KeyboardButton.shift())
            mods.addButton(KeyboardButton.control())
            mods.addButton(KeyboardButton.alt())
            bt.node().setModifierButtons(mods)
            self.buttonThrowers.append(bt)
            if win.hasPointer(i):
                self.pointerWatcherNodes.append(mw.node())
            
        
        self.mouseWatcher = self.buttonThrowers[0].getParent()
        self.mouseWatcherNode = self.mouseWatcher.node()
        if self.recorder:
            mw = self.buttonThrowers[0].getParent()
            mouseRecorder = MouseRecorder('mouse')
            self.recorder.addRecorder('mouse', mouseRecorder.upcastToRecorderBase())
            np = mw.getParent().attachNewNode(mouseRecorder)
            mw.reparentTo(np)
        
        self.trackball = self.dataUnused.attachNewNode(Trackball('trackball'))
        self.drive = self.dataUnused.attachNewNode(DriveInterface('drive'))
        self.mouse2cam = self.dataUnused.attachNewNode(Transform2SG('mouse2cam'))
        self.mouse2cam.node().setNode(self.camera.node())
        self.mouseInterface = self.trackball
        self.useTrackball()
        mw = self.buttonThrowers[0].getParent()
        self.timeButtonThrower = mw.attachNewNode(ButtonThrower('timeButtons'))
        self.timeButtonThrower.node().setPrefix('time-')
        self.timeButtonThrower.node().setTimeFlag(1)
        self.aspect2d.node().setMouseWatcher(mw.node())
        self.aspect2dp.node().setMouseWatcher(mw.node())
        mw.node().addRegion(PGMouseWatcherBackground())

    
    def enableSoftwareMousePointer(self):
        mouseViz = render2d.attachNewNode('mouseViz')
        lilsmiley = loader.loadModel('lilsmiley')
        lilsmiley.reparentTo(mouseViz)
        aspectRatio = self.getAspectRatio()
        lilsmiley.setScale(32.0 / self.win.getHeight() / aspectRatio, 1.0, 32.0 / self.win.getHeight())

    
    def getAlt(self):
        return self.mouseWatcherNode.getModifierButtons().isDown(KeyboardButton.alt())

    
    def getShift(self):
        return self.mouseWatcherNode.getModifierButtons().isDown(KeyboardButton.shift())

    
    def getControl(self):
        return self.mouseWatcherNode.getModifierButtons().isDown(KeyboardButton.control())

    
    def addAngularIntegrator(self):
        if self.physicsMgrAngular == 0:
            self.physicsMgrAngular = 1
            integrator = AngularEulerIntegrator()
            self.physicsMgr.attachAngularIntegrator(integrator)
        

    
    def enableParticles(self):
        self.particleMgrEnabled = 1
        self.physicsMgrEnabled = 1
        self.taskMgr.remove('manager-update')
        self.taskMgr.add(self.updateManagers, 'manager-update')

    
    def disableParticles(self):
        self.particleMgrEnabled = 0
        self.physicsMgrEnabled = 0
        self.taskMgr.remove('manager-update')

    
    def toggleParticles(self):
        if self.particleMgrEnabled == 0:
            self.enableParticles()
        else:
            self.disableParticles()

    
    def isParticleMgrEnabled(self):
        return self.particleMgrEnabled

    
    def isPhysicsMgrEnabled(self):
        return self.physicsMgrEnabled

    
    def updateManagers(self, state):
        dt = globalClock.getDt()
        if self.particleMgrEnabled == 1:
            self.particleMgr.doParticles(dt)
        
        if self.physicsMgrEnabled == 1:
            self.physicsMgr.doPhysics(dt)
        
        return Task.cont

    
    def createStats(self):
        if self.wantStats:
            PStatClient.connect()
        

    
    def addSfxManager(self, extraSfxManager):
        self.sfxManagerList.append(extraSfxManager)
        if extraSfxManager != None:
            pass
        newSfxManagerIsValid = extraSfxManager.isValid()
        self.sfxManagerIsValidList.append(newSfxManagerIsValid)
        if newSfxManagerIsValid:
            extraSfxManager.setActive(self.sfxActive)
        

    
    def createBaseAudioManagers(self):
        self.sfxPlayer = SfxPlayer.SfxPlayer()
        sfxManager = AudioManager.createAudioManager()
        self.addSfxManager(sfxManager)
        self.musicManager = AudioManager.createAudioManager()
        if self.musicManager != None:
            pass
        self.musicManagerIsValid = self.musicManager.isValid()
        if self.musicManagerIsValid:
            self.musicManager.setConcurrentSoundLimit(1)
            self.musicManager.setActive(self.musicActive)
        

    
    def enableMusic(self, bEnableMusic):
        if self.AppHasAudioFocus and self.musicManagerIsValid:
            self.musicManager.setActive(bEnableMusic)
        
        self.musicActive = bEnableMusic
        if bEnableMusic:
            self.notify.debug('Enabling music')
        else:
            self.notify.debug('Disabling music')

    
    def SetAllSfxEnables(self, bEnabled):
        for i in range(len(self.sfxManagerList)):
            if self.sfxManagerIsValidList[i]:
                self.sfxManagerList[i].setActive(bEnabled)
            
        

    
    def enableSoundEffects(self, bEnableSoundEffects):
        if self.AppHasAudioFocus or bEnableSoundEffects == 0:
            self.SetAllSfxEnables(bEnableSoundEffects)
        
        self.sfxActive = bEnableSoundEffects
        if bEnableSoundEffects:
            self.notify.debug('Enabling sound effects')
        else:
            self.notify.debug('Disabling sound effects')

    
    def disableAllAudio(self):
        self.AppHasAudioFocus = 0
        self.SetAllSfxEnables(0)
        if self.musicManagerIsValid:
            self.musicManager.setActive(0)
        
        self.notify.debug('Disabling audio')

    
    def enableAllAudio(self):
        self.AppHasAudioFocus = 1
        self.SetAllSfxEnables(self.sfxActive)
        if self.musicManagerIsValid:
            self.musicManager.setActive(self.musicActive)
        
        self.notify.debug('Enabling audio')

    
    def loadSfx(self, name):
        return self.loader.loadSfx(name)

    
    def loadMusic(self, name):
        return self.loader.loadMusic(name)

    
    def playSfx(self, sfx, looping = 0, interrupt = 1, volume = None, time = 0.0, node = None):
        return self.sfxPlayer.playSfx(sfx, looping, interrupt, volume, time, node)

    
    def playMusic(self, music, looping = 0, interrupt = 1, volume = None, time = 0.0):
        if music:
            if volume != None:
                music.setVolume(volume)
            
            if interrupt or music.status() != AudioSound.PLAYING:
                music.setTime(time)
                music.setLoop(looping)
                music.play()
            
        

    
    def resetPrevTransform(self, state):
        if self.cTrav:
            self.cTrav.resetPrevTransform(self.render)
        
        return Task.cont

    
    def dataLoop(self, state):
        self.dgTrav.traverse(self.dataRootNode)
        return Task.cont

    
    def ivalLoop(self, state):
        ivalMgr.step()
        return Task.cont

    
    def shadowCollisionLoop(self, state):
        if self.shadowTrav:
            self.shadowTrav.traverse(self.render)
        
        return Task.cont

    
    def collisionLoop(self, state):
        if self.cTrav:
            self.cTrav.traverse(self.render)
        
        if self.appTrav:
            self.appTrav.traverse(self.render)
        
        return Task.cont

    
    def igLoop(self, state):
        onScreenDebug.render()
        if self.recorder:
            self.recorder.recordFrame()
        
        self.graphicsEngine.renderFrame()
        if self.clusterSyncFlag:
            self.graphicsEngine.syncFrame()
        
        onScreenDebug.clear()
        if self.recorder:
            self.recorder.playFrame()
        
        if self.mainWinMinimized:
            time.sleep(0.10000000000000001)
        elif self.mwClientSleep:
            time.sleep(self.mwClientSleep)
        elif self.clientSleep:
            time.sleep(self.clientSleep)
        
        throwNewFrame()
        return Task.cont

    
    def restart(self):
        self.shutdown()
        self.taskMgr.add(self.resetPrevTransform, 'resetPrevTransform', priority = -51)
        self.taskMgr.add(self.dataLoop, 'dataLoop', priority = -50)
        self.taskMgr.add(self.ivalLoop, 'ivalLoop', priority = 20)
        self.taskMgr.add(self.collisionLoop, 'collisionLoop', priority = 30)
        self.taskMgr.add(self.shadowCollisionLoop, 'shadowCollisionLoop', priority = 34)
        self.taskMgr.add(self.igLoop, 'igLoop', priority = 50)
        self.eventMgr.restart()

    
    def shutdown(self):
        self.taskMgr.remove('igLoop')
        self.taskMgr.remove('shadowCollisionLoop')
        self.taskMgr.remove('collisionLoop')
        self.taskMgr.remove('dataLoop')
        self.taskMgr.remove('resetPrevTransform')
        self.taskMgr.remove('ivalLoop')
        self.eventMgr.shutdown()

    
    def getBackgroundColor(self, win = None):
        if win == None:
            win = self.win
        
        return VBase4(win.getClearColor())

    
    def setBackgroundColor(self, r = None, g = None, b = None, a = 1.0, win = None):
        if g != None:
            color = VBase4(r, g, b, a)
        else:
            arg = r
            if isinstance(arg, VBase4):
                color = arg
            else:
                color = VBase4(arg[0], arg[1], arg[2], a)
        if win == None:
            win = self.win
        
        if win:
            win.setClearColor(color)
        

    
    def toggleBackface(self):
        if self.backfaceCullingEnabled:
            self.backfaceCullingOff()
        else:
            self.backfaceCullingOn()

    
    def backfaceCullingOn(self):
        if not (self.backfaceCullingEnabled):
            self.render.setTwoSided(0)
        
        self.backfaceCullingEnabled = 1

    
    def backfaceCullingOff(self):
        if self.backfaceCullingEnabled:
            self.render.setTwoSided(1)
        
        self.backfaceCullingEnabled = 0

    
    def toggleTexture(self):
        if self.textureEnabled:
            self.textureOff()
        else:
            self.textureOn()

    
    def textureOn(self):
        self.render.clearTexture()
        self.textureEnabled = 1

    
    def textureOff(self):
        self.render.setTextureOff(100)
        self.textureEnabled = 0

    
    def toggleWireframe(self):
        if self.wireframeEnabled:
            self.wireframeOff()
        else:
            self.wireframeOn()

    
    def wireframeOn(self):
        self.render.setRenderModeWireframe(100)
        self.render.setTwoSided(1)
        self.wireframeEnabled = 1

    
    def wireframeOff(self):
        self.render.clearRenderMode()
        render.setTwoSided(not (self.backfaceCullingEnabled))
        self.wireframeEnabled = 0

    
    def disableMouse(self):
        if self.mouse2cam:
            self.mouse2cam.reparentTo(self.dataUnused)
        

    
    def enableMouse(self):
        if self.mouse2cam:
            self.mouse2cam.reparentTo(self.mouseInterface)
        

    
    def setMouseOnNode(self, newNode):
        if self.mouse2cam:
            self.mouse2cam.node().setNode(newNode)
        

    
    def changeMouseInterface(self, changeTo):
        self.mouseInterface.reparentTo(self.dataUnused)
        self.mouseInterface = changeTo
        self.mouseInterfaceNode = self.mouseInterface.node()
        self.mouseInterface.reparentTo(self.mouseWatcher)
        if self.mouse2cam:
            self.mouse2cam.reparentTo(self.mouseInterface)
        

    
    def useDrive(self):
        if self.drive:
            self.changeMouseInterface(self.drive)
            self.mouseInterfaceNode.reset()
            self.mouseInterfaceNode.setZ(4.0)
        

    
    def useTrackball(self):
        if self.trackball:
            self.changeMouseInterface(self.trackball)
        

    
    def oobe(self):
        
        try:
            pass
        except:
            self.oobeMode = 0
            self.oobeCamera = self.hidden.attachNewNode('oobeCamera')
            self.oobeCameraTrackball = self.oobeCamera.attachNewNode('oobeCameraTrackball')
            self.oobeLens = PerspectiveLens()
            self.oobeLens.setAspectRatio(self.getAspectRatio())
            self.oobeLens.setNearFar(0.10000000000000001, 10000.0)
            self.oobeLens.setFov(52.0)
            self.oobeTrackball = self.dataUnused.attachNewNode(Trackball('oobeTrackball'), 1)
            self.oobe2cam = self.oobeTrackball.attachNewNode(Transform2SG('oobe2cam'))
            self.oobe2cam.node().setNode(self.oobeCameraTrackball.node())
            self.oobeVis = loader.loadModelOnce('models/misc/camera')
            if self.oobeVis:
                self.oobeVis.node().setFinal(1)
            
            self.oobeCullFrustum = None
            self.oobeCullFrustumVis = None

        if self.oobeMode:
            if self.oobeCullFrustum != None:
                self.oobeCull()
            
            if self.oobeVis:
                self.oobeVis.reparentTo(self.hidden)
            
            self.oobeTrackball.reparentTo(self.dataUnused)
            self.cam.reparentTo(self.camera)
            self.camNode.setLens(self.camLens)
            self.oobeCamera.reparentTo(self.hidden)
            self.oobeMode = 0
        else:
            cameraParent = self.camera.getParent()
            self.oobeCamera.reparentTo(cameraParent)
            self.oobeCamera.clearMat()
            self.oobeTrackball.reparentTo(self.mouseWatcher)
            mat = Mat4.translateMat(0, -10, 3) * self.camera.getMat(cameraParent)
            mat.invertInPlace()
            self.oobeTrackball.node().setMat(mat)
            self.cam.reparentTo(self.oobeCameraTrackball)
            if self.oobeVis:
                self.oobeVis.reparentTo(self.camera)
            
            self.oobeMode = 1

    
    def oobeCull(self):
        
        try:
            if not (self.oobeMode):
                self.oobe()
        except:
            self.oobe()

        if self.oobeCullFrustum == None:
            pnode = LensNode('oobeCull')
            pnode.setLens(self.camLens)
            self.oobeCullFrustum = self.camera.attachNewNode(pnode)
            geom = self.camLens.makeGeometry()
            if geom != None:
                gn = GeomNode('frustum')
                gn.addGeom(geom)
                self.oobeCullFrustumVis = self.oobeVis.attachNewNode(gn)
            
            self.camNode.setCullCenter(self.oobeCullFrustum)
        else:
            self.camNode.setCullCenter(NodePath())
            self.oobeCullFrustum.removeNode()
            self.oobeCullFrustum = None
            if self.oobeCullFrustumVis != None:
                self.oobeCullFrustumVis.removeNode()
                self.oobeCullFrustumVis = None
            

    
    def showCameraFrustum(self):
        self.removeCameraFrustum()
        geom = self.camLens.makeGeometry()
        if geom != None:
            gn = GeomNode('frustum')
            gn.addGeom(geom)
            self.camFrustumVis = self.camera.attachNewNode(gn)
        

    
    def removeCameraFrustum(self):
        if self.camFrustumVis:
            self.camFrustumVis.removeNode()
        

    
    def screenshot(self, namePrefix = 'screenshot'):
        filename = self.win.saveScreenshotDefault(namePrefix)
        if filename.empty():
            return 0
        
        messenger.send('screenshot', [
            filename])
        return 1

    
    def movie(self, namePrefix = 'movie', duration = 1.0, fps = 30, format = 'rgb', sd = 4):
        globalClock.setMode(ClockObject.MNonRealTime)
        globalClock.setDt(1.0 / float(fps))
        t = taskMgr.add(self._movieTask, namePrefix + '_task')
        t.endT = globalClock.getFrameTime() + duration
        t.frameIndex = 1
        t.outputString = namePrefix + '_%0' + `sd` + 'd.' + format
        
        t.uponDeath = lambda state: globalClock.setMode(ClockObject.MNormal)

    
    def _movieTask(self, state):
        currT = globalClock.getFrameTime()
        if currT >= state.endT:
            return Task.done
        else:
            frameName = state.outputString % state.frameIndex
            self.notify.info('Capturing frame: ' + frameName)
            self.win.saveScreenshot(Filename(frameName))
            state.frameIndex += 1
            return Task.cont

    
    def _ShowBase__windowEvent(self, win):
        if win == self.win:
            properties = win.getProperties()
            self.notify.info('Got window event: %s' % repr(properties))
            if not properties.getOpen():
                self.notify.info('User closed main window.')
                self.userExit()
            
            if properties.getMinimized() and not (self.mainWinMinimized):
                self.mainWinMinimized = 1
                messenger.send('PandaPaused')
            elif not properties.getMinimized() and self.mainWinMinimized:
                self.mainWinMinimized = 0
                messenger.send('PandaRestarted')
            
        

    
    def userExit(self):
        if self.exitFunc:
            self.exitFunc()
        
        self.notify.info('Exiting ShowBase.')
        self.finalizeExit()

    
    def finalizeExit(self):
        sys.exit()

    
    def startTk(self, fWantTk = 1):
        self.wantTk = fWantTk
        if self.wantTk:
            import TkGlobal
            taskMgr.remove('tkLoop')
            TkGlobal.spawnTkLoop()
        

    
    def startDirect(self, fWantDirect = 1, fWantTk = 1):
        self.startTk(fWantTk)
        self.wantDirect = fWantDirect
        if self.wantDirect:
            DirectSession = DirectSession
            import direct.directtools
            direct.enable()
        else:
            __builtins__['direct'] = None
            self.direct = None

    
    def run(self):
        self.taskMgr.run()


