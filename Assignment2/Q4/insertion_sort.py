def insertionsort(datalist):
    len_data = len(datalist)
    for i in range(1, len_data):
        for j in range(i, 0, -1):
            if datalist[j] < datalist[j - 1]:
                datalist[j], datalist[j - 1] = datalist[j - 1], datalist[j]
            else:
                break
