# File: F (Python 2.2)

import FishBase
import Localizer
CARD_INDEX = 0
LOCK_INDEX = 1
RewardDict = {
    (5,): (100, Localizer.FishPoker5OfKind),
    (4, 1): (50, Localizer.FishPoker4OfKind),
    (3, 2): (25, Localizer.FishPokerFullHouse),
    (3, 1, 1): (10, Localizer.FishPoker3OfKind),
    (2, 2, 1): (5, Localizer.FishPoker2Pair),
    (2, 1, 1, 1): (2, Localizer.FishPokerPair) }

class FishPokerBase:
    NumSlots = 5
    
    def __init__(self):
        self._FishPokerBase__cards = { }
        self.clear()

    
    def isCard(self, index):
        return self._FishPokerBase__cards[index][CARD_INDEX] is not None

    
    def isLocked(self, index):
        return self._FishPokerBase__cards[index][LOCK_INDEX]

    
    def indexAvailable(self, index):
        (card, locked) = self._FishPokerBase__cards[index]
        if card is None or not locked:
            return 1
        else:
            return 0

    
    def getFirstIndexAvailable(self):
        for i in range(self.NumSlots):
            if not self.isCard(i):
                return i
            
        
        for i in range(self.NumSlots):
            if not self.isLocked(i):
                return i
            
        
        return -1

    
    def setLockStatus(self, index, lockStatus):
        if self._FishPokerBase__cards[index][CARD_INDEX]:
            self._FishPokerBase__cards[index][LOCK_INDEX] = lockStatus
            return 1
        else:
            return 0

    
    def cashIn(self):
        (value, handName) = self.getCurrentValue()
        self.clear()
        return value

    
    def drawCard(self, card):
        index = self.getFirstIndexAvailable()
        if index == -1:
            return -1
        else:
            self._FishPokerBase__cards[index] = [
                card,
                0]
            return index

    
    def getCurrentValue(self):
        cards = { }
        noneList = []
        for cardInfo in self._FishPokerBase__cards.values():
            (card, locked) = cardInfo
            if card is None:
                noneList.append(1)
            else:
                genus = card.getGenus()
                if cards.has_key(genus):
                    cards[genus] += 1
                else:
                    cards[genus] = 1
        
        cardList = cards.values()
        cardList.sort()
        cardList.reverse()
        cardList.extend(noneList)
        cardList = tuple(cardList)
        rewardInfo = RewardDict.get(cardList, (0, ''))
        return rewardInfo

    
    def clear(self):
        for i in range(self.NumSlots):
            self._FishPokerBase__cards[i] = [
                None,
                0]
        

    
    def __str__(self):
        s = ''
        availIndex = self.getFirstIndexAvailable()
        for i in range(self.NumSlots):
            (card, locked) = self._FishPokerBase__cards[i]
            if locked:
                lockedStr = 'Locked'
            else:
                lockedStr = 'Unlocked'
            s += '%s : %s, %s' % (i, card, lockedStr)
            if i == availIndex:
                s += ' <--'
            
            s += '\n'
        
        return s


