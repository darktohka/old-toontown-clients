# File: R (Python 2.2)

from pandac.PandaModules import *
import types

class Rope(NodePath):
    showRope = base.config.GetBool('show-rope', 1)
    
    def __init__(self, name = 'Rope'):
        self.ropeNode = RopeNode(name)
        self.curve = NurbsCurveEvaluator()
        self.ropeNode.setCurve(self.curve)
        NodePath.__init__(self, self.ropeNode)
        self.name = name

    
    def setup(self, order, verts, knots = None):
        self.order = order
        self.verts = verts
        self.knots = knots
        self.recompute()

    
    def recompute(self):
        if not (self.showRope):
            return None
        
        numVerts = len(self.verts)
        self.curve.reset(numVerts)
        self.curve.setOrder(self.order)
        for i in range(numVerts):
            (nodePath, point) = self.verts[i]
            if isinstance(point, types.TupleType):
                if len(point) >= 4:
                    self.curve.setVertex(i, VBase4(point[0], point[1], point[2], point[3]))
                else:
                    self.curve.setVertex(i, VBase3(point[0], point[1], point[2]))
            else:
                self.curve.setVertex(i, point)
            if nodePath:
                self.curve.setVertexSpace(i, nodePath)
            
        
        if self.knots != None:
            for i in range(len(self.knots)):
                self.curve.setKnot(i, self.knots[i])
            
        
        self.ropeNode.resetBound(self)

    
    def getPoints(self, len):
        result = self.curve.evaluate(self)
        numPts = len
        ropePts = []
        for i in range(numPts):
            pt = Point3()
            result.evalPoint(i / float(numPts - 1), pt)
            ropePts.append(pt)
        
        return ropePts


