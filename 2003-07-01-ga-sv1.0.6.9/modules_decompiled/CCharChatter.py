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
    if charName == 'Mickey':
        return MickeyChatter
    elif charName == 'Minnie':
        return MinnieChatter
    elif charName == 'Goofy':
        return GoofyChatter
    elif charName == 'Donald':
        return DonaldChatter
    elif charName == 'Pluto':
        return None
    

