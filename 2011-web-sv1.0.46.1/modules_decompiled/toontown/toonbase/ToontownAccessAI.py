# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\toonbase\ToontownAccessAI.py
from otp.otpbase import OTPGlobals
from otp.ai import BanManagerAI
from toontown.toonbase import ToontownGlobals
from toontown.hood import ZoneUtil

def canAccess(avatarId, zoneId, function=''):
    avatar = simbase.air.doId2do.get(avatarId)
    if avatar and avatar.getGameAccess() != OTPGlobals.AccessFull and not openToAll(zoneId, avatar):
        if cmp(function, 'DistributedBoardingPartyAI.checkBoard') == 0:
            return False
        simbase.air.writeServerEvent('suspicious', avatarId, 'User with rights: %s requesting enter for paid access content without proper rights in zone %s from %s' % (avatar.getGameAccess(), zoneId, function))
        if simbase.config.GetBool('want-ban-ispaid', True):
            commentStr = 'User with rights: %s tried to gain access zone %s from function %s, an area they were not allowed to using TTInjector Hack' % (avatar.getGameAccess(), zoneId, function)
            dislId = avatar.DISLid
            simbase.air.banManager.ban(avatarId, dislId, commentStr)
        return False
    else:
        return True


def openToAll(zoneId, avatar):
    allowed = False
    canonicalZoneId = ZoneUtil.getCanonicalHoodId(zoneId)
    allowedZones = [
     ToontownGlobals.ToontownCentral, ToontownGlobals.MyEstate, ToontownGlobals.GoofySpeedway, ToontownGlobals.Tutorial]
    specialZones = [
     ToontownGlobals.SellbotLobby]
    if ToontownGlobals.SELLBOT_NERF_HOLIDAY in simbase.air.holidayManager.currentHolidays:
        specialZones.append(ToontownGlobals.SellbotHQ)
    ownerId = simbase.air.estateMgr.getOwnerFromZone(zoneId)
    if ownerId:
        for zone in simbase.air.estateMgr.getEstateZones(ownerId):
            specialZones.append(zone)

    if canonicalZoneId in allowedZones or avatar.isInEstate():
        allowed = True
    elif zoneId in specialZones:
        allowed = True
    elif canonicalZoneId >= ToontownGlobals.DynamicZonesBegin and not avatar.getTutorialAck():
        zoneDict = simbase.air.tutorialManager.playerDict.get(avatar.doId)
        if zoneDict:
            allowed = True
    return allowed


def canWearSuit(avatarId, zoneId):
    canonicalZoneId = ZoneUtil.getCanonicalHoodId(zoneId)
    allowedSuitZones = [
     ToontownGlobals.LawbotHQ, ToontownGlobals.CashbotHQ, ToontownGlobals.SellbotHQ, ToontownGlobals.BossbotHQ]
    if canonicalZoneId in allowedSuitZones:
        return True
    elif zoneId >= ToontownGlobals.DynamicZonesBegin:
        return True
    else:
        return False