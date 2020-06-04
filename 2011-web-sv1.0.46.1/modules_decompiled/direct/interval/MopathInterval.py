# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\interval\MopathInterval.py
__all__ = [
 'MopathInterval']
import LerpInterval
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *

class MopathInterval(LerpInterval.LerpFunctionInterval):
    __module__ = __name__
    mopathNum = 1
    notify = directNotify.newCategory('MopathInterval')

    def __init__(self, mopath, node, fromT=0, toT=None, duration=None, blendType='noBlend', name=None):
        if toT == None:
            toT = mopath.getMaxT()
        if duration == None:
            duration = abs(toT - fromT)
        if name == None:
            name = 'Mopath-%d' % MopathInterval.mopathNum
            MopathInterval.mopathNum += 1
        LerpInterval.LerpFunctionInterval.__init__(self, self.__doMopath, fromData=fromT, toData=toT, duration=duration, blendType=blendType, name=name)
        self.mopath = mopath
        self.node = node
        return

    def destroy(self):
        self.function = None
        return

    def __doMopath(self, t):
        self.mopath.goTo(self.node, t)