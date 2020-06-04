# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\BulletinBoard.py
__all__ = [
 'BulletinBoard']
from direct.directnotify import DirectNotifyGlobal

class BulletinBoard:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('BulletinBoard')

    def __init__(self):
        self._dict = {}

    def get(self, postName, default=None):
        return self._dict.get(postName, default)

    def has(self, postName):
        return postName in self._dict

    def getEvent(self, postName):
        return 'bboard-%s' % postName

    def getRemoveEvent(self, postName):
        return 'bboard-remove-%s' % postName

    def post(self, postName, value=None):
        if postName in self._dict:
            BulletinBoard.notify.warning('changing %s from %s to %s' % (postName, self._dict[postName], value))
        self.update(postName, value)

    def update(self, postName, value):
        if postName in self._dict:
            BulletinBoard.notify.info('update: posting %s' % postName)
        self._dict[postName] = value
        messenger.send(self.getEvent(postName))

    def remove(self, postName):
        if postName in self._dict:
            del self._dict[postName]
            messenger.send(self.getRemoveEvent(postName))

    def removeIfEqual(self, postName, value):
        if self.has(postName):
            if self.get(postName) == value:
                self.remove(postName)

    def __repr__(self):
        str = 'Bulletin Board Contents\n'
        str += '======================='
        keys = self._dict.keys()
        keys.sort()
        for postName in keys:
            str += '\n%s: %s' % (postName, self._dict[postName])

        return str