import cv2
import os
import glob
from skimage import io
from matplotlib import pyplot as plt
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_ubyte, img_as_float
import numpy as np
from skimage import io

img_dir = "path to the images folder" # Enter Directory of all images
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
i=0

names = [os.path.basename(x) for x in glob.glob(data_path)]

for f1 in files:
    #img = img_as_float(io.imread(f1))
    img = cv2.imread(f1)
    # Converting image to LAB Color so CLAHE can be applied to the luminance channel
    lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    # Splitting the LAB image to L, A and B channels, respectively
    l, a, b = cv2.split(lab_img)
    ###########Histogram Equlization#############
    # Apply histogram equalization to the L channel
    equ = cv2.equalizeHist(l)
    # Combine the Hist. equalized L-channel back with A and B channels
    updated_lab_img1 = cv2.merge((equ, a, b))
    # Convert LAB image back to color (RGB)
    hist_eq_img = cv2.cvtColor(updated_lab_img1, cv2.COLOR_LAB2BGR)
    ###########CLAHE#########################

    cv2.imwrite('prefixname'+str(names[i]), hist_eq_img)
    i+=1


# print(i)



