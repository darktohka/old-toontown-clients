# File: O (Python 2.2)

from PandaObject import *
import DirectGuiGlobals
import types
Plain = 1
ScreenTitle = 2
ScreenPrompt = 3
NameConfirm = 4
BlackOnWhite = 5

class OnscreenText(PandaObject, NodePath):
    
    def __init__(self, text = '', style = Plain, pos = (0, 0), scale = None, fg = None, bg = None, shadow = None, shadowOffset = (0.040000000000000001, 0.040000000000000001), frame = None, align = None, wordwrap = None, drawOrder = None, font = None, parent = None, sort = 0, mayChange = 0):
        if parent == None:
            parent = aspect2d
        
        textNode = TextNode('')
        self.textNode = textNode
        NodePath.__init__(self)
        if style == Plain:
            if not scale:
                pass
            scale = 0.070000000000000007
            if not fg:
                pass
            fg = (0, 0, 0, 1)
            if not bg:
                pass
            bg = (0, 0, 0, 0)
            if not shadow:
                pass
            shadow = (0, 0, 0, 0)
            if not frame:
                pass
            frame = (0, 0, 0, 0)
            if align == None:
                align = TextNode.ACenter
            
        elif style == ScreenTitle:
            if not scale:
                pass
            scale = 0.14999999999999999
            if not fg:
                pass
            fg = (1, 0.20000000000000001, 0.20000000000000001, 1)
            if not bg:
                pass
            bg = (0, 0, 0, 0)
            if not shadow:
                pass
            shadow = (0, 0, 0, 1)
            if not frame:
                pass
            frame = (0, 0, 0, 0)
            if align == None:
                align = TextNode.ACenter
            
        elif style == ScreenPrompt:
            if not scale:
                pass
            scale = 0.10000000000000001
            if not fg:
                pass
            fg = (1, 1, 0, 1)
            if not bg:
                pass
            bg = (0, 0, 0, 0)
            if not shadow:
                pass
            shadow = (0, 0, 0, 1)
            if not frame:
                pass
            frame = (0, 0, 0, 0)
            if align == None:
                align = TextNode.ACenter
            
        elif style == NameConfirm:
            if not scale:
                pass
            scale = 0.10000000000000001
            if not fg:
                pass
            fg = (0, 1, 0, 1)
            if not bg:
                pass
            bg = (0, 0, 0, 0)
            if not shadow:
                pass
            shadow = (0, 0, 0, 0)
            if not frame:
                pass
            frame = (0, 0, 0, 0)
            if align == None:
                align = TextNode.ACenter
            
        elif style == BlackOnWhite:
            if not scale:
                pass
            scale = 0.10000000000000001
            if not fg:
                pass
            fg = (0, 0, 0, 1)
            if not bg:
                pass
            bg = (1, 1, 1, 1)
            if not shadow:
                pass
            shadow = (0, 0, 0, 0)
            if not frame:
                pass
            frame = (0, 0, 0, 0)
            if align == None:
                align = TextNode.ACenter
            
        else:
            raise ValueError
        if not isinstance(scale, types.TupleType):
            scale = (scale, scale)
        
        self.scale = scale
        self.pos = pos
        if font == None:
            font = DirectGuiGlobals.getDefaultFont()
        
        textNode.freeze()
        textNode.setFont(font)
        textNode.setTextColor(fg[0], fg[1], fg[2], fg[3])
        textNode.setAlign(align)
        if wordwrap:
            textNode.setWordwrap(wordwrap)
        
        if bg[3] != 0:
            textNode.setCardColor(bg[0], bg[1], bg[2], bg[3])
            textNode.setCardAsMargin(0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001)
        
        if shadow[3] != 0:
            textNode.setShadowColor(shadow[0], shadow[1], shadow[2], shadow[3])
            textNode.setShadow(*shadowOffset)
        
        if frame[3] != 0:
            textNode.setFrameColor(frame[0], frame[1], frame[2], frame[3])
            textNode.setFrameAsMargin(0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001)
        
        mat = Mat4.scaleMat(scale[0], 1, scale[1]) * Mat4.translateMat(pos[0], 0, pos[1])
        textNode.setTransform(mat)
        if drawOrder != None:
            textNode.setBin('fixed')
            textNode.setDrawOrder(drawOrder)
        
        textNode.setText(text)
        if not text:
            self.mayChange = 1
        else:
            self.mayChange = mayChange
        if self.mayChange:
            textNode.thaw()
        else:
            self.textNode = textNode.generate()
        self.isClean = 0
        self.assign(parent.attachNewNode(self.textNode, sort))

    
    def cleanup(self):
        self.textNode = None
        if self.isClean == 0:
            self.isClean = 1
            self.removeNode()
        

    
    def destroy(self):
        self.cleanup()

    
    def freeze(self):
        self.textNode.freeze()

    
    def thaw(self):
        self.textNode.thaw()

    
    def setFont(self, font):
        self.textNode.setFont(font)

    
    def getFont(self):
        return self.textNode.getFont()

    
    def setText(self, text):
        self.textNode.setText(text)

    
    def getText(self):
        return self.textNode.getText()

    
    def setX(self, x):
        self.setPos(x, self.pos[1])

    
    def setY(self, y):
        self.setPos(self.pos[0], y)

    
    def setPos(self, x, y):
        self.pos = (x, y)
        mat = Mat4.scaleMat(self.scale[0], 1, self.scale[1]) * Mat4.translateMat(self.pos[0], 0, self.pos[1])
        self.textNode.setTransform(mat)

    
    def getPos(self):
        return self.pos

    
    def setScale(self, sx, sy = None):
        if sy == None:
            if isinstance(sx, types.TupleType):
                self.scale = sx
            else:
                self.scale = (sx, sx)
        else:
            self.scale = (sx, sy)
        mat = Mat4.scaleMat(self.scale[0], 1, self.scale[1]) * Mat4.translateMat(self.pos[0], 0, self.pos[1])
        self.textNode.setTransform(mat)

    
    def getScale(self):
        return self.scale

    
    def setWordwrap(self, wordwrap):
        if wordwrap:
            self.textNode.setWordwrap(wordwrap)
        else:
            self.textNode.clearWordwrap()

    
    def setFg(self, fg):
        self.textNode.setTextColor(fg[0], fg[1], fg[2], fg[3])

    
    def setBg(self, bg):
        self.textNode.freeze()
        if bg[3] != 0:
            self.textNode.setCardColor(bg[0], bg[1], bg[2], bg[3])
            self.textNode.setCardAsMargin(0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001)
        else:
            self.textNode.clearCard()
        self.textNode.thaw()

    
    def setShadow(self, shadow):
        self.textNode.freeze()
        if shadow[3] != 0:
            self.textNode.setShadowColor(*shadow)
            self.textNode.setShadow(*shadowOffset)
        else:
            self.textNode.clearShadow()
        self.textNode.thaw()

    
    def setFrame(self, frame):
        self.textNode.freeze()
        if frame[3] != 0:
            self.textNode.setFrameColor(frame[0], frame[1], frame[2], frame[3])
            self.textNode.setFrameAsMargin(0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001)
        else:
            self.textNode.clearFrame()
        self.textNode.thaw()

    
    def configure(self, option = None, **kw):
        if not (self.mayChange):
            print 'OnscreenText.configure: mayChange == 0'
            return None
        
        self.freeze()
        for (option, value) in kw.items():
            
            try:
                setter = eval('self.set' + string.upper(option[0]) + option[1:])
                if setter == self.setPos:
                    setter(value[0], value[1])
                else:
                    setter(value)
            except AttributeError:
                print 'OnscreenText.configure: invalid option:', option

        
        self.thaw()

    
    def __setitem__(self, key, value):
        apply(self.configure, (), {
            key: value })

    
    def cget(self, option):
        getter = eval('self.get' + string.upper(option[0]) + option[1:])
        return getter()

    
    def setAlign(self, align):
        self.textNode.setAlign(align)

    __getitem__ = cget

