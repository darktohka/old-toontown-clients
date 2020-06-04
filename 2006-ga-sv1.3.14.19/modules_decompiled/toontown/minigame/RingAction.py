# File: R (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
import RingTrack

class RingAction:
    notify = DirectNotifyGlobal.directNotify.newCategory('RingAction')
    
    def __init__(self):
        pass

    
    def eval(self, t):
        return (0, 0)



class RingActionStaticPos(RingAction):
    
    def __init__(self, pos):
        RingAction.__init__(self)
        self._RingActionStaticPos__pos = pos

    
    def eval(self, t):
        return self._RingActionStaticPos__pos



class RingActionFunction(RingAction):
    
    def __init__(self, func, args):
        RingAction.__init__(self)
        self._RingActionFunction__func = func
        self._RingActionFunction__args = args

    
    def eval(self, t):
        return self._RingActionFunction__func(t, *self._RingActionFunction__args)



class RingActionRingTrack(RingAction):
    
    def __init__(self, ringTrack):
        RingAction.__init__(self)
        self._RingActionRingTrack__track = ringTrack

    
    def eval(self, t):
        return self._RingActionRingTrack__track.eval(t)


