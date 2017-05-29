
import os
import glob
import argparse
import numpy as np
import random

classes_path  = glob.glob('/raid/yuanyong/neuralcode/ncdata/*')
train_samples = []
val_samples = []

imgs_total = 0

for i, class_path in enumerate(classes_path):
    class_ = class_path.split('/')[-1]
    imgs_path = glob.glob(class_path + '//*')
    num_imgs = len(imgs_path)
    num_train = int(num_imgs*0.6)
    num_val = num_imgs - num_train

    np.random.seed(1024)
    sample_idx = np.random.choice(range(num_imgs), num_imgs, replace=False)
    train_idx = sample_idx[0:num_train]
    val_idx = sample_idx[num_train:]

    for idx_ in train_idx:
        img_path = imgs_path[idx_]
        train_samples.append(img_path + ' ' + class_ + '\n')

    for idx_ in val_idx:
        img_path = imgs_path[idx_]
        val_samples.append(img_path + ' ' + class_ + '\n')

    imgs_total += num_imgs


random.shuffle(train_samples)
random.shuffle(val_samples)

with open('lmdb/train.txt', 'w') as f_train, open('lmdb/val.txt', 'w') as f_val:
    for sample in train_samples:
        f_train.write(sample)
    for sample in val_samples:
        f_val.write(sample)
