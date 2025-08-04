import os
import sys
import logging

log_string = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_directory = "logs"

logfile_path = os.path.join(log_directory,"running_logs.log")
os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_string,
    handlers=[logging.FileHandler(logfile_path),
              logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("mlops_logger")