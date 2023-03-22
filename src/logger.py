import logging
import os
from datetime import datetime

LOG_DIRECTORY = "logs"
LOG_FILENAME_FORMAT = "{:%m_%d_%Y_%H_%M_%S}.log"
LOG_FILE_PATH = os.path.join(os.getcwd(), LOG_DIRECTORY, LOG_FILENAME_FORMAT.format(datetime.now()))

# Create the log directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

# Configure the logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Get the logger
logger = logging.getLogger(__name__)
