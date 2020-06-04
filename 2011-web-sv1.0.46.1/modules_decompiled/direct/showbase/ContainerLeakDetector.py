# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\ContainerLeakDetector.py
from pandac.PandaModules import PStatCollector
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.PythonUtil import Queue, invertDictLossless, makeFlywheelGen
from direct.showbase.PythonUtil import itype, serialNum, safeRepr, fastRepr
from direct.showbase.Job import Job
import types, weakref, random, __builtin__

def _createContainerLeak():

    def leakContainer(task=None):
        base = getBase()
        if not hasattr(base, 'leakContainer'):
            base.leakContainer = {}

        class LeakKey:
            __module__ = __name__

        base.leakContainer[(LeakKey(),)] = {}
        if random.random() < 0.01:
            key = random.choice(base.leakContainer.keys())
            ContainerLeakDetector.notify.debug('removing reference to leakContainer key %s so it will be garbage-collected' % safeRepr(key))
            del base.leakContainer[key]
        taskMgr.doMethodLater(10, leakContainer, 'leakContainer-%s' % serialNum())
        if task:
            return task.done

    leakContainer()
    return


def _createTaskLeak():
    leakTaskName = uniqueName('leakedTask')
    leakDoLaterName = uniqueName('leakedDoLater')

    def nullTask(task=None):
        return task.cont

    def nullDoLater(task=None):
        return task.done

    def leakTask(task=None, leakTaskName=leakTaskName):
        base = getBase()
        taskMgr.add(nullTask, uniqueName(leakTaskName))
        taskMgr.doMethodLater(1 << 31, nullDoLater, uniqueName(leakDoLaterName))
        taskMgr.doMethodLater(10, leakTask, 'doLeakTask-%s' % serialNum())
        if task:
            return task.done

    leakTask()
    return


class NoDictKey:
    __module__ = __name__


class Indirection:
    __module__ = __name__

    def __init__(self, evalStr=None, dictKey=NoDictKey):
        self.evalStr = evalStr
        self.dictKey = NoDictKey
        self._isWeakRef = False
        self._refCount = 0
        if dictKey is not NoDictKey:
            keyRepr = safeRepr(dictKey)
            useEval = False
            try:
                keyEval = eval(keyRepr)
                useEval = True
            except:
                pass
            else:
                if useEval:
                    if hash(keyEval) != hash(dictKey):
                        useEval = False
                if useEval:
                    self.evalStr = '[%s]' % keyRepr
                else:
                    try:
                        self.dictKey = weakref.ref(dictKey)
                        self._isWeakRef = True
                    except TypeError, e:
                        ContainerLeakDetector.notify.debug('could not weakref dict key %s' % keyRepr)
                        self.dictKey = dictKey
                        self._isWeakRef = False

    def destroy(self):
        self.dictKey = NoDictKey

    def acquire(self):
        self._refCount += 1

    def release(self):
        self._refCount -= 1
        if self._refCount == 0:
            self.destroy()

    def isDictKey(self):
        return self.dictKey is not NoDictKey

    def _getNonWeakDictKey(self):
        if not self._isWeakRef:
            return self.dictKey
        else:
            key = self.dictKey()
            if key is None:
                return '<garbage-collected dict key>'
            return key
        return

    def dereferenceDictKey(self, parentDict):
        key = self._getNonWeakDictKey()
        if parentDict is None:
            return key
        return parentDict[key]

    def getString(self, prevIndirection=None, nextIndirection=None):
        instanceDictStr = '.__dict__'
        if self.evalStr is not None:
            if nextIndirection is not None and self.evalStr[-len(instanceDictStr):] == instanceDictStr:
                return self.evalStr[:-len(instanceDictStr)]
            if prevIndirection is not None and prevIndirection.evalStr is not None:
                if prevIndirection.evalStr[-len(instanceDictStr):] == instanceDictStr:
                    return '.%s' % self.evalStr[2:-2]
            return self.evalStr
        keyRepr = safeRepr(self._getNonWeakDictKey())
        if prevIndirection is not None and prevIndirection.evalStr is not None:
            if prevIndirection.evalStr[-len(instanceDictStr):] == instanceDictStr:
                return '.%s' % keyRepr
        return '[%s]' % keyRepr

    def __repr__(self):
        return self.getString()


class ObjectRef:
    __module__ = __name__
    notify = directNotify.newCategory('ObjectRef')

    class FailedEval(Exception):
        __module__ = __name__

    def __init__(self, indirection, objId, other=None):
        self._indirections = []
        if other is not None:
            for ind in other._indirections:
                self._indirections.append(ind)

        self._indirections.append(indirection)
        for ind in self._indirections:
            ind.acquire()

        self.notify.debug(repr(self))
        return

    def destroy(self):
        for indirection in self._indirections:
            indirection.release()

        del self._indirections

    def getNumIndirections(self):
        return len(self._indirections)

    def goesThroughGen(self, obj=None, objId=None):
        if obj is None:
            pass
        else:
            objId = id(obj)
        o = None
        evalStr = ''
        curObj = None
        indirections = self._indirections
        for indirection in indirections:
            yield None
            indirection.acquire()

        for indirection in indirections:
            yield None
            if not indirection.isDictKey():
                evalStr += indirection.getString()
            else:
                curObj = self._getContainerByEval(evalStr, curObj=curObj)
                if curObj is None:
                    raise FailedEval(evalStr)
                curObj = indirection.dereferenceDictKey(curObj)
                evalStr = ''
            yield None
            o = self._getContainerByEval(evalStr, curObj=curObj)
            if id(o) == objId:
                break

        for indirection in indirections:
            yield None
            indirection.release()

        yield id(o) == objId
        return

    def goesThrough(self, obj=None, objId=None):
        for goesThrough in self.goesThroughGen(obj=obj, objId=objId):
            pass

        return goesThrough

    def _getContainerByEval(self, evalStr, curObj=None):
        if curObj is not None:
            evalStr = 'curObj%s' % evalStr
        else:
            bis = '__builtin__'
            if evalStr[:len(bis)] != bis:
                evalStr = '%s.%s' % (bis, evalStr)
        try:
            container = eval(evalStr)
        except NameError, ne:
            return
        except AttributeError, ae:
            return
        except KeyError, ke:
            return

        return container

    def getContainerGen(self, getInstance=False):
        evalStr = ''
        curObj = None
        indirections = self._indirections
        for indirection in indirections:
            indirection.acquire()

        for indirection in indirections:
            yield None
            if not indirection.isDictKey():
                evalStr += indirection.getString()
            else:
                curObj = self._getContainerByEval(evalStr, curObj=curObj)
                if curObj is None:
                    raise FailedEval(evalStr)
                curObj = indirection.dereferenceDictKey(curObj)
                evalStr = ''

        for indirection in indirections:
            yield None
            indirection.release()

        if getInstance:
            lenDict = len('.__dict__')
            if evalStr[-lenDict:] == '.__dict__':
                evalStr = evalStr[:-lenDict]
        yield self._getContainerByEval(evalStr, curObj=curObj)
        return

    def getEvalStrGen(self, getInstance=False):
        str = ''
        prevIndirection = None
        curIndirection = None
        nextIndirection = None
        indirections = self._indirections
        for indirection in indirections:
            indirection.acquire()

        for i in xrange(len(indirections)):
            yield None
            if i > 0:
                prevIndirection = indirections[(i - 1)]
            else:
                prevIndirection = None
            curIndirection = indirections[i]
            if i < len(indirections) - 1:
                nextIndirection = indirections[(i + 1)]
            else:
                nextIndirection = None
            str += curIndirection.getString(prevIndirection=prevIndirection, nextIndirection=nextIndirection)

        if getInstance:
            lenDict = len('.__dict__')
            if str[-lenDict:] == '.__dict__':
                str = str[:-lenDict]
        for indirection in indirections:
            yield None
            indirection.release()

        yield str
        return

    def getFinalIndirectionStr(self):
        prevIndirection = None
        if len(self._indirections) > 1:
            prevIndirection = self._indirections[(-2)]
        return self._indirections[(-1)].getString(prevIndirection=prevIndirection)

    def __repr__(self):
        for result in self.getEvalStrGen():
            pass

        return result


class FindContainers(Job):
    __module__ = __name__

    def __init__(self, name, leakDetector):
        Job.__init__(self, name)
        self._leakDetector = leakDetector
        self._id2ref = self._leakDetector._id2ref
        self._id2baseStartRef = {}
        self._id2discoveredStartRef = {}
        self._baseStartRefWorkingList = ScratchPad(refGen=nullGen(), source=self._id2baseStartRef)
        self._discoveredStartRefWorkingList = ScratchPad(refGen=nullGen(), source=self._id2discoveredStartRef)
        self.notify = self._leakDetector.notify
        ContainerLeakDetector.addPrivateObj(self.__dict__)
        ref = ObjectRef(Indirection(evalStr='__builtin__.__dict__'), id(__builtin__.__dict__))
        self._id2baseStartRef[id(__builtin__.__dict__)] = ref
        if not hasattr(__builtin__, 'leakDetectors'):
            __builtin__.leakDetectors = {}
        ref = ObjectRef(Indirection(evalStr='leakDetectors'), id(leakDetectors))
        self._id2baseStartRef[id(leakDetectors)] = ref
        for i in self._addContainerGen(__builtin__.__dict__, ref):
            pass

        try:
            base
        except:
            pass
        else:
            ref = ObjectRef(Indirection(evalStr='base.__dict__'), id(base.__dict__))
            self._id2baseStartRef[id(base.__dict__)] = ref
            for i in self._addContainerGen(base.__dict__, ref):
                pass

            try:
                simbase
            except:
                pass
            else:
                ref = ObjectRef(Indirection(evalStr='simbase.__dict__'), id(simbase.__dict__))
                self._id2baseStartRef[id(simbase.__dict__)] = ref
                for i in self._addContainerGen(simbase.__dict__, ref):
                    pass

    def destroy(self):
        ContainerLeakDetector.removePrivateObj(self.__dict__)
        Job.destroy(self)

    def getPriority(self):
        return Job.Priorities.Low

    @staticmethod
    def getStartObjAffinity(startObj):
        try:
            return len(startObj)
        except:
            return 1

    def _isDeadEnd(self, obj, objName=None):
        if type(obj) in (types.BooleanType, types.BuiltinFunctionType, types.BuiltinMethodType, types.ComplexType, types.FloatType, types.IntType, types.LongType, types.NoneType, types.NotImplementedType, types.TypeType, types.CodeType, types.FunctionType, types.StringType, types.UnicodeType, types.TupleType):
            return True
        if id(obj) in ContainerLeakDetector.PrivateIds:
            return True
        if type(objName) == types.StringType and objName in ('im_self', 'im_class'):
            return True
        try:
            className = obj.__class__.__name__
        except:
            pass
        else:
            if className == 'method-wrapper':
                return True

        return False

    def _hasLength(self, obj):
        return hasattr(obj, '__len__')

    def _addContainerGen(self, cont, objRef):
        contId = id(cont)
        if contId in self._id2ref:
            for existingRepr in self._id2ref[contId].getEvalStrGen():
                yield None

            for newRepr in objRef.getEvalStrGen():
                yield None

        if contId not in self._id2ref or len(newRepr) < len(existingRepr):
            if contId in self._id2ref:
                self._leakDetector.removeContainerById(contId)
            self._id2ref[contId] = objRef
        return

    def _addDiscoveredStartRef(self, obj, ref):
        objId = id(obj)
        if objId in self._id2discoveredStartRef:
            existingRef = self._id2discoveredStartRef[objId]
            if type(existingRef) not in (types.IntType, types.LongType):
                if existingRef.getNumIndirections() >= ref.getNumIndirections():
                    return
        if objId in self._id2ref:
            if self._id2ref[objId].getNumIndirections() >= ref.getNumIndirections():
                return
        storedItem = ref
        if objId in self._id2ref:
            storedItem = objId
        self._id2discoveredStartRef[objId] = storedItem

    def run(self):
        try:
            workingListSelector = nullGen()
            curObjRef = None
            while True:
                yield None
                if curObjRef is None:
                    try:
                        startRefWorkingList = workingListSelector.next()
                    except StopIteration:
                        baseLen = len(self._baseStartRefWorkingList.source)
                        discLen = len(self._discoveredStartRefWorkingList.source)
                        minLen = float(max(1, min(baseLen, discLen)))
                        minLen *= 3.0
                        workingListSelector = flywheel([self._baseStartRefWorkingList, self._discoveredStartRefWorkingList], [
                         baseLen / minLen, discLen / minLen])
                        yield None
                        continue
                    else:
                        while True:
                            yield None
                            try:
                                curObjRef = startRefWorkingList.refGen.next()
                                break
                            except StopIteration:
                                if len(startRefWorkingList.source) == 0:
                                    break
                                for fw in makeFlywheelGen(startRefWorkingList.source.values(), countFunc=lambda x: self.getStartObjAffinity(x), scale=0.05):
                                    yield None

                                startRefWorkingList.refGen = fw

                        if curObjRef is None:
                            continue
                        if type(curObjRef) in (types.IntType, types.LongType):
                            startId = curObjRef
                            curObjRef = None
                            try:
                                for containerRef in self._leakDetector.getContainerByIdGen(startId):
                                    yield None

                            except:
                                self.notify.debug('invalid startRef, stored as id %s' % startId)
                                self._leakDetector.removeContainerById(startId)
                                continue
                            else:
                                curObjRef = containerRef
                try:
                    for curObj in curObjRef.getContainerGen():
                        yield None

                except:
                    self.notify.debug('lost current container, ref.getContainerGen() failed')
                    curObjRef = None
                    continue

                self.notify.debug('--> %s' % curObjRef)
                parentObjRef = curObjRef
                curObjRef = None
                if hasattr(curObj, '__dict__'):
                    child = curObj.__dict__
                    hasLength = self._hasLength(child)
                    notDeadEnd = not self._isDeadEnd(child)
                    if hasLength or notDeadEnd:
                        for goesThrough in parentObjRef.goesThroughGen(child):
                            pass

                        if not goesThrough:
                            objRef = ObjectRef(Indirection(evalStr='.__dict__'), id(child), parentObjRef)
                            yield None
                            if hasLength:
                                for i in self._addContainerGen(child, objRef):
                                    yield None

                            if notDeadEnd:
                                self._addDiscoveredStartRef(child, objRef)
                                curObjRef = objRef
                    continue
                if type(curObj) is types.DictType:
                    key = None
                    attr = None
                    keys = curObj.keys()
                    numKeysLeft = len(keys) + 1
                    for key in keys:
                        yield None
                        numKeysLeft -= 1
                        try:
                            attr = curObj[key]
                        except KeyError, e:
                            self.notify.debug('could not index into %s with key %s' % (parentObjRef, safeRepr(key)))
                            continue

                        hasLength = self._hasLength(attr)
                        notDeadEnd = False
                        if curObjRef is None:
                            notDeadEnd = not self._isDeadEnd(attr, key)
                        if hasLength or notDeadEnd:
                            for goesThrough in parentObjRef.goesThroughGen(curObj[key]):
                                pass

                            if not goesThrough:
                                if curObj is __builtin__.__dict__:
                                    objRef = ObjectRef(Indirection(evalStr='%s' % key), id(curObj[key]))
                                else:
                                    objRef = ObjectRef(Indirection(dictKey=key), id(curObj[key]), parentObjRef)
                                yield None
                                if hasLength:
                                    for i in self._addContainerGen(attr, objRef):
                                        yield None

                                if notDeadEnd:
                                    self._addDiscoveredStartRef(attr, objRef)
                                    if curObjRef is None and random.randrange(numKeysLeft) == 0:
                                        curObjRef = objRef

                    del key
                    del attr
                    continue
                    try:
                        childNames = dir(curObj)
                    except:
                        pass
                    else:
                        try:
                            index = -1
                            attrs = []
                            while 1:
                                yield None
                                try:
                                    attr = itr.next()
                                except:
                                    attr = None
                                    break

                                attrs.append(attr)

                            numAttrsLeft = len(attrs) + 1
                            for attr in attrs:
                                yield None
                                index += 1
                                numAttrsLeft -= 1
                                hasLength = self._hasLength(attr)
                                notDeadEnd = False
                                if curObjRef is None:
                                    notDeadEnd = not self._isDeadEnd(attr)
                                if hasLength or notDeadEnd:
                                    for goesThrough in parentObjRef.goesThrough(curObj[index]):
                                        pass

                                    if not goesThrough:
                                        objRef = ObjectRef(Indirection(evalStr='[%s]' % index), id(curObj[index]), parentObjRef)
                                        yield None
                                        if hasLength:
                                            for i in self._addContainerGen(attr, objRef):
                                                yield None

                                        if notDeadEnd:
                                            self._addDiscoveredStartRef(attr, objRef)
                                            if curObjRef is None and random.randrange(numAttrsLeft) == 0:
                                                curObjRef = objRef

                            del attr
                        except StopIteration, e:
                            pass
                        else:
                            del itr
                            continue

        except Exception, e:
            print 'FindContainers job caught exception: %s' % e
            if __dev__:
                raise

        yield Job.Done
        return


class CheckContainers(Job):
    __module__ = __name__
    ReprItems = 5

    def __init__(self, name, leakDetector, index):
        Job.__init__(self, name)
        self._leakDetector = leakDetector
        self.notify = self._leakDetector.notify
        self._index = index
        ContainerLeakDetector.addPrivateObj(self.__dict__)

    def destroy(self):
        ContainerLeakDetector.removePrivateObj(self.__dict__)
        Job.destroy(self)

    def getPriority(self):
        return Job.Priorities.Normal

    def run(self):
        try:
            self._leakDetector._index2containerId2len[self._index] = {}
            ids = self._leakDetector.getContainerIds()
            for objId in ids:
                yield None
                try:
                    for result in self._leakDetector.getContainerByIdGen(objId):
                        yield None

                    container = result
                except Exception, e:
                    if self.notify.getDebug():
                        for contName in self._leakDetector.getContainerNameByIdGen(objId):
                            yield None

                        self.notify.debug('%s no longer exists; caught exception in getContainerById (%s)' % (contName, e))
                    self._leakDetector.removeContainerById(objId)
                    continue

                if container is None:
                    if self.notify.getDebug():
                        for contName in self._leakDetector.getContainerNameByIdGen(objId):
                            yield None

                        self.notify.debug('%s no longer exists; getContainerById returned None' % contName)
                    self._leakDetector.removeContainerById(objId)
                    continue
                try:
                    cLen = len(container)
                except Exception, e:
                    if self.notify.getDebug():
                        for contName in self._leakDetector.getContainerNameByIdGen(objId):
                            yield None

                        self.notify.debug('%s is no longer a container, it is now %s (%s)' % (contName, safeRepr(container), e))
                    self._leakDetector.removeContainerById(objId)
                    continue

                self._leakDetector._index2containerId2len[self._index][objId] = cLen

            if self._index > 0:
                idx2id2len = self._leakDetector._index2containerId2len
                for objId in idx2id2len[self._index]:
                    yield None
                    if objId in idx2id2len[(self._index - 1)]:
                        diff = idx2id2len[self._index][objId] - idx2id2len[(self._index - 1)][objId]
                        if self._index > 2 and objId in idx2id2len[(self._index - 2)] and objId in idx2id2len[(self._index - 3)]:
                            diff2 = idx2id2len[(self._index - 1)][objId] - idx2id2len[(self._index - 2)][objId]
                            diff3 = idx2id2len[(self._index - 2)][objId] - idx2id2len[(self._index - 3)][objId]
                            if self._index <= 4:
                                if diff > 0 and diff2 > 0 and diff3 > 0:
                                    name = self._leakDetector.getContainerNameById(objId)
                                    try:
                                        for container in self._leakDetector.getContainerByIdGen(objId):
                                            yield None

                                    except:
                                        self.notify.debug('caught exception in getContainerByIdGen (2)')
                                    else:
                                        msg = '%s (%s) consistently increased in size over the last 3 periods (%s items at last measurement, current contents: %s)' % (name, itype(container), idx2id2len[self._index][objId], fastRepr(container, maxLen=CheckContainers.ReprItems))
                                        self.notify.warning(msg)

                                    yield None
                            elif objId in idx2id2len[(self._index - 4)] and objId in idx2id2len[(self._index - 5)]:
                                diff4 = idx2id2len[(self._index - 3)][objId] - idx2id2len[(self._index - 4)][objId]
                                diff5 = idx2id2len[(self._index - 4)][objId] - idx2id2len[(self._index - 5)][objId]
                                if diff > 0 and diff2 > 0 and diff3 > 0 and diff4 > 0 and diff5 > 0:
                                    name = self._leakDetector.getContainerNameById(objId)
                                    try:
                                        for container in self._leakDetector.getContainerByIdGen(objId):
                                            yield None

                                    except:
                                        self.notify.debug('caught exception in getContainerByIdGen (3)')
                                    else:
                                        msg = 'leak detected: %s (%s) consistently increased in size over the last 5 periods (%s items at last measurement, current contents: %s)' % (name, itype(container), idx2id2len[self._index][objId], fastRepr(container, maxLen=CheckContainers.ReprItems))
                                        self.notify.warning(msg)
                                        yield None
                                        messenger.send(self._leakDetector.getLeakEvent(), [container, name])
                                        if config.GetBool('pdb-on-leak-detect', 0):
                                            import pdb
                                            pdb.set_trace()

        except Exception, e:
            print 'CheckContainers job caught exception: %s' % e
            if __dev__:
                raise

        yield Job.Done
        return


class FPTObjsOfType(Job):
    __module__ = __name__

    def __init__(self, name, leakDetector, otn, doneCallback=None):
        Job.__init__(self, name)
        self._leakDetector = leakDetector
        self.notify = self._leakDetector.notify
        self._otn = otn
        self._doneCallback = doneCallback
        self._ldde = self._leakDetector._getDestroyEvent()
        self.accept(self._ldde, self._handleLDDestroy)
        ContainerLeakDetector.addPrivateObj(self.__dict__)

    def destroy(self):
        self.ignore(self._ldde)
        self._leakDetector = None
        self._doneCallback = None
        ContainerLeakDetector.removePrivateObj(self.__dict__)
        Job.destroy(self)
        return

    def _handleLDDestroy(self):
        self.destroy()

    def getPriority(self):
        return Job.Priorities.High

    def run(self):
        ids = self._leakDetector.getContainerIds()
        try:
            for id in ids:
                getInstance = self._otn.lower() not in 'dict'
                yield None
                try:
                    for container in self._leakDetector.getContainerByIdGen(id, getInstance=getInstance):
                        yield None

                except:
                    pass
                else:
                    if hasattr(container, '__class__'):
                        cName = container.__class__.__name__
                    else:
                        cName = container.__name__
                    if self._otn.lower() in cName.lower():
                        try:
                            for ptc in self._leakDetector.getContainerNameByIdGen(id, getInstance=getInstance):
                                yield None

                        except:
                            pass
                        else:
                            print 'GPTC(' + self._otn + '):' + self.getJobName() + ': ' + ptc

        except Exception, e:
            print 'FPTObjsOfType job caught exception: %s' % e
            if __dev__:
                raise

        yield Job.Done
        return

    def finished(self):
        if self._doneCallback:
            self._doneCallback(self)


class FPTObjsNamed(Job):
    __module__ = __name__

    def __init__(self, name, leakDetector, on, doneCallback=None):
        Job.__init__(self, name)
        self._leakDetector = leakDetector
        self.notify = self._leakDetector.notify
        self._on = on
        self._doneCallback = doneCallback
        self._ldde = self._leakDetector._getDestroyEvent()
        self.accept(self._ldde, self._handleLDDestroy)
        ContainerLeakDetector.addPrivateObj(self.__dict__)

    def destroy(self):
        self.ignore(self._ldde)
        self._leakDetector = None
        self._doneCallback = None
        ContainerLeakDetector.removePrivateObj(self.__dict__)
        Job.destroy(self)
        return

    def _handleLDDestroy(self):
        self.destroy()

    def getPriority(self):
        return Job.Priorities.High

    def run(self):
        ids = self._leakDetector.getContainerIds()
        try:
            for id in ids:
                yield None
                try:
                    for container in self._leakDetector.getContainerByIdGen(id):
                        yield None

                except:
                    pass
                else:
                    name = self._leakDetector._id2ref[id].getFinalIndirectionStr()
                    if self._on.lower() in name.lower():
                        try:
                            for ptc in self._leakDetector.getContainerNameByIdGen(id):
                                yield None

                        except:
                            pass
                        else:
                            print 'GPTCN(' + self._on + '):' + self.getJobName() + ': ' + ptc

        except Exception, e:
            print 'FPTObjsNamed job caught exception: %s' % e
            if __dev__:
                raise

        yield Job.Done
        return

    def finished(self):
        if self._doneCallback:
            self._doneCallback(self)


class PruneObjectRefs(Job):
    __module__ = __name__

    def __init__(self, name, leakDetector):
        Job.__init__(self, name)
        self._leakDetector = leakDetector
        self.notify = self._leakDetector.notify
        ContainerLeakDetector.addPrivateObj(self.__dict__)

    def destroy(self):
        ContainerLeakDetector.removePrivateObj(self.__dict__)
        Job.destroy(self)

    def getPriority(self):
        return Job.Priorities.Normal

    def run(self):
        try:
            ids = self._leakDetector.getContainerIds()
            for id in ids:
                yield None
                try:
                    for container in self._leakDetector.getContainerByIdGen(id):
                        yield None

                except:
                    self._leakDetector.removeContainerById(id)

            _id2baseStartRef = self._leakDetector._findContainersJob._id2baseStartRef
            ids = _id2baseStartRef.keys()
            for id in ids:
                yield None
                try:
                    for container in _id2baseStartRef[id].getContainerGen():
                        yield None

                except:
                    del _id2baseStartRef[id]

            _id2discoveredStartRef = self._leakDetector._findContainersJob._id2discoveredStartRef
            ids = _id2discoveredStartRef.keys()
            for id in ids:
                yield None
                try:
                    for container in _id2discoveredStartRef[id].getContainerGen():
                        yield None

                except:
                    del _id2discoveredStartRef[id]

        except Exception, e:
            print 'PruneObjectRefs job caught exception: %s' % e
            if __dev__:
                raise

        yield Job.Done
        return


class ContainerLeakDetector(Job):
    __module__ = __name__
    notify = directNotify.newCategory('ContainerLeakDetector')
    PrivateIds = set()

    def __init__(self, name, firstCheckDelay=None):
        Job.__init__(self, name)
        self._serialNum = serialNum()
        self._findContainersJob = None
        self._checkContainersJob = None
        self._pruneContainersJob = None
        if firstCheckDelay is None:
            firstCheckDelay = 60.0 * 15.0
        self._nextCheckDelay = firstCheckDelay / 2.0
        self._checkDelayScale = config.GetFloat('leak-detector-check-delay-scale', 1.5)
        self._pruneTaskPeriod = config.GetFloat('leak-detector-prune-period', 60.0 * 30.0)
        self._id2ref = {}
        self._index2containerId2len = {}
        self._index2delay = {}
        if config.GetBool('leak-container', 0):
            _createContainerLeak()
        if config.GetBool('leak-tasks', 0):
            _createTaskLeak()
        ContainerLeakDetector.addPrivateObj(ContainerLeakDetector.PrivateIds)
        ContainerLeakDetector.addPrivateObj(self.__dict__)
        self.setPriority(Job.Priorities.Min)
        jobMgr.add(self)
        return

    def destroy(self):
        messenger.send(self._getDestroyEvent())
        self.ignoreAll()
        if self._pruneContainersJob is not None:
            jobMgr.remove(self._pruneContainersJob)
            self._pruneContainersJob = None
        if self._checkContainersJob is not None:
            jobMgr.remove(self._checkContainersJob)
            self._checkContainersJob = None
        jobMgr.remove(self._findContainersJob)
        self._findContainersJob = None
        del self._id2ref
        del self._index2containerId2len
        del self._index2delay
        return

    def _getDestroyEvent(self):
        return 'cldDestroy-%s' % self._serialNum

    def getLeakEvent(self):
        return 'containerLeakDetected-%s' % self._serialNum

    @classmethod
    def addPrivateObj(cls, obj):
        cls.PrivateIds.add(id(obj))

    @classmethod
    def removePrivateObj(cls, obj):
        cls.PrivateIds.remove(id(obj))

    def _getCheckTaskName(self):
        return 'checkForLeakingContainers-%s' % self._serialNum

    def _getPruneTaskName(self):
        return 'pruneLeakingContainerRefs-%s' % self._serialNum

    def getContainerIds(self):
        return self._id2ref.keys()

    def getContainerByIdGen(self, id, **kwArgs):
        return self._id2ref[id].getContainerGen(**kwArgs)

    def getContainerById(self, id):
        for result in self._id2ref[id].getContainerGen():
            pass

        return result

    def getContainerNameByIdGen(self, id, **kwArgs):
        return self._id2ref[id].getEvalStrGen(**kwArgs)

    def getContainerNameById(self, id):
        if id in self._id2ref:
            return repr(self._id2ref[id])
        return '<unknown container>'

    def removeContainerById(self, id):
        if id in self._id2ref:
            self._id2ref[id].destroy()
            del self._id2ref[id]

    def run(self):
        self._findContainersJob = FindContainers('%s-findContainers' % self.getJobName(), self)
        jobMgr.add(self._findContainersJob)
        self._scheduleNextLeakCheck()
        self._scheduleNextPruning()
        while True:
            yield Job.Sleep

    def getPathsToContainers(self, name, ot, doneCallback=None):
        j = FPTObjsOfType(name, self, ot, doneCallback)
        jobMgr.add(j)
        return j

    def getPathsToContainersNamed(self, name, on, doneCallback=None):
        j = FPTObjsNamed(name, self, on, doneCallback)
        jobMgr.add(j)
        return j

    def _scheduleNextLeakCheck(self):
        taskMgr.doMethodLater(self._nextCheckDelay, self._checkForLeaks, self._getCheckTaskName())
        self._nextCheckDelay = self._nextCheckDelay * self._checkDelayScale

    def _checkForLeaks(self, task=None):
        self._index2delay[len(self._index2containerId2len)] = self._nextCheckDelay
        self._checkContainersJob = CheckContainers('%s-checkForLeaks' % self.getJobName(), self, len(self._index2containerId2len))
        self.acceptOnce(self._checkContainersJob.getFinishedEvent(), self._scheduleNextLeakCheck)
        jobMgr.add(self._checkContainersJob)
        return task.done

    def _scheduleNextPruning(self):
        taskMgr.doMethodLater(self._pruneTaskPeriod, self._pruneObjectRefs, self._getPruneTaskName())

    def _pruneObjectRefs(self, task=None):
        self._pruneContainersJob = PruneObjectRefs('%s-pruneObjectRefs' % self.getJobName(), self)
        self.acceptOnce(self._pruneContainersJob.getFinishedEvent(), self._scheduleNextPruning)
        jobMgr.add(self._pruneContainersJob)
        return task.done