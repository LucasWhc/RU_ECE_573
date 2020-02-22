import time
import merge_sort
import bubble_sort
import insertion_sort

file = "/Users/lucifer.w/Documents/573/Assignment2/Q4/data.txt"
with open(file, 'w') as f:
    for i in range(0, 1024):
        f.write("1\n")
    for i in range(0, 2048):
        f.write("11\n")
    for i in range(0, 4096):
        f.write("111\n")
    for i in range(0, 1024):
        f.write("1111\n")

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
merge_sort.merge_sort(datalist1)
spent_time1 = time.time() - start_time1
print("The runtime cost of merge sort is", spent_time1)

start_time2 = time.time()
bubble_sort.bubble_sort(datalist2)
spent_time2 = time.time() - start_time2
print("The runtime cost of bubble sort is", spent_time2)

start_time3 = time.time()
insertion_sort.insertionsort(datalist3)
spent_time3 = time.time() - start_time3
print("The runtime cost of insertion sort is", spent_time3)
