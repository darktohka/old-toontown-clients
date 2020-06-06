# File: T (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
import DirectNotifyGlobal
import ToontownDialog
import ToonHead

class ToonHeadDialog(ToontownDialog.ToontownDialog):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonHeadDialog')
    
    def __init__(self, dna, **kw):
        self.dna = dna
        head = hidden.attachNewNode('head', 20)
        self.headModel = ToonHead.ToonHead()
        self.headModel.setupHead(self.dna, forGui = 1)
        self.headModel.fitAndCenterHead(1.0, forGui = 1)
        self.headModel.reparentTo(head)
        self.headModel.setName('headModel')
        self.headModel.startBlink()
        optiondefs = (('dialogName', 'ToonHeadDialog', None), ('style', ToontownDialog.NoButtons, None), ('geom', head, None), ('geom_scale', 0.34999999999999998, None), ('geom_pos', (-0.25, 0, 0), None), ('text_wordwrap', 9, None), ('fadeScreen', 0, None))
        self.defineoptions(kw, optiondefs)
        ToontownDialog.ToontownDialog.__init__(self, style = self['style'])
        self.initialiseoptions(ToonHeadDialog)
        self.postInitialiseFuncList.append(self.replaceHead)

    
    def replaceHead(self):
        head = self.stateNodePath[0].find('**/head')
        headModelCopy = self.stateNodePath[0].find('**/headModel')
        headModelCopy.removeNode()
        self.headModel.reparentTo(head)

    
    def cleanup(self):
        ToontownDialog.ToontownDialog.cleanup(self)
        self.headModel.stopBlink()
        self.headModel.stopLookAroundNow()


