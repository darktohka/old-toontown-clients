# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\BulletinBoardWatcher.py
__all__ = [
 'BulletinBoardWatcher']
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.PythonUtil import Functor, makeList
from direct.showbase import DirectObject

class BulletinBoardWatcher(DirectObject.DirectObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('BulletinBoardWatcher')

    def __init__(self, name, postNames, callback, removeNames=None):
        self.notify.debug('__init__: %s, %s, %s' % (name, postNames, callback))
        if removeNames is None:
            removeNames = []
        self.name = name
        self.postNames = makeList(postNames)
        self.removeNames = makeList(removeNames)
        self.callback = callback
        self.waitingOn = set()
        for name in self.postNames:
            if not bboard.has(name):
                eventName = bboard.getEvent(name)
                self.waitingOn.add(eventName)
                self.acceptOnce(eventName, Functor(self._handleEvent, eventName))

        for name in self.removeNames:
            if bboard.has(name):
                eventName = bboard.getRemoveEvent(name)
                self.waitingOn.add(eventName)
                self.acceptOnce(eventName, Functor(self._handleEvent, eventName))

        self._checkDone()
        return

    def destroy(self):
        self.ignoreAll()
        if hasattr(self, 'callback'):
            del self.callback
            del self.waitingOn

    def isDone(self):
        return len(self.waitingOn) == 0

    def _checkDone(self):
        if self.isDone():
            self.notify.debug('%s: done' % self.name)
            self.callback()
            self.destroy()

    def _handleEvent(self, eventName):
        self.notify.debug('%s: handlePost(%s)' % (self.name, eventName))
        self.waitingOn.remove(eventName)
        self._checkDone()