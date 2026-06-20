from . import logger
from liquid import Environment, FileSystemLoader
from marko import Markdown
from marko.html_renderer import HTMLRenderer
import os

markdown = Markdown(extensions=['gfm'], renderer=HTMLRenderer)

def render_page(content, navbar_content, dstFolder):
  logger.log.debug(f'Page content: {content}')
  env = Environment(loader=FileSystemLoader(f'{os.getcwd()}/src/templates', ext='.html'))

  template_name = None
  
  # Get template
  if 'template' in content['metadata']:
    template_name = content['metadata']['template']
  else:
    template_name = 'default'
  
  try:
    template = env.get_template(template_name)
  except:
    return logger.log.error(f'Template not found: {template_name}.html')

  # Convert Markdown content
  if content['metadata']['type'] == 'markdown':
    content['content'] = markdown.convert(content['content'])

  # Generate HTML file
  with open(f'{os.getcwd()}/{dstFolder}/{content['metadata']['uri']}.html', 'w') as outFile:
    try:
      outFile.write(template.render(page_metadata=content['metadata'], page_content=content['content'], navbar_content=navbar_content))
      logger.log.success(f'Page generated: /{content['metadata']['uri']}.html')
    except:
      return logger.log.error(f'Error while writing file: /{content['metadata']['uri']}.html')
  
  

