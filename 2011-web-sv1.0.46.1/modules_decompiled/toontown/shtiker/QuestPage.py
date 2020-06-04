# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\shtiker\QuestPage.py
from pandac.PandaModules import *
import ShtikerPage
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.quest import Quests
from toontown.toon import NPCToons
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.quest import QuestPoster
from direct.directnotify import DirectNotifyGlobal

class QuestPage(ShtikerPage.ShtikerPage):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('QuestPage')

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.quests = {0: None, 1: None, 2: None, 3: None}
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)
        self.onscreen = 0
        self.lastQuestTime = globalClock.getRealTime()
        return

    def load(self):
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.QuestPageToonTasks, text_scale=0.12, textMayChange=0, pos=(0,
                                                                                                                                       0,
                                                                                                                                       0.6))
        questFramePlaceList = (
         (
          -0.45, 0, 0.25, 0, 0, 0), (-0.45, 0, -0.35, 0, 0, 0), (0.45, 0, 0.25, 0, 0, 0), (0.45, 0, -0.35, 0, 0, 0))
        self.questFrames = []
        for i in range(ToontownGlobals.MaxQuestCarryLimit):
            frame = QuestPoster.QuestPoster(reverse=i > 1)
            frame.reparentTo(self)
            frame.setPosHpr(*questFramePlaceList[i])
            frame.setScale(1.06)
            self.questFrames.append(frame)

        return

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
        return

    def fillQuestFrame(self, questDesc, index):
        self.questFrames[index].update(questDesc)
        self.quests[index] = questDesc

    def getLowestUnusedIndex(self):
        for i in range(ToontownGlobals.MaxQuestCarryLimit):
            if self.quests[i] == None:
                return i

        return -1

    def updatePage(self):
        self.notify.debug('updatePage()')
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

        for (i, questDesc) in self.quests.iteritems():
            if questDesc:
                if self.canDeleteQuest(questDesc):
                    self.questFrames[i].setDeleteCallback(self.__deleteQuest)
                else:
                    self.questFrames[i].setDeleteCallback(None)
                self.questFrames[i].update(questDesc)
            else:
                self.questFrames[i].unbindMouseEnter()

        return

    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)
        self.accept('questsChanged', self.updatePage)

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        self.ignore('questsChanged')

    def showQuestsOnscreenTutorial(self):
        self.setPos(0, 0, -0.2)
        self.showQuestsOnscreen()

    def showQuestsOnscreen(self):
        messenger.send('wakeup')
        timedif = globalClock.getRealTime() - self.lastQuestTime
        if timedif < 0.7:
            return
        self.lastQuestTime = globalClock.getRealTime()
        if self.onscreen or base.localAvatar.invPage.onscreen:
            return
        self.onscreen = 1
        self.updatePage()
        self.reparentTo(aspect2d)
        self.title.hide()
        self.show()

    def hideQuestsOnscreenTutorial(self):
        self.setPos(0, 0, 0)
        self.hideQuestsOnscreen()

    def hideQuestsOnscreen(self):
        if not self.onscreen:
            return
        self.onscreen = 0
        self.reparentTo(self.book)
        self.title.show()
        self.hide()

    def canDeleteQuest(self, questDesc):
        return Quests.isQuestJustForFun(questDesc[0], questDesc[3]) and self.onscreen == 0

    def __deleteQuest(self, questDesc):
        base.localAvatar.d_requestDeleteQuest(questDesc)