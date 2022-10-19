import os
from PIL import Image


catIm = Image.open('image.jpg')
print(catIm.size)
croppedIm = catIm.crop((0,390,520,780))
croppedIm.save('cropped.jpg')
