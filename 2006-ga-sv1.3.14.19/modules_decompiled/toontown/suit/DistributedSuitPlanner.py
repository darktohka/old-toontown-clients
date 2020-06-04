# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.distributed import DistributedObject
import SuitPlannerBase
from toontown.toonbase import ToontownGlobals

class DistributedSuitPlanner(DistributedObject.DistributedObject, SuitPlannerBase.SuitPlannerBase):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        SuitPlannerBase.SuitPlannerBase.__init__(self)
        self.suitList = []
        self.buildingList = [
            0,
            0,
            0,
            0]
        self.pathViz = None
        return None

    
    def generate(self):
        self.notify.info('DistributedSuitPlanner %d: generating' % self.getDoId())
        DistributedObject.DistributedObject.generate(self)
        base.cr.currSuitPlanner = self

    
    def disable(self):
        self.notify.info('DistributedSuitPlanner %d: disabling' % self.getDoId())
        self.hidePaths()
        DistributedObject.DistributedObject.disable(self)
        base.cr.currSuitPlanner = None

    
    def d_suitListQuery(self):
        self.sendUpdate('suitListQuery')

    
    def suitListResponse(self, suitList):
        self.suitList = suitList
        messenger.send('suitListResponse')

    
    def d_buildingListQuery(self):
        self.sendUpdate('buildingListQuery')

    
    def buildingListResponse(self, buildingList):
        self.buildingList = buildingList
        messenger.send('buildingListResponse')

    
    def hidePaths(self):
        if self.pathViz:
            self.pathViz.detachNode()
            self.pathViz = None
        

    
    def showPaths(self):
        self.hidePaths()
        vizNode = GeomNode(self.uniqueName('PathViz'))
        lines = LineSegs()
        self.pathViz = render.attachNewNode(vizNode)
        points = self.frontdoorPointList + self.sidedoorPointList + self.cogHQDoorPointList + self.streetPointList
        while len(points) > 0:
            self._DistributedSuitPlanner__doShowPoints(vizNode, lines, None, points)
        cnode = CollisionNode('battleCells')
        cnode.setCollideMask(BitMask32.allOff())
        for (zoneId, cellPos) in self.battlePosDict.items():
            cnode.addSolid(CollisionSphere(cellPos, 9))
            text = '%s' % zoneId
            self._DistributedSuitPlanner__makePathVizText(text, cellPos[0], cellPos[1], cellPos[2] + 9, (1, 1, 1, 1))
        
        self.pathViz.attachNewNode(cnode).show()

    
    def _DistributedSuitPlanner__doShowPoints(self, vizNode, lines, p, points):
        if p == None:
            pi = len(points) - 1
            if pi < 0:
                return None
            
            p = points[pi]
            del points[pi]
        elif p not in points:
            return None
        
        pi = points.index(p)
        del points[pi]
        text = '%s' % p.getIndex()
        pos = p.getPos()
        if p.getPointType() == DNASuitPoint.FRONTDOORPOINT:
            color = (1, 0, 0, 1)
        elif p.getPointType() == DNASuitPoint.SIDEDOORPOINT:
            color = (0, 0, 1, 1)
        else:
            color = (0, 1, 0, 1)
        self._DistributedSuitPlanner__makePathVizText(text, pos[0], pos[1], pos[2], color)
        adjacent = self.dnaStore.getAdjacentPoints(p)
        numPoints = adjacent.getNumPoints()
        for i in range(numPoints):
            qi = adjacent.getPointIndex(i)
            q = self.dnaStore.getSuitPointWithIndex(qi)
            pp = p.getPos()
            qp = q.getPos()
            v = Vec3(qp - pp)
            v.normalize()
            c = v.cross(Vec3.up())
            p1a = pp + v * 2 + c * 0.5
            p1b = pp + v * 3
            p1c = pp + v * 2 - c * 0.5
            lines.reset()
            lines.moveTo(pp)
            lines.drawTo(qp)
            lines.moveTo(p1a)
            lines.drawTo(p1b)
            lines.drawTo(p1c)
            lines.create(vizNode, 0)
            self._DistributedSuitPlanner__doShowPoints(vizNode, lines, q, points)
        

    
    def _DistributedSuitPlanner__makePathVizText(self, text, x, y, z, color):
        if not hasattr(self, 'debugTextNode'):
            self.debugTextNode = TextNode('debugTextNode')
            self.debugTextNode.setAlign(TextNode.ACenter)
            self.debugTextNode.setFont(ToontownGlobals.getSignFont())
        
        self.debugTextNode.setTextColor(*color)
        self.debugTextNode.setText(text)
        np = self.pathViz.attachNewNode(self.debugTextNode.generate())
        np.setPos(x, y, z + 1)
        np.setScale(1.0)
        np.setBillboardPointEye(2)


