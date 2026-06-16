from module.logger import Logger
from module.md_content import get_md_content

log = Logger(mode="DEBUG")

def generate_static_site():
  log.info("Starting the generator")
  pages = get_md_content('src/pages')
  posts = get_md_content('src/posts')
  print(pages)
  print(posts)

if __name__ == "__main__":
  generate_static_site()
