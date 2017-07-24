import os
from os import rename, listdir
imgAPath = 'A'
imgBPath = 'B'
imAlist = [os.path.basename(os.path.join(imgAPath,f)) for f in os.listdir(imgAPath)]
imBlist = [os.path.basename(os.path.join(imgBPath,f)) for f in os.listdir(imgBPath)]

abspath = os.path.dirname(os.path.abspath("./A/jaffe_KA.AN1.39_1.jpg"))

for i, filename in enumerate(imAlist):
    os.rename(os.path.join(abspath,filename), os.path.join(abspath,imBlist[i]))