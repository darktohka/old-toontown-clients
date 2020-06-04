# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\distributed\DistributedObjectGlobalUD.py
from DistributedObjectUD import DistributedObjectUD
from direct.directnotify.DirectNotifyGlobal import directNotify
import sys

class DistributedObjectGlobalUD(DistributedObjectUD):
    __module__ = __name__
    notify = directNotify.newCategory('DistributedObjectGlobalUD')
    doNotDeallocateChannel = 1
    isGlobalDistObj = 1

    def __init__(self, air):
        DistributedObjectUD.__init__(self, air)
        self.ExecNamespace = {'self': self}

    def announceGenerate(self):
        self.air.registerForChannel(self.doId)
        DistributedObjectUD.announceGenerate(self)

    def delete(self):
        self.air.unregisterForChannel(self.doId)
        DistributedObjectUD.delete(self)

    def execCommand(self, command, mwMgrId, avId, zoneId):
        text = str(self.__execMessage(command))[:config.GetInt('ai-debug-length', 300)]
        dclass = uber.air.dclassesByName.get('PiratesMagicWordManagerAI')
        dg = dclass.aiFormatUpdate('setMagicWordResponse', mwMgrId, (1 << 32) + avId, uber.air.ourChannel, [text])
        uber.air.send(dg)

    def __execMessage(self, message):
        if not self.ExecNamespace:
            exec 'from pandac.PandaModules import *' in globals(), self.ExecNamespace
        try:
            return str(eval(message, globals(), self.ExecNamespace))
        except SyntaxError:
            try:
                exec message in globals(), self.ExecNamespace
                return 'ok'
            except:
                exception = sys.exc_info()[0]
                extraInfo = sys.exc_info()[1]
                if extraInfo:
                    return str(extraInfo)
                else:
                    return str(exception)

        except:
            exception = sys.exc_info()[0]
            extraInfo = sys.exc_info()[1]
            if extraInfo:
                return str(extraInfo)
            else:
                return str(exception)