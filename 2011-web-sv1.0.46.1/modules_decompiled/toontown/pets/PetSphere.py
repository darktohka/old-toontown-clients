# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\pets\PetSphere.py
from pandac.PandaModules import *
from direct.showbase.PythonUtil import reduceAngle
from otp.movement import Impulse
from otp.otpbase import OTPGlobals

class PetSphere(Impulse.Impulse):
    __module__ = __name__
    SerialNum = 0

    def __init__(self, petRadius, collTrav):
        Impulse.Impulse.__init__(self)
        self.serialNum = PetSphere.SerialNum
        PetSphere.SerialNum += 1
        self.petRadius = petRadius
        self.collTrav = collTrav

    def _setMover(self, mover):
        Impulse.Impulse._setMover(self, mover)
        self.cSphere = CollisionSphere(0.0, 0.0, 0.0, self.petRadius)
        cSphereNode = CollisionNode('PetSphere')
        cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = hidden.attachNewNode(cSphereNode)
        self.cSphereNodePath.reparentTo(self.nodePath)
        cSphereNode.setFromCollideMask(OTPGlobals.WallBitmask)
        cSphereNode.setIntoCollideMask(OTPGlobals.WallBitmask)
        self.pusher = CollisionHandlerPusher()
        self.pusher.setHorizontal(1)
        self.pusher.setInPattern('enter%in')
        self.pusher.setOutPattern('exit%in')
        self.pusher.addCollider(self.cSphereNodePath, self.nodePath)
        self.pusher.addInPattern(self._getCollisionEvent())
        self.collTrav.addCollider(self.cSphereNodePath, self.pusher)
        self.accept(self._getCollisionEvent(), self._handleCollision)

    def _clearMover(self, mover):
        self.ignore(self._getCollisionEvent())
        self.collTrav.removeCollider(self.cSphereNodePath)
        del self.cSphere
        del self.pusher
        del self.collTrav
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath

    def _getCollisionEvent(self):
        return 'petSphereColl-%s' % self.serialNum

    def _handleCollision(self, collEntry):
        messenger.send(self.mover.getCollisionEventName(), [collEntry])