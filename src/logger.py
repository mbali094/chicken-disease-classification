import os
import logging
from datetime import datetime

file_name=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
filename_path = os.path.join(os.getcwd(), "logs", file_name)
os.makedirs(filename_path, exist_ok=True)

file_dir_path = os.path.join(filename_path, file_name)

logging.basicConfig(
    filename=file_dir_path,
    format ='[%(asctime)s] - %(lineno)s -%(name)s -%(message)s',
    level=logging.INFO
)
