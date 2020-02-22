def insertionsort(datalist):
    len_data = len(datalist)
    cnt = 0
    for i in range(1, len_data):
        for j in range(i, 0, -1):
            cnt += 1
            if datalist[j] < datalist[j - 1]:
                datalist[j], datalist[j - 1] = datalist[j - 1], datalist[j]
            else:
                break
    print("The amount of comparison with insertion sort is ", cnt)
