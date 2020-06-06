# File: N (Python 2.2)

import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject

class NametagGroup(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libtoontownDowncasts]
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
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libtoontown._inPPj7bpVyl()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libtoontown and libtoontown._inPPj7biJVz:
            libtoontown._inPPj7biJVz(self.this)
        

    
    def getNametag2d(self):
        returnValue = libtoontown._inPPj7bWZsx(self.this)
        import Nametag2d
        returnObject = Nametag2d.Nametag2d(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNametag3d(self):
        returnValue = libtoontown._inPPj7b2lTy(self.this)
        import Nametag3d
        returnObject = Nametag3d.Nametag3d(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def addNametag(self, tag):
        returnValue = libtoontown._inPPj7bYh_6(self.this, tag.this)
        return returnValue

    
    def removeNametag(self, tag):
        returnValue = libtoontown._inPPj7bmyAU(self.this, tag.this)
        return returnValue

    
    def clearAuxNametags(self):
        returnValue = libtoontown._inPPj7ba6CN(self.this)
        return returnValue

    
    def getNumNametags(self):
        returnValue = libtoontown._inPPj7bgAh_(self.this)
        return returnValue

    
    def getNametag(self, n):
        returnValue = libtoontown._inPPj7bcZB4(self.this, n)
        import Nametag
        returnObject = Nametag.Nametag(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setFont(self, font):
        returnValue = libtoontown._inPPj7btk7P(self.this, font.this)
        return returnValue

    
    def setNameFont(self, font):
        returnValue = libtoontown._inPPj7bJKcd(self.this, font.this)
        return returnValue

    
    def getNameFont(self):
        returnValue = libtoontown._inPPj7bpVcO(self.this)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setChatFont(self, font):
        returnValue = libtoontown._inPPj7bKsV_(self.this, font.this)
        return returnValue

    
    def getChatFont(self):
        returnValue = libtoontown._inPPj7bYbUw(self.this)
        import TextFont
        returnObject = TextFont.TextFont(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setAvatar(self, node):
        returnValue = libtoontown._inPPj7boQlI(self.this, node.this)
        return returnValue

    
    def getAvatar(self):
        returnValue = libtoontown._inPPj7bzNb7(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNameIcon(self):
        returnValue = libtoontown._inPPj7bVM7o(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setColorCode(self, code):
        returnValue = libtoontown._inPPj7bFMVu(self.this, code)
        return returnValue

    
    def getColorCode(self):
        returnValue = libtoontown._inPPj7bGKPB(self.this)
        return returnValue

    
    def setName(self, name):
        returnValue = libtoontown._inPPj7bwOEf(self.this, name)
        return returnValue

    
    def getName(self):
        returnValue = libtoontown._inPPj7bBjhN(self.this)
        return returnValue

    
    def setDisplayName(self, name):
        returnValue = libtoontown._inPPj7brmld(self.this, name)
        return returnValue

    
    def getDisplayName(self):
        returnValue = libtoontown._inPPj7bqKNe(self.this)
        return returnValue

    
    def _NametagGroup__overloaded_setChat_ptrNametagGroup_atomicstring_int_int(self, chat, chatFlags, pageNumber):
        returnValue = libtoontown._inPPj7bAWyM(self.this, chat, chatFlags, pageNumber)
        return returnValue

    
    def _NametagGroup__overloaded_setChat_ptrNametagGroup_atomicstring_int(self, chat, chatFlags):
        returnValue = libtoontown._inPPj7bQB5E(self.this, chat, chatFlags)
        return returnValue

    
    def clearChat(self):
        returnValue = libtoontown._inPPj7bORZr(self.this)
        return returnValue

    
    def _NametagGroup__overloaded_getChat_ptrConstNametagGroup(self):
        returnValue = libtoontown._inPPj7bQXZv(self.this)
        return returnValue

    
    def _NametagGroup__overloaded_getChat_ptrConstNametagGroup_int(self, pageNumber):
        returnValue = libtoontown._inPPj7bhrdc(self.this, pageNumber)
        return returnValue

    
    def getChatFlags(self):
        returnValue = libtoontown._inPPj7b_Nze(self.this)
        return returnValue

    
    def setPageNumber(self, pageNumber):
        returnValue = libtoontown._inPPj7bv8N_(self.this, pageNumber)
        return returnValue

    
    def getPageNumber(self):
        returnValue = libtoontown._inPPj7bu09h(self.this)
        return returnValue

    
    def getNumChatPages(self):
        returnValue = libtoontown._inPPj7brjh9(self.this)
        return returnValue

    
    def setUniqueId(self, event):
        returnValue = libtoontown._inPPj7bfUfG(self.this, event)
        return returnValue

    
    def getUniqueId(self):
        returnValue = libtoontown._inPPj7bFtWj(self.this)
        return returnValue

    
    def setObjectCode(self, code):
        returnValue = libtoontown._inPPj7bKyVo(self.this, code)
        return returnValue

    
    def getObjectCode(self):
        returnValue = libtoontown._inPPj7bCKFM(self.this)
        return returnValue

    
    def click(self):
        returnValue = libtoontown._inPPj7bSMcI(self.this)
        return returnValue

    
    def manage(self, manager):
        returnValue = libtoontown._inPPj7bVhks(self.this, manager.this)
        return returnValue

    
    def unmanage(self, manager):
        returnValue = libtoontown._inPPj7b_Twc(self.this, manager.this)
        return returnValue

    
    def isManaged(self):
        returnValue = libtoontown._inPPj7bBM3g(self.this)
        return returnValue

    
    def setContents(self, flags):
        returnValue = libtoontown._inPPj7bDoxe(self.this, flags)
        return returnValue

    
    def getContents(self):
        returnValue = libtoontown._inPPj7bBI8E(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libtoontown._inPPj7bVGf_(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libtoontown._inPPj7bZPl9(self.this)
        return returnValue

    
    def hasPageButton(self):
        returnValue = libtoontown._inPPj7bC4_A(self.this)
        return returnValue

    
    def hasQuitButton(self):
        returnValue = libtoontown._inPPj7b4BPb(self.this)
        return returnValue

    
    def hasButton(self):
        returnValue = libtoontown._inPPj7bjw2w(self.this)
        return returnValue

    
    def willHaveButton(self):
        returnValue = libtoontown._inPPj7bMw0M(self.this)
        return returnValue

    
    def displayAsActive(self):
        returnValue = libtoontown._inPPj7bPE2K(self.this)
        return returnValue

    
    def getChat(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._NametagGroup__overloaded_getChat_ptrConstNametagGroup()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NametagGroup__overloaded_getChat_ptrConstNametagGroup_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setChat(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._NametagGroup__overloaded_setChat_ptrNametagGroup_atomicstring_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._NametagGroup__overloaded_setChat_ptrNametagGroup_atomicstring_int_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


