from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import cv2
import os
import glob


img_dir = "path to the images folder" # Enter Directory of all images
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
i=0
names = [os.path.basename(x) for x in glob.glob(data_path)]

for f1 in files:

    image = imread(f1)

    # selecting part of the image only
    cropped = image[100:(image.shape[0]-100),100:(image.shape[1]-100)]

    plt.imsave('prefixname' + str(names[i]), cropped)
    i += 1


print(i)