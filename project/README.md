Pixated Camera Demo
Overview
The Pixated Camera Demo is a Python project that captures video from a webcam and applies a pixelation effect to the video feed in real-time. The pixelation effect is achieved by converting the video frames into a dotted image format, where each dot represents a pixel block of the original frame. This project demonstrates the use of OpenCV for video capture and manipulation, as well as the Python Imaging Library (PIL) for image processing.

Files
camera.py
This is the main script of the project. It contains the following key components:

Imports: The script imports necessary libraries including OpenCV (cv2), NumPy (np), and PIL (Image, ImageDraw).

Constants:

DOT_SIZE: Defines the size of each dot in the pixelated image.
RADIUS: Defines the radius of each dot, calculated as half of DOT_SIZE.
Window Setup:

cv2.namedWindow("Pixated Camera"): Creates a window named "Pixated Camera" to display the video feed.
vc = cv2.VideoCapture(0): Initializes video capture from the default webcam (usually indexed as 0).
Frame Capture:

The script attempts to capture the first frame from the webcam to ensure it is working correctly.
convert Function:

This function takes a source image (source_img) and converts it into a pixelated image.
It creates a new image (dotted_img) with the same dimensions as the source image.
It iterates over the source image in blocks of size DOT_SIZE and draws a dot for each block using the average color of the block.
The color space is converted from BGR (used by OpenCV) to RGB (used by PIL) and back to BGR after processing.
Main Loop:

The script enters a loop where it continuously captures frames from the webcam.
Each frame is processed using the convert function to apply the pixelation effect.
The processed frame is displayed in the "Pixated Camera" window.
The loop exits when the ESC key (key code 27) is pressed.
Cleanup:

The script destroys the window created for displaying the video feed when the loop exits.
Design Choices
Pixelation Effect
The pixelation effect was chosen to demonstrate basic image processing techniques using Python. The effect is achieved by dividing the image into blocks and representing each block with a single dot of the average color. This approach simplifies the image while retaining the overall structure and colors.

Libraries
OpenCV: Used for video capture and display. OpenCV is a powerful library for computer vision tasks and provides efficient methods for handling video streams.
PIL (Pillow): Used for image processing. PIL provides a simple and intuitive interface for manipulating images, making it suitable for tasks like drawing shapes and converting color spaces.

Performance Considerations
The script processes each frame in real-time, which can be computationally intensive. The choice of DOT_SIZE affects the performance and visual quality of the pixelation effect. A larger DOT_SIZE reduces the number of dots to be drawn, improving performance but reducing detail. Conversely, a smaller DOT_SIZE increases detail but may impact performance.

