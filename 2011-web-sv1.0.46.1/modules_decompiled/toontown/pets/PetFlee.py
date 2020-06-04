# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\pets\PetFlee.py
from pandac.PandaModules import *
from direct.showbase.PythonUtil import reduceAngle
from otp.movement import Impulse

class PetFlee(Impulse.Impulse):
    __module__ = __name__

    def __init__(self, chaser=None, maxDist=50.0, moveAngle=20.0):
        Impulse.Impulse.__init__(self)
        self.chaser = chaser
        self.maxDist = maxDist
        self.moveAngle = moveAngle
        self.lookAtNode = NodePath('lookatNode')
        self.lookAtNode.hide()
        self.vel = None
        self.rotVel = None
        return

    def destroy(self):
        self.lookAtNode.removeNode()
        del self.lookAtNode
        del self.chaser
        del self.vel
        del self.rotVel

    def setChaser(self, chaser):
        self.chaser = chaser

    def _setMover(self, mover):
        Impulse.Impulse._setMover(self, mover)
        self.lookAtNode.reparentTo(self.nodePath)
        self.vel = self.VecType(0)
        self.rotVel = self.VecType(0)

    def _process(self, dt):
        Impulse.Impulse._process(self, dt)
        me = self.nodePath
        chaser = self.chaser
        chaserPos = chaser.getPos(me)
        chaserPos.setZ(0)
        distance = self.VecType(chaserPos).length()
        self.lookAtNode.lookAt(chaser)
        relH = reduceAngle(self.lookAtNode.getH(me) + 180.0)
        epsilon = 0.005
        rotSpeed = self.mover.getRotSpeed()
        if relH < -epsilon:
            vH = -rotSpeed
        elif relH > epsilon:
            vH = rotSpeed
        else:
            vH = 0
        if abs(vH * dt) > abs(relH):
            vH = relH / dt
        if distance < self.maxDist and abs(relH) < self.moveAngle:
            vForward = self.mover.getFwdSpeed()
        else:
            vForward = 0
        distanceLeft = self.maxDist - distance
        if distanceLeft > 0.0 and vForward * dt > distanceLeft:
            vForward = distanceLeft / dt
        self.vel.setY(vForward)
        self.rotVel.setX(vH)
        self.mover.addShove(self.vel)
        self.mover.addRotShove(self.rotVel)