# File: C (Python 2.2)

from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE07a',
        'wantDoors': 1 },
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None },
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': [] },
    10001: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-27.3600006104, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'cellId': 0,
        'radius': 10.0 },
    10002: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(57.021869659399997, 3.7922432422600001, 0.0),
        'hpr': Vec3(111.037513733, 0.0, 0.0),
        'scale': Vec3(1.7259607315100001, 1.7259607315100001, 1.7259607315100001),
        'collisionsOnly': 0,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/boiler_B1.bam' },
    10004: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-7.6732335090600001, -61.404102325399997, 0.20731438696400001),
        'hpr': Vec3(169.69515991200001, 0.0, 0.0),
        'scale': Vec3(1.9143627882000001, 1.9143627882000001, 1.9143627882000001),
        'collisionsOnly': 0,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/boiler_A2.bam' },
    10005: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-25.9598789215, 44.826011657700001, 9.7355136871300001),
        'hpr': Vec3(94.085617065400001, 0.0, 0.0),
        'scale': Vec3(1.53790044785, 1.53790044785, 1.53790044785),
        'collisionsOnly': 0,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_F1.bam' },
    10000: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-52.790771484399997, 0.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10003: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 } }
Scenario0 = { }
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0] }
