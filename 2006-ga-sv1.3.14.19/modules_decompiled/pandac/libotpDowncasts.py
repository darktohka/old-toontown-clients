# File: l (Python 2.2)

import types
import libotp
import Nametag2d
import MarginPopup
import Nametag3d
import PandaNode
import Nametag
import ClickablePopup
import WhisperPopup

def downcastToNametag2dFromMarginPopup(this):
    returnValue = libotp._inPPj7bB3LF(this.this)
    import Nametag2d
    returnObject = Nametag2d.Nametag2d(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToNametag3dFromPandaNode(this):
    returnValue = libotp._inPPj7bJoRs(this.this)
    import Nametag3d
    returnObject = Nametag3d.Nametag3d(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToNametagFromClickablePopup(this):
    returnValue = libotp._inPPj7bo5La(this.this)
    import Nametag
    returnObject = Nametag.Nametag(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToWhisperPopupFromClickablePopup(this):
    returnValue = libotp._inPPj7bi1Xd(this.this)
    import WhisperPopup
    returnObject = WhisperPopup.WhisperPopup(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject

