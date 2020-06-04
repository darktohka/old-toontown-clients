# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\uberdog\OtpAvatarManager.py
from cPickle import loads, dumps
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
notify = DirectNotifyGlobal.directNotify.newCategory('AvatarManager')

class OtpAvatarManager(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = notify
    OnlineEvent = 'GlobalAvatarManagerOnline'

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.avatars = {}

    def delete(self):
        self.ignoreAll()
        self.cr.avatarManager = None
        DistributedObject.DistributedObject.delete(self)
        return

    def online(self):
        messenger.send(OtpAvatarManager.OnlineEvent)

    def sendRequestAvatarList(self):
        self.sendUpdate('requestAvatarList', [0])

    def rejectAvatarList(self, result):
        messenger.send('avatarListFailed', [result])

    def avatarListResponse(self, pickleData):
        avatars = loads(pickleData)
        messenger.send('avatarList', [avatars])

    def rejectCreateAvatar(self, result):
        messenger.send('createdNewAvatarFailed', [result])

    def createAvatarResponse(self, avatarId, subId, access, founder):
        self.notify.info('new avatarId: %s subId: %s access: %s founder: %s' % (avatarId, subId, access, founder))
        messenger.send('createdNewAvatar', [avatarId, subId])

    def sendRequestRemoveAvatar(self, avatarId, subId, confirmPassword):
        self.sendUpdate('requestRemoveAvatar', [0, avatarId, subId, confirmPassword])

    def rejectRemoveAvatar(self, reasonId):
        messenger.send('rejectRemoveAvatar', [reasonId])

    def removeAvatarResponse(self, avatarId, subId):
        messenger.send('removeAvatarResponse', [avatarId, subId])

    def sendRequestShareAvatar(self, avatarId, subId, shared):
        self.sendUpdate('requestShareAvatar', [0, avatarId, subId, shared])

    def rejectShareAvatar(self, reasonId):
        messenger.send('rejectShareAvatar', [reasonId])

    def shareAvatarResponse(self, avatarId, subId, shared):
        messenger.send('shareAvatarResponse', [avatarId, subId, shared])

    def sendRequestAvatarSlot(self, subId, slot):
        self.sendUpdate('requestAvatarSlot', [0, subId, slot])

    def rejectAvatarSlot(self, reasonId, subId, slot):
        messenger.send('rejectAvatarSlot', [reasonId, subId, slot])

    def avatarSlotResponse(self, subId, slot):
        messenger.send('avatarSlotResponse', [subId, slot])

    def sendRequestPlayAvatar(self, avatarId, subId):
        self.sendUpdate('requestPlayAvatar', [0, avatarId, subId])

    def rejectPlayAvatar(self, reasonId, avatarId):
        messenger.send('rejectPlayAvatar', [reasonId, avatarId])

    def playAvatarResponse(self, avatarId, subId, access, founder):
        messenger.send('playAvatarResponse', [avatarId, subId, access, founder])