import imageio.v3 as iio
from PIL import Image,ImageOps
import numpy as np

filenames=['monkey2.jpeg','monkey3.jpeg','monkey5.jpeg']
images=[]

#to resize my images to the same size
base_image=Image.open(filenames[0])
base_image=ImageOps.exif_transpose(base_image)
base_size=base_image.size

for filename in filenames:
    img=Image.open(filename)
    img=ImageOps.exif_transpose(img)
    img=img.resize(base_size)
    images.append(np.array(img))
    
iio.imwrite('me.gif',images,duration=500,loop=0)