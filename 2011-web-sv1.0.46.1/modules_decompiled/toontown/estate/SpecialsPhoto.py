# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\estate\SpecialsPhoto.py
from direct.directnotify import DirectNotifyGlobal
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.fishing import FishGlobals
import GardenGlobals
from direct.actor import Actor
import random

class DirectRegion(NodePath):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DirectRegion')

    def __init__(self, parent=aspect2d):
        NodePath.__init__(self)
        self.assign(parent.attachNewNode('DirectRegion'))

    def destroy(self):
        self.unload()
        self.parent = None
        return

    def setBounds(self, *bounds):
        self.bounds = bounds

    def setColor(self, *colors):
        self.color = colors

    def show(self):
        pass

    def hide(self):
        NodePath.NodePath.hide(self)

    def load(self):
        if not hasattr(self, 'cRender'):
            self.cRender = NodePath('fishSwimRender')
            self.fishSwimCamera = self.cRender.attachNewNode('fishSwimCamera')
            self.cCamNode = Camera('fishSwimCam')
            self.cLens = PerspectiveLens()
            self.cLens.setFov(40, 40)
            self.cLens.setNear(0.1)
            self.cLens.setFar(100.0)
            self.cCamNode.setLens(self.cLens)
            self.cCamNode.setScene(self.cRender)
            self.fishSwimCam = self.fishSwimCamera.attachNewNode(self.cCamNode)
            cm = CardMaker('displayRegionCard')
            apply(cm.setFrame, self.bounds)
            self.card = card = self.attachNewNode(cm.generate())
            apply(card.setColor, self.color)
            newBounds = card.getTightBounds()
            ll = render2d.getRelativePoint(card, newBounds[0])
            ur = render2d.getRelativePoint(card, newBounds[1])
            newBounds = [ll.getX(), ur.getX(), ll.getZ(), ur.getZ()]
            newBounds = map(lambda x: max(0.0, min(1.0, (x + 1.0) / 2.0)), newBounds)
            self.cDr = base.win.makeDisplayRegion(*newBounds)
            self.cDr.setSort(10)
            self.cDr.setClearColor(card.getColor())
            self.cDr.setClearDepthActive(1)
            self.cDr.setClearColorActive(1)
            self.cDr.setCamera(self.fishSwimCam)
        return self.cRender

    def unload(self):
        if hasattr(self, 'cRender'):
            base.win.removeDisplayRegion(self.cDr)
            del self.cRender
            del self.fishSwimCamera
            del self.cCamNode
            del self.cLens
            del self.fishSwimCam
            del self.cDr


class SpecialsPhoto(NodePath):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('SpecialsPhoto')

    def __init__(self, type=None, parent=aspect2d):
        NodePath.__init__(self)
        self.assign(parent.attachNewNode('SpecialsPhoto'))
        self.type = type
        self.actor = None
        self.sound = None
        self.soundTrack = None
        self.track = None
        self.specialsFrame = None
        return

    def destroy(self):
        self.hide()
        if hasattr(self, 'background'):
            self.background.destroy()
            del self.background
        if hasattr(self, 'specialsFrame') and hasattr(self.specialsFrame, 'destroy'):
            self.specialsFrame.destroy()
        if hasattr(self, 'toonStatuary'):
            if self.toonStatuary.toon:
                self.toonStatuary.deleteToon()
        self.type = None
        del self.soundTrack
        del self.track
        self.parent = None
        return

    def update(self, type):
        self.type = type

    def setBackBounds(self, *bounds):
        self.backBounds = bounds

    def setBackColor(self, *colors):
        self.backColor = colors

    def load(self):
        pass

    def makeSpecialsFrame(self, actor):
        actor.setDepthTest(1)
        actor.setDepthWrite(1)
        if not hasattr(self, 'specialsDisplayRegion'):
            self.specialsDisplayRegion = DirectRegion(parent=self)
            apply(self.specialsDisplayRegion.setBounds, self.backBounds)
            apply(self.specialsDisplayRegion.setColor, self.backColor)
        frame = self.specialsDisplayRegion.load()
        pitch = frame.attachNewNode('pitch')
        rotate = pitch.attachNewNode('rotate')
        scale = rotate.attachNewNode('scale')
        actor.reparentTo(scale)
        (bMin, bMax) = actor.getTightBounds()
        center = (bMin + bMax) / 2.0
        actor.setPos(-center[0], -center[1], -center[2])
        pitch.setY(2.5)
        return frame

    def loadModel(self, specialsIndex):
        if specialsIndex == -1:
            nodePath = self.attachNewNode('blank')
            return nodePath
        if specialsIndex >= 105 and specialsIndex <= 108:
            from toontown.estate import DistributedToonStatuary
            self.toonStatuary = DistributedToonStatuary.DistributedToonStatuary(None)
            self.toonStatuary.setupStoneToon(base.localAvatar.style)
            self.toonStatuary.poseToonFromSpecialsIndex(specialsIndex)
            self.toonStatuary.toon.setH(180)
            pedestalModelPath = GardenGlobals.Specials[specialsIndex]['photoModel']
            pedestal = loader.loadModel(pedestalModelPath)
            self.toonStatuary.toon.reparentTo(pedestal)
            pedestal.setScale(GardenGlobals.Specials[specialsIndex]['photoScale'] * 0.5)
            return pedestal
        elif specialsIndex == 135:
            model = Actor.Actor()
            modelPath = GardenGlobals.Specials[specialsIndex]['photoModel']
            anims = GardenGlobals.Specials[specialsIndex]['photoAnimation']
            animPath = modelPath + anims[1]
            model.loadModel(modelPath + anims[0])
            model.loadAnims(dict([[anims[1], animPath]]))
            frameNo = random.randint(1, 2)
            model.pose(anims[1], 1)
            model.setScale(GardenGlobals.Specials[specialsIndex]['photoScale'] * 0.1)
            return model
        else:
            modelName = GardenGlobals.Specials[specialsIndex]['photoModel']
            nodePath = loader.loadModel(modelName)
            desat = None
            colorTuple = (1, 1, 1)
            if desat and not desat.isEmpty():
                desat.setColorScale(colorTuple[0], colorTuple[1], colorTuple[2], 1.0)
            else:
                nodePath.setColorScale(colorTuple[0], colorTuple[1], colorTuple[2], 1.0)
            nodePath.setScale(GardenGlobals.Specials[specialsIndex]['photoScale'] * 0.5)
            return nodePath
        return

    def show(self, showBackground=0):
        self.notify.debug('show')
        messenger.send('wakeup')
        if self.specialsFrame:
            if hasattr(self.actor, 'cleanup'):
                self.actor.cleanup()
            if hasattr(self, 'specialsDisplayRegion'):
                self.specialsDisplayRegion.unload()
            self.hide()
        self.actor = self.loadModel(self.type)
        self.specialsFrame = self.makeSpecialsFrame(self.actor)
        if showBackground:
            if not hasattr(self, 'background'):
                background = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
                background = background.find('**/Fish_BG')
                self.background = background
            self.background.setPos(0, 15, 0)
            self.background.setScale(11)
            self.background.reparentTo(self.specialsFrame)

    def hide(self):
        NodePath.NodePath.hide(self)
        if hasattr(self, 'specialsDisplayRegion'):
            self.specialsDisplayRegion.unload()
        if hasattr(self, 'background'):
            self.background.hide()
        if self.actor:
            if hasattr(self.actor, 'stop'):
                self.actor.stop()
            self.actor.hide()
        if self.sound:
            self.sound.stop()
            self.sound = None
        if self.soundTrack:
            self.soundTrack.pause()
            self.soundTrack = None
        if self.track:
            self.track.pause()
            self.track = None
        if hasattr(self, 'toonStatuary'):
            if self.toonStatuary.toon:
                self.toonStatuary.deleteToon()
        return

    def changeVariety(self, variety):
        self.variety = variety