# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\EntityStateVarSet.py
from direct.fsm.StatePush import StateVar
from direct.showbase.PythonUtil import getSetterName
from otp.level.Entity import Entity

class EntityStateVarSet(Entity):
    __module__ = __name__

    def __init__(self, entType):
        self._entType = entType
        self._attribNames = []
        for attrib in self._entType.attribs:
            (name, defaultVal, type) = attrib
            self._addAttrib(name, defaultVal, type)

    def initializeEntity(self, level, entId):
        stateVars = {}
        for attribName in self._attribNames:
            stateVars[attribName] = getattr(self, attribName)

        Entity.initializeEntity(self, level, entId)
        for attribName in self._attribNames:
            stateVars[attribName].set(getattr(self, attribName))

        for attribName in self._attribNames:
            setattr(self, attribName, stateVars[attribName])

    def _getAttributeNames(self):
        return self._attribNames[:]

    def _setter(self, name, value):
        getattr(self, name).set(value)

    def _addAttrib(self, name, defaultVal, type):
        setattr(self, name, StateVar(defaultVal))
        setattr(self, getSetterName(name), Functor(self._setter, name))
        self._attribNames.append(name)