import csv
import logging

class Logger:
    def __init__(self, output_file):
        self.output_file = output_file

    @staticmethod
    def setup_logging(log_level=logging.INFO):
        # Create a custom logger
        logger = logging.getLogger()
        logger.setLevel(log_level)

        # Create handlers
        file_handler = logging.FileHandler('app.log')
        console_handler = logging.StreamHandler()

        # Set levels for handlers
        file_handler.setLevel(logging.DEBUG)
        console_handler.setLevel(log_level)

        # Create formatters and add them to handlers
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')

        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        print("Logging setup complete. Logs will be saved to 'app.log' and output to console.")

    def log_differences(self, differences):
        with open(self.output_file, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['URL', 'Old Score', 'New Score'])
            for url, (old_score, new_score) in differences.items():
                writer.writerow([url, old_score, new_score])
