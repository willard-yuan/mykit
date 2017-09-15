cmake_minimum_required(VERSION 2.8)
project(logo_dectect_pro)

set(CMAKE_CXX_FLAGS "-std=c++11 -fno-operator-names")

find_package(OpenMP)
if (OPENMP_FOUND)
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

set(OpenCV_DIR /home/yuanyong/opencv3/share/OpenCV)
find_package(OpenCV REQUIRED)

message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

include_directories(${OpenCV_INCLUDE_DIRS})

file(GLOB logo_dectect_pro
    "*.hpp"
    "*.cpp"
)

add_executable(logo_dectect_sift ${logo_dectect_pro})
target_link_libraries (logo_dectect_sift ${OpenCV_LIBS})
