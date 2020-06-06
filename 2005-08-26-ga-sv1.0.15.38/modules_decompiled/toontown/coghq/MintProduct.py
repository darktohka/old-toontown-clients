# File: M (Python 2.2)

from toontown.toonbase.ToontownGlobals import *
from otp.level import BasicEntities

class MintProduct(BasicEntities.NodePathEntity):
    Models = {
        CashbotMintIntA: 'phase_10/models/cashbotHQ/MoneyBag',
        CashbotMintIntB: 'phase_10/models/cashbotHQ/MoneyStackPallet',
        CashbotMintIntC: 'phase_10/models/cashbotHQ/GoldBarStack' }
    Scales = {
        CashbotMintIntA: 0.97999999999999998,
        CashbotMintIntB: 0.38,
        CashbotMintIntC: 0.59999999999999998 }
    
    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.model = None
        self.mintId = self.level.mintId
        self.loadModel()

    
    def destroy(self):
        if self.model:
            self.model.removeNode()
            del self.model
        
        BasicEntities.NodePathEntity.destroy(self)

    
    def loadModel(self):
        if self.model:
            self.model.removeNode()
            self.model = None
        
        self.model = loader.loadModelCopy(self.Models[self.mintId])
        self.model.setScale(self.Scales[self.mintId])
        self.model.flattenStrong()
        if self.model:
            self.model.reparentTo(self)
        

    if __dev__:
        
        def setMintId(self, mintId):
            self.mintId = mintId
            self.loadModel()

    

