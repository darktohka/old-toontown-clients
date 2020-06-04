# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\pets\PetCollider.py
from pandac.PandaModules import *
from direct.showbase.PythonUtil import reduceAngle
from otp.movement import Impulse
from otp.otpbase import OTPGlobals

class PetCollider(Impulse.Impulse):
    __module__ = __name__
    SerialNum = 0

    def __init__(self, petRadius, collTrav):
        Impulse.Impulse.__init__(self)
        self.petRadius = petRadius
        self.collTrav = collTrav
        self.vel = None
        self.rotVel = None
        self.vH = 0
        self.fwdCLine = CollisionSegment(0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        self.leftCLine = CollisionSegment(0.0, 0.0, 0.0, -1.0, 1.0, 0.0)
        self.rightCLine = CollisionSegment(0.0, 0.0, 0.0, 1.0, 1.0, 0.0)
        self.calcCollLines()
        cLineNode = CollisionNode('cLineNode')
        cLineNode.addSolid(self.fwdCLine)
        cLineNode.addSolid(self.leftCLine)
        cLineNode.addSolid(self.rightCLine)
        cLineNode.setFromCollideMask(OTPGlobals.WallBitmask)
        cLineNode.setIntoCollideMask(BitMask32.allOff())
        self.cLineNodePath = hidden.attachNewNode(cLineNode)
        self.cHandler = CollisionHandlerEvent()
        self.cHandler.addInPattern(self._getCollisionEvent())
        self.cHandler.addAgainPattern(self._getCollisionEvent())
        self.collTrav.addCollider(self.cLineNodePath, self.cHandler)
        self.accept(self._getCollisionEvent(), self.handleCollision)
        return

    def _setMover(self, mover):
        Impulse.Impulse._setMover(self, mover)
        self.cLineNodePath.reparentTo(self.nodePath)
        self.vel = self.VecType(0)
        self.rotVel = self.VecType(0)

    def destroy(self):
        self.ignore(self._getCollisionEvent())
        self.collTrav.removeCollider(self.cLineNodePath)
        del self.cHandler
        del self.collTrav
        self.cLineNodePath.removeNode()
        del self.cLineNodePath
        del self.vel

    def calcCollLines(self):
        self.fwdCLine.setPointB(Point3(0, self.mover.getFwdSpeed(), 0))
        self.leftCLine.setPointB(Point3(-self.petRadius, self.petRadius, 0))
        self.rightCLine.setPointB(Point3(self.petRadius, self.petRadius, 0))

    def _getSerialNum(self):
        if not hasattr(self, 'serialNum'):
            self.serialNum = PetCollider.SerialNum
            PetCollider.SerialNum += 1
        return self.serialNum

    def _getCollisionEvent(self):
        return 'petFeeler-%s' % self._getSerialNum()

    def handleCollision(self, collEntry):
        print 'collision!'
        cPoint = collEntry.getSurfacePoint(self.cLineNodePath)
        cNormal = collEntry.getSurfaceNormal(self.cLineNodePath)
        messenger.send(self.mover.getCollisionEventName(), [
         cPoint, cNormal])