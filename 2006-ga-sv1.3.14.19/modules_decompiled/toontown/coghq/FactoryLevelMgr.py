# File: F (Python 2.2)

from direct.level import LevelMgr
import FactoryUtil
from direct.showbase.PythonUtil import Functor
from toontown.toonbase import ToontownGlobals

class FactoryLevelMgr(LevelMgr.LevelMgr):
    InterestingLocations = [
        (((-866, -272, -40), -101), ((-662, -242, 7.5), 0), ((-20, -180, 20), 0), ((-249, 258, 111), 0), ((318, 241, 115), -16), ((-251, 241, 109), -180), ((296, 292, 703), 56), ((-740, 122, 28), 90), ((210, -270, 38), -90)),
        (((20, 21, 0), 0), ((3, 404, 39), -16), ((-496, 358, 5), 0))]
    
    def __init__(self, level, entId):
        LevelMgr.LevelMgr.__init__(self, level, entId)
        if self.modelFilename == 'phase_9/models/cogHQ/FactoryLayout2':
            
            def hideLift(geom, liftName):
                lift = geom.find('**/%s' % liftName)
                lift.stash()

            hideLift(self.geom, 'Zone22ElevatorLT1')
            hideLift(self.geom, 'Zone23ElevatorRT1')
            
            def renameZoneNodes(prefix):
                allZoneNodes = self.geom.findAllMatches('**/%s*' % prefix).asList()
                for node in allZoneNodes:
                    name = node.getName()
                    
                    try:
                        num = int(name[len(prefix):])
                    except ValueError:
                        node.setName('renamed-%s' % name)

                

            renameZoneNodes('Zone')
            renameZoneNodes('zone')
            dw = self.geom.attachNewNode('Doorway27')
            dw.setPos(-49.399999999999999, 86.700000000000003, 19.260000000000002)
            dw.setH(0)
            doorwayNodes = self.geom.findAllMatches('**/Doorway*').asList()
            for node in doorwayNodes:
                name = node.getName()
                num = int(name[len('Doorway'):])
                name = '%s%s' % ('Zone', 1000 + num)
                node.setName(name)
            
        
        if base.config.GetBool('want-factory-lifter', 0):
            self.toonLifter = FactoryUtil.ToonLifter('f3')
        
        self.callSetters('farPlaneDistance')
        self.geom.reparentTo(render)

    
    def destroy(self):
        if hasattr(self, 'toonLifter'):
            self.toonLifter.destroy()
            del self.toonLifter
        
        LevelMgr.LevelMgr.destroy(self)

    
    def setFarPlaneDistance(self, farPlaneDistance):
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, farPlaneDistance)

    if __dev__:
        
        def setWantDoors(self, wantDoors):
            self.wantDoors = wantDoors
            messenger.send('wantDoorsChanged')

    

