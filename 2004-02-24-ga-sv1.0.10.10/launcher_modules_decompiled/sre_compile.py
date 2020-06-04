# File: s (Python 2.2)

import _sre
import sys
from sre_constants import *
MAXCODE = 65535

def _compile(code, pattern, flags):
    emit = code.append
    for (op, av) in pattern:
        if op in (LITERAL, NOT_LITERAL):
            if flags & SRE_FLAG_IGNORECASE:
                emit(OPCODES[OP_IGNORE[op]])
                emit(_sre.getlower(av, flags))
            else:
                emit(OPCODES[op])
                emit(av)
        elif op is IN:
            if flags & SRE_FLAG_IGNORECASE:
                emit(OPCODES[OP_IGNORE[op]])
                
                def fixup(literal, flags = flags):
                    return _sre.getlower(literal, flags)

            else:
                emit(OPCODES[op])
                
                fixup = lambda x: x
            skip = len(code)
            emit(0)
            _compile_charset(av, flags, code, fixup)
            code[skip] = len(code) - skip
        elif op is ANY:
            if flags & SRE_FLAG_DOTALL:
                emit(OPCODES[ANY_ALL])
            else:
                emit(OPCODES[ANY])
        elif op in (REPEAT, MIN_REPEAT, MAX_REPEAT):
            if flags & SRE_FLAG_TEMPLATE:
                raise error, 'internal: unsupported template operator'
                emit(OPCODES[REPEAT])
                skip = len(code)
                emit(0)
                emit(av[0])
                emit(av[1])
                _compile(code, av[2], flags)
                emit(OPCODES[SUCCESS])
                code[skip] = len(code) - skip
            elif _simple(av) and op == MAX_REPEAT:
                emit(OPCODES[REPEAT_ONE])
                skip = len(code)
                emit(0)
                emit(av[0])
                emit(av[1])
                _compile(code, av[2], flags)
                emit(OPCODES[SUCCESS])
                code[skip] = len(code) - skip
            else:
                emit(OPCODES[REPEAT])
                skip = len(code)
                emit(0)
                emit(av[0])
                emit(av[1])
                _compile(code, av[2], flags)
                code[skip] = len(code) - skip
                if op == MAX_REPEAT:
                    emit(OPCODES[MAX_UNTIL])
                else:
                    emit(OPCODES[MIN_UNTIL])
        elif op is SUBPATTERN:
            if av[0]:
                emit(OPCODES[MARK])
                emit((av[0] - 1) * 2)
            
            _compile(code, av[1], flags)
            if av[0]:
                emit(OPCODES[MARK])
                emit((av[0] - 1) * 2 + 1)
            
        elif op in (SUCCESS, FAILURE):
            emit(OPCODES[op])
        elif op in (ASSERT, ASSERT_NOT):
            emit(OPCODES[op])
            skip = len(code)
            emit(0)
            if av[0] >= 0:
                emit(0)
            else:
                (lo, hi) = av[1].getwidth()
                if lo != hi:
                    raise error, 'look-behind requires fixed-width pattern'
                
                emit(lo)
            _compile(code, av[1], flags)
            emit(OPCODES[SUCCESS])
            code[skip] = len(code) - skip
        elif op is CALL:
            emit(OPCODES[op])
            skip = len(code)
            emit(0)
            _compile(code, av, flags)
            emit(OPCODES[SUCCESS])
            code[skip] = len(code) - skip
        elif op is AT:
            emit(OPCODES[op])
            if flags & SRE_FLAG_MULTILINE:
                av = AT_MULTILINE.get(av, av)
            
            if flags & SRE_FLAG_LOCALE:
                av = AT_LOCALE.get(av, av)
            elif flags & SRE_FLAG_UNICODE:
                av = AT_UNICODE.get(av, av)
            
            emit(ATCODES[av])
        elif op is BRANCH:
            emit(OPCODES[op])
            tail = []
            for av in av[1]:
                skip = len(code)
                emit(0)
                _compile(code, av, flags)
                emit(OPCODES[JUMP])
                tail.append(len(code))
                emit(0)
                code[skip] = len(code) - skip
            
            emit(0)
            for tail in tail:
                code[tail] = len(code) - tail
            
        elif op is CATEGORY:
            emit(OPCODES[op])
            if flags & SRE_FLAG_LOCALE:
                av = CH_LOCALE[av]
            elif flags & SRE_FLAG_UNICODE:
                av = CH_UNICODE[av]
            
            emit(CHCODES[av])
        elif op is GROUPREF:
            if flags & SRE_FLAG_IGNORECASE:
                emit(OPCODES[OP_IGNORE[op]])
            else:
                emit(OPCODES[op])
            emit(av - 1)
        else:
            raise ValueError, ('unsupported operand type', op)
    


def _compile_charset(charset, flags, code, fixup = None):
    emit = code.append
    if not fixup:
        
        fixup = lambda x: x
    
    for (op, av) in _optimize_charset(charset, fixup):
        emit(OPCODES[op])
        if op is NEGATE:
            pass
        1
        if op is LITERAL:
            emit(fixup(av))
        elif op is RANGE:
            emit(fixup(av[0]))
            emit(fixup(av[1]))
        elif op is CHARSET:
            code.extend(av)
        elif op is BIGCHARSET:
            code.extend(av)
        elif op is CATEGORY:
            if flags & SRE_FLAG_LOCALE:
                emit(CHCODES[CH_LOCALE[av]])
            elif flags & SRE_FLAG_UNICODE:
                emit(CHCODES[CH_UNICODE[av]])
            else:
                emit(CHCODES[av])
        else:
            raise error, 'internal: unsupported set operator'
    
    emit(OPCODES[FAILURE])


def _optimize_charset(charset, fixup):
    out = []
    charmap = [
        0] * 256
    
    try:
        for (op, av) in charset:
            if op is NEGATE:
                out.append((op, av))
            elif op is LITERAL:
                charmap[fixup(av)] = 1
            elif op is RANGE:
                for i in range(fixup(av[0]), fixup(av[1]) + 1):
                    charmap[i] = 1
                
            elif op is CATEGORY:
                return charset
            
    except IndexError:
        if sys.maxunicode != 65535:
            return charset
        
        return _optimize_unicode(charset, fixup)

    i = 0
    p = 0
    n = 0
    runs = []
    for c in charmap:
        if c:
            if n == 0:
                p = i
            
            n = n + 1
        elif n:
            runs.append((p, n))
            n = 0
        
        i = i + 1
    
    if n:
        runs.append((p, n))
    
    if len(runs) <= 2:
        for (p, n) in runs:
            if n == 1:
                out.append((LITERAL, p))
            else:
                out.append((RANGE, (p, p + n - 1)))
        
        if len(out) < len(charset):
            return out
        
    else:
        data = _mk_bitmap(charmap)
        out.append((CHARSET, data))
        return out
    return charset


def _mk_bitmap(bits):
    data = []
    m = 1
    v = 0
    for c in bits:
        if c:
            v = v + m
        
        m = m << 1
        if m > MAXCODE:
            data.append(v)
            m = 1
            v = 0
        
    
    return data


def _optimize_unicode(charset, fixup):
    charmap = [
        0] * 65536
    negate = 0
    for (op, av) in charset:
        if op is NEGATE:
            negate = 1
        elif op is LITERAL:
            charmap[fixup(av)] = 1
        elif op is RANGE:
            for i in range(fixup(av[0]), fixup(av[1]) + 1):
                charmap[i] = 1
            
        elif op is CATEGORY:
            return charset
        
    
    if negate:
        for i in range(65536):
            charmap[i] = not charmap[i]
        
    
    comps = { }
    mapping = [
        0] * 256
    block = 0
    data = []
    for i in range(256):
        chunk = tuple(charmap[i * 256:(i + 1) * 256])
        new = comps.setdefault(chunk, block)
        mapping[i] = new
        if new == block:
            block = block + 1
            data = data + _mk_bitmap(chunk)
        
    
    header = [
        block]
    for i in range(128):
        if sys.byteorder == 'big':
            header.append(256 * mapping[2 * i] + mapping[2 * i + 1])
        else:
            header.append(mapping[2 * i] + 256 * mapping[2 * i + 1])
    
    data[0:0] = header
    return [
        (BIGCHARSET, data)]


def _simple(av):
    (lo, hi) = av[2].getwidth()
    if lo == 0 and hi == MAXREPEAT:
        raise error, 'nothing to repeat'
    
    if lo == hi:
        pass
    hi == 1
    if 1:
        pass
    return av[2][0][0] != SUBPATTERN


def _compile_info(code, pattern, flags):
    (lo, hi) = pattern.getwidth()
    if lo == 0:
        return None
    
    prefix = []
    prefix_skip = 0
    charset = []
    if not (flags & SRE_FLAG_IGNORECASE):
        for (op, av) in pattern.data:
            if op is LITERAL:
                if len(prefix) == prefix_skip:
                    prefix_skip = prefix_skip + 1
                
                prefix.append(av)
            elif op is SUBPATTERN and len(av[1]) == 1:
                (op, av) = av[1][0]
                if op is LITERAL:
                    prefix.append(av)
                else:
                    break
            else:
                break
        
        if not prefix and pattern.data:
            (op, av) = pattern.data[0]
            if op is SUBPATTERN and av[1]:
                (op, av) = av[1][0]
                if op is LITERAL:
                    charset.append((op, av))
                elif op is BRANCH:
                    c = []
                    for p in av[1]:
                        if not p:
                            break
                        
                        (op, av) = p[0]
                        if op is LITERAL:
                            c.append((op, av))
                        else:
                            break
                    else:
                        charset = c
                
            elif op is BRANCH:
                c = []
                for p in av[1]:
                    if not p:
                        break
                    
                    (op, av) = p[0]
                    if op is LITERAL:
                        c.append((op, av))
                    else:
                        break
                else:
                    charset = c
            elif op is IN:
                charset = av
            
        
    
    emit = code.append
    emit(OPCODES[INFO])
    skip = len(code)
    emit(0)
    mask = 0
    if prefix:
        mask = SRE_INFO_PREFIX
        if len(prefix) == prefix_skip:
            pass
        prefix_skip == len(pattern.data)
        if 1:
            mask = mask + SRE_INFO_LITERAL
        
    elif charset:
        mask = mask + SRE_INFO_CHARSET
    
    emit(mask)
    if lo < MAXCODE:
        emit(lo)
    else:
        emit(MAXCODE)
        prefix = prefix[:MAXCODE]
    if hi < MAXCODE:
        emit(hi)
    else:
        emit(0)
    if prefix:
        emit(len(prefix))
        emit(prefix_skip)
        code.extend(prefix)
        table = [
            -1] + [
            0] * len(prefix)
        for i in range(len(prefix)):
            table[i + 1] = table[i] + 1
            while table[i + 1] > 0 and prefix[i] != prefix[table[i + 1] - 1]:
                table[i + 1] = table[table[i + 1] - 1] + 1
        
        code.extend(table[1:])
    elif charset:
        _compile_charset(charset, 0, code)
    
    code[skip] = len(code) - skip

STRING_TYPES = [
    type('')]

try:
    STRING_TYPES.append(type(unicode('')))
except NameError:
    pass


def _code(p, flags):
    flags = p.pattern.flags | flags
    code = []
    _compile_info(code, p, flags)
    _compile(code, p.data, flags)
    code.append(OPCODES[SUCCESS])
    return code


def compile(p, flags = 0):
    if type(p) in STRING_TYPES:
        import sre_parse
        pattern = p
        p = sre_parse.parse(p, flags)
    else:
        pattern = None
    code = _code(p, flags)
    groupindex = p.pattern.groupdict
    indexgroup = [
        None] * p.pattern.groups
    for (k, i) in groupindex.items():
        indexgroup[i] = k
    
    return _sre.compile(pattern, flags, code, p.pattern.groups - 1, groupindex, indexgroup)

