# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\suit\SellbotBossGlobals.py
from pandac.PandaModules import *
from toontown.coghq import DistributedHealBarrelAI
from toontown.coghq import DistributedGagBarrelAI
PieToonup = 1
PieToonupNerfed = 2
PieDamageMult = 1.0
PieDamageMultNerfed = 2.0
AttackMult = 1.0
AttackMultNerfed = 0.5
HitCountDamage = 35
HitCountDamageNerfed = 50
BarrelDefs = {8000: {'type': DistributedHealBarrelAI.DistributedHealBarrelAI, 'pos': Point3(15, 23, 0), 'hpr': Vec3(-45, 0, 0), 'rewardPerGrab': 50, 'rewardPerGrabMax': 0}, 8001: {'type': DistributedGagBarrelAI.DistributedGagBarrelAI, 'pos': Point3(15, -23, 0), 'hpr': Vec3(-135, 0, 0), 'gagLevel': 3, 'gagLevelMax': 0, 'gagTrack': 3, 'rewardPerGrab': 10, 'rewardPerGrabMax': 0}, 8002: {'type': DistributedGagBarrelAI.DistributedGagBarrelAI, 'pos': Point3(21, 20, 0), 'hpr': Vec3(-45, 0, 0), 'gagLevel': 3, 'gagLevelMax': 0, 'gagTrack': 4, 'rewardPerGrab': 10, 'rewardPerGrabMax': 0}, 8003: {'type': DistributedGagBarrelAI.DistributedGagBarrelAI, 'pos': Point3(21, -20, 0), 'hpr': Vec3(-135, 0, 0), 'gagLevel': 3, 'gagLevelMax': 0, 'gagTrack': 5, 'rewardPerGrab': 10, 'rewardPerGrabMax': 0}}

def setBarrelAttr(barrel, entId):
    for (defAttr, defValue) in BarrelDefs[entId].iteritems():
        setattr(barrel, defAttr, defValue)


BarrelsStartPos = (0, -36, -8)
BarrelsFinalPos = (0, -36, 0)