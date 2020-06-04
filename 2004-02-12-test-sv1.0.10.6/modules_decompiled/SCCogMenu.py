# File: S (Python 2.2)

from SCMenu import SCMenu
from SCStaticTextTerminal import SCStaticTextTerminal

class SCCogMenu(SCMenu):
    
    def __init__(self, indices):
        SCMenu.__init__(self)
        for index in indices:
            term = SCStaticTextTerminal(index)
            self.append(term)
        

    
    def destroy(self):
        SCMenu.destroy(self)


