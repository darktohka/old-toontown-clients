# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\BossbotCountryClubMazeRoom_Battle03.py
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'LevelMgr', 'comment': '', 'parentEntId': 0, 'cogLevel': 0, 'farPlaneDistance': 1500, 'modelFilename': 'phase_12/models/bossbotHQ/BossbotMazex4_C', 'wantDoors': 1}, 1001: {'type': 'editMgr', 'name': 'EditMgr', 'parentEntId': 0, 'insertEntity': None, 'removeEntity': None, 'requestNewEntity': None, 'requestSave': None}, 0: {'type': 'zone', 'name': 'UberZone', 'comment': '', 'parentEntId': 0, 'scale': 1, 'description': '', 'visibility': []}, 110000: {'type': 'battleBlocker', 'name': '<unnamed>', 'comment': '', 'parentEntId': 0, 'pos': Point3(209.474, 84.9249, 0), 'hpr': Point3(270, 0, 0), 'scale': Vec3(1, 1, 1), 'cellId': 0, 'radius': 10}, 110202: {'type': 'door', 'name': '<unnamed>', 'comment': '', 'parentEntId': 110001, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1, 'color': Vec4(1, 1, 1, 1), 'isLock0Unlocked': 1, 'isLock1Unlocked': 0, 'isLock2Unlocked': 1, 'isLock3Unlocked': 1, 'isOpen': 0, 'isOpenEvent': 0, 'isVisBlocker': 0, 'secondsOpen': 1, 'unlock0Event': 0, 'unlock1Event': 110000, 'unlock2Event': 0, 'unlock3Event': 0}, 110002: {'type': 'maze', 'name': '<unnamed>', 'comment': '', 'parentEntId': 0, 'pos': Point3(-141.563, -78.8353, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'numSections': 4}, 10002: {'type': 'nodepath', 'name': 'props', 'comment': '', 'parentEntId': 0, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1}, 110001: {'type': 'nodepath', 'name': '<unnamed>', 'comment': '', 'parentEntId': 0, 'pos': Point3(231.424, 83.2459, 0), 'hpr': Point3(270, 0, 0), 'scale': Vec3(1, 1, 1)}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [Scenario0]}