import os
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
        # Images goes into the image processor
        shutil.copy(src_file, dst_file)
        img_compressor(src_file, dst_file)
      else:
        shutil.copy(src_file, dst_file)


def static_processor(src, dst):
  entries = os.scandir(src)
  _static_processor(entries=list(entries), src=src, dst=dst)
