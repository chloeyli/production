import sys
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

sys.path.append("./05_src")  # Add your src folder to the path

from utils.logger import get_logger

_logs = get_logger(__name__)
_logs.info("Hello world!")

print("Script ran!")  # This line helps confirm the script is running
