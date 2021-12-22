import cv2
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_ubyte, img_as_float
from matplotlib import pyplot as plt
from skimage import io
import numpy as np
import os
import glob

img_dir = "path to the images folder" # Enter Directory of all images
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
i=3870
for f1 in files:
    img = img_as_float(io.imread(f1))



    #Need to convert to float as we will be doing math on the array

    from scipy import ndimage as nd


    ##### NLM#####

    sigma_est = np.mean(estimate_sigma(img, multichannel=True))

    denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=True,
                                   patch_size=5, patch_distance=3, multichannel=True)

    plt.imsave('prefixname' + str(i) + '.jpeg', denoise_img)
    i += 1
    data.append(img)

# print(len(data))