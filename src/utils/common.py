import os
import yaml 
import json
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from src.logger import logging
from src.exception import MyException

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    "reads yaml file and returns"

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            logging.info(f"yaml file: {yaml_file} loaded successfully")
            return ConfigBox(content)
        
    except Exception as e:
        raise MyException(e,sys)
    


@ensure_annotations
def create_dir(path_to_dir:list, verbose=True):
    "creates directories"

    for path in path_to_dir:
        os.makedirs(path, exist_ok=true)

        if verbose:
            logging.info(f"created directory at: {path}")



@ensure_annotations
def save_json(path: Path, data: dict):
    "saves json data"

    with open(path, "w") as file:
        json.dump(data, file, indent=4)

    logging.info(f"json file saved at: {path}")



@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    "loads json file data"

    with open(path) as file:
        content = json.load(file)

    logging.info(f"json file loaded from: {path}")
    return ConfigBox(content)



@ensure_annotations
def save_binary(data: Any, path: Path):
    "saves binary file"

    joblib.dump(value = data, filename = path)
    logging.info(f"binary file saved at: {path}")



@ensure_annotations
def load_binary(path:Path) -> Any:
    "loads binary data"

    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")

    return data