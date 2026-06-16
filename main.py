import os
import shutil
from module import logger
from module.get_content import get_content
from module.html_renderer import render_page

logger.init_logger(mode="DEBUG")

def create_dist_folder(dst_folder):
  logger.log.set(f'Cleaning output folder: {dst_folder}')
  # Delete 'dist' folder if he exists
  if os.path.exists(dst_folder):
    try:
      shutil.rmtree(f'{os.getcwd()}/{dst_folder}')
      logger.log.debug(f'Deleting output folder: /{dst_folder}')
    except:
      logger.log.error(f'Error while deleting output folder: /{dst_folder}')

  # Create 'dist' folder
  if not os.path.exists(dst_folder):
    try:
      os.makedirs(f'{os.getcwd()}/{dst_folder}')
      logger.log.debug(f'Creating output folder: /{dst_folder}')
    except:
      logger.log.error(f'Error while creating output folder: /{dst_folder}')

def generate_static_site():
  logger.log.set("Starting the generator")

  create_dist_folder('dist')

  pages = get_content('src/pages')

  for page in pages:
    render_page(page, 'dist')
  
  logger.log.success("Generation completed!")

if __name__ == "__main__":
  generate_static_site()
