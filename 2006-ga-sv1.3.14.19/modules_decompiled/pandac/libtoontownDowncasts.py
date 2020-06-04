# File: l (Python 2.2)

import types
import libtoontown
import DNAGroup
import Namable

def downcastToDNAGroupFromNamable(this):
    returnValue = libtoontown._inPdt4yJJp5(this.this)
    import DNAGroup
    returnObject = DNAGroup.DNAGroup(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject

