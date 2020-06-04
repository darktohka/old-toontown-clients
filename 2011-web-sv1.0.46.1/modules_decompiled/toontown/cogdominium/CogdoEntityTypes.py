# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\CogdoEntityTypes.py
from otp.level.EntityTypes import *

class CogdoLevelMgr(LevelMgr):
    __module__ = __name__
    type = 'levelMgr'


class CogdoBoardroomGameSettings(Entity):
    __module__ = __name__
    type = 'cogdoBoardroomGameSettings'
    attribs = (('TimerScale', 1.0, 'float'), )


class CogdoCraneGameSettings(Entity):
    __module__ = __name__
    type = 'cogdoCraneGameSettings'
    attribs = (('GameDuration', 180.0, 'float'), ('EmptyFrictionCoef', 0.1, 'float'), ('Gravity', -32, 'int'), ('RopeLinkMass', 1.0, 'float'), ('MagnetMass', 1.0, 'float'), ('MoneyBagGrabHeight', -8.2, 'float'))


class CogdoCraneCogSettings(Entity):
    __module__ = __name__
    type = 'cogdoCraneCogSettings'
    attribs = (('CogSpawnPeriod', 10.0, 'float'), ('CogWalkSpeed', 2.0, 'float'), ('CogMachineInteractDuration', 2.0, 'float'), ('CogFlyAwayHeight', 50.0, 'float'), ('CogFlyAwayDuration', 4.0, 'float'))