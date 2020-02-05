//
// Created by Haocong Wang on 2/3/20.
//

#include "Timer.h"

Timer::Timer() {
    start = clock();
}

Timer::~Timer() {}

double Timer::Counter() {
    end = clock();
    double time = end - start;
    return time / CLOCKS_PER_SEC * 1000;
}