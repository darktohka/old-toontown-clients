# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\LawbotOfficeLobby_Trap00_Cogs.py
from SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 10000
CogParent1 = 100021
BattlePlace1 = 100020
BattlePlace2 = 100022
BattleCellId = 0
BattleCellId1 = 1
BattleCells = {BattleCellId: {'parentEntId': BattlePlace1, 'pos': Point3(0, 0, 0)}, BattleCellId1: {'parentEntId': BattlePlace2, 'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel, 'battleCell': BattleCellId, 'pos': Point3(-6, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 1}, {'parentEntId': CogParent, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel + 1, 'battleCell': BattleCellId, 'pos': Point3(-2, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 1}, {'parentEntId': CogParent, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel, 'battleCell': BattleCellId, 'pos': Point3(2, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 1}, {'parentEntId': CogParent, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel + 1, 'battleCell': BattleCellId, 'pos': Point3(6, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 1}, {'parentEntId': CogParent1, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel, 'battleCell': BattleCellId1, 'pos': Point3(-6, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 1}, {'parentEntId': CogParent1, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel + 1, 'battleCell': BattleCellId1, 'pos': Point3(-2, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 1}, {'parentEntId': CogParent1, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel, 'battleCell': BattleCellId1, 'pos': Point3(2, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 1}, {'parentEntId': CogParent1, 'boss': 0, 'level': ToontownGlobals.CashbotMintCogLevel + 1, 'battleCell': BattleCellId1, 'pos': Point3(6, 0, 0), 'h': 180, 'behavior': 'stand', 'path': None, 'skeleton': 1}]
ReserveCogData = []