# File: T (Python 2.2)

from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.task import Task

class Transitions:
    IrisModelName = 'models/misc/iris'
    FadeModelName = 'models/misc/fade'
    
    def __init__(self, loader):
        self.iris = None
        self.fade = None
        self.fadeColor = Vec3(0)
        self.irisTaskName = 'irisTask'
        self.fadeTaskName = 'fadeTask'

    
    def _Transitions__fadeInLerpDone(self, task):
        self.fade.reparentTo(hidden)
        return Task.done

    
    def fadeIn(self, t = 0.5, block = 0):
        self.noTransitions()
        self.loadFade()
        self.fade.reparentTo(aspect2d, FADE_SORT_INDEX)
        if t == 0:
            self.fade.reparentTo(hidden)
        else:
            r = self.fadeColor[0]
            g = self.fadeColor[1]
            b = self.fadeColor[2]
            task = Task.sequence(self.fade.lerpColor(r, g, b, 1, r, g, b, 0, t), Task.Task(self._Transitions__fadeInLerpDone))
            if not block:
                taskMgr.add(task, self.fadeTaskName)
            else:
                return task

    
    def fadeInTask(self, task, time = 0.5):
        seq = Task.sequence(self.fadeIn(time, block = 1), task)
        taskMgr.add(seq, 'fadeInTaskSeq')

    
    def fadeOut(self, t = 0.5, block = 0):
        self.noTransitions()
        self.loadFade()
        self.fade.reparentTo(aspect2d, FADE_SORT_INDEX)
        r = self.fadeColor[0]
        g = self.fadeColor[1]
        b = self.fadeColor[2]
        if t == 0:
            self.fade.setColor(r, g, b, 1)
        elif not block:
            self.fade.lerpColor(r, g, b, 0, r, g, b, 1, t, task = self.fadeTaskName)
        else:
            return self.fade.lerpColor(r, g, b, 0, r, g, b, 1, t)

    
    def fadeScreen(self, alpha = 0.5):
        self.noTransitions()
        self.loadFade()
        self.fade.reparentTo(aspect2d, FADE_SORT_INDEX)
        self.fade.setColor(self.fadeColor[0], self.fadeColor[1], self.fadeColor[2], alpha)

    
    def fadeScreenColor(self, color):
        self.noTransitions()
        self.loadFade()
        self.fade.reparentTo(aspect2d, FADE_SORT_INDEX)
        self.fade.setColor(color)

    
    def fadeOutTask(self, task, time = 0.29999999999999999, noFade = 1):
        if noFade:
            
            def noFadeTask(task):
                task.noFade()
                return Task.done

            nft = Task.Task(noFadeTask)
            nft.noFade = self.noFade
            seq = Task.sequence(self.fadeOut(time, block = 1), task, nft)
        else:
            seq = Task.sequence(self.fadeOut(time, block = 1), task)
        taskMgr.add(seq, 'fadeOutTaskSeq')

    
    def noFade(self):
        taskMgr.remove(self.fadeTaskName)
        if self.fade != None:
            self.fade.reparentTo(hidden)
        

    
    def setFadeColor(self, r, g, b):
        self.fadeColor.set(r, g, b)

    
    def _Transitions__irisInLerpDone(self, task):
        self.iris.reparentTo(hidden)
        return Task.done

    
    def irisIn(self, t = 0.5, block = 0):
        self.noTransitions()
        self.loadIris()
        if t == 0:
            self.iris.reparentTo(hidden)
        else:
            self.iris.reparentTo(aspect2d, FADE_SORT_INDEX)
            self.iris.setScale(0.014999999999999999)
            task = Task.sequence(self.iris.lerpScale(0.17999999999999999, 0.17999999999999999, 0.17999999999999999, t, blendType = 'noBlend'), Task.Task(self._Transitions__irisInLerpDone))
            if not block:
                taskMgr.add(task, self.irisTaskName)
            else:
                return task

    
    def irisInTask(self, task, time = 0.5):
        seq = Task.sequence(self.irisIn(time, block = 1), task)
        taskMgr.add(seq, 'irisInTaskSeq')

    
    def irisOutLerpDone(self, task):
        self.iris.reparentTo(hidden)
        self.fadeOut(0)
        return Task.done

    
    def irisOut(self, t = 0.5, block = 0):
        self.noTransitions()
        self.loadIris()
        self.loadFade()
        if t == 0:
            self.iris.reparentTo(hidden)
        else:
            self.iris.reparentTo(aspect2d, FADE_SORT_INDEX)
            self.iris.setScale(0.17999999999999999)
            task = Task.sequence(self.iris.lerpScale(0.014999999999999999, 0.014999999999999999, 0.014999999999999999, t, blendType = 'noBlend'), Task.Task(self.irisOutLerpDone))
            if not block:
                taskMgr.add(task, self.irisTaskName)
            else:
                return task

    
    def irisOutTask(self, task, time = 0.5, noIris = 1):
        if noIris:
            
            def noIrisTask(task):
                task.noIris()
                return Task.done

            nit = Task.Task(noIrisTask)
            nit.noIris = self.noIris
            seq = Task.sequence(self.irisOut(time, block = 1), task, nit)
        else:
            seq = Task.sequence(self.irisOut(time, block = 1), task)
        taskMgr.add(seq, 'irisOutTaskSeq')

    
    def noIris(self):
        taskMgr.remove(self.irisTaskName)
        if self.iris != None:
            self.iris.reparentTo(hidden)
        
        self.noFade()

    
    def noTransitions(self):
        self.noFade()
        self.noIris()

    
    def loadIris(self):
        if self.iris == None:
            self.iris = loader.loadModel(self.IrisModelName)
            self.iris.setPos(0, 0, 0)
        

    
    def loadFade(self):
        if self.fade == None:
            fadeModel = loader.loadModel(self.FadeModelName)
            self.fade = DirectFrame(parent = hidden, guiId = 'fade', relief = None, image = fadeModel, image_scale = 3.0, state = NORMAL)
            fadeModel.removeNode()
        


