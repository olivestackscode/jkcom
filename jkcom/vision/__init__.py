import random

class VisionEngine:
    def __init__(self):
        self.model_name = "YOLOv11-JKCOM-Custom"
    
    def detect_objects(self, frame=None):
        """Simulate object detection results."""
        classes = ["car", "truck", "pedestrian", "cyclist", "traffic_light"]
        detections = []
        for i in range(random.randint(1, 5)):
            detections.append({
                "id": i,
                "label": random.choice(classes),
                "confidence": random.uniform(0.7, 0.99),
                "bbox": [random.randint(0, 640), random.randint(0, 480), random.randint(50, 100), random.randint(50, 100)]
            })
        return detections

def get_engine():
    return VisionEngine()
