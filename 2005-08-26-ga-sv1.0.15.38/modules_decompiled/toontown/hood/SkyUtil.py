# File: S (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *

def cloudSkyTrack(task):
    task.h += globalClock.getDt() * 0.25
    task.cloud1.setH(task.h)
    task.cloud2.setH(-(task.h) * 0.80000000000000004)
    return Task.cont


def startCloudSky(hood):
    hood.sky.reparentTo(camera)
    hood.sky.setDepthTest(0)
    hood.sky.setDepthWrite(0)
    hood.sky.setBin('background', 100)
    hood.sky.find('**/Sky').reparentTo(hood.sky, -1)
    hood.sky.reparentTo(camera)
    hood.sky.setZ(0.0)
    hood.sky.setHpr(0.0, 0.0, 0.0)
    ce = CompassEffect.make(NodePath(), CompassEffect.PRot | CompassEffect.PZ)
    hood.sky.node().setEffect(ce)
    skyTrackTask = Task.Task(hood.skyTrack)
    skyTrackTask.h = 0
    skyTrackTask.cloud1 = hood.sky.find('**/cloud1')
    skyTrackTask.cloud2 = hood.sky.find('**/cloud2')
    taskMgr.add(skyTrackTask, 'skyTrack')

