# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\SuitPlannerCogdoInteriorAI.py
from toontown.building.SuitPlannerInteriorAI import SuitPlannerInteriorAI

class SuitPlannerCogdoInteriorAI(SuitPlannerInteriorAI):
    __module__ = __name__

    def __init__(self, cogdoLayout, bldgLevel, bldgTrack, zone):
        self._cogdoLayout = cogdoLayout
        SuitPlannerInteriorAI.__init__(self, self._cogdoLayout.getNumGameFloors(), bldgLevel, bldgTrack, zone, respectInvasions=0)

    def _genSuitInfos(self, numFloors, bldgLevel, bldgTrack):
        SuitPlannerInteriorAI._genSuitInfos(self, self._cogdoLayout.getNumFloors(), bldgLevel, bldgTrack)