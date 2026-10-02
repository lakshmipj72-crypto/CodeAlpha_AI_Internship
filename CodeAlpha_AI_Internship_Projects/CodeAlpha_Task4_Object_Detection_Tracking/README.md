# CodeAlpha Task 4 — Object Detection and Tracking

## Features
- Webcam or video-file input using OpenCV
- YOLO pre-trained object detection
- Bounding boxes and class labels
- Object tracking IDs using YOLO tracking
- Saves annotated output video

## Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python object_detection_tracking.py
```

The first run downloads the YOLO model automatically. Press **Q** to stop.

For a video file:
```bash
python object_detection_tracking.py --source input/video.mp4 --output output/tracked_output.mp4
```
