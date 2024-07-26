import argparse
import os
from pathlib import Path
from src.downloader import ImageDownloader
from src.quality_assessor import QualityAssessor
from src.comparator import ScoreComparator
from src.logger import Logger
from src.csv_helper import CSVHelper

def main(dry_run):
    # Define paths
    urls_csv = 'data/input/urls.csv'
    old_scores_csv = 'data/input/old_scores.csv'
    new_scores_csv = 'data/output/new_scores.csv'
    differences_csv = 'data/output/differences.csv'

    # Set up logging
    Logger.setup_logging()

    # Read the list of URLs from CSV
    url_list = CSVHelper.read_urls_from_csv(urls_csv)

    # Ensure the download path exists
    download_path = 'data/input/'
    Path(download_path).mkdir(parents=True, exist_ok=True)

    # Download images
    downloader = ImageDownloader(download_path)
    downloader.download_images(url_list)

    # Assess image quality
    assessor = QualityAssessor(download_path, new_scores_csv)
    assessor.assess_images()

    if dry_run:
        # Dry run: Skip comparison
        print("Dry run mode activated. New scores generated but not compared.")
    else:
        # Check if old scores file exists and compare scores
        if os.path.exists(old_scores_csv):
            comparator = ScoreComparator(old_scores_csv, new_scores_csv, differences_csv)
            comparator.compare_scores()
            print(f"Score comparison complete. Check the differences file: {differences_csv}")
        else:
            # Log that there are no old scores
            print("No old scores found. Skipping score comparison.")

    print("Processing complete. Check the output files for results.")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run image quality assessment.")
    parser.add_argument('--dry_run', action='store_true', help="Run in dry run mode (generate new scores only, skip comparison)")

    # Parse arguments
    args = parser.parse_args()

    # Call main function with dry_run flag
    main(dry_run=args.dry_run)
