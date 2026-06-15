import sys
from pathlib import Path
import frontmatter

def get_md_content(path):
  files = Path(path).glob('*.md')
  file_list = []

  for file in files :
    with open(file) as f:
      metadata, content = frontmatter.parse(f.read())
      if sys.flags.dev_mode:
        # In dev mode, retreive all the content
        file_list.append({"metadata": metadata, "content": content})
      else:
        if metadata['published']:
          # Otherwise, retreive only the content with the metadata published set to True
          file_list.append({"metadata": metadata, "content": content})

  return file_list
