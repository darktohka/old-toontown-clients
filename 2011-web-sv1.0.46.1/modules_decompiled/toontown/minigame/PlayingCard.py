# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\PlayingCard.py
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.task import Task
from toontown.toonbase import TTLocalizer
import PlayingCardGlobals

class PlayingCardBase:
    __module__ = __name__

    def __init__(self, value):
        self.faceUp = 1
        self.setValue(value)

    def getCardName(self):
        PlayingCardGlobals.getCardName(self.value)

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def setImage(self):
        pass

    def setValue(self, value):
        self.value = value
        if self.value == PlayingCardGlobals.Unknown:
            self.suit = None
            self.rank = None
            self.turnDown()
        else:
            self.suit = value / PlayingCardGlobals.MaxRank
            self.rank = value % PlayingCardGlobals.MaxRank
        self.setImage()
        return

    def isFaceUp(self):
        return self.faceUp

    def isFaceDown(self):
        return not self.faceUp

    def turnUp(self):
        self.faceUp = 1
        self.setImage()

    def turnDown(self):
        self.faceUp = 0
        self.setImage()


class PlayingCardNodePath(NodePath, PlayingCardBase):
    __module__ = __name__

    def __init__(self, style, value):
        self.image = None
        self.style = style
        NodePath.__init__(self, 'PlayingCard')
        PlayingCardBase.__init__(self, value)
        return

    def setImage(self):
        if self.faceUp:
            image = PlayingCardGlobals.getImage(self.style, self.suit, self.rank)
        else:
            image = PlayingCardGlobals.getBack(self.style)
        if self.image:
            self.image.removeNode()
        self.image = image.copyTo(self)


class PlayingCardButton(PlayingCardBase, DirectButton):
    __module__ = __name__

    def __init__(self, style, value):
        PlayingCardBase.__init__(self, value)
        self.style = style
        DirectButton.__init__(self, relief=None)
        self.initialiseoptions(PlayingCardButton)
        self.bind(DGG.B1PRESS, self.dragStart)
        self.bind(DGG.B1RELEASE, self.dragStop)
        return

    def setImage(self):
        if self.faceUp:
            image = PlayingCardGlobals.getImage(self.style, self.suit, self.rank)
        else:
            image = PlayingCardGlobals.getBack(self.style)
        self['image'] = image

    def dragStart(self, event):
        taskMgr.remove(self.taskName('dragTask'))
        vWidget2render2d = self.getPos(render2d)
        vMouse2render2d = Point3(event.getMouse()[0], 0, event.getMouse()[1])
        editVec = Vec3(vWidget2render2d - vMouse2render2d)
        task = taskMgr.add(self.dragTask, self.taskName('dragTask'))
        task.editVec = editVec

    def dragTask(self, task):
        mwn = base.mouseWatcherNode
        if mwn.hasMouse():
            vMouse2render2d = Point3(mwn.getMouse()[0], 0, mwn.getMouse()[1])
            newPos = vMouse2render2d + task.editVec
            self.setPos(render2d, newPos)
        return Task.cont

    def dragStop(self, event):
        taskMgr.remove(self.taskName('dragTask'))
        messenger.send('PlayingCardDrop', sentArgs=[self])

    def destroy(self):
        taskMgr.remove(self.taskName('dragTask'))
        DirectButton.destroy(self)