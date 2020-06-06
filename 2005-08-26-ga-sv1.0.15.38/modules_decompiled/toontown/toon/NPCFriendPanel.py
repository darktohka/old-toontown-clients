# File: N (Python 2.2)

from direct.gui.DirectGui import *
import NPCToons
import ToonHead
import ToonDNA
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals

class NPCFriendPanel(DirectFrame):
    
    def __init__(self, parent = aspect2d, **kw):
        optiondefs = (('relief', None, None), ('doneEvent', None, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent = parent)
        self.cardList = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None]
        xOffset = -5.25
        yOffset = 2.2999999999999998
        count = 0
        for i in range(8):
            card = NPCFriendCard(parent = self, doneEvent = self['doneEvent'])
            self.cardList[count] = card
            card.setPos(xOffset, 1, yOffset)
            xOffset += 3.5
            count += 1
            if count == 4:
                xOffset = -5.25
                yOffset = -2.2999999999999998
            
        
        self.initialiseoptions(NPCFriendPanel)

    
    def update(self, friendDict, fCallable = 0):
        friendList = friendDict.keys()
        for i in range(8):
            card = self.cardList[i]
            
            try:
                NPCID = friendList[i]
                count = friendDict[NPCID]
            except IndexError:
                NPCID = None
                count = 0

            card.update(NPCID, count, fCallable)
        



class NPCFriendCard(DirectFrame):
    normalTextColor = (0.29999999999999999, 0.25, 0.20000000000000001, 1)
    maxRarity = 5
    sosTracks = ToontownBattleGlobals.Tracks + ToontownBattleGlobals.NPCTracks
    
    def __init__(self, parent = aspect2dp, **kw):
        optiondefs = (('NPCID', 'Uninitialized', None), ('relief', None, None), ('doneEvent', None, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent = parent)
        self.initialiseoptions(NPCFriendCard)
        cardModel = loader.loadModelOnce('phase_3.5/models/gui/playingCard')
        self.front = DirectFrame(parent = self, relief = None, image = cardModel.find('**/card_front'))
        self.front.hide()
        self.back = DirectFrame(parent = self, relief = None, image = cardModel.find('**/card_back'), geom = cardModel.find('**/logo'))
        self.sosTypeInfo = DirectLabel(parent = self.front, relief = None, text = '', text_font = ToontownGlobals.getMinnieFont(), text_fg = self.normalTextColor, text_scale = 0.34999999999999998, text_align = TextNode.ACenter, text_wordwrap = 7.0, pos = (0, 0, 1.6000000000000001))
        self.NPCHead = None
        self.NPCName = DirectLabel(parent = self.front, relief = None, text = '', text_fg = self.normalTextColor, text_scale = 0.34000000000000002, text_align = TextNode.ACenter, text_wordwrap = 8.0, pos = (0, 0, -0.78000000000000003))
        buttonModels = loader.loadModelOnce('phase_3.5/models/gui/inventory_gui')
        upButton = buttonModels.find('**/InventoryButtonUp')
        downButton = buttonModels.find('**/InventoryButtonDown')
        rolloverButton = buttonModels.find('**/InventoryButtonRollover')
        self.sosCallButton = DirectButton(parent = self.front, relief = None, text = TTLocalizer.NPCCallButtonLabel, text_fg = self.normalTextColor, text_scale = 0.28000000000000003, text_align = TextNode.ACenter, image = (upButton, downButton, rolloverButton, upButton), image_color = (1.0, 0.20000000000000001, 0.20000000000000001, 1), image0_color = Vec4(1.0, 0.40000000000000002, 0.40000000000000002, 1), image3_color = Vec4(1.0, 0.40000000000000002, 0.40000000000000002, 0.40000000000000002), image_scale = (4.4000000000000004, 1, 3.6000000000000001), image_pos = Vec3(0, 0, 0.080000000000000002), pos = (-0.95999999999999996, 0, -1.6000000000000001), scale = 1.25, command = self._NPCFriendCard__chooseNPCFriend)
        self.sosCallButton.hide()
        self.sosCountInfo = DirectLabel(parent = self.front, relief = None, text = '', text_fg = self.normalTextColor, text_scale = 0.40000000000000002, text_align = TextNode.ALeft, textMayChange = 1, pos = (0.0, 0, -1.5))
        star = loader.loadModelCopy('phase_3.5/models/gui/name_star')
        self.rarityStars = []
        for i in range(self.maxRarity):
            label = DirectLabel(parent = self.front, relief = None, image = star, image_scale = 0.20000000000000001, image_color = Vec4(0.502, 0.251, 0.251, 1.0), pos = (1.1000000000000001 - i * 0.23999999999999999, 0, -1.8))
            label.hide()
            self.rarityStars.append(label)
        

    
    def _NPCFriendCard__chooseNPCFriend(self):
        if self['NPCID'] and self['doneEvent']:
            doneStatus = { }
            doneStatus['mode'] = 'NPCFriend'
            doneStatus['friend'] = self['NPCID']
            messenger.send(self['doneEvent'], [
                doneStatus])
        

    
    def update(self, NPCID, count = 0, fCallable = 0):
        oldNPCID = self['NPCID']
        self['NPCID'] = NPCID
        if NPCID != oldNPCID:
            if self.NPCHead:
                self.NPCHead.detachNode()
            
            if NPCID is None:
                self.showBack()
                return None
            
            self.front.show()
            self.back.hide()
            self.NPCName['text'] = TTLocalizer.NPCToonNames[NPCID]
            self.NPCHead = self.createNPCToonHead(NPCID, dimension = 1.3999999999999999)
            self.NPCHead.reparentTo(self.front)
            self.NPCHead.setZ(0.29999999999999999)
            (track, level, hp, rarity) = NPCToons.getNPCTrackLevelHpRarity(NPCID)
            sosText = self.sosTracks[track]
            if track == ToontownBattleGlobals.NPC_RESTOCK_GAGS:
                if level == -1:
                    sosText += ' All'
                else:
                    sosText += ' ' + self.sosTracks[level]
            
            sosText = TextEncoder.upper(sosText)
            self.sosTypeInfo['text'] = sosText
            for i in range(self.maxRarity):
                if i < rarity:
                    self.rarityStars[i].show()
                else:
                    self.rarityStars[i].hide()
            
        
        if fCallable:
            self.sosCallButton.show()
            self.sosCountInfo.setPos(-0.40000000000000002, 0, -1.54)
            self.sosCountInfo['text_scale'] = 0.28000000000000003
            self.sosCountInfo['text_align'] = TextNode.ALeft
        else:
            self.sosCallButton.hide()
            self.sosCountInfo.setPos(0, 0, -1.5)
            self.sosCountInfo['text_scale'] = 0.40000000000000002
            self.sosCountInfo['text_align'] = TextNode.ACenter
        if count > 0:
            countText = '%d Remaining' % count
            self.sosCallButton['state'] = NORMAL
        else:
            countText = 'Unavailable'
            self.sosCallButton['state'] = DISABLED
        self.sosCountInfo['text'] = countText

    
    def showFront(self):
        self.front.show()
        self.back.hide()

    
    def showBack(self):
        self.front.hide()
        self.back.show()

    
    def createNPCToonHead(self, NPCID, dimension = 0.5):
        NPCInfo = NPCToons.NPCToonDict[NPCID]
        dnaList = NPCInfo[2]
        gender = NPCInfo[3]
        if dnaList == 'r':
            dnaList = NPCToons.getRandomDNA(NPCID, gender)
        
        dna = ToonDNA.ToonDNA()
        dna.newToonFromProperties(*dnaList)
        head = ToonHead.ToonHead()
        head.setupHead(dna, forGui = 1)
        self.fitGeometry(head, fFlip = 1, dimension = dimension)
        return head

    
    def fitGeometry(self, geom, fFlip = 0, dimension = 0.5):
        p1 = Point3()
        p2 = Point3()
        geom.calcTightBounds(p1, p2)
        if fFlip:
            t = p1[0]
            p1.setX(-p2[0])
            p2.setX(-t)
        
        d = p2 - p1
        biggest = max(d[0], d[2])
        s = dimension / biggest
        mid = (p1 + d / 2.0) * s
        geomXform = hidden.attachNewNode('geomXform')
        for child in geom.getChildrenAsList():
            child.reparentTo(geomXform)
        
        geomXform.setPosHprScale(-mid[0], -mid[1] + 1, -mid[2], 180, 0, 0, s, s, s)
        geomXform.reparentTo(geom)


