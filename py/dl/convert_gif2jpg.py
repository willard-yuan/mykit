
from PIL import Image
import glob
import os

imgs_list = glob.glob('/raid/yuanyong/neuralcode/ncdata/*/*.png')

for img in imgs_list:
    print img
    basename = os.path.splitext(os.path.basename(img))[0] + '.jpg'
    dir_ = os.path.dirname(img)
    save_name = os.path.join(dir_, basename)
    im = Image.open(img).convert('RGB').save(save_name)
    os.remove(img)
