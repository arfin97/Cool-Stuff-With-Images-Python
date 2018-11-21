from PIL import Image, ImageFilter
import os

image1 = Image.open('pup6.jpg')
image1.filter(ImageFilter.GaussianBlur(15)).save('pup6_blur.jpg')