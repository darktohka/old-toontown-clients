# File: D (Python 2.2)

from ShowBaseGlobal import *
import DistributedObject
import SuitPlannerBase

class DistributedSuitPlanner(DistributedObject.DistributedObject, SuitPlannerBase.SuitPlannerBase):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        SuitPlannerBase.SuitPlannerBase.__init__(self)
        self.suitList = []
        self.buildingList = [
            0,
            0,
            0,
            0]
        return None

    
    def generate(self):
        self.notify.info('DistributedSuitPlanner %d: generating' % self.getDoId())
        DistributedObject.DistributedObject.generate(self)
        toonbase.tcr.currSuitPlanner = self

    
    def disable(self):
        self.notify.info('DistributedSuitPlanner %d: disabling' % self.getDoId())
        DistributedObject.DistributedObject.disable(self)
        toonbase.tcr.currSuitPlanner = None

    
    def d_suitListQuery(self):
        self.sendUpdate('suitListQuery')

    
    def suitListResponse(self, suitList):
        self.suitList = suitList
        messenger.send('suitListResponse')

    
    def d_buildingListQuery(self):
        self.sendUpdate('buildingListQuery')

    
    def buildingListResponse(self, buildingList):
        self.buildingList = buildingList
        messenger.send('buildingListResponse')


