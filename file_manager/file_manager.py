# Libraries
import json

# Internal modules
from config import Config


class FileManager:
    """
    The FileManager class is responsible for managing the reading and writing of offers data to and from a specified file.

    It provides methods for loading offers from a file and saving offers to a file in JSON format. The file path, read mode, write mode, 
    and encoding settings are configurable through the `Config` module.

    Attributes:
        file_path (str): The path to the file where offers are stored.

    Methods:
        load_offers(): Loads offers from the file specified by `file_path`. Returns a list of offers, or an empty list if the file is not found.
        save_offers(offers): Saves the provided list of offers to the file specified by `file_path`, using the configurations for file write mode and encoding.

    Constants:
        None

    Args:
        file_path (str): The file path to load from or save to. This path should point to a valid file location on the system.
    """

    def __init__(self, file_path):
        """
        Initializes the FileManager object with the specified file path.
        
        Args:
            file_path (str): The file path where the offers will be saved or loaded from.
        """
        self.file_path = file_path
    

    def load_offers(self):
        """
        Loads the offers from the file specified by `file_path`.

        Tries to open and read the file in the specified read mode and encoding from the `Config` module. 
        If the file does not exist, it returns an empty list.

        Returns:
            list: A list of offers loaded from the file. If the file is not found, an empty list is returned.
        """
        try:
            with open(self.file_path, Config.FILE_READ_MODE, encoding=Config.DEFAULT_ENCODING) as file:
                return json.load(file)
        
        except FileNotFoundError:
            return []
        

    def save_offers(self, offers):
        """
        Saves the provided list of offers to the file specified by `file_path`.

        Serializes the offers list to JSON format and writes it to the file using the specified write mode and encoding from the `Config` module.

        Args:
            offers (list): A list of offers to be saved to the file. Each offer should be a dictionary containing relevant offer information.

        Returns:
            None
        """
        with open(self.file_path, Config.FILE_WRITE_MODE, encoding=Config.DEFAULT_ENCODING) as file:
            json.dump(offers, file, indent=Config.FILE_INDENT)
