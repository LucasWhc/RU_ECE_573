//
// Created by Haocong Wang on 2/2/20.
//

#ifndef Q1_ALGORITHM_H
#define Q1_ALGORITHM_H

#include "Timer.h"
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

class Algorithm {
public:
    Algorithm();

    virtual ~Algorithm();

    //Some codes are original from the course slides
    void naive3Sum(vector<int> data);

    void sophi3Sum(vector<int> data);
};


#endif //Q1_ALGORITHM_H
