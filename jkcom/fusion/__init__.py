class FusionEngine:
    def __init__(self, vision_engine, localizer):
        self.vision = vision_engine
        self.localizer = localizer
    
    def fuse(self, radar_data=None):
        """Fuse objects and localization."""
        vision_objects = self.vision.detect_objects()
        location = self.localizer.update()
        
        # Simple fusion logic: just bundle them for now
        return {
            "location": location,
            "perception": vision_objects,
            "fusion_status": "synced"
        }

def get_engine(vision, localizer):
    return FusionEngine(vision, localizer)
