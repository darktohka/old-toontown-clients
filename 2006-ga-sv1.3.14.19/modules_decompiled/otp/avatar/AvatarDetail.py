# File: A (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from otp.avatar import Avatar

class AvatarDetail:
    notify = DirectNotifyGlobal.directNotify.newCategory('AvatarDetail')
    notify.setDebug(True)
    
    def __init__(self, doId, callWhenDone):
        print 'Getting avatar detail for %s from the DB' % doId
        self.id = doId
        self.callWhenDone = callWhenDone
        self.enterQuery()

    
    def isReady(self):
        return true

    
    def getId(self):
        return self.id

    
    def enterQuery(self):
        self.avatar = base.cr.doId2do.get(self.id)
        if self.avatar != None and not (self.avatar.ghostMode):
            self.createdAvatar = 0
            self._AvatarDetail__handleResponse(True, self.avatar)
        else:
            self.avatar = self.createHolder()
            self.createdAvatar = 1
            self.avatar.doId = self.id
            base.cr.getAvatarDetails(self.avatar, self._AvatarDetail__handleResponse)

    
    def exitQuery(self):
        return true

    
    def createHolder(self):
        pass

    
    def _AvatarDetail__handleResponse(self, gotData, avatar):
        if avatar != self.avatar:
            self.notify.warning('Ignoring unexpected request for avatar %s' % avatar.doId)
            return None
        
        if gotData:
            self.callWhenDone(self.avatar)
            del self.callWhenDone
        else:
            self.callWhenDone(None)
            del self.callWhenDone


