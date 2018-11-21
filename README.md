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


## 2. image resizer
By applying method ```.thumbnail(_)``` in the ```Image Object``` with a tuple ```(300,300)``` we can change the image sizes. We saved these images in a seperate folder named ```300```. 
+ ```i.thumbnail(size_700)``` is resizing the images to 700px by 700 pixel images using the tuple ```size_700 = (700, 700)```
+ ```i.save('700/{}_700.{}'.format(fn, fext))``` is saving the image in folder ```700/``` with the name ```original_700.same_extention```

## 1. Opening Files
## 1. Opening Files
