# File: M (Python 2.2)

from IntervalGlobal import *
import MovieCamera
import DirectNotifyGlobal
import Localizer
notify = DirectNotifyGlobal.directNotify.newCategory('MovieSOS')

def doSOSs(calls):
    if len(calls) == 0:
        return (None, None)
    
    
    def callerFunc(toon, handle):
        toon.setChatAbsolute(Localizer.MovieSOSCallHelp % handle.getName(), CFSpeech | CFTimeout)
        handle.d_battleSOS(toonbase.localToon.doId)

    
    def calleeFunc(toon, handle):
        toon.setChatAbsolute(Localizer.MovieSOSCallHelp % handle.getName(), CFSpeech | CFTimeout)

    
    def observerFunc(toon):
        toon.setChatAbsolute(Localizer.MovieSOSObserverHelp, CFSpeech | CFTimeout)

    mtrack = Sequence()
    for c in calls:
        toon = c['toon']
        targetType = c['targetType']
        handle = c['target']
        mtrack.append(Wait(0.5))
        if targetType == 'observer':
            ival = Func(observerFunc, toon)
        elif targetType == 'caller':
            ival = Func(callerFunc, toon, handle)
        elif targetType == 'callee':
            ival = Func(calleeFunc, toon, handle)
        else:
            notify.error('ivalid target type: %s' % targetType)
        mtrack.append(ival)
        mtrack.append(Wait(2.0))
        notify.debug('toon: %s calls for help' % toon.getName())
    
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseSOSShot(toon, camDuration)
    return (mtrack, camTrack)

