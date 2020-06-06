# File: l (Python 2.2)

import types
import libpandaegg
import PandaNode
import EggData

def loadEggData(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        return __overloaded_loadEggData_ptrEggData(*_args)
    elif numArgs == 2:
        return __overloaded_loadEggData_ptrEggData___enum__CoordinateSystem(*_args)
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


def loadEggFile(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        return __overloaded_loadEggFile_atomicstring(*_args)
    elif numArgs == 2:
        return __overloaded_loadEggFile_atomicstring___enum__CoordinateSystem(*_args)
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


def __overloaded_loadEggFile_atomicstring___enum__CoordinateSystem(filename, cs):
    returnValue = libpandaegg._inP9UozB_T_(filename, cs)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadEggFile_atomicstring(filename):
    returnValue = libpandaegg._inP9UozsvmK(filename)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadEggData_ptrEggData___enum__CoordinateSystem(data, cs):
    returnValue = libpandaegg._inP9UozJ5SD(data.this, cs)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadEggData_ptrEggData(data):
    returnValue = libpandaegg._inP9Uozf56f(data.this)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()

HCCUT = 1
HCFREE = 2
HCG1 = 3
HCSMOOTH = 4
PCTHPR = 2
PCTNONE = 0
PCTT = 3
PCTXYZ = 1
