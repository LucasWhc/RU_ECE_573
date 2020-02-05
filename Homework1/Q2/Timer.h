//
// Created by Haocong Wang on 2/2/20.
//

#ifndef Q2_TIMER_H
#define Q2_TIMER_H

#include <time.h>

class Timer {
public:
    Timer();

    virtual ~Timer();

    double Counter();

private:
    clock_t start, end;
};


#endif //Q2_TIMER_H
