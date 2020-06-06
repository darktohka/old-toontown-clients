# File: S (Python 2.2)

from ShowBase import *
CollisionHandlerRayStart = 4000.0
directNotify.setDconfigLevels()

def inspect(anObject):
    Inspector = Inspector
    import direct.tkpanels
    return Inspector.inspect(anObject)

__builtins__['inspect'] = inspect
if not __debug__ and __dev__:
    notify = directNotify.newCategory('ShowBaseGlobal')
    notify.error("You must set 'want-dev' to false in non-debug mode.")

