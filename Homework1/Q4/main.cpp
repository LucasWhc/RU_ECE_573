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
    string preFileName = "/Users/lucifer.w/Documents/573/Homework1/DataSet/hw1-1.data/";
    string postFileName = "int.txt";
    vector<int> fileList = {8, 32, 128, 512, 1024, 4096, 4192, 8192};

    for (int i = 0; i < fileList.size(); i++) {
        string file = to_string(fileList[i]) + postFileName;
        string fileName = preFileName + file;
        ifs.open(fileName, ios_base::in);

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
