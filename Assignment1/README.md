1. For every question, I used the following code to read the data from a certain file:
```cpp
    vector<string> fileList = {"8int.txt", "32int.txt", "128int.txt", "512int.txt",
    "1042int.txt", "4096int.txt", "4192int.txt", "8192int.txt"};
```
If you want to test it with another dataset, please change the fileList, but please make sure they are in the cmkae-build-debug folder. Or you can choose absolute path, like"/Users/.../Documents/.../8int.txt".
If there is something when opening the file, please change the fileList into a one element vector, like \{8\} or \{32\}.\
2. For question 1 and question 2, part of my codes are original from the java codes provided in the course slides. I wrote the cpp codes based on those.\
3. I used online MATLAB to plot all the curve fitting figures. To do that, I first uploaded a text file to input the data into a variable. Then I took advantage of the cftool to help finishing curve fitting.}
