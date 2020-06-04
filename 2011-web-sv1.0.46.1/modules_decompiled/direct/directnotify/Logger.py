# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\directnotify\Logger.py
import sys, time, math

class Logger:
    __module__ = __name__

    def __init__(self, fileName='log'):
        self.__timeStamp = 1
        self.__startTime = 0.0
        self.__logFile = None
        self.__logFileName = fileName
        return

    def setTimeStamp(self, bool):
        self.__timeStamp = bool

    def getTimeStamp(self):
        return self.__timeStamp

    def resetStartTime(self):
        self.__startTime = time.time()

    def log(self, entryString):
        if self.__logFile == None:
            self.__openLogFile()
        if self.__timeStamp:
            self.__logFile.write(self.__getTimeStamp())
        self.__logFile.write(entryString + '\n')
        return

    def __openLogFile(self):
        self.resetStartTime()
        t = time.localtime(self.__startTime)
        st = time.strftime('%m-%d-%Y-%H-%M-%S', t)
        logFileName = self.__logFileName + '.' + st
        self.__logFile = open(logFileName, 'w')

    def __closeLogFile(self):
        if self.__logFile != None:
            self.__logFile.close()
        return

    def __getTimeStamp(self):
        t = time.time()
        dt = t - self.__startTime
        if dt >= 86400:
            days = int(math.floor(dt / 86400))
            dt = dt % 86400
        else:
            days = 0
        if dt >= 3600:
            hours = int(math.floor(dt / 3600))
            dt = dt % 3600
        else:
            hours = 0
        if dt >= 60:
            minutes = int(math.floor(dt / 60))
            dt = dt % 60
        else:
            minutes = 0
        seconds = int(math.ceil(dt))
        return '%02d:%02d:%02d:%02d: ' % (days, hours, minutes, seconds)