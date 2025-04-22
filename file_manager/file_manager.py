# Libraries
import json

# Internal modules
from recruitment_tracker.config import Config

class FileManager:

    def __init__(self, file_path):
        self.file_path = file_path
    

    def load_offers(self):
        try:
            with open(self.file_path, Config.FILE_READ_MODE, encoding=Config.DEFAULT_ENCODING) as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        

    def save_offers(self, offers):
        with open(self.file_path, Config.FILE_WRITE_MODE, encoding=Config.DEFAULT_ENCODING) as file:
            json.dump(offers, file, indent=Config.FILE_INDENT)
