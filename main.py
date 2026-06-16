from module import logger
from module.get_content import get_content
from module.html_renderer import render_page

logger.init_logger(mode="DEBUG")

def generate_static_site():
  logger.log.set("Starting the generator")
  pages = get_content('src/pages')

  for page in pages:
    render_page(page, 'dist')

if __name__ == "__main__":
  generate_static_site()
