# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\distributed\NonRepeatableRandomSourceUD.py
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify.DirectNotifyGlobal import directNotify
import random

class NonRepeatableRandomSourceUD(DistributedObjectGlobalUD):
    __module__ = __name__
    notify = directNotify.newCategory('NonRepeatableRandomSourceUD')
    RandomNumberCacheSize = 2000000

    class Request(ScratchPad):
        __module__ = __name__

        def __init__(self, replyTo, replyToClass, context, num):
            ScratchPad.__init__(self, replyTo=replyTo, replyToClass=replyToClass, context=context, num=num, randoms=[])

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)
        self._randoms = []
        self._requests = []
        self._fakeIt = 0
        if __dev__:
            NonRepeatableRandomSourceUD.RandomNumberCacheSize = config.GetInt('random-source-cache-size', 5000)
            self._fakeIt = config.GetBool('fake-non-repeatable-random-source', self._fakeIt)

    def randomSample(self, nrrsDoId, random):
        self._randoms = [
         random] + self._randoms
        if len(self._randoms) > self.RandomNumberCacheSize:
            self._randoms.pop()
        self._processRequests()
        self.air.sendUpdateToDoId('NonRepeatableRandomSource', 'randomSampleAck', nrrsDoId, [])

    def getRandomSamples(self, replyTo, replyToClass, context, num):
        self._requests.append(self.Request(replyTo, replyToClass, context, num))
        self._processRequests()

    def _processRequests(self):
        while len(self._requests):
            request = self._requests[0]
            if not self._fakeIt and len(request.randoms) < request.num:
                if len(self._randoms) == 0:
                    break
            needed = request.num - len(request.randoms)
            if needed > 0:
                numRandoms = min(needed, len(self._randoms))
                if self._fakeIt:
                    for i in xrange(numRandoms):
                        request.randoms.append(random.random() * 4294967295)

                else:
                    request.randoms += self._randoms[:numRandoms]
                    self._randoms = self._randoms[numRandoms:]
            if request.num == len(request.randoms):
                self._requests.pop(0)
                self.air.dispatchUpdateToDoId(request.replyToClass, 'getRandomSamplesReply', request.replyTo, [
                 request.context, request.randoms])