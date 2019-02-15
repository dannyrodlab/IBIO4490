#!/bin/py

import subprocess
import os
import matplotlib.pyplot as plt
import numpy as np
import math
import shutil
import time

start_time = time.time()

## Let us put things in order ##
folder = '/media/disk1/vision/dannyrodlab/'
os.chdir(folder)

link_database = "http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz"
name_file = "BSR_bsds500.tgz"
name_folder = "BSR"

## If file exists, don't download it ##
if os.path.isfile(name_file):
    ## Show an error ##
    print("Error: %s - File already exists" % name_file)
else:
    subprocess.call(['wget',link_database])

if os.path.isfile(name_file):
    subprocess.call(['tar','-zxvf', name_file])
else:
    print("Error: Database not found.")
    break

# Random number of images between 6 and 24
number_images = irandom.randint(6,24)

# Holder of all images
image_holder = []

# Where them images are
path = '/BSR/BSDS500/data/images/test'

# Create temporal directory
dirName = '/tempDir'

try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " created ") 
except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))

# Randomly select images from the directory
for in range(1, number_images):
    name_random_file = random.choice([image for image in os.listdir(path) if os.path.isfile(os.path.join(path, image))])
    img = Image.open(name_random_file)
    # Make image of the proper dimensions
    new_img = img.resize((256,256))
    image_holder.append(new_img)
    # Save image in temporal directory
    img.save(os.path.join(dirName,name_random_file), 'JPEG')
    # Boundaries
    # Groundtruth

# Get the image size (all images have size [256x256])
x,y = image_holder[0].size

# Number of rows and columns in new large image.
ncol = nrow = math.ceil(math.sqrt(number_images))

# Generate the canvas to arrange all images just loaded.
canvas = Image.new('RGB',(x*ncol, y *nrow)
# Paste images
for i in range(len(image_holder)):
	px, py = x*int(i/nrow), y*(i%nrow)
    canvas.paste(image_holder[i],(px,py))
# Save the beautiful canvas in location
location = '/home/vision/dannyrodlab/tempDir/my_beautiful_canvas.png'
canvas.save(location,format='png')

## Display image
subprocess.call(['eog',location])

## Try to delete the file ##
try:
        os.remove(name_file)
except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))

## Try to remove tree; if failed show an error using try...except on screen
try:
        shutil.rmtree(name_folder)
except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror)

## Try to remove temporal directory; if failed show an error using try...except on screen
try:
        shutil.rmtree(dirName)
except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror)
            
print("--- %s seconds ---" % (time.time() - start_time))
