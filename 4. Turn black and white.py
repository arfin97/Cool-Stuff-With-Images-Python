from PIL import Image
import os

image1 = Image.open('pup6.jpg')
image1.convert(mode='L').save('pup6_BW.jpg')