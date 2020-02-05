//
// Created by Haocong Wang on 2/2/20.
//

#ifndef Q2_QUICKFIND_H
#define Q2_QUICKFIND_H


#include <iostream>

using namespace std;

class quickFind {
public:
    //Some codes are original from the course slides
    quickFind(int N);

    virtual ~quickFind();

    bool Connected(int p, int q);

    void Union(int p, int q);

private:
    int length;
    int *id;
};


#endif //Q2_QUICKFIND_H
