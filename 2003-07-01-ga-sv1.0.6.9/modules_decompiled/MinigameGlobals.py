# File: M (Python 2.2)

import PythonUtil
import ToontownGlobals
latencyTolerance = 10.0
MaxLoadTime = 40.0
rulesDuration = 16
DifficultyOverrideMult = int(1 << 16)

def QuantizeDifficultyOverride(diffOverride):
    return int(round(diffOverride * DifficultyOverrideMult)) / float(DifficultyOverrideMult)

NoDifficultyOverride = 2147483647
NoTrolleyZoneOverride = -1
SafeZones = [
    ToontownGlobals.ToontownCentral,
    ToontownGlobals.DonaldsDock,
    ToontownGlobals.DaisyGardens,
    ToontownGlobals.MinniesMelodyland,
    ToontownGlobals.TheBrrrgh,
    ToontownGlobals.DonaldsDreamland]

def getDifficulty(trolleyZone):
    hoodZone = getSafezoneId(trolleyZone)
    return float(SafeZones.index(hoodZone)) / (len(SafeZones) - 1)


def getSafezoneId(trolleyZone):
    
    def zoneToSafezone(zone):
        return zone - zone % 1000

    return zoneToSafezone(trolleyZone)

