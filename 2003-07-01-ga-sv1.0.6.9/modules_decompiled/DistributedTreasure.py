# File: D (Python 2.2)

from ShowBaseGlobal import *
from PandaObject import *
from IntervalGlobal import *
from ToontownGlobals import *
import DistributedObject
import DirectNotifyGlobal

class DistributedTreasure(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTreasure')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.av = None
        self.treasureFlyTrack = None
        self.modelPath = None
        self.modelFindString = None
        self.grabSoundPath = None
        self.rejectSoundPath = 'phase_4/audio/sfx/ring_miss.mp3'
        self.playSoundForRemoteToons = 1
        self.scale = 1.0
        self.shadow = 1
        self.fly = 1
        self.zOffset = 0.0
        self.billboard = 0

    
    def disable(self):
        self.ignoreAll()
        self.nodePath.reparentTo(hidden)

    
    def delete(self):
        if self.treasureFlyTrack:
            self.treasureFlyTrack.finish()
            self.treasureFlyTrack = None
        
        self.nodePath.removeNode()
        del self.nodePath
        del self.collSphere
        self.collNodePath.removeNode()
        del self.collNodePath
        del self.collNode

    
    def generateInit(self):
        self.nodePath = self.loadModel()
        self.collSphere = CollisionSphere(0, 0, 0, self.getSphereRadius())
        self.collSphere.setTangible(0)
        self.collNode = CollisionNode(self.uniqueName('treasureSphere'))
        self.collNode.setIntoCollideMask(WallBitmask)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.nodePath.attachNewNode(self.collNode)
        self.collNodePath.hide()

    
    def generate(self):
        self.nodePath.wrtReparentTo(render)
        self.accept(self.uniqueName('entertreasureSphere'), self.handleEnterSphere)

    
    def handleEnterSphere(self, collEntry):
        localAvId = toonbase.localToon.getDoId()
        if not (self.fly):
            self.handleGrab(localAvId)
        
        self.d_requestGrab()

    
    def d_requestGrab(self):
        self.sendUpdate('requestGrab', [])

    
    def getSphereRadius(self):
        return 2.0

    
    def loadModel(self):
        self.grabSound = base.loadSfx(self.grabSoundPath)
        self.rejectSound = base.loadSfx(self.rejectSoundPath)
        treasure = NodePath(self.uniqueName('treasure'))
        model = loader.loadModelOnce(self.modelPath)
        if self.modelFindString != None:
            model = model.find('**/' + self.modelFindString)
        
        model.instanceTo(treasure)
        if self.billboard:
            treasure.setBillboardPointEye()
        
        treasure.setScale(0.90000000000000002 * self.scale)
        if self.shadow:
            self.dropShadow = loader.loadModelCopy('phase_3/models/props/drop_shadow')
            self.dropShadow.setColor(0, 0, 0, 0.5)
            self.dropShadow.reparentTo(treasure)
            self.dropShadow.setPos(0, 0, 0.025000000000000001)
            self.dropShadow.setScale(0.40000000000000002 * self.scale)
            self.dropShadow.flattenLight()
        
        treasure.reparentTo(self.getParentNodePath())
        return treasure

    
    def getParentNodePath(self):
        return render

    
    def setPosition(self, x, y, z):
        self.nodePath.setPos(x, y, z + self.zOffset)

    
    def setGrab(self, avId):
        if self.fly or avId != toonbase.localToon.getDoId():
            self.handleGrab(avId)
        

    
    def setReject(self):
        if self.treasureFlyTrack:
            self.treasureFlyTrack.finish()
            self.treasureFlyTrack = None
        
        base.playSfx(self.rejectSound)
        self.treasureFlyTrack = Sequence(LerpColorScaleInterval(self.nodePath, 0.80000000000000004, colorScale = VBase4(0, 0, 0, 0), startColorScale = VBase4(1, 1, 1, 1), blendType = 'easeIn'), LerpColorScaleInterval(self.nodePath, 0.20000000000000001, colorScale = VBase4(1, 1, 1, 1), startColorScale = VBase4(0, 0, 0, 0), blendType = 'easeOut'), name = self.uniqueName('treasureFlyTrack'))
        self.treasureFlyTrack.start()

    
    def handleGrab(self, avId):
        self.ignore(self.uniqueName('entertreasureSphere'))
        self.avId = avId
        if self.shadow:
            self.dropShadow.hide()
        
        if self.cr.doId2do.has_key(avId):
            av = self.cr.doId2do[avId]
            self.av = av
        else:
            self.nodePath.reparentTo(hidden)
            return None
        if self.playSoundForRemoteToons or self.avId == toonbase.localToon.getDoId():
            base.playSfx(self.grabSound)
        
        if not (self.fly):
            self.nodePath.reparentTo(hidden)
            return None
        
        self.nodePath.wrtReparentTo(av)
        if self.treasureFlyTrack:
            self.treasureFlyTrack.finish()
            self.treasureFlyTrack = None
        
        flytime = 1.0
        self.treasureFlyTrack = Sequence(LerpPosInterval(self.nodePath, flytime, pos = Point3(0, 0, 3), startPos = self.nodePath.getPos(), blendType = 'easeInOut'), ParentInterval(self.nodePath, hidden), name = self.uniqueName('treasureFlyTrack'))
        self.treasureFlyTrack.start()
        self.accept(self.av.uniqueName('disable'), self.handleUnexpectedExit)

    
    def handleUnexpectedExit(self):
        self.notify.warning('While getting treasure, ' + str(self.avId) + ' disconnected.')
        if self.treasureFlyTrack:
            self.treasureFlyTrack.finish()
            self.treasureFlyTrack = None
        

    
    def getStareAtNodeAndOffset(self):
        return (self.nodePath, Point3())


