import os
import csv
from .quality_checker import QualityChecker

class QualityAssessor:
    def __init__(self, images_dir, new_scores_csv):
        self.images_dir = images_dir
        self.new_scores_csv = new_scores_csv
        self.quality_checker = QualityChecker()

        # Define the maximum possible values for each quality metric
        self.max_resolution = 10  # Example maximum value for resolution
        self.max_blurriness = 10  # Example maximum value for blurriness
        self.max_brightness = 10  # Example maximum value for brightness
        self.max_contrast = 10    # Example maximum value for contrast

        # Define the weights for each metric
        self.weight_resolution = 20
        self.weight_blurriness = 10
        self.weight_brightness = 10
        self.weight_contrast = 10

        # Calculate the maximum possible score
        self.max_possible_score = (self.max_resolution * self.weight_resolution +
                                   self.max_blurriness * self.weight_blurriness +
                                   self.max_brightness * self.weight_brightness +
                                   self.max_contrast * self.weight_contrast)

    def assess_images(self):
        with open(self.new_scores_csv, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['url', 'score'])

            for filename in os.listdir(self.images_dir):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    img_path = os.path.join(self.images_dir, filename)

                    # Calculate the score
                    raw_score = (self.quality_checker.check_resolution(img_path) * self.weight_resolution +
                                 self.quality_checker.check_blurriness(img_path) * self.weight_blurriness +
                                 self.quality_checker.check_brightness(img_path) * self.weight_brightness +
                                 self.quality_checker.check_contrast(img_path) * self.weight_contrast)

                    # Normalize the score to be within 0 to 100
                    normalized_score = (raw_score / self.max_possible_score) * 100

                    # Write the URL and normalized score to the CSV
                    csv_writer.writerow([filename, normalized_score])

        print(f"New image quality scores generated and saved to {self.new_scores_csv}.")
