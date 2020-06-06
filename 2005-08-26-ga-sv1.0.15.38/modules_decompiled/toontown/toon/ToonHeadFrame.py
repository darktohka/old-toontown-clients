# File: T (Python 2.2)

from direct.gui.DirectGui import *
import ToonHead
from direct.distributed import DelayDelete
from toontown.toonbase import ToontownGlobals

class ToonHeadFrame(DirectFrame):
    
    def __init__(self, av):
        DirectFrame.__init__(self, relief = None, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (1, 1, 0.5), pos = (0, 0, 0))
        self.initialiseoptions(ToonHeadFrame)
        self.av = av
        self.avKeep = DelayDelete.DelayDelete(av)
        self.head = self.stateNodePath[0].attachNewNode('head', 20)
        self.head.setPosHprScale(-0.27000000000000002, 10.0, -0.089999999999999997, 180.0, 0.0, 0.0, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001)
        self.headModel = ToonHead.ToonHead()
        self.headModel.startBlink()
        self.headModel.setupHead(self.av.style, forGui = 1)
        self.headModel.reparentTo(self.head)
        self.tag1Node = NametagFloat2d()
        self.tag1Node.setContents(Nametag.CSpeech | Nametag.CThought)
        self.av.nametag.addNametag(self.tag1Node)
        self.tag1 = self.attachNewNode(self.tag1Node.upcastToPandaNode())
        self.tag1.setPosHprScale(-0.16, 0, -0.089999999999999997, 0, 0, 0, 0.055, 0.055, 0.055)
        self.tag2Node = NametagFloat2d()
        self.tag2Node.setContents(Nametag.CName)
        self.av.nametag.addNametag(self.tag2Node)
        self.tag2 = self.attachNewNode(self.tag2Node.upcastToPandaNode())
        self.tag2.setPosHprScale(-0.27000000000000002, 10.0, 0.16, 0, 0, 0, 0.050000000000000003, 0.050000000000000003, 0.050000000000000003)

    
    def destroy(self):
        DirectFrame.destroy(self)
        self.headModel.delete()
        del self.headModel
        self.head.removeNode()
        del self.head
        self.av.nametag.removeNametag(self.tag1Node)
        self.av.nametag.removeNametag(self.tag2Node)
        self.tag1.removeNode()
        self.tag2.removeNode()
        del self.tag1
        del self.tag2
        del self.tag1Node
        del self.tag2Node
        del self.av
        del self.avKeep


