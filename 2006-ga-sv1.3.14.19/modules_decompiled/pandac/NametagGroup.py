# File: N (Python 2.2)

import types
import libotp
import libotpDowncasts
from direct.ffi import FFIExternalObject

class NametagGroup(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libotpDowncasts]
    CCToonBuilding = 4
    CCHouseBuilding = 6
    CCNormal = 0
    CCNonPlayer = 2
    CCNoChat = 1
    CCSuitBuilding = 5
    CCSuit = 3
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libotp._inPPj7boVyl()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libotp and libotp._inPPj7btJVz:
            libotp._inPPj7btJVz(self.this)
        

    
    def getNametag2d(self):
        returnValue = libotp._inPPj7bRZsx(self.this)
        import Nametag2d
        returnObject = Nametag2d.Nametag2d(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNametag3d(self):
        returnValue = libotp._inPPj7bxlTy(self.this)
        import Nametag3d
        returnObject = Nametag3d.Nametag3d(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def addNametag(self, tag):
        returnValue = libotp._inPPj7bZh_6(self.this, tag.this)
        return returnValue

    
    def removeNametag(self, tag):
        returnValue = libotp._inPPj7bmyAU(self.this, tag.this)
        return returnValue

    
    def clearAuxNametags(self):
        returnValue = libotp._inPPj7ba6CN(self.this)
        return returnValue

    
    def getNumNametags(self):
        returnValue = libotp._inPPj7bvAh_(self.this)
        return returnValue

    
    def getNametag(self, n):
        returnValue = libotp._inPPj7bfZB4(self.this, n)
        import Nametag
        returnObject = Nametag.Nametag(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setFont(self, font):
        returnValue = libotp._inPPj7btk7P(self.this, font.this)
        return returnValue

    
    def setNameFont(self, font):
        returnValue = libotp._inPPj7bJKcd(self.this, font.this)
        return returnValue

    
    def getNameFont(self):
        returnValue = libotp._inPPj7bpVcO(self.this)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setChatFont(self, font):
        returnValue = libotp._inPPj7bLsV_(self.this, font.this)
        return returnValue

    
    def getChatFont(self):
        returnValue = libotp._inPPj7bXbUw(self.this)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setAvatar(self, node):
        returnValue = libotp._inPPj7boQlI(self.this, node.this)
        return returnValue

    
    def getAvatar(self):
        returnValue = libotp._inPPj7byNb7(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNameIcon(self):
        returnValue = libotp._inPPj7bUM7o(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setNameWordwrap(self, nameWordwrap):
        returnValue = libotp._inPPj7bLovf(self.this, nameWordwrap)
        return returnValue

    
    def getNameWordwrap(self):
        returnValue = libotp._inPPj7bLH6E(self.this)
        return returnValue

    
    def setColorCode(self, code):
        returnValue = libotp._inPPj7bGMVu(self.this, code)
        return returnValue

    
    def getColorCode(self):
        returnValue = libotp._inPPj7bGKPB(self.this)
        return returnValue

    
    def setQtColor(self, color):
        returnValue = libotp._inPPj7bhJqj(self.this, color.this)
        return returnValue

    
    def getQtColor(self):
        returnValue = libotp._inPPj7bewH0(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setShadow(self, xoffset, yoffset):
        returnValue = libotp._inPPj7bm0NC(self.this, xoffset, yoffset)
        return returnValue

    
    def clearShadow(self):
        returnValue = libotp._inPPj7b9dMi(self.this)
        return returnValue

    
    def hasShadow(self):
        returnValue = libotp._inPPj7bAZuj(self.this)
        return returnValue

    
    def getShadow(self):
        returnValue = libotp._inPPj7bUuN5(self.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setName(self, name):
        returnValue = libotp._inPPj7bwOEf(self.this, name)
        return returnValue

    
    def getName(self):
        returnValue = libotp._inPPj7bBjhN(self.this)
        return returnValue

    
    def setDisplayName(self, name):
        returnValue = libotp._inPPj7brmld(self.this, name)
        return returnValue

    
    def getDisplayName(self):
        returnValue = libotp._inPPj7bqKNe(self.this)
        return returnValue

    
    def _NametagGroup__overloaded_setChat_ptrNametagGroup_atomicstring_int_int(self, chat, chatFlags, pageNumber):
        returnValue = libotp._inPPj7bAWyM(self.this, chat, chatFlags, pageNumber)
        return returnValue

    
    def _NametagGroup__overloaded_setChat_ptrNametagGroup_atomicstring_int(self, chat, chatFlags):
        returnValue = libotp._inPPj7bQB5E(self.this, chat, chatFlags)
        return returnValue

    
    def clearChat(self):
        returnValue = libotp._inPPj7bPRZr(self.this)
        return returnValue

    
    def _NametagGroup__overloaded_getChat_ptrConstNametagGroup(self):
        returnValue = libotp._inPPj7bTXZv(self.this)
        return returnValue

    
    def _NametagGroup__overloaded_getChat_ptrConstNametagGroup_int(self, pageNumber):
        returnValue = libotp._inPPj7bhrdc(self.this, pageNumber)
        return returnValue

    
    def getChatFlags(self):
        returnValue = libotp._inPPj7b_Nze(self.this)
        return returnValue

    
    def setPageNumber(self, pageNumber):
        returnValue = libotp._inPPj7bg8N_(self.this, pageNumber)
        return returnValue

    
    def getPageNumber(self):
        returnValue = libotp._inPPj7bp09h(self.this)
        return returnValue

    
    def getNumChatPages(self):
        returnValue = libotp._inPPj7bUjh9(self.this)
        return returnValue

    
    def setUniqueId(self, event):
        returnValue = libotp._inPPj7bfUfG(self.this, event)
        return returnValue

    
    def getUniqueId(self):
        returnValue = libotp._inPPj7batWj(self.this)
        return returnValue

    
    def setObjectCode(self, code):
        returnValue = libotp._inPPj7bLyVo(self.this, code)
        return returnValue

    
    def getObjectCode(self):
        returnValue = libotp._inPPj7bCKFM(self.this)
        return returnValue

    
    def click(self):
        returnValue = libotp._inPPj7bSMcI(self.this)
        return returnValue

    
    def manage(self, manager):
        returnValue = libotp._inPPj7bUhks(self.this, manager.this)
        return returnValue

    
    def unmanage(self, manager):
        returnValue = libotp._inPPj7b_Twc(self.this, manager.this)
        return returnValue

    
    def isManaged(self):
        returnValue = libotp._inPPj7bOM3g(self.this)
        return returnValue

    
    def setContents(self, flags):
        returnValue = libotp._inPPj7bDoxe(self.this, flags)
        return returnValue

    
    def getContents(self):
        returnValue = libotp._inPPj7bBI8E(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libotp._inPPj7bWGf_(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libotp._inPPj7bePl9(self.this)
        return returnValue

    
    def hasPageButton(self):
        returnValue = libotp._inPPj7bC4_A(self.this)
        return returnValue

    
    def hasQuitButton(self):
        returnValue = libotp._inPPj7b4BPb(self.this)
        return returnValue

    
    def hasButton(self):
        returnValue = libotp._inPPj7biw2w(self.this)
        return returnValue

    
    def willHaveButton(self):
        returnValue = libotp._inPPj7bMw0M(self.this)
        return returnValue

    
    def displayAsActive(self):
        returnValue = libotp._inPPj7bPE2K(self.this)
        return returnValue

    
    def getChat(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NametagGroup__overloaded_getChat_ptrConstNametagGroup(*_args)
        elif numArgs == 1:
            return self._NametagGroup__overloaded_getChat_ptrConstNametagGroup_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setChat(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NametagGroup__overloaded_setChat_ptrNametagGroup_atomicstring_int(*_args)
        elif numArgs == 3:
            return self._NametagGroup__overloaded_setChat_ptrNametagGroup_atomicstring_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


