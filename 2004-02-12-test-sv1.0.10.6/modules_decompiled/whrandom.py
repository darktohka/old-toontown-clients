# File: w (Python 2.2)


class whrandom:
    
    def __init__(self, x = 0, y = 0, z = 0):
        self.seed(x, y, z)

    
    def seed(self, x = 0, y = 0, z = 0):
        if type(x) == type(y) and type(y) == type(z):
            pass
        type(z) == type(0)
        if not 1:
            raise TypeError, 'seeds must be integers'
        
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
            raise ValueError, 'seeds must be in range(0, 256)'
        
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

    
    def random(self):
        (x, y, z) = self._seed
        x = 171 * x % 30269
        y = 172 * y % 30307
        z = 170 * z % 30323
        self._seed = (x, y, z)
        return (x / 30269.0 + y / 30307.0 + z / 30323.0) % 1.0

    
    def uniform(self, a, b):
        return a + (b - a) * self.random()

    
    def randint(self, a, b):
        return self.randrange(a, b + 1)

    
    def choice(self, seq):
        return seq[int(self.random() * len(seq))]

    
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
        
        if step == 1:
            if istart < istop:
                return istart + int(self.random() * (istop - istart))
            
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


_inst = whrandom()
seed = _inst.seed
random = _inst.random
uniform = _inst.uniform
randint = _inst.randint
choice = _inst.choice
randrange = _inst.randrange
