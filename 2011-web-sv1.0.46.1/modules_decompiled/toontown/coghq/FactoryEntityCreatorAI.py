# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\FactoryEntityCreatorAI.py
from otp.level import EntityCreatorAI
from direct.showbase.PythonUtil import Functor
import DistributedBeanBarrelAI, DistributedButtonAI, DistributedCrateAI, DistributedLiftAI, DistributedDoorEntityAI, DistributedGagBarrelAI, DistributedGridAI
from toontown.suit import DistributedGridGoonAI
from toontown.suit import DistributedGoonAI
import DistributedHealBarrelAI, DistributedStomperPairAI, DistributedTriggerAI, DistributedStomperAI, DistributedLaserFieldAI, DistributedSecurityCameraAI, DistributedMoverAI, DistributedElevatorMarkerAI, DistributedSinkingPlatformAI, ActiveCellAI, CrusherCellAI, DirectionalCellAI, FactoryLevelMgrAI, BattleBlockerAI, DistributedGolfGreenGameAI
from toontown.coghq import DistributedMoleFieldAI
from toontown.coghq import DistributedMazeAI

class FactoryEntityCreatorAI(EntityCreatorAI.EntityCreatorAI):
    __module__ = __name__

    def __init__(self, level):
        EntityCreatorAI.EntityCreatorAI.__init__(self, level)
        cDE = EntityCreatorAI.createDistributedEntity
        cLE = EntityCreatorAI.createLocalEntity
        nothing = EntityCreatorAI.nothing
        self.privRegisterTypes({'activeCell': Functor(cDE, ActiveCellAI.ActiveCellAI), 'crusherCell': Functor(cDE, CrusherCellAI.CrusherCellAI), 'battleBlocker': Functor(cDE, BattleBlockerAI.BattleBlockerAI), 'beanBarrel': Functor(cDE, DistributedBeanBarrelAI.DistributedBeanBarrelAI), 'button': DistributedButtonAI.DistributedButtonAI, 'conveyorBelt': nothing, 'crate': Functor(cDE, DistributedCrateAI.DistributedCrateAI), 'directionalCell': Functor(cDE, DirectionalCellAI.DirectionalCellAI), 'door': DistributedDoorEntityAI.DistributedDoorEntityAI, 'gagBarrel': Functor(cDE, DistributedGagBarrelAI.DistributedGagBarrelAI), 'gear': nothing, 'goon': Functor(cDE, DistributedGoonAI.DistributedGoonAI), 'gridGoon': Functor(cDE, DistributedGridGoonAI.DistributedGridGoonAI), 'golfGreenGame': Functor(cDE, DistributedGolfGreenGameAI.DistributedGolfGreenGameAI), 'goonClipPlane': nothing, 'grid': Functor(cDE, DistributedGridAI.DistributedGridAI), 'healBarrel': Functor(cDE, DistributedHealBarrelAI.DistributedHealBarrelAI), 'levelMgr': Functor(cLE, FactoryLevelMgrAI.FactoryLevelMgrAI), 'lift': Functor(cDE, DistributedLiftAI.DistributedLiftAI), 'mintProduct': nothing, 'mintProductPallet': nothing, 'mintShelf': nothing, 'mover': Functor(cDE, DistributedMoverAI.DistributedMoverAI), 'paintMixer': nothing, 'pathMaster': nothing, 'rendering': nothing, 'platform': nothing, 'sinkingPlatform': Functor(cDE, DistributedSinkingPlatformAI.DistributedSinkingPlatformAI), 'stomper': Functor(cDE, DistributedStomperAI.DistributedStomperAI), 'stomperPair': Functor(cDE, DistributedStomperPairAI.DistributedStomperPairAI), 'laserField': Functor(cDE, DistributedLaserFieldAI.DistributedLaserFieldAI), 'securityCamera': Functor(cDE, DistributedSecurityCameraAI.DistributedSecurityCameraAI), 'elevatorMarker': Functor(cDE, DistributedElevatorMarkerAI.DistributedElevatorMarkerAI), 'trigger': DistributedTriggerAI.DistributedTriggerAI, 'moleField': Functor(cDE, DistributedMoleFieldAI.DistributedMoleFieldAI), 'maze': Functor(cDE, DistributedMazeAI.DistributedMazeAI)})