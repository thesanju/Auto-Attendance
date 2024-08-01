import cv2
import os

# Initialize the video capture
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Could not open video device")
    exit()

# Set video frame width and height
video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Ensure the directory to save frames exists
os.makedirs('camera_test_frames', exist_ok=True)

frame_count = 0
while frame_count < 5:  # Capture 5 frames
    ret, frame = video.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Save the frame to disk
    frame_path = f"camera_test_frames/frame_{frame_count}.jpg"
    cv2.imwrite(frame_path, frame)
    print(f"Saved {frame_path}")
    frame_count += 1

    # Introduce a small delay to avoid high CPU usage
    time.sleep(1)

# Release the video capture
video.release()
