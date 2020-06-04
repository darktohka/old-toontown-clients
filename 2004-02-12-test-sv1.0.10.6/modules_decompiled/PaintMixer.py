# File: P (Python 2.2)

import PlatformEntity

class PaintMixer(PlatformEntity.PlatformEntity):
    
    def start(self):
        PlatformEntity.PlatformEntity.start(self)
        model = self.platform.model
        shaft = model.find('**/PaintMixerBase1')
        shaft.setSz(self.shaftScale)


