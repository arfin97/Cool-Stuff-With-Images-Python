# Introduction

This is a repository where I've accumulated all the codes and their their cheet sheet relating for image processsing in python usile *Pillow* library. This is more like a reference for my own learning path. You might also find it useful. Let's dig in..

# To run the scripts

To run the scripts you'll need to install a python library called Pillow. Link: https://pypi.org/project/Pillow/2.2.1/ 
This library will help you to work with images in python. 
Also you'll need to set up a folder structure that suits the code. I have given the folder of images that the codes were written for. The forlder name is Demo. If you want to see real time results with the scripts and the images, put the scripts into the Demo folder and run. Also this folder will be useful for your practicing. 

# Installing Pillow

Use the command: 
```
pip install pillow
```
# Using the scripts

We need to import the ```Pillow``` package to work with images and we need to import ```os``` module to work with files and folders.
The description of each scripts workings as follows.

## 1. Convert jpg to png

+ Used a loop to go throuh each files in the current folder ```for file in os.listdir('.'):```
+ ```os.listdir('.')``` returns the list of the files in the parameter folder, ```'.'``` means the current folder
+ ```if file.endswith('.jpg'):``` If the file name ends with ```.jpg``` We create an image object with that file. 
+ ```i = Image.open(file)``` is creating an image object named ```i``` using the ```file```
+ ```i.show()``` will open the image file using default viewer.
+ ```fn, fext = os.path.splitext(file)``` We are taking the ```file```'s path and splitting it. By default it'll split it in ```fn```=file name and ```fext``` = file extention.
+ ```i.save('pngs/{}.png'.format(fn))``` is saving the ```i``` image object in the folder ```png``` with the name ```fn```.png


## 2. Image resizer
By applying method ```.thumbnail(_)``` in the ```Image Object``` with a tuple ```(300,300)``` we can change the image sizes. We saved these images in a seperate folder named ```300```. 
+ ```i.thumbnail(size_700)``` is resizing the images to 700px by 700 pixel images using the tuple ```size_700 = (700, 700)```
+ ```i.save('700/{}_700.{}'.format(fn, fext))``` is saving the image in folder ```700/``` with the name ```original_700.same_extention```

## 3. Do rotate
It is fairly easy. We just need to apply ```.rotate(degree)``` method to the image object.
```python
image1 = Image.open('pup6.jpg')
image1.rotate(90).save('pup6_BW.jpg')
```
Note: We are also saving the image in current folder with ```pup6_BW.jpg``` name.
## 4. Turn black and white
It is also easy, no fancy tricks. Just need to apply ```.convert(mode='L')``` method to the image object.
```python
image1 = Image.open('pup6.jpg')
image1.convert(mode='L').save('pup6_BW.jpg')
```

## 5. Blurring
There's only one little difference between blurring and rotating or converting. We just need to import another module with ```Image``` module from the ```Pillow``` package. The module is ```ImageFilter```.

+ ```from PIL import Image, ImageFilter```
+ ```image1.filter(ImageFilter.GaussianBlur(15)).save('pup6_blur.jpg')```

We applied ```GaussianBlur``` with ```15``` radius using the ```ImageFilter.GaussianBlur(15)``` to the image.

# Reference
https://pillow.readthedocs.io/en/3.1.x/reference/Image.html

# My Folder Structure

###### Demo
###### --> pngs
###### --> 300
###### --> 700
###### --= ['1. Convert jpg to png.py', '2. Image resizer.py', '3. Do rotate.py', '300', '4. Turn black and white.py', '5. Turn blur.py', '700', 'pngs', 'pup1.jpg', 'pup2.jpg', 'pup3.jpg', 'pup4.jpg', 'pup5.png', 'pup6.jpg']

©Arfin
