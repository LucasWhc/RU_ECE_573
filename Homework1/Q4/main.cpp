//
// Created by Haocong Wang on 2/3/20.
//

#include "Algorithm.h"
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
    vector<vector<double>> dataList;
    vector<double> data;
    ifstream ifs;
    string line;
    double dataBit;
    vector<string> fileList = {"8int.txt", "32int.txt", "128int.txt", "512int.txt",
                            "1042int.txt", "4096int.txt", "4192int.txt", "8192int.txt"};

    for (int i = 0; i < fileList.size(); i++) {
        ifs.open(fileList[i], ios_base::in);

        if (!ifs.is_open() || ifs.fail()) {
            cout << "Error! Cannot open this file!" << endl;
        } else {
            while (getline(ifs, line)) {
                dataBit = stod(line);
                data.push_back(dataBit);
            }
            dataList.push_back(data);
            ifs.close();
        }
    }
    Algorithm algo;
    for (int i = 0; i < dataList.size(); i++) {
        algo.findMostDifference(dataList[i]);
    }
    return 0;
}
