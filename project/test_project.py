# FILE: test_camera.py
import unittest
import numpy as np
from camera import convert

class TestCamera(unittest.TestCase):

    def test_convert_basic(self):
        # Create a simple 2x2 image with distinct colors
        source_img = np.array([[[255, 0, 0], [0, 255, 0]],
                               [[0, 0, 255], [255, 255, 0]]], dtype=np.uint8)

        # Convert the image
        result_img = convert(source_img)

        # Check the shape of the result image
        self.assertEqual(result_img.shape, (2, 2, 3))

        # Check the colors in the result image
        expected_colors = [
            [result_img[0, 0], [0, 0, 255]],  # Red in BGR
            [result_img[0, 1], [0, 255, 0]],  # Green in BGR
            [result_img[1, 0], [255, 0, 0]],  # Blue in BGR
            [result_img[1, 1], [0, 255, 255]] # Yellow in BGR
        ]

        for actual, expected in expected_colors:
            self.assertTrue(np.array_equal(actual, expected))

    def test_convert_empty_image(self):
        # Create an empty image
        source_img = np.array([[]], dtype=np.uint8)

        # Convert the image
        result_img = convert(source_img)

        # Check the shape of the result image
        self.assertEqual(result_img.shape, (1, 0, 3))

    def test_convert_single_pixel(self):
        # Create a single pixel image
        source_img = np.array([[[123, 234, 45]]], dtype=np.uint8)

        # Convert the image
        result_img = convert(source_img)

        # Check the shape of the result image
        self.assertEqual(result_img.shape, (1, 1, 3))

        # Check the color in the result image
        self.assertTrue(np.array_equal(result_img[0, 0], [45, 234, 123]))  # BGR

if __name__ == '__main__':
    unittest.main()
