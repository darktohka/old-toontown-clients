# File: S (Python 2.2)

from SCMenu import SCMenu
from SCEmoteTerminal import SCEmoteTerminal

class SCEmoteMenu(SCMenu):
    
    def __init__(self):
        SCMenu.__init__(self)
        self.accept('emotesChanged', self._SCEmoteMenu__emoteAccessChanged)
        self._SCEmoteMenu__emoteAccessChanged()

    
    def destroy(self):
        SCMenu.destroy(self)

    
    def _SCEmoteMenu__emoteAccessChanged(self):
        self.clearMenu()
        
        try:
            lt = base.localAvatar
        except:
            return None

        for i in range(len(lt.emoteAccess)):
            if lt.emoteAccess[i]:
                self.append(SCEmoteTerminal(i))
            
        


