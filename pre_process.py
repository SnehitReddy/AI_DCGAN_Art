import os
from PIL import Image

data_dir = './dataset/'
save_dir = './DCGAN/processed_data/0/'

image_size = 64

if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

img_list = os.listdir(data_dir)

for i in range(100000):
    img = Image.open(data_dir + img_list[i])
    img = img.resize((image_size, image_size), Image.BILINEAR)
    img.save(save_dir + img_list[i], 'JPEG')

    if i % 1000 == 0:
        print('Resizing %d images...' % i)