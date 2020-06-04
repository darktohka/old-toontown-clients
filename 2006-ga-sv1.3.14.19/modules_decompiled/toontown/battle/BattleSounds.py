# File: B (Python 2.2)

from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
import os

class BattleSounds:
    notify = DirectNotifyGlobal.directNotify.newCategory('BattleSounds')
    
    def __init__(self):
        self.mgr = AudioManager.createAudioManager()
        self.isValid = 0
        if self.mgr != None and self.mgr.isValid():
            self.isValid = 1
            limit = base.config.GetInt('battle-sound-cache-size', 15)
            self.mgr.setCacheLimit(limit)
            base.addSfxManager(self.mgr)
            self.sfxSearchPath = DSearchPath()
            self.sfxSearchPath.appendDirectory(Filename('phase_3.5/audio/sfx'))
            self.sfxSearchPath.appendDirectory(Filename('phase_4/audio/sfx'))
            self.sfxSearchPath.appendDirectory(Filename('phase_5/audio/sfx'))
            self.sfxSearchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TTMODELS/phase_3.5/audio/sfx')))
            self.sfxSearchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TTMODELS/phase_4/audio/sfx')))
            self.sfxSearchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TTMODELS/phase_5/audio/sfx')))
        

    
    def clear(self):
        if self.isValid:
            self.mgr.clearCache()
        

    
    def getSound(self, name):
        sound = None
        if self.isValid:
            filename = Filename(name)
            if vfs:
                found = vfs.resolveFilename(filename, self.sfxSearchPath)
            else:
                found = filename.resolveFilename(self.sfxSearchPath)
            if not found:
                self.notify.warning('%s not found.' % name)
            else:
                sound = self.mgr.getSound(filename.getFullpath())
        
        return sound


globalBattleSoundCache = BattleSounds()
