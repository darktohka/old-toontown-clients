# File: I (Python 2.2)

from pandac.PandaModules import *
from direct.showbase.ShowBaseGlobal import *
from IntervalGlobal import *
from direct.actor.Actor import *
from direct.directutil import Mopath
boat = loader.loadModel('models/misc/smiley')
boat.reparentTo(render)
donald = Actor()
donald.loadModel('phase_6/models/char/donald-wheel-1000')
donald.loadAnims({
    'steer': 'phase_6/models/char/donald-wheel-wheel' })
donald.reparentTo(boat)
dock = loader.loadModel('models/misc/smiley')
dock.reparentTo(render)
sound = loader.loadSfx('phase_6/audio/sfx/SZ_DD_waterlap.mp3')
foghorn = loader.loadSfx('phase_6/audio/sfx/SZ_DD_foghorn.mp3')
mp = Mopath.Mopath()
mp.loadFile(Filename('phase_6/paths/dd-e-w'))
boatMopath = MopathInterval(mp, boat, 'boatpath')
boatTrack = Track([
    boatMopath], 'boattrack')
BOAT_START = boatTrack.getIntervalStartTime('boatpath')
BOAT_END = boatTrack.getIntervalEndTime('boatpath')
donaldSteerInterval = ActorInterval(donald, 'steer')
donaldLoopInterval = ActorInterval(donald, 'steer', loop = 1, duration = 10.0)
donaldSteerTrack = Track([
    donaldSteerInterval,
    donaldLoopInterval], name = 'steerTrack')
dockLerp = LerpPosHprInterval(dock, 5.0, pos = Point3(0, 0, -5), hpr = Vec3(0, 0, 0), name = 'dock-lerp')
dockPos = PosHprInterval(dock, dock.getPos(), dock.getHpr(), 1.0, 'dockpos')
dockUpTime = BOAT_END - dockLerp.getDuration()
hpr2 = Vec3(90.0, 90.0, 90.0)
dockLerp2 = LerpHprInterval(dock, 3.0, hpr2, name = 'hpr-lerp')
dockTrack = Track([
    dockLerp2,
    dockPos,
    dockLerp], 'docktrack')
dockTrack.setIntervalStartTime('dock-lerp', dockUpTime)
dockTrack.setIntervalStartTime('hpr-lerp', BOAT_START)
waterStartTime = BOAT_START + 5.0
waterSound = SoundInterval(sound, name = 'watersound')
soundTrack = Track([
    waterSound], 'soundtrack')
soundTrack.setIntervalStartTime('watersound', waterStartTime)
eventTime = soundTrack.getIntervalEndTime('watersound')
waterDone = EventInterval('water-is-done')
waterEventTrack = Track([
    waterDone])
waterEventTrack.setIntervalStartTime('water-is-done', eventTime)

def handleWaterDone():
    print 'water is done'

messenger.accept('water-is-done', waterDone, handleWaterDone)
foghornStartTime = BOAT_START + 4.0
foghornSound = SoundInterval(foghorn, name = 'foghorn')
soundTrack2 = Track([
    (foghornStartTime, foghornSound)], 'soundtrack2')
mtrack = MultiTrack([
    boatTrack,
    dockTrack,
    soundTrack,
    soundTrack2,
    waterEventTrack,
    donaldSteerTrack])
print mtrack
i1 = FunctionInterval(lambda : base.transitions.fadeOut())
i2 = FunctionInterval(lambda : base.transitions.fadeIn())

def caughtIt():
    print 'Caught here-is-an-event'


class DummyAcceptor(DirectObject):
    pass

da = DummyAcceptor()
i3 = AcceptInterval(da, 'here-is-an-event', caughtIt)
i4 = EventInterval('here-is-an-event')
i5 = IgnoreInterval(da, 'here-is-an-event')

def printDone():
    print 'done'

i6 = FunctionInterval(printDone)
t1 = Track([
    (0.0, i1),
    (2.0, i2),
    (4.0, i3),
    (5.0, i4),
    (6.0, i5),
    (7.0, i4),
    (8.0, i6)], name = 'demo')
print t1
startTime = 0.0

def printStart():
    global startTime
    startTime = globalClock.getFrameTime()
    print 'Start'


def printPreviousStart():
    currTime = globalClock.getFrameTime()
    print 'PREVIOUS_END %0.2f' % (currTime - startTime)


def printPreviousEnd():
    currTime = globalClock.getFrameTime()
    print 'PREVIOUS_END %0.2f' % (currTime - startTime)


def printTrackStart():
    currTime = globalClock.getFrameTime()
    print 'TRACK_START %0.2f' % (currTime - startTime)


def printArguments(a, b, c):
    print 'My args were %d, %d, %d' % (a, b, c)

i1 = FunctionInterval(printStart)
i2 = LerpPosInterval(camera, 2.0, Point3(0, 10, 5))
i3 = FunctionInterval(printPreviousEnd)
i4 = LerpPosInterval(camera, 2.0, Point3(0, 0, 5))
i5 = FunctionInterval(printPreviousStart)
i6 = FunctionInterval(printTrackStart)
i7 = FunctionInterval(printArguments, extraArgs = [
    1,
    10,
    100])
t2 = Track([
    (0.0, i1),
    (1.0, i2, TRACK_START),
    (2.0, i3, PREVIOUS_END),
    (1.0, i4, PREVIOUS_END),
    (3.0, i5, PREVIOUS_START),
    (10.0, i6, TRACK_START),
    (12.0, i7)], name = 'startTimeDemo')
print t2

def test(n):
    lerps = []
    for i in range(n):
        lerps.append(LerpPosHprInterval(dock, 5.0, pos = Point3(0, 0, -5), hpr = Vec3(0, 0, 0), startPos = dock.getPos(), startHpr = dock.getHpr(), name = 'dock-lerp'))
        lerps.append(EventInterval('joe'))
    
    t = Track(lerps)
    mt = MultiTrack([
        t])

