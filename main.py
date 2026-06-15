from module.logger import log
from module.md_content import get_md_content

def generate_static_site():
  log("Starting the generator", 'INFO')
  pages = get_md_content('src/pages')
  posts = get_md_content('src/posts')
  print(pages)
  print(posts)

if __name__ == "__main__":
  generate_static_site()
