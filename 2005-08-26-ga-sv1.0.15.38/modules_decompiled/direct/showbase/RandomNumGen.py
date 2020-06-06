# File: R (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from pandac import Mersenne

def randHash(num):
    rng = RandomNumGen(num)
    return rng.randint(0, (1 << 16) - 1)


class RandomNumGen:
    notify = DirectNotifyGlobal.directNotify.newCategory('RandomNumGen')
    
    def __init__(self, seed):
        if isinstance(seed, RandomNumGen):
            rng = seed
            seed = rng.randint(0, 0x1L << 16)
        
        self.notify.debug('seed: ' + str(seed))
        seed = int(seed)
        rng = Mersenne.Mersenne(seed)
        self._RandomNumGen__rng = rng

    
    def _RandomNumGen__rand(self, N):
        return int(self._RandomNumGen__rng.getUint31() * long(N) >> 31)

    
    def choice(self, seq):
        return seq[self._RandomNumGen__rand(len(seq))]

    
    def shuffle(self, x):
        for i in xrange(len(x) - 1, 0, -1):
            j = int(self._RandomNumGen__rand(i + 1))
            (x[i], x[j]) = (x[j], x[i])
        

    
    def randrange(self, start, stop = None, step = 1):
        istart = int(start)
        if istart != start:
            raise ValueError, 'non-integer arg 1 for randrange()'
        
        if stop is None:
            if istart > 0:
                return self._RandomNumGen__rand(istart)
            
            raise ValueError, 'empty range for randrange()'
        
        istop = int(stop)
        if istop != stop:
            raise ValueError, 'non-integer stop for randrange()'
        
        if step == 1:
            if istart < istop:
                return istart + self._RandomNumGen__rand(istop - istart)
            
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
        
        return istart + istep * int(self._RandomNumGen__rand(n))

    
    def randint(self, a, b):
        range = (b - a) + 1
        r = self._RandomNumGen__rand(range)
        return a + r

    
    def random(self):
        return float(self._RandomNumGen__rng.getUint31()) / float(0x1L << 31)


