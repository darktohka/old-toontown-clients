# File: S (Python 2.2)

from SCMenu import SCMenu
from SCToontaskTerminal import SCToontaskTerminal
from SCStaticTextTerminal import SCStaticTextTerminal
import Quests

class SCToontaskMenu(SCMenu):
    
    def __init__(self):
        SCMenu.__init__(self)
        self.accept('questsChanged', self._SCToontaskMenu__tasksChanged)
        self._SCToontaskMenu__tasksChanged()

    
    def destroy(self):
        SCMenu.destroy(self)

    
    def _SCToontaskMenu__tasksChanged(self):
        self.clearMenu()
        
        try:
            lt = toonbase.localToon
        except:
            return None

        phrases = []
        
        def addTerminal(terminal, self = self, phrases = phrases):
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
                addTerminal(SCToontaskTerminal(msgs[i], taskId, toNpcId, toonProgress, i))
            
        
        needToontask = 1
        if hasattr(lt, 'questCarryLimit'):
            needToontask = len(lt.quests) != lt.questCarryLimit
        
        if needToontask:
            addTerminal(SCStaticTextTerminal(1299))
        


