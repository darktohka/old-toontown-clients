# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\CashbotMintDuctRoom_Battle01_Cogs.py
from SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 10000
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': CogParent, 'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent, 'boss': 1, 'level': ToontownGlobals.CashbotMintBossLevel, 'battleCell': BattleCellId, 'pos': Point3(-6, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 1}, {'parentEntId': CogParent, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel + 1, 'battleCell': BattleCellId, 'pos': Point3(-2, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 0}, {'parentEntId': CogParent, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel + 1, 'battleCell': BattleCellId, 'pos': Point3(2, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 0}, {'parentEntId': CogParent, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel + 1, 'battleCell': BattleCellId, 'pos': Point3(6, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 0}]
ReserveCogData = []