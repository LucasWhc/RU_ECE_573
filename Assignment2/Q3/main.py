import os
import time
import merge_sort

# The way I read files from a folder is learned from this website: https://blog.csdn.net/LZGS_4/article/details/50371030
dir_data = os.listdir("/Users/lucifer.w/Documents/573/Assignment2/DataSet")
os.chdir("/Users/lucifer.w/Documents/573/Assignment2/DataSet")

for file in dir_data:
    datalist1 = []
    datalist2 = []
    print(file)
    f = open(file, "r")
    f_line = f.readlines()
    for line in f_line:
        datalist1.append(line.strip())
        datalist2.append(line.strip())
    datalist1 = list(map(int, datalist1))
    datalist2 = list(map(int, datalist2))

    start_time1 = time.time()
    final_list1, result1 = merge_sort.merge_sort(datalist1)
    spent_time1 = time.time() - start_time1
    print("In merge sort, the number of comparision is", result1, "and the runtime cost is", spent_time1)

    start_time2 = time.time()
    final_list2, result2 = merge_sort.bottomup_merge(datalist2)
    spent_time2 = time.time() - start_time2
    print("In bottom-up merge sort, the number of comparision is ", result2, " and the runtime cost is ", spent_time2)
