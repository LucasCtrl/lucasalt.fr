import sys
import os
from pathlib import Path
import frontmatter


def get_content(path):
  files = Path(path).glob("*")
  file_content = []

  for file in files:
    with open(file) as f:
      file_name = os.path.basename(file)
      uri, ext = os.path.splitext(file_name)
      metadata, content = frontmatter.parse(f.read())

      # Add required metadata
      if "navbar" not in metadata:
        metadata["navbar"] = False
      if "navbarPos" not in metadata:
        metadata["navbarPos"] = 100
      if "published" not in metadata:
        metadata["published"] = True
      if "uri" not in metadata:
        metadata["uri"] = uri
      if "title" not in metadata:
        metadata["title"] = uri[0].upper() + uri[1:]
      if ext == ".md":
        metadata["type"] = "markdown"
      elif ext == ".html":
        metadata["type"] = "html"

      if sys.flags.dev_mode:
        # In dev mode, retreive all the content
        file_content.append({"metadata": metadata, "content": content})
      else:
        if metadata["published"]:
          # Otherwise, retreive only the content with the metadata published set to True
          file_content.append({"metadata": metadata, "content": content})

  return file_content
