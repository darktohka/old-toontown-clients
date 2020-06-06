# File: B (Python 2.2)

import ShtikerPage
from DirectGui import *
import Localizer

class BuildingPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent = self, relief = None, text = Localizer.BuildingPageTitle, text_scale = 0.12, pos = (0, 0, 0.59999999999999998))

    
    def unload(self):
        del self.title
        ShtikerPage.ShtikerPage.unload(self)


