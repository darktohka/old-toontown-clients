# File: S (Python 2.2)

from PandaModules import *
from DirectNotifyGlobal import *
from MessengerGlobal import *
from TaskManagerGlobal import *
from EventManagerGlobal import *
from PythonUtil import *
from ParticleManagerGlobal import *
from PhysicsManagerGlobal import *
from IntervalManager import ivalMgr
import Task
import EventManager
import math
import sys
import Loader
import time
import FSM
import State
import DirectObject
import SfxPlayer
__builtins__['FADE_SORT_INDEX'] = 1000
__builtins__['NO_FADE_SORT_INDEX'] = 2000

class ShowBase(DirectObject.DirectObject):
    notify = directNotify.newCategory('ShowBase')
    
    def __init__(self):
        self.config = ConfigConfigureGetConfigConfigShowbase
        if self.config.GetBool('use-vfs', 1):
            vfs = VirtualFileSystem.getGlobalPtr()
        else:
            vfs = None
        self.sfxActive = self.config.GetBool('audio-sfx-active', 1)
        self.musicActive = self.config.GetBool('audio-music-active', 1)
        self.wantFog = self.config.GetBool('want-fog', 1)
        self.screenshotExtension = self.config.GetString('screenshot-extension', 'jpg')
        self.musicManager = None
        self.musicManagerIsValid = None
        self.sfxManagerList = []
        self.sfxManagerIsValidList = []
        self.wantStats = self.config.GetBool('want-stats', 0)
        self.exitFunc = None
        taskMgr.taskTimerVerbose = self.config.GetBool('task-timer-verbose', 0)
        taskMgr.extendedExceptions = self.config.GetBool('extended-exceptions', 0)
        taskMgr.pStatsTasks = self.config.GetBool('pstats-tasks', 0)
        taskMgr.resumeFunc = PStatClient.resumeAfterPause
        fsmRedefine = self.config.GetBool('fsm-redefine', 0)
        State.FsmRedefine = fsmRedefine
        
        try:
            self.clusterSyncFlag = clusterSyncFlag
        except NameError:
            self.clusterSyncFlag = self.config.GetBool('cluster-sync', 0)

        self.hidden = NodePath('hidden')
        self.graphicsEngine = GraphicsEngine()
        self.setupRender()
        self.setupRender2d()
        self.setupDataGraph()
        self.cTrav = 0
        self.appTrav = 0
        self.dgTrav = DataGraphTraverser()
        self.win = None
        self.winList = []
        self.mainWinMinimized = 0
        self.pipe = None
        self.pipeList = []
        self.mak = None
        self.cam = None
        self.camList = []
        self.camNode = None
        self.camLens = None
        self.camera = None
        self.cameraList = []
        self.camera2d = self.render2d.attachNewNode('camera2d')
        self.oldexitfunc = getattr(sys, 'exitfunc', None)
        sys.exitfunc = self.exitfunc
        if self.config.GetBool('open-default-window', 1):
            self.openMainWindow()
            self.graphicsEngine.renderFrame()
            self.graphicsEngine.renderFrame()
            if self.win.isClosed():
                self.notify.info('Window did not open, removing.')
                self.closeWindow(self.win)
            
            if self.win == None:
                self.makeAllPipes()
                while self.win == None and len(self.pipeList) > 1:
                    self.pipeList.remove(self.pipe)
                    self.pipe = self.pipeList[0]
                    self.openMainWindow()
                    self.graphicsEngine.renderFrame()
                    self.graphicsEngine.renderFrame()
                    if self.win.isClosed():
                        self.notify.info('Window did not open, removing.')
                        self.closeWindow(self.win)
                    
            
        
        self.loader = Loader.Loader(self)
        self.eventMgr = eventMgr
        self.messenger = messenger
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
        __builtins__['aspect2d'] = self.aspect2d
        __builtins__['render'] = self.render
        __builtins__['hidden'] = self.hidden
        __builtins__['camera'] = self.camera
        __builtins__['loader'] = self.loader
        __builtins__['taskMgr'] = self.taskMgr
        __builtins__['eventMgr'] = self.eventMgr
        __builtins__['messenger'] = self.messenger
        __builtins__['config'] = self.config
        __builtins__['run'] = self.run
        __builtins__['ostream'] = Notify.out()
        __builtins__['directNotify'] = directNotify
        __builtins__['globalClock'] = ClockObject.getGlobalClock()
        __builtins__['vfs'] = vfs
        self.accept('window-event', self._ShowBase__windowEvent)
        import Transitions
        self.transitions = Transitions.Transitions(self.loader)
        self.startTk(self.config.GetBool('want-tk', 0))
        self.startDirect(self.config.GetBool('want-directtools', 0))
        self.restart()

    
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
            self.notify.error('No graphics pipe is available!  Check your Configrc!')
        
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
            
        

    
    def openWindow(self):
        if self.pipe == None:
            self.makeDefaultPipe()
        
        chanString = self.config.GetString('chan-config', 'single')
        chanConfig = ChanConfig(self.graphicsEngine, self.pipe, chanString, self.render)
        win = chanConfig.getWin()
        if win != None:
            props = WindowProperties()
            windowTitle = self.config.GetString('window-title', '')
            if windowTitle:
                props.setTitle(windowTitle)
            
            win.requestProperties(props)
            if self.win == None:
                self.win = win
            
            self.winList.append(win)
            self.getCameras(chanConfig)
        
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
                
                if not cam.isEmpty():
                    camera = cam.getParent()
                    if self.cameraList.count(camera) != 0:
                        self.cameraList.remove(camera)
                    
                    if cam == self.cam:
                        self.cam = None
                    
                    cam.removeNode()
                
            
        
        self.graphicsEngine.removeWindow(win)
        self.winList.remove(win)
        if win == self.win:
            self.win = None
        

    
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
            self.setupMouse(self.win)
            self.makeCamera2d(self.win, -1, 1, -1, 1)
            if oldLens != None:
                self.camNode.setLens(oldLens)
                self.camLens = oldLens
            
            if oldClearColorActive != None:
                self.win.setClearColorActive(oldClearColorActive)
                self.win.setClearColor(oldClearColor)
                self.win.setClearDepthActive(oldClearDepthActive)
                self.win.setClearDepth(oldClearDepth)
            
        
        return success

    
    def setupRender(self):
        self.render = NodePath('render')
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
        self.aspectRatio = self.config.GetFloat('aspect-ratio', 4.0 / 3.0)
        self.aspect2d = self.render2d.attachNewNode(PGTop('aspect2d'))
        self.aspect2d.setScale(1.0 / self.aspectRatio, 1.0, 1.0)
        self.a2dTop = 1.0
        self.a2dBottom = -1.0
        self.a2dLeft = -(self.aspectRatio)
        self.a2dRight = self.aspectRatio

    
    def makeCamera2d(self, win, left, right, bottom, top):
        chan = win.getChannel(0)
        layer = chan.makeLayer()
        dr = layer.makeDisplayRegion()
        dr.setClearDepthActive(1)
        cam2dNode = Camera('cam2d')
        lens = OrthographicLens()
        lens.setFilmSize(right - left, top - bottom)
        lens.setFilmOffset((right + left) * 0.5, (top + bottom) * 0.5)
        lens.setNearFar(-1000, 1000)
        cam2dNode.setLens(lens)
        cam2dNode.setScene(self.render2d)
        camera2d = self.camera2d.attachNewNode(cam2dNode)
        dr.setCamera(camera2d)
        return camera2d

    
    def setupDataGraph(self):
        self.dataRoot = NodePath('dataRoot')
        self.dataRootNode = self.dataRoot.node()
        self.dataUnused = NodePath('dataUnused')

    
    def setupMouse(self, win):
        if self.mak != None:
            self.mak.node().setSource(win, 0)
            bt = self.buttonThrower.node()
            mb = ModifierButtons(bt.getModifierButtons())
            mb.allButtonsUp()
            bt.setModifierButtons(mb)
            return None
        
        self.mak = self.dataRoot.attachNewNode(MouseAndKeyboard(win, 0, 'mak'))
        self.mouseWatcherNode = MouseWatcher('mouseWatcher')
        self.mouseWatcher = self.mak.attachNewNode(self.mouseWatcherNode)
        mb = self.mouseWatcherNode.getModifierButtons()
        mb.addButton(KeyboardButton.shift())
        mb.addButton(KeyboardButton.control())
        mb.addButton(KeyboardButton.alt())
        self.mouseWatcherNode.setModifierButtons(mb)
        self.trackball = self.dataUnused.attachNewNode(Trackball('trackball'))
        self.drive = self.dataUnused.attachNewNode(DriveInterface('drive'))
        self.mouse2cam = self.dataUnused.attachNewNode(Transform2SG('mouse2cam'))
        self.mouse2cam.node().setNode(self.camera.node())
        self.mouseInterface = self.trackball
        self.useTrackball()
        self.buttonThrower = self.mouseWatcher.attachNewNode(ButtonThrower('buttons'))
        mods = ModifierButtons()
        mods.addButton(KeyboardButton.shift())
        mods.addButton(KeyboardButton.control())
        mods.addButton(KeyboardButton.alt())
        self.buttonThrower.node().setModifierButtons(mods)
        self.aspect2d.node().setMouseWatcher(self.mouseWatcherNode)
        self.mouseWatcherNode.addRegion(PGMouseWatcherBackground())

    
    def enableSoftwareMousePointer(self):
        mouseViz = render2d.attachNewNode('mouseViz')
        lilsmiley = loader.loadModel('lilsmiley')
        lilsmiley.reparentTo(mouseViz)
        lilsmiley.setScale(32.0 / self.win.getHeight() / self.aspectRatio, 1.0, 32.0 / self.win.getHeight())

    
    def getCameras(self, chanConfig):
        for i in range(chanConfig.getNumGroups()):
            camera = NodePath(chanConfig.getGroupNode(i))
            cam = camera.find('**/+Camera')
            if self.camera != None and len(self.cameraList) == 0:
                camera = self.camera
                cam.reparentTo(camera)
            else:
                camera.reparentTo(self.render)
            self.cameraList.append(camera)
            self.camList.append(cam)
            lens = cam.node().getLens()
            lens.setAspectRatio(self.aspectRatio)
        
        if self.camera == None:
            self.camera = self.cameraList[0]
        
        if self.cam == None:
            self.cam = self.camList[0]
            self.camNode = self.cam.node()
            self.camLens = self.camNode.getLens()
        

    
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
        dt = min(globalClock.getDt(), 0.10000000000000001)
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
            self.musicManager.setMutuallyExclusive(1)
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
            
        

    
    def dataloop(self, state):
        self.dgTrav.traverse(self.dataRootNode)
        return Task.cont

    
    def ivalloop(self, state):
        ivalMgr.step()
        return Task.cont

    
    def collisionloop(self, state):
        if self.cTrav:
            self.cTrav.traverse(self.render)
        
        if self.appTrav:
            self.appTrav.traverse(self.render)
        
        return Task.cont

    
    def igloop(self, state):
        self.graphicsEngine.renderFrame()
        if self.clusterSyncFlag:
            self.graphicsEngine.syncFrame()
        
        if self.mainWinMinimized:
            time.sleep(0.10000000000000001)
        
        throwNewFrame()
        return Task.cont

    
    def restart(self):
        self.shutdown()
        self.taskMgr.add(self.igloop, 'igloop', priority = 50)
        self.taskMgr.add(self.collisionloop, 'collisionloop', priority = 45)
        self.taskMgr.add(self.dataloop, 'dataloop', priority = -50)
        self.taskMgr.add(self.ivalloop, 'ivalloop', priority = 10)
        self.eventMgr.restart()

    
    def shutdown(self):
        self.taskMgr.remove('igloop')
        self.taskMgr.remove('collisionloop')
        self.taskMgr.remove('dataloop')
        self.taskMgr.remove('ivalloop')
        self.eventMgr.shutdown()

    
    def getBackgroundColor(self):
        return VBase4(self.win.getClearColor())

    
    def setBackgroundColor(self, *args):
        numArgs = len(args)
        if numArgs == 3 or numArgs == 4:
            color = VBase4(args[0], args[1], args[2], 1.0)
        elif numArgs == 1:
            arg = args[0]
            color = VBase4(arg[0], arg[1], arg[2], 1.0)
        else:
            raise TypeError, 'Invalid number of arguments: %d, expected 1, 3, or 4.' % numArgs
        self.win.setClearColor(color)

    
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
        self.mouse2cam.reparentTo(self.dataUnused)

    
    def enableMouse(self):
        self.mouse2cam.reparentTo(self.mouseInterface)

    
    def setMouseOnNode(self, newNode):
        self.mouse2cam.node().setNode(newNode)

    
    def useDrive(self):
        self.mouseInterface.reparentTo(self.dataUnused)
        self.mouseInterface = self.drive
        self.mouseInterfaceNode = self.mouseInterface.node()
        self.mouseInterface.reparentTo(self.mouseWatcher)
        self.mouse2cam.reparentTo(self.mouseInterface)
        self.mouseInterfaceNode.reset()
        self.mouseInterfaceNode.setZ(4.0)

    
    def useTrackball(self):
        self.mouseInterface.reparentTo(self.dataUnused)
        self.mouseInterface = self.trackball
        self.mouseInterfaceNode = self.mouseInterface.node()
        self.mouseInterface.reparentTo(self.mouseWatcher)
        self.mouse2cam.reparentTo(self.mouseInterface)

    
    def oobe(self):
        
        try:
            pass
        except:
            self.oobeMode = 0
            self.oobeCamera = self.hidden.attachNewNode('oobeCamera')
            self.oobeCameraTrackball = self.oobeCamera.attachNewNode('oobeCameraTrackball')
            self.oobeLens = PerspectiveLens()
            self.oobeLens.setAspectRatio(self.aspectRatio)
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
            self.camNode.setLens(self.oobeLens)
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
            
            numDisplayRegions = self.camNode.getNumDisplayRegions()
            for d in range(0, numDisplayRegions):
                dr = self.camNode.getDisplayRegion(d)
                dr.setCullFrustum(pnode)
            
        else:
            numDisplayRegions = self.camNode.getNumDisplayRegions()
            for d in range(0, numDisplayRegions):
                dr = self.camNode.getDisplayRegion(d)
                dr.setCullFrustum(self.camNode)
            
            self.oobeCullFrustum.removeNode()
            self.oobeCullFrustum = None
            if self.oobeCullFrustumVis != None:
                self.oobeCullFrustumVis.removeNode()
                self.oobeCullFrustumVis = None
            

    
    def screenshot(self, namePrefix = 'screenshot'):
        date = time.ctime(time.time())
        frameCount = globalClock.getFrameCount()
        date = date.replace(' ', '-')
        date = date.replace(':', '-')
        imageName = '%s-%s-%d.%s' % (namePrefix, date, frameCount, self.screenshotExtension)
        self.notify.info('Taking screenshot: ' + imageName)
        takeSnapshot(self.win, imageName)
        messenger.send('screenshot')

    
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
            takeSnapshot(self.win, frameName)
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
        sys.exit()

    
    def startTk(self, fWantTk = 1):
        self.wantTk = fWantTk
        if self.wantTk:
            import TkGlobal
        

    
    def startDirect(self, fWantDirect = 1):
        self.wantDirect = fWantDirect
        if self.wantDirect:
            import DirectSession
            direct.enable()
        else:
            __builtins__['direct'] = None
            self.direct = None

    
    def run(self):
        self.taskMgr.run()


