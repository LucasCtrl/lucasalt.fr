import os
from module import logger
from module.get_content import get_content
from module.html_renderer import render_page
from module.utils import delete_folder, create_folder

logger.init_logger(mode="DEBUG")


def create_dist_folder(dst_folder):
  logger.log.set(f"Cleaning output folder: {dst_folder}")
  delete_folder(dst_folder)
  create_folder(dst_folder)


def generate_static_site():
  logger.log.set("Starting the generator")

  create_dist_folder(f"{os.getcwd()}/dist")

  pages = get_content("src/pages")
  navbar_content = []

  for page in pages:
    if page["metadata"]["navbar"]:
      navbar_content.append(page["metadata"])

  for page in pages:
    render_page(page, navbar_content, "dist")

  logger.log.success("Generation completed!")


if __name__ == "__main__":
  generate_static_site()
