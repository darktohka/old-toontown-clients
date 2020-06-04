# File: E (Python 2.2)

from toontown.toonbase import ToontownGlobals
import ShtikerPage
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
PICKER_START_POS = (-0.55500000000000005, 0, 0)
MAX_FRAMES = 15
emoteAnimDict = {
    'Jump': 'jump',
    'Happy': 'Happy',
    'Sad': 'Sad',
    'Sleepy': 'Sleep',
    'Dance': 'victory' }

class EmoteFrame(DirectFrame):
    
    def __init__(self, emoteName = '?'):
        DirectFrame.__init__(self, relief = None)
        bookModel = loader.loadModelOnce('phase_3.5/models/gui/stickerbook_gui')
        self.normalTextColor = (0.29999999999999999, 0.25, 0.20000000000000001, 1)
        self.name = emoteName
        self.frame = DirectFrame(parent = self, relief = None, image = bookModel.find('**/paper_note'), image_scale = (0.80000000000000004, 0.90000000000000002, 0.90000000000000002), text = self.name, text_pos = (0, -0.34000000000000002), text_fg = self.normalTextColor, text_scale = 0.14999999999999999)
        self.question = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, -0.14999999999999999), text = '?', text_scale = 0.40000000000000002, text_pos = (0, 0), text_fg = (0.29999999999999999, 0.25, 0.20000000000000001, 0.10000000000000001))
        self.toon = None
        if self.name != '?':
            self.makeToon()
        
        bookModel.removeNode()

    
    def updateEmote(self, emoteName):
        self.name = emoteName
        self.frame['text'] = self.name
        self.frame.setText()
        self.makeToon()
        self.question.hide()

    
    def makeToon(self):
        if self.toon != None:
            del self.toon
        
        self.toon = Toon.Toon()
        self.toon.setDNA(base.localAvatar.getStyle())
        self.toon.getGeomNode().setDepthWrite(1)
        self.toon.getGeomNode().setDepthTest(1)
        self.toon.useLOD(500)
        self.toon.reparentTo(self.frame)
        self.toon.setPosHprScale(0, 10, -0.25, 210, 0, 0, 0.14999999999999999, 0.14999999999999999, 0.14999999999999999)
        self.toon.loop('neutral')
        
        try:
            anim = emoteAnimDict[self.name]
        except:
            print 'we didnt get the right animation'
            anim = 'neutral'

        self.toon.animFSM.request(anim)

    
    def play(self, trackId):
        if not (base.launcher) and base.launcher and base.launcher.getPhaseComplete(5):
            anim = emoteAnimDict[self.emoteName]
        else:
            anim = 'neutral'
        if self.toon == None:
            self.makeToon()
        
        self.toon.play(anim)

    
    def setTrained(self, trackId):
        if self.toon == None:
            self.makeToon()
        
        if not (base.launcher) and base.launcher and base.launcher.getPhaseComplete(5):
            anim = emoteAnimDict[self.emoteName]
        else:
            anim = 'neutral'
        self.toon.pose(anim, 0)
        self.toon.show()
        self.question.hide()
        self.frame['image_color'] = Vec4(1, 1, 1, 1)

    
    def setUntrained(self, trackId):
        if self.toon:
            self.toon.hide()
        
        self.question.show()
        self.frame['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 0.5)



class EmotePage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.emotes = []
        self.emoteFrames = []
        self.avatar = None
        self.state = NORMAL

    
    def setAvatar(self, av):
        self.avatar = av

    
    def getAvatar(self):
        return self.avatar

    
    def placeFrames(self):
        rowPos = [
            0.26000000000000001,
            -0.089999999999999997,
            -0.44]
        colPos = [
            -0.69999999999999996,
            -0.34999999999999998,
            0,
            0.34999999999999998,
            0.69999999999999996]
        for index in range(1, MAX_FRAMES + 1):
            frame = self.emoteFrames[index - 1]
            col = (index - 1) % 5
            row = (index - 1) / 5
            frame.setPos(colPos[col], 0, rowPos[row])
            frame.setScale(0.40000000000000002)
        

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent = self, relief = None, text = TTLocalizer.EmotePageTitle, text_scale = 0.12, pos = (0, 0, 0.59999999999999998))
        for index in range(1, MAX_FRAMES + 1):
            if index < len(self.emotes):
                frame = EmoteFrame(self.emotes[index - 1])
            else:
                frame = EmoteFrame()
            frame.reparentTo(self)
            self.emoteFrames.append(frame)
        
        self.placeFrames()
        self.updatePage()

    
    def unload(self):
        del self.title
        del self.emoteFrames
        ShtikerPage.ShtikerPage.unload(self)

    
    def updatePage(self):
        newEmotes = base.localAvatar.emotes
        for i in range(len(newEmotes)):
            emote = newEmotes[i]
            self.emotes.append(emote)
            self.emoteFrames[i].updateEmote(emote)
        

    
    def makeEmoteButton(self, emote):
        return DirectButton(parent = self, relief = None, text = emote, text_scale = 0.080000000000000002, text_align = TextNode.ALeft, text1_bg = Vec4(1, 1, 0, 1), text2_bg = Vec4(0.5, 0.90000000000000002, 1, 1), text3_fg = Vec4(0.40000000000000002, 0.80000000000000004, 0.40000000000000002, 1), command = self.showEmotePanel, extraArgs = [
            emote], pos = (-0.25 + 0.050000000000000003 * len(self.emotes), 0, -0.25))

    
    def showEmotePanel(self):
        self.emotePanel.show()

    
    def hideEmotePanel(self):
        self.emotePanel.hide()


