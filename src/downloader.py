import requests
from pathlib import Path

class ImageDownloader:
    def __init__(self, download_path):
        self.download_path = Path(download_path)
        self.download_path.mkdir(parents=True, exist_ok=True)

    def download_image(self, url, filename):
        response = requests.get(url)
        response.raise_for_status()
        file_path = self.download_path / filename
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_path

    def download_images(self, url_list):
        for index, url in enumerate(url_list):
            filename = f"POI_{index}_{url.split('/')[-1]}"
            self.download_image(url, filename)
