# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class AnimControlCollection(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPn9gMEVyR()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPn9gMjmCm:
            libpanda._inPn9gMjmCm(self.this)
        

    
    def storeAnim(self, control, name):
        returnValue = libpanda._inPn9gMGmt2(self.this, control.this, name)
        return returnValue

    
    def findAnim(self, name):
        returnValue = libpanda._inPn9gMDivI(self.this, name)
        import AnimControl
        returnObject = AnimControl.AnimControl(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def unbindAnim(self, name):
        returnValue = libpanda._inPn9gMd9bu(self.this, name)
        return returnValue

    
    def getNumAnims(self):
        returnValue = libpanda._inPn9gMpONk(self.this)
        return returnValue

    
    def clearAnims(self):
        returnValue = libpanda._inPn9gMNiLN(self.this)
        return returnValue

    
    def setStopEvent(self, stopEvent):
        returnValue = libpanda._inPn9gMx4vI(self.this, stopEvent.this)
        return returnValue

    
    def clearStopEvent(self):
        returnValue = libpanda._inPn9gMlSKm(self.this)
        return returnValue

    
    def hasStopEvent(self):
        returnValue = libpanda._inPn9gM26tA(self.this)
        return returnValue

    
    def getStopEvent(self):
        returnValue = libpanda._inPn9gMWoZz(self.this)
        import Event
        returnObject = Event.Event(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _AnimControlCollection__overloaded_play_ptrAnimControlCollection_atomicstring(self, animName):
        returnValue = libpanda._inPn9gMUNjN(self.this, animName)
        return returnValue

    
    def _AnimControlCollection__overloaded_play_ptrAnimControlCollection_atomicstring_int_int(self, animName, _from, to):
        returnValue = libpanda._inPn9gMxGRl(self.this, animName, _from, to)
        return returnValue

    
    def _AnimControlCollection__overloaded_loop_ptrAnimControlCollection_atomicstring_bool(self, animName, restart):
        returnValue = libpanda._inPn9gMBJEH(self.this, animName, restart)
        return returnValue

    
    def _AnimControlCollection__overloaded_loop_ptrAnimControlCollection_atomicstring_bool_int_int(self, animName, restart, _from, to):
        returnValue = libpanda._inPn9gMSOG2(self.this, animName, restart, _from, to)
        return returnValue

    
    def stop(self, animName):
        returnValue = libpanda._inPn9gMunhQ(self.this, animName)
        return returnValue

    
    def pose(self, animName, frame):
        returnValue = libpanda._inPn9gMmA9Z(self.this, animName, frame)
        return returnValue

    
    def _AnimControlCollection__overloaded_playAll_ptrAnimControlCollection(self):
        returnValue = libpanda._inPn9gMuiz5(self.this)
        return returnValue

    
    def _AnimControlCollection__overloaded_playAll_ptrAnimControlCollection_int_int(self, _from, to):
        returnValue = libpanda._inPn9gMc5qb(self.this, _from, to)
        return returnValue

    
    def _AnimControlCollection__overloaded_loopAll_ptrAnimControlCollection_bool(self, restart):
        returnValue = libpanda._inPn9gMNeO5(self.this, restart)
        return returnValue

    
    def _AnimControlCollection__overloaded_loopAll_ptrAnimControlCollection_bool_int_int(self, restart, _from, to):
        returnValue = libpanda._inPn9gMOl09(self.this, restart, _from, to)
        return returnValue

    
    def stopAll(self):
        returnValue = libpanda._inPn9gMYUx8(self.this)
        return returnValue

    
    def poseAll(self, frame):
        returnValue = libpanda._inPn9gMKter(self.this, frame)
        return returnValue

    
    def _AnimControlCollection__overloaded_getFrame_ptrConstAnimControlCollection(self):
        returnValue = libpanda._inPn9gMhXpY(self.this)
        return returnValue

    
    def _AnimControlCollection__overloaded_getFrame_ptrConstAnimControlCollection_atomicstring(self, animName):
        returnValue = libpanda._inPn9gM7Cy2(self.this, animName)
        return returnValue

    
    def getNumFrames(self, animName):
        returnValue = libpanda._inPn9gMvkKP(self.this, animName)
        return returnValue

    
    def _AnimControlCollection__overloaded_isPlaying_ptrConstAnimControlCollection(self):
        returnValue = libpanda._inPn9gM5Fhs(self.this)
        return returnValue

    
    def _AnimControlCollection__overloaded_isPlaying_ptrConstAnimControlCollection_atomicstring(self, animName):
        returnValue = libpanda._inPn9gMne5y(self.this, animName)
        return returnValue

    
    def whichAnimPlaying(self):
        returnValue = libpanda._inPn9gMBIcV(self.this)
        return returnValue

    
    def play(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._AnimControlCollection__overloaded_play_ptrAnimControlCollection_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._AnimControlCollection__overloaded_play_ptrAnimControlCollection_atomicstring_int_int(_args[0], _args[1], _args[2])
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
            return self._AnimControlCollection__overloaded_isPlaying_ptrConstAnimControlCollection()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._AnimControlCollection__overloaded_isPlaying_ptrConstAnimControlCollection_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def playAll(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AnimControlCollection__overloaded_playAll_ptrAnimControlCollection()
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._AnimControlCollection__overloaded_playAll_ptrAnimControlCollection_int_int(_args[0], _args[1])
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
                return self._AnimControlCollection__overloaded_loopAll_ptrAnimControlCollection_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._AnimControlCollection__overloaded_loopAll_ptrAnimControlCollection_bool_int_int(_args[0], _args[1], _args[2])
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
            return self._AnimControlCollection__overloaded_getFrame_ptrConstAnimControlCollection()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._AnimControlCollection__overloaded_getFrame_ptrConstAnimControlCollection_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def loop(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._AnimControlCollection__overloaded_loop_ptrAnimControlCollection_atomicstring_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.IntType):
                            return self._AnimControlCollection__overloaded_loop_ptrAnimControlCollection_atomicstring_bool_int_int(_args[0], _args[1], _args[2], _args[3])
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


