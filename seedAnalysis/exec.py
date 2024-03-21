import os
import argparse
import matplotlib
import cv2
import numpy as np

from plantcv import plantcv as pcv

# Input image into self.image (include file path if image is not in 
# the same folder as jupyter notebook)

# Set self.debug to "plot" so that image outputs for each step is shown
# once cell is run in jupyter notebooks (recommended)

class options:
    def __init__(self):        
        self.image = "./quinoa_seeds.jpg" # "./1_12-04-19.jpeg"  "./quinoa_seeds.jpg"  "./1_12-01-19.png"
        self.debug = "print" # ou "plot" para apenas exibir as saídas, sem salvar em arquivos
        self.writeimg = False
        self.result = "seed_analysis_results"
        self.outdir = "."

# Get options
args = options()

# Set debug to the global parameter
pcv.params.debug = args.debug

# Set plotting size (default = 100)
pcv.params.dpi = 100

# Increase text size and thickness to make labels clearer
# (size may need to be altered based on original image size)
pcv.params.text_size = 10
pcv.params.text_thickness = 20

# Inputs:
#   filename = Image file to be read in 
#   mode     = How to read in the image; either 'native' (default), 'rgb', 'gray', or 'csv'
img, path, filename = pcv.readimage(filename=args.image)

# Inputs:
#   x = top left x-coordinate
#   y = top left y-coordinate
#   h = height of final cropped image
#   w = width of final cropped image



#para executar turorial, "descomentar" essa linha
# print("Initial crop")
# img = pcv.crop(img=img, x=1300, y=750, h=1750, w=2100)
# print("End!\n")




# Inputs:
#   rbg_img      = original image
#   original_img = whether to include the original RGB images in the display: True (default) or False
print("See different spectrums")
colorspace_img = pcv.visualize.colorspaces(rgb_img=img)
print("End!\n")

# Inputs:
#   rbg_img - original image
#   channel - desired colorspace ('l', 'a', or 'b')
print("Show black spectrum")
b_img = pcv.rgb2gray_lab(rgb_img=img, channel='b')
print("End!\n")

#Channel B is used because it provides the best separation of seeds from background.


# Inputs:
#   img         = gray image in selected colorspace
#   mask        = None (default), or mask
#   bins        = 100 (default) or number of desired number of evenly spaced bins
#   lower-bound = None (default) or minimum value on x-axis
#   upper-bound = None (default) or maximum value on x-axis
#   title       = None (default) or custom plot title
#   hist_data   = False (default) or True (if frequency distribution data is desired)
print("See histogram")
hist = pcv.visualize.histogram(img=b_img)
print("End!\n")

# Inputs:
#   gray_img    = black and white image created from selected colorspace
#   threshold   = cutoff pixel intensity value (all pixels below value will become black, all above will become white)
#   object_type = 'dark' or 'light' depending on if seeds are darker or lighter than background.
print("Define contrast of background and seeds")
b_thresh = pcv.threshold.binary(gray_img=b_img, threshold=140, object_type='light') 
print("End!\n")

# Inputs:
#   bin_img - binary mask image
#   size - maximum size for objects that should be filled in as background (non-plant) pixels
b_fill = pcv.fill(bin_img=b_thresh, size=300)
#                                         ^
#                                         |
#                                 change this value

#Labeled mask is the mask which labels each individual seed to allow it to be measured.

        #Inputs:
        #Mask = mask created earlier in workflow
print("Create labels")
labeled_mask, num = pcv.create_labels(mask=b_fill)
print("End!\n")

#Find number of objects in image. Num=number of seeds captured in image.

print ("Number of objects in image "+str(num)+"\n")

        # Analyze shape and size perameters of each seed
        #
        # Inputs:
        #   img = rgb image
        #   mask = mask which has labeled each individual seed in image
        #   label = how many labels based on number of seeds in image. Num->all seeds in image
print("Show shape")
shape_img = pcv.analyze.size(img=img, labeled_mask=labeled_mask, n_labels=num)
print("End!\n")

        # Analyze color of each seed
        #
        # Inputs:
        #   img = rgb image
        #   labeled_mask = labeled mask
        #   hist_plot_type = 'hsv', or None for no histogram plot
        #   n_labels = 'num' 
print("Show difference of color of each seed")
analysis_image = pcv.analyze.color(rgb_img=img, labeled_mask=b_fill, n_labels=num, colorspaces='hsv')
print("End!\n")

print("let's crop!")
# Crop image
crop_img = pcv.auto_crop(img=img, mask=b_fill, padding_x=20, padding_y=20, color='black')
print("End crop!\n")

# Inputs:
#   img = image for shape analysis
pcv.plot_image(img=shape_img)

# Inputs:
#   img = image for color analysis
pcv.plot_image(img=img)

# Inputs:
#   filename  = filename for saving results
#   outformat = output file format: "json" (default) hierarchical format or "csv" tabular format
pcv.outputs.save_results(filename=args.result, outformat="csv")