#coding=utf-8
#Author: yongyuan.name

import numpy as np
import sys,os
import matplotlib
matplotlib.use('Agg')
import caffe
import time
import cv2

MODEL = "snapshots__iter_3000.caffemodel"
PROTO = "deploy.prototxt"
MEAN = "mean.npy"


class EmojiPredictModel(object):

  def __init__(self, gpuid, modelDir):
    self.gpuid = gpuid
    self.model = os.path.join(modelDir, MODEL)
    self.proto = os.path.join(modelDir, PROTO)
    self.mean = os.path.join(modelDir, MEAN)
    self.initcaffe()
  
  def initcaffe(self):
    caffe.set_device(self.gpuid)
    caffe.set_mode_gpu()
    self.net = caffe.Net(self.proto, self.model, caffe.TEST)
    self.net.forward()
    self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
    self.transformer.set_transpose('data', (2,0,1))
    self.transformer.set_mean('data', np.load(self.mean).mean(1).mean(1))
    self.transformer.set_raw_scale('data', 255) 
    self.transformer.set_channel_swap('data', (2,1,0))
    
  def predict(self, image):
    array = np.fromstring(image, dtype='uint8')
    im = cv2.imdecode(array,1)
    im = im / 255.
    im = im[:,:,(2,1,0)]
    self.net.blobs['data'].data[...] = self.transformer.preprocess('data', im)
    self.net.forward()
    output_prob = self.net.blobs['prob'].data[0]
    top_inds = output_prob.argsort()[::-1][:1][0]
    prob = output_prob[top_inds]
    print "%d %f" % (top_inds, output_prob[top_inds])  
    return prob

if __name__ == "__main__":
    img_path = '/raid/yuanyong/magic/magic/1/2101234569_h.jpg'
    with open(img_path,'rb') as infile:
      buf = infile.read()
    EPredor = EmojiPredictModel(0, '/raid/yuanyong/magic/magic_release/models/')
    EPredor.predict(buf)
