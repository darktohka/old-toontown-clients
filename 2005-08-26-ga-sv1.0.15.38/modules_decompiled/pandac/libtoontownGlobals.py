# File: l (Python 2.2)

import types
import libtoontown
import ConfigVariableSearchPath
import PandaNode
import DNAStorage
import DNAData
import HTTPClient

def loadDNAFile(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        return __overloaded_loadDNAFile_ptrDNAStorage_atomicstring(*_args)
    elif numArgs == 3:
        return __overloaded_loadDNAFile_ptrDNAStorage_atomicstring___enum__CoordinateSystem(*_args)
    elif numArgs == 4:
        return __overloaded_loadDNAFile_ptrDNAStorage_atomicstring___enum__CoordinateSystem_int(*_args)
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '


def loadDNAFileAI(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        return __overloaded_loadDNAFileAI_ptrDNAStorage_atomicstring(*_args)
    elif numArgs == 3:
        return __overloaded_loadDNAFileAI_ptrDNAStorage_atomicstring___enum__CoordinateSystem(*_args)
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


def getDnaPath():
    returnValue = libtoontown._inPdt4yvtlr()
    import ConfigVariableSearchPath
    returnObject = ConfigVariableSearchPath.ConfigVariableSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def __overloaded_loadDNAFile_ptrDNAStorage_atomicstring___enum__CoordinateSystem_int(dnaStore, filename, cs, editing):
    returnValue = libtoontown._inPdt4yq_U1(dnaStore.this, filename, cs, editing)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadDNAFile_ptrDNAStorage_atomicstring___enum__CoordinateSystem(dnaStore, filename, cs):
    returnValue = libtoontown._inPdt4y4qN9(dnaStore.this, filename, cs)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadDNAFile_ptrDNAStorage_atomicstring(dnaStore, filename):
    returnValue = libtoontown._inPdt4ypfFQ(dnaStore.this, filename)
    import PandaNode
    returnObject = PandaNode.PandaNode(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadDNAFileAI_ptrDNAStorage_atomicstring___enum__CoordinateSystem(dnaStore, filename, cs):
    returnValue = libtoontown._inPdt4yxsfU(dnaStore.this, filename, cs)
    import DNAData
    returnObject = DNAData.DNAData(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def __overloaded_loadDNAFileAI_ptrDNAStorage_atomicstring(dnaStore, filename):
    returnValue = libtoontown._inPdt4y3_Um(dnaStore.this, filename)
    import DNAData
    returnObject = DNAData.DNAData(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def prepareAvatar(http):
    returnValue = libtoontown._inPw_HEnYec(http.this)
    return returnValue

HCCUT = 1
HCFREE = 2
HCG1 = 3
HCSMOOTH = 4
PCTHPR = 2
PCTNONE = 0
PCTT = 3
PCTXYZ = 1
