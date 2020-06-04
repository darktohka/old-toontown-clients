# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\EntityTypes.py
from EntityTypeDesc import EntityTypeDesc
from toontown.coghq.SpecImports import *

class Entity(EntityTypeDesc):
    __module__ = __name__
    abstract = 1
    type = 'entity'
    attribs = (('type', None, 'const'), ('name', '<unnamed>', 'string'), ('comment', '', 'string'), ('parentEntId', 0, 'entId'))


class LevelMgr(Entity):
    __module__ = __name__
    type = 'levelMgr'
    permanent = 1
    attribs = (('name', 'LevelMgr', 'const'), ('parentEntId', 0, 'const'), ('modelFilename', '', 'const'))


class EditMgr(Entity):
    __module__ = __name__
    type = 'editMgr'
    permanent = 1
    blockAttribs = ('comment', )
    attribs = (
     ('name', 'LevelMgr', 'const'), ('parentEntId', 0, 'const'), ('requestSave', None, 'const'), ('requestNewEntity', None, 'const'), ('insertEntity', None, 'const'), ('removeEntity', None, 'const'))


class AttribModifier(Entity):
    __module__ = __name__
    type = 'attribModifier'
    attribs = (('recursive', 0, 'bool'), ('typeName', '', 'string'), ('attribName', '', 'string'), ('value', '', 'string'))


class Locator(Entity):
    __module__ = __name__
    type = 'locator'
    attribs = (('searchPath', '', 'string'), )


class Nodepath(Entity):
    __module__ = __name__
    type = 'nodepath'
    attribs = (('parentEntId', 0, 'entId', {'type': 'nodepath'}), ('pos', Point3(0, 0, 0), 'pos'), ('hpr', Vec3(0, 0, 0), 'hpr'), ('scale', 1, 'scale'))


class Zone(Nodepath):
    __module__ = __name__
    type = 'zone'
    permanent = 1
    blockAttribs = ('pos', 'hpr')
    attribs = (
     ('parentEntId', 0, 'const'), ('description', '', 'string'), ('visibility', [], 'visZoneList'))


class EntrancePoint(Nodepath):
    __module__ = __name__
    type = 'entrancePoint'
    attribs = (('entranceId', -1, 'int'), ('radius', 15, 'float', {'min': 0}), ('theta', 20, 'float', {'min': 0}))


class LogicGate(Entity):
    __module__ = __name__
    type = 'logicGate'
    output = 'bool'
    attribs = (('input1Event', 0, 'entId', {'output': 'bool'}), ('input2Event', 0, 'entId', {'output': 'bool'}), ('isInput1', 0, 'bool'), ('isInput2', 0, 'bool'), ('logicType', 'or', 'choice', {'choiceSet': ['or', 'and', 'xor', 'nand', 'nor', 'xnor']}))


class CutScene(Entity):
    __module__ = __name__
    type = 'cutScene'
    output = 'bool'
    attribs = (('pos', Point3(0, 0, 0), 'pos'), ('hpr', Vec3(0, 0, 0), 'hpr'), ('startStopEvent', 0, 'entId', {'output': 'bool'}), ('effect', 'irisInOut', 'choice', {'choiceSet': ['nothing', 'irisInOut', 'letterBox']}), ('motion', 'foo1', 'choice', {'choiceSet': ['foo1']}), ('duration', 5.0, 'float'))


class CollisionSolid(Nodepath):
    __module__ = __name__
    type = 'collisionSolid'
    attribs = (('solidType', 'sphere', 'choice', {'choiceSet': ['sphere', 'tube']}), ('radius', 1.0, 'float'), ('length', 0.0, 'float'), ('showSolid', 0, 'bool'))


class Model(Nodepath):
    __module__ = __name__
    type = 'model'
    attribs = (('loadType', 'loadModelCopy', 'choice', {'choiceSet': ['loadModelCopy', 'loadModel', 'loadModelOnce']}), ('modelPath', None, 'bamfilename'), ('flattenType', 'light', 'choice', {'choiceSet': ['none', 'light', 'medium', 'strong']}), ('collisionsOnly', 0, 'bool'), ('goonHatType', 'none', 'choice', {'choiceSet': ['none', 'hardhat', 'security']}))


class Path(Nodepath):
    __module__ = __name__
    type = 'path'
    attribs = (('pathIndex', 0, 'int'), ('pathScale', 1.0, 'float'))


class VisibilityExtender(Entity):
    __module__ = __name__
    type = 'visibilityExtender'
    attribs = (('event', None, 'entId', {'output': 'bool'}), ('newZones', [], 'visZoneList'))


class AmbientSound(Nodepath):
    __module__ = __name__
    type = 'ambientSound'
    attribs = (('soundPath', '', 'bamfilename'), ('volume', 1, 'float', {'min': 0, 'max': 1}), ('enabled', 1, 'bool'))


class PropSpinner(Entity):
    __module__ = __name__
    type = 'propSpinner'


class EntityGroup(Entity):
    __module__ = __name__
    type = 'entityGroup'