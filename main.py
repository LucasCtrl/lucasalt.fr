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
  posts = get_content("src/posts")
  site_content = {"navbar_content": [], "posts": []}

  for page in pages:
    if page["metadata"]["navbar"]:
      site_content["navbar_content"].append(page["metadata"])

  for post in posts:
    site_content["posts"].append(post["metadata"])

  for page in pages:
    render_page(page, site_content, "dist")

  for post in posts:
    render_page(post, site_content, "dist/posts")

  logger.log.success("Generation completed!")


if __name__ == "__main__":
  generate_static_site()
