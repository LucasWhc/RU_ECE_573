//
// Created by Haocong Wang on 2/2/20.
//

#ifndef Q2_WEIGHTEDQUICKUNION_H
#define Q2_WEIGHTEDQUICKUNION_H


#include <iostream>

using namespace std;

class weightedQuickUnion {
public:
    //Some codes are original from the course slides
    weightedQuickUnion(int N);

    virtual ~weightedQuickUnion();

    bool Connected(int p, int q);

    void Union(int p, int q);

private:
    int Root(int i);

    int *id, *sz;
};


#endif //Q2_WEIGHTEDQUICKUNION_H
