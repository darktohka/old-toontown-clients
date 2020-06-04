# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\BpDb.py
import inspect, sys

class BpMan:
    __module__ = __name__

    def __init__(self):
        self.bpInfos = {}

    def partsToPath(self, parts):
        cfg = parts.get('cfg')
        grp = parts.get('grp')
        id = parts.get('id', '*')
        path = ''
        if cfg:
            path += '%s' % (cfg,)
            if grp or id:
                path += '::'
        if grp:
            path += '%s' % (grp,)
        if isinstance(id, int):
            path += '(%s)' % (id,)
        elif grp:
            path += '.%s' % (id,)
        else:
            path += '%s' % (id,)
        return path

    def pathToParts(self, path=None):
        parts = {'cfg': None, 'grp': None, 'id': None}
        if not isinstance(path, type('')):
            return parts
        tokens = path.split('::')
        if len(tokens) > 1 and len(tokens[0]) > 0:
            parts['cfg'] = tokens[0]
            path = tokens[1]
        tokens = path.split('.')
        if len(tokens) == 1:
            tokens = path.rsplit(')', 1)
            if len(tokens) > 1 and tokens[(-1)] == '':
                tokens = tokens[(-2)].rsplit('(', 1)
                if len(tokens) > 1:
                    try:
                        verifyInt = int(tokens[(-1)])
                        parts['grp'] = tokens[0]
                        path = tokens[(-1)]
                    except:
                        pass

        elif len(tokens) > 1 and len(tokens[0]) > 0:
            parts['grp'] = tokens[0]
            path = tokens[1]
        if len(path) > 0:
            parts['id'] = path
        if parts['id'] == '*':
            parts['id'] = None
        return parts

    def bpToPath(self, bp):
        if type(bp) is type(''):
            bp = self.pathToParts(bp)
        return self.partsToPath(bp)

    def bpToParts(self, bp):
        if type(bp) is type({}):
            bp = self.partsToPath(bp)
        return self.pathToParts(bp)

    def makeBpInfo(self, grp, id):
        self.bpInfos.setdefault(grp, {None: {}})
        self.bpInfos[grp].setdefault(id, {})
        return

    def getEnabled(self, bp):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(parts['grp'], parts['id'])
        if not self.bpInfos[grp][None].get('enabled', True):
            return False
        if not self.bpInfos[grp][id].get('enabled', True):
            return False
        return True

    def setEnabled(self, bp, enabled=True):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        self.bpInfos[grp][id]['enabled'] = enabled
        return enabled

    def toggleEnabled(self, bp):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        newEnabled = not self.bpInfos[grp][id].get('enabled', True)
        self.bpInfos[grp][id]['enabled'] = newEnabled
        return newEnabled

    def getIgnoreCount(self, bp, decrement=False):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        ignoreCount = self.bpInfos[grp][id].get('ignoreCount', 0)
        if ignoreCount > 0 and decrement:
            self.bpInfos[grp][id]['ignoreCount'] = ignoreCount - 1
        return ignoreCount

    def setIgnoreCount(self, bp, ignoreCount=0):
        if not isinstance(ignoreCount, int):
            print 'error: first argument should be integer ignoreCount'
            return
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        self.bpInfos[grp][id]['ignoreCount'] = ignoreCount
        return ignoreCount

    def getLifetime(self, bp):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        lifetime = self.bpInfos[grp][id].get('lifetime', -1)
        return lifetime

    def setLifetime(self, bp, newLifetime):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        self.bpInfos[grp][id]['lifetime'] = newLifetime
        return lifetime

    def decLifetime(self, bp):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        lifetime = self.bpInfos[grp][id].get('lifetime', -1)
        if lifetime > 0:
            lifetime = lifetime - 1
        self.bpInfos[grp][id]['lifetime'] = lifetime
        return lifetime

    def getHitCount(self, bp):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        return self.bpInfos[grp][id].get('count', 0)

    def setHitCount(self, bp, newHitCount):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        self.bpInfos[grp][id]['count'] = newHitCount

    def incHitCount(self, bp):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        self.bpInfos[grp][id]['count'] = self.bpInfos[grp][id].get('count', 0) + 1

    def resetBp(self, bp):
        parts = self.bpToParts(bp)
        grp, id = parts['grp'], parts['id']
        self.makeBpInfo(grp, id)
        self.bpInfos[grp][id] = {}
        if id is None:
            del self.bpInfos[grp]
        return


class BpDb:
    __module__ = __name__

    def __init__(self):
        self.enabled = True
        self.cfgInfos = {None: True}
        self.codeInfoCache = {}
        self.bpMan = BpMan()
        self.lastBp = None
        self.pdbAliases = {}
        self.configCallback = None
        return

    def setEnabledCallback(self, callback):
        self.enabledCallback = callback

    def verifyEnabled(self):
        if self.enabledCallback:
            return self.enabledCallback()
        return True

    def setConfigCallback(self, callback):
        self.configCallback = callback

    def verifySingleConfig(self, cfg):
        if cfg in self.cfgInfos:
            return self.cfgInfos[cfg]
        return not self.configCallback or self.configCallback(cfg)

    def verifyConfig(self, cfg):
        cfgList = choice(isinstance(cfg, tuple), cfg, (cfg,))
        passedCfgs = [ c for c in cfgList if self.verifySingleConfig(c) ]
        return len(passedCfgs) > 0

    def toggleConfig(self, cfg):
        self.cfgInfos[cfg] = not self.verifyConfig(cfg)
        return self.cfgInfos[cfg]

    def resetConfig(self, cfg):
        self.cfgInfos.pop(cfg, None)
        return

    def displayHelp(self):
        print 'You may use normal pdb commands plus the following:'
        print '    _i   [n <0> [, path=<curr>]] set ignore count for bp [path] to [n]'
        print '    _t   [path <curr>]   toggle bp [path]'
        print '    _tg  [grp <curr>]    toggle grp'
        print '    _tc  [cfg <curr>]    toggle cfg'
        print '    _z   [path <curr>]   clear all settings for bp [path]'
        print '    _zg  [grp <curr>]    clear all settings for grp'
        print '    _zc  [cfg <curr>]    clear all settings for cfg (restore .prc setting)'
        print '    _h                   displays this usage help'
        print '    _ua                  unalias these commands from pdb'

    def addPdbAliases(self):
        self.makePdbAlias('_i', 'bpdb._i(%*)')
        self.makePdbAlias('_t', 'bpdb._t(%*)')
        self.makePdbAlias('_tg', 'bpdb._tg(%*)')
        self.makePdbAlias('_tc', 'bpdb._tc(%*)')
        self.makePdbAlias('_z', 'bpdb._z(%*)')
        self.makePdbAlias('_zg', 'bpdb._zg(%*)')
        self.makePdbAlias('_zc', 'bpdb._zc(%*)')
        self.makePdbAlias('_h', 'bpdb.displayHelp()')
        self.makePdbAlias('_ua', 'bpdb.removePdbAliases()')

    def makePdbAlias(self, aliasName, aliasCmd):
        self.pdbAliases[aliasName] = aliasCmd
        self.pdb.do_alias('%s %s' % (aliasName, aliasCmd))

    def removePdbAliases(self):
        for aliasName in self.pdbAliases.iterkeys():
            self.pdb.do_unalias(aliasName)

        self.pdbAliases = {}
        print '(bpdb aliases removed)'

    def _e(self, *args, **kwargs):
        bp = self._getArg(args, [type(''), type({})], kwargs, ['path', 'bp', 'name'], self.lastBp)
        enabled = self._getArg(args, [type(True), type(1)], kwargs, ['enabled', 'on'], True)
        newEnabled = self.bpMan.setEnabled(bp, enabled)
        print "'%s' is now %s." % (self.bpMan.bpToPath(bp), choice(newEnabled, 'enabled', 'disabled'))

    def _i(self, *args, **kwargs):
        bp = self._getArg(args, [type(''), type({})], kwargs, ['path', 'bp', 'name'], self.lastBp)
        count = self._getArg(args, [type(1)], kwargs, ['ignoreCount', 'count', 'n'], 0)
        newCount = self.bpMan.setIgnoreCount(bp, count)
        print "'%s' will ignored %s times." % (self.bpMan.bpToPath(bp), newCount)

    def _t(self, *args, **kwargs):
        bp = self._getArg(args, [type(''), type({})], kwargs, ['path', 'bp', 'name'], self.lastBp)
        newEnabled = self.bpMan.toggleEnabled(bp)
        print "'%s' is now %s." % (self.bpMan.bpToPath(bp), choice(newEnabled, 'enabled', 'disabled'))

    def _tg(self, *args, **kwargs):
        bp = self._getArg(args, [type(''), type({})], kwargs, ['grp'], self.lastBp)
        if type(bp) == type(''):
            bp = {'grp': bp}
        bp = {'grp': bp.get('grp')}
        newEnabled = self.bpMan.toggleEnabled(bp)
        print "'%s' is now %s." % (self.bpMan.bpToPath(bp), choice(newEnabled, 'enabled', 'disabled'))

    def _tc(self, *args, **kwargs):
        bp = self._getArg(args, [type(''), type({})], kwargs, ['cfg'], self.lastBp)
        if type(bp) == type(''):
            bp = {'cfg': bp}
        bp = {'cfg': bp.get('cfg')}
        newEnabled = self.toggleConfig(bp['cfg'])
        print "'%s' is now %s." % (self.bpMan.bpToPath(bp), choice(newEnabled, 'enabled', 'disabled'))

    def _z(self, *args, **kwargs):
        bp = self._getArg(args, [type(''), type({})], kwargs, ['path', 'bp', 'name'], self.lastBp)
        self.bpMan.resetBp(bp)
        print "'%s' has been reset." % (self.bpMan.partsToPath(bp),)

    def _zg(self, *args, **kwargs):
        bp = self._getArg(args, [type(''), type({})], kwargs, ['grp'], self.lastBp)
        if type(bp) == type(''):
            bp = {'grp': bp}
        bp = {'grp': bp.get('grp')}
        self.bpMan.resetBp(bp)
        print "'%s' has been reset." % (self.bpMan.partsToPath(bp),)

    def _zc(self, *args, **kwargs):
        bp = self._getArg(args, [type(''), type({})], kwargs, ['cfg'], self.lastBp)
        if type(bp) == type(''):
            bp = {'cfg': bp}
        bp = {'cfg': bp.get('cfg')}
        self.resetConfig(bp['cfg'])
        print "'%s' has been reset." % (self.bpMan.bpToPath(bp),)

    def _getArg(self, args, goodTypes, kwargs, goodKeys, default=None):
        argVal = default
        for val in args:
            if type(val) in goodTypes:
                argVal = val

        for key in goodKeys:
            if key in kwargs:
                argVal = kwargs[key]

        return argVal

    def getFrameCodeInfo(self, frameCount=1):
        stack = inspect.stack()
        try:
            primaryFrame = stack[frameCount][0]
        except:
            return ('<stdin>', None, -1)

        moduleName = None
        callingModule = inspect.getmodule(primaryFrame)
        if callingModule and callingModule.__name__ != '__main__':
            moduleName = callingModule.__name__
        className = None
        for i in range(frameCount, len(stack)):
            callingContexts = stack[i][4]
            if callingContexts:
                contextTokens = callingContexts[0].split()
                if contextTokens[0] in ['class', 'def'] and len(contextTokens) > 1:
                    callingContexts[0] = callingContexts[0].replace('(', ' ').replace(':', ' ')
                    contextTokens = callingContexts[0].split()
                    className = contextTokens[1]
                    break

        if className is None:
            slf = primaryFrame.f_locals.get('self')
            try:
                if slf:
                    className = slf.__class__.__name__
            except:
                pass

        def byteOffsetToLineno(code, byte):
            import array
            lnotab = array.array('B', code.co_lnotab)
            line = code.co_firstlineno
            for i in range(0, len(lnotab), 2):
                byte -= lnotab[i]
                if byte <= 0:
                    return line
                line += lnotab[(i + 1)]

            return line

        lineNumber = byteOffsetToLineno(primaryFrame.f_code, primaryFrame.f_lasti)
        codeInfo = (
         moduleName, className, lineNumber)
        return codeInfo

    def set_trace(self, bp, frameCount=1):
        self.currFrame = sys._getframe()
        interactFrame = self.currFrame
        while frameCount > 0:
            interactFrame = interactFrame.f_back
            frameCount -= 1

        self.lastBp = bp.getParts()
        import pdb
        self.pdb = pdb.Pdb()
        self.addPdbAliases()
        self.pdb.set_trace(interactFrame)

    def bp(self, id=None, grp=None, cfg=None, iff=True, enabled=True, test=None, frameCount=1):
        if not (self.enabled and self.verifyEnabled()):
            return
        if not (enabled and iff):
            return
        bpi = bp(id=id, grp=grp, cfg=cfg, frameCount=frameCount + 1)
        bpi.maybeBreak(test=test, frameCount=frameCount + 1)

    def bpCall(self, id=None, grp=None, cfg=None, iff=True, enabled=True, test=None, frameCount=1, onEnter=1, onExit=0):

        def decorator(f):
            return f

        if not (self.enabled and self.verifyEnabled()):
            return decorator
        if not (enabled and iff):
            return decorator
        bpi = bp(id=id, grp=grp, cfg=cfg, frameCount=frameCount + 1)
        if bpi.disabled:
            return decorator

        def decorator(f):

            def wrap(*args, **kwds):
                dbp = bp(id=id or f.__name__, grp=bpi.grp, cfg=bpi.cfg, frameCount=frameCount + 1)
                if onEnter:
                    dbp.maybeBreak(test=test, frameCount=frameCount + 1, displayPrefix='Calling ')
                f_result = f(*args, **kwds)
                if onExit:
                    dbp.maybeBreak(test=test, frameCount=frameCount + 1, displayPrefix='Exited ')
                return f_result

            wrap.func_name = f.func_name
            wrap.func_dict = f.func_dict
            wrap.func_doc = f.func_doc
            wrap.__module__ = f.__module__
            return wrap

        return decorator

    def bpPreset(self, *args, **kArgs):

        def functor(*cArgs, **ckArgs):
            pass

        if kArgs.get('call', None):

            def functor(*cArgs, **ckArgs):

                def decorator(f):
                    return f

                return decorator

        if self.enabled and self.verifyEnabled():
            argsCopy = args[:]

            def functor(*cArgs, **ckArgs):
                kwArgs = {}
                kwArgs.update(kArgs)
                kwArgs.update(ckArgs)
                kwArgs.pop('static', None)
                kwArgs['frameCount'] = ckArgs.get('frameCount', 1) + 1
                if kwArgs.pop('call', None):
                    return self.bpCall(*cArgs, **kwArgs)
                else:
                    return self.bp(*cArgs, **kwArgs)
                return

        if kArgs.get('static', None):
            return staticmethod(functor)
        else:
            return functor
        return

    @staticmethod
    def bpGroup(*args, **kArgs):
        print 'BpDb.bpGroup is deprecated, use bpdb.bpPreset instead'
        kwArgs = {}
        kwArgs.update(kArgs)
        kwArgs['frameCount'] = kArgs.get('frameCount', 1) + 1
        return bpdb.bpPreset(*args, **kwArgs)


class bp:
    __module__ = __name__

    def __init__(self, id=None, grp=None, cfg=None, frameCount=1):
        self.disabled = False
        if not bpdb.enabled:
            self.disabled = True
            return
        (moduleName, className, lineNumber) = bpdb.getFrameCodeInfo(frameCount=frameCount + 1)
        if moduleName:
            moduleName = moduleName.split('.')[(-1)]
        self.grp = grp or className or moduleName
        self.id = id or lineNumber
        if cfg is None and moduleName:
            cfg = moduleName.lower()
            if cfg.find('distributed') == 0:
                cfg = cfg[len('distributed'):]
        self.cfg = cfg
        if not bpdb.verifyConfig(self.cfg):
            self.disabled = True
            return
        return

    def getParts(self):
        return {'id': self.id, 'grp': self.grp, 'cfg': self.cfg}

    def displayContextHint(self, displayPrefix=''):
        contextString = displayPrefix + bpdb.bpMan.partsToPath({'id': self.id, 'grp': self.grp, 'cfg': self.cfg})
        dashes = '-' * max(0, (80 - len(contextString) - 4) / 2)
        print '<%s %s %s>' % (dashes, contextString, dashes)

    def maybeBreak(self, test=None, frameCount=1, displayPrefix=''):
        if self.shouldBreak(test=test):
            self.doBreak(frameCount=frameCount + 1, displayPrefix=displayPrefix)

    def shouldBreak(self, test=None):
        if self.disabled:
            return False
        if test:
            if not isinstance(test, (list, tuple)):
                test = (
                 test,)
            for atest in test:
                if not atest():
                    return False

        if not bpdb.bpMan.getEnabled({'grp': self.grp, 'id': self.id}):
            return False
        if not bpdb.verifyConfig(self.cfg):
            return False
        if bpdb.bpMan.getIgnoreCount({'grp': self.grp, 'id': self.id}, decrement=True):
            return False
        if bpdb.bpMan.getLifetime({'grp': self.grp, 'id': self.id}) == 0:
            return False
        return True

    def doBreak(self, frameCount=1, displayPrefix=''):
        bpdb.bpMan.decLifetime({'grp': self.grp, 'id': self.id})
        bpdb.bpMan.incHitCount({'grp': self.grp, 'id': self.id})
        self.displayContextHint(displayPrefix=displayPrefix)
        bpdb.set_trace(self, frameCount=frameCount + 1)