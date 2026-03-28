# JKCOM

**AI-Powered GPS Mapping and Perception Stack for Autonomous Electric Vehicles**

JKCOM is an open-source framework that combines **computer vision**, **radar sensing**, and **GPS** to create accurate, real-time HD maps and robust localization for self-driving electric vehicles - with a focus on safety, efficiency, and real-world deployment.

### Core Capabilities
- **Multi-Sensor Fusion**: Camera (semantic segmentation, object detection) + Radar (velocity & range in all weather) + GPS/IMU
- **HD Map Generation**: Automatic creation and updating of high-definition maps (lanes, signs, obstacles)
- **Real-time Localization**: Visual + radar-enhanced positioning, even in GPS-denied environments (urban canyons, tunnels)
- **Perception Pipeline**: Object detection, tracking, free-space segmentation, and dynamic obstacle prediction
- **Electric Vehicle Optimized**: Energy-efficient routing, battery-aware path planning, and regenerative braking integration
- **Simulation Ready**: Compatible with CARLA, NVIDIA Isaac Sim, and ROS 2

### Key Features
- End-to-end perception → mapping → localization pipeline
- Radar-camera fusion models for adverse weather (rain, fog, night)
- AI-driven map feature extraction (lanes, traffic signs, road boundaries)
- GNSS-free fallback using visual localization
- Lightweight models suitable for edge deployment on vehicle compute units
- Modular design - easily swap sensors or add new modalities (LiDAR support planned)

### Tech Stack
- **Computer Vision**: OpenCV, YOLO, Segment Anything, Detectron2 / custom transformers
- **Radar Processing**: Radar point cloud processing + Doppler velocity
- **Sensor Fusion**: Kalman filters, Deep fusion networks, ROS 2
- **Mapping & Localization**: ORB-SLAM / Visual SLAM + HD map formats (OpenDrive, Lanelet2)
- **AI Framework**: PyTorch / TensorFlow with ONNX export
- **Simulation**: CARLA + ROS 2
- **Deployment**: Docker, NVIDIA Jetson / edge hardware support

### Why JKCOM?
While projects like Autoware provide full autonomous stacks, JKCOM focuses specifically on **mapping + localization** with a strong emphasis on **camera + radar fusion** for cost-effective autonomous electric vehicles. It's designed to be lightweight, open, and extensible for researchers, startups, and EV manufacturers in emerging markets (e.g., enabling autonomous buses in Enugu, Nigeria).

---

**Open Source • Self-hosted • Real-time • EV-focused**

Built for the future of sustainable autonomous mobility.

**License**: Apache 2.0
