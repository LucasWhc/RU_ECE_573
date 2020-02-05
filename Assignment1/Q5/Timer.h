//
// Created by Haocong Wang on 2/3/20.
//

#ifndef Q5_TIMER_H
#define Q5_TIMER_H

#include "time.h"

class Timer {
public:
    Timer();

    virtual ~Timer();

    double Counter();

private:
    clock_t t1, t2;
};


#endif //Q5_TIMER_H
