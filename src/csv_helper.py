import csv
from typing import List, Dict

class CSVHelper:
    @staticmethod
    def read_urls_from_csv(file_path: str) -> List[str]:
        url_list = []
        try:
            with open(file_path, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip header
                for row in csv_reader:
                    url_list.append(row[0])
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"An error occurred while reading {file_path}: {e}")
        return url_list

    @staticmethod
    def read_scores_from_csv(file_path: str) -> Dict[str, float]:
        scores_dict = {}
        try:
            with open(file_path, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip header
                for row in csv_reader:
                    print(row)
                    if len(row) < 2:
                        print(f"Warning: Row in {file_path} is missing data: {row}")
                        continue
                    try:
                        scores_dict[row[0]] = float(row[1])
                    except ValueError:
                        print(f"Warning: Invalid score format in row: {row}")
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"An error occurred while reading {file_path}: {e}")
        return scores_dict