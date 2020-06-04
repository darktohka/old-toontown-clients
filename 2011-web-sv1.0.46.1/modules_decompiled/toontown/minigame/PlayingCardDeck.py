# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\PlayingCardDeck.py
import random, PlayingCardGlobals
from toontown.minigame.PlayingCard import PlayingCardBase

class PlayingCardDeck:
    __module__ = __name__

    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.cards = range(0, PlayingCardGlobals.MaxSuit * PlayingCardGlobals.MaxRank)
        random.shuffle(self.cards)

    def shuffleWithSeed(self, seed):
        generator = random.Random()
        generator.seed(seed)
        self.cards = range(0, PlayingCardGlobals.MaxSuit * PlayingCardGlobals.MaxRank)
        generator.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop(0)

    def dealCards(self, num):
        cardList = []
        for i in range(num):
            cardList.append(self.cards.pop(0))

        return cardList

    def count(self):
        return len(self.cards)

    def removeRanksAbove(self, maxRankInDeck):
        done = False
        while not done:
            removedOne = False
            for cardValue in self.cards:
                tempCard = PlayingCardBase(cardValue)
                if tempCard.rank > maxRankInDeck:
                    self.cards.remove(cardValue)
                    removedOne = True

            if not removedOne:
                done = True