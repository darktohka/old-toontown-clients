# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\PropSpinner.py
import string
from direct.interval.IntervalGlobal import *
from Entity import Entity
from pandac.PandaModules import Vec3

class PropSpinner(Entity):
    __module__ = __name__

    def __init__(self, level, entId):
        Entity.__init__(self, level, entId)
        self.initProps()

    def destroy(self):
        self.destroyProps()
        Entity.destroy(self)

    def initProps(self):
        topNode = self.getZoneNode()
        props = topNode.findAllMatches('**/Prop_*')
        spinTracks = Parallel()
        for prop in props:
            name = prop.getName()
            nameParts = name.split('_')
            axis = nameParts[2]
            rate = 0
            neg = string.upper(nameParts[3][0]) == 'N'
            if neg:
                nameParts[3] = nameParts[3][1:]
            try:
                rate = int(nameParts[3])
            except:
                print 'invalid prop rotate string: %s' % name

            if neg:
                rate = -rate
            prop.setHpr(0, 0, 0)
            if axis == 'X':
                hpr = Vec3(0, rate * 360, 0)
            elif axis == 'Y':
                hpr = Vec3(rate * 360, 0, 0)
            elif axis == 'Z':
                hpr = Vec3(0, 0, rate * 360)
            else:
                print 'error', axis
            spinTracks.append(LerpHprInterval(prop, 60, hpr))

        spinTracks.loop()
        self.spinTracks = spinTracks

    def destroyProps(self):
        if hasattr(self, 'spinTracks'):
            self.spinTracks.pause()
            del self.spinTracks

    if __dev__:

        def attribChanged(self, *args):
            self.destroyProps()
            self.initProps()