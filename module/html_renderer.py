import os
from liquid import Environment, FileSystemLoader
from marko import Markdown
from marko.html_renderer import HTMLRenderer
from . import logger
from module.utils import create_folder


class CustomMarkoRenderer(HTMLRenderer):
  def render_heading(self, element):
    level = element.level
    title = self.render_children(element)
    id = title.lower().replace(" ", "_")
    return f"<h{level} id='{id}'>{title}</h{level}>"

  def render_image(self, element):
    imgPath = element.dest
    path, ext = os.path.splitext(imgPath)

    alt_text = self.render_children(element)

    html = (
      f"<figure>\n"
      f'  <a href="{imgPath}" target="_blank">\n'
      f'    <img src="{path}.webp" alt="{alt_text}" />\n'
      f"  </a>\n"
      f"  <figcaption>{alt_text}</figcaption>\n"
      f"</figure>"
    )

    return html


markdown = Markdown(
  extensions=["gfm", "footnote", "codehilite"], renderer=CustomMarkoRenderer
)


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
