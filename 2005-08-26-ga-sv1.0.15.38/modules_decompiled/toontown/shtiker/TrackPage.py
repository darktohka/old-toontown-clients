# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
import ShtikerPage
from direct.gui.DirectGui import *
from toontown.quest import Quests
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
MAX_FRAMES = 18
Track2Anim = {
    ToontownBattleGlobals.HEAL_TRACK: 'juggle',
    ToontownBattleGlobals.TRAP_TRACK: 'toss',
    ToontownBattleGlobals.LURE_TRACK: 'hypnotize',
    ToontownBattleGlobals.SOUND_TRACK: 'sound',
    ToontownBattleGlobals.THROW_TRACK: 'throw',
    ToontownBattleGlobals.SQUIRT_TRACK: 'firehose',
    ToontownBattleGlobals.DROP_TRACK: 'pushbutton' }

class TrackFrame(DirectFrame):
    
    def __init__(self, index):
        DirectFrame.__init__(self, relief = None)
        self.initialiseoptions(TrackFrame)
        filmstrip = loader.loadModelOnce('phase_3.5/models/gui/filmstrip')
        self.index = index
        self.frame = DirectFrame(parent = self, relief = None, image = filmstrip, image_scale = 1, text = str(self.index - 1), text_pos = (0.26000000000000001, -0.22), text_fg = (1, 1, 1, 1), text_scale = 0.10000000000000001)
        self.question = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, -0.14999999999999999), text = '?', text_scale = 0.40000000000000002, text_pos = (0, 0.040000000000000001), text_fg = (0.71999999999999997, 0.71999999999999997, 0.71999999999999997, 1))
        self.toon = None
        filmstrip.removeNode()

    
    def makeToon(self):
        self.toon = Toon.Toon()
        self.toon.setDNA(base.localAvatar.getStyle())
        self.toon.getGeomNode().setDepthWrite(1)
        self.toon.getGeomNode().setDepthTest(1)
        self.toon.useLOD(500)
        self.toon.reparentTo(self.frame)
        self.toon.setPosHprScale(0, 10, -0.25, 210, 0, 0, 0.12, 0.12, 0.12)

    
    def play(self, trackId):
        if not (base.launcher) and base.launcher and base.launcher.getPhaseComplete(5):
            anim = Track2Anim[trackId]
        else:
            anim = 'neutral'
        if self.toon:
            numFrames = self.toon.getNumFrames(anim) - 1
            fromFrame = 0
            toFrame = ((self.toon.getNumFrames(anim) - 1) / MAX_FRAMES) * self.index
            self.toon.play(anim, None, fromFrame, toFrame - 1)
        

    
    def setTrained(self, trackId):
        if self.toon == None:
            self.makeToon()
        
        if not (base.launcher) and base.launcher and base.launcher.getPhaseComplete(5):
            anim = Track2Anim[trackId]
            frame = ((self.toon.getNumFrames(anim) - 1) / MAX_FRAMES) * self.index
        else:
            anim = 'neutral'
            frame = 0
        self.toon.pose(anim, frame)
        self.toon.show()
        self.question.hide()
        (trackColorR, trackColorG, trackColorB) = ToontownBattleGlobals.TrackColors[trackId]
        self.frame['image_color'] = Vec4(trackColorR, trackColorG, trackColorB, 1)
        self.frame['text_fg'] = Vec4(trackColorR * 0.29999999999999999, trackColorG * 0.29999999999999999, trackColorB * 0.29999999999999999, 1)

    
    def setUntrained(self, trackId):
        if self.toon:
            self.toon.hide()
        
        self.question.show()
        if trackId == -1:
            self.frame['image_color'] = Vec4(0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 1)
            self.frame['text_fg'] = Vec4(0.5, 0.5, 0.5, 1)
            self.question['text_fg'] = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1)
        else:
            (trackColorR, trackColorG, trackColorB) = ToontownBattleGlobals.TrackColors[trackId]
            self.frame['image_color'] = Vec4(trackColorR * 0.69999999999999996, trackColorG * 0.69999999999999996, trackColorB * 0.69999999999999996, 1)
            self.frame['text_fg'] = Vec4(trackColorR * 0.29999999999999999, trackColorG * 0.29999999999999999, trackColorB * 0.29999999999999999, 1)
            self.question['text_fg'] = Vec4(trackColorR * 0.59999999999999998, trackColorG * 0.59999999999999998, trackColorB * 0.59999999999999998, 1)



class TrackPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.trackFrames = []

    
    def placeFrames(self):
        rowY = 0.38
        rowSpace = -0.32000000000000001
        rowPos = []
        for i in range(3):
            rowPos.append(rowY)
            rowY += rowSpace
        
        colX = -0.69999999999999996
        colSpace = 0.27600000000000002
        colPos = []
        for i in range(6):
            colPos.append(colX)
            colX += colSpace
        
        for index in range(1, MAX_FRAMES + 1):
            frame = self.trackFrames[index - 1]
            col = (index - 1) % 6
            row = (index - 1) / 6
            frame.setPos(colPos[col], 0, rowPos[row])
            frame.setScale(0.39000000000000001)
        

    
    def load(self):
        self.title = DirectLabel(parent = self, relief = None, text = TTLocalizer.TrackPageTitle, text_scale = 0.10000000000000001, pos = (0, 0, 0.65000000000000002))
        self.subtitle = DirectLabel(parent = self, relief = None, text = TTLocalizer.TrackPageSubtitle, text_scale = 0.050000000000000003, text_fg = (0.5, 0.10000000000000001, 0.10000000000000001, 1), pos = (0, 0, 0.56000000000000005))
        self.trackText = DirectLabel(parent = self, relief = None, text = '', text_scale = 0.050000000000000003, text_fg = (0.5, 0.10000000000000001, 0.10000000000000001, 1), pos = (0, 0, -0.5))
        for index in range(1, MAX_FRAMES + 1):
            frame = TrackFrame(index)
            frame.reparentTo(self)
            self.trackFrames.append(frame)
        
        self.placeFrames()
        self.startFrame = self.trackFrames[0]
        self.endFrame = self.trackFrames[-1]
        self.startFrame.frame['text'] = ''
        self.startFrame.frame['text_scale'] = 0.12
        self.startFrame.frame['image_color'] = Vec4(0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 1)
        self.startFrame.frame['text_fg'] = (1, 1, 1, 1)
        self.startFrame.frame['text_pos'] = (0, 0.080000000000000002)
        self.startFrame.question.hide()
        self.endFrame.frame['text'] = TTLocalizer.TrackPageDone
        self.endFrame.frame['text_scale'] = 0.12
        self.endFrame.frame['image_color'] = Vec4(0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 1)
        self.endFrame.frame['text_fg'] = (1, 1, 1, 1)
        self.endFrame.frame['text_pos'] = (0, 0)
        self.endFrame.question.hide()

    
    def unload(self):
        del self.title
        del self.subtitle
        del self.trackText
        del self.trackFrames
        ShtikerPage.ShtikerPage.unload(self)

    
    def clearPage(self):
        for index in range(1, MAX_FRAMES - 1):
            self.trackFrames[index].setUntrained(-1)
        
        self.startFrame.frame['text'] = ''
        self.trackText['text'] = TTLocalizer.TrackPageClear
        return None

    
    def updatePage(self):
        (trackId, trackProgress) = base.localAvatar.getTrackProgress()
        if trackId == -1:
            self.clearPage()
        else:
            trackName = ToontownBattleGlobals.Tracks[trackId].capitalize()
            self.trackText['text'] = TTLocalizer.TrackPageTraining % (trackName, trackName)
            trackProgressArray = base.localAvatar.getTrackProgressAsArray()
            for index in range(1, MAX_FRAMES - 2):
                if trackProgressArray[index - 1]:
                    self.trackFrames[index].setTrained(trackId)
                else:
                    self.trackFrames[index].setUntrained(trackId)
            
            self.trackFrames[MAX_FRAMES - 2].setUntrained(trackId)
            self.startFrame.frame['text'] = TTLocalizer.TrackPageFilmTitle % trackName
        return None

    
    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)
        return None

    
    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        return None


