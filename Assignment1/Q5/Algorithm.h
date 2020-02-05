//
// Created by Haocong Wang on 2/3/20.
//

#ifndef Q5_ALGORITHM_H
#define Q5_ALGORITHM_H

#include "Timer.h"
#include <iostream>
#include <vector>

using namespace std;

class Algorithm {
public:
    Algorithm();

    virtual ~Algorithm();

    void fastest3Sum(vector<int> data);
};


#endif //Q5_ALGORITHM_H
