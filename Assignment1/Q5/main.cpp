//
// Created by Haocong Wang on 2/3/20.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include "Algorithm.h"

using namespace std;

int main() {
    //Use this 2-D dimensional vector as the result
    vector<vector<int>> dataList;
    //Use this vector to initialize one data container
    vector<int> data;
    ifstream ifs;
    string line;
    int dataBit;

    vector<string> fileList = {"8int.txt", "32int.txt", "128int.txt", "512int.txt",
                            "1024int.txt", "4096int.txt", "4192int.txt", "8192int.txt"};

    for (int i = 0; i < fileList.size(); i++) {
        ifs.open(fileList[i], ios_base::in);
        //Check if there is any error when opening files
        if (!ifs.is_open() || ifs.fail()) {
            cout << "Error! Cannot open this file!" << endl;
        } else {
            //Get all data in the file
            while (getline(ifs, line)) {
                dataBit = stoi(line);
                data.push_back(dataBit);
            }
            dataList.push_back(data);
            ifs.close();
        }
        data.clear();
    }
    Algorithm algo;
    for (int i = 0; i < dataList.size(); i++) {
        algo.fastest3Sum(dataList[i]);
    }
    return 0;
}
