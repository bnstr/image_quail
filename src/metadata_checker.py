from PIL import Image

class MetadataChecker:
    def get_exif_data(self, img_path):
        img = Image.open(img_path)
        return img._getexif()
