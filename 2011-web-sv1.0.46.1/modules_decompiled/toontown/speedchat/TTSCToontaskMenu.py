# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\speedchat\TTSCToontaskMenu.py
from otp.speedchat.SCMenu import SCMenu
from TTSCToontaskTerminal import TTSCToontaskTerminal
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from toontown.quest import Quests

class TTSCToontaskMenu(SCMenu):
    __module__ = __name__

    def __init__(self):
        SCMenu.__init__(self)
        self.accept('questsChanged', self.__tasksChanged)
        self.__tasksChanged()

    def destroy(self):
        SCMenu.destroy(self)

    def __tasksChanged(self):
        self.clearMenu()
        try:
            lt = base.localAvatar
        except:
            return

        phrases = []

        def addTerminal(terminal, self=self, phrases=phrases):
            displayText = terminal.getDisplayText()
            if displayText not in phrases:
                self.append(terminal)
                phrases.append(displayText)

        for task in lt.quests:
            (taskId, fromNpcId, toNpcId, rewardId, toonProgress) = task
            q = Quests.getQuest(taskId)
            if q is None:
                continue
            msgs = q.getSCStrings(toNpcId, toonProgress)
            if type(msgs) != type([]):
                msgs = [
                 msgs]
            for i in xrange(len(msgs)):
                addTerminal(TTSCToontaskTerminal(msgs[i], taskId, toNpcId, toonProgress, i))

        needToontask = 1
        if hasattr(lt, 'questCarryLimit'):
            needToontask = len(lt.quests) != lt.questCarryLimit
        if needToontask:
            addTerminal(SCStaticTextTerminal(1299))
        return