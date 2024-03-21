
from plantcv import plantcv as pcv

# Set global debug behavior to None (default), "print" (to file), 
# or "plot" (Jupyter Notebooks or X11)

pcv.params.debug = "plot"

# Crop image
crop_img = pcv.auto_crop(img="M:\EMBRAPA\codigos\LIA-EMBrAPA\parcelas_B3B4_0_5CM_12-03-19\0-5_12-03-19.png", padding_x=20, padding_y=20, color='black')

crop_img2 = pcv.auto_crop(img=rgb_img, mask=bin_mask, padding_x=20, padding_y=20, color='image')
