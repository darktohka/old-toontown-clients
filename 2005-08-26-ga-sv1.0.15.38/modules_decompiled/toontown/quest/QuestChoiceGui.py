# File: Q (Python 2.2)

from direct.gui.DirectGui import *
import QuestPoster
from toontown.toonbase import ToontownTimer
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class QuestChoiceGui(DirectFrame):
    
    def __init__(self):
        DirectFrame.__init__(self, relief = None, geom = getDefaultDialogGeom(), geom_color = Vec4(0.80000000000000004, 0.59999999999999998, 0.40000000000000002, 1), geom_scale = (1.8500000000000001, 1, 0.90000000000000002), geom_hpr = (0, 0, -90), pos = (-0.84999999999999998, 0, 0))
        self.initialiseoptions(QuestChoiceGui)
        self.questChoicePosters = []
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.cancelButton = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.69999999999999996, 1, 1), text = TTLocalizer.QuestChoiceGuiCancel, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self.chooseQuest, extraArgs = [
            0])
        guiButton.removeNode()
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(self)
        self.timer.setScale(0.29999999999999999)
        base.setCellsAvailable(base.leftCells, 0)
        base.setCellsAvailable([
            base.bottomCells[0],
            base.bottomCells[1]], 0)

    
    def setQuests(self, quests, fromNpcId, timeout):
        for i in range(0, len(quests), 3):
            (questId, rewardId, toNpcId) = quests[i:i + 3]
            qp = QuestPoster.QuestPoster()
            qp.reparentTo(self)
            qp.showChoicePoster(questId, fromNpcId, toNpcId, rewardId, self.chooseQuest)
            self.questChoicePosters.append(qp)
        
        if len(quests) == 1 * 3:
            self['geom_scale'] = (1, 1, 0.90000000000000002)
            self.questChoicePosters[0].setPos(0, 0, 0.10000000000000001)
            self.cancelButton.setPos(0.14999999999999999, 0, -0.375)
            self.timer.setPos(-0.20000000000000001, 0, -0.34999999999999998)
        elif len(quests) == 2 * 3:
            self['geom_scale'] = (1.5, 1, 0.90000000000000002)
            self.questChoicePosters[0].setPos(0, 0, -0.20000000000000001)
            self.questChoicePosters[1].setPos(0, 0, 0.40000000000000002)
            self.cancelButton.setPos(0.14999999999999999, 0, -0.625)
            self.timer.setPos(-0.20000000000000001, 0, -0.59999999999999998)
        elif len(quests) == 3 * 3:
            self['geom_scale'] = (1.8500000000000001, 1, 0.90000000000000002)
            map(lambda x: x.setScale(0.94999999999999996), self.questChoicePosters)
            self.questChoicePosters[0].setPos(0, 0, -0.40000000000000002)
            self.questChoicePosters[1].setPos(0, 0, 0.125)
            self.questChoicePosters[2].setPos(0, 0, 0.65000000000000002)
            self.cancelButton.setPos(0.14999999999999999, 0, -0.80000000000000004)
            self.timer.setPos(-0.20000000000000001, 0, -0.77500000000000002)
        
        self.timer.countdown(timeout, self.timeout)

    
    def chooseQuest(self, questId):
        base.setCellsAvailable(base.leftCells, 1)
        base.setCellsAvailable([
            base.bottomCells[0],
            base.bottomCells[1]], 1)
        self.timer.stop()
        messenger.send('chooseQuest', [
            questId])

    
    def timeout(self):
        messenger.send('chooseQuest', [
            0])


