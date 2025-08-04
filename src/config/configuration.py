from src.utils import read_yaml, create_dir
from src.constants import *
from src.entity.config_entity import IngestionConfig



class ConfigurationManager:
    def __init__(self,
                 config_filepath=Config_file_path,
                 params_filepath=Params_file_path,
                 schema_filepath=Schema_file_path):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_dir([self.config.artifact_root])


    def get_ingestion_config(self) -> IngestionConfig:
        config = self.config.Ingestion

        create_dir([config.root_directory])

        Ingestion_config = IngestionConfig(
            root_dir = config.root_directory,
            source_URL = config.src_url,
            local_data = config.local_data
        )

        return Ingestion_config
