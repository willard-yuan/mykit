#coding=utf-8
#Anthor: yuanyong.name

import numpy as np
import sys,os
import matplotlib
matplotlib.use('Agg')
import caffe
import cv2
import time

net_file = './models/deploy.prototxt'
caffe_model = './models/snapshots__iter_3000.caffemodel'
mean_file = './models/mean.npy'

caffe.set_device(0)
caffe.set_mode_gpu()

if __name__ == '__main__':

    net = caffe.Net(net_file, caffe_model, caffe.TEST)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
    transformer.set_raw_scale('data', 255) 
    transformer.set_channel_swap('data', (2,1,0))

    img_path = '/raid/yuanyong/magic/magic/1/2101234569_h.jpg'

    # a method to load image
    #im = caffe.io.load_image(img_path)

    # another method
    with open(img_path, 'rb') as infile:
        buf = infile.read()
    array = np.fromstring(buf, dtype='uint8')
    im = cv2.imdecode(array, 1)
    im = im / 255.
    im = im[:,:,(2,1,0)]

    # test timen with 50 times
    for i in range(50):
        start_time = time.time()
        net.blobs['data'].data[...] = transformer.preprocess('data', im)
        net.forward()
        # obtain the output probabilities
        output_prob = net.blobs['prob'].data[0]
        # sort top one predictions from softmax output
        top_inds = output_prob.argsort()[::-1][:1][0]
        print("--- %s seconds ---" % (time.time() - start_time))
        basename = os.path.basename(img_path)
        prob = output_prob[top_inds]
        print '%s %d %f' %(basename, top_inds, prob)
