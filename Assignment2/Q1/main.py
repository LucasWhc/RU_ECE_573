import os
import shellsort
import insertionsort
import time

# The way I read files from a folder is learned from this website: https://blog.csdn.net/LZGS_4/article/details/50371030
dir_data = os.listdir("/Users/lucifer.w/Documents/573/Assignment2/DataSet")
os.chdir("/Users/lucifer.w/Documents/573/Assignment2/DataSet")
h_list = [7, 3, 1]

for file in dir_data:
    datalist1 = []
    # For insertion sort, you can also change the h_list to [1], then the shell sort will become insertion sort
    datalist2 = []
    print(file)  # Display the file that we are currently processing
    f = open(file, "r")
    f_line = f.readlines()
    for line in f_line:
        datalist1.append(line.strip())
        datalist2.append(line.strip())
    datalist1 = list(map(int, datalist1))
    datalist2 = list(map(int, datalist2))

    start_time1 = time.time()
    shellsort.shellsort(datalist1, h_list)
    spent_time1 = time.time() - start_time1
    print("The runtime cost is", spent_time1)

    start_time2 = time.time()
    insertionsort.insertionsort(datalist2)
    spent_time2 = time.time() - start_time2
    print("The runtime cost is", spent_time2)
