# File: S (Python 2.2)

from ShowBase import *
ShowBase()
directNotify.setDconfigLevels()

def inspect(anObject):
    import Inspector
    return Inspector.inspect(anObject)

__builtins__['inspect'] = inspect
__builtins__['__dev__'] = base.config.GetBool('want-dev', 0)
if not __debug__ and __dev__:
    notify = directNotify.newCategory('ShowBaseGlobal')
    notify.error("You must set 'want-dev' to false in non-debug mode.")

