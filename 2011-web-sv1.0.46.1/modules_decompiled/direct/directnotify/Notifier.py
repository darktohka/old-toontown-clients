# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\directnotify\Notifier.py
from LoggerGlobal import defaultLogger
from direct.showbase import PythonUtil
from libpandaexpress import ConfigVariableBool
import time, types, sys

class Notifier:
    __module__ = __name__
    serverDelta = 0
    streamWriter = None
    showTime = ConfigVariableBool('notify-timestamp', False)

    def __init__(self, name, logger=None):
        self.__name = name
        if logger == None:
            self.__logger = defaultLogger
        else:
            self.__logger = logger
        self.__info = 1
        self.__warning = 1
        self.__debug = 0
        self.__logging = 0
        return

    def setServerDelta(self, delta, timezone):
        delta = int(round(delta))
        Notifier.serverDelta = delta + time.timezone - timezone
        from pandac.PandaModules import NotifyCategory
        NotifyCategory.setServerDelta(self.serverDelta)
        self.info('Notify clock adjusted by %s (and timezone adjusted by %s hours) to synchronize with server.' % (PythonUtil.formatElapsedSeconds(delta), (time.timezone - timezone) / 3600))

    def getTime(self):
        return time.strftime(':%m-%d-%Y %H:%M:%S ', time.localtime(time.time() + self.serverDelta))

    def getOnlyTime(self):
        return time.strftime('%H:%M:%S', time.localtime(time.time() + self.serverDelta))

    def __str__(self):
        return '%s: info = %d, warning = %d, debug = %d, logging = %d' % (self.__name, self.__info, self.__warning, self.__debug, self.__logging)

    def setSeverity(self, severity):
        from pandac.PandaModules import NSDebug, NSInfo, NSWarning, NSError
        if severity >= NSError:
            self.setWarning(0)
            self.setInfo(0)
            self.setDebug(0)
        elif severity == NSWarning:
            self.setWarning(1)
            self.setInfo(0)
            self.setDebug(0)
        elif severity == NSInfo:
            self.setWarning(1)
            self.setInfo(1)
            self.setDebug(0)
        elif severity <= NSDebug:
            self.setWarning(1)
            self.setInfo(1)
            self.setDebug(1)

    def getSeverity(self):
        from pandac.PandaModules import NSDebug, NSInfo, NSWarning, NSError
        if self.getDebug():
            return NSDebug
        elif self.getInfo():
            return NSInfo
        elif self.getWarning():
            return NSWarning
        else:
            return NSError

    def error(self, errorString, exception=StandardError):
        message = str(errorString)
        if Notifier.showTime.getValue():
            string = self.getTime() + str(exception) + ': ' + self.__name + '(error): ' + message
        else:
            string = str(exception) + ': ' + self.__name + '(error): ' + message
        self.__log(string)
        raise exception(errorString)

    def warning(self, warningString):
        if self.__warning:
            message = str(warningString)
            if Notifier.showTime.getValue():
                string = self.getTime() + self.__name + '(warning): ' + message
            else:
                string = ':' + self.__name + '(warning): ' + message
            self.__log(string)
            self.__print(string)
        return 1

    def setWarning(self, bool):
        self.__warning = bool

    def getWarning(self):
        return self.__warning

    def debug(self, debugString):
        if self.__debug:
            message = str(debugString)
            if Notifier.showTime.getValue():
                string = self.getTime() + self.__name + '(debug): ' + message
            else:
                string = ':' + self.__name + '(debug): ' + message
            self.__log(string)
            self.__print(string)
        return 1

    def setDebug(self, bool):
        self.__debug = bool

    def getDebug(self):
        return self.__debug

    def info(self, infoString):
        if self.__info:
            message = str(infoString)
            if Notifier.showTime.getValue():
                string = self.getTime() + self.__name + ': ' + message
            else:
                string = ':' + self.__name + ': ' + message
            self.__log(string)
            self.__print(string)
        return 1

    def getInfo(self):
        return self.__info

    def setInfo(self, bool):
        self.__info = bool

    def __log(self, logEntry):
        if self.__logging:
            self.__logger.log(logEntry)

    def getLogging(self):
        return self.__logging

    def setLogging(self, bool):
        self.__logging = bool

    def __print(self, string):
        if self.streamWriter:
            self.streamWriter.appendData(string + '\n')
        else:
            print >> sys.stderr, string

    def debugStateCall(self, obj=None, fsmMemberName='fsm', secondaryFsm='secondaryFSM'):
        if self.__debug:
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
            string = ':%s:%s [%-7s] id(%s)%s %s' % (self.getOnlyTime(), self.__name, state, id(obj), doId, PythonUtil.traceParentCall())
            self.__log(string)
            self.__print(string)
        return 1

    def debugCall(self, debugString=''):
        if self.__debug:
            message = str(debugString)
            string = ':%s:%s "%s" %s' % (self.getOnlyTime(), self.__name, message, PythonUtil.traceParentCall())
            self.__log(string)
            self.__print(string)
        return 1