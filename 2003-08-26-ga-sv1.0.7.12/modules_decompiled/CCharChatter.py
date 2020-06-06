# File: C (Python 2.2)

import Localizer
GREETING = 0
COMMENT = 1
GOODBYE = 2
MickeyChatter = Localizer.MickeyChatter
MinnieChatter = Localizer.MinnieChatter
GoofyChatter = Localizer.GoofyChatter
DonaldChatter = Localizer.DonaldChatter

def getChatter(charName):
    if charName == Localizer.Mickey:
        return MickeyChatter
    elif charName == Localizer.Minnie:
        return MinnieChatter
    elif charName == Localizer.Goofy:
        return GoofyChatter
    elif charName == Localizer.Donald:
        return DonaldChatter
    elif charName == Localizer.Pluto:
        return None
    

