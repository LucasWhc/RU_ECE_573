//
// Created by Haocong Wang on 2/2/20.
//

#include "weightedQuickUnion.h"

weightedQuickUnion::weightedQuickUnion(int N) {
    id = new int[N];
    sz = new int[N];
    for (int i = 0; i < N; i++)  //set id each object to itself
    {
        id[i] = i;
        sz[i] = 1;
    }
}

weightedQuickUnion::~weightedQuickUnion() {
    delete[] id;
    delete[] sz;
}

int weightedQuickUnion::Root(int i) {
    while (i != id[i]) {
        i = id[i];
    }
    return i;
}

bool weightedQuickUnion::Connected(int p, int q) {
    return Root(p) == Root(q);
}

void weightedQuickUnion::Union(int p, int q) {
    int i = Root(p);
    int j = Root(q);
    if (sz[i] < sz[j]) {
        id[i] = j;
        sz[j] += sz[i];
    } else {
        id[j] = i;
        sz[i] += sz[j];
    }
}