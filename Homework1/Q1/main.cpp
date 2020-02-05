//
// Created by Haocong Wang on 2/2/20.
//

#include "Algorithm.h"
#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main() {
    //Use this 2-D dimensional vector as the result
    vector<vector<int>> dataList;
    //Use this vector to initialize one data container
    vector<int> data;
    ifstream ifs;
    string line;
    int dataBit;
    //This string can be changed according to the location where the user stores the file
    string preFileName = "/Users/lucifer.w/Documents/573/Homework1/DataSet/hw1-1.data/";
    string postFileName = "int.txt";
    vector<int> fileList = {8, 32, 128, 512, 1042, 4096, 4192, 8192};

    for (int i = 0; i < fileList.size(); i++) {
        string file = to_string(fileList[i]) + postFileName;
        string fileName = preFileName + file;
        ifs.open(fileName, ios_base::in);

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
    }
    Algorithm algo;
    for (int i = 0; i < dataList.size(); i++) {
        algo.naive3Sum(dataList[i]);
        algo.sophi3Sum(dataList[i]);
    }
    return 0;
}