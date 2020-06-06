# File: D (Python 2.2)

from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
from KnockKnockJokes import *
import ToontownGlobals
import DirectNotifyGlobal
import FSM
import DistributedAnimatedProp
import DelayDelete
import Localizer

class DistributedKnockKnockDoor(DistributedAnimatedProp.DistributedAnimatedProp):
    
    def __init__(self, cr):
        DistributedAnimatedProp.DistributedAnimatedProp.__init__(self, cr)
        self.fsm.setName('DistributedKnockKnockDoor')
        self.rimshot = None
        self.knockSfx = None

    
    def generate(self):
        DistributedAnimatedProp.DistributedAnimatedProp.generate(self)
        self.avatarTracks = []
        self.avatarId = 0

    
    def announceGenerate(self):
        DistributedAnimatedProp.DistributedAnimatedProp.announceGenerate(self)
        self.accept('exitKnockKnockDoorSphere_' + str(self.propId), self.exitTrigger)
        self.acceptAvatar()

    
    def disable(self):
        self.ignore('exitKnockKnockDoorSphere_' + str(self.propId))
        self.ignore('enterKnockKnockDoorSphere_' + str(self.propId))
        DistributedAnimatedProp.DistributedAnimatedProp.disable(self)

    
    def delete(self):
        DistributedAnimatedProp.DistributedAnimatedProp.delete(self)
        if self.rimshot:
            self.rimshot = None
        
        if self.knockSfx:
            self.knockSfx = None
        

    
    def acceptAvatar(self):
        self.acceptOnce('enterKnockKnockDoorSphere_' + str(self.propId), self.enterTrigger)

    
    def setAvatarInteract(self, avatarId):
        DistributedAnimatedProp.DistributedAnimatedProp.setAvatarInteract(self, avatarId)

    
    def avatarExit(self, avatarId):
        if avatarId == self.avatarId:
            for track in self.avatarTracks:
                if track.isPlaying():
                    track.stop()
                
            
            self.avatarTracks = []
        

    
    def knockKnockTrack(self, avatar, duration):
        if avatar == None:
            return None
        
        self.rimshot = base.loadSfx('phase_5/audio/sfx/AA_heal_telljoke.mp3')
        self.knockSfx = base.loadSfx('phase_5/audio/sfx/GUI_knock_3.mp3')
        joke = KnockKnockJokes[self.propId % len(KnockKnockJokes)]
        self.nametag = None
        self.nametagNP = None
        doorNP = render.find('**/KnockKnockDoorSphere_' + str(self.propId) + ';+s')
        if doorNP.isEmpty():
            self.notify.warning('Could not find KnockKnockDoorSphere_%s' % self.propId)
            return None
        
        self.nametag = NametagGroup()
        self.nametag.setAvatar(doorNP)
        self.nametag.setFont(ToontownGlobals.getToonFont())
        self.nametag.setName('door')
        self.nametag.setActive(0)
        self.nametag.manage(toonbase.marginManager)
        self.nametag.getNametag3d().setBillboardOffset(4)
        nametagNode = self.nametag.getNametag3d().upcastToPandaNode()
        self.nametagNP = render.attachNewNode(nametagNode)
        self.nametagNP.setName('knockKnockDoor_nt_' + str(self.propId))
        pos = doorNP.node().getSolid(0).getCenter()
        self.nametagNP.setPos(pos + Vec3(0, 0, avatar.getHeight() + 2))
        d = duration * 0.125
        track = Sequence(Parallel(Sequence(Wait(d * 0.5), SoundInterval(self.knockSfx)), Func(self.nametag.setChat, Localizer.DoorKnockKnock, CFSpeech), Wait(d)), Func(avatar.setChatAbsolute, Localizer.DoorWhosThere, CFSpeech | CFTimeout, openEnded = 0), Wait(d), Func(self.nametag.setChat, joke[0], CFSpeech), Wait(d), Func(avatar.setChatAbsolute, joke[0] + Localizer.DoorWhoAppendix, CFSpeech | CFTimeout, openEnded = 0), Wait(d), Func(self.nametag.setChat, joke[1], CFSpeech), Parallel(SoundInterval(self.rimshot, startTime = 2.0), Wait(d * 4)), Func(self.cleanupTrack))
        track.delayDelete = DelayDelete.DelayDelete(avatar)
        return track

    
    def cleanupTrack(self):
        avatar = self.cr.doId2do.get(self.avatarId, None)
        if avatar:
            avatar.clearChat()
        
        if self.nametag:
            self.nametag.unmanage(toonbase.marginManager)
            self.nametagNP.removeNode()
        
        self.nametag = None
        self.nametagNP = None
        return None

    
    def enterOff(self):
        DistributedAnimatedProp.DistributedAnimatedProp.enterOff(self)

    
    def exitOff(self):
        DistributedAnimatedProp.DistributedAnimatedProp.exitOff(self)

    
    def enterAttract(self, ts):
        DistributedAnimatedProp.DistributedAnimatedProp.enterAttract(self, ts)
        self.acceptAvatar()

    
    def exitAttract(self):
        DistributedAnimatedProp.DistributedAnimatedProp.exitAttract(self)

    
    def enterPlaying(self, ts):
        DistributedAnimatedProp.DistributedAnimatedProp.enterPlaying(self, ts)
        if self.avatarId:
            avatar = self.cr.doId2do.get(self.avatarId, None)
            track = self.knockKnockTrack(avatar, 8)
            if track != None:
                track.start(ts)
                self.avatarTracks.append(track)
            
        

    
    def exitPlaying(self):
        DistributedAnimatedProp.DistributedAnimatedProp.exitPlaying(self)
        for track in self.avatarTracks:
            track.finish()
        
        self.avatarTracks = []
        self.avatarId = 0


