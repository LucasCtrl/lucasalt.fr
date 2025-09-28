import os
import shutil
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

def copyStaticContent():
  if not os.path.exists('dist/styles'):
      os.makedirs('dist/styles')

  shutil.rmtree('dist/styles')
  shutil.copytree('src/styles', 'dist/styles')

def createPostPages():
  env=Environment(loader=FileSystemLoader("src/templates", ext=".html"))
  template = env.get_template('default')

  posts = Path('src/posts').glob('**/*.html')

  for post in posts:
    if not os.path.exists('dist/posts'):
      os.makedirs(f'dist/posts/{post.stem}')

    postContent = open(post, 'r').read()
    with open(f'dist/posts/{post.stem}/index.html', 'w') as file:
      file.write(template.render(page_content=postContent, links=listPages()))

  # for page in pages:
  #   pageContent = open(page, 'r').read()
  #   with open(f'dist/{page.name}', 'w') as file:
  #     file.write(template.render(page_content=pageContent, links=listPages()))

copyStaticContent()
createPages()
createPostPages()
