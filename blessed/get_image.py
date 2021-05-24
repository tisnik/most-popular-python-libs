"""Retrieve test image, resize it, and store under new filename."""

from PIL import Image
import urllib.request

url = "https://homepages.cae.wisc.edu/~ece533/images/fruits.png"

original_filename = "fruits_.png"
resized_filename = "fruits.png"

urllib.request.urlretrieve(url, original_filename)

img = Image.open(original_filename)
resized = img.resize((128, 128), Image.BILINEAR)
resized.save(resized_filename)
