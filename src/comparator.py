import csv
from src.csv_helper import CSVHelper

class ScoreComparator:
    def __init__(self, old_scores_csv, new_scores_csv, differences_csv):
        self.old_scores_csv = old_scores_csv
        self.new_scores_csv = new_scores_csv
        self.differences_csv = differences_csv

    def compare_scores(self):
        try:
            # Load the scores from CSV files using CSVHelper
            old_scores = CSVHelper.read_scores_from_csv(self.old_scores_csv)
            new_scores = CSVHelper.read_scores_from_csv(self.new_scores_csv)

            # Ensure both score dictionaries are not empty
            if not old_scores or not new_scores:
                raise ValueError('One or both score dictionaries are empty.')

            # Create sets of URLs to compare
            old_urls = set(old_scores.keys())
            new_urls = set(new_scores.keys())

            # Find common URLs
            common_urls = old_urls.intersection(new_urls)

            # Prepare a list to hold differences
            differences = []

            for url in common_urls:
                old_score = old_scores[url]
                new_score = new_scores[url]
                difference = new_score - old_score
                differences.append({
                    'url': url,
                    'old': old_score,
                    'new': new_score,
                    'difference': difference
                })

            # Write differences to a CSV file
            with open(self.differences_csv, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['url', 'old', 'new', 'difference'])
                writer.writeheader()
                writer.writerows(differences)

            print(f"Score comparison complete. Differences saved to {self.differences_csv}")

        except Exception as e:
            print(f"An error occurred during score comparison: {e}")
