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
    //This requires that the data files are in the cmake-build-debug folder
    //Or you can choose absolute path, like"/Users/.../Documents/.../8int.txt"
    vector<string> fileList = {"8int.txt", "32int.txt", "128int.txt", "512int.txt",
                               "1042int.txt", "4096int.txt", "4192int.txt", "8192int.txt"};
    //vector<string> fileList = {"/Users/.../Documents/.../8int.txt"};
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
    }
    Algorithm algo;
    for (int i = 0; i < dataList.size(); i++) {
        algo.naive3Sum(dataList[i]);
        algo.sophi3Sum(dataList[i]);
    }
    return 0;
}