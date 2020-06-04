# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\avatar\AvatarDetail.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.avatar import Avatar

class AvatarDetail:
    __module__ = __name__
    notify = directNotify.newCategory('AvatarDetail')

    def __init__(self, doId, callWhenDone):
        self.id = doId
        self.callWhenDone = callWhenDone
        self.enterQuery()

    def isReady(self):
        return true

    def getId(self):
        return self.id

    def enterQuery(self):
        self.avatar = base.cr.doId2do.get(self.id)
        if self.avatar != None and not self.avatar.ghostMode:
            self.createdAvatar = 0
            dclass = self.getDClass()
            self.__handleResponse(True, self.avatar, dclass)
        else:
            self.avatar = self.createHolder()
            self.createdAvatar = 1
            self.avatar.doId = self.id
            dclass = self.getDClass()
            base.cr.getAvatarDetails(self.avatar, self.__handleResponse, dclass)
        return

    def exitQuery(self):
        return true

    def createHolder(self):
        pass

    def getDClass(self):
        pass

    def __handleResponse(self, gotData, avatar, dclass):
        if avatar != self.avatar:
            self.notify.warning('Ignoring unexpected request for avatar %s' % avatar.doId)
            return
        if gotData:
            self.callWhenDone(self.avatar)
            del self.callWhenDone
        else:
            self.callWhenDone(None)
            del self.callWhenDone
        return