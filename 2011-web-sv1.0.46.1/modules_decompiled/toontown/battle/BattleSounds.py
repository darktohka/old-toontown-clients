# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\battle\BattleSounds.py
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import AppRunnerGlobal
import os

class BattleSounds:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('BattleSounds')

    def __init__(self):
        self.mgr = AudioManager.createAudioManager()
        self.isValid = 0
        if self.mgr != None and self.mgr.isValid():
            self.isValid = 1
            limit = base.config.GetInt('battle-sound-cache-size', 15)
            self.mgr.setCacheLimit(limit)
            base.addSfxManager(self.mgr)
            self.setupSearchPath()
        return

    def setupSearchPath(self):
        self.sfxSearchPath = DSearchPath()
        if AppRunnerGlobal.appRunner:
            self.sfxSearchPath.appendDirectory(Filename.expandFrom('$TT_3_ROOT/phase_3/audio/sfx'))
            self.sfxSearchPath.appendDirectory(Filename.expandFrom('$TT_3_5_ROOT/phase_3.5/audio/sfx'))
            self.sfxSearchPath.appendDirectory(Filename.expandFrom('$TT_4_ROOT/phase_4/audio/sfx'))
            self.sfxSearchPath.appendDirectory(Filename.expandFrom('$TT_5_ROOT/phase_5/audio/sfx'))
        else:
            self.sfxSearchPath.appendDirectory(Filename('phase_3/audio/sfx'))
            self.sfxSearchPath.appendDirectory(Filename('phase_3.5/audio/sfx'))
            self.sfxSearchPath.appendDirectory(Filename('phase_4/audio/sfx'))
            self.sfxSearchPath.appendDirectory(Filename('phase_5/audio/sfx'))
            self.sfxSearchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TTMODELS/built/phase_3/audio/sfx')))
            self.sfxSearchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TTMODELS/built/phase_3.5/audio/sfx')))
            self.sfxSearchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TTMODELS/built/phase_4/audio/sfx')))
            self.sfxSearchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TTMODELS/built/phase_5/audio/sfx')))

    def clear(self):
        if self.isValid:
            self.mgr.clearCache()

    def getSound(self, name):
        if self.isValid:
            filename = Filename(name)
            found = vfs.resolveFilename(filename, self.sfxSearchPath)
            if not found:
                self.setupSearchPath()
                found = vfs.resolveFilename(filename, self.sfxSearchPath)
            if not found:
                self.notify.warning('%s not found on:' % name)
                print self.sfxSearchPath
            else:
                return self.mgr.getSound(filename.getFullpath())
        return self.mgr.getNullSound()


globalBattleSoundCache = BattleSounds()