# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VirtualFile

class HTTPChannel(VirtualFile.VirtualFile, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
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
        

    
    def getClassType():
        returnValue = libpandaexpress._inP2KOdf2x8()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isValid(self):
        returnValue = libpandaexpress._inP2KOdWoes(self.this)
        return returnValue

    
    def isConnectionReady(self):
        returnValue = libpandaexpress._inP2KOdmmy8(self.this)
        return returnValue

    
    def getUrl(self):
        returnValue = libpandaexpress._inP2KOd_XTe(self.this)
        import URLSpec
        returnObject = URLSpec.URLSpec(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getHttpVersion(self):
        returnValue = libpandaexpress._inP2KOdGji4(self.this)
        return returnValue

    
    def getHttpVersionString(self):
        returnValue = libpandaexpress._inP2KOd8qBF(self.this)
        return returnValue

    
    def getStatusCode(self):
        returnValue = libpandaexpress._inP2KOdd4Hd(self.this)
        return returnValue

    
    def getStatusString(self):
        returnValue = libpandaexpress._inP2KOdvrvb(self.this)
        return returnValue

    
    def getWwwRealm(self):
        returnValue = libpandaexpress._inP2KOdHxhf(self.this)
        return returnValue

    
    def getProxyRealm(self):
        returnValue = libpandaexpress._inP2KOd8j1e(self.this)
        return returnValue

    
    def getRedirect(self):
        returnValue = libpandaexpress._inP2KOd2aFd(self.this)
        import URLSpec
        returnObject = URLSpec.URLSpec(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getHeaderValue(self, key):
        returnValue = libpandaexpress._inP2KOdsfPw(self.this, key)
        return returnValue

    
    def setPersistentConnection(self, persistentConnection):
        returnValue = libpandaexpress._inP2KOdc944(self.this, persistentConnection)
        return returnValue

    
    def getPersistentConnection(self):
        returnValue = libpandaexpress._inP2KOdhWP3(self.this)
        return returnValue

    
    def setConnectTimeout(self, timeoutSeconds):
        returnValue = libpandaexpress._inP2KOdg_Dp(self.this, timeoutSeconds)
        return returnValue

    
    def getConnectTimeout(self):
        returnValue = libpandaexpress._inP2KOdR14O(self.this)
        return returnValue

    
    def setBlockingConnect(self, blockingConnect):
        returnValue = libpandaexpress._inP2KOdDZOE(self.this, blockingConnect)
        return returnValue

    
    def getBlockingConnect(self):
        returnValue = libpandaexpress._inP2KOdmdZu(self.this)
        return returnValue

    
    def setDownloadThrottle(self, downloadThrottle):
        returnValue = libpandaexpress._inP2KOdFJnS(self.this, downloadThrottle)
        return returnValue

    
    def getDownloadThrottle(self):
        returnValue = libpandaexpress._inP2KOdrGLu(self.this)
        return returnValue

    
    def setMaxBytesPerSecond(self, maxBytesPerSecond):
        returnValue = libpandaexpress._inP2KOdqw0a(self.this, maxBytesPerSecond)
        return returnValue

    
    def getMaxBytesPerSecond(self):
        returnValue = libpandaexpress._inP2KOdi_cQ(self.this)
        return returnValue

    
    def setMaxUpdatesPerSecond(self, maxUpdatesPerSecond):
        returnValue = libpandaexpress._inP2KOd5shL(self.this, maxUpdatesPerSecond)
        return returnValue

    
    def getMaxUpdatesPerSecond(self):
        returnValue = libpandaexpress._inP2KOdHMcA(self.this)
        return returnValue

    
    def getFileSize(self):
        returnValue = libpandaexpress._inP2KOdsNiH(self.this)
        return returnValue

    
    def writeHeaders(self, out):
        returnValue = libpandaexpress._inP2KOdN8ab(self.this, out.this)
        return returnValue

    
    def reset(self):
        returnValue = libpandaexpress._inP2KOdIvGa(self.this)
        return returnValue

    
    def clearExtraHeaders(self):
        returnValue = libpandaexpress._inP2KOdAzJt(self.this)
        return returnValue

    
    def sendExtraHeader(self, key, value):
        returnValue = libpandaexpress._inP2KOddFsV(self.this, key, value)
        return returnValue

    
    def getDocument(self, url):
        returnValue = libpandaexpress._inP2KOdkTtg(self.this, url.this)
        return returnValue

    
    def getSubdocument(self, url, firstByte, lastByte):
        returnValue = libpandaexpress._inP2KOdhfE8(self.this, url.this, firstByte, lastByte)
        return returnValue

    
    def getHeader(self, url):
        returnValue = libpandaexpress._inP2KOdd_VQ(self.this, url.this)
        return returnValue

    
    def postForm(self, url, body):
        returnValue = libpandaexpress._inP2KOdUAm6(self.this, url.this, body)
        return returnValue

    
    def putDocument(self, url, body):
        returnValue = libpandaexpress._inP2KOdkt00(self.this, url.this, body)
        return returnValue

    
    def deleteDocument(self, url):
        returnValue = libpandaexpress._inP2KOdi7T9(self.this, url.this)
        return returnValue

    
    def getTrace(self, url):
        returnValue = libpandaexpress._inP2KOdN3h1(self.this, url.this)
        return returnValue

    
    def connectTo(self, url):
        returnValue = libpandaexpress._inP2KOdE81P(self.this, url.this)
        return returnValue

    
    def beginGetDocument(self, url):
        returnValue = libpandaexpress._inP2KOdh_lN(self.this, url.this)
        return returnValue

    
    def beginGetSubdocument(self, url, firstByte, lastByte):
        returnValue = libpandaexpress._inP2KOdKPUp(self.this, url.this, firstByte, lastByte)
        return returnValue

    
    def beginGetHeader(self, url):
        returnValue = libpandaexpress._inP2KOdsR0z(self.this, url.this)
        return returnValue

    
    def beginPostForm(self, url, body):
        returnValue = libpandaexpress._inP2KOdZfvL(self.this, url.this, body)
        return returnValue

    
    def run(self):
        returnValue = libpandaexpress._inP2KOdU81y(self.this)
        return returnValue

    
    def beginConnectTo(self, url):
        returnValue = libpandaexpress._inP2KOdvm0T(self.this, url.this)
        return returnValue

    
    def readBody(self):
        returnValue = libpandaexpress._inP2KOdO1_j(self.this)
        import ISocketStream
        returnObject = ISocketStream.ISocketStream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _HTTPChannel__overloaded_downloadToFile_ptrHTTPChannel_ptrConstFilename_bool(self, filename, subdocumentResumes):
        returnValue = libpandaexpress._inP2KOdPbQV(self.this, filename.this, subdocumentResumes)
        return returnValue

    
    def _HTTPChannel__overloaded_downloadToFile_ptrHTTPChannel_ptrConstFilename(self, filename):
        returnValue = libpandaexpress._inP2KOdKhGP(self.this, filename.this)
        return returnValue

    
    def _HTTPChannel__overloaded_downloadToRam_ptrHTTPChannel_ptrRamfile_bool(self, ramfile, subdocumentResumes):
        returnValue = libpandaexpress._inP2KOdovIW(self.this, ramfile.this, subdocumentResumes)
        return returnValue

    
    def _HTTPChannel__overloaded_downloadToRam_ptrHTTPChannel_ptrRamfile(self, ramfile):
        returnValue = libpandaexpress._inP2KOdlZ_P(self.this, ramfile.this)
        return returnValue

    
    def getConnection(self):
        returnValue = libpandaexpress._inP2KOdQUR4(self.this)
        import SocketStream
        returnObject = SocketStream.SocketStream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getBytesDownloaded(self):
        returnValue = libpandaexpress._inP2KOdH2KX(self.this)
        return returnValue

    
    def getBytesRequested(self):
        returnValue = libpandaexpress._inP2KOdxOVm(self.this)
        return returnValue

    
    def isDownloadComplete(self):
        returnValue = libpandaexpress._inP2KOdXuSB(self.this)
        return returnValue

    
    def downloadToRam(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ramfile
            if isinstance(_args[0], Ramfile.Ramfile):
                return self._HTTPChannel__overloaded_downloadToRam_ptrHTTPChannel_ptrRamfile(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ramfile.Ramfile> '
        elif numArgs == 2:
            import Ramfile
            if isinstance(_args[0], Ramfile.Ramfile):
                if isinstance(_args[1], types.IntType):
                    return self._HTTPChannel__overloaded_downloadToRam_ptrHTTPChannel_ptrRamfile_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ramfile.Ramfile> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def downloadToFile(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                return self._HTTPChannel__overloaded_downloadToFile_ptrHTTPChannel_ptrConstFilename(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        elif numArgs == 2:
            import Filename
            if isinstance(_args[0], Filename.Filename):
                if isinstance(_args[1], types.IntType):
                    return self._HTTPChannel__overloaded_downloadToFile_ptrHTTPChannel_ptrConstFilename_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def spawnTask(self, name = None, callback = None, extraArgs = []):
        if not name:
            name = self.getUrl().cStr()
        
        import Task
        task = Task.Task(self.doTask)
        task.callback = callback
        task.extraArgs = extraArgs
        return taskMgr.add(task, name)

    
    def doTask(self, task):
        import Task
        if self.run():
            return Task.cont
        
        if task.callback:
            task.callback(*task.extraArgs)
        
        return Task.done


