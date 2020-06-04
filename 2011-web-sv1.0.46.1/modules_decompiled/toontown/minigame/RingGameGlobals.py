# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\RingGameGlobals.py
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
ENDLESS_GAME = config.GetBool('endless-ring-game', 0)
NUM_RING_GROUPS = 16
MAX_TOONXZ = 10.0
CollisionRadius = 1.5
CollideMask = ToontownGlobals.CatchGameBitmask
RING_RADIUS = MAX_TOONXZ / 3.0 * 0.9
ringColors = (
 (
  TTLocalizer.ColorRed, VBase4(1.0, 0.4, 0.2, 1.0)), (TTLocalizer.ColorGreen, VBase4(0.0, 0.9, 0.2, 1.0)), (TTLocalizer.ColorOrange, VBase4(1.0, 0.5, 0.25, 1.0)), (TTLocalizer.ColorPurple, VBase4(1.0, 0.0, 1.0, 1.0)), (TTLocalizer.ColorWhite, VBase4(1.0, 1.0, 1.0, 1.0)), (TTLocalizer.ColorBlack, VBase4(0.0, 0.0, 0.0, 1.0)), (TTLocalizer.ColorYellow, VBase4(1.0, 1.0, 0.2, 1.0)))
ringColorSelection = [
 (0, 1, 2), 3, 4, 5, 6]