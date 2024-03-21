import sys, traceback
import cv2
import os
import re
import numpy as np
import argparse
import string
from plantcv import plantcv as pcv

### Parse command-line arguments
def options():
    parser = argparse.ArgumentParser(description="Imaging processing with opencv")
    parser.add_argument("-i", "--image", help="Input image file.", required=True)
    parser.add_argument("-o", "--outdir", help="Output directory for image files.", required=True)
    parser.add_argument("-n", "--names", help="path to txt file with names of genotypes to split images into", required =False)
    parser.add_argument("-D", "--debug", help="Turn on debug, prints intermediate images.", action=None)
    args = parser.parse_args()
    return args

### Main workflow
def main():
    # Get options
    args = options()

    # Read image
    img, path, filename = pcv.readimage(args.image)

    pcv.params.debug= "print" #args.debug #set debug mode

    # STEP 1: Check if this is a night image, for some of these dataset's images were captured
    # at night, even if nothing is visible. To make sure that images are not taken at
    # night we check that the image isn't mostly dark (0=black, 255=white).
    # if it is a night image it throws a fatal error and stops the workflow.

    if np.average(img) < 50:
        pcv.fatal_error("Night Image")
    else:
        pass

    # STEP 2: Normalize the white color so you can later
    # compare color between images.
    # Inputs:
    #   img = image object, RGB colorspace
    #   roi = region for white reference, if none uses the whole image,
    #         otherwise (x position, y position, box width, box height)

    # white balance image based on white toughspot

    #img1 = pcv.white_balance(img=img,roi=(400,800,200,200))
    img1 = pcv.white_balance(img=img, mode='hist', roi=None)

    # STEP 3: Rotate the image
    # Inputs:
    #   img = image object, RGB color space
    #   rotation_deg = Rotation angle in degrees, can be negative, positive values 
    #                  will move counter-clockwise 
    #   crop = If True then image will be cropped to original image dimensions, if False
    #          the image size will be adjusted to accommodate new image dimensions 


    rotate_img = pcv.transform.rotate(img=img1,rotation_deg=-1, crop=False)

    # STEP 4: Shift image. This step is important for clustering later on.
    # For this image it also allows you to push the green raspberry pi camera
    # out of the image. This step might not be necessary for all images.
    # The resulting image is the same size as the original.
    # Inputs:
    #   img    = image object
    #   number = integer, number of pixels to move image
    #   side   = direction to move from "top", "bottom", "right","left"

    shift1 = pcv.shift_img(img=img1, number=300, side='top')
    img1 = shift1

    # STEP 5: Convert image from RGB colorspace to LAB colorspace
    # Keep only the green-magenta channel (grayscale)
    # Inputs:
    #    img     = image object, RGB colorspace
    #    channel = color subchannel ('l' = lightness, 'a' = green-magenta , 'b' = blue-yellow)

    #a = pcv.rgb2gray_lab(img=img1, channel='a')
    a = pcv.rgb2gray_lab(rgb_img=img1, channel='a')

    # STEP 6: Set a binary threshold on the saturation channel image
    # Inputs:
    #    img         = img object, grayscale
    #    threshold   = threshold value (0-255)
    #    max_value   = value to apply above threshold (usually 255 = white)
    #    object_type = light or dark
    #       - If object is light then standard thresholding is done
    #       - If object is dark then inverse thresholding is done

    img_binary = pcv.threshold.binary(gray_img=a, threshold=120, object_type='dark')
    #img_binary = pcv.threshold.binary(gray_img=a, threshold=120, max_value=255, object_type'dark')
    #                                                   ^
    #                                                   |
    #                                     adjust this value

    # STEP 7: Fill in small objects (speckles)
    # Inputs:
    #    bin_img  = image object, binary. img will be returned after filling
    #    size = minimum object area size in pixels (integer)

    fill_image = pcv.fill(bin_img=img_binary, size=10)
    #                                          ^
    #                                          |
    #                           adjust this value

    rois = pcv.roi.auto_grid(mask=a_fill, nrows=4, ncols=5, img=img)



    labeled_mask, num_plants = pcv.create_labels(mask=a_fill, rois=rois, roi_type="partial")



    shape_img = pcv.analyze.color(rgb_img=img, labeled_mask=labeled_mask, n_labels=20, colorspaces="HSV")

    pcv.outputs.save_results(filename=args.outdir)


    pcv.params.debug = "print"

    out = args.outdir
    names = args.names

    output_path, imgs, masks = pcv.cluster_contour_splitimg(rgb_img=img1, grouped_contour_indexes=clusters_i, 
                                                            contours=contours, hierarchy=hierarchies, 
                                                            outdir=out, file=filename, filenames=names)
    #output_path, imgs, masks = pcv.cluster_contour_splitimg(rgb_img, grouped_contour_indexes, contours, hierarchy)

# Call program
if __name__ == '__main__':
    main()