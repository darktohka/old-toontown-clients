# File: F (Python 2.2)

from direct.level import EntityCreator
import FactoryLevelMgr
import PlatformEntity
import ConveyorBelt
import GearEntity
import PaintMixer
import GoonClipPlane

class FactoryEntityCreator(EntityCreator.EntityCreator):
    
    def __init__(self, level):
        EntityCreator.EntityCreator.__init__(self, level)
        nothing = EntityCreator.nothing
        self.privRegisterTypes({
            'activeCell': nothing,
            'crusherCell': nothing,
            'battleBlocker': nothing,
            'beanBarrel': nothing,
            'button': nothing,
            'conveyorBelt': ConveyorBelt.ConveyorBelt,
            'crate': nothing,
            'door': nothing,
            'directionalCell': nothing,
            'gagBarrel': nothing,
            'gear': GearEntity.GearEntity,
            'goon': nothing,
            'gridGoon': nothing,
            'goonClipPlane': GoonClipPlane.GoonClipPlane,
            'grid': nothing,
            'healBarrel': nothing,
            'levelMgr': FactoryLevelMgr.FactoryLevelMgr,
            'lift': nothing,
            'paintMixer': PaintMixer.PaintMixer,
            'platform': PlatformEntity.PlatformEntity,
            'sinkingPlatform': nothing,
            'stomper': nothing,
            'stomperPair': nothing,
            'trigger': nothing })


