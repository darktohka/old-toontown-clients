# File: S (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.showbase.DirectObject import DirectObject

class SCObject(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('SpeedChat')
    
    def __init__(self):
        self.settingsRef = None
        self._SCObject__visible = 0
        self._SCObject__dirty = 1

    
    def destroy(self):
        self.ignoreAll()
        if self.isVisible():
            self.exitVisible()
        

    
    def enterVisible(self):
        self._SCObject__visible = 1

    
    def exitVisible(self):
        self._SCObject__visible = 0

    
    def isVisible(self):
        return self._SCObject__visible

    
    def invalidate(self):
        self._SCObject__dirty = 1

    
    def isDirty(self):
        return self._SCObject__dirty

    
    def validate(self):
        self._SCObject__dirty = 0

    
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

    
    def privSetSettingsRef(self, settingsRef):
        self.settingsRef = settingsRef

    
    def privAdoptSCObject(self, scObj):
        scObj.privSetSettingsRef(self.settingsRef)

    
    def invalidateAll(self):
        self.invalidate()

    
    def finalizeAll(self):
        self.finalize()


