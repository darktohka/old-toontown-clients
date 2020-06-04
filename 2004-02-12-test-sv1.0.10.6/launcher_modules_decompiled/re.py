# File: r (Python 2.2)

engine = 'sre'
if engine == 'sre':
    from sre import *
    from sre import __all__
else:
    from pre import *
    from pre import __all__
