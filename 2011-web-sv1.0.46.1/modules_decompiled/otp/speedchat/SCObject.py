# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\speedchat\SCObject.py
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.DirectObject import DirectObject

class SCObject(DirectObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('SpeedChat')

    def __init__(self):
        self.settingsRef = None
        self.__visible = 0
        self.__dirty = 1
        return

    def destroy(self):
        self.ignoreAll()
        if self.isVisible():
            self.exitVisible()

    def enterVisible(self):
        self.__visible = 1

    def exitVisible(self):
        self.__visible = 0

    def isVisible(self):
        return self.__visible

    def invalidate(self):
        self.__dirty = 1

    def isDirty(self):
        return self.__dirty

    def validate(self):
        self.__dirty = 0

    def finalize(self):
        pass

    def getEventName(self, name):
        return '%s%s' % (self.settingsRef.eventPrefix, name)

    def getColorScheme(self):
        return self.settingsRef.colorScheme

    def isWhispering(self):
        return self.settingsRef.whisperMode

    def getSubmenuOverlap(self):
        return self.settingsRef.submenuOverlap

    def getTopLevelOverlap(self):
        if self.settingsRef.topLevelOverlap is None:
            return self.getSubmenuOverlap()
        else:
            return self.settingsRef.topLevelOverlap
        return

    def privSetSettingsRef(self, settingsRef):
        self.settingsRef = settingsRef

    def privAdoptSCObject(self, scObj):
        scObj.privSetSettingsRef(self.settingsRef)

    def invalidateAll(self):
        self.invalidate()

    def finalizeAll(self):
        self.finalize()