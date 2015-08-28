# my-utils

在编码过程中积累下来的有用的脚本文件

1. OpenCV在安装过程中出现跟`avcodec_encode_video`这类字眼的错误，可能跟ffmpeg有关，需要在编译OpenCV之前安装ffmpeg：
```text
For installing ffmpeg you should download its sources from official site or clone GIT repository (git://source.ffmpeg.org/ffmpeg.git), then enter source directory and run

./configure --enable-shared --disable-static
make
sudo make install
```
具体可以参考[Installing OpenCV in Ubuntu 14.10](http://stackoverflow.com/questions/26592577/installing-opencv-in-ubuntu-14-10/27020828#27020828)，在CentOS上安装好ffmpeg后重新编译OpenCV后成功。

2. 在CentOS上[How to Install gcc 4.7.x/4.8.x on CentOS](http://superuser.com/questions/381160/how-to-install-gcc-4-7-x-4-8-x-on-centos)，可以采用：
```text
[DevToolset-2]
name=RedHat DevToolset v2 $releasever - $basearch
baseurl=http://people.centos.org/tru/devtools-2/$basearch/
enabled=1
gpgcheck=0
Testing run

# yum install devtoolset-2-gcc-4.8.2 devtoolset-2-gcc-c++-4.8.2
# /opt/rh/devtoolset-2/root/usr/bin/gcc --version
export

ln -s /opt/rh/devtoolset-2/root/usr/bin/* /usr/local/bin/
hash -r
gcc --version
```
在CentOS上成功安装g++4.8.x，注意4.7.x不支持c++11语法。
