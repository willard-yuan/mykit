# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples


# anaconda2
export PATH="/home/yuanyong/anaconda2/bin:$PATH"

# swig
export SWIG_HOME=/home/yuanyong/lib/swig
export PATH=$FFMPEG_HOME/bin:$PATH

# OpenCV2
export OPENV_HOME=/home/yuanyong/local
export PATH=$OPENV_HOME/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$OPENV_HOME/lib
#export PYTHONPATH=$PYTHONPATH:/home/lvyue/lib/opencv/lib/python2.7/site-packages

#OpenCV3
export OPENV_HOME=/home/yuanyong/opencv3
export PATH=$OPENV_HOME/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$OPENV_HOME/lib
#export PYTHONPATH=$PYTHONPATH:/home/lvyue/lib/opencv/lib/python2.7/site-packages

# cuda 8.0
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH

# cuda 7.5
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/yuanyong/lib/cuda-7.5/lib64:$LD_LIBRARY_PATH

# ffmpeg
export FFMPEG_HOME=/home/yuanyong/lib/ffmpeg
export PATH=$FFMPEG_HOME/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$FFMPEG_HOME/lib:/usr/local/lib

# imageMagick
export MAGICK_HOME=/home/yuanyong/lib/imageMagick
export PATH=$MAGICK_HOME/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MAGICK_HOME/lib:/usr/local/lib

# openblas
export CPLUS_INCLUDE_PATH=/opt/OpenBLAS/include:$CPLUS_INCLUDE_PATH
export LD_LIBRARY_PATH=/opt/OpenBLAS/lib:$LD_LIBRARY_PATH

# python module
export PYTHONPATH=/home/yuanyong/caffe/python:$PYTHONPATH
export PYTHONPATH=/home/yuanyong/py/yael:$PYTHONPATH
export PYTHONPATH=/home/yuanyong/cpp/KMeansRex/python/KMeansRex:$PYTHONPATH

# cudnn
export C_INCLUDE_PATH=/home/yuanyong/lib/cudnn/include:$C_INCLUDE_PATH
export CPLUS_INCLUDE_PATH=/home/yuanyong/lib/cudnn/include:$CPLUS_INCLUDE_PATH
export LD_LIBRARY_PATH=/home/yuanyong/lib/cudnn/lib64:$LD_LIBRARY_PATH

#export PYTHONPATH="$PYTHONPATH:/home/yuanyong/local/lib/python2.7/site-packages"
export PYTHONPATH="$PYTHONPATH:/home/yuanyong/anaconda2/lib/python2.7/site-packages"

# faiss
export PYTHONPATH=$PYTHONPATH:/raid/yuanyong/faiss

# torch
. /home/yuanyong/torch/install/bin/torch-activate

# libevent
export LD_LIBRARY_PATH=/home/yuanyong/lib/libevent/lib:$LD_LIBRARY_PATH

# tmux
export PATH=/home/yuanyong/lib/tmux/bin:$PATH

# openssl
export LD_LIBRARY_PATH=/home/yuanyong/lib/openssl/lib:$LD_LIBRARY_PATH

# bzip2
export BZIP_HOME=/home/yuanyong/lib/bzip
export PATH=$BZIP_HOME/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$BZIP_HOME/lib:/usr/local/lib
