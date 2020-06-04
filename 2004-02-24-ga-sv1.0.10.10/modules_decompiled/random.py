# File: r (Python 2.2)

from math import log as _log, exp as _exp, pi as _pi, e as _e
from math import sqrt as _sqrt, acos as _acos, cos as _cos, sin as _sin
from math import floor as _floor
__all__ = [
    'Random',
    'seed',
    'random',
    'uniform',
    'randint',
    'choice',
    'randrange',
    'shuffle',
    'normalvariate',
    'lognormvariate',
    'cunifvariate',
    'expovariate',
    'vonmisesvariate',
    'gammavariate',
    'stdgamma',
    'gauss',
    'betavariate',
    'paretovariate',
    'weibullvariate',
    'getstate',
    'setstate',
    'jumpahead',
    'whseed']

def _verify(name, computed, expected):
    if abs(computed - expected) > 9.9999999999999995e-008:
        raise ValueError('computed value for %s deviates too much (computed %g, expected %g)' % (name, computed, expected))
    

NV_MAGICCONST = 4 * _exp(-0.5) / _sqrt(2.0)
_verify('NV_MAGICCONST', NV_MAGICCONST, 1.71552776992141)
TWOPI = 2.0 * _pi
_verify('TWOPI', TWOPI, 6.2831853071800001)
LOG4 = _log(4.0)
_verify('LOG4', LOG4, 1.3862943611198899)
SG_MAGICCONST = 1.0 + _log(4.5)
_verify('SG_MAGICCONST', SG_MAGICCONST, 2.5040773967762702)
del _verify

class Random:
    VERSION = 1
    
    def __init__(self, x = None):
        self.seed(x)

    
    def seed(self, a = None):
        if a is None:
            import time
            a = long(time.time() * 256)
        
        if type(a) not in (type(3), type(0x3L)):
            a = hash(a)
        
        (a, x) = divmod(a, 30268)
        (a, y) = divmod(a, 30306)
        (a, z) = divmod(a, 30322)
        self._seed = (int(x) + 1, int(y) + 1, int(z) + 1)
        self.gauss_next = None

    
    def random(self):
        (x, y, z) = self._seed
        x = 171 * x % 30269
        y = 172 * y % 30307
        z = 170 * z % 30323
        self._seed = (x, y, z)
        return (x / 30269.0 + y / 30307.0 + z / 30323.0) % 1.0

    
    def getstate(self):
        return (self.VERSION, self._seed, self.gauss_next)

    
    def setstate(self, state):
        version = state[0]
        if version == 1:
            (version, self._seed, self.gauss_next) = state
        else:
            raise ValueError('state with version %s passed to Random.setstate() of version %s' % (version, self.VERSION))

    
    def jumpahead(self, n):
        if not (n >= 0):
            raise ValueError('n must be >= 0')
        
        (x, y, z) = self._seed
        x = int(x * pow(171, n, 30269)) % 30269
        y = int(y * pow(172, n, 30307)) % 30307
        z = int(z * pow(170, n, 30323)) % 30323
        self._seed = (x, y, z)

    
    def _Random__whseed(self, x = 0, y = 0, z = 0):
        if type(x) == type(y) and type(y) == type(z):
            pass
        type(z) == type(0)
        if not 1:
            raise TypeError('seeds must be integers')
        
        if 0 <= x:
            pass
        x < 256
        if 1:
            if 0 <= y:
                pass
            y < 256
            if 1:
                if 0 <= z:
                    pass
                z < 256
        if not 1:
            raise ValueError('seeds must be in range(0, 256)')
        
        if 0 == x and x == y:
            pass
        y == z
        if 1:
            import time
            t = long(time.time() * 256)
            t = int(t & 16777215 ^ t >> 24)
            (t, x) = divmod(t, 256)
            (t, y) = divmod(t, 256)
            (t, z) = divmod(t, 256)
        
        if not x:
            pass
        if not y:
            pass
        if not z:
            pass
        self._seed = (1, 1, 1)
        self.gauss_next = None

    
    def whseed(self, a = None):
        if a is None:
            self._Random__whseed()
            return None
        
        a = hash(a)
        (a, x) = divmod(a, 256)
        (a, y) = divmod(a, 256)
        (a, z) = divmod(a, 256)
        if not (x + a) % 256:
            pass
        x = 1
        if not (y + a) % 256:
            pass
        y = 1
        if not (z + a) % 256:
            pass
        z = 1
        self._Random__whseed(x, y, z)

    
    def __getstate__(self):
        return self.getstate()

    
    def __setstate__(self, state):
        self.setstate(state)

    
    def randrange(self, start, stop = None, step = 1, int = int, default = None):
        istart = int(start)
        if istart != start:
            raise ValueError, 'non-integer arg 1 for randrange()'
        
        if stop is default:
            if istart > 0:
                return int(self.random() * istart)
            
            raise ValueError, 'empty range for randrange()'
        
        istop = int(stop)
        if istop != stop:
            raise ValueError, 'non-integer stop for randrange()'
        
        if step == 1 and istart < istop:
            
            try:
                return istart + int(self.random() * (istop - istart))
            except OverflowError:
                return int(istart + _floor(self.random() * (istop - istart)))

        
        if step == 1:
            raise ValueError, 'empty range for randrange()'
        
        istep = int(step)
        if istep != step:
            raise ValueError, 'non-integer step for randrange()'
        
        if istep > 0:
            n = ((istop - istart) + istep - 1) / istep
        elif istep < 0:
            n = ((istop - istart) + istep + 1) / istep
        else:
            raise ValueError, 'zero step for randrange()'
        if n <= 0:
            raise ValueError, 'empty range for randrange()'
        
        return istart + istep * int(self.random() * n)

    
    def randint(self, a, b):
        return self.randrange(a, b + 1)

    
    def choice(self, seq):
        return seq[int(self.random() * len(seq))]

    
    def shuffle(self, x, random = None, int = int):
        if random is None:
            random = self.random
        
        for i in xrange(len(x) - 1, 0, -1):
            j = int(random() * (i + 1))
            (x[i], x[j]) = (x[j], x[i])
        

    
    def uniform(self, a, b):
        return a + (b - a) * self.random()

    
    def normalvariate(self, mu, sigma):
        random = self.random
        while 1:
            u1 = random()
            u2 = random()
            z = NV_MAGICCONST * (u1 - 0.5) / u2
            zz = z * z / 4.0
            if zz <= -_log(u2):
                break
            
        return mu + z * sigma

    
    def lognormvariate(self, mu, sigma):
        return _exp(self.normalvariate(mu, sigma))

    
    def cunifvariate(self, mean, arc):
        return (mean + arc * (self.random() - 0.5)) % _pi

    
    def expovariate(self, lambd):
        random = self.random
        u = random()
        while u <= 9.9999999999999995e-008:
            u = random()
        return -_log(u) / lambd

    
    def vonmisesvariate(self, mu, kappa):
        random = self.random
        if kappa <= 9.9999999999999995e-007:
            return TWOPI * random()
        
        a = 1.0 + _sqrt(1.0 + 4.0 * kappa * kappa)
        b = (a - _sqrt(2.0 * a)) / 2.0 * kappa
        r = (1.0 + b * b) / 2.0 * b
        while 1:
            u1 = random()
            z = _cos(_pi * u1)
            f = (1.0 + r * z) / (r + z)
            c = kappa * (r - f)
            u2 = random()
            if u2 >= c * (2.0 - c):
                pass
            if not (u2 > c * _exp(1.0 - c)):
                break
            
        u3 = random()
        if u3 > 0.5:
            theta = mu % TWOPI + _acos(f)
        else:
            theta = mu % TWOPI - _acos(f)
        return theta

    
    def gammavariate(self, alpha, beta):
        if alpha <= 0.0 or beta <= 0.0:
            raise ValueError, 'gammavariate: alpha and beta must be > 0.0'
        
        random = self.random
        if alpha > 1.0:
            ainv = _sqrt(2.0 * alpha - 1.0)
            bbb = alpha - LOG4
            ccc = alpha + ainv
            while 1:
                u1 = random()
                u2 = random()
                v = _log(u1 / (1.0 - u1)) / ainv
                x = alpha * _exp(v)
                z = u1 * u1 * u2
                r = bbb + ccc * v - x
                if r + SG_MAGICCONST - 4.5 * z >= 0.0 or r >= _log(z):
                    return x * beta
                
        elif alpha == 1.0:
            u = random()
            while u <= 9.9999999999999995e-008:
                u = random()
            return -_log(u) * beta
        else:
            while 1:
                u = random()
                b = (_e + alpha) / _e
                p = b * u
                if p <= 1.0:
                    x = pow(p, 1.0 / alpha)
                else:
                    x = -_log((b - p) / alpha)
                u1 = random()
                if p <= 1.0 and u1 > _exp(-x) and p > 1:
                    pass
                if not (u1 > pow(x, alpha - 1.0)):
                    break
                
            return x * beta

    
    def stdgamma(self, alpha, ainv, bbb, ccc):
        import warnings
        warnings.warn('The stdgamma function is deprecated; use gammavariate() instead', DeprecationWarning)
        return self.gammavariate(alpha, 1.0)

    
    def gauss(self, mu, sigma):
        random = self.random
        z = self.gauss_next
        self.gauss_next = None
        if z is None:
            x2pi = random() * TWOPI
            g2rad = _sqrt(-2.0 * _log(1.0 - random()))
            z = _cos(x2pi) * g2rad
            self.gauss_next = _sin(x2pi) * g2rad
        
        return mu + z * sigma

    
    def betavariate(self, alpha, beta):
        y = self.gammavariate(alpha, 1.0)
        if y == 0:
            return 0.0
        else:
            return y / (y + self.gammavariate(beta, 1.0))

    
    def paretovariate(self, alpha):
        u = self.random()
        return 1.0 / pow(u, 1.0 / alpha)

    
    def weibullvariate(self, alpha, beta):
        u = self.random()
        return alpha * pow(-_log(u), 1.0 / beta)



def _test_generator(n, funccall):
    import time
    print n, 'times', funccall
    code = compile(funccall, funccall, 'eval')
    sum = 0.0
    sqsum = 0.0
    smallest = 10000000000.0
    largest = -10000000000.0
    t0 = time.time()
    for i in range(n):
        x = eval(code)
        sum = sum + x
        sqsum = sqsum + x * x
        smallest = min(x, smallest)
        largest = max(x, largest)
    
    t1 = time.time()
    print round(t1 - t0, 3), 'sec,'avg = sum / nstddev = _sqrt(sqsum / n - avg * avg), 'avg %g, stddev %g, min %g, max %g' % (avg, stddev, smallest, largest)


def _test(N = 20000):
    print 'TWOPI         =', TWOPI
    print 'LOG4          =', LOG4
    print 'NV_MAGICCONST =', NV_MAGICCONST
    print 'SG_MAGICCONST =', SG_MAGICCONST
    _test_generator(N, 'random()')
    _test_generator(N, 'normalvariate(0.0, 1.0)')
    _test_generator(N, 'lognormvariate(0.0, 1.0)')
    _test_generator(N, 'cunifvariate(0.0, 1.0)')
    _test_generator(N, 'expovariate(1.0)')
    _test_generator(N, 'vonmisesvariate(0.0, 1.0)')
    _test_generator(N, 'gammavariate(0.01, 1.0)')
    _test_generator(N, 'gammavariate(0.1, 1.0)')
    _test_generator(N, 'gammavariate(0.1, 2.0)')
    _test_generator(N, 'gammavariate(0.5, 1.0)')
    _test_generator(N, 'gammavariate(0.9, 1.0)')
    _test_generator(N, 'gammavariate(1.0, 1.0)')
    _test_generator(N, 'gammavariate(2.0, 1.0)')
    _test_generator(N, 'gammavariate(20.0, 1.0)')
    _test_generator(N, 'gammavariate(200.0, 1.0)')
    _test_generator(N, 'gauss(0.0, 1.0)')
    _test_generator(N, 'betavariate(3.0, 3.0)')
    _test_generator(N, 'paretovariate(1.0)')
    _test_generator(N, 'weibullvariate(1.0, 1.0)')
    s = getstate()
    jumpahead(N)
    r1 = random()
    setstate(s)
    for i in range(N):
        random()
    
    r2 = random()
    if r1 != r2:
        raise ValueError('jumpahead test failed ' + `(N, r1, r2)`)
    

_inst = Random()
seed = _inst.seed
random = _inst.random
uniform = _inst.uniform
randint = _inst.randint
choice = _inst.choice
randrange = _inst.randrange
shuffle = _inst.shuffle
normalvariate = _inst.normalvariate
lognormvariate = _inst.lognormvariate
cunifvariate = _inst.cunifvariate
expovariate = _inst.expovariate
vonmisesvariate = _inst.vonmisesvariate
gammavariate = _inst.gammavariate
stdgamma = _inst.stdgamma
gauss = _inst.gauss
betavariate = _inst.betavariate
paretovariate = _inst.paretovariate
weibullvariate = _inst.weibullvariate
getstate = _inst.getstate
setstate = _inst.setstate
jumpahead = _inst.jumpahead
whseed = _inst.whseed
if __name__ == '__main__':
    _test()

