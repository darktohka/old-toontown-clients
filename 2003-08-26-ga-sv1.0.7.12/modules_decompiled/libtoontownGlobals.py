# File: l (Python 2.2)

import types
import libtoontown
import DSearchPath
import PandaNode
import DNAStorage
import DNAData

def loadDNAFile(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import DNAStorage
        if isinstance(_args[0], DNAStorage.DNAStorage):
            if isinstance(_args[1], types.StringType):
                return __overloaded_loadDNAFile_ptrDNAStorage_atomicstring(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <DNAStorage.DNAStorage> '
    elif numArgs == 3:
        import DNAStorage
        if isinstance(_args[0], DNAStorage.DNAStorage):
            if isinstance(_args[1], types.StringType):
                if isinstance(_args[2], types.IntType):
                    return __overloaded_loadDNAFile_ptrDNAStorage_atomicstring___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <DNAStorage.DNAStorage> '
    elif numArgs == 4:
        import DNAStorage
        if isinstance(_args[0], DNAStorage.DNAStorage):
            if isinstance(_args[1], types.StringType):
                if isinstance(_args[2], types.IntType):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_loadDNAFile_ptrDNAStorage_atomicstring___enum__CoordinateSystem_int(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <DNAStorage.DNAStorage> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '


def loadDNAFileAI(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import DNAStorage
        if isinstance(_args[0], DNAStorage.DNAStorage):
            if isinstance(_args[1], types.StringType):
                return __overloaded_loadDNAFileAI_ptrDNAStorage_atomicstring(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <DNAStorage.DNAStorage> '
    elif numArgs == 3:
        import DNAStorage
        if isinstance(_args[0], DNAStorage.DNAStorage):
            if isinstance(_args[1], types.StringType):
                if isinstance(_args[2], types.IntType):
                    return __overloaded_loadDNAFileAI_ptrDNAStorage_atomicstring___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <DNAStorage.DNAStorage> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


def getDnaPath():
    returnValue = libtoontown._inPet4yutlr()
    import DSearchPath
    returnObject = DSearchPath.DSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def __overloaded_loadDNAFile_ptrDNAStorage_atomicstring___enum__CoordinateSystem_int(dnaStore, filename, cs, editing):
    returnValue = libtoontown._inPet4yr_U1(dnaStore.this, filename, cs, editing)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadDNAFile_ptrDNAStorage_atomicstring___enum__CoordinateSystem(dnaStore, filename, cs):
    returnValue = libtoontown._inPet4y7qN9(dnaStore.this, filename, cs)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadDNAFile_ptrDNAStorage_atomicstring(dnaStore, filename):
    returnValue = libtoontown._inPet4ypfFQ(dnaStore.this, filename)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadDNAFileAI_ptrDNAStorage_atomicstring___enum__CoordinateSystem(dnaStore, filename, cs):
    returnValue = libtoontown._inPet4yxsfU(dnaStore.this, filename, cs)
    import DNAData
    returnObject = DNAData.DNAData(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadDNAFileAI_ptrDNAStorage_atomicstring(dnaStore, filename):
    returnValue = libtoontown._inPet4y2_Um(dnaStore.this, filename)
    import DNAData
    returnObject = DNAData.DNAData(None)
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
