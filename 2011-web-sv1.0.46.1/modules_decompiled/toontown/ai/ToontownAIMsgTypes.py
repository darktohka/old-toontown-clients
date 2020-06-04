# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\ai\ToontownAIMsgTypes.py
from otp.ai.AIMsgTypes import *
TTAIMsgName2Id = {'DBSERVER_GET_ESTATE': 1040, 'DBSERVER_GET_ESTATE_RESP': 1041, 'PARTY_MANAGER_UD_TO_ALL_AI': 1042, 'IN_GAME_NEWS_MANAGER_UD_TO_ALL_AI': 1043, 'WHITELIST_MANAGER_UD_TO_ALL_AI': 1044}
TTAIMsgId2Names = invertDictLossless(TTAIMsgName2Id)
for (name, value) in TTAIMsgName2Id.items():
    exec '%s = %s' % (name, value)

del name
del value
DBSERVER_PET_OBJECT_TYPE = 5