from . import logger
from liquid import Environment, FileSystemLoader
from marko import Markdown
from marko.html_renderer import HTMLRenderer
import os

markdown = Markdown(extensions=['gfm'], renderer=HTMLRenderer)

def render_page(content, dstFolder):
  logger.log.debug(f'Page content: {content}')
  env = Environment(loader=FileSystemLoader(f'{os.getcwd()}/src/templates', ext='.html'))

  template_name = None
  
  if 'template' in content['metadata']:
    template_name = content['metadata']['template']
  else:
    template_name = 'index'

  try:
    template = env.get_template(template_name)

    try:
      with open(f'{os.getcwd()}/{dstFolder}/{content['metadata']['uri']}.html', 'w') as outFile:
        try:
          outFile.write(template.render(page_content=content['content']))
          logger.log.success(f'Page generated: /{content['metadata']['uri']}.html')
        except:
          logger.log.error(f'Error while writing file: /{content['metadata']['uri']}.html')
    except:
      logger.log.error(f'Error while opening file: /{content['metadata']['uri']}.html')
  except:
    logger.log.error(f'Template not found: {template_name}.html')
  

