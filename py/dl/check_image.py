from PIL import Image
import glob
import cv2
import os
import numpy as np

from PIL import Image

def check_pic(path):
    try:
        Image.open(path).load()
    except:
        print 'ERROR: %s' % path
        return False
    else:
        return True


imgs_list = glob.glob('/raid/yuanyong/neuralcode/ncdata/*/*')

for img_path in imgs_list:
    #img = Image.open(img_path)
    #if img.verify() is not None or img is None:
    #    print img_path
    try:
        img = Image.open(img_path)
        im = img.load()
    except IOError:
        print 'ERROR: %s' % img_path
        continue
    try:
        img = np.array(img, dtype=np.float32)
    except SystemError:
        print 'ERROR: %s' % img_path
        continue
    if len(img.shape) != 3:
        print 'ERROR: %s' % img_path
