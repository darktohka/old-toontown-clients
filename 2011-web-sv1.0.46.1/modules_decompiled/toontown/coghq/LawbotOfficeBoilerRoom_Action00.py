# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\LawbotOfficeBoilerRoom_Action00.py
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'LevelMgr', 'comment': '', 'parentEntId': 0, 'cogLevel': 0, 'farPlaneDistance': 1500, 'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone08a', 'wantDoors': 1}, 1001: {'type': 'editMgr', 'name': 'EditMgr', 'parentEntId': 0, 'insertEntity': None, 'removeEntity': None, 'requestNewEntity': None, 'requestSave': None}, 0: {'type': 'zone', 'name': 'UberZone', 'comment': '', 'parentEntId': 0, 'scale': 1, 'description': '', 'visibility': []}, 10055: {'type': 'attribModifier', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10001, 'attribName': 'modelPath', 'recursive': 1, 'typeName': 'model', 'value': ''}, 10045: {'type': 'gagBarrel', 'name': 'gag', 'comment': '', 'parentEntId': 10002, 'pos': Point3(1.36977, 0.773027, 0), 'hpr': Vec3(51.1067, 0, 0), 'scale': Vec3(1, 1, 1), 'gagLevel': 5, 'gagLevelMax': 0, 'gagTrack': 'random', 'rewardPerGrab': 5, 'rewardPerGrabMax': 0}, 10047: {'type': 'gagBarrel', 'name': 'gag', 'comment': '', 'parentEntId': 10002, 'pos': Point3(0.137292, 2.83576, 0), 'hpr': Vec3(-210.473, 0, 0), 'scale': Vec3(1, 1, 1), 'gagLevel': 5, 'gagLevelMax': 0, 'gagTrack': 'random', 'rewardPerGrab': 5, 'rewardPerGrabMax': 0}, 10054: {'type': 'gagBarrel', 'name': 'gag', 'comment': '', 'parentEntId': 10002, 'pos': Point3(-2.34864, 2.16796, 0), 'hpr': Vec3(-141.716, 0, 0), 'scale': Vec3(1, 1, 1), 'gagLevel': 5, 'gagLevelMax': 0, 'gagTrack': 'random', 'rewardPerGrab': 5, 'rewardPerGrabMax': 0}, 10020: {'type': 'gear', 'name': 'upper', 'comment': '', 'parentEntId': 10044, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': Point3(1, 1, 1.6), 'degreesPerSec': -5.0, 'gearScale': 24.3, 'modelType': 'mint', 'orientation': 'horizontal', 'phaseShift': 0}, 10004: {'type': 'healBarrel', 'name': 'heal', 'comment': '', 'parentEntId': 10002, 'pos': Point3(0, -0.748415, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'rewardPerGrab': 6, 'rewardPerGrabMax': 8}, 10005: {'type': 'healBarrel', 'name': 'heal', 'comment': '', 'parentEntId': 10002, 'pos': Point3(-2.20196, -0.384304, 0), 'hpr': Vec3(-64.4313, 0, 0), 'scale': Vec3(1, 1, 1), 'rewardPerGrab': 6, 'rewardPerGrabMax': 8}, 10037: {'type': 'healBarrel', 'name': 'atTheEnd', 'comment': '', 'parentEntId': 10028, 'pos': Point3(64.2821, 42.851, 0), 'hpr': Vec3(274.907, 0, 0), 'scale': Vec3(1, 1, 1), 'rewardPerGrab': 5, 'rewardPerGrabMax': 0}, 100000: {'type': 'laserField', 'name': 'test trap', 'comment': '', 'parentEntId': 0, 'pos': Point3(0, 0, 0.0402111), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'cellId': 0, 'laserFactor': 3, 'modelPath': 0}, 10000: {'type': 'model', 'name': 'crate', 'comment': '', 'parentEntId': 10009, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10007: {'type': 'model', 'name': 'upper', 'comment': '', 'parentEntId': 10059, 'pos': Point3(0, 2, 5.5), 'hpr': Vec3(0, 0, 0), 'scale': 1, 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10008: {'type': 'model', 'name': 'crate', 'comment': '', 'parentEntId': 10009, 'pos': Point3(0, -5.79679, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10012: {'type': 'model', 'name': 'copy of crate', 'comment': '', 'parentEntId': 10011, 'pos': Point3(0, -5.79679, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10013: {'type': 'model', 'name': 'copy of crate (2)', 'comment': '', 'parentEntId': 10011, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10014: {'type': 'model', 'name': 'copy of crate (2)', 'comment': '', 'parentEntId': 10011, 'pos': Point3(-5.65285, -11.6495, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10015: {'type': 'model', 'name': 'copy of crate (2)', 'comment': '', 'parentEntId': 10011, 'pos': Point3(-5.8057, -5.79679, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10016: {'type': 'model', 'name': 'copy of crate (3)', 'comment': '', 'parentEntId': 10011, 'pos': Point3(-3.9383, -17.6478, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10018: {'type': 'model', 'name': 'copy of upper', 'comment': '', 'parentEntId': 10059, 'pos': Point3(0, -3.83362, 5.5), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10019: {'type': 'model', 'name': 'copy of upper (2)', 'comment': '', 'parentEntId': 10059, 'pos': Point3(0, -9.69305, 5.5), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10030: {'type': 'model', 'name': 'lastCrateStack', 'comment': '', 'parentEntId': 10029, 'pos': Point3(47.9849, 27.7105, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10031: {'type': 'model', 'name': 'upper', 'comment': '', 'parentEntId': 10030, 'pos': Point3(0, 0, 5.5), 'hpr': Vec3(0, 0, 0), 'scale': 1, 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10033: {'type': 'model', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10032, 'pos': Point3(-41.8699, -36.9582, 0), 'hpr': Point3(180, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cashbotHQ/pipes_D1.bam'}, 10034: {'type': 'model', 'name': 'crateStack', 'comment': '', 'parentEntId': 10029, 'pos': Point3(47.9849, -3.09667, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10035: {'type': 'model', 'name': 'upper', 'comment': '', 'parentEntId': 10034, 'pos': Point3(0, 0, 5.5), 'hpr': Vec3(0, 0, 0), 'scale': 1, 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10036: {'type': 'model', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10032, 'pos': Point3(0, -41.4516, 30.2685), 'hpr': Vec3(180, 0, 180), 'scale': Vec3(0.850346, 0.850346, 0.850346), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'}, 10041: {'type': 'model', 'name': 'crateStack', 'comment': '', 'parentEntId': 10040, 'pos': Point3(36.5905, -31.6759, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10042: {'type': 'model', 'name': 'upper', 'comment': '', 'parentEntId': 10041, 'pos': Point3(0, 0, 5.5), 'hpr': Vec3(0, 0, 0), 'scale': 1, 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10043: {'type': 'model', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10032, 'pos': Point3(19.5017, 84.0786, 10.0059), 'hpr': Vec3(171.254, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cashbotHQ/boiler_B1.bam'}, 10048: {'type': 'model', 'name': 'crate', 'comment': '', 'parentEntId': 10046, 'pos': Point3(0, 0, 8.25759), 'hpr': Vec3(0, 0, 0), 'scale': Point3(1.3, 1.3, 1.65), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10050: {'type': 'model', 'name': 'support', 'comment': '', 'parentEntId': 10046, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1, 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cashbotHQ/gears_C2.bam'}, 10052: {'type': 'model', 'name': 'crate', 'comment': '', 'parentEntId': 10051, 'pos': Point3(0, 0, 8.25759), 'hpr': Vec3(0, 0, 0), 'scale': Point3(1.3, 1.3, 1.65), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10053: {'type': 'model', 'name': 'support', 'comment': '', 'parentEntId': 10051, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1, 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cashbotHQ/gears_C2.bam'}, 10056: {'type': 'model', 'name': 'collision', 'comment': '', 'parentEntId': 10002, 'pos': Point3(-0.625704, 0.824797, 0), 'hpr': Vec3(318.366, 0, 0), 'scale': Vec3(0.644618, 0.64, 1.28726), 'collisionsOnly': 1, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'}, 10057: {'type': 'model', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10044, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(11.0614, 11.0614, 11.0614), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/RoundShadow.bam'}, 10058: {'type': 'model', 'name': 'shelf', 'comment': '', 'parentEntId': 10028, 'pos': Point3(62.9969, 21.7125, 0), 'hpr': Vec3(270, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cashbotHQ/shelf_A1.bam'}, 10062: {'type': 'model', 'name': 'copy of upper', 'comment': '', 'parentEntId': 10061, 'pos': Point3(0, -3.83362, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10063: {'type': 'model', 'name': 'copy of upper (2)', 'comment': '', 'parentEntId': 10061, 'pos': Point3(0, -9.69305, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10064: {'type': 'model', 'name': 'upper', 'comment': '', 'parentEntId': 10061, 'pos': Point3(0, 2, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1, 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'}, 10001: {'type': 'nodepath', 'name': 'crates', 'comment': '', 'parentEntId': 10028, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1.3, 1.3, 1.64892)}, 10002: {'type': 'nodepath', 'name': 'rewardBarrels', 'comment': '', 'parentEntId': 0, 'pos': Point3(-0.719734, 56.9691, 10.0021), 'hpr': Vec3(61.6992, 0, 0), 'scale': Vec3(1, 1, 1)}, 10003: {'type': 'nodepath', 'name': 'upperWall', 'comment': 'TODO: replace with lines of shelves', 'parentEntId': 0, 'pos': Point3(-20.3203, 52.6549, 9.90873), 'hpr': Vec3(270, 0, 0), 'scale': Vec3(1.1143, 1.1143, 1.1143)}, 10009: {'type': 'nodepath', 'name': 'toGear0', 'comment': '', 'parentEntId': 10001, 'pos': Point3(-26.5593, 31.856, 0), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1)}, 10011: {'type': 'nodepath', 'name': 'toGear1', 'comment': '', 'parentEntId': 10001, 'pos': Point3(-25.884, 13.6749, 0), 'hpr': Vec3(41.6335, 0, 0), 'scale': Vec3(1, 1, 1)}, 10023: {'type': 'nodepath', 'name': 'leftWall', 'comment': '', 'parentEntId': 10003, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1}, 10024: {'type': 'nodepath', 'name': 'rightWall', 'comment': '', 'parentEntId': 10003, 'pos': Point3(-26.7112, 6.85982, 0), 'hpr': Point3(180, 0, 0), 'scale': Vec3(1, 1, 1)}, 10028: {'type': 'nodepath', 'name': 'lowerPuzzle', 'comment': '', 'parentEntId': 0, 'pos': Point3(0, 0, 0.05), 'hpr': Vec3(0, 0, 0), 'scale': 1}, 10029: {'type': 'nodepath', 'name': 'entranceWall', 'comment': '', 'parentEntId': 10001, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1}, 10032: {'type': 'nodepath', 'name': 'props', 'comment': '', 'parentEntId': 0, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1}, 10038: {'type': 'nodepath', 'name': 'archStompers', 'comment': '', 'parentEntId': 10028, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1}, 10040: {'type': 'nodepath', 'name': 'backWall', 'comment': '', 'parentEntId': 10001, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1}, 10044: {'type': 'nodepath', 'name': 'gear', 'comment': '', 'parentEntId': 10028, 'pos': Point3(11.85, -11.38, 12.528), 'hpr': Vec3(0, 0, 0), 'scale': Vec3(1, 1, 1)}, 10046: {'type': 'nodepath', 'name': 'supportedCrateBackWall', 'comment': '', 'parentEntId': 10028, 'pos': Point3(34.9045, -34.0589, -1.51687), 'hpr': Vec3(63.4349, 0, 0), 'scale': Vec3(1, 1, 1)}, 10051: {'type': 'nodepath', 'name': 'supportedCrateEntrance', 'comment': '', 'parentEntId': 10028, 'pos': Point3(48.5077, 7.75915, 0.357897), 'hpr': Point3(0, 0, 0), 'scale': Vec3(1, 1, 1)}, 10059: {'type': 'nodepath', 'name': 'largeStack', 'comment': '', 'parentEntId': 10029, 'pos': Point3(47.98, -16.98, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1}, 10061: {'type': 'nodepath', 'name': 'lower', 'comment': '', 'parentEntId': 10059, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1}, 100001: {'type': 'nodepath', 'name': 'trap1 cog node', 'comment': '', 'parentEntId': 100000, 'pos': Point3(0, 0, 0), 'hpr': Vec3(0, 0, 0), 'scale': 1}, 10049: {'type': 'stomper', 'name': 'second', 'comment': '', 'parentEntId': 10038, 'pos': Point3(62.3685, -19.4457, 18.1217), 'hpr': Point3(0, 0, 0), 'scale': Vec3(1, 1, 1), 'animateShadow': 1, 'crushCellId': None, 'damage': 8, 'headScale': Point3(3.8, 4.3, 3.8), 'modelPath': 0, 'motion': 3, 'period': 3.0, 'phaseShift': 0.34, 'range': 7.0, 'removeCamBarrierCollisions': 0, 'removeHeadFloor': 1, 'shaftScale': Point3(1.71, 2.79, 1.71), 'soundLen': 0, 'soundOn': 1, 'soundPath': 1, 'style': 'vertical', 'switchId': 0, 'wantShadow': 1, 'wantSmoke': 1, 'zOffset': 0}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [Scenario0]}