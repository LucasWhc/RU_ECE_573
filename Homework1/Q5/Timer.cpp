//
// Created by Haocong Wang on 2/3/20.
//

#include "Timer.h"

Timer::Timer() {
    t1 = clock();
}

Timer::~Timer() {}

double Timer::Counter() {
    t2 = clock();
    double time = t2 - t1;
    return time / CLOCKS_PER_SEC * 1000;
}