import os
import time
import mergesort

# The way I read files from a folder is learned from this website: https://blog.csdn.net/LZGS_4/article/details/50371030
dir_data = os.listdir("/Users/lucifer.w/Documents/573/Assignment2/DataSet")
os.chdir("/Users/lucifer.w/Documents/573/Assignment2/DataSet")

for file in dir_data:
    datalist = []
    print(file)
    f = open(file, "r")
    f_line = f.readlines()
    for line in f_line:
        datalist.append(line.strip())
    datalist = list(map(int, datalist))
    start_time = time.time()
    final_list, cnt = mergesort.merge_sort(datalist)
    spent_time = time.time() - start_time
    print("The runtime is", spent_time, "and the distance is", cnt)
