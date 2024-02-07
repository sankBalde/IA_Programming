# Apple VISION Touch

This Python script uses MediaPipe to track the hand in real-time from a webcam feed and replaces the background with a random color. The script utilizes the OpenCV library for webcam access and image manipulation, as well as the MediaPipe library for hand tracking.

## Requirements

- Python 3.x
- OpenCV (cv2)
- MediaPipe
- NumPy

You can install the required libraries using pip:

```bash
pip install opencv-python mediapipe numpy
```

## Usage

1. Run the script `vision_touch.py`.
2. Place your hand in front of the webcam.
3. The script will track your hand and replace the background with a random color.
4. Press 'q' or 'ctrl + c' to exit the script.

## Code Explanation

- The script captures video from the webcam using OpenCV (`cv2.VideoCapture`).
- It processes the video frames using MediaPipe to detect and track the hand landmarks.
- For each detected hand, it calculates the bounding box and extracts the region of interest (hand).
- The background is replaced with a random color, and the hand region is superimposed on the new background.
- Finally, the script displays the modified video feed with the hand and the new background.

## Acknowledgments

This script is inspired by the MediaPipe hands example and incorporates OpenCV for image processing and manipulation.

