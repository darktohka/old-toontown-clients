# File: D (Python 2.2)

from ShowBaseGlobal import *
import Hood
import DDTownLoader
import DDSafeZoneLoader
from ToontownGlobals import *

class DDHood(Hood.Hood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore)
        self.id = DonaldsDock
        self.townLoaderClass = DDTownLoader.DDTownLoader
        self.safeZoneLoaderClass = DDSafeZoneLoader.DDSafeZoneLoader
        self.storageDNAFile = 'phase_6/dna/storage_DD.dna'
        self.skyFile = 'phase_6/models/props/BR_sky'
        self.titleColor = (0.80000000000000004, 0.59999999999999998, 0.5, 1.0)
        self.whiteFogColor = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        self.underwaterFogColor = Vec4(0.0, 0.0, 0.59999999999999998, 1.0)

    
    def load(self):
        Hood.Hood.load(self)
        self.parentFSM.getStateNamed('DDHood').addChild(self.fsm)
        self.fog = Fog('DDFog')

    
    def unload(self):
        self.parentFSM.getStateNamed('DDHood').removeChild(self.fsm)
        Hood.Hood.unload(self)
        self.fog = None

    
    def enter(self, *args):
        Hood.Hood.enter(self, *args)

    
    def exit(self):
        Hood.Hood.exit(self)

    
    def setUnderwaterFog(self):
        if base.wantFog:
            self.fog.setColor(self.underwaterFogColor)
            self.fog.setLinearRange(0.10000000000000001, 100.0)
            render.setFog(self.fog)
            self.sky.setFog(self.fog)
        

    
    def setWhiteFog(self):
        if base.wantFog:
            self.fog.setColor(self.whiteFogColor)
            self.fog.setLinearRange(0.0, 400.0)
            render.clearFog()
            render.setFog(self.fog)
            self.sky.clearFog()
            self.sky.setFog(self.fog)
        

    
    def setNoFog(self):
        if base.wantFog:
            render.clearFog()
            self.sky.clearFog()
        


