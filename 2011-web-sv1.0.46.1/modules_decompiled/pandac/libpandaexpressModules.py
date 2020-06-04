# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\built\lib\pandac\libpandaexpressModules.py
from extension_native_helpers import *
Dtool_PreloadDLL('libpandaexpress')
from libpandaexpress import *
from extension_native_helpers import *
Dtool_PreloadDLL('libpandaexpress')
from libpandaexpress import *

def readlines(self):
    lines = []
    line = self.readline()
    while line:
        lines.append(line)
        line = self.readline()

    return lines


Dtool_funcToMethod(readlines, Ramfile)
del readlines
from extension_native_helpers import *
Dtool_PreloadDLL('libpandaexpress')
from libpandaexpress import *

def readlines(self):
    lines = []
    line = self.readline()
    while line:
        lines.append(line)
        line = self.readline()

    return lines


Dtool_funcToMethod(readlines, StreamReader)
del readlines
from extension_native_helpers import *
Dtool_PreloadDLL('libpandaexpress')
from libpandaexpress import *

def spawnTask(self, name=None, callback=None, extraArgs=[]):
    if not name:
        name = self.getUrl().cStr()
    from direct.task import Task
    task = Task.Task(self.doTask)
    task.callback = callback
    task.callbackArgs = extraArgs
    return taskMgr.add(task, name)


Dtool_funcToMethod(spawnTask, HTTPChannel)
del spawnTask

def doTask(self, task):
    from direct.task import Task
    if self.run():
        return Task.cont
    if task.callback:
        task.callback(*task.callbackArgs)
    return Task.done


Dtool_funcToMethod(doTask, HTTPChannel)
del doTask