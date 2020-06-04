# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\RaceGameGlobals.py
from toontown.toonbase import TTLocalizer
ValidChoices = [
 0, 1, 2, 3, 4]
NumberToWin = 14
InputTimeout = 20
ChanceRewards = (
 (
  (1, 0), TTLocalizer.RaceGameForwardOneSpace, 0), ((1, 0), TTLocalizer.RaceGameForwardOneSpace, 0), ((1, 0), TTLocalizer.RaceGameForwardOneSpace, 0), ((2, 0), TTLocalizer.RaceGameForwardTwoSpaces, 0), ((2, 0), TTLocalizer.RaceGameForwardTwoSpaces, 0), ((2, 0), TTLocalizer.RaceGameForwardTwoSpaces, 0), ((3, 0), TTLocalizer.RaceGameForwardThreeSpaces, 0), ((3, 0), TTLocalizer.RaceGameForwardThreeSpaces, 0), ((3, 0), TTLocalizer.RaceGameForwardThreeSpaces, 0), ((0, -3), TTLocalizer.RaceGameOthersBackThree, 0), ((0, -3), TTLocalizer.RaceGameOthersBackThree, 0), ((-1, 0), TTLocalizer.RaceGameBackOneSpace, 0), ((-1, 0), TTLocalizer.RaceGameBackOneSpace, 0), ((-2, 0), TTLocalizer.RaceGameBackTwoSpaces, 0), ((-2, 0), TTLocalizer.RaceGameBackTwoSpaces, 0), ((-3, 0), TTLocalizer.RaceGameBackThreeSpaces, 0), ((-3, 0), TTLocalizer.RaceGameBackThreeSpaces, 0), ((0, 3), TTLocalizer.RaceGameOthersForwardThree, 0), ((0, 3), TTLocalizer.RaceGameOthersForwardThree, 0), ((0, 0), TTLocalizer.RaceGameJellybeans2, 2), ((0, 0), TTLocalizer.RaceGameJellybeans2, 2), ((0, 0), TTLocalizer.RaceGameJellybeans2, 2), ((0, 0), TTLocalizer.RaceGameJellybeans2, 2), ((0, 0), TTLocalizer.RaceGameJellybeans4, 4), ((0, 0), TTLocalizer.RaceGameJellybeans4, 4), ((0, 0), TTLocalizer.RaceGameJellybeans4, 4), ((0, 0), TTLocalizer.RaceGameJellybeans4, 4), ((0, 0), TTLocalizer.RaceGameJellybeans10, 10), ((0, 0), -1, 0), ((NumberToWin, 0), TTLocalizer.RaceGameInstantWinner, 0))