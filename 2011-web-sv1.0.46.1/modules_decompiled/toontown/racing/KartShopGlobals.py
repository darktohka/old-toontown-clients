# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\racing\KartShopGlobals.py
from direct.showbase import PythonUtil

class KartShopGlobals:
    __module__ = __name__
    EVENTDICT = {'guiDone': 'guiDone', 'returnKart': 'returnKart', 'buyKart': 'buyAKart', 'buyAccessory': 'buyAccessory'}
    KARTCLERK_TIMER = 180
    MAX_KART_ACC = 16


class KartGlobals:
    __module__ = __name__
    ENTER_MOVIE = 1
    EXIT_MOVIE = 2
    COUNTDOWN_TIME = 30
    BOARDING_TIME = 10.0
    ENTER_RACE_TIME = 6.0
    ERROR_CODE = PythonUtil.Enum('success, eGeneric, eTickets, eBoardOver, eNoKart, eOccupied, eTrackClosed, eTooLate, eUnpaid')
    FRONT_LEFT_SPOT = 0
    FRONT_RIGHT_SPOT = 1
    REAR_LEFT_SPOT = 2
    REAR_RIGHT_SPOT = 3
    PAD_GROUP_NUM = 4

    def getPadLocation(padId):
        return padId % KartGlobals.PAD_GROUP_NUM

    getPadLocation = staticmethod(getPadLocation)