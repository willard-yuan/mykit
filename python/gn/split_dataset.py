# -*- coding: utf-8 -*-
# 说明：对文本行进行等分分割

import os
import glob

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]

parts = 10

dir_images = '/raid/yuanyong/geo_models/geo_imgs/*.jpg'
path_images = [os.path.join(dir_images, f) for f in sorted(glob.glob(dir_images)) if f.endswith('.jpg')]

blocks = split_list(path_images, wanted_parts = parts)
for i, block in enumerate(blocks):
    save_fname = str(i) + '.txt'
    f = open(save_fname, 'w')
    for item in block:
        f.write(item + '\n')
    f.close()
