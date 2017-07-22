
/raid/caffe/tools/caffe train -solver solver_vgg16.prototxt -weights /home/yuanyong/models/vgg.model -gpu all 2>&1 | tee log.txt
