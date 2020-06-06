# File: N (Python 2.2)

from LoggerGlobal import *
from direct.showbase import PythonUtil
import time
import types

class Notifier:
    serverDelta = 0
    
    def __init__(self, name, logger = None):
        self._Notifier__name = name
        if logger == None:
            self._Notifier__logger = defaultLogger
        else:
            self._Notifier__logger = logger
        self._Notifier__info = 1
        self._Notifier__warning = 1
        self._Notifier__debug = 0
        self._Notifier__logging = 0

    
    def setServerDelta(self, delta, timezone):
        delta = int(round(delta))
        Notifier.serverDelta = delta + time.timezone - timezone
        NotifyCategory = NotifyCategory
        import pandac
        NotifyCategory.NotifyCategory.setServerDelta(self.serverDelta)
        self.info('Notify clock adjusted by %s (and timezone adjusted by %s hours) to synchronize with server.' % (PythonUtil.formatElapsedSeconds(delta), (time.timezone - timezone) / 3600))

    
    def getTime(self):
        return time.strftime(':%m-%d-%Y %H:%M:%S ', time.localtime(time.time() + self.serverDelta))

    
    def getOnlyTime(self):
        return time.strftime('%H:%M:%S', time.localtime(time.time() + self.serverDelta))

    
    def __str__(self):
        return '%s: info = %d, warning = %d, debug = %d, logging = %d' % (self._Notifier__name, self._Notifier__info, self._Notifier__warning, self._Notifier__debug, self._Notifier__logging)

    
    def setSeverity(self, severity):
        NotifySeverity = NotifySeverity
        import pandac
        if severity >= NotifySeverity.NSError:
            self.setWarning(0)
            self.setInfo(0)
            self.setDebug(0)
        elif severity == NotifySeverity.NSWarning:
            self.setWarning(1)
            self.setInfo(0)
            self.setDebug(0)
        elif severity == NotifySeverity.NSInfo:
            self.setWarning(1)
            self.setInfo(1)
            self.setDebug(0)
        elif severity <= NotifySeverity.NSDebug:
            self.setWarning(1)
            self.setInfo(1)
            self.setDebug(1)
        

    
    def getSeverity(self):
        NotifySeverity = NotifySeverity
        import pandac
        if self.getDebug():
            return NotifySeverity.NSDebug
        elif self.getInfo():
            return NotifySeverity.NSInfo
        elif self.getWarning():
            return NotifySeverity.NSWarning
        else:
            return NotifySeverity.NSError

    
    def error(self, errorString, exception = StandardError):
        string = self.getTime() + str(exception) + ': ' + self._Notifier__name + ': ' + errorString
        self._Notifier__log(string)
        raise exception(errorString)

    
    def warning(self, warningString):
        if self._Notifier__warning:
            string = self.getTime() + self._Notifier__name + '(warning): ' + warningString
            self._Notifier__log(string)
            self._Notifier__print(string)
        
        return 1

    
    def setWarning(self, bool):
        self._Notifier__warning = bool

    
    def getWarning(self):
        return self._Notifier__warning

    
    def debug(self, debugString):
        if self._Notifier__debug:
            string = self.getTime() + self._Notifier__name + '(debug): ' + debugString
            self._Notifier__log(string)
            self._Notifier__print(string)
        
        return 1

    
    def setDebug(self, bool):
        self._Notifier__debug = bool

    
    def getDebug(self):
        return self._Notifier__debug

    
    def info(self, infoString):
        if self._Notifier__info:
            string = self.getTime() + self._Notifier__name + '(info): ' + infoString
            self._Notifier__log(string)
            self._Notifier__print(string)
        
        return 1

    
    def getInfo(self):
        return self._Notifier__info

    
    def setInfo(self, bool):
        self._Notifier__info = bool

    
    def _Notifier__log(self, logEntry):
        if self._Notifier__logging:
            self._Notifier__logger.log(logEntry)
        

    
    def getLogging(self):
        return self._Notifier__logging

    
    def setLogging(self, bool):
        self._Notifier__logging = bool

    
    def _Notifier__print(self, string):
        print string

    
    def debugStateCall(self, obj = None, fsmMemberName = 'fsm', secondaryFsm = 'secondaryFSM'):
        if self._Notifier__debug:
            state = ''
            doId = ''
            if obj is not None:
                fsm = obj.__dict__.get(fsmMemberName)
                if fsm is not None:
                    stateObj = fsm.getCurrentState()
                    if stateObj is not None:
                        state = stateObj.getName()
                    
                
                fsm = obj.__dict__.get(secondaryFsm)
                if fsm is not None:
                    stateObj = fsm.getCurrentState()
                    if stateObj is not None:
                        state = '%s, %s' % (state, stateObj.getName())
                    
                
                if hasattr(obj, 'doId'):
                    doId = ' doId:%s' % (obj.doId,)
                
            
            if 1 or type(obj) == types.ClassType:
                name = '%s.' % (obj.__class__.__name__,)
            else:
                name = '%s ' % (self._Notifier__name,)
            string = ':%s [%-7s]%s %s %s%s' % (self.getOnlyTime(), state, doId, id(obj), name, PythonUtil.traceParentCall())
            self._Notifier__log(string)
            self._Notifier__print(string)
        
        return 1

    
    def debugCall(self, debugString = ''):
        if self._Notifier__debug:
            string = ':%s %s %s.%s' % (self.getOnlyTime(), debugString, self._Notifier__name, PythonUtil.traceParentCall())
            self._Notifier__log(string)
            self._Notifier__print(string)
        
        return 1


