//
// Created by Haocong Wang on 2/2/20.
//

#include "quickFind.h"

quickFind::quickFind(int N) {
    length = N;
    id = new int[N];
    for (int i = 0; i < N; i++)  //set id each object to itself
    {
        id[i] = i;
    }
}

quickFind::~quickFind() {
    delete[] id;
}

bool quickFind::Connected(int p, int q) {
    return id[p] == id[q];
}

void quickFind::Union(int p, int q) {
    int pID = id[p];
    int qID = id[q];
    for (int i = 0; i < length; i++) {
        if (id[i] == pID) {
            id[i] = qID;
        }
    }
}