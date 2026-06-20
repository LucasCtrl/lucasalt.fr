import os
from liquid import Environment, FileSystemLoader
from marko import Markdown
from marko.html_renderer import HTMLRenderer
from . import logger
from module.utils import create_folder

markdown = Markdown(extensions=["gfm"], renderer=HTMLRenderer)


def render_page(content, site_content, dst_folder):
  logger.log.debug(f"Page content: {content, site_content}")
  env = Environment(
    loader=FileSystemLoader(f"{os.getcwd()}/src/templates", ext=".html")
  )

  template_name = None

  # Get template
  if "template" in content["metadata"]:
    template_name = content["metadata"]["template"]
  else:
    template_name = "default"

  try:
    template = env.get_template(template_name)
  except Exception as e:
    return logger.log.error(f"Template not found: {e}")

  # Convert Markdown content
  if content["metadata"]["type"] == "markdown":
    content["content"] = markdown.convert(content["content"])

  # Generate HTML file
  file_path = None
  if content["metadata"]["uri"] == "index":
    file_path = f"{os.getcwd()}/{dst_folder}/index.html"
  else:
    create_folder(f"{os.getcwd()}/{dst_folder}/{content['metadata']['uri']}")
    file_path = (
      f"{os.getcwd()}/{dst_folder}/{content['metadata']['uri']}/index.html"
    )

  with open(file_path, "w") as outFile:
    try:
      outFile.write(
        template.render(
          page_metadata=content["metadata"],
          page_content=env.render(
            content["content"], posts=site_content["posts"]
          ),
          navbar_content=site_content["navbar_content"],
        )
      )
      logger.log.success(f"Page generated: {file_path}")
    except Exception as e:
      return logger.log.error(f"Error while writing file: {e}")
