# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\distributed\NonRepeatableRandomSourceAI.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.task import Task
from otp.distributed import OtpDoGlobals
import random

class NonRepeatableRandomSourceAI(DistributedObjectAI):
    __module__ = __name__
    notify = directNotify.newCategory('NonRepeatableRandomSourceAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        self._contextGen = SerialMaskedGen((1 << 32) - 1)
        self._requests = {}
        self._sampleTask = self.doMethodLater(3 * 60, self._sampleRandomTask, self.uniqueName('sampleRandom'))
        self._sampleRandom()

    def delete(self):
        self.removeTask(self._sampleTask)
        self._sampleTask = None
        DistributedObjectAI.delete(self)
        return

    def _sampleRandomTask(self, task=None):
        self._sampleRandom()
        return Task.again

    def _sampleRandom(self):
        self.air.sendUpdateToDoId('NonRepeatableRandomSource', 'randomSample', OtpDoGlobals.OTP_DO_ID_TOONTOWN_NON_REPEATABLE_RANDOM_SOURCE, [
         self.doId, int(random.randrange(1 << 32))])

    def randomSampleAck(self):
        self._sampleRandom()

    def getRandomSamples(self, callback, num=None):
        if num is None:
            num = 1
        context = self._contextGen.next()
        self._requests[context] = (callback,)
        self.air.sendUpdateToDoId('NonRepeatableRandomSource', 'getRandomSamples', OtpDoGlobals.OTP_DO_ID_TOONTOWN_NON_REPEATABLE_RANDOM_SOURCE, [
         self.doId, 'NonRepeatableRandomSource', context, num])
        return

    def getRandomSamplesReply(self, context, samples):
        (callback,) = self._requests.pop(context)
        callback(samples)