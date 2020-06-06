# File: M (Python 2.2)

import Interval
from PandaModules import *
from DirectNotifyGlobal import *

class MopathInterval(Interval.Interval):
    mopathNum = 1
    notify = directNotify.newCategory('MopathInterval')
    
    def __init__(self, mopath, node, name = None):
        self.mopath = mopath
        self.node = node
        if name == None:
            name = 'Mopath-%d' % MopathInterval.mopathNum
            MopathInterval.mopathNum += 1
        
        duration = self.mopath.getMaxT()
        Interval.Interval.__init__(self, name, duration)

    
    def privStep(self, t):
        self.mopath.goTo(self.node, t)
        self.state = CInterval.SStarted
        self.currT = t


