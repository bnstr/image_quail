import cv2
import numpy as np
from skimage import exposure

class QualityChecker:
    def check_resolution(self, img_path):
        img = cv2.imread(img_path)
        height, width = img.shape[:2]
        # Example resolution check: prefer larger resolutions
        return min(height, width) / 1000  # Adjust as necessary

    def check_blurriness(self, img_path):
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        variance = cv2.Laplacian(img, cv2.CV_64F).var()
        # Example: Higher variance indicates less blurriness
        return min(variance / 100, 10)  # Normalize and cap the value

    def check_brightness(self, img_path):
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mean_brightness = np.mean(gray)
        # Example: Normalize brightness
        return min(mean_brightness / 255, 10)

    def check_contrast(self, img_path):
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        p2, p98 = np.percentile(gray, (2, 98))
        contrast = p98 - p2
        # Example: Normalize contrast
        return min(contrast / 100, 10)
