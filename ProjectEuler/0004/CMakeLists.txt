cmake_minimum_required(VERSION 3.5)
project(0004)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main2.cpp)
add_executable(0004 ${SOURCE_FILES})