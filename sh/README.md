1. switch_opencv_version.sh 在OpenCV2.x和OpenCV3.0之间进行切换。
2. look_up_cpu_information_in_osx.h  OS X下查看硬件信息


### 有用博文
1. [Compiling GCC 5 on OS X](https://solarianprogrammer.com/2015/05/01/compiling-gcc-5-mac-os-x/)  OS X下openMP的解决方案。"xcode-select --install"记得在安装前安装。编译成功后，在`.zshrc`中添加export PATH=“/usr/gcc-5.1.0/bin:$PATH”，`source ./zshrc`后即可调用gcc了，不过需要注意是，在使用gcc的时候，一定要加上版本后缀，即用gcc编译的时候，一定是`g++-5.2.0 xxx`，如果直接用`g++ xxx`，使用的是clang，这一点非常的重要。
