//
// Created by Haocong Wang on 2/2/20.
//

#ifndef Q1_TIMER_H
#define Q1_TIMER_H

#include <time.h>

class Timer {
public:
    Timer();

    virtual ~Timer();

    double Counter();

private:
    clock_t t1, t2;
};


#endif //Q1_TIMER_H
