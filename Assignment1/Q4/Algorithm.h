//
// Created by 王皓聪 on 2/3/20.
//

#ifndef Q4_ALGORITHM_H
#define Q4_ALGORITHM_H

#include "Timer.h"
#include <iostream>
#include <vector>
#include <float.h>

using namespace std;

class Algorithm {
public:
    Algorithm();

    virtual ~Algorithm();

    void findMostDifference(vector<double> data);
};


#endif //Q4_ALGORITHM_H
