import os

path_ = '/raid/yuanyong/neuralcode/ncdata'
dirs = os.walk(path_).next()[1]

dirs.sort()

for i, dir_ in enumerate(dirs):
    print '%d, %s' %(i, dir_)
    os.rename(os.path.join(path_, dir_), os.path.join(path_, str(i)))
