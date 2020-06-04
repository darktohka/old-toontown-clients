# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\FactoryEntityCreator.py
from otp.level import EntityCreator
import FactoryLevelMgr, PlatformEntity, ConveyorBelt, GearEntity, PaintMixer, GoonClipPlane, MintProduct, MintProductPallet, MintShelf, PathMasterEntity, RenderingEntity

class FactoryEntityCreator(EntityCreator.EntityCreator):
    __module__ = __name__

    def __init__(self, level):
        EntityCreator.EntityCreator.__init__(self, level)
        nothing = EntityCreator.nothing
        nonlocal = EntityCreator.nonlocal
        self.privRegisterTypes({'activeCell': nonlocal, 'crusherCell': nonlocal, 'battleBlocker': nonlocal, 'beanBarrel': nonlocal, 'button': nonlocal, 'conveyorBelt': ConveyorBelt.ConveyorBelt, 'crate': nonlocal, 'door': nonlocal, 'directionalCell': nonlocal, 'gagBarrel': nonlocal, 'gear': GearEntity.GearEntity, 'goon': nonlocal, 'gridGoon': nonlocal, 'golfGreenGame': nonlocal, 'goonClipPlane': GoonClipPlane.GoonClipPlane, 'grid': nonlocal, 'healBarrel': nonlocal, 'levelMgr': FactoryLevelMgr.FactoryLevelMgr, 'lift': nonlocal, 'mintProduct': MintProduct.MintProduct, 'mintProductPallet': MintProductPallet.MintProductPallet, 'mintShelf': MintShelf.MintShelf, 'mover': nonlocal, 'paintMixer': PaintMixer.PaintMixer, 'pathMaster': PathMasterEntity.PathMasterEntity, 'rendering': RenderingEntity.RenderingEntity, 'platform': PlatformEntity.PlatformEntity, 'sinkingPlatform': nonlocal, 'stomper': nonlocal, 'stomperPair': nonlocal, 'laserField': nonlocal, 'securityCamera': nonlocal, 'elevatorMarker': nonlocal, 'trigger': nonlocal, 'moleField': nonlocal, 'maze': nonlocal})