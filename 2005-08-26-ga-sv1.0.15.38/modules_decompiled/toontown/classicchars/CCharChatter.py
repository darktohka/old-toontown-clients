# File: C (Python 2.2)

from toontown.toonbase import TTLocalizer
GREETING = 0
COMMENT = 1
GOODBYE = 2
MickeyChatter = TTLocalizer.MickeyChatter
MinnieChatter = TTLocalizer.MinnieChatter
GoofyChatter = TTLocalizer.GoofyChatter
DonaldChatter = TTLocalizer.DonaldChatter

def getChatter(charName):
    if charName == TTLocalizer.Mickey:
        return MickeyChatter
    elif charName == TTLocalizer.Minnie:
        return MinnieChatter
    elif charName == TTLocalizer.Goofy:
        return GoofyChatter
    elif charName == TTLocalizer.Donald:
        return DonaldChatter
    elif charName == TTLocalizer.Pluto:
        return None
    

