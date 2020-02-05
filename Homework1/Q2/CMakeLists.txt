cmake_minimum_required(VERSION 3.15)
project(Q2)

set(CMAKE_CXX_STANDARD 14)

add_executable(Q2 main.cpp Timer.cpp Timer.h quickFind.cpp quickFind.h quickUnion.cpp quickUnion.h weightedQuickUnion.cpp weightedQuickUnion.h)