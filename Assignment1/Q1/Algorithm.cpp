//
// Created by Haocong Wang on 2/2/20.
//

#include "Algorithm.h"

Algorithm::Algorithm() {}

Algorithm::~Algorithm() {}

void Algorithm::naive3Sum(vector<int> data) {
    Timer time;
    int count = 0;
    for (int i = 0; i < data.size(); i++) {
        for (int j = i + 1; j < data.size(); j++) {
            for (int k = j + 1; k < data.size(); k++) {
                if (data[i] + data[j] + data[k] == 0) {
                    count++;
                }
            }

        }
    }
    double runTime = time.Counter();
    cout << "The run time cost of the program is " << runTime << " ms." << endl;
    cout << "There are " << count << " 3-sum." << endl;
}

void Algorithm::sophi3Sum(vector<int> data) {
    Timer time;
    int count = 0;
    //The sophisticated 3-sum requires sorting
    sort(data.begin(), data.end());
    for (int i = 0; i < data.size(); i++) {
        for (int j = i + 1; j < data.size(); j++) {
            if (binary_search(data.begin() + j + 1, data.end(), -(data[i] + data[j]))) {
                count++;
            }
        }
    }
    double runTime = time.Counter();
    cout << "The run time cost of the program is " << runTime << " ms." << endl;
    cout << "There are " << count << " 3-sum." << endl;
}