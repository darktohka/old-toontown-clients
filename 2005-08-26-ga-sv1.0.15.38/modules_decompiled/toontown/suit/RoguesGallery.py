# File: R (Python 2.2)

from pandac.PandaModules import *
from direct.showbase import PandaObject
from direct.fsm import StateData
import Suit
import SuitDNA
from toontown.toonbase import ToontownGlobals
import whrandom

class RoguesGallery(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, rognamestr = None):
        StateData.StateData.__init__(self, 'roguesDone')
        self.rognamestr = rognamestr
        self.left = -1.333
        self.right = 1.333
        self.bottom = -1.0
        self.top = 1.0
        self.sideMargins = 0.10000000000000001
        self.topMargins = 0.10000000000000001
        self.xSpaceBetweenDifferentSuits = 0.01
        self.xSpaceBetweenSameSuits = 0.0
        self.ySpaceBetweenSuits = 0.050000000000000003
        self.labelScale = 1.0

    
    def load(self):
        if StateData.StateData.load(self):
            self.width = self.right - self.left - self.sideMargins * 2.0
            self.height = self.top - self.bottom - self.topMargins * 2.0
            if self.rognamestr == None:
                self.numSuitTypes = SuitDNA.suitsPerDept
                self.numSuitDepts = len(SuitDNA.suitDepts)
            else:
                self.numSuitTypes = 1
                self.numSuitDepts = 1
                self.xSpaceBetweenDifferentSuits = 0.0
                self.xSpaceBetweenSameSuits = 0.0
                self.ySpaceBetweenSuits = 0.0
            self.ySuitInc = (self.height + self.ySpaceBetweenSuits) / self.numSuitDepts
            self.ySuitMaxAllowed = self.ySuitInc - self.ySpaceBetweenSuits
            self.xRowSpace = self.width - (self.numSuitTypes - 1) * self.xSpaceBetweenDifferentSuits - self.numSuitTypes * self.xSpaceBetweenSameSuits
            self._RoguesGallery__makeGallery()
        

    
    def unload(self):
        if StateData.StateData.unload(self):
            self.gallery.removeNode()
            del self.suits
            del self.actors
        

    
    def enter(self):
        if StateData.StateData.enter(self):
            render.hide()
            aspect2d.hide()
            self.gallery.reparentTo(render2d)
            self.gallery.setMat(base.aspect2d.getMat())
            self.gallery.setPos(0.0, 10.0, 0.0)
            base.setBackgroundColor(0.59999999999999998, 0.59999999999999998, 0.59999999999999998)
        

    
    def exit(self):
        if StateData.StateData.exit(self):
            self.stop()
            render.show()
            aspect2d.show()
            self.gallery.reparentTo(hidden)
            self.gallery.clearMat()
            base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
            self.ignoreAll()
        

    
    def animate(self):
        self.load()
        for suit in self.actors:
            suit.pose('neutral', whrandom.randint(0, suit.getNumFrames('neutral') - 1))
            suit.loop('neutral', 0)
        

    
    def stop(self):
        self.load()
        for suit in self.actors:
            suit.pose('neutral', 30)
        

    
    def autoExit(self):
        self.acceptOnce('mouse1', self.exit)

    
    def _RoguesGallery__makeGallery(self):
        self.gallery = hidden.attachNewNode('gallery')
        self.gallery.setDepthWrite(1)
        self.gallery.setDepthTest(1)
        self.suits = []
        self.actors = []
        self.text = TextNode('rogues')
        self.text.setFont(ToontownGlobals.getInterfaceFont())
        self.text.setAlign(TextNode.ACenter)
        self.text.setTextColor(0.0, 0.0, 0.0, 1.0)
        self.rowHeight = 0.0
        self.minXScale = None
        print "rognamestr='", self.rognamestr, "'\n"
        if self.rognamestr == None or len(self.rognamestr) == 0:
            for dept in SuitDNA.suitDepts:
                self._RoguesGallery__makeDept(dept)
            
        else:
            self.suitRow = []
            self.rowWidth = 0.0
            self._RoguesGallery__makeSuit(None, None, self.rognamestr)
            self.minXScale = self.xRowSpace / self.rowWidth
            self.suits.append((self.rowWidth, self.suitRow))
            del self.suitRow
        self._RoguesGallery__rescaleSuits()

    
    def _RoguesGallery__makeDept(self, dept):
        self.suitRow = []
        self.rowWidth = 0.0
        for type in range(self.numSuitTypes):
            self._RoguesGallery__makeSuit(dept, type)
        
        xScale = self.xRowSpace / self.rowWidth
        if self.minXScale == None or self.minXScale > xScale:
            self.minXScale = xScale
        
        self.suits.append((self.rowWidth, self.suitRow))
        del self.suitRow

    
    def _RoguesGallery__makeSuit(self, dept, type, name = None):
        dna = SuitDNA.SuitDNA()
        if name != None:
            dna.newSuit(name)
        else:
            dna.newSuitRandom(type + 1, dept)
        suit = Suit.Suit()
        suit.setStyle(dna)
        suit.generateSuit()
        suit.pose('neutral', 30)
        ll = Point3()
        ur = Point3()
        suit.update()
        suit.calcTightBounds(ll, ur)
        suitWidth = ur[0] - ll[0]
        suitDepth = ur[1] - ll[1]
        suitHeight = ur[2] - ll[2]
        self.rowWidth += suitWidth + suitDepth
        self.rowHeight = max(self.rowHeight, suitHeight)
        suit.reparentTo(self.gallery)
        suit.setHpr(180.0, 0.0, 0.0)
        profile = Suit.Suit()
        profile.setStyle(dna)
        profile.generateSuit()
        profile.pose('neutral', 30)
        profile.reparentTo(self.gallery)
        profile.setHpr(90.0, 0.0, 0.0)
        self.suitRow.append((type, suitWidth, suit, suitDepth, profile))
        self.actors.append(suit)
        self.actors.append(profile)

    
    def _RoguesGallery__rescaleSuits(self):
        yScale = self.ySuitMaxAllowed / self.rowHeight
        scale = min(self.minXScale, yScale)
        y = (self.top - self.topMargins) + self.ySpaceBetweenSuits
        for (rowWidth, suitRow) in self.suits:
            rowWidth *= scale
            extraSpace = self.xRowSpace - rowWidth
            extraSpacePerSuit = extraSpace / (self.numSuitTypes * 2 - 1)
            x = self.left + self.sideMargins
            y -= self.ySuitInc
            for (type, width, suit, depth, profile) in suitRow:
                left = x
                width *= scale
                suit.setScale(scale)
                suit.setPos(x + width / 2.0, 0.0, y)
                x += width + self.xSpaceBetweenSameSuits + extraSpacePerSuit
                depth *= scale
                profile.setScale(scale)
                profile.setPos(x + depth / 2.0, 0.0, y)
                x += depth
                right = x
                x += self.xSpaceBetweenDifferentSuits + extraSpacePerSuit
                self.text.setText(suit.getName())
                name = self.gallery.attachNewNode(self.text.generate())
                name.setPos((right + left) / 2.0, 0.0, y + (suit.height + self.labelScale * 0.5) * scale)
                name.setScale(self.labelScale * scale)
            
        


