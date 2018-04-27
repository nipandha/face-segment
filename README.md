![Img](https://github.com/nipandha/face-segment/blob/master/1.jpg)
This is the implementation of ‘Scaled Neural Style Transfer for Bounded Face Regions’

I) To create a regular Neural Style Image Transfer:
1. Run the following command with these arguments provided: usage: nst_baseline.py [-h] [--height H] [--width W] [--input I] [--style S]
[--num_iter N]

Neural Style Transfer

optional arguments:
-h, --help    show this help message and exit
--height H    image height
--width W     image width
--input I     input content image
--style S     style image
--num_iter N  number of iterations to run the style transfer
II) To create a masked face style transfer:
1. Generate a mask file for the face image by running the following:
usage: face_detection.py [-h] [--fname F]

Face Detection

optional arguments:
-h, --help  show this help message and exit
--fname F   image to be masked,output stored at name_mask.jpg

2. Run the Neural Style Transfer giving the mask file as input mask_img: usage: neural_style_transfer.py [-h] [--height H] [--width W] [--factor FC]
[--mask_img M] [--input I] [--style S]
[--num_iter N]

PyTorch Gentle Neural Style Transfer for Faces

optional arguments:
-h, --help    show this help message and exit
--height H    image height
--width W     image width
--factor FC   factor of making style less pronounced on mask
--mask_img M  mask image
--input I     input content image
--style S     style image
--num_iter N  number of iterations to run the style transfer

Contact:
nitishavp@gmail.com, anandsb7@gmail.com
# face-segment
