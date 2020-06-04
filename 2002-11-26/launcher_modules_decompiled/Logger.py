# File: L (Python 2.2)

import sys
import time
import math

class Logger:
    
    def __init__(self, fileName = 'log'):
        self._Logger__timeStamp = 1
        self._Logger__startTime = 0.0
        self._Logger__logFile = None
        self._Logger__logFileName = fileName

    
    def setTimeStamp(self, bool):
        self._Logger__timeStamp = bool

    
    def getTimeStamp(self):
        return self._Logger__timeStamp

    
    def resetStartTime(self):
        self._Logger__startTime = time.time()

    
    def log(self, entryString):
        if self._Logger__logFile == None:
            self._Logger__openLogFile()
        
        if self._Logger__timeStamp:
            self._Logger__logFile.write(self._Logger__getTimeStamp())
        
        self._Logger__logFile.write(entryString + '\n')

    
    def _Logger__openLogFile(self):
        self.resetStartTime()
        t = time.localtime(self._Logger__startTime)
        st = time.strftime('%m-%d-%Y-%H-%M-%S', t)
        logFileName = self._Logger__logFileName + '.' + st
        self._Logger__logFile = open(logFileName, 'w')

    
    def _Logger__closeLogFile(self):
        if self._Logger__logFile != None:
            self._Logger__logFile.close()
        

    
    def _Logger__getTimeStamp(self):
        t = time.time()
        dt = t - self._Logger__startTime
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


