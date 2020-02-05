//
// Created by Haocong Wang on 2/2/20.
//

#include "quickUnion.h"

quickUnion::quickUnion(int N) {
    id = new int[N];
    for (int i = 0; i < N; i++)  //set id each object to itself
    {
        id[i] = i;
    }
}

quickUnion::~quickUnion() {
    delete[] id;
}

int quickUnion::Root(int i) {
    while (i != id[i]) {
        i = id[i];
    }
    return i;
}

bool quickUnion::Connected(int p, int q) {
    return Root(p) == Root(q);
}

void quickUnion::Union(int p, int q) {
    int i = Root(p);
    int j = Root(q);
    id[i] = j;
}