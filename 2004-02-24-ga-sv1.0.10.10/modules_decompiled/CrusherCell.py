# File: C (Python 2.2)

import ActiveCell
import DirectNotifyGlobal

class CrusherCell(ActiveCell.ActiveCell):
    notify = DirectNotifyGlobal.directNotify.newCategory('CrusherCell')
    
    def __init__(self, cr):
        ActiveCell.ActiveCell.__init__(self, cr)


