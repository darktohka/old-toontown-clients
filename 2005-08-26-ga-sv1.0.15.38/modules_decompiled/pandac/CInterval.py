# File: C (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class CInterval(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts,
        libpandaexpressDowncasts]
    ETReverseFinalize = 6
    ETInitialize = 0
    ETFinalize = 3
    ETReverseInitialize = 4
    ETInterrupt = 7
    ETReverseInstant = 5
    ETInstant = 1
    ETStep = 2
    SPaused = 2
    SInitial = 0
    SStarted = 1
    SFinal = 3
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libdirect._inPSpsCStxv()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getName(self):
        returnValue = libdirect._inPSpsCfV5F(self.this)
        return returnValue

    
    def getDuration(self):
        returnValue = libdirect._inPSpsC8svE(self.this)
        return returnValue

    
    def getOpenEnded(self):
        returnValue = libdirect._inPSpsCB6uv(self.this)
        return returnValue

    
    def getState(self):
        returnValue = libdirect._inPSpsCvfjT(self.this)
        return returnValue

    
    def isStopped(self):
        returnValue = libdirect._inPSpsCs6CA(self.this)
        return returnValue

    
    def setDoneEvent(self, event):
        returnValue = libdirect._inPSpsCso5p(self.this, event)
        return returnValue

    
    def getDoneEvent(self):
        returnValue = libdirect._inPSpsCU1_s(self.this)
        return returnValue

    
    def _CInterval__cSetT(self, t):
        returnValue = libdirect._inPSpsCnHap(self.this, t)
        return returnValue

    
    def getT(self):
        returnValue = libdirect._inPSpsCEMrp(self.this)
        return returnValue

    
    def setAutoPause(self, autoPause):
        returnValue = libdirect._inPSpsCK6Bt(self.this, autoPause)
        return returnValue

    
    def getAutoPause(self):
        returnValue = libdirect._inPSpsCLOK8(self.this)
        return returnValue

    
    def setAutoFinish(self, autoFinish):
        returnValue = libdirect._inPSpsCwEgz(self.this, autoFinish)
        return returnValue

    
    def getAutoFinish(self):
        returnValue = libdirect._inPSpsCK3xj(self.this)
        return returnValue

    
    def setWantsTCallback(self, wantsTCallback):
        returnValue = libdirect._inPSpsCU4Wd(self.this, wantsTCallback)
        return returnValue

    
    def getWantsTCallback(self):
        returnValue = libdirect._inPSpsCzuIb(self.this)
        return returnValue

    
    def setManager(self, manager):
        returnValue = libdirect._inPSpsCVrzY(self.this, manager.this)
        return returnValue

    
    def getManager(self):
        returnValue = libdirect._inPSpsCzijv(self.this)
        import CIntervalManager
        returnObject = CIntervalManager.CIntervalManager(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _CInterval__overloaded_start_ptrCInterval_double_double_double(self, startT, endT, playRate):
        returnValue = libdirect._inPSpsCOA1D(self.this, startT, endT, playRate)
        return returnValue

    
    def _CInterval__overloaded_start_ptrCInterval_double_double(self, startT, endT):
        returnValue = libdirect._inPSpsCsz84(self.this, startT, endT)
        return returnValue

    
    def _CInterval__overloaded_start_ptrCInterval_double(self, startT):
        returnValue = libdirect._inPSpsCV_pK(self.this, startT)
        return returnValue

    
    def _CInterval__overloaded_start_ptrCInterval(self):
        returnValue = libdirect._inPSpsCI9Ch(self.this)
        return returnValue

    
    def _CInterval__overloaded_loop_ptrCInterval_double_double_double(self, startT, endT, playRate):
        returnValue = libdirect._inPSpsClvuV(self.this, startT, endT, playRate)
        return returnValue

    
    def _CInterval__overloaded_loop_ptrCInterval_double_double(self, startT, endT):
        returnValue = libdirect._inPSpsCN0b7(self.this, startT, endT)
        return returnValue

    
    def _CInterval__overloaded_loop_ptrCInterval_double(self, startT):
        returnValue = libdirect._inPSpsCDdAk(self.this, startT)
        return returnValue

    
    def _CInterval__overloaded_loop_ptrCInterval(self):
        returnValue = libdirect._inPSpsCdHuO(self.this)
        return returnValue

    
    def pause(self):
        returnValue = libdirect._inPSpsCYZXB(self.this)
        return returnValue

    
    def _CInterval__overloaded_resume_ptrCInterval(self):
        returnValue = libdirect._inPSpsCOoeF(self.this)
        return returnValue

    
    def _CInterval__overloaded_resume_ptrCInterval_double(self, startT):
        returnValue = libdirect._inPSpsCC2L6(self.this, startT)
        return returnValue

    
    def resumeUntil(self, endT):
        returnValue = libdirect._inPSpsCYMh8(self.this, endT)
        return returnValue

    
    def finish(self):
        returnValue = libdirect._inPSpsCIWoe(self.this)
        return returnValue

    
    def isPlaying(self):
        returnValue = libdirect._inPSpsCLlcY(self.this)
        return returnValue

    
    def privDoEvent(self, t, event):
        returnValue = libdirect._inPSpsCsrd8(self.this, t, event)
        return returnValue

    
    def privInitialize(self, t):
        returnValue = libdirect._inPSpsCADw2(self.this, t)
        return returnValue

    
    def privInstant(self):
        returnValue = libdirect._inPSpsC_B_n(self.this)
        return returnValue

    
    def privStep(self, t):
        returnValue = libdirect._inPSpsCU3CU(self.this, t)
        return returnValue

    
    def privFinalize(self):
        returnValue = libdirect._inPSpsCcdRd(self.this)
        return returnValue

    
    def privReverseInitialize(self, t):
        returnValue = libdirect._inPSpsCzQVo(self.this, t)
        return returnValue

    
    def privReverseInstant(self):
        returnValue = libdirect._inPSpsCyAlT(self.this)
        return returnValue

    
    def privReverseFinalize(self):
        returnValue = libdirect._inPSpsCtoBu(self.this)
        return returnValue

    
    def privInterrupt(self):
        returnValue = libdirect._inPSpsCpKBe(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libdirect._inPSpsC6w_D(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libdirect._inPSpsCLeD7(self.this, out.this, indentLevel)
        return returnValue

    
    def setupPlay(self, startTime, endTime, playRate, doLoop):
        returnValue = libdirect._inPSpsCzgQa(self.this, startTime, endTime, playRate, doLoop)
        return returnValue

    
    def setupResume(self):
        returnValue = libdirect._inPSpsCUryc(self.this)
        return returnValue

    
    def setupResumeUntil(self, endT):
        returnValue = libdirect._inPSpsCscch(self.this, endT)
        return returnValue

    
    def stepPlay(self):
        returnValue = libdirect._inPSpsCNGqy(self.this)
        return returnValue

    
    def start(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CInterval__overloaded_start_ptrCInterval(*_args)
        elif numArgs == 1:
            return self._CInterval__overloaded_start_ptrCInterval_double(*_args)
        elif numArgs == 2:
            return self._CInterval__overloaded_start_ptrCInterval_double_double(*_args)
        elif numArgs == 3:
            return self._CInterval__overloaded_start_ptrCInterval_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '

    
    def loop(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CInterval__overloaded_loop_ptrCInterval(*_args)
        elif numArgs == 1:
            return self._CInterval__overloaded_loop_ptrCInterval_double(*_args)
        elif numArgs == 2:
            return self._CInterval__overloaded_loop_ptrCInterval_double_double(*_args)
        elif numArgs == 3:
            return self._CInterval__overloaded_loop_ptrCInterval_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '

    
    def resume(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CInterval__overloaded_resume_ptrCInterval(*_args)
        elif numArgs == 1:
            return self._CInterval__overloaded_resume_ptrCInterval_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    from direct.directnotify.DirectNotifyGlobal import directNotify
    notify = directNotify.newCategory('Interval')
    
    def setT(self, t):
        self._CInterval__cSetT(t)
        self.privPostEvent()

    
    def play(self, t0 = 0.0, duration = None, scale = 1.0):
        self.notify.error('using deprecated CInterval.play() interface')
        if duration:
            self.start(t0, t0 + duration, scale)
        else:
            self.start(t0, -1, scale)

    
    def stop(self):
        self.notify.error('using deprecated CInterval.stop() interface')
        self.finish()

    
    def setFinalT(self):
        self.notify.error('using deprecated CInterval.setFinalT() interface')
        self.finish()

    
    def privPostEvent(self):
        t = self.getT()
        if hasattr(self, 'setTHooks'):
            for func in self.setTHooks:
                func(t)
            
        

    
    def popupControls(self, tl = None):
        Toplevel = Toplevel
        Frame = Frame
        Button = Button
        LEFT = LEFT
        X = X
        Pmw = Pmw
        import direct.showbase.TkGlobal
        import math
        EntryScale = EntryScale
        import direct.tkwidgets
        if tl == None:
            tl = Toplevel()
            tl.title('Interval Controls')
        
        outerFrame = Frame(tl)
        
        def entryScaleCommand(t, s = self):
            s.setT(t)
            s.pause()

        self.es = EntryScale.EntryScale(outerFrame, text = self.getName(), min = 0, max = math.floor(self.getDuration() * 100) / 100, command = entryScaleCommand)
        es = EntryScale.EntryScale(outerFrame, text = self.getName(), min = 0, max = math.floor(self.getDuration() * 100) / 100, command = entryScaleCommand)
        es.set(self.getT(), fCommand = 0)
        es.pack(expand = 1, fill = X)
        bf = Frame(outerFrame)
        
        def toStart(s = self, es = es):
            s.setT(0.0)
            s.pause()

        
        def toEnd(s = self):
            s.setT(s.getDuration())
            s.pause()

        jumpToStart = Button(bf, text = '<<', command = toStart)
        
        def doPlay(s = self, es = es):
            s.resume(es.get())

        stop = Button(bf, text = 'Stop', command = lambda s = self: s.pause())
        play = Button(bf, text = 'Play', command = doPlay)
        jumpToEnd = Button(bf, text = '>>', command = toEnd)
        jumpToStart.pack(side = LEFT, expand = 1, fill = X)
        play.pack(side = LEFT, expand = 1, fill = X)
        stop.pack(side = LEFT, expand = 1, fill = X)
        jumpToEnd.pack(side = LEFT, expand = 1, fill = X)
        bf.pack(expand = 1, fill = X)
        outerFrame.pack(expand = 1, fill = X)
        
        def update(t, es = es):
            es.set(t, fCommand = 0)

        if not hasattr(self, 'setTHooks'):
            self.setTHooks = []
        
        self.setTHooks.append(update)
        self.setWantsTCallback(1)
        
        def onDestroy(e, s = self, u = update):
            if u in s.setTHooks:
                s.setTHooks.remove(u)
            

        tl.bind('<Destroy>', onDestroy)


