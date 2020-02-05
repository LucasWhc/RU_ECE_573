//
// Created by Haocong Wang on 2/2/20.
//

#include "Timer.h"
#include "quickFind.h"
#include "quickUnion.h"
#include "weightedQuickUnion.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>

int main() {
    vector<vector<int> > dataList;
    vector<int> dataP;
    vector<int> dataQ;ifstream ifs;
    string line;
    int dataBitP;
    int dataBitQ;
    vector<string> fileList = {"8pair.txt", "32pair.txt", "128pair.txt", "512pair.txt",
                               "1024pair.txt", "4096pair.txt", "8192pair.txt"};

    for (int i = 0; i < fileList.size(); i++) {
        ifs.open(fileList[i], ios_base::in);
        if (!ifs.is_open() || ifs.fail()) {
            cout << "Error! Cannot open this file!" << endl;
        } else {
            while (getline(ifs, line)) {
                stringstream ss(line);
                string pStr, qStr;
                getline(ss, pStr, ' ');
                getline(ss, qStr);
                dataBitP = stoi(pStr);   //change the data format from string to integer
                dataBitQ = stoi(qStr);
                dataP.push_back(dataBitP);
                dataQ.push_back(dataBitQ);
            }
            dataList.push_back(dataP);
            dataList.push_back(dataQ);
            ifs.close();
        }
    }

    for (int i = 0; i < fileList.size(); i++) {
        vector<int> p = dataList[i * 2];
        vector<int> q = dataList[i * 2 + 1];
        int N = stoi(fileList[i]);

        //quickFind
        quickFind Find(N);
        Timer timer1;
        for (int j = 0; j < N; j++) {
            if (!Find.Connected(p[j], q[j])) {
                Find.Union(p[j], q[j]);
            }
        }
        double runTime1 = timer1.Counter();
        cout << "The run time cost of quick find is " << runTime1 << " ms." << endl;

        //quickUnion
        quickUnion Union(N);
        Timer timer2;
        for (int j = 0; j < N; j++) {
            if (!Union.Connected(p[j], q[j])) {
                Union.Union(p[j], q[j]);
            }
        }
        double runTime2 = timer2.Counter();
        cout << "The run time cost of quick union is " << runTime2 << " ms." << endl;

        //weightedQuickUnion
        weightedQuickUnion weightedUnion(N);
        Timer timer3;
        for(int j = 0; j < N; j++) {
            if (!weightedUnion.Connected(p[j], q[j])) {
                weightedUnion.Union(p[j], q[j]);
            }
        }
        double runTime3 = timer3.Counter();
        cout << "The run time cost of weighted quick union is " << runTime3 << " ms." << endl;
    }
    return 0;
}
