# File: P (Python 2.2)

from toontown.toonbase.ToontownGlobals import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
import BasicEntities
from toontown.suit import GoonPathData

class PathEntity(BasicEntities.NodePathEntity):
    
    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.path = GoonPathData.Paths[self.level.factoryId][self.pathIndex]

    
    def destroy(self):
        BasicEntities.NodePathEntity.destroy(self)

    
    def setPathIndex(self, pathIndex):
        self.pathIndex = pathIndex
        self.path = GoonPathData.Paths[self.level.factoryId][self.pathIndex]

    
    def makePathTrack(self, node, velocity, name, turnTime = 1, lookAroundNode = None):
        track = Sequence(name = name)
        path = self.path + [
            self.path[0]]
        for pointIndex in range(len(path) - 1):
            startPoint = path[pointIndex]
            endPoint = path[pointIndex + 1]
            v = startPoint - endPoint
            node.setPos(startPoint[0], startPoint[1], startPoint[2])
            node.headsUp(endPoint[0], endPoint[1], endPoint[2])
            theta = node.getH() % 360
            track.append(LerpHprInterval(node, turnTime, Vec3(theta, 0, 0)))
            distance = Vec3(v).length()
            duration = distance / velocity
            track.append(LerpPosInterval(node, duration = duration, pos = Point3(endPoint), startPos = Point3(startPoint)))
        
        return track


