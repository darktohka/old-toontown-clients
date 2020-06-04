# File: Q (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
import ShtikerPage
from direct.gui.DirectGui import *
from toontown.quest import Quests
from toontown.toon import NPCToons
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.quest import QuestPoster

class QuestPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.quests = {
            0: None,
            1: None,
            2: None,
            3: None }
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.90000000000000002, 1, 1)
        self.textDisabledColor = Vec4(0.40000000000000002, 0.80000000000000004, 0.40000000000000002, 1)
        self.onscreen = 0

    
    def load(self):
        self.title = DirectLabel(parent = self, relief = None, text = TTLocalizer.QuestPageToonTasks, text_scale = 0.12, textMayChange = 0, pos = (0, 0, 0.59999999999999998))
        questFramePlaceList = ((-0.45000000000000001, 0, 0.25, 0, 0, 0), (-0.45000000000000001, 0, -0.34999999999999998, 0, 0, 0), (0.45000000000000001, 0, 0.25, 0, 0, 0), (0.45000000000000001, 0, -0.34999999999999998, 0, 0, 0))
        self.questFrames = []
        for i in range(ToontownGlobals.MaxQuestCarryLimit):
            frame = QuestPoster.QuestPoster(reverse = i > 1)
            frame.reparentTo(self)
            frame.setPosHpr(*questFramePlaceList[i])
            frame.setScale(1.0600000000000001)
            self.questFrames.append(frame)
        

    
    def acceptOnscreenHooks(self):
        self.accept(ToontownGlobals.QuestsHotkeyOn, self.showQuestsOnscreen)
        self.accept(ToontownGlobals.QuestsHotkeyOff, self.hideQuestsOnscreen)

    
    def ignoreOnscreenHooks(self):
        self.ignore(ToontownGlobals.QuestsHotkeyOn)
        self.ignore(ToontownGlobals.QuestsHotkeyOff)

    
    def unload(self):
        del self.title
        del self.quests
        del self.questFrames
        loader.unloadModel('phase_3.5/models/gui/stickerbook_gui')
        ShtikerPage.ShtikerPage.unload(self)

    
    def clearQuestFrame(self, index):
        self.questFrames[index].clear()
        self.quests[index] = None

    
    def fillQuestFrame(self, questDesc, index):
        self.questFrames[index].update(questDesc)
        self.quests[index] = questDesc

    
    def getLowestUnusedIndex(self):
        for i in range(ToontownGlobals.MaxQuestCarryLimit):
            if self.quests[i] == None:
                return i
            
        
        return -1

    
    def updatePage(self):
        newQuests = base.localAvatar.quests
        carryLimit = base.localAvatar.getQuestCarryLimit()
        for i in range(ToontownGlobals.MaxQuestCarryLimit):
            if i < carryLimit:
                self.questFrames[i].show()
            else:
                self.questFrames[i].hide()
        
        for (index, questDesc) in self.quests.items():
            if questDesc is not None and list(questDesc) not in newQuests:
                self.clearQuestFrame(index)
            
        
        for questDesc in newQuests:
            newQuestDesc = tuple(questDesc)
            if newQuestDesc not in self.quests.values():
                index = self.getLowestUnusedIndex()
                self.fillQuestFrame(newQuestDesc, index)
            
        
        for i in self.quests.keys():
            questDesc = self.quests[i]
            if questDesc:
                questId = questDesc[0]
                if Quests.getQuestClass(questId) == Quests.FriendQuest:
                    self.questFrames[i].update(questDesc)
                
            
        

    
    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)

    
    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)

    
    def showQuestsOnscreenTutorial(self):
        self.setPos(0, 0, -0.20000000000000001)
        self.showQuestsOnscreen()

    
    def showQuestsOnscreen(self):
        if self.onscreen or base.localAvatar.invPage.onscreen:
            return None
        
        self.onscreen = 1
        self.updatePage()
        self.reparentTo(aspect2d)
        self.title.hide()
        self.show()

    
    def hideQuestsOnscreenTutorial(self):
        self.setPos(0, 0, 0)
        self.hideQuestsOnscreen()

    
    def hideQuestsOnscreen(self):
        if not (self.onscreen):
            return None
        
        self.onscreen = 0
        self.reparentTo(self.book)
        self.title.show()
        self.hide()


