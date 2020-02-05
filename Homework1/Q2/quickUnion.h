//
// Created by Haocong Wang on 2/2/20.
//

#ifndef Q2_QUICKUNION_H
#define Q2_QUICKUNION_H


#include <iostream>

using namespace std;

class quickUnion {
public:
    //Some codes are original from the course slides
    quickUnion(int N, int Max);

    virtual ~quickUnion();

    bool Connected(int p, int q);

    void Union(int p, int q);

private:
    int Root(int i);

    int *id;
};


#endif //Q2_QUICKUNION_H
