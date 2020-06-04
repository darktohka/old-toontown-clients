# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\EditMgrAI.py
import EditMgrBase
if __dev__:
    from direct.showbase.PythonUtil import list2dict
    import EditorGlobals

class EditMgrAI(EditMgrBase.EditMgrBase):
    __module__ = __name__
    if __dev__:

        def setRequestNewEntity(self, data):
            spec = self.level.levelSpec
            entIds = spec.getAllEntIds()
            entIdDict = list2dict(entIds)
            allocRange = EditorGlobals.getEntIdAllocRange()
            if not hasattr(self, 'lastAllocatedEntId'):
                self.lastAllocatedEntId = allocRange[0]
            idChosen = 0
            while not idChosen:
                for id in xrange(self.lastAllocatedEntId, allocRange[1]):
                    print id
                    if id not in entIdDict:
                        idChosen = 1
                        break
                else:
                    if self.lastAllocatedEntId != allocRange[0]:
                        self.lastAllocatedEntId = allocRange[0]
                    else:
                        self.notify.error('out of entIds')

            data.update({'entId': id})
            self.lastAllocatedEntId = id
            self.level.setAttribChange(self.entId, 'insertEntity', data)
            self.level.levelSpec.doSetAttrib(self.entId, 'requestNewEntity', None)
            return

        def getSpecSaveEvent(self):
            return 'requestSave-%s' % self.level.levelId

        def setRequestSave(self, data):
            messenger.send(self.getSpecSaveEvent())
            self.level.levelSpec.doSetAttrib(self.entId, 'requestSave', None)
            return