# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\TravelGameGlobals.py
DefaultStartingVotes = 5
FinalMetagameRoundIndex = 5
BaseBeans = 10
PercentOfVotesConverted = {1: 50, 2: 33, 3: 66, 4: 100}
InputTimeout = 15
MaxDirections = 2
ReasonVote = 0
ReasonPlaceDecider = 1
ReasonRandom = 2
DisplayVotesTimePerPlayer = 2
MoveTrolleyTime = 5
FudgeTime = 0
SpoofFour = False
ReverseWin = False
xInc = 60
yInc = 15
BoardLayout4VotingRounds = {0: {'links': (1, 2), 'pos': (0, 0, 0)}, 1: {'links': (3, 4), 'pos': (xInc, yInc, 0)}, 2: {'links': (4, 5), 'pos': (xInc, -yInc, 0)}, 3: {'links': (6, 7), 'pos': (2 * xInc, 2 * yInc, 0)}, 4: {'links': (7, 8), 'pos': (2 * xInc, 0, 0)}, 5: {'links': (8, 9), 'pos': (2 * xInc, -2 * yInc, 0)}, 6: {'links': (10, 11), 'pos': (3 * xInc, 3 * yInc, 0)}, 7: {'links': (11, 12), 'pos': (3 * xInc, yInc, 0)}, 8: {'links': (12, 13), 'pos': (3 * xInc, -yInc, 0)}, 9: {'links': (13, 14), 'pos': (3 * xInc, -3 * yInc, 0)}, 10: {'links': (), 'pos': (4 * xInc, 4 * yInc, 0), 'baseBonus': 3}, 11: {'links': (), 'pos': (4 * xInc, 2 * yInc, 0), 'baseBonus': 2}, 12: {'links': (), 'pos': (4 * xInc, 0, 0), 'baseBonus': 1}, 13: {'links': (), 'pos': (4 * xInc, -2 * yInc, 0), 'baseBonus': 2}, 14: {'links': (), 'pos': (4 * xInc, -4 * yInc, 0), 'baseBonus': 3}}
BoardLayout0 = {0: {'links': (1, 2), 'pos': (0, 0, 0)}, 1: {'links': (3, 4), 'pos': (xInc, 2 * yInc, 0)}, 2: {'links': (4, 5), 'pos': (xInc, -2 * yInc, 0)}, 3: {'links': (6, 7), 'pos': (2 * xInc, 4 * yInc, 0)}, 4: {'links': (8, 9), 'pos': (2 * xInc, 0, 0)}, 5: {'links': (10, 11), 'pos': (2 * xInc, -4 * yInc, 0)}, 6: {'links': (), 'pos': (3 * xInc, 5 * yInc, 0), 'baseBonus': 2}, 7: {'links': (), 'pos': (3 * xInc, 3 * yInc, 0), 'baseBonus': 2}, 8: {'links': (), 'pos': (3 * xInc, 1 * yInc, 0), 'baseBonus': 1}, 9: {'links': (), 'pos': (3 * xInc, -1 * yInc, 0), 'baseBonus': 1}, 10: {'links': (), 'pos': (3 * xInc, -3 * yInc, 0), 'baseBonus': 2}, 11: {'links': (), 'pos': (3 * xInc, -5 * yInc, 0), 'baseBonus': 2}}
BoardLayout1 = {0: {'links': (1, 2), 'pos': (0, 0, 0)}, 1: {'links': (3, 4), 'pos': (xInc, 3 * yInc, 0)}, 2: {'links': (5, 6), 'pos': (xInc, -3 * yInc, 0)}, 3: {'links': (7, 8), 'pos': (2 * xInc, 4 * yInc, 0)}, 4: {'links': (8, 9), 'pos': (2 * xInc, 2 * yInc, 0)}, 5: {'links': (10, 11), 'pos': (2 * xInc, -2 * yInc, 0)}, 6: {'links': (11, 12), 'pos': (2 * xInc, -4 * yInc, 0)}, 7: {'links': (), 'pos': (3 * xInc, 5 * yInc, 0), 'baseBonus': 2}, 8: {'links': (), 'pos': (3 * xInc, 3 * yInc, 0), 'baseBonus': 1}, 9: {'links': (), 'pos': (3 * xInc, 1 * yInc, 0), 'baseBonus': 2}, 10: {'links': (), 'pos': (3 * xInc, -1 * yInc, 0), 'baseBonus': 2}, 11: {'links': (), 'pos': (3 * xInc, -3 * yInc, 0), 'baseBonus': 1}, 12: {'links': (), 'pos': (3 * xInc, -5 * yInc, 0), 'baseBonus': 2}}
BoardLayout2 = {0: {'links': (1, 2), 'pos': (0, 0, 0)}, 1: {'links': (3, 4), 'pos': (xInc, 3 * yInc, 0)}, 2: {'links': (5, 6), 'pos': (xInc, -3 * yInc, 0)}, 3: {'links': (7, 8), 'pos': (2 * xInc, 4 * yInc, 0)}, 4: {'links': (8, 9), 'pos': (2 * xInc, 2 * yInc, 0)}, 5: {'links': (9, 10), 'pos': (2 * xInc, 0 * yInc, 0)}, 6: {'links': (11, 12), 'pos': (2 * xInc, -4 * yInc, 0)}, 7: {'links': (), 'pos': (3 * xInc, 5 * yInc, 0), 'baseBonus': 2}, 8: {'links': (), 'pos': (3 * xInc, 3 * yInc, 0), 'baseBonus': 1}, 9: {'links': (), 'pos': (3 * xInc, 1 * yInc, 0), 'baseBonus': 1}, 10: {'links': (), 'pos': (3 * xInc, -1 * yInc, 0), 'baseBonus': 2}, 11: {'links': (), 'pos': (3 * xInc, -3 * yInc, 0), 'baseBonus': 2}, 12: {'links': (), 'pos': (3 * xInc, -5 * yInc, 0), 'baseBonus': 2}}
BoardLayout3 = {0: {'links': (1, 2), 'pos': (0, 0, 0)}, 1: {'links': (3, 4), 'pos': (xInc, 2 * yInc, 0)}, 2: {'links': (5, 6), 'pos': (xInc, -3 * yInc, 0)}, 3: {'links': (7, 8), 'pos': (2 * xInc, 4 * yInc, 0)}, 4: {'links': (9, 10), 'pos': (2 * xInc, 0 * yInc, 0)}, 5: {'links': (10, 11), 'pos': (2 * xInc, -2 * yInc, 0)}, 6: {'links': (11, 12), 'pos': (2 * xInc, -4 * yInc, 0)}, 7: {'links': (), 'pos': (3 * xInc, 5 * yInc, 0), 'baseBonus': 2}, 8: {'links': (), 'pos': (3 * xInc, 3 * yInc, 0), 'baseBonus': 2}, 9: {'links': (), 'pos': (3 * xInc, 1 * yInc, 0), 'baseBonus': 2}, 10: {'links': (), 'pos': (3 * xInc, -1 * yInc, 0), 'baseBonus': 1}, 11: {'links': (), 'pos': (3 * xInc, -3 * yInc, 0), 'baseBonus': 1}, 12: {'links': (), 'pos': (3 * xInc, -5 * yInc, 0), 'baseBonus': 2}}
BoardLayouts = (
 BoardLayout0, BoardLayout1, BoardLayout2, BoardLayout3)