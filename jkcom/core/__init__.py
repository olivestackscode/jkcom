from . import vision, localization, fusion

class JKCOMStack:
    def __init__(self):
        self.vision = vision.get_engine()
        self.localization = localization.get_engine()
        self.fusion = fusion.get_engine(self.vision, self.localization)
    
    def step(self):
        """Execute one iteration of the autonomous stack."""
        return self.fusion.fuse()

def get_stack():
    return JKCOMStack()
