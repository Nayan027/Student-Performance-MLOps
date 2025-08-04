import os
import urllib.request as request
from pathlib import Path
from src.logger import logging
from src.entity.config_entity import IngestionConfig



class DataIngestion:
    def __init__(self,
                 config: IngestionConfig):
        
        self.config = config


    def download_csv_file(self):
        if not os.path.exists(self.config.local_data):
            filename, headers = request.urlretrieve(
                url= self.config.source_URL,
                filename=self.config.local_data)
            
            logging.info(f"{filename} downloaded!!")
        
        else:
            logging.info(f"file {filename} already exists")