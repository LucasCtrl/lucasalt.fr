import os
import sys
import shutil
import frontmatter
from pathlib import Path
from marko import Markdown
from marko.html_renderer import HTMLRenderer
from liquid import Environment
from liquid import FileSystemLoader

class CustomMarkoRenderer(HTMLRenderer):
  def render_image(self, element):
    url = element.dest
    alt_text = self.render_children(element)

    html = (
      f'<figure>\n'
      f'  <a href="{url}" target="_blank">\n'
      f'    <img src="{url}" alt="{alt_text}" />\n'
      f'  </a>\n'
      f'  <figcaption>{alt_text}</figcaption>\n'
      f'</figure>'
    )

    return html

markdown = Markdown(extensions=['gfm', 'footnote'], renderer=CustomMarkoRenderer)

def log(message):
  print(f'[Log] - {message}')

# Get all posts listed in 'posts' folder
def getPosts():
  postFiles = Path('src/posts').glob('*.md')
  postList = []
  for postFile in postFiles:
    with open(postFile) as f:
      metadata, content = frontmatter.parse(f.read())
      if sys.flags.dev_mode:
        postList.append({'title': metadata['title'], 'publishDate': metadata['publishDate'], 'uri': f'posts/{postFile.stem}', 'content': content})
      else:
        if metadata['published']:
          postList.append({'title': metadata['title'], 'publishDate': metadata['publishDate'], 'uri': f'posts/{postFile.stem}', 'content': content})
  return postList

# Get all pages listed in 'pages' folder
def getPages():
  pageFiles = Path('src/pages').glob('*.md')
  pageList = []
  for pageFile in pageFiles:
    with open(pageFile) as f:
      metadata, content = frontmatter.parse(f.read())
      if sys.flags.dev_mode:
        pageList.append({'title': metadata['title'], 'uri': pageFile.stem, 'navbar': metadata['navbar'], 'content': content})
      else:
        if metadata['published']:
          pageList.append({'title': metadata['title'], 'uri': pageFile.stem, 'navbar': metadata['navbar'], 'content': content})
  return pageList

# Generate static content
def copyStaticContent(outputFolder):
  log('Copying static files')
  shutil.copytree('src/static', outputFolder, dirs_exist_ok=True)

# Generate index page
def createIndexPage(outputFolder):
  env=Environment(loader=FileSystemLoader("src/templates", ext=".html"))
  template = env.get_template('index')

  log('Creating index.html')
  with open(f'{outputFolder}/index.html', 'w') as file:
    file.write(template.render(navItems=getPages(), postList=getPosts()))

# Generate pages
def createPages(outputFolder):
  env=Environment(loader=FileSystemLoader("src/templates", ext=".html"))
  template = env.get_template('page')

  for page in getPages():
    pageUri = page['uri']
    pageTitle = page['title']
    pageContent = markdown.convert(page['content'])

    if not os.path.exists(f'dist/{pageUri}'):
      os.makedirs(f'dist/{pageUri}')

    log(f'Creating {pageUri}/index.html')
    with open(f'{outputFolder}/{pageUri}/index.html', 'w') as file:
      file.write(template.render(navItems=getPages(), pageContent=pageContent, title=pageTitle))

# Generate posts pages
def createPostsPage(outputFolder):
  env=Environment(loader=FileSystemLoader("src/templates", ext=".html"))
  template = env.get_template('post')

  for post in getPosts():
    postUri = post['uri']
    postTitle = post['title']
    postPublishDate = post['publishDate']
    postContent = markdown.convert(post['content'])

    if not os.path.exists(f'dist/{postUri}'):
      os.makedirs(f'dist/{postUri}')

    log(f'Creating {postUri}/index.html')
    with open(f'{outputFolder}/{postUri}/index.html', 'w') as file:
      file.write(template.render(navItems=getPages(), postContent=postContent, title=postTitle, publishDate=postPublishDate))

def main():
  outputFolder = 'dist'

  # Delete 'dist' folder if he exists
  if os.path.exists(outputFolder):
    shutil.rmtree(outputFolder)

  # Create 'dist' folder
  if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

  copyStaticContent(outputFolder)
  createIndexPage(outputFolder)
  createPostsPage(outputFolder)
  createPages(outputFolder)

if __name__ == '__main__':
  main()
