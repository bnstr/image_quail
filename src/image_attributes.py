# image_attributes.py
from skimage import io, color, exposure

class ImageAttributes:
    def __init__(self):
        pass

    def check_brightness(self, img_path):
        img = io.imread(img_path)
        gray_img = color.rgb2gray(img)
        hist, _ = exposure.histogram(gray_img)
        return hist.mean() > 0.5

    def check_contrast(self, img_path):
        img = io.imread(img_path)
        gray_img = color.rgb2gray(img)
        hist, _ = exposure.histogram(gray_img)
        return hist.max() - hist.min() > 0.5
