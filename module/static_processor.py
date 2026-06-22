import os
import re
import shutil
from PIL import Image
from . import logger


def img_compressor(src, dst):
  outPath, ext = os.path.splitext(dst)
  try:
    with Image.open(src) as image:
      if image.width > 1280 or image.height > 720:
        imgRatio = image.width / image.height
        reduced_size = (1280, int(1280 / imgRatio))
        resized_image = image.resize(size=reduced_size)
        resized_image.save(f"{outPath}.webp", quality=80)
      else:
        image.save(f"{outPath}.webp", quality=80)
  except OSError:
    logger.log.error(f"Cannot convert: {src}")


def css_minifier(src, dst):
  """Minify CSS by removing comments, whitespace, and optimizing syntax."""
  css = None
  with open(src) as f:
    css = f.read()

  # Step 1: Remove all comments (/* ... */)
  css = re.sub(r"/\*[\s\S]*?\*/", "", css)

  # Step 2: Remove whitespace and normalize syntax
  css = re.sub(r"\s+", " ", css).strip()  # Collapse whitespace and trim
  css = re.sub(r" {", "{", css)  # Remove space before "{"
  css = re.sub(r"{ ", "{", css)  # Remove space after "{"
  css = re.sub(r" :", ":", css)  # Remove space before ":"
  css = re.sub(r": ", ":", css)  # Remove space after ":"
  css = re.sub(r" ;", ";", css)  # Remove space before ";"
  css = re.sub(r"; ", ";", css)  # Remove space after ";"
  css = re.sub(r" ,", ",", css)  # Remove space before ","
  css = re.sub(r", ", ",", css)  # Remove space after ","

  # Step 3: Shorten 6-character hex colors to 3-character (e.g., #aabbcc → #abc)
  css = re.sub(
    r"#([0-9a-fA-F])\1([0-9a-fA-F])\2([0-9a-fA-F])\3", r"#\1\2\3", css
  )

  # Step 4: Remove redundant semicolons before closing braces
  css = re.sub(r";}", "}", css)

  # Step 5: write output file
  with open(dst, "a") as f:
    f.write(css)


def _static_processor(entries, src, dst):
  for entry in entries:
    src_file = os.path.join(src, entry.name)
    dst_file = os.path.join(dst, entry.name)

    if entry.is_dir():
      # If entry is a folder, scan it
      os.makedirs(dst_file, exist_ok=True)
      static_processor(src=src_file, dst=dst_file)
    else:
      # Otherwise, it's a file, process it
      if src_file.endswith("png") or src_file.endswith("jpg"):
        shutil.copy(src_file, dst_file)
        img_compressor(src_file, dst_file)
      elif src_file.endswith("css"):
        css_minifier(src_file, dst_file)
      else:
        shutil.copy(src_file, dst_file)


def static_processor(src, dst):
  entries = os.scandir(src)
  _static_processor(entries=list(entries), src=src, dst=dst)
