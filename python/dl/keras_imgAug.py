#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author: yuanyong.name

import os
import random
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

num_wanted = 800
target_path_dir = '/raid/yuanyong/neuralcode/ncdata'

datagen = ImageDataGenerator(
        rotation_range = 10,
        width_shift_range = 0.2,
        height_shift_range = 0.2,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        fill_mode = 'nearest')

sub_dirs = os.walk(target_path_dir).next()[1]
for k, sub_dir in enumerate(sub_dirs):
    print 'to be processed: %s (%d/%d), contains images: %d' % (sub_dirs, k+1, len(sub_dirs), sub_dir, len(img_basenames))
    sub_dir_full = os.path.join(target_path_dir, sub_dir)
    img_basenames = os.listdir(sub_dir_full)
    num_imgs = len(img_basenames)
    num_perAug = int(float(num_wanted)/float(num_imgs)) - 1
    if num_imgs >= num_wanted:
        continue
    num_total = 0
    for i, img_basename in enumerate(img_basenames):
        num_total = num_imgs + i*num_perAug
        if num_total >= num_wanted:
            break
        img_path = os.path.join(sub_dir_full, img_basename)
        #print "Aug: %s" % img_path
        img = load_img(img_path) # this is a PIL image, please replace to your own file path
        if img == None:
            continue
        try:
            x = img_to_array(img) # this is a Numpy array with shape (3, 150, 150)
            x = x.reshape((1,) + x.shape) # this is a Numpy array with shape (1, 3, 150, 150)
            i = 0
            for batch in datagen.flow(x, batch_size = 1, save_to_dir = sub_dir_full, save_prefix = 'aug', save_format = 'jpg'):
                i += 1
                if i >= num_perAug:
                    break # otherwise the generator would loop indefinitely
        except:
            print "%s" % img_path

# delete extra aug images
for sub_dir in sub_dirs:
    sub_dir_full = os.path.join(target_path_dir, sub_dir)
    img_basenames = os.listdir(sub_dir_full)
    num_imgs = len(img_basenames)
    if num_imgs <= num_wanted:
        continue
    aug_imgs = [img_basename for img_basename in img_basenames if img_basename.startswith('aug_')]
    random.shuffle(aug_imgs, random.random)
    num_del = num_imgs - num_wanted
    aug_imgs_del = aug_imgs[-num_del:]

    for img_basename in aug_imgs_del:
        img_full = os.path.join(sub_dir_full, img_basename)
        os.remove(img_full)
