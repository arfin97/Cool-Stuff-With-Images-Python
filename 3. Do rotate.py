from PIL import Image
import os

image1 = Image.open('pup6.jpg')
image1.rotate(90).save('pup6_90.jpg')