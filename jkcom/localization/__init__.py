import random

class LocalizationEngine:
    def __init__(self):
        self.state = {"lat": 6.4542, "lng": 3.3887, "heading": 0.0}
    
    def update(self, dt=0.1):
        """Simulate motion update."""
        self.state["lat"] += random.uniform(-0.0001, 0.0001)
        self.state["lng"] += random.uniform(-0.0001, 0.0001)
        self.state["heading"] = (self.state["heading"] + random.uniform(-1, 1)) % 360
        return self.state

def get_engine():
    return LocalizationEngine()
