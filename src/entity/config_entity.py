from dataclasses import dataclass
from pathlib import Path


@dataclass
class IngestionConfig:
    root_dir: Path
    source_URL: str
    local_data: Path