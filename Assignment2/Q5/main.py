import os
import time
import merge_sort
import quick_sort

# The way I read files from a folder is learned from this website: https://blog.csdn.net/LZGS_4/article/details/50371030
dir_data = os.listdir("/Users/lucifer.w/Documents/573/Assignment2/DataSet")
os.chdir("/Users/lucifer.w/Documents/573/Assignment2/DataSet")
cutoff = 15

for file in dir_data:
    datalist1 = []
    datalist2 = []
    datalist3 = []
    print(file)
    f = open(file, "r")
    f_line = f.readlines()
    for line in f_line:
        datalist1.append(line.strip())
        datalist2.append(line.strip())
        datalist3.append(line.strip())
    datalist1 = list(map(int, datalist1))
    datalist2 = list(map(int, datalist2))
    datalist3 = list(map(int, datalist3))

    start_time1 = time.time()
    final_list1 = merge_sort.merge_sort(datalist1)
    spent_time1 = time.time() - start_time1
    print("The runtime cost of merge sort is", spent_time1)

    start_time2 = time.time()
    quick_sort.quick_sort(datalist2, 0, len(datalist2))
    spent_time2 = time.time() - start_time2
    print("The runtime cost of quick sort is", spent_time2)

    start_time3 = time.time()
    quick_sort.quick_sort_cutoff(datalist3, 0, len(datalist3), cutoff)
    spent_time3 = time.time() - start_time3
    print("The runtime cost of quick sort with cutoff", cutoff, "is", spent_time3)
