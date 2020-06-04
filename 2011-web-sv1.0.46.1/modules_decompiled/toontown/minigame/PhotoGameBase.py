# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\PhotoGameBase.py
import PhotoGameGlobals, random

class PhotoGameBase:
    __module__ = __name__

    def __init__(self):
        pass

    def load(self):
        self.data = PhotoGameGlobals.AREA_DATA[self.getSafezoneId()]

    def generateAssignmentTemplates(self, numAssignments):
        self.data = PhotoGameGlobals.AREA_DATA[self.getSafezoneId()]
        random.seed(self.doId)
        assignmentTemplates = []
        numPathes = len(self.data['PATHS'])
        if numPathes == 0:
            return assignmentTemplates
        while len(assignmentTemplates) < numAssignments:
            subjectIndex = random.choice(range(numPathes))
            pose = (None, None)
            while pose[0] == None:
                animSetIndex = self.data['PATHANIMREL'][subjectIndex]
                pose = random.choice(self.data['ANIMATIONS'][animSetIndex] + self.data['MOVEMODES'][animSetIndex])

            newTemplate = (
             subjectIndex, pose[0])
            if newTemplate not in assignmentTemplates:
                assignmentTemplates.append((subjectIndex, pose[0]))

        self.notify.debug('assignment templates')
        self.notify.debug(str(assignmentTemplates))
        for template in assignmentTemplates:
            self.notify.debug(str(template))

        return assignmentTemplates