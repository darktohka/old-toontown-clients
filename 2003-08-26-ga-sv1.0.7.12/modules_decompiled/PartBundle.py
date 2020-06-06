# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PartGroup
import AnimControlCollection

class PartBundle(PartGroup.PartGroup, AnimControlCollection.AnimControlCollection, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    BTNormalizedLinear = 2
    BTSingle = 0
    BTLinear = 1
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPn9gMB9Ou:
            libpanda._inPn9gMB9Ou(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPn9gM7Q2E()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setBlendType(self, bt):
        returnValue = libpanda._inPn9gM0WPI(self.this, bt)
        return returnValue

    
    def getBlendType(self):
        returnValue = libpanda._inPn9gMyXKU(self.this)
        return returnValue

    
    def getNode(self):
        returnValue = libpanda._inPn9gMwx2U(self.this)
        import PartBundleNode
        returnObject = PartBundleNode.PartBundleNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def clearControlEffects(self):
        returnValue = libpanda._inPn9gMXSiY(self.this)
        return returnValue

    
    def setControlEffect(self, control, effect):
        returnValue = libpanda._inPn9gMc9Oe(self.this, control.this, effect)
        return returnValue

    
    def getControlEffect(self, control):
        returnValue = libpanda._inPn9gMFYhs(self.this, control.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPn9gMGRkL(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPn9gMAA1u(self.this, out.this, indentLevel)
        return returnValue

    
    def _PartBundle__overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_atomicstring_int(self, anim, name, hierarchyMatchFlags):
        returnValue = libpanda._inPn9gMiKUy(self.this, anim.this, name, hierarchyMatchFlags)
        return returnValue

    
    def _PartBundle__overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_atomicstring(self, anim, name):
        returnValue = libpanda._inPn9gMYNTE(self.this, anim.this, name)
        return returnValue

    
    def _PartBundle__overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_int(self, anim, hierarchyMatchFlags):
        returnValue = libpanda._inPn9gM9D6Q(self.this, anim.this, hierarchyMatchFlags)
        import AnimControl
        returnObject = AnimControl.AnimControl(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _PartBundle__overloaded_bindAnim_ptrPartBundle_ptrAnimBundle(self, anim):
        returnValue = libpanda._inPn9gMdsSx(self.this, anim.this)
        import AnimControl
        returnObject = AnimControl.AnimControl(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def upcastToAnimControlCollection(self):
        returnValue = libpanda._inPn9gMi45Z(self.this)
        import AnimControlCollection
        returnObject = AnimControlCollection.AnimControlCollection(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumChildren(self):
        upcastSelf = self
        returnValue = libpanda._inPn9gM3fp4(upcastSelf.this)
        return returnValue

    
    def getChild(self, n):
        upcastSelf = self
        returnValue = libpanda._inPn9gMMhIO(upcastSelf.this, n)
        import PartGroup
        returnObject = PartGroup.PartGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findChild(self, name):
        upcastSelf = self
        returnValue = libpanda._inPn9gM9aSh(upcastSelf.this, name)
        import PartGroup
        returnObject = PartGroup.PartGroup(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def writeWithValue(self, out, indentLevel):
        upcastSelf = self
        returnValue = libpanda._inPn9gM6PSE(upcastSelf.this, out.this, indentLevel)
        return returnValue

    
    def upcastToNamable(self):
        upcastSelf = self
        returnValue = libpanda._inPn9gMHyTs(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpanda._inPelbolcf_(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtmFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtkXzz(upcastSelf.this, handle.this)
        return returnValue

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtM11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtVS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtzyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtupj2(upcastSelf.this)
        return returnValue

    
    def assign(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtp1bI(upcastSelf.this, other.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setName(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtLNBW(upcastSelf.this, name)
        return returnValue

    
    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtavUl(upcastSelf.this)
        return returnValue

    
    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtYjhC(upcastSelf.this)
        return returnValue

    
    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtfARN(upcastSelf.this)
        return returnValue

    
    def storeAnim(self, control, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMGmt2(upcastSelf.this, control.this, name)
        return returnValue

    
    def findAnim(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMDivI(upcastSelf.this, name)
        import AnimControl
        returnObject = AnimControl.AnimControl(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def unbindAnim(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMd9bu(upcastSelf.this, name)
        return returnValue

    
    def getNumAnims(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMpONk(upcastSelf.this)
        return returnValue

    
    def clearAnims(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMNiLN(upcastSelf.this)
        return returnValue

    
    def setStopEvent(self, stopEvent):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMx4vI(upcastSelf.this, stopEvent.this)
        return returnValue

    
    def clearStopEvent(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMlSKm(upcastSelf.this)
        return returnValue

    
    def hasStopEvent(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gM26tA(upcastSelf.this)
        return returnValue

    
    def getStopEvent(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMWoZz(upcastSelf.this)
        import Event
        returnObject = Event.Event(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _PartBundle__overloaded_play_ptrAnimControlCollection_atomicstring(self, animName):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMUNjN(upcastSelf.this, animName)
        return returnValue

    
    def _PartBundle__overloaded_play_ptrAnimControlCollection_atomicstring_int_int(self, animName, _from, to):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMxGRl(upcastSelf.this, animName, _from, to)
        return returnValue

    
    def _PartBundle__overloaded_loop_ptrAnimControlCollection_atomicstring_bool(self, animName, restart):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMBJEH(upcastSelf.this, animName, restart)
        return returnValue

    
    def _PartBundle__overloaded_loop_ptrAnimControlCollection_atomicstring_bool_int_int(self, animName, restart, _from, to):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMSOG2(upcastSelf.this, animName, restart, _from, to)
        return returnValue

    
    def stop(self, animName):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMunhQ(upcastSelf.this, animName)
        return returnValue

    
    def pose(self, animName, frame):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMmA9Z(upcastSelf.this, animName, frame)
        return returnValue

    
    def _PartBundle__overloaded_playAll_ptrAnimControlCollection(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMuiz5(upcastSelf.this)
        return returnValue

    
    def _PartBundle__overloaded_playAll_ptrAnimControlCollection_int_int(self, _from, to):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMc5qb(upcastSelf.this, _from, to)
        return returnValue

    
    def _PartBundle__overloaded_loopAll_ptrAnimControlCollection_bool(self, restart):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMNeO5(upcastSelf.this, restart)
        return returnValue

    
    def _PartBundle__overloaded_loopAll_ptrAnimControlCollection_bool_int_int(self, restart, _from, to):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMOl09(upcastSelf.this, restart, _from, to)
        return returnValue

    
    def stopAll(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMYUx8(upcastSelf.this)
        return returnValue

    
    def poseAll(self, frame):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMKter(upcastSelf.this, frame)
        return returnValue

    
    def _PartBundle__overloaded_getFrame_ptrConstAnimControlCollection(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMhXpY(upcastSelf.this)
        return returnValue

    
    def _PartBundle__overloaded_getFrame_ptrConstAnimControlCollection_atomicstring(self, animName):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gM7Cy2(upcastSelf.this, animName)
        return returnValue

    
    def getNumFrames(self, animName):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMvkKP(upcastSelf.this, animName)
        return returnValue

    
    def _PartBundle__overloaded_isPlaying_ptrConstAnimControlCollection(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gM5Fhs(upcastSelf.this)
        return returnValue

    
    def _PartBundle__overloaded_isPlaying_ptrConstAnimControlCollection_atomicstring(self, animName):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMne5y(upcastSelf.this, animName)
        return returnValue

    
    def whichAnimPlaying(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToAnimControlCollection()
        returnValue = libpanda._inPn9gMBIcV(upcastSelf.this)
        return returnValue

    
    def play(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._PartBundle__overloaded_play_ptrAnimControlCollection_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._PartBundle__overloaded_play_ptrAnimControlCollection_atomicstring_int_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def isPlaying(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PartBundle__overloaded_isPlaying_ptrConstAnimControlCollection()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._PartBundle__overloaded_isPlaying_ptrConstAnimControlCollection_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def playAll(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PartBundle__overloaded_playAll_ptrAnimControlCollection()
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._PartBundle__overloaded_playAll_ptrAnimControlCollection_int_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '

    
    def loopAll(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._PartBundle__overloaded_loopAll_ptrAnimControlCollection_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._PartBundle__overloaded_loopAll_ptrAnimControlCollection_bool_int_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def getFrame(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PartBundle__overloaded_getFrame_ptrConstAnimControlCollection()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._PartBundle__overloaded_getFrame_ptrConstAnimControlCollection_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def loop(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._PartBundle__overloaded_loop_ptrAnimControlCollection_atomicstring_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.IntType):
                            return self._PartBundle__overloaded_loop_ptrAnimControlCollection_atomicstring_bool_int_int(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

    
    def bindAnim(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import AnimBundle
            if isinstance(_args[0], AnimBundle.AnimBundle):
                return self._PartBundle__overloaded_bindAnim_ptrPartBundle_ptrAnimBundle(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <AnimBundle.AnimBundle> '
        elif numArgs == 2:
            import AnimBundle
            if isinstance(_args[0], AnimBundle.AnimBundle):
                if isinstance(_args[1], types.IntType):
                    return self._PartBundle__overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_int(_args[0], _args[1])
                elif isinstance(_args[1], types.StringType):
                    return self._PartBundle__overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <AnimBundle.AnimBundle> '
        elif numArgs == 3:
            import AnimBundle
            if isinstance(_args[0], AnimBundle.AnimBundle):
                if isinstance(_args[1], types.StringType):
                    if isinstance(_args[2], types.IntType):
                        return self._PartBundle__overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_atomicstring_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <AnimBundle.AnimBundle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '


