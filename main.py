from module import logger
from module.md_content import get_md_content

logger.init_logger(mode="DEBUG")

def generate_static_site():
  logger.log.set("Starting the generator")
  pages = get_md_content('src/pages')
  posts = get_md_content('src/posts')
  print(pages)
  print(posts)

if __name__ == "__main__":
  generate_static_site()
