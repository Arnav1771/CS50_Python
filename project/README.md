# Pixalated Camera Demo
#### Video Demo : https://youtu.be/sRM0-i8bbcA
#### Description

# Pixated Camera

## Overview

Pixated Camera is a Python project that captures video from a webcam and applies a pixelation effect to the video feed. The pixelation effect is achieved by converting the video frames into a dotted image format. This project uses the OpenCV library for video capture and the Pillow library for image processing.

## Files

### `project.py`

This is the main script of the project. It contains the following functions:

- `initialize_camera()`: Initializes the webcam and attempts to capture the first frame. It returns the video capture object, a boolean indicating if the capture was successful, and the first frame.
- `convert(source_img)`: Converts a source image into a dotted image. It creates a new image with dots of a specified size and color based on the source image.
- `display_frames(vc, rval, frame)`: Continuously captures frames from the webcam, applies the pixelation effect using the `convert` function, and displays the processed frames in a window. The loop exits when the ESC key is pressed.
- `main()`: The main function that initializes the camera and starts the frame display loop if the camera initialization is successful.

### Design Choices

1. **Function Decomposition**: The code is divided into multiple functions to enhance readability and maintainability. Each function has a single responsibility, making the code easier to understand and test.
2. **Use of Libraries**: OpenCV is used for video capture due to its efficiency and ease of use. Pillow is used for image processing because it provides a simple interface for drawing shapes and manipulating images.
3. **Pixelation Effect**: The pixelation effect is achieved by drawing ellipses on a blank image based on the colors of the source image. This approach was chosen for its simplicity and visual appeal.

## Unit Tests

Each function in the `camera.py` script is accompanied by unit tests to ensure correctness. The tests cover various scenarios, including successful and unsuccessful camera initialization, image conversion, and frame display.

## Running the Project

To run the project, execute the `camera.py` script. Ensure that you have a webcam connected and the required libraries installed.

```sh
python3 camera.py
