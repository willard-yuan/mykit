
/raid/caffe/tools/caffe train -solver solver.prototxt -weights /home/yuanyong/models/ResNet-101-model.caffemodel -gpu 0,1,2,3,4,5,6 2>&1 | tee log.txt
