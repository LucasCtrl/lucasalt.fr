from liquid import Environment
from liquid import FileSystemLoader
from pathlib import Path

def createPages():
  env=Environment(loader=FileSystemLoader("src/templates", ext=".html"))
  template = env.get_template('default')

  pages = Path('src/pages').glob('**/*.html')

  for page in pages:
    pageContent = open(page, 'r').read()
    with open(f'dist/{page.name}', 'w') as file:
      file.write(template.render(page_content=pageContent, links=listPages()))

def listPages():
  pageList = []

  pages = Path('src/pages').glob('*.html')

  for page in pages:
    pageList.append({'uri': page.name, 'name': page.stem.capitalize()})

  return pageList

# print(listPages())
createPages()
