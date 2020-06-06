# File: M (Python 2.2)

import LerpInterval
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *

class MopathInterval(LerpInterval.LerpFunctionInterval):
    mopathNum = 1
    notify = directNotify.newCategory('MopathInterval')
    
    def __init__(self, mopath, node, fromT = 0, toT = None, blendType = 'noBlend', name = None):
        if toT == None:
            toT = mopath.getMaxT()
        
        if name == None:
            name = 'Mopath-%d' % MopathInterval.mopathNum
            MopathInterval.mopathNum += 1
        
        LerpInterval.LerpFunctionInterval.__init__(self, self._MopathInterval__doMopath, fromData = fromT, toData = toT, duration = abs(toT - fromT), blendType = blendType, name = name)
        self.mopath = mopath
        self.node = node

    
    def _MopathInterval__doMopath(self, t):
        self.mopath.goTo(self.node, t)


