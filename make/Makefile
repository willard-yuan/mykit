CFLAGS = -std=c++11

#SRCS =      helloOpenCV.cpp

LIBS =  -lopencv_core -lopencv_imgproc -lopencv_calib3d -lopencv_video -lopencv_features2d -lopencv_ml -lopencv_highgui -lopencv_objdetect -lopencv_contrib -lopencv_legacy -lopencv_gpu

#INCPATH = -I/usr/local/Cellar/opencv/2.4.11_1/include
#LIBPATH = -L/usr/local/Cellar/opencv/2.4.11_1/lib

INCPATH = -I/usr/local/include
LIBPATH = -L/usr/local/lib

#TARGET =    helloOpenCV

#$(TARGET):    $(SRCS)
#	g++ $(CFLAGS) $(INCPATH) $(LIBPATH) -o $(TARGET) $(SRCS) $(LIBS) 
#all:    $(TARGET)

#clean:
#	rm -f $(TARGET)

#######################################
# Scheme Two:

LIBS =  -lopencv_core -lopencv_imgproc -lopencv_calib3d -lopencv_video -lopencv_features2d -lopencv_ml -lopencv_highgui -lopencv_objdetect -lopencv_contrib -lopencv_legacy -lopencv_gpu

#INCPATH = -I/usr/local/Cellar/opencv/2.4.11_1/include
#LIBPATH = -L/usr/local/Cellar/opencv/2.4.11_1/lib

INCPATH = -I/usr/local/include
LIBPATH = -L/usr/local/lib

all:    helloOpenCV helloWorld
helloOpenCV:    helloOpenCV.cpp
	g++ $(CFLAGS) $(INCPATH) $(LIBPATH) -o helloOpenCV helloOpenCV.cpp $(LIBS)
helloWorld:    helloWorld.cpp
	g++ $(CFLAGS) $(INCPATH) $(LIBPATH) -o helloWorld helloWorld.cpp $(LIBS)

clean:
	rm -f helloOpenCV helloWorld