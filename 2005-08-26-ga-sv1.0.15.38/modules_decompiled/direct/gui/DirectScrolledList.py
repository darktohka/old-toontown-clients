# File: D (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from DirectFrame import *
from DirectButton import *
from direct.task import Task
import types

class DirectScrolledListItem(DirectButton):
    notify = DirectNotifyGlobal.directNotify.newCategory('DirectScrolledListItem')
    
    def __init__(self, parent = None, **kw):
        self.parent = parent
        if kw.has_key('command'):
            self.nextCommand = kw.get('command')
            del kw['command']
        
        if kw.has_key('extraArgs'):
            self.nextCommandExtraArgs = kw.get('extraArgs')
            del kw['extraArgs']
        
        optiondefs = (('parent', self.parent, None), ('command', self.select, None))
        self.defineoptions(kw, optiondefs)
        DirectButton.__init__(self)
        self.initialiseoptions(DirectScrolledListItem)

    
    def select(self):
        apply(self.nextCommand, self.nextCommandExtraArgs)
        self.parent.selectListItem(self)



class DirectScrolledList(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('DirectScrolledList')
    
    def __init__(self, parent = None, **kw):
        self.index = 0
        self.forceHeight = None
        if kw.has_key('items'):
            for item in kw['items']:
                if type(item) != type(''):
                    break
                
            else:
                kw['items'] = kw['items'][:]
        
        self.nextItemID = 10
        optiondefs = (('items', [], None), ('itemsAlign', TextNode.ACenter, INITOPT), ('itemsWordwrap', None, INITOPT), ('command', None, None), ('extraArgs', [], None), ('itemMakeFunction', None, None), ('itemMakeExtraArgs', [], None), ('numItemsVisible', 1, self.setNumItemsVisible), ('scrollSpeed', 8, self.setScrollSpeed), ('forceHeight', None, self.setForceHeight))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.incButton = self.createcomponent('incButton', (), None, DirectButton, (self,))
        self.incButton.bind(B1PRESS, self._DirectScrolledList__incButtonDown)
        self.incButton.bind(B1RELEASE, self._DirectScrolledList__buttonUp)
        self.decButton = self.createcomponent('decButton', (), None, DirectButton, (self,))
        self.decButton.bind(B1PRESS, self._DirectScrolledList__decButtonDown)
        self.decButton.bind(B1RELEASE, self._DirectScrolledList__buttonUp)
        self.itemFrame = self.createcomponent('itemFrame', (), None, DirectFrame, (self,))
        for item in self['items']:
            if item.__class__.__name__ != 'str':
                item.reparentTo(self.itemFrame)
            
        
        self.initialiseoptions(DirectScrolledList)
        self.recordMaxHeight()
        self.scrollTo(0)

    
    def setForceHeight(self):
        self.forceHeight = self['forceHeight']

    
    def recordMaxHeight(self):
        if self.forceHeight is not None:
            self.maxHeight = self.forceHeight
        else:
            self.maxHeight = 0.0
            for item in self['items']:
                if item.__class__.__name__ != 'str':
                    self.maxHeight = max(self.maxHeight, item.getHeight())
                
            

    
    def setScrollSpeed(self):
        self.scrollSpeed = self['scrollSpeed']
        if self.scrollSpeed <= 0:
            self.scrollSpeed = 1
        

    
    def setNumItemsVisible(self):
        self.numItemsVisible = self['numItemsVisible']

    
    def destroy(self):
        taskMgr.remove(self.taskName('scroll'))
        if hasattr(self, 'currentSelected'):
            del self.currentSelected
        
        DirectFrame.destroy(self)

    
    def selectListItem(self, item):
        if hasattr(self, 'currentSelected'):
            self.currentSelected['state'] = NORMAL
        
        item['state'] = DISABLED
        self.currentSelected = item

    
    def scrollBy(self, delta):
        return self.scrollTo(self.index + delta)

    
    def getItemIndexForItemID(self, itemID):
        if len(self['items']) == 0:
            return 0
        
        if type(self['items'][0]) != types.InstanceType:
            print 'warning: getItemIndexForItemID: cant find itemID for non-class list items!'
            return 0
        
        for i in range(len(self['items'])):
            if self['items'][i].itemID == itemID:
                return i
            
        
        print 'warning: getItemIndexForItemID: item not found!'
        return 0

    
    def scrollToItemID(self, itemID, centered = 0):
        self.scrollTo(self.getItemIndexForItemID(itemID), centered)

    
    def scrollTo(self, index, centered = 0):
        numItemsVisible = self['numItemsVisible']
        numItemsTotal = len(self['items'])
        if centered:
            self.index = index - numItemsVisible / 2
        else:
            self.index = index
        if len(self['items']) <= numItemsVisible:
            self.incButton['state'] = DISABLED
            self.decButton['state'] = DISABLED
            self.index = 0
            ret = 0
        elif self.index <= 0:
            self.index = 0
            self.decButton['state'] = DISABLED
            self.incButton['state'] = NORMAL
            ret = 0
        elif self.index >= numItemsTotal - numItemsVisible:
            self.index = numItemsTotal - numItemsVisible
            self.incButton['state'] = DISABLED
            self.decButton['state'] = NORMAL
            ret = 0
        else:
            self.incButton['state'] = NORMAL
            self.decButton['state'] = NORMAL
            ret = 1
        for item in self['items']:
            if item.__class__.__name__ != 'str':
                item.hide()
            
        
        upperRange = min(numItemsTotal, numItemsVisible)
        for i in range(self.index, self.index + upperRange):
            item = self['items'][i]
            if item.__class__.__name__ == 'str':
                if self['itemMakeFunction']:
                    item = apply(self['itemMakeFunction'], (item, i, self['itemMakeExtraArgs']))
                else:
                    item = DirectFrame(text = item, text_align = self['itemsAlign'], text_wordwrap = self['itemsWordwrap'], relief = None)
                self['items'][i] = item
                item.reparentTo(self.itemFrame)
                self.recordMaxHeight()
            
            item.show()
            item.setPos(0, 0, -(i - self.index) * self.maxHeight)
        
        if self['command']:
            apply(self['command'], self['extraArgs'])
        
        return ret

    
    def makeAllItems(self):
        for i in range(len(self['items'])):
            item = self['items'][i]
            print 'Making ' + str(item)
            if item.__class__.__name__ == 'str':
                if self['itemMakeFunction']:
                    item = apply(self['itemMakeFunction'], (item, i, self['itemMakeExtraArgs']))
                else:
                    item = DirectFrame(text = item, text_align = self['itemsAlign'], text_wordwrap = self['itemsWordwrap'], relief = None)
                self['items'][i] = item
                item.reparentTo(self.itemFrame)
            
        
        self.recordMaxHeight()

    
    def _DirectScrolledList__scrollByTask(self, task):
        if task.time - task.prevTime < task.delayTime:
            return Task.cont
        else:
            ret = self.scrollBy(task.delta)
            task.prevTime = task.time
            if ret:
                return Task.cont
            else:
                return Task.done

    
    def _DirectScrolledList__incButtonDown(self, event):
        task = Task.Task(self._DirectScrolledList__scrollByTask)
        task.delayTime = 1.0 / self.scrollSpeed
        task.prevTime = 0.0
        task.delta = 1
        self.scrollBy(task.delta)
        taskMgr.add(task, self.taskName('scroll'))

    
    def _DirectScrolledList__decButtonDown(self, event):
        task = Task.Task(self._DirectScrolledList__scrollByTask)
        task.delayTime = 1.0 / self.scrollSpeed
        task.prevTime = 0.0
        task.delta = -1
        self.scrollBy(task.delta)
        taskMgr.add(task, self.taskName('scroll'))

    
    def _DirectScrolledList__buttonUp(self, event):
        taskMgr.remove(self.taskName('scroll'))

    
    def addItem(self, item, refresh = 1):
        if type(item) == types.InstanceType:
            item.itemID = self.nextItemID
            self.nextItemID += 1
        
        self['items'].append(item)
        if type(item) != type(''):
            item.reparentTo(self.itemFrame)
        
        if refresh:
            self.refresh()
        
        if type(item) == types.InstanceType:
            return item.itemID
        
        return None

    
    def removeItem(self, item, refresh = 1):
        if item in self['items']:
            if hasattr(self, 'currentSelected') and self.currentSelected is item:
                del self.currentSelected
            
            self['items'].remove(item)
            if type(item) != type(''):
                item.reparentTo(hidden)
            
            self.refresh()
            return 1
        else:
            return 0

    
    def refresh(self):
        self.recordMaxHeight()
        self.scrollTo(self.index)

    
    def getSelectedIndex(self):
        return self.index

    
    def getSelectedText(self):
        return self['items'][self.index]['text']


