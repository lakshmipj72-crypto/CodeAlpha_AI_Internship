import argparse
import cv2
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description="YOLO object detection and tracking")
    parser.add_argument("--source", default="0", help="0 for webcam or path to a video file")
    parser.add_argument("--output", default="output/tracked_output.mp4")
    parser.add_argument("--model", default="yolo11n.pt")
    args = parser.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source
    model = YOLO(args.model)

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open source: {args.source}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)
    writer = cv2.VideoWriter(
        args.output,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps, (width, height)
    )

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        results = model.track(frame, persist=True, verbose=False)
        annotated = results[0].plot()
        writer.write(annotated)
        cv2.imshow("CodeAlpha - Object Detection & Tracking", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
