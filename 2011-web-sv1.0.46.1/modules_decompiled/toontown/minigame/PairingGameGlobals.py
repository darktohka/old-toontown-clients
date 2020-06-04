# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\PairingGameGlobals.py
import PlayingCardDeck
EasiestGameDuration = 120
HardestGameDuration = 90
EndlessGame = config.GetBool('endless-pairing-game', 0)
MaxRankIndexUsed = [
 7, 7, 7, 8, 9]

def createDeck(deckSeed, numPlayers):
    deck = PlayingCardDeck.PlayingCardDeck()
    deck.shuffleWithSeed(deckSeed)
    deck.removeRanksAbove(MaxRankIndexUsed[numPlayers])
    return deck


def calcGameDuration(difficulty):
    difference = EasiestGameDuration - HardestGameDuration
    adjust = difference * difficulty
    retval = EasiestGameDuration - adjust
    return retval


def calcLowFlipModifier(matches, flips):
    idealFlips = round(matches * 2 * 1.6)
    if idealFlips < 2:
        idealFlips = 2
    maxFlipsForBonus = idealFlips * 2
    retval = 0
    if flips < idealFlips:
        retval = 1
    elif maxFlipsForBonus < flips:
        retval = 0
    else:
        divisor = maxFlipsForBonus - idealFlips
        difference = maxFlipsForBonus - flips
        retval = float(difference) / divisor
    return retval