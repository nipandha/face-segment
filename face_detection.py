
# coding: utf-8

# In[1]:


import sys
import dlib
from skimage import io
from PIL import Image, ImageDraw
import numpy as np
import argparse



parser = argparse.ArgumentParser(description='Face Detection')
parser.add_argument('--fname', type=str, default='fname', metavar='F',
                    help="image to be masked,output stored at name_mask.jpg")
args = parser.parse_args()
# In[2]:


def gen(fname):
    # Take the image file name from the command line
    file_name = fname

    # Create a HOG face detector using the built-in dlib class
    face_detector = dlib.get_frontal_face_detector()

    #win = dlib.image_window()

    # Load the image into an array
    image = io.imread(file_name)

    # Run the HOG face detector on the image data.
    # The result will be the bounding boxes of the faces in our image.
    detected_faces = face_detector(image, 1)

    print("I found {} faces in the file {}".format(len(detected_faces), file_name))

    # Open a window on the desktop showing the image
    #win.set_image(image)
    
    # Loop through each face we found in the image
    im = Image.open(fname)
    imgcopy = np.array(im)
    (height, width, _) = imgcopy.shape

    #draw = ImageDraw.Draw(im)
    for x in range(width):
        for y in range(height):
            imgcopy[y, x,:] = 255
    for i, face_rect in enumerate(detected_faces):

        # Detected faces are returned as an object with the coordinates 
        # of the top, left, right and bottom edges
        print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))
        #draw.line((face_rect.left(),face_rect.top(),face_rect.left(),face_rect.bottom()), fill=128)
        #draw.line((face_rect.right(),face_rect.top(),face_rect.right(),face_rect.bottom()), fill=128)
        #draw.line((face_rect.left(),face_rect.top(),face_rect.right(),face_rect.top()), fill=128)
        #draw.line((face_rect.left(),face_rect.bottom(),face_rect.right(),face_rect.bottom()), fill=128)
        for x in range(face_rect.left(),face_rect.right()+1):
            for y in range(face_rect.top(),face_rect.bottom()+1):
                imgcopy[y, x,:] = 0
    sf=fname.split('.')[0]+"_mask.jpg"
    print("Saving at "+sf)
    imcopy = Image.fromarray(imgcopy)
    imcopy.save(sf)
                    #del draw
        
    #im.save(fname.split('.')[0]+"_mask.jpg")
    # write to stdout
    
        # Draw a box around each face we found
        #win.add_overlay(face_rect)

    
    # Wait until the user hits <enter> to close the window	        
    dlib.hit_enter_to_continue()

gen(args.fname)

# In[23]:




