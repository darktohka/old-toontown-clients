# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\CogdoCraneGameConsts.py
from direct.fsm.StatePush import StateVar
from otp.level.EntityStateVarSet import EntityStateVarSet
from toontown.cogdominium.CogdoEntityTypes import CogdoCraneGameSettings, CogdoCraneCogSettings
Settings = EntityStateVarSet(CogdoCraneGameSettings)
CogSettings = EntityStateVarSet(CogdoCraneCogSettings)
CranePosHprs = [
 (13.4, -136.6, 6, -45, 0, 0), (13.4, -91.4, 6, -135, 0, 0), (58.6, -91.4, 6, 135, 0, 0), (58.6, -136.6, 6, 45, 0, 0)]
MoneyBagPosHprs = [
 [
  77.2 - 84, -329.3 + 201, 0, -90, 0, 0], [77.1 - 84, -302.7 + 201, 0, -90, 0, 0], [165.7 - 84, -326.4 + 201, 0, 90, 0, 0], [165.5 - 84, -302.4 + 201, 0, 90, 0, 0], [107.8 - 84, -359.1 + 201, 0, 0, 0, 0], [133.9 - 84, -359.1 + 201, 0, 0, 0, 0], [107.0 - 84, -274.7 + 201, 0, 180, 0, 0], [134.2 - 84, -274.7 + 201, 0, 180, 0, 0]]
for i in xrange(len(MoneyBagPosHprs)):
    MoneyBagPosHprs[i][2] += 6