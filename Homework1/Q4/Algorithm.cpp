//
// Created by Haocong Wang on 2/3/20.
//

#include "Algorithm.h"

Algorithm::Algorithm() {}

Algorithm::~Algorithm() {}

void Algorithm::findMostDifference(vector<double> data) {
    double Max = DBL_MIN;
    double Min = DBL_MAX;
    Timer timer;
    for (double i : data) {
        if (i > Max) {
            Max = i;
        }
        if (i < Min) {
            Min = i;
        }
    }
    double res = Max - Min;
    double runTime = timer.Counter();
    cout << "The max absolute difference is " << res << endl;
    cout << "The cost of this program is " << runTime << " ms" << endl;
    cout << "The pair for this result is " << Max << "," << Min << endl;
}