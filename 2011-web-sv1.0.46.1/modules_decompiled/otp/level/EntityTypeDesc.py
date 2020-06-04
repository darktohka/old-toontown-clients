# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\EntityTypeDesc.py
from direct.directnotify import DirectNotifyGlobal
import AttribDesc
from direct.showbase.PythonUtil import mostDerivedLast

class EntityTypeDesc:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('EntityTypeDesc')
    output = None

    def __init__(self):
        self.__class__.privCompileAttribDescs(self.__class__)
        self.attribNames = []
        self.attribDescDict = {}
        attribDescs = self.__class__._attribDescs
        for desc in attribDescs:
            attribName = desc.getName()
            self.attribNames.append(attribName)
            self.attribDescDict[attribName] = desc

    def isConcrete(self):
        return not self.__class__.__dict__.has_key('abstract')

    def isPermanent(self):
        return self.__class__.__dict__.has_key('permanent')

    def getOutputType(self):
        return self.output

    def getAttribNames(self):
        return self.attribNames

    def getAttribDescDict(self):
        return self.attribDescDict

    def getAttribsOfType(self, type):
        names = []
        for (attribName, desc) in self.attribDescDict.items():
            if desc.getDatatype() == type:
                names.append(attribName)

        return names

    @staticmethod
    def privCompileAttribDescs(entTypeClass):
        if entTypeClass.__dict__.has_key('_attribDescs'):
            return
        c = entTypeClass
        EntityTypeDesc.notify.debug('compiling attrib descriptors for %s' % c.__name__)
        for base in c.__bases__:
            EntityTypeDesc.privCompileAttribDescs(base)

        blockAttribs = c.__dict__.get('blockAttribs', [])
        baseADs = []
        bases = list(c.__bases__)
        mostDerivedLast(bases)
        for base in bases:
            for desc in base._attribDescs:
                if desc.getName() in blockAttribs:
                    continue
                for d in baseADs:
                    if desc.getName() == d.getName():
                        EntityTypeDesc.notify.warning('%s inherits attrib %s from multiple bases' % (c.__name__, desc.getName()))
                        break
                else:
                    baseADs.append(desc)

        attribDescs = []
        if c.__dict__.has_key('attribs'):
            for attrib in c.attribs:
                desc = AttribDesc.AttribDesc(*attrib)
                if desc.getName() == 'type' and entTypeClass.__name__ != 'Entity':
                    EntityTypeDesc.notify.error("(%s): '%s' is a reserved attribute name" % (entTypeClass.__name__, desc.getName()))
                for ad in baseADs:
                    if ad.getName() == desc.getName():
                        baseADs.remove(ad)
                        break

                attribDescs.append(desc)

        c._attribDescs = baseADs + attribDescs

    def __str__(self):
        return str(self.__class__)

    def __repr__(self):
        return str(self.__class__.__dict__.get('type', None)) + str(self.output) + str(self.attribDescDict)