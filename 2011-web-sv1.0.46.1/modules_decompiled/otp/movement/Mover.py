# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\movement\Mover.py
from pandac.PandaModules import *
from libotp import CMover
from direct.directnotify import DirectNotifyGlobal
from otp.movement.PyVec3 import PyVec3
from direct.showbase import PythonUtil
import __builtin__

class Mover(CMover):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('Mover')
    SerialNum = 0
    Profile = 0
    Pstats = 1
    PSCCpp = 'App:Show code:moveObjects:MoverC++'
    PSCPy = 'App:Show code:moveObjects:MoverPy'
    PSCInt = 'App:Show code:moveObjects:MoverIntegrate'

    def __init__(self, objNodePath, fwdSpeed=1, rotSpeed=1):
        CMover.__init__(self, objNodePath, fwdSpeed, rotSpeed)
        self.serialNum = Mover.SerialNum
        Mover.SerialNum += 1
        self.VecType = Vec3
        self.impulses = {}
        if Mover.Pstats:
            self.pscCpp = PStatCollector(Mover.PSCCpp)
            self.pscPy = PStatCollector(Mover.PSCPy)
            self.pscInt = PStatCollector(Mover.PSCInt)

    def destroy(self):
        for (name, impulse) in self.impulses.items():
            Mover.notify.debug('removing impulse: %s' % name)
            self.removeImpulse(name)

    def addImpulse(self, name, impulse):
        if impulse.isCpp():
            CMover.addCImpulse(self, name, impulse)
        else:
            self.impulses[name] = impulse
            impulse._setMover(self)

    def removeImpulse(self, name):
        if name not in self.impulses:
            if not CMover.removeCImpulse(self, name):
                Mover.notify.warning("Mover.removeImpulse: unknown impulse '%s'" % name)
            return
        self.impulses[name]._clearMover(self)
        del self.impulses[name]

    def getCollisionEventName(self):
        return 'moverCollision-%s' % self.serialNum

    def move(self, dt=-1, profile=0):
        if Mover.Profile and not profile:

            def func(doMove=self.move):
                for i in xrange(10000):
                    doMove(dt, profile=1)

            __builtin__.func = func
            PythonUtil.startProfile(cmd='func()', filename='profile', sorts=['cumulative'], callInfo=0)
            del __builtin__.func
            return
        if Mover.Pstats:
            self.pscCpp.start()
        CMover.processCImpulses(self, dt)
        if Mover.Pstats:
            self.pscCpp.stop()
            self.pscPy.start()
        for impulse in self.impulses.values():
            impulse._process(self.getDt())

        if Mover.Pstats:
            self.pscPy.stop()
            self.pscInt.start()
        CMover.integrate(self)
        if Mover.Pstats:
            self.pscInt.stop()