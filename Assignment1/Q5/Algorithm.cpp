//
// Created by Haocong Wang on 2/3/20.
//

#include "Algorithm.h"

Algorithm::Algorithm() {}

Algorithm::~Algorithm() {}

void Algorithm::fastest3Sum(vector<int> data) {
    vector<vector<int>> res;
    sort(data.begin(), data.end());
    Timer timer;

    for (int i = 0; i < data.size(); i++) {
        if (i > 0 && data[i] == data[i - 1]) {
            continue;
        }

        int target = 0 - data[i];
        int j = i + 1, k = data.size() - 1;

        while (j < k) {
            if (data[j] + data[k] == target) {
                res.push_back({data[i], data[j], data[k]});
                while (j < k && data[j] == data[j + 1]) ++j;
                while (j < k && data[k] == data[k - 1]) --k;
                ++j;
                --k;
            } else if (data[j] + data[k] < target) {
                j++;
            } else {
                k--;
            }
        }
    }

    double runTime = timer.Counter();
    cout << "The run time cost is " << runTime << " ms." << endl;
    for (int i = 0; i < res.size(); i++) {
        cout << "The result pairs are " << res[i][0] << " ," << res[i][1] << " ," << res[i][2] << " ." << endl;
    }
}