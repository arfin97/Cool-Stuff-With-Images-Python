from PIL import Image
import os

for file in os.listdir('.'):
	print(os.listdir('.'))
	if file.endswith('.jpg'):

		i = Image.open(file)
		i.show()
		fn, fext = os.path.splitext(file)
		print(fn, fext)
		i.save('pngs/{}.png'.format(fn))

image1 = Image.open('pup6.jpg')
