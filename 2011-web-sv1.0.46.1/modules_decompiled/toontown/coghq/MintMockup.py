# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\MintMockup.py
from pandac.PandaModules import *
from direct.showbase.PythonUtil import Enum
import random

def zoneNum2str(num):
    return 'ZONE%02i.mb' % num


class Room(NodePath):
    __module__ = __name__
    ModulePath = '/i/beta/toons/maya/work/CogHeadquarters/CogFactoriesInteriors/AllFactories/MintFactory/'
    StartingRooms = ('ZONE03a.mb', 'ZONE16a.mb')
    MiddleRooms = ('ZONE04a.mb', 'ZONE07a.mb', 'ZONE08a.mb', 'ZONE10a.mb', 'ZONE13a.mb',
                   'ZONE15a.mb', 'ZONE17a.mb', 'ZONE18a.mb', 'ZONE19a.mb')
    ConnectorRooms = ('connectors/connector_7cubeL2.mb', 'connectors/connector_7cubeR2.mb')
    EndingRooms = ('ZONE11a.mb', 'ZONE22a.mb', 'ZONE31a.mb')
    AllRooms = StartingRooms + MiddleRooms + ConnectorRooms + EndingRooms

    def __init__(self, name=None, num=None, dbg=0):
        self.loaded = False
        self.num = num
        self.name = name
        NodePath.__init__(self, hidden.attachNewNode('MintRoom-%s' % self._getModelName()))
        self.load()
        self.reparentTo(render)
        if dbg:
            self.showAxes()
            self.ls()
            print self.getPos(render)

    def __del__(self):
        self.unload()

    def load(self):
        if self.loaded:
            return
        self.loaded = True
        self.model = loader.loadModel(Room.ModulePath + self._getModelName())
        self.model.reparentTo(self)
        self.entrances = self._getEntrances()
        self.exits = self._getExits()

    def attachTo(self, other, otherDoor=None, thisDoor=None, rng=random):
        if otherDoor is None:
            otherDoor = rng.choice(other.exits)
        if thisDoor is None:
            thisDoor = rng.choice(self.entrances)
        self.reparentTo(otherDoor)
        self.clearMat()
        self.model.setPos(Vec3(0) - thisDoor.getPos(self.model))
        self.setH(-thisDoor.getH(otherDoor))
        self.wrtReparentTo(other.getParent())
        return

    def showAxes(self):
        self.axes = []
        axis = loader.loadModel('models/misc/xyzAxis.bam')
        axis.setColorOff()
        axis.setColorScale(1, 1, 1, 1, 1)
        for doorway in self.entrances + self.exits:
            self.axes.append(axis.copyTo(doorway))

        self.axes.append(axis.copyTo(self.model))
        self.axes[(-1)].setScale(0.6)

    def isolateAxis(self, index):
        for i in range(len(self.axes)):
            if i == index:
                self.axes[i].show()
            else:
                self.axes[i].hide()

    def hideAxes(self):
        for axis in self.axes:
            axis.removeNode()

        del self.axes

    def unload(self):
        if not self.loaded:
            return
        self.loaded = False
        self.model.removeNode()

    def _getModelName(self):
        if self.name is not None:
            return self.name
        return zoneNum2str(self.num)

    def _getEntrances(self):
        return self.model.findAllMatches('**/ENTRANCE*')

    def _getExits(self):
        return self.model.findAllMatches('**/EXIT*')


class MintLevel(NodePath):
    __module__ = __name__

    def __init__(self, roomNames):
        NodePath.__init__(self, hidden.attachNewNode('MintLevel'))
        self.rooms = []
        for name in roomNames:
            room = Room(name=name)
            if not len(self.rooms):
                room.reparentTo(self)
            else:
                room.attachTo(self.rooms[(-1)])
            self.rooms.append(room)


def createLevel(numRooms=None, seed=None, rooms=None):
    if rooms is None:
        if seed is None:
            seed = random.randrange(0, 50)
        rng = random.Random(seed)
        if numRooms is None:
            numRooms = rng.randrange(2, 8)
        StartingRooms = Room.StartingRooms
        EndingRooms = Room.EndingRooms
        MiddleRooms = list(Room.MiddleRooms)
        MiddleRooms.sort()
        roomNames = []

        def getARoom(choices, rng, alreadyChosen):
            while 1:
                room = rng.choice(choices)
                if room not in alreadyChosen:
                    return room

        def addRoomWithConnector(roomName, rng):
            if len(roomNames):
                connector = rng.choice(Room.ConnectorRooms)
                roomNames.append(connector)
            roomNames.append(roomName)

        addRoomWithConnector(getARoom(StartingRooms, rng, roomNames), rng)
        for i in range(numRooms - 2):
            addRoomWithConnector(getARoom(MiddleRooms, rng, roomNames), rng)

        addRoomWithConnector(getARoom(EndingRooms, rng, roomNames), rng)
    roomNames = []
    for roomName in rooms:
        if type(roomName) == type(1):
            roomName = zoneNum2str(roomName)
        roomNames.append(roomName)

    return MintLevel(roomNames)


class MintDemo:
    __module__ = __name__

    def __init__(self):
        self.level = None
        self.newLevel()
        return

    def destroy(self):
        self.level.removeNode()
        try:
            base.cr.playGame.hood.loader.geom.unstash()
        except:
            pass

    def cache(self):
        for name in Room.AllRooms:
            r = Room(name=name)
            r.unload()

    def newLevel(self, numRooms=None):
        if numRooms == None:
            numRooms = random.randrange(3, 7)
        if self.level is not None:
            self.level.removeNode()
            self.level = None
        try:
            base.cr.playGame.hood.loader.geom.stash()
        except:
            pass

        self.level = createLevel(numRooms=numRooms)
        self.level.reparentTo(render)
        base.localAvatar.clearMat()
        return