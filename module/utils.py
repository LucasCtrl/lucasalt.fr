import os
import shutil
from . import logger


def create_folder(folder_location):
  if not os.path.exists(folder_location):
    try:
      os.makedirs(folder_location)
      logger.log.debug(f"Creating output folder: {folder_location}")
    except Exception as e:
      logger.log.error(f"Error while creating output folder: {e}")


def delete_folder(folder_location):
  if os.path.exists(folder_location):
    try:
      shutil.rmtree(folder_location)
      logger.log.debug(f"Deleting output folder: {folder_location}")
    except Exception as e:
      logger.log.error(f"Error while deleting output folder: {e}")
