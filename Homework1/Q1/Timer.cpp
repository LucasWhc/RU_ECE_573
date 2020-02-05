//
// Created by Haocong Wang on 2/2/20.
//

#include "Timer.h"

Timer::Timer() {
    start = clock();
}

Timer::~Timer() {}

double Timer::Counter() {
    end = clock();
    double time = end - start;
    //Count the running time in millisecond
    return time / CLOCKS_PER_SEC * 1000;
}