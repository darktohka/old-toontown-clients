# File: S (Python 2.2)

from pandac.PandaModules import *
from direct.gui.DirectGui import *
from SCConstants import *
from direct.interval.IntervalGlobal import *
from SCObject import SCObject
import types

class SCMenu(SCObject, NodePath):
    SpeedChatRolloverTolerance = base.config.GetFloat('speedchat-rollover-tolerance', 0.080000000000000002)
    WantFade = base.config.GetBool('want-speedchat-fade', 0)
    FadeDuration = base.config.GetFloat('speedchat-fade-duration', 0.20000000000000001)
    SerialNum = 0
    BackgroundModelName = None
    GuiModelName = None
    
    def __init__(self, holder = None):
        SCObject.__init__(self)
        self.SerialNum = SCMenu.SerialNum
        SCMenu.SerialNum += 1
        node = hidden.attachNewNode('SCMenu%s' % self.SerialNum)
        NodePath.__init__(self, node)
        self.setHolder(holder)
        self.FinalizeTaskName = 'SCMenu%s_Finalize' % self.SerialNum
        self.ActiveMemberSwitchTaskName = 'SCMenu%s_SwitchActiveMember' % self.SerialNum
        self.bg = loader.loadModelCopy(self.BackgroundModelName)
        
        def findNodes(names, model = self.bg):
            results = []
            for name in names:
                results.append(model.find('**/%s' % name))
            
            return results

        (self.bgTop, self.bgBottom, self.bgLeft, self.bgRight, self.bgMiddle, self.bgTopLeft, self.bgBottomLeft, self.bgTopRight, self.bgBottomRight) = findNodes([
            'top',
            'bottom',
            'left',
            'right',
            'middle',
            'topLeft',
            'bottomLeft',
            'topRight',
            'bottomRight'])
        self.bg.reparentTo(self, -1)
        self._SCMenu__members = []
        self.activeMember = None
        self.activeCandidate = None
        self.fadeIval = None
        self.width = 1
        self.inFinalize = 0

    
    def destroy(self):
        self.stopFade()
        SCObject.destroy(self)
        del self.bgTop
        del self.bgBottom
        del self.bgLeft
        del self.bgRight
        del self.bgMiddle
        del self.bgBottomLeft
        del self.bgTopRight
        del self.bgBottomRight
        self.bg.removeNode()
        del self.bg
        self.holder = None
        for member in self._SCMenu__members:
            member.destroy()
        
        del self._SCMenu__members
        self.removeNode()
        taskMgr.remove(self.FinalizeTaskName)
        taskMgr.remove(self.ActiveMemberSwitchTaskName)

    
    def clearMenu(self):
        while len(self):
            item = self[0]
            del self[0]
            item.destroy()

    
    def rebuildFromStructure(self, structure, title = None):
        self.clearMenu()
        if title:
            holder = self.getHolder()
            if holder:
                holder.setTitle(title)
            
        
        self.appendFromStructure(structure)

    
    def appendFromStructure(self, structure):
        SCMenuHolder = SCMenuHolder
        SCStaticTextTerminal = SCStaticTextTerminal
        import SpeedChatTypes
        OTPLocalizer = OTPLocalizer
        import otp.otpbase
        
        def addChildren(menu, childList):
            for child in childList:
                emote = None
                if type(child) == type({ }):
                    item = child.keys()[0]
                    emote = child[item]
                    child = item
                
                if type(child) == type(0):
                    terminal = SCStaticTextTerminal(child)
                    if emote is not None:
                        terminal.setLinkedEmote(emote)
                    
                    menu.append(terminal)
                elif type(child) == type([]):
                    if type(child[0]) == type(''):
                        holderTitle = child[0]
                        subMenu = SCMenu()
                        subMenuChildren = child[1:]
                    else:
                        (menuType, holderTitle) = (child[0], child[1])
                        subMenu = menuType()
                        subMenuChildren = child[2:]
                    if emote:
                        print 'warning: tried to link emote %s to a menu holder' % emote
                    
                    holder = SCMenuHolder(holderTitle, menu = subMenu)
                    menu.append(holder)
                    addChildren(subMenu, subMenuChildren)
                else:
                    raise 'error parsing speedchat structure. invalid child: %s' % child
            

        addChildren(self, structure)

    
    def fadeFunc(self, t):
        cs = self.getColorScale()
        self.setColorScale(cs[0], cs[1], cs[2], t)

    
    def stopFade(self):
        if self.fadeIval is not None:
            self.fadeIval.pause()
            self.fadeIval = None
        

    
    def enterVisible(self):
        SCObject.enterVisible(self)
        self.privScheduleFinalize()
        for member in self:
            if member.isViewable():
                if not member.isVisible():
                    member.enterVisible()
                
            
        
        self.childHasFaded = 0
        alreadyFaded = 0
        parentMenu = None
        if self.holder is not None:
            if self.holder.parentMenu is not None:
                parentMenu = self.holder.parentMenu
                alreadyFaded = parentMenu.childHasFaded
            
        
        if SCMenu.WantFade:
            if alreadyFaded:
                self.fadeFunc(1.0)
            else:
                self.stopFade()
                self.fadeIval = LerpFunctionInterval(self.fadeFunc, fromData = 0.0, toData = 1.0, duration = SCMenu.FadeDuration)
                self.fadeIval.play()
                if parentMenu is not None:
                    parentMenu.childHasFaded = 1
                
        

    
    def exitVisible(self):
        SCObject.exitVisible(self)
        self.stopFade()
        self.privCancelFinalize()
        self._SCMenu__cancelActiveMemberSwitch()
        self._SCMenu__setActiveMember(None)
        for member in self:
            if member.isVisible():
                member.exitVisible()
            
        

    
    def setHolder(self, holder):
        self.holder = holder

    
    def getHolder(self):
        return self.holder

    
    def isTopLevel(self):
        return self.holder == None

    
    def memberSelected(self, member):
        self._SCMenu__cancelActiveMemberSwitch()
        self._SCMenu__setActiveMember(member)

    
    def _SCMenu__setActiveMember(self, member):
        if self.activeMember is member:
            return None
        
        if self.activeMember is not None:
            self.activeMember.exitActive()
        
        self.activeMember = member
        if self.activeMember is not None:
            self.activeMember.reparentTo(self)
            self.activeMember.enterActive()
        

    
    def memberGainedInputFocus(self, member):
        self._SCMenu__cancelActiveMemberSwitch()
        if member is self.activeMember:
            return None
        
        if self.activeMember is None and SCMenu.SpeedChatRolloverTolerance == 0 or member.posInParentMenu < self.activeMember.posInParentMenu:
            self._SCMenu__setActiveMember(member)
        else:
            
            def doActiveMemberSwitch(task, self = self, member = member):
                self.activeCandidate = None
                self._SCMenu__setActiveMember(member)
                return Task.done

            minFrameRate = 1.0 / SCMenu.SpeedChatRolloverTolerance
            if globalClock.getAverageFrameRate() > minFrameRate:
                taskMgr.doMethodLater(SCMenu.SpeedChatRolloverTolerance, doActiveMemberSwitch, self.ActiveMemberSwitchTaskName)
                self.activeCandidate = member
            else:
                self._SCMenu__setActiveMember(member)

    
    def _SCMenu__cancelActiveMemberSwitch(self):
        taskMgr.remove(self.ActiveMemberSwitchTaskName)
        self.activeCandidate = None

    
    def memberLostInputFocus(self, member):
        if member is self.activeCandidate:
            self._SCMenu__cancelActiveMemberSwitch()
        
        if member is not self.activeMember:
            pass
        1
        if not member.hasStickyFocus():
            self._SCMenu__setActiveMember(None)
        

    
    def memberViewabilityChanged(self, member):
        self.invalidate()

    
    def invalidate(self):
        SCObject.invalidate(self)
        if self.isVisible():
            self.privScheduleFinalize()
        

    
    def privScheduleFinalize(self):
        
        def finalizeMenu(task, self = self):
            self.finalize()
            return Task.done

        taskMgr.remove(self.FinalizeTaskName)
        taskMgr.add(finalizeMenu, self.FinalizeTaskName, priority = SCMenuFinalizePriority)

    
    def privCancelFinalize(self):
        taskMgr.remove(self.FinalizeTaskName)

    
    def isFinalizing(self):
        return self.inFinalize

    
    def finalize(self):
        if not self.isDirty():
            return None
        
        self.inFinalize = 1
        SCObject.finalize(self)
        visibleMembers = []
        for member in self:
            if member.isViewable():
                visibleMembers.append(member)
                member.reparentTo(self)
            else:
                member.reparentTo(hidden)
                if self.activeMember is member:
                    self._SCMenu__setActiveMember(None)
                
        
        maxWidth = 0.0
        maxHeight = 0.0
        for member in visibleMembers:
            (width, height) = member.getMinDimensions()
            maxWidth = max(maxWidth, width)
            maxHeight = max(maxHeight, height)
        
        holder = self.getHolder()
        if holder is not None:
            widthToCover = holder.getMinSubmenuWidth()
            maxWidth = max(maxWidth, widthToCover)
        
        (memberWidth, memberHeight) = (maxWidth, maxHeight)
        self.width = maxWidth
        for i in xrange(len(visibleMembers)):
            member = visibleMembers[i]
            member.setPos(0, 0, -i * maxHeight)
            member.setDimensions(memberWidth, memberHeight)
            member.finalize()
        
        sX = memberWidth
        sZ = memberHeight * len(visibleMembers)
        self.bgMiddle.setScale(sX, 1, sZ)
        self.bgTop.setScale(sX, 1, 1)
        self.bgBottom.setScale(sX, 1, 1)
        self.bgLeft.setScale(1, 1, sZ)
        self.bgRight.setScale(1, 1, sZ)
        self.bgBottomLeft.setZ(-sZ)
        self.bgBottom.setZ(-sZ)
        self.bgTopRight.setX(sX)
        self.bgRight.setX(sX)
        self.bgBottomRight.setX(sX)
        self.bgBottomRight.setZ(-sZ)
        sB = 0.14999999999999999
        self.bgTopLeft.setSx(aspect2d, sB)
        self.bgTopLeft.setSz(aspect2d, sB)
        self.bgBottomRight.setSx(aspect2d, sB)
        self.bgBottomRight.setSz(aspect2d, sB)
        self.bgBottomLeft.setSx(aspect2d, sB)
        self.bgBottomLeft.setSz(aspect2d, sB)
        self.bgTopRight.setSx(aspect2d, sB)
        self.bgTopRight.setSz(aspect2d, sB)
        self.bgTop.setSz(aspect2d, sB)
        self.bgBottom.setSz(aspect2d, sB)
        self.bgLeft.setSx(aspect2d, sB)
        self.bgRight.setSx(aspect2d, sB)
        (r, g, b) = self.getColorScheme().getFrameColor()
        a = self.getColorScheme().getAlpha()
        self.bg.setColorScale(r, g, b, a)
        if self.activeMember is not None:
            self.activeMember.reparentTo(self)
        
        self.validate()
        self.inFinalize = 0

    
    def append(self, element):
        if isinstance(self._SCMenu__members, types.TupleType):
            self._SCMenu__members = list(self._SCMenu__members)
        
        self._SCMenu__members.append(element)
        self.privMemberListChanged(added = [
            element])

    
    def extend(self, elements):
        self += elements

    
    def index(self, element):
        return self._SCMenu__members.index(element)

    
    def __len__(self):
        return len(self._SCMenu__members)

    
    def __getitem__(self, index):
        return self._SCMenu__members[index]

    
    def __setitem__(self, index, value):
        if isinstance(self._SCMenu__members, types.TupleType):
            self._SCMenu__members = list(self._SCMenu__members)
        
        removedMember = self._SCMenu__members[index]
        self._SCMenu__members[index] = value
        self.privMemberListChanged(added = [
            value], removed = [
            removedMember])

    
    def __delitem__(self, index):
        if isinstance(self._SCMenu__members, types.TupleType):
            self._SCMenu__members = list(self._SCMenu__members)
        
        removedMember = self._SCMenu__members[index]
        del self._SCMenu__members[index]
        self.privMemberListChanged(removed = [
            removedMember])

    
    def __getslice__(self, i, j):
        if isinstance(self._SCMenu__members, types.TupleType):
            self._SCMenu__members = list(self._SCMenu__members)
        
        return self._SCMenu__members[i:j]

    
    def __setslice__(self, i, j, s):
        if isinstance(self._SCMenu__members, types.TupleType):
            self._SCMenu__members = list(self._SCMenu__members)
        
        removedMembers = self._SCMenu__members[i:j]
        self._SCMenu__members[i:j] = list(s)
        self.privMemberListChanged(added = list(s), removed = removedMembers)

    
    def __delslice__(self, i, j):
        if isinstance(self._SCMenu__members, types.TupleType):
            self._SCMenu__members = list(self._SCMenu__members)
        
        removedMembers = self._SCMenu__members[i:j]
        del self._SCMenu__members[i:j]
        self.privMemberListChanged(removed = removedMembers)

    
    def __iadd__(self, other):
        if isinstance(self._SCMenu__members, types.TupleType):
            self._SCMenu__members = list(self._SCMenu__members)
        
        if isinstance(other, SCMenu):
            otherMenu = other
            other = otherMenu._SCMenu__members
            del otherMenu[:]
        
        self._SCMenu__members += list(other)
        self.privMemberListChanged(added = list(other))
        return self

    
    def privMemberListChanged(self, added = None, removed = None):
        if removed is not None:
            for element in removed:
                if element is self.activeMember:
                    self._SCMenu__setActiveMember(None)
                
                if element.getParentMenu() is self:
                    if element.isVisible():
                        element.exitVisible()
                    
                    element.setParentMenu(None)
                    element.reparentTo(hidden)
                
            
        
        if added is not None:
            for element in added:
                self.privAdoptSCObject(element)
                element.setParentMenu(self)
            
        
        if self.holder is not None:
            self.holder.updateViewability()
        
        for i in range(len(self._SCMenu__members)):
            self._SCMenu__members[i].posInParentMenu = i
        
        self.invalidate()

    
    def privSetSettingsRef(self, settingsRef):
        SCObject.privSetSettingsRef(self, settingsRef)
        for member in self:
            member.privSetSettingsRef(settingsRef)
        

    
    def invalidateAll(self):
        SCObject.invalidateAll(self)
        for member in self:
            member.invalidateAll()
        

    
    def finalizeAll(self):
        SCObject.finalizeAll(self)
        for member in self:
            member.finalizeAll()
        

    
    def getWidth(self):
        return self.width

    
    def __str__(self):
        return '%s: menu%s' % (self.__class__.__name__, self.SerialNum)


